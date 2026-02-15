# Chess Diary - Workspace Instructions

This is a chess blog where I (ohnonotmyhorsey, ~750 rated on chess.com) review my games. It's a Jekyll site hosted on GitHub Pages.

## Repository

- Remote: `git@github.com:mbuhot/chess-diary.git`
- GitHub Pages URL: `https://mbuhot.github.io/chess-diary/`
- Theme: minima

## How I provide game data

I'll give you a dictated voice recording of my self-review plus the PGN and engine analysis. The dictation will have voice-to-text errors (e.g. "porn" for "pawn", "keen" for "king", "roof" for "rook"). Clean these up but preserve my voice and opinions.

## Writing style

- Mix of casual/personal and educational/analytical tone. First person, conversational.
- No emdashes (`—`). Use periods, commas, or colons instead. Emdashes are too indicative of AI-assisted writing.
- Bold move notation inline (e.g. `**12...f5**`).
- Keep engine analysis observations in the Engine Review section, not in the narrative sections. The narrative should describe what I was thinking during the game.
- Don't embellish or invent thoughts I didn't express. Stick to what I said in the dictation.

## Post structure

Each post follows this template:

```markdown
---
layout: post
title: "Result vs opponent (rating)"
date: YYYY-MM-DD HH:MM:SS
---

<style>
figure {
  margin: 1.5em 0 2em;
}
figcaption {
  font-style: italic;
  color: #555;
  margin-top: 0.5em;
}
</style>

**Opening:** Name | **Result:** X-X (Method) | **Time Control:** X min Rapid | **Rated/Unrated**

[View on Chess.com](URL)

<iframe ...embed from chess.com Share > Embed tab...></iframe>
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
- Links to relevant chess.com articles/resources
```

## Images

- 8-12 board position screenshots per game, covering every major moment.
- Screenshots come from chess.com Share > Image > Download at each position URL (`?move=N` where N is the half-move/ply number).
- Store in `assets/images/YYYY-MM-DD-gameN/` (e.g. `2026-02-15-game2/`).
- Name files by half-move number: `move12.png`, `move24.png`, etc.
- User may also provide annotated screenshots (with arrows/highlights) for key positions.
- Use `<figure>` and `<figcaption>` HTML, not markdown image syntax:

```html
<figure>
  <img src="{{ '/assets/images/YYYY-MM-DD-gameN/moveNN.png' | relative_url }}" alt="Description">
  <figcaption>After X...move: Description of the position.</figcaption>
</figure>
```

## Chess.com embed

Get the embed ID from the Share > Embed tab. The iframe format is:

```html
<iframe id="EMBED_ID" allowtransparency="true" frameborder="0" style="width:100%;border:none;" src="https://www.chess.com/emboard?id=EMBED_ID"></iframe>
<script>window.addEventListener("message",e=>{if(e.data&&"EMBED_ID"===e.data.id&&document.getElementById(e.data.id)){document.getElementById(e.data.id).style.height=(e.data.frameHeight+37)+"px"}})</script>
```

## Chess.com move URLs

To link to a specific position: `https://www.chess.com/game/live/GAME_ID?move=N`

The `move` parameter is the half-move (ply) number, not the full-move number. For example, after White's 6th move is `?move=11`, after Black's 6th move is `?move=12`.

## Post dating

When multiple games are posted on the same day, use the `date` front matter with a time component to control sort order (e.g. `2026-02-15 14:00:00` for the second game). The `_config.yml` has `future: true` so time-of-day won't prevent publishing.
