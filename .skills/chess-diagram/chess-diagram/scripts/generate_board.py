#!/usr/bin/env python3
"""
Generate annotated chess board diagrams as PNG images.

Usage:
    python generate_board.py --config config.json --output board.png

Config JSON format:
{
    "fen": "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1",
    "size": 720,
    "orientation": "white",
    "arrows": [
        {"from": "e2", "to": "e4", "color": "#e8a838"},
        {"from": "g1", "to": "f3", "color": "#e8a838"}
    ],
    "highlights": [
        {"square": "e4", "color": "#e8a83880"}
    ],
    "coordinates": true,
    "colors": {
        "square_light": "#f0d9b5",
        "square_dark": "#b58863"
    },
    "arrow_style": {
        "shaft_width": 5.5,
        "head_scale": 0.55,
        "opacity": 0.8
    }
}

All fields except output path are optional and have sensible defaults.
"""

import argparse
import json
import math
import re
import sys

import chess
import chess.svg
import cairosvg


BOARD_MARGIN = 15  # python-chess coordinate margin with coordinates=True
BOARD_MARGIN_NO_COORDS = 0


def parse_square(name):
    """Convert a square name like 'e4' to a python-chess square constant."""
    return chess.parse_square(name.lower())


def is_knight_move(from_sq, to_sq):
    """Check if a move is an L-shaped knight move."""
    from_file = chess.square_file(from_sq)
    from_rank = chess.square_rank(from_sq)
    to_file = chess.square_file(to_sq)
    to_rank = chess.square_rank(to_sq)
    df = abs(from_file - to_file)
    dr = abs(from_rank - to_rank)
    return (df == 1 and dr == 2) or (df == 2 and dr == 1)


def square_center(sq, size, orientation, has_coords):
    """Get the pixel center of a square on the board image."""
    margin = BOARD_MARGIN if has_coords else BOARD_MARGIN_NO_COORDS
    board_size = size - 2 * margin
    sq_size = board_size / 8

    file_idx = chess.square_file(sq)
    rank_idx = chess.square_rank(sq)

    if orientation == "white":
        x = margin + (file_idx + 0.5) * sq_size
        y = margin + (7 - rank_idx + 0.5) * sq_size
    else:
        x = margin + (7 - file_idx + 0.5) * sq_size
        y = margin + (rank_idx + 0.5) * sq_size

    return x, y


def build_straight_arrows(arrow_configs):
    """Build chess.svg.Arrow objects for non-knight moves."""
    arrows = []
    for a in arrow_configs:
        from_sq = parse_square(a["from"])
        to_sq = parse_square(a["to"])
        if is_knight_move(from_sq, to_sq):
            continue
        color = a.get("color", "#e8a838")
        arrows.append(chess.svg.Arrow(from_sq, to_sq, color=color))
    return arrows


def get_knight_arrow_configs(arrow_configs):
    """Filter arrow configs to only knight moves."""
    result = []
    for a in arrow_configs:
        from_sq = parse_square(a["from"])
        to_sq = parse_square(a["to"])
        if is_knight_move(from_sq, to_sq):
            result.append(a)
    return result


def build_fill(highlight_configs):
    """Build a fill dict for square highlights."""
    fill = {}
    for h in highlight_configs:
        sq = parse_square(h["square"])
        fill[sq] = h.get("color", "#e8a83880")
    return fill


def parse_polygon_points(points_str):
    """Parse 'x,y x,y x,y' into list of [x,y] pairs."""
    return [[float(c) for c in p.split(",")] for p in points_str.split()]


def shrink_polygon_keep_tip(tip, base1, base2, scale):
    """Shrink the arrowhead keeping the tip fixed at the destination square center.
    Move base1 and base2 toward the tip."""
    new_base1 = [
        tip[0] + (base1[0] - tip[0]) * scale,
        tip[1] + (base1[1] - tip[1]) * scale,
    ]
    new_base2 = [
        tip[0] + (base2[0] - tip[0]) * scale,
        tip[1] + (base2[1] - tip[1]) * scale,
    ]
    return tip, new_base1, new_base2


