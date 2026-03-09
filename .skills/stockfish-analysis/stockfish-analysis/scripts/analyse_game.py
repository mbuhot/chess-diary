#!/usr/bin/env python3
"""
Analyse a chess game with Stockfish and produce annotated PGN.

Two-pass approach (inspired by chesscli):
  Pass 1: MultiPV 1 at target depth for all positions → fast classification
  Pass 2: MultiPV N only for inaccuracies/mistakes/blunders → get alternative lines

Usage:
  python analyse_game.py --pgn game.pgn --depth 18 --format annotated_pgn
  python analyse_game.py --pgn game.pgn --depth 20 --format json
  python analyse_game.py --pgn game.pgn --depth 18 --format both --output analysis

Options:
  --pgn FILE        Path to PGN file (required)
  --depth N         Stockfish search depth (default: 18)
  --threads N       Stockfish threads (default: 4)
  --hash N          Stockfish hash table MB (default: 256)
  --multipv N       Number of alternative lines for mistakes (default: 3)
  --pv-depth N      Moves deep for each variation line (default: 5)
  --stockfish PATH  Path to stockfish binary (default: /opt/homebrew/bin/stockfish)
  --format FMT      Output format: annotated_pgn, json, both (default: annotated_pgn)
  --output PATH     Output file path without extension (default: stdout for pgn, analysis.json for json)
  --player COLOR    Which side to annotate: white, black, both (default: both)
"""

import argparse
import json
import sys
import chess
import chess.pgn
import chess.engine


# Move classification thresholds (centipawn loss).
# "miss" is a special category: moderate loss (50-100cp) in a winning position (>=150cp).
# This matches the chesscli classification system.
THRESHOLDS = {
    "best": 0,
    "excellent": 10,
    "good": 25,
    "inaccuracy": 50,
    "miss": 100,       # 50-100cp loss in winning position
    "mistake": 150,
    "blunder": float("inf"),
}

# NAG (Numeric Annotation Glyph) codes for PGN
NAGS = {
    "best": chess.pgn.NAG_GOOD_MOVE,         # $1 !
    "excellent": chess.pgn.NAG_GOOD_MOVE,     # $1 !
    "inaccuracy": chess.pgn.NAG_DUBIOUS_MOVE, # $6 ?!
    "miss": chess.pgn.NAG_DUBIOUS_MOVE,       # $6 ?!
    "mistake": chess.pgn.NAG_MISTAKE,         # $2 ?
    "blunder": chess.pgn.NAG_BLUNDER,         # $4 ??
}

# Categories that warrant alternative lines in annotated PGN
ANNOTATE_CATEGORIES = {"inaccuracy", "miss", "mistake", "blunder"}


def classify_move(cp_loss, played_best, mover_eval_before):
    """Classify a move based on centipawn loss.

    The 'miss' category (from chesscli) captures moderate losses in winning
    positions: you had a significant advantage and let some of it slip.
    """
    if played_best:
        return "best"
    if cp_loss <= THRESHOLDS["excellent"]:
        return "excellent"
    if cp_loss <= THRESHOLDS["good"]:
        return "good"
    if cp_loss <= THRESHOLDS["inaccuracy"]:
        return "inaccuracy"
    # Miss: 50-100cp loss when already winning (>=150cp advantage)
    if cp_loss <= THRESHOLDS["miss"] and abs(mover_eval_before) >= 150:
        return "miss"
    if cp_loss <= THRESHOLDS["mistake"]:
        return "mistake"
    return "blunder"


def format_eval(score_cp):
    """Format centipawn score as human-readable string."""
    if abs(score_cp) >= 9000:
        mate_in = (10000 - abs(score_cp))
        sign = "+" if score_cp > 0 else "-"
        return f"{sign}M{mate_in}"
    return f"{score_cp / 100:+.1f}"


