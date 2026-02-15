---
name: chess-diagram
description: >
  Generate annotated chess board diagrams as PNG images using python-chess.
  Use this skill whenever the user asks for a chess board image, position diagram,
  opening setup illustration, or any visual showing pieces, arrows, or highlighted
  squares on a chess board. Also trigger when the user says things like "show me
  the position after move 12", "draw arrows for the Italian Game setup", "create
  a diagram of the mating pattern", or "annotate this position". If a chess
  position needs to be visualised as an image file, this is the skill to use.
---

# Chess Diagram Generator

Generate polished, annotated chess board PNG images with arrows and square highlights. The output matches the visual style of chess.com board screenshots, making diagrams consistent with screenshots taken from game reviews.

## Dependencies

This skill requires `python-chess` and `cairosvg`. Install them if not already available:

```bash
pip install python-chess cairosvg --break-system-packages
```

## How It Works

The generation script at `scripts/generate_board.py` accepts a JSON config and an output path. You build the config based on what the user asks for, write it to a temp file, run the script, and deliver the PNG.

### Workflow

1. Interpret the user's request into a board position (FEN string) and annotations (arrows, highlights).
2. Write a JSON config file (see format below).
3. Run the script: `python <skill-path>/scripts/generate_board.py --config config.json --output board.png`
4. Verify the output by reading the PNG.
5. Deliver the file to the user.

### Config Format

```json
{
  "fen": "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1",
  "size": 720,
  "orientation": "white",
  "arrows": [
    {"from": "e2", "to": "e4", "color": "#e8a838"}
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
```

All fields are optional. Defaults produce a standard starting position board at 720px with chess.com-style colours.

### Field Reference

- **fen**: The board position as a FEN string. Use `chess.STARTING_FEN` for the opening position. To get a FEN after a sequence of moves, play them on a `chess.Board()` in Python and call `board.fen()`.
- **size**: Image width/height in pixels. 720 is a good default for blog posts.
- **orientation**: `"white"` (default) or `"black"` for the board perspective.
- **arrows**: List of arrows. Each has `from` and `to` as algebraic square names (e.g. `"e2"`, `"f3"`), and an optional `color` (hex string, default `"#e8a838"` gold).
- **highlights**: List of square highlights. Each has `square` (algebraic) and optional `color` (hex with alpha, e.g. `"#e8a83880"`).
- **coordinates**: Whether to show rank/file labels around the board edge. Default true.
- **colors**: Board square colours. Defaults to chess.com's wood theme (`#f0d9b5` light, `#b58863` dark).
- **arrow_style**: Controls arrow rendering. `shaft_width` (default 5.5), `head_scale` (default 0.55, where 1.0 is the original python-chess size), and `opacity` (default 0.8, where 1.0 is fully opaque). Smaller `head_scale` values give sleeker arrows.

### Common Colour Choices for Arrows

Use a consistent colour for all arrows unless the user specifically asks for colour-coding by piece type or purpose:

- Gold/orange (default, chess.com style): `#e8a838`
- Green (good moves): `#5b8c3e`
- Red (blunders/threats): `#c83030`
- Blue (alternative lines): `#3070c8`

### Getting a FEN from a Move Sequence

When the user describes a position by its moves rather than providing a FEN, play the moves on a board to derive the FEN:

```python
import chess
board = chess.Board()
moves = ["e4", "e5", "Nf3", "Nc6", "Bb5"]
for move in moves:
    board.push_san(move)
fen = board.fen()
```

Use this FEN in the config. For positions from PGN files, parse the PGN with `chess.pgn` and navigate to the desired move.

### Opening Setup Diagrams

For "show me the setup for opening X" requests where the user wants arrows from starting squares to destination squares: use the starting position FEN and add arrows showing where each piece moves to reach the target formation. This is more informative than just showing the completed position because it shows the development plan.

### Knight Move Arrows

Knight moves are automatically detected and rendered as L-shaped (right-angled) arrows, matching how chess.com displays them. The script identifies knight moves by checking the file/rank difference (1+2 or 2+1) and draws two line segments forming the L, with the longer leg first. No special config is needed: just specify the from/to squares and the script handles the rest.

### Arrow Styling Details

The script post-processes the SVG that python-chess generates. By default, python-chess draws oversized arrowheads. The script shrinks them by scaling the triangular head polygon while keeping the tip anchored at the destination square center, and extends the shaft line to connect to the resized head. This produces clean, proportional arrows that terminate precisely at the center of the target square.

All arrows are wrapped in an SVG opacity group (default 0.8) so pieces remain visible underneath the arrows. This is especially important for busy diagrams like opening setups with many overlapping arrows.
