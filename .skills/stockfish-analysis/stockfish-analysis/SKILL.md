---
name: stockfish-analysis
description: >
  Analyse a chess game with Stockfish. Use when asked to "analyse this game",
  "find mistakes", "run engine analysis", "annotate the PGN", "what were the
  blunders", "create a Lichess study", or "add variations to the PGN".
  Produces annotated PGN with move classifications and alternative lines.
---

# Stockfish Game Analysis

Analyse chess games using the local Stockfish 18 engine via python-chess. Classifies every move and produces annotated PGN with alternative lines at decision points.

## Dependencies

- **Stockfish 18:** `/opt/homebrew/bin/stockfish`
- **python-chess:** installed in the chess-diagram venv at `.skills/chess-diagram/chess-diagram/.venv/`
- No additional packages needed beyond what the chess-diagram skill already provides.

## How It Works (Two-Pass Approach)

Inspired by the chesscli analysis engine, the script uses a two-pass strategy to balance speed and depth:

1. **Pass 1 (fast):** MultiPV 1 at target depth for ALL positions. This gives the best move and eval for every position, enough to classify all moves.
2. **Classify:** Compute centipawn loss and assign categories to every move.
3. **Pass 2 (targeted):** MultiPV N only for positions classified as inaccuracy/miss/mistake/blunder. These are the positions that need alternative lines for annotation.

This is much faster than running MultiPV 3 on all positions, since typically only 10-20% of moves need alternative lines.

## Move Classification

Thresholds (centipawn loss from the moving player's perspective):

| Category    | CP Loss       | Condition                      | NAG  | Symbol |
|-------------|---------------|--------------------------------|------|--------|
| Best        | 0 (exact)     | Played engine's top choice     | $1   | !      |
| Excellent   | ≤ 10          |                                | —    |        |
| Good        | ≤ 25          |                                | —    |        |
| Inaccuracy  | ≤ 50          |                                | $6   | ?!     |
| Miss        | ≤ 100         | Only in winning positions (≥150cp) | $6   | ?!     |
| Mistake     | ≤ 150         |                                | $2   | ?      |
| Blunder     | > 150         |                                | $4   | ??     |

The "Miss" category (from chesscli) captures a specific pattern: you had a significant advantage and let some of it slip. It's distinct from a plain inaccuracy because the context matters: missing an opportunity when winning is different from making a slightly imprecise move in an equal position.

Evaluations are always from White's perspective internally, then flipped for Black's cp_loss calculation.

## Usage

```bash
VENV=".skills/chess-diagram/chess-diagram/.venv/bin/python3"
SCRIPT=".skills/stockfish-analysis/stockfish-analysis/scripts/analyse_game.py"

# Annotated PGN to stdout
$VENV $SCRIPT --pgn game.pgn --depth 18

# JSON report to file
$VENV $SCRIPT --pgn game.pgn --depth 20 --format json --output analysis

# Both formats to files
$VENV $SCRIPT --pgn game.pgn --depth 18 --format both --output analysis

# Only annotate White's moves
$VENV $SCRIPT --pgn game.pgn --player white
```

## Options

| Flag          | Default                        | Description                                  |
|---------------|--------------------------------|----------------------------------------------|
| `--pgn`       | (required)                     | Path to PGN file                             |
| `--depth`     | 18                             | Stockfish search depth                       |
| `--threads`   | 4                              | Stockfish threads                            |
| `--hash`      | 256                            | Hash table size in MB                        |
| `--multipv`   | 3                              | Number of alternative lines (pass 2 only)    |
| `--pv-depth`  | 5                              | Moves deep for each variation line           |
| `--stockfish` | `/opt/homebrew/bin/stockfish`  | Path to stockfish binary                     |
| `--format`    | `annotated_pgn`                | Output: `annotated_pgn`, `json`, `both`      |
| `--output`    | stdout                         | File path without extension                  |
| `--player`    | `both`                         | Annotate: `white`, `black`, or `both`        |

## Output Formats

### Annotated PGN

Standard PGN with:
- `{comments}` containing eval and classification at every inaccuracy/miss/mistake/blunder
- `[%eval +1.5]` tags for Lichess compatibility
- NAG symbols (`!`, `?!`, `?`, `??`)
- Variation branches `(1. e4 e5 2. Nf3)` showing the engine's best line and an alternative
- Best moves marked with `!`

This format imports directly into Lichess studies with all branches and comments preserved.

### JSON Report

Structured data with:
- Per-move classifications, cp_loss, eval before/after
- Best alternative lines for mistakes/blunders
- Summary statistics: move counts by category, average cp_loss per side

## Workflow: Blog Post with Engine Analysis

1. Save the game PGN to a temp file.
2. Run the analysis script to produce both annotated PGN and JSON.
3. Use the JSON report to write the Engine Review section of the blog post.
4. Use the annotated PGN for Lichess study import (if using studies).
5. The JSON `moves` array identifies which positions deserve diagrams (mistakes/blunders are natural decision points).

## Workflow: Lichess Study Import

The Lichess API cannot create studies, only import chapters into existing ones.

1. User creates a Lichess study manually and provides the study ID.
2. Run analysis to produce annotated PGN.
3. Import the annotated PGN as a new chapter via `POST /api/study/{study_id}/import-pgn`.
4. The `berserk` Python library wraps this: `client.studies.import_pgn(study_id, chapter_name, pgn, orientation)`.
5. Lichess preserves all comments `{...}` and variations `(...)` from the PGN.

Note: `berserk` is not yet installed. Install with: `pip install berserk` in the chess-diagram venv when ready.

## Performance

With the two-pass approach on a 46-move game (91 half-moves):
- Pass 1 (MultiPV 1, depth 18): ~90 seconds
- Pass 2 (MultiPV 3, ~10-15 positions): ~20-30 seconds
- Total: ~2 minutes (vs ~3+ minutes for single-pass MultiPV 3 on all positions)

The savings scale with game quality: cleaner games with fewer mistakes skip more positions in pass 2.

## Technical Notes

- Evaluations use `mate_score=10000` to convert mate scores to comparable centipawn values.
- Pass 1 uses the next position's eval as the "after" score for cp_loss calculation. This avoids a second analysis per position.
- Pass 2 re-analyses only positions needing alternative lines, using the stored FEN.
- MultiPV lines are converted to SAN notation for human readability and PGN compatibility.
- The annotated PGN builder adds variations as siblings of the played move node, which is the standard PGN variation format that Lichess understands.
- The "miss" classification is borrowed from the chesscli project's `analysis.gleam`, which distinguishes between ordinary inaccuracies and missed opportunities in winning positions.

## Related: chesscli

The classification thresholds and two-pass strategy are informed by `/Users/michaelbuhot/src/mbuhot/chesscli`, a Gleam/Bun chess TUI with Stockfish integration. See `src/chesscli/engine/analysis.gleam` for the move classification logic and `ARCHITECTURE.md` for the two-pass analysis design.
