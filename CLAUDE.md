# Chess Diary - Workspace Instructions

This is a chess blog where I (ohnonotmyhorsey, ~750 rated on chess.com) review my games. It's a Jekyll site hosted on GitHub Pages.

## Repository

- Remote: `git@github.com:mbuhot/chess-diary.git`
- URL: `https://ohnonotmyhorsey.com`
- Theme: minima

## How I provide game data

I'll give you a dictated voice recording of my self-review plus the PGN and engine analysis. The dictation will have voice-to-text errors (e.g. "porn" for "pawn", "keen" for "king", "roof" for "rook"). Clean these up but preserve my voice and opinions.

## Writing style

- Mix of casual/personal and educational/analytical tone. First person, conversational.
- No emdashes (`—`). Use periods, commas, or colons instead. Emdashes are too indicative of AI-assisted writing.
- Bold move notation inline (e.g. `**12...f5**`).
- Don't embellish or invent thoughts I didn't express. Stick to what I said in the dictation.

## Post types

There are two post formats: **single game reviews** (for rapid games) and **bullet session summaries** (for a batch of bullet games with highlighted games).

### Single game review structure

For detailed reviews of individual games (typically rapid):

```markdown
---
layout: post
title: "Result vs opponent (rating)"
date: YYYY-MM-DD HH:MM:SS
---

<style>
figure { margin: 1.5em 0 2em; }
figcaption { font-style: italic; color: #555; margin-top: 0.5em; }
</style>

**Opening:** Name | **Result:** X-X (Method) | **Time Control:** X min Rapid | **Rated/Unrated**

[View on Chess.com](URL)

<iframe ...chess.com embed...></iframe>
<script>...resize script...</script>

---

### Game Overview
Short summary of the game arc.

---

### Section Title (Moves X-Y)
**move notation in bold**
Narrative paragraphs describing what happened and what I was thinking.
<figure> elements for board positions.

---
(repeat sections as needed)

---

### Engine Review
Engine observations, chess.com ratings (great/best/excellent), key mistakes and alternatives.

---

### Reflections
Overall thoughts, "What went well" and "What to work on" bullet lists.

---

*Full PGN:*
```pgn block```

---

### Further Reading
- Links to relevant chess.com articles/resources/YouTube videos
```

Engine analysis observations belong in the Engine Review section, not in the narrative. The narrative should describe what I was thinking during the game.

### Bullet session summary structure

For a batch of bullet games with 2 highlighted games:

```markdown
---
layout: post
title: "Bullet Session N: Title"
date: YYYY-MM-DD HH:MM:SS
---

<style>
figure { margin: 1.5em 0 2em; }
figcaption { font-style: italic; color: #555; margin-top: 0.5em; }
table { width: 100%; border-collapse: collapse; margin: 1.5em 0; font-size: 0.9em; }
th, td { border: 1px solid #ddd; padding: 6px 10px; text-align: center; }
th { background-color: #f5f5f5; }
</style>

**Time Control:** 2 min + 1 sec increment (Bullet) | **Games:** N | **Record:** XW / YD / ZL

---

### Overview
Short summary of the session.

---

### All Games

<table> with columns: #, emoji, Color, Opponent, Result, Moves, My Acc, Rating
- No row colour highlighting (it clashes with theme striping)
- Emoji column for result method: ⚔️ checkmate, ⏳ time, 🏳️ resignation, 🤝 draw
- Bold the highest accuracy value(s)

---

### Highlight: Win vs opponent (rating) as Color

<iframe ...chess.com embed...></iframe>
<script>...resize script...</script>

Intro paragraph (scene-setting, opening name).

**Chunked move list up to first diagram position**

<figure>...</figure>

Narrative for this section.

**Next chunk of moves up to next diagram**

<figure>...</figure>

(repeat as needed, engine commentary can be woven into narrative)

---

(second highlight)

---

### Reflections
"What went well" and "What to work on" bullet lists.

---

### Further Reading
```

Key differences from single game reviews: engine commentary is woven into the highlight narrative rather than a separate section. Move lists are chunked between diagrams rather than showing the full PGN upfront. Typically 2-3 diagrams per highlighted game.

## Board diagrams

Diagrams are generated using python-chess via the chess-diagram skill at `.skills/chess-diagram/chess-diagram/`. Do NOT use chess.com screenshot exports.

### Generation workflow

1. Parse the PGN to get the FEN at the target ply.
2. Build a JSON config with the FEN, orientation, colours, and last-move highlights.
3. Run: `python .skills/chess-diagram/chess-diagram/scripts/generate_board.py --config config.json --output board.png`

### Config settings

- **Chess.com green theme colours:** `#ebecd0` (light squares), `#739552` (dark squares)
- **Last move highlights:** from-square `#829769A0`, to-square `#BACB44A0`
- **Board orientation:** match the player's colour (Black games = `"black"`, White games = `"white"`)
- **Size:** 720px
- **Coordinates:** true

### File naming and storage

- Single game reviews: `assets/images/YYYY-MM-DD-gameN/moveNN.png` (NN = ply number)
- Bullet sessions: `assets/images/YYYY-MM-DD/opponent_moveNN.png` (NN = ply number)

### Quantity

- Single game reviews: 8-12 diagrams covering every major moment.
- Bullet session highlights: 2-3 diagrams per highlighted game.

### HTML format

Use `<figure>` and `<figcaption>` HTML, not markdown image syntax:

```html
<figure>
  <img src="{{ '/assets/images/YYYY-MM-DD/filename.png' | relative_url }}" alt="Description">
  <figcaption>After X...move: Description of the position.</figcaption>
</figure>
```

Diagrams appear BEFORE their associated narrative text.

## Move list pacing

In highlight sections, chunk the move list between diagrams. Each bold move block covers from the previous diagram position to the next one. Don't dump the full PGN before the first diagram. Instead, show moves up to the first diagram position, then continue in chunks.

## Chess.com embed

The embed ID comes from the Share > Embed tab on chess.com. The iframe format is:

```html
<iframe id="EMBED_ID" allowtransparency="true" frameborder="0" style="width:100%;border:none;" src="https://www.chess.com/emboard?id=EMBED_ID"></iframe><script nonce="chesscom-diagram">window.addEventListener("message",e=>{e['data']&&"EMBED_ID"===e['data']['id']&&document.getElementById(`${e['data']['id']}`)&&(document.getElementById(`${e['data']['id']}`).style.height=`${e['data']['frameHeight']+37}px`)})</script>
```

The embed goes directly after the section heading, before any intro text.

## Post dating

When multiple games are posted on the same day, use the `date` front matter with a time component to control sort order (e.g. `2026-02-15 14:00:00` for the second game). The `_config.yml` has `future: true` so time-of-day won't prevent publishing.
