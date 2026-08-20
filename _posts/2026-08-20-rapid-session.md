---
layout: post
title: "August 20 Rapid Session: Trouble as White"
date: 2026-08-20 14:00:00 +1000
---

<style>
figure { margin: 1.5em 0 2em; }
figcaption { font-style: italic; color: #555; margin-top: 0.5em; }
table { width: 100%; border-collapse: collapse; margin: 1.5em 0; font-size: 0.9em; }
th, td { border: 1px solid #ddd; padding: 6px 10px; text-align: center; }
th { background-color: #f5f5f5; }
td.comment { text-align: left; }
</style>

**Time Control:** 10 min (Rapid) | **Games:** 6 | **Record:** 3W / 1D / 2L

---

### Overview

Six rapid games, three wins, one draw and two losses. The ratings attached to the games ran 887, 895, 887, 895, 895, 903, so I finished the night a little higher than I started it.

The split was clean along colour lines. I had White three times and dropped material in the opening in every one of them: a knight on move 9, a knight and a bishop on move 10, and a pawn on move 12. I had Black three times and won twice with a draw in the third.

The two best games were both as Black, and both followed the same recipe. Trade the queens early, then hunt for loose pieces.

---

### All Games

<table>
<tr><th>#</th><th></th><th>Color</th><th>Opponent</th><th>Result</th><th>Moves</th><th>Comment</th></tr>
<tr><td>1</td><td>⚔️</td><td>White</td><td>santa0700</td><td>0-1</td><td>36</td><td class="comment">Loss. 8.Nb3 walked into 8...c4 and the knight had nowhere safe to go.</td></tr>
<tr><td>2</td><td>🏳️</td><td>Black</td><td>clintocki</td><td>0-1</td><td>59</td><td class="comment"><strong>Highlight.</strong> A three-move tactic on move 13 won a piece, then a fianchetto on b7 won the exchange.</td></tr>
<tr><td>3</td><td>⚔️</td><td>White</td><td>UmaeTeam</td><td>0-1</td><td>50</td><td class="comment">Loss. 10.Bd2 blocked a check instead of 10.Kf1, which wins the black queen.</td></tr>
<tr><td>4</td><td>⚔️</td><td>White</td><td>benjaminarnal</td><td>1-0</td><td>29</td><td class="comment">Win. My opponent missed Nxf2 three moves running, then 14.Qxg4 won a knight.</td></tr>
<tr><td>5</td><td>🤝</td><td>Black</td><td>DARKSEID_OTH</td><td>1/2-1/2</td><td>63</td><td class="comment">Draw. Two pawns up in a rook endgame, then 44...g2 gave it all back.</td></tr>
<tr><td>6</td><td>⚔️</td><td>Black</td><td>TheM4sterM1nd</td><td>0-1</td><td>30</td><td class="comment"><strong>Best game.</strong> Won the exchange with a pin on f2, then a ladder mate on the h-file.</td></tr>
</table>

---

### Game 1: Loss vs santa0700 as White

A French with an early c6. I pushed **4.e5** to take space and had a comfortable position out of the opening.

<figure>
  <img src="{{ '/assets/images/2026-08-20/santa0700_move14.png' | relative_url }}" alt="Position after 7...c5, White to play">
  <figcaption>After 7...c5: the d4 pawn is challenged and my knight sits on d2.</figcaption>
</figure>

**8.Nb3 c4 9.Na5 Qxa5**

**8.dxc5** was the move here. Instead **8.Nb3** put the knight on the one square the c-pawn could reach, **8...c4** hit it, and a5 was the only forward square left. It hangs to the queen on d8. Two moves took the evaluation from nearly two pawns in my favour to more than three against me. I played on for another 27 moves and got mated on move 36.

---

### Game 2: Win vs clintocki as Black

White opened **1.g3**, the King's Fianchetto Opening. I played it like a typical King's Indian Defence or Pirc.

**1.g3 Nf6 2.d3 g6 3.Bg2 Bg7 4.c3 O-O 5.h3 d6 6.g4 e5 7.Bg5 h6 8.Bxf6 Qxf6 9.e4 Nd7 10.Qf3 Qxf3 11.Nxf3**

<figure>
  <img src="{{ '/assets/images/2026-08-20/clintocki_move21.png' | relative_url }}" alt="Position after 11.Nxf3, Black to play">
  <figcaption>After 11.Nxf3: the queens are off and material is level.</figcaption>
</figure>

**11...Nc5 12.Kd2 f5 13.b4**

We traded queens early on f3. Material was equal, but Stockfish rated the position about 1.4 pawns in my favour. White had spent the opening pushing pawns and the king had no castling rights left.

<figure>
  <img src="{{ '/assets/images/2026-08-20/clintocki_move25.png' | relative_url }}" alt="Position after 13.b4, Black to play">
  <figcaption>After 13.b4: my knight on c5 is attacked and White's knight sits on f3.</figcaption>
</figure>

**13...fxe4 14.bxc5 exf3 15.Bxf3 Rxf3 16.Ke2 Rf4 17.Na3 b6 18.Nc4 bxc5 19.Ne3**

On move 13 I spotted a tactic. **13...fxe4** allows **14.bxc5**, temporarily sacrificing a knight. **14...exf3** gains the knight back, and if White recaptures the pawn on f3 he loses the bishop to **15...Rxf3**. White was careless with **15.Bxf3** and is now down a piece.

<figure>
  <img src="{{ '/assets/images/2026-08-20/clintocki_move37.png' | relative_url }}" alt="Position after 19.Ne3, Black to play">
  <figcaption>After 19.Ne3: my light-squared bishop is still at home on c8.</figcaption>
</figure>

**19...Bb7 20.Rab1 Bxh1 21.Rxh1 e4 22.Nd5 Rf7 23.dxe4 Re8 24.f3 c6 25.Ne3 d5 26.c4 dxe4 27.f4**

My next idea was to activate the light-squared bishop. I went for a fianchetto on b7, targeting the rook on h1. White missed the idea and targeted my bishop with the a-rook. **20.Rab1** lost an exchange. The h-rook was the one to move.

<figure>
  <img src="{{ '/assets/images/2026-08-20/clintocki_move53.png' | relative_url }}" alt="Position after 27.f4, Black to play">
  <figcaption>After 27.f4: White has one rook left, on h1.</figcaption>
</figure>

**27...Rxf4 28.Rf1 Rxf1 29.Kxf1 Rf8+ 30.Ke2 Rf3 31.h4 Rh3 32.h5 gxh5 33.gxh5 Rxh5 34.a4 Rh2+ 35.Kf1 Ra2 36.Nf5 Rxa4 37.Ne7+ Kf7 38.Nxc6 h5 39.Nd8+ Ke7 40.Nc6+ Ke6 41.Nd8+ Kf5 42.Nb7**

A few more pawn pushes and I traded White's last remaining rook on f1.

<figure>
  <img src="{{ '/assets/images/2026-08-20/clintocki_move83.png' | relative_url }}" alt="Position after 42.Nb7, Black to play">
  <figcaption>After 42.Nb7: my rook is on a4, my king on f5, and the knight is heading for d6.</figcaption>
</figure>

**42...Rxc4 43.Nd6+ Kf4 44.Nxc4 Bc3**

I got careless and fell prey to a fork, losing my rook for a pawn.

<figure>
  <img src="{{ '/assets/images/2026-08-20/clintocki_move88.png' | relative_url }}" alt="Position after 44...Bc3, White to play">
  <figcaption>After 44...Bc3: White has no pawns, so all four of mine are passed.</figcaption>
</figure>

**45.Ke2 a5 46.Na3 h4 47.Nb5 Bb4 48.Nd6 h3 49.Kf2 e3+ 50.Kg1 Kf3 51.Nf5 e2 52.Nh4+ Kg3 53.Nf5+ Kf3 54.Nh4+ Ke3 55.Nf5+ Kd2 56.Kh2 e1=Q 57.Kxh3 Qe6 58.Kg4 a4 59.Kf4 a3 0-1**

With four passed pawns against a knight I was still comfortably winning. After promoting a queen and then pushing my other outside passed pawn, White resigned.

White's position started crumbling on move 15 when he went down a bishop, and it went from bad to worse on move 20 losing the exchange. Chess.com calls the rook move that lost my rook a miss rather than a mistake. I consider it a blunder. I should not be walking into forks like that, losing a rook for a pawn. The rest of my game was solid.

---

### Game 3: Loss vs UmaeTeam as White

A Scotch Game. Black grabbed the b2 pawn with **7...Qxb2** and I played **9.Rb1** to hunt the queen down.

<figure>
  <img src="{{ '/assets/images/2026-08-20/umaeteam_move18.png' | relative_url }}" alt="Position after 9...Bxc3+, White to play">
  <figcaption>After 9...Bxc3+: my rook on b1 attacks the queen and I am in check.</figcaption>
</figure>

**10.Bd2 Bxd2+ 11.Kxd2 Qe5**

**10.Kf1** was the move, and it wins the queen. The check disappears, the rook still attacks b2, and the best Black gets is **10...Qxb5 11.Rxb5**, a queen for a rook and a knight. I blocked with **10.Bd2** instead and lost a knight and a bishop for one bishop. Three moves later **13.exd5** dropped the queen to **13...Bxg4**. Mated on move 50.

---

### Game 4: Win vs benjaminarnal as White

A French Advance. I had already dropped a pawn with **12.axb5** when this position came up.

<figure>
  <img src="{{ '/assets/images/2026-08-20/benjaminarnal_move25.png' | relative_url }}" alt="Position after 13.c3, Black to play">
  <figcaption>After 13.c3: the black knight on g4 is undefended and my queen is on d1.</figcaption>
</figure>

**13...Nc4 14.Qxg4 e5 15.Bxe5 Nxe5 16.Rxe5+ Be7 17.Nf5**

Black had **Nxf2** available on moves 11, 12 and 13 and never played it. **13...Nc4** ignored the knight on g4 and **14.Qxg4** picked it up. After **16.Rxe5+** his king was stuck in the centre with the rook on h8 still at home. **17.Nf5**, **18.Qxg7+**, **19.Qxh8+** and **21.Qxa8** collected the rest, and I mated with **29.Rh6#**.

---

### Game 5: Draw vs DARKSEID_OTH as Black

A Pirc, Austrian Attack. I won the exchange in the middlegame and reached a rook endgame two pawns up.

<figure>
  <img src="{{ '/assets/images/2026-08-20/darkseid_oth_move87.png' | relative_url }}" alt="Position after 44.Rxf7, Black to play">
  <figcaption>After 44.Rxf7: my g-pawn is one square from promoting.</figcaption>
</figure>

**44...g2 45.Rg7+ Kf4 46.Rxg2**

This was the turning point. The evaluation was over seven pawns in my favour and **44...g2** levelled it. Both **44...Rg4** and **44...Kg4** keep the win. It got worse on move 52: **52...Kxe4** loses outright to the pawn race, where **52...dxe4** draws. White then returned the favour with **59.Qf4**, which let me promote with check and force the queens off. Drawn on insufficient material.

---

### Game 6: Win vs TheM4sterM1nd as Black

The best game of the session. Another Pirc Defence.

**1.e4 d6 2.d4 Nf6 3.Nc3 g6 4.Nf3 Bg7 5.e5 dxe5 6.dxe5**

<figure>
  <img src="{{ '/assets/images/2026-08-20/them4sterm1nd_move11.png' | relative_url }}" alt="Position after 6.dxe5, Black to play">
  <figcaption>After 6.dxe5: the d-file is open with the white queen on d1.</figcaption>
</figure>

**6...Qxd1+ 7.Nxd1 Ng4 8.Bc4 Nxe5 9.Nxe5 Bxe5 10.f4 Bg7 11.O-O O-O 12.Nc3 Bf5 13.Rf2**

White recaptured on e5 with the d-pawn, which opened the d-file for a queen trade with check. **7.Nxd1** put the knight back on the first rank, **7...Ng4** attacked the pawn on e5, and I won it back with **8...Nxe5**.

<figure>
  <img src="{{ '/assets/images/2026-08-20/them4sterm1nd_move25.png' | relative_url }}" alt="Position after 13.Rf2, Black to play">
  <figcaption>After 13.Rf2: the rook stands between the a1-h8 diagonal and the king on g1.</figcaption>
</figure>

**13...Nc6 14.Be3 Nd4 15.Bxd4 Bxd4 16.Nb5 Bxf2+ 17.Kxf2**

By move 13 the centre had opened up, the queens had come off, and White had placed the rook where I could pin it to the king. I routed the knight over with **13...Nc6** and **14...Nd4**. **15.Bxd4** handed me the diagonal. My bishop recaptured on d4, the rook on f2 was pinned against the king on g1, and **16...Bxf2+** won the exchange.

The engine wanted **13...Bd4** immediately, which wins the same exchange two moves earlier. **15.Nd5** was White's better try.

<figure>
  <img src="{{ '/assets/images/2026-08-20/them4sterm1nd_move33.png' | relative_url }}" alt="Position after 17.Kxf2, Black to play">
  <figcaption>After 17.Kxf2: I am up the exchange and the white king has no rook cover.</figcaption>
</figure>

**17...c6 18.Nd4 Rad8 19.Nxf5 gxf5 20.Re1**

Up the exchange, I started looking for trades.

<figure>
  <img src="{{ '/assets/images/2026-08-20/them4sterm1nd_move39.png' | relative_url }}" alt="Position after 20.Re1, Black to play">
  <figcaption>After 20.Re1: the d-file is mine and the white king sits on f2.</figcaption>
</figure>

**20...Rd2+ 21.Kf3 e6 22.g4 fxg4+ 23.Kxg4 Rxc2**

I brought the rook to the second rank and grabbed a pawn. **22.g4** opened White's own king and dragged it out to g4.

<figure>
  <img src="{{ '/assets/images/2026-08-20/them4sterm1nd_move46.png' | relative_url }}" alt="Position after 23...Rxc2, White to play">
  <figcaption>After 23...Rxc2: my rook attacks the bishop on c4.</figcaption>
</figure>

**24.Rg1 Rxc4 25.Kh5+ Kh8 26.Kh6**

White blundered with **24.Rg1**, leaving the bishop hanging. He did manage a discovered check: **25.Kh5+** stepped the king off the g-file and let the rook on g1 hit my king. I moved the king to h8.

<figure>
  <img src="{{ '/assets/images/2026-08-20/them4sterm1nd_move51.png' | relative_url }}" alt="Position after 26.Kh6, Black to play">
  <figcaption>After 26.Kh6: Rg8 is mate next move.</figcaption>
</figure>

**26...Rg8 27.Rf1**

**26.Kh6** threatened mate on g8, so I blocked the file and offered a rook trade. White declined with **27.Rf1**. Taking on g8 was forced. It was still lost, but declining walked into mate.

<figure>
  <img src="{{ '/assets/images/2026-08-20/them4sterm1nd_move53.png' | relative_url }}" alt="Position after 27.Rf1, Black to play">
  <figcaption>After 27.Rf1: the white king on h6 has nothing around it.</figcaption>
</figure>

**27...Rg6+ 28.Kh5 Rc5+ 29.Kh4 Rc2 30.Rd1 Rxh2#**

A ladder mate on the h-file was a few moves away. The rook on g6 takes the whole g-file, the other rook drops to the second rank, and **30...Rxh2#** finishes it.

<figure>
  <img src="{{ '/assets/images/2026-08-20/them4sterm1nd_move60.png' | relative_url }}" alt="Position after 30...Rxh2 checkmate">
  <figcaption>After 30...Rxh2#: the king on h4 has no square left.</figcaption>
</figure>

---

### Reflections

**What went well:**

- Both wins as Black came from the same recipe. Trade queens early, then hunt for loose pieces.
- Spotting the tactic on move 13 against clintocki. It runs three moves deep with a temporary piece sacrifice in the middle.
- The finish against TheM4sterM1nd. I saw the ladder mate coming and worked towards it instead of grabbing more material.

**What to work on:**

- The opening as White. I dropped material in the opening in all three White games. I only won the third because my opponent missed **Nxf2** three moves running.
- Checking knight squares before I move a rook. **42...Rxc4** against clintocki walked straight into **43.Nd6+**.
- Rook endgame technique. **44...g2** against DARKSEID_OTH turned a two-pawn win into a level position, and **52...Kxe4** was losing when **52...dxe4** draws.

---

*Full PGN of Game 6:*

```
1. e4 d6 2. d4 Nf6 3. Nc3 g6 4. Nf3 Bg7 5. e5 dxe5 6. dxe5 Qxd1+ 7. Nxd1 Ng4 8.
Bc4 Nxe5 9. Nxe5 Bxe5 10. f4 Bg7 11. O-O O-O 12. Nc3 Bf5 13. Rf2 Nc6 14. Be3 Nd4
15. Bxd4 Bxd4 16. Nb5 Bxf2+ 17. Kxf2 c6 18. Nd4 Rad8 19. Nxf5 gxf5 20. Re1 Rd2+
21. Kf3 e6 22. g4 fxg4+ 23. Kxg4 Rxc2 24. Rg1 Rxc4 25. Kh5+ Kh8 26. Kh6 Rg8 27.
Rf1 Rg6+ 28. Kh5 Rc5+ 29. Kh4 Rc2 30. Rd1 Rxh2# 0-1
```

---

### Further Reading

- [Checkmate with Two Rooks](https://www.chess.com/lessons/winning-the-game/checkmate-with-two-rooks)
- [Fork](https://www.chess.com/terms/fork-chess)
- [King's Fianchetto Opening](https://www.chess.com/openings/Kings-Fianchetto-Opening)