def analyse_game(pgn_path, depth, threads, hash_mb, multipv, pv_depth, stockfish_path, player_filter):
    """Run Stockfish analysis using a two-pass approach.

    Pass 1: MultiPV 1 at target depth for all positions (fast eval + best move).
    Pass 2: MultiPV N only for positions classified as inaccuracy/miss/mistake/blunder
            (get alternative lines for annotation).
    """
    with open(pgn_path) as f:
        game = chess.pgn.read_game(f)

    if game is None:
        print("Error: Could not parse PGN file", file=sys.stderr)
        sys.exit(1)

    board = game.board()
    moves = list(game.mainline_moves())
    total = len(moves)

    engine = chess.engine.SimpleEngine.popen_uci(stockfish_path)
    engine.configure({"Threads": threads, "Hash": hash_mb})

    # === Pass 1: Fast eval with MultiPV 1 ===
    sys.stderr.write(f"Pass 1/{total}: evaluating all positions (depth {depth}, multipv 1)...\n")
    positions = []
    for i, move in enumerate(moves):
        result = engine.analyse(board, chess.engine.Limit(depth=depth), multipv=1)

        best_move = result[0]["pv"][0]
        best_score = result[0]["score"].white().score(mate_score=10000)

        # Store the single best PV line
        pv_san = []
        temp = board.copy()
        for pv_move in result[0]["pv"][:pv_depth]:
            pv_san.append(temp.san(pv_move))
            temp.push(pv_move)

        positions.append({
            "ply": i + 1,
            "move_num": (i // 2) + 1,
            "is_white": (i % 2 == 0),
            "move_san": board.san(move),
            "move_uci": move.uci(),
            "fen_before": board.fen(),
            "eval_before": best_score,
            "best_move": best_move,
            "played_best": (move == best_move),
            "pvs": [{
                "moves": pv_san,
                "score_cp": best_score,
                "first_move": best_move,
                "pv_uci": [m.uci() for m in result[0]["pv"][:pv_depth]],
            }],
        })

        board.push(move)
        sys.stderr.write(f"\r  {i + 1}/{total}")
        sys.stderr.flush()

    # Final position eval
    final_result = engine.analyse(board, chess.engine.Limit(depth=depth), multipv=1)
    final_eval = final_result[0]["score"].white().score(mate_score=10000)
    sys.stderr.write("\n")

    # Classify all moves
    for i, pos in enumerate(positions):
        eval_after = positions[i + 1]["eval_before"] if i + 1 < len(positions) else final_eval

        if pos["is_white"]:
            cp_loss = pos["eval_before"] - eval_after
            mover_eval = pos["eval_before"]
        else:
            cp_loss = eval_after - pos["eval_before"]
            mover_eval = -pos["eval_before"]  # flip for black's perspective

        pos["eval_after"] = eval_after
        pos["cp_loss"] = cp_loss
        pos["category"] = classify_move(cp_loss, pos["played_best"], mover_eval)

    # === Pass 2: MultiPV N only for positions needing alternative lines ===
    needs_multipv = [i for i, pos in enumerate(positions) if pos["category"] in ANNOTATE_CATEGORIES]

    if needs_multipv and multipv > 1:
        sys.stderr.write(f"Pass 2: analysing {len(needs_multipv)} positions with multipv {multipv}...\n")
        for count, idx in enumerate(needs_multipv):
            pos = positions[idx]
            analysis_board = chess.Board(pos["fen_before"])

            result = engine.analyse(analysis_board, chess.engine.Limit(depth=depth), multipv=multipv)

            pvs = []
            for info in result:
                pv_san = []
                temp = analysis_board.copy()
                for pv_move in info["pv"][:pv_depth]:
                    pv_san.append(temp.san(pv_move))
                    temp.push(pv_move)
                pvs.append({
                    "moves": pv_san,
                    "score_cp": info["score"].white().score(mate_score=10000),
                    "first_move": info["pv"][0],
                    "pv_uci": [m.uci() for m in info["pv"][:pv_depth]],
                })

            pos["pvs"] = pvs
            sys.stderr.write(f"\r  {count + 1}/{len(needs_multipv)}")
            sys.stderr.flush()

        sys.stderr.write("\n")

    engine.quit()
    return game, positions


def build_annotated_pgn(game, positions, player_filter):
    """Build an annotated PGN game with comments and variations."""
    annotated = chess.pgn.Game()

    # Copy headers
    for key, value in game.headers.items():
        annotated.headers[key] = value

    board = annotated.board()
    node = annotated

    for pos in positions:
        move = chess.Move.from_uci(pos["move_uci"])
        node = node.add_main_variation(move)

        # Determine if we should annotate this side
        if player_filter == "white" and not pos["is_white"]:
            continue
        if player_filter == "black" and pos["is_white"]:
            continue

        category = pos["category"]

        # Add NAG for non-trivial classifications
        if category in NAGS:
            node.nags.add(NAGS[category])

        # Add eval comment
        after_str = format_eval(pos["eval_after"])

        if category in ANNOTATE_CATEGORIES:
            # Add comment explaining the issue
            node.comment = (
                f"[%eval {after_str}] "
                f"{category.title()} (cp loss: {pos['cp_loss']}). "
                f"Best was {pos['pvs'][0]['moves'][0]}."
            )

            # Add best move as a variation
            parent = node.parent
            if parent is not None:
                best_pv = pos["pvs"][0]
                # board is at position before current move (updated at end of each iteration)
                var_board = board.copy()

                var_node = parent.add_variation(best_pv["first_move"])
                var_node.comment = f"[%eval {format_eval(best_pv['score_cp'])}] Engine's top choice."

                # Add continuation moves
                var_temp = var_board.copy()
                var_temp.push(best_pv["first_move"])
                for san_move in best_pv["moves"][1:]:
                    parsed = var_temp.parse_san(san_move)
                    var_node = var_node.add_main_variation(parsed)
                    var_temp.push(parsed)

                # Add second-best line if available and different
                if len(pos["pvs"]) > 1:
                    alt_pv = pos["pvs"][1]
                    if alt_pv["first_move"] != best_pv["first_move"]:
                        alt_node = parent.add_variation(alt_pv["first_move"])
                        alt_node.comment = f"[%eval {format_eval(alt_pv['score_cp'])}]"

                        alt_temp = var_board.copy()
                        alt_temp.push(alt_pv["first_move"])
                        for san_move in alt_pv["moves"][1:]:
                            parsed = alt_temp.parse_san(san_move)
                            alt_node = alt_node.add_main_variation(parsed)
                            alt_temp.push(parsed)
        elif category == "best":
            node.comment = f"[%eval {after_str}]"

        # Update board to position after current move by replaying mainline
        board = annotated.board()
        for m in node.game().mainline_moves():
            board.push(m)
            if m == move:
                break

    return annotated


def build_json_report(positions):
    """Build a JSON analysis report."""
    moves = []
    cats = {"best": 0, "excellent": 0, "good": 0, "inaccuracy": 0, "miss": 0, "mistake": 0, "blunder": 0}
    white_summary = dict(cats)
    black_summary = dict(cats)
    total_cp_loss_white = 0
    total_cp_loss_black = 0
    white_moves = 0
    black_moves = 0

    for pos in positions:
        cat = pos["category"]
        cats[cat] += 1

        if pos["is_white"]:
            white_summary[cat] += 1
            total_cp_loss_white += max(0, pos["cp_loss"])
            white_moves += 1
        else:
            black_summary[cat] += 1
            total_cp_loss_black += max(0, pos["cp_loss"])
            black_moves += 1

        move_data = {
            "ply": pos["ply"],
            "move_number": pos["move_num"],
            "side": "white" if pos["is_white"] else "black",
            "move": pos["move_san"],
            "category": cat,
            "cp_loss": pos["cp_loss"],
            "eval_before": format_eval(pos["eval_before"]),
            "eval_after": format_eval(pos["eval_after"]),
        }

        if cat in ANNOTATE_CATEGORIES:
            move_data["best_line"] = " ".join(pos["pvs"][0]["moves"])
            move_data["best_eval"] = format_eval(pos["pvs"][0]["score_cp"])
            if len(pos["pvs"]) > 1:
                move_data["alt_line"] = " ".join(pos["pvs"][1]["moves"])
                move_data["alt_eval"] = format_eval(pos["pvs"][1]["score_cp"])

        moves.append(move_data)

    return {
        "summary": {
            "total_moves": len(positions),
            "classifications": cats,
            "white": {
                "classifications": white_summary,
                "avg_cp_loss": round(total_cp_loss_white / white_moves, 1) if white_moves else 0,
            },
            "black": {
                "classifications": black_summary,
                "avg_cp_loss": round(total_cp_loss_black / black_moves, 1) if black_moves else 0,
            },
        },
        "moves": moves,
    }


def main():
    parser = argparse.ArgumentParser(description="Analyse a chess game with Stockfish")
    parser.add_argument("--pgn", required=True, help="Path to PGN file")
    parser.add_argument("--depth", type=int, default=18, help="Search depth (default: 18)")
    parser.add_argument("--threads", type=int, default=4, help="Stockfish threads (default: 4)")
    parser.add_argument("--hash", type=int, default=256, help="Hash table MB (default: 256)")
    parser.add_argument("--multipv", type=int, default=3, help="Number of PV lines for mistakes (default: 3)")
    parser.add_argument("--pv-depth", type=int, default=5, help="Moves per PV line (default: 5)")
    parser.add_argument("--stockfish", default="/opt/homebrew/bin/stockfish", help="Stockfish path")
    parser.add_argument("--format", choices=["annotated_pgn", "json", "both"], default="annotated_pgn")
    parser.add_argument("--output", help="Output file path without extension")
    parser.add_argument("--player", choices=["white", "black", "both"], default="both")
    args = parser.parse_args()

    game, positions = analyse_game(
        args.pgn, args.depth, args.threads, args.hash,
        args.multipv, args.pv_depth, args.stockfish, args.player,
    )

    if args.format in ("annotated_pgn", "both"):
        annotated = build_annotated_pgn(game, positions, args.player)
        if args.output:
            with open(f"{args.output}.pgn", "w") as f:
                print(annotated, file=f)
            print(f"Wrote {args.output}.pgn", file=sys.stderr)
        else:
            print(annotated)

    if args.format in ("json", "both"):
        report = build_json_report(positions)
        if args.output:
            with open(f"{args.output}.json", "w") as f:
                json.dump(report, f, indent=2)
            print(f"Wrote {args.output}.json", file=sys.stderr)
        else:
            print(json.dumps(report, indent=2))


if __name__ == "__main__":
    main()
