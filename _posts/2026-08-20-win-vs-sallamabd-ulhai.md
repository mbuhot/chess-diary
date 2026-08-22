---
layout: post
title: "Win vs Sallamabd-ulhai: A Pawn Push Turns the Tide"
date: 2026-08-20 13:45:00 +1000
---

<style>
figure { margin: 1.5em 0 2em; }
figcaption { font-style: italic; color: #555; margin-top: 0.5em; }
</style>

**Opening:** Pirc Defense | **Result:** 0-1 (Resignation) | **Time Control:** 10 min Rapid | **Rated**

[View on Chess.com](https://www.chess.com/game/live/173255705406?move=0)

<iframe id="15572138" allowtransparency="true" frameborder="0" style="width:100%;border:none;" src="https://www.chess.com/emboard?id=15572138"></iframe><script nonce="chesscom-diagram">window.addEventListener("message",e=>{e['data']&&"15572138"===e['data']['id']&&document.getElementById(`${e['data']['id']}`)&&(document.getElementById(`${e['data']['id']}`).style.height=`${e['data']['frameHeight']+37}px`)})</script>

---

### Game Overview

This one was an amazing turnaround. I was a pawn down with my bishop against a knight from move 31, and then a simple pawn push blunder gave me the game. I took en passant with unstoppable promotion and my opponent resigned.

---

### The Opening (Moves 7-10)

<figure>
  <img src="{{ '/assets/images/2026-08-20-game3/move13.png' | relative_url }}" alt="Position after 7.Re1, Black to play">
  <figcaption>After 7.Re1: a standard Pirc setup with both sides castled.</figcaption>
</figure>

**7...Nc6 8.Bg5 h6 9.Bh4 g5 10.Bg3**

The game started with pretty typical Pirc Defense moves. When White brought the bishop to g5 I chased it away with **8...h6** and **9...g5**.

---

### Opening the Centre (Moves 10-13)

<figure>
  <img src="{{ '/assets/images/2026-08-20-game3/move19.png' | relative_url }}" alt="Position after 10.Bg3, Black to play">
  <figcaption>After 10.Bg3: the white bishop is back on the b8-h2 diagonal.</figcaption>
</figure>

**10...d5 11.exd5 Nxd5 12.Nxd5 Qxd5 13.c3**

Then I didn't see an obvious path forward, so I decided to open up the centre with **10...d5**. The knights came off on d5 and I recaptured with the queen.

---

### The e4 Push (Moves 13-17)

<figure>
  <img src="{{ '/assets/images/2026-08-20-game3/move25.png' | relative_url }}" alt="Position after 13.c3, Black to play">
  <figcaption>After 13.c3: my queen on d5 and my pawn on e5 face White's pawn on d3.</figcaption>
</figure>

**13...e4 14.dxe4 Qxe4 15.Bb5 Qf5 16.Bxc6 bxc6 17.Bxc7**

I was going okay until I pushed **13...e4**. This allowed White to trade a bishop for my knight and give me doubled pawns on the c-file. And then I lose the c7 pawn.

---

### White Trades Down (Moves 17-20)

<figure>
  <img src="{{ '/assets/images/2026-08-20-game3/move33.png' | relative_url }}" alt="Position after 17.Bxc7, Black to play">
  <figcaption>After 17.Bxc7: White is a pawn up and my c-pawns are doubled.</figcaption>
</figure>

**17...Be6 18.Be5 Rad8 19.Qc1 Rd5 20.Bxg7 Kxg7**

White was then able to trade the dark-squared bishops.

---

### Manoeuvring and the Rook Trade (Moves 21-27)

<figure>
  <img src="{{ '/assets/images/2026-08-20-game3/move40.png' | relative_url }}" alt="Position after 20...Kxg7, White to play">
  <figcaption>After 20...Kxg7: the dark-squared bishops are gone and my king sits on g7.</figcaption>
</figure>

**21.Rd1 Rfd8 22.Rxd5 Bxd5 23.Nd4 Qe4 24.f3 Qe5 25.Qe1 Re8 26.Qxe5+ Rxe5 27.Kf2**

After some more manoeuvring we traded a pair of rooks, and then the queens as well.

---

### A Pawn Down (Moves 27-32)

<figure>
  <img src="{{ '/assets/images/2026-08-20-game3/move53.png' | relative_url }}" alt="Position after 27.Kf2, Black to play">
  <figcaption>After 27.Kf2: rook and bishop against rook and knight, and White is a pawn up.</figcaption>
</figure>

**27...c5 28.Nb5 a6 29.Nc7 Bc4 30.Re1 Rxe1 31.Kxe1 Bxa2 32.Nxa6 c4**

So by move 31 White has an extra pawn, and it's my bishop against White's knight.

---

### The Pawn Push That Flips It (Moves 33-34)

<figure>
  <img src="{{ '/assets/images/2026-08-20-game3/move64.png' | relative_url }}" alt="Position after 32...c4, White to play">
  <figcaption>After 32...c4: my bishop on a2 covers b3 and my pawn sits on c4.</figcaption>
</figure>

**33.b4 cxb3 34.Kd1 b2**

And then on move 33, a simple pawn push flips the story. **33.b4** pushes the pawn two squares past my pawn on c4, so I take on b3 en passant, supported by my bishop on a2. The pawn is going to make it to the promotion square.

<figure>
  <img src="{{ '/assets/images/2026-08-20-game3/engine-line-en-passant.gif' | relative_url }}" alt="Animated finish: 33.b4 cxb3 34.Kd1 b2">
  <figcaption>33.b4 cxb3 34.Kd1 b2: the pawn walks in and the bishop covers b1.</figcaption>
</figure>

<figure>
  <img src="{{ '/assets/images/2026-08-20-game3/move68.png' | relative_url }}" alt="Position after 34...b2, White resigned">
  <figcaption>After 34...b2: White cannot cover b1 and resigned here.</figcaption>
</figure>

---

### Engine Review

Once the pawn promotes to a queen it's checkmate in fourteen according to the chess.com engine. Stockfish agrees: from the position where White resigned it gives mate in sixteen, which is the same count once you add the king move and the promotion.

<figure>
  <img src="{{ '/assets/images/2026-08-20-game3/engine-line-mate.gif' | relative_url }}" alt="Animated engine line: the forced mate after 35.Kd2 b1=Q">
  <figcaption>The forced mate: 35.Kd2 b1=Q 36.Nc7 Qb2+ 37.Kd3 Qxg2 38.Ne8+ Kg6 39.c4 Qxf3+ 40.Kd4 Qf4+ 41.Kc5 Qxc4+ 42.Kd6 Qe6+ 43.Kc5 Qxe8 44.Kb6 Qe5 45.Kc6 Qd5+ 46.Kb6 Bc4 47.Kc7 Qc5+ 48.Kb7 Bd5+ 49.Ka6 Bc6 50.h3 Qb5+ 51.Ka7 Qb7#.</figcaption>
</figure>

**33.b4** swung the evaluation by nearly nine pawns, from 3.6 in White's favour to 5.3 in mine. The move was **33.Nb4**, which keeps White around four pawns up. The engine line runs **33...Bb1 34.Nd5**.

My own worst move was **13...e4**, which cost about two and a half pawns. Before it I was slightly better. After **14.dxe4 Qxe4 15.Bb5** the bishop hit the knight on c6, and once it came off with **16.Bxc6 bxc6** my c-pawns were doubled and the pawn on c7 had nothing defending it.

---

### Reflections

**What went well:**

- Chasing the dark-squared bishop away with **8...h6** and **9...g5** in a standard Pirc setup.

**What to work on:**

- Pawn breaks. **13...e4** looked like it was opening lines for my queen and it just dropped a piece's worth of pressure and then a pawn.

This game really goes to show that it's never too late to lose from a winning position, and it doesn't always look like blundering a high value piece. It can be a pawn push, or forgetting about en passant, that turns the tide of a game.

---

*Full PGN:*

```
1. e4 d6 2. Nf3 Nf6 3. Nc3 g6 4. d3 Bg7 5. Be2 O-O 6. O-O e5 7. Re1 Nc6 8. Bg5
h6 9. Bh4 g5 10. Bg3 d5 11. exd5 Nxd5 12. Nxd5 Qxd5 13. c3 e4 14. dxe4 Qxe4 15.
Bb5 Qf5 16. Bxc6 bxc6 17. Bxc7 Be6 18. Be5 Rad8 19. Qc1 Rd5 20. Bxg7 Kxg7 21.
Rd1 Rfd8 22. Rxd5 Bxd5 23. Nd4 Qe4 24. f3 Qe5 25. Qe1 Re8 26. Qxe5+ Rxe5 27. Kf2
c5 28. Nb5 a6 29. Nc7 Bc4 30. Re1 Rxe1 31. Kxe1 Bxa2 32. Nxa6 c4 33. b4 cxb3 34.
Kd1 b2 0-1
```

---

### Further Reading

- [En Passant](https://www.chess.com/terms/en-passant)
- [Pirc Defense](https://www.chess.com/openings/Pirc-Defense)
- [Doubled Pawns](https://www.chess.com/terms/doubled-pawns-chess)