def refine_arrows(svg_data, head_scale=0.55, shaft_width=5.5):
    """Post-process SVG to shrink arrowheads and thin shafts.

    python-chess renders arrows as a <line> (shaft) + <polygon> (triangular head).
    The shaft endpoint sits at the base of the original triangle. When we shrink
    the triangle (keeping the tip fixed at the destination square center), the base
    moves closer to the tip, so we also extend the shaft to meet the new base.
    """
    arrow_polygons = list(
        re.finditer(
            r'<polygon points="([^"]+)" fill="([^"]+)" class="arrow" />',
            svg_data,
        )
    )

    arrow_lines = list(
        re.finditer(
            r'<line x1="([^"]+)" y1="([^"]+)" x2="([^"]+)" y2="([^"]+)" '
            r'stroke="([^"]+)" stroke-width="[^"]+" stroke-linecap="[^"]+" '
            r'class="arrow" />',
            svg_data,
        )
    )

    replacements = []

    for poly_match in arrow_polygons:
        points = parse_polygon_points(poly_match.group(1))
        fill = poly_match.group(2)

        if len(points) != 3:
            continue

        tip, base1, base2 = points
        new_tip, new_base1, new_base2 = shrink_polygon_keep_tip(
            tip, base1, base2, head_scale
        )

        new_base_mid = [
            (new_base1[0] + new_base2[0]) / 2,
            (new_base1[1] + new_base2[1]) / 2,
        ]

        new_poly = (
            f'<polygon points="{new_tip[0]},{new_tip[1]} '
            f'{new_base1[0]},{new_base1[1]} '
            f'{new_base2[0]},{new_base2[1]}" '
            f'fill="{fill}" class="arrow" />'
        )
        replacements.append((poly_match.start(), poly_match.end(), new_poly))

        # Find the corresponding shaft line by matching its endpoint
        # to the original triangle's base midpoint.
        orig_base_mid = [
            (base1[0] + base2[0]) / 2,
            (base1[1] + base2[1]) / 2,
        ]

        best_line = None
        best_dist = float("inf")
        for line_match in arrow_lines:
            lx2 = float(line_match.group(3))
            ly2 = float(line_match.group(4))
            dist = math.hypot(lx2 - orig_base_mid[0], ly2 - orig_base_mid[1])
            if dist < best_dist:
                best_dist = dist
                best_line = line_match

        if best_line and best_dist < 50:
            old_line = best_line.group(0)
            new_line = old_line.replace(
                f'x2="{best_line.group(3)}" y2="{best_line.group(4)}"',
                f'x2="{new_base_mid[0]}" y2="{new_base_mid[1]}"',
            )
            replacements.append(
                (best_line.start(), best_line.end(), new_line)
            )

    # Apply from end to start to preserve string offsets
    replacements.sort(key=lambda r: r[0], reverse=True)
    for start, end, new_text in replacements:
        svg_data = svg_data[:start] + new_text + svg_data[end:]

    # Adjust shaft width
    svg_data = svg_data.replace('stroke-width="9.0"', f'stroke-width="{shaft_width}"')

    return svg_data


def build_knight_arrow_svg(from_sq, to_sq, color, size, orientation, has_coords,
                           shaft_width=5.5, head_scale=0.55):
    """Build an L-shaped SVG arrow for a knight move.

    The arrow goes horizontally/vertically first along the longer leg,
    then turns 90 degrees for the shorter leg, with an arrowhead at the end.
    """
    x1, y1 = square_center(from_sq, size, orientation, has_coords)
    x2, y2 = square_center(to_sq, size, orientation, has_coords)

    from_file = chess.square_file(from_sq)
    from_rank = chess.square_rank(from_sq)
    to_file = chess.square_file(to_sq)
    to_rank = chess.square_rank(to_sq)

    df = abs(from_file - to_file)
    dr = abs(from_rank - to_rank)

    # The longer leg determines which direction we go first.
    # If file difference is larger (2), go horizontally first then vertically.
    # If rank difference is larger (2), go vertically first then horizontally.
    if df > dr:
        # Horizontal first, then vertical
        corner_x = x2
        corner_y = y1
    else:
        # Vertical first, then horizontal
        corner_x = x1
        corner_y = y2

    # Direction from corner to destination for the arrowhead
    dx = x2 - corner_x
    dy = y2 - corner_y
    length = math.hypot(dx, dy)

    if length > 0:
        ux = dx / length
        uy = dy / length
    else:
        ux, uy = 0, 0

    # Arrowhead dimensions
    orig_head_length = 18
    orig_head_width = 9
    head_length = orig_head_length * head_scale
    head_width = orig_head_width * head_scale

    # Tip is at the destination center
    tip_x, tip_y = x2, y2

    # Base of arrowhead (where shaft meets the head)
    base_x = tip_x - ux * head_length
    base_y = tip_y - uy * head_length

    # Perpendicular direction for arrowhead width
    perp_x = -uy
    perp_y = ux

    # Arrowhead triangle points
    left_x = base_x + perp_x * head_width
    left_y = base_y + perp_y * head_width
    right_x = base_x - perp_x * head_width
    right_y = base_y - perp_y * head_width

    # The shaft: two line segments forming the L, ending at arrowhead base
    # Segment 1: from start to corner
    # Segment 2: from corner to arrowhead base
    svg_parts = []

    # Shaft segment 1: start to corner
    svg_parts.append(
        f'<line x1="{x1}" y1="{y1}" x2="{corner_x}" y2="{corner_y}" '
        f'stroke="{color}" stroke-width="{shaft_width}" '
        f'stroke-linecap="round" class="arrow" />'
    )

    # Shaft segment 2: corner to arrowhead base
    svg_parts.append(
        f'<line x1="{corner_x}" y1="{corner_y}" x2="{base_x}" y2="{base_y}" '
        f'stroke="{color}" stroke-width="{shaft_width}" '
        f'stroke-linecap="round" class="arrow" />'
    )

    # Arrowhead polygon
    svg_parts.append(
        f'<polygon points="{tip_x},{tip_y} {left_x},{left_y} {right_x},{right_y}" '
        f'fill="{color}" class="arrow" />'
    )

    return "\n".join(svg_parts)


