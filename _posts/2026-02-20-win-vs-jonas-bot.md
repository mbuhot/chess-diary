---
layout: post
title: "Win vs Jonas-BOT (1700)"
date: 2026-02-20 16:00:00
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

**Opening:** English Opening | **Result:** 0-1 (Checkmate) | **Time Control:** Bot Match | **Unrated**

[View on Chess.com](https://www.chess.com/game/computer/769042259)

<iframe id="14611333" allowtransparency="true" frameborder="0" style="width:100%;border:none;" src="https://www.chess.com/emboard?id=14611333"></iframe><script nonce="chesscom-diagram">window.addEventListener("message",e=>{e['data']&&"14611333"===e['data']['id']&&document.getElementById(`${e['data']['id']}`)&&(document.getElementById(`${e['data']['id']}`).style.height=`${e['data']['frameHeight']+37}px`)});</script>

---

### Game Overview

My most difficult bot victory so far. Jonas-BOT is rated 1700, way above my level, and higher rated bots rarely make blunders. But I traded bishops in a way that ripped open the kingside, and the bot took the bait by grabbing a free knight instead of dealing with the checkmate threat. Mate in 16 moves.

---

### The Bishop Exchange (Moves 1-13)

**1. c4 Nf6 2. g3 g6 3. Bg2 Bg7 4. d3 O-O 5. e4 d6 6. Ne2 e5 7. O-O Ng4 8. h3 Nh6 9. Nbc3 Be6 10. Qb3 Qd7 11. Qxb7 Nc6 12. Nd5 Bxh3 13. Bxh3 Qxh3**

<figure>
  <img src="{{ '/assets/images/2026-02-20-game2/move24.png' | relative_url }}" alt="After 12...Bxh3">
  <figcaption>After 12...Bxh3: The bishop exchange. Stockfish says this is a mistake (+4.64 for White), but it leaves the king exposed.</figcaption>
</figure>

White's queen was off raiding on the queenside after **11. Qxb7**, so I traded bishops to tear open the h-file. Stockfish actually thinks Black is at a huge disadvantage here, nearly +5 for White. Objectively it's a bad move, but against a bot that loves grabbing material, it's a different story. The engine flagged **9...Be6** and **12...Bxh3** as mistakes and **10...Qd7** as a blunder. From a pure material standpoint they are, but they're also setting the trap.

---

### The Trap (Moves 14-16)

**14. Qxc6 Ng4 15. Rd1 Qh2+ 16. Kf1 Qxf2#**

<figure>
  <img src="{{ '/assets/images/2026-02-20-game2/move27.png' | relative_url }}" alt="After 14. Qxc6">
  <figcaption>After 14. Qxc6: The bot takes the hanging knight instead of defending. The queen and knight are already zeroing in on f2.</figcaption>
</figure>

This is where the bot fell for it. **14. Qxc6** was the biggest blunder of the game. Instead of dealing with the mating threats on the kingside, it grabbed the hanging knight on c6. Now my queen is on h3, my knight is ready to jump to g4, and there's nothing White can do about it. **14...Ng4** was rated great by the engine. It threatens Qh2+ followed by Qxf2#, and that's exactly what happened.

<figure>
  <img src="{{ '/assets/images/2026-02-20-game2/move32.png' | relative_url }}" alt="16...Qxf2# Checkmate">
  <figcaption>16...Qxf2#: Checkmate. The queen is protected by the knight on g4.</figcaption>
</figure>

---

### Reflections

Bot matches don't really count, but it's nice to get a win and reach a new record for bot rating difficulty after some recent losses. The bishop exchange was objectively a mistake, but it created exactly the kind of trap that bots fall for: a free piece dangling while a mating attack brews on the other side of the board.

---

*Full PGN:*

```
1. c4 Nf6 2. g3 g6 3. Bg2 Bg7 4. d3 O-O 5. e4 d6 6. Ne2 e5 7. O-O Ng4 8. h3 Nh6
9. Nbc3 Be6 10. Qb3 Qd7 11. Qxb7 Nc6 12. Nd5 Bxh3 13. Bxh3 Qxh3 14. Qxc6 Ng4 15.
Rd1 Qh2+ 16. Kf1 Qxf2# 0-1
```