def inject_knight_arrows(svg_data, knight_configs, size, orientation, has_coords, arrow_style):
    """Inject L-shaped knight arrows into the SVG before the closing </svg> tag."""
    if not knight_configs:
        return svg_data

    shaft_width = arrow_style.get("shaft_width", 5.5)
    head_scale = arrow_style.get("head_scale", 0.55)

    knight_svgs = []
    for a in knight_configs:
        from_sq = parse_square(a["from"])
        to_sq = parse_square(a["to"])
        color = a.get("color", "#e8a838")
        knight_svgs.append(
            build_knight_arrow_svg(
                from_sq, to_sq, color, size, orientation, has_coords,
                shaft_width, head_scale
            )
        )

    insert_block = "\n".join(knight_svgs)
    svg_data = svg_data.replace("</svg>", f"{insert_block}\n</svg>")
    return svg_data


def apply_opacity(svg_data, opacity):
    """Wrap all arrow elements in a group with the specified opacity."""
    if opacity >= 1.0:
        return svg_data

    # python-chess puts arrow elements at the end of the SVG.
    # We find all arrow class elements and wrap them in an opacity group.
    # Strategy: collect arrow elements, remove them, re-insert inside a <g> wrapper.
    arrow_pattern = r'(<(?:line|polygon)[^>]*class="arrow"[^/]*/?>)'
    arrow_matches = list(re.finditer(arrow_pattern, svg_data))

    if not arrow_matches:
        return svg_data

    # Extract all arrow elements
    arrow_elements = [m.group(0) for m in arrow_matches]

    # Remove arrow elements from SVG (process from end to preserve offsets)
    for m in reversed(arrow_matches):
        svg_data = svg_data[:m.start()] + svg_data[m.end():]

    # Build the opacity group
    group = f'<g opacity="{opacity}">\n' + "\n".join(arrow_elements) + "\n</g>"

    # Insert before </svg>
    svg_data = svg_data.replace("</svg>", f"{group}\n</svg>")

    return svg_data


def generate_board(config, output_path):
    """Generate a chess board PNG from a config dict."""
    fen = config.get("fen", chess.STARTING_FEN)
    size = config.get("size", 720)
    orientation = config.get("orientation", "white")
    show_coords = config.get("coordinates", True)
    board_colors = config.get("colors", {})
    arrow_style = config.get("arrow_style", {})
    opacity = arrow_style.get("opacity", 0.8)

    board = chess.Board(fen)

    arrow_configs = config.get("arrows", [])
    straight_arrows = build_straight_arrows(arrow_configs)
    knight_configs = get_knight_arrow_configs(arrow_configs)
    fill = build_fill(config.get("highlights", []))

    colors = {}
    if "square_light" in board_colors:
        colors["square light"] = board_colors["square_light"]
    if "square_dark" in board_colors:
        colors["square dark"] = board_colors["square_dark"]

    svg_kwargs = dict(
        arrows=straight_arrows,
        fill=fill,
        size=size,
        coordinates=show_coords,
        orientation=chess.WHITE if orientation == "white" else chess.BLACK,
    )
    if colors:
        svg_kwargs["colors"] = colors

    svg_data = chess.svg.board(board, **svg_kwargs)

    # Refine straight arrow styling
    if straight_arrows:
        head_scale = arrow_style.get("head_scale", 0.55)
        shaft_width = arrow_style.get("shaft_width", 5.5)
        svg_data = refine_arrows(svg_data, head_scale, shaft_width)

    # Inject L-shaped knight arrows
    svg_data = inject_knight_arrows(
        svg_data, knight_configs, size, orientation, show_coords, arrow_style
    )

    # Apply opacity to all arrows
    svg_data = apply_opacity(svg_data, opacity)

    cairosvg.svg2png(
        bytestring=svg_data.encode(),
        write_to=output_path,
        output_width=size,
        output_height=size,
    )
    print(f"Saved board diagram to {output_path}")


def main():
    parser = argparse.ArgumentParser(description="Generate annotated chess board diagrams")
    parser.add_argument("--config", required=True, help="Path to JSON config file")
    parser.add_argument("--output", required=True, help="Output PNG path")
    args = parser.parse_args()

    with open(args.config) as f:
        config = json.load(f)

    generate_board(config, args.output)


if __name__ == "__main__":
    main()
