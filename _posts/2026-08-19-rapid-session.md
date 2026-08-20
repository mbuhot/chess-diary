---
layout: post
title: "August 19 Rapid Session: The Long Diagonal"
date: 2026-08-19 14:00:00 +1000
---

<style>
figure { margin: 1.5em 0 2em; }
figcaption { font-style: italic; color: #555; margin-top: 0.5em; }
table { width: 100%; border-collapse: collapse; margin: 1.5em 0; font-size: 0.9em; }
th, td { border: 1px solid #ddd; padding: 6px 10px; text-align: center; }
th { background-color: #f5f5f5; }
td.comment { text-align: left; }
</style>

**Time Control:** 10 min (Rapid) | **Games:** 10 | **Record:** 6W / 2D / 2L

---

### Overview

Ten rapid games. Six wins, two draws and two losses, and my rating went from 847 up to 903.

Both draws were stalemates, in opposite directions. In game 3 I was the one winning and stalemated my opponent. In game 9 I was nine pawns down and my opponent stalemated me. One of those I earned and one I did not.

The highlight is game 5, where I scored the highest accuracy of the session over a full game. It was a Pirc, I got the f-pawn break in, and the whole game turned on a battery pointing down the long diagonal at White's rook on a1.

---

### All Games

<table>
<tr><th>#</th><th></th><th>Colour</th><th>Opponent</th><th>Result</th><th>Moves</th><th>My Acc</th><th>Comment</th></tr>
<tr><td>1</td><td>⚔️</td><td>White</td><td>PinoTryhard (872)</td><td>0-1</td><td>24</td><td>64.2</td><td class="comment">Loss. Five blunders after move 14. Mated on e1.</td></tr>
<tr><td>2</td><td>🏳️</td><td>White</td><td>ARRahamed (815)</td><td>1-0</td><td>39</td><td>88.0</td><td class="comment">Queen trade on move 6, then a long grind with the c-pawn.</td></tr>
<tr><td>3</td><td>🤝</td><td>Black</td><td>AronSzucs (842)</td><td>½-½</td><td>44</td><td>78.4</td><td class="comment">Draw. Queen and rook against king and pawn, and I stalemated him with <strong>44...Qxh7</strong>.</td></tr>
<tr><td>4</td><td>⚔️</td><td>Black</td><td>Knqz33cs (825)</td><td>0-1</td><td>52</td><td>82.0</td><td class="comment">Win. A long queen chase across the board, mate on a3.</td></tr>
<tr><td>5</td><td>🏳️</td><td>Black</td><td>Ajubhai10 (835)</td><td>0-1</td><td>30</td><td><strong>91.4</strong></td><td class="comment"><strong>Best game.</strong> Pirc, f5 break, and the battery on the long diagonal won the exchange.</td></tr>
<tr><td>6</td><td>⚔️</td><td>White</td><td>balbaidsrf (841)</td><td>1-0</td><td>16</td><td>90.8</td><td class="comment">Win. <strong>14.Rxh6</strong> and mate on h7 two moves later.</td></tr>
<tr><td>7</td><td>🏳️</td><td>White</td><td>Xanqoja (855)</td><td>1-0</td><td>12</td><td>95.3</td><td class="comment">Win. Twelve moves, no move flagged, opponent abandoned.</td></tr>
<tr><td>8</td><td>🏳️</td><td>Black</td><td>KoK1n1NamMo (895)</td><td>0-1</td><td>27</td><td>64.7</td><td class="comment">Win. Two blunders early, then <strong>13...Nxd4</strong> and the rooks took over.</td></tr>
<tr><td>9</td><td>🤝</td><td>White</td><td>jackjames90123 (917)</td><td>½-½</td><td>46</td><td>89.7</td><td class="comment">Draw. Lost from move 12, saved by his stalemate on move 46.</td></tr>
<tr><td>10</td><td>🏳️</td><td>White</td><td>CalinRotaru (867)</td><td>1-0</td><td>12</td><td>84.9</td><td class="comment">Win. Bishop collected the rook on a8 and he resigned.</td></tr>
</table>

Accuracy is Stockfish 16.1 at depth 14 through python-chess, using chess.com's win-percentage formula. Chess.com weights by position volatility, so its own numbers differ by a few points.

---

### Highlight: Win vs Ajubhai10 (835) as Black

This was a Pirc Defense, and White chose to lock the centre with **6.d5**.

**1.e4 d6 2.d4 Nf6 3.Nc3 g6 4.Nf3 Bg7 5.Bd3 e5 6.d5**

<figure>
  <img src="{{ '/assets/images/2026-08-19/ajubhai10_move12.png' | relative_url }}" alt="Position after 6.d5, Black to play">
  <figcaption>After 6.d5: pawns locked on e4/d5 against d6/e5.</figcaption>
</figure>

**6...O-O 7.Bg5 h6 8.Bh4 g5 9.Bg3**

White played **7.Bg5**, which I kicked with **7...h6**. He retreated with **8.Bh4** and I kept pressuring with **8...g5**.

<figure>
  <img src="{{ '/assets/images/2026-08-19/ajubhai10_move18.png' | relative_url }}" alt="Position after 9.Bg3, Black to play">
  <figcaption>After 9.Bg3: the bishop is parked on g3 behind the e5 pawn.</figcaption>
</figure>

**9...Ng4 10.O-O f5 11.exf5 Bxf5 12.Bxf5 Rxf5**

Then I went for the thematic **10...f5** pawn break and we traded the light-squared bishops.

<figure>
  <img src="{{ '/assets/images/2026-08-19/ajubhai10_move24.png' | relative_url }}" alt="Position after 12...Rxf5, White to play">
  <figcaption>After 12...Rxf5: the rook lands on the half-open f-file.</figcaption>
</figure>

**13.Ne4 Nd7 14.c4 Ndf6 15.Nfd2 Nxe4 16.Nxe4 Nf6 17.Nxf6+ Qxf6 18.b4 Rf8**

Some knight manoeuvring and trades, and I ended up with a triple battery of rook, queen and rook on the f-file.

<figure>
  <img src="{{ '/assets/images/2026-08-19/ajubhai10_move36.png' | relative_url }}" alt="Position after 18...Rf8, White to play">
  <figcaption>After 18...Rf8: rook on f5, queen on f6 and rook on f8.</figcaption>
</figure>

**19.f3 e4 20.c5**

Here I spotted a tactic. Pushing **19...e4** puts my queen on double duty: it stays on the f-file and it forms a second battery with the bishop on g7, aimed at White's rook on a1.

<figure>
  <img src="{{ '/assets/images/2026-08-19/ajubhai10_move40.png' | relative_url }}" alt="Position after 20.c5, Black to play">
  <figcaption>After 20.c5: the a1-h8 diagonal is clear from g7 to a1.</figcaption>
</figure>

**20...Qxa1 21.Qxa1 Bxa1 22.Rxa1**

White didn't see the plan. I temporarily sacrificed the queen for the rook on a1, he recaptured with his queen, and I recaptured with the bishop. That left me up an exchange.

<figure>
  <img src="{{ '/assets/images/2026-08-19/ajubhai10_move44.png' | relative_url }}" alt="Position after 22.Rxa1, Black to play">
  <figcaption>After 22.Rxa1: two rooks against a rook, and my e-pawn is on f3.</figcaption>
</figure>

**22...exf3 23.cxd6 f2+ 24.Bxf2 Rxf2 25.dxc7**

I took on f3 and pushed **23...f2+**. The only other legal king moves let the pawn queen, so White gave up the bishop with **24.Bxf2**, and after **24...Rxf2** I was up a rook.

White tried to get some counterplay with **25.dxc7**, but I had the back rank covered with the rook on f8.

<figure>
  <img src="{{ '/assets/images/2026-08-19/ajubhai10_move50.png' | relative_url }}" alt="Position after 25.dxc7, Black to play">
  <figcaption>After 25.dxc7: the c8 promotion square is covered by the rook on f8.</figcaption>
</figure>

**25...Rd2 26.Rc1 Rc8 27.d6 Rxd6 28.a4 Rd7 29.b5 Rdxc7**

I collected the d and c pawns with my rooks and formed a battery against White's rook on c1.

<figure>
  <img src="{{ '/assets/images/2026-08-19/ajubhai10_move58.png' | relative_url }}" alt="Position after 29...Rdxc7, White to play">
  <figcaption>After 29...Rdxc7: rooks doubled on c7 and c8 against the rook on c1.</figcaption>
</figure>

**30.a5 Rxc1+**

White blundered with **30.a5** and I took the rook for free. He resigned.

<figure>
  <img src="{{ '/assets/images/2026-08-19/ajubhai10_move60.png' | relative_url }}" alt="Position after 30...Rxc1+, White to play">
  <figcaption>After 30...Rxc1+: two rooks against four pawns.</figcaption>
</figure>

---

### Engine Review

90.7% accuracy for me against 85.1% for White at depth 20. Sixteen of my thirty moves were the engine's first choice, with one mistake, three inaccuracies and no blunders.

The mistake was **9...Ng4**, and it cost about two pawns of evaluation. White's answer is **10.h4**, attacking the pawn on g5. If I take with **10...gxh4** then **11.Bxh4** gains a tempo against my queen on d8.

<figure>
  <img src="{{ '/assets/images/2026-08-19/engine-line-h4-tempo.gif' | relative_url }}" alt="Animated line: 10.h4 gxh4 11.Bxh4">
  <figcaption>10.h4 gxh4 11.Bxh4, hitting the queen on d8.</figcaption>
</figure>

If instead I play another developing move and allow **11.hxg5 hxg5**, the g-pawn is weak and the h-file is open for the white rook.

<figure>
  <img src="{{ '/assets/images/2026-08-19/engine-line-h4-hfile.gif' | relative_url }}" alt="Animated line: 10.h4 Nd7 11.hxg5 hxg5 12.Qd2">
  <figcaption>10.h4 Nd7 11.hxg5 hxg5 12.Qd2, with the h-file open and the g-pawn weak.</figcaption>
</figure>

The position was pretty equal until **19.f3**, which the engine has at 0.05 before and 1.96 in my favour after. The engine's line from there is flashy but it just leaves Black better: **19...e4 20.Qe2 h5 21.Rae1 h4 22.Bf2 exf3 23.gxf3 Qc3**.

**20.c5** was the real mistake, dropping White from about two pawns down to five. There was a better way for me to play it, though. Rather than going straight for **20...Qxa1**, the stronger move is **20...Qd4+**, which leads to White giving up a bishop.

<figure>
  <img src="{{ '/assets/images/2026-08-19/engine-line-qd4.gif' | relative_url }}" alt="Animated line: 20...Qd4+ 21.Bf2 e3 22.Qxd4 Bxd4 23.Bxe3 Bxe3+ 24.Kh1">
  <figcaption>20...Qd4+ 21.Bf2 e3 22.Qxd4 Bxd4 23.Bxe3 Bxe3+ 24.Kh1.</figcaption>
</figure>

White sealed their fate with **30.a5**. The engine calls it mate in seven: a ladder mate, where White prolongs the game with a few pawn moves.

<figure>
  <img src="{{ '/assets/images/2026-08-19/engine-line-ladder-mate.gif' | relative_url }}" alt="Animated line: the mate in seven after 30...Rxc1+">
  <figcaption>31.Kf2 R8c3 32.b6 a6 33.h3 Rb1 34.Ke2 Rb2+ 35.Kd1 Rxg2 36.h4 gxh4 37.Ke1 Rc1#.</figcaption>
</figure>

---

### Reflections

**What went well:**

- The Pirc plan held up. Lock the centre, kick the bishop, play the f5 break, and take the open lines that come out of it.
- Seeing that the e-pawn push made my queen do two jobs at once. That is the move the whole game rested on.
- Covering the back rank before White got the pawn to c7, so his counterplay never started.

**What to work on:**

- Knight moves that do not have a target. **9...Ng4** gave White **10.h4** with tempo and was my only real mistake of the game.
- Taking the first winning tactic I see instead of the best one. **20...Qd4+** was half a pawn better than **20...Qxa1** and I did not look for it.

---

*Full PGN of Game 5:*

```
1. e4 d6 2. d4 Nf6 3. Nc3 g6 4. Nf3 Bg7 5. Bd3 e5 6. d5 O-O 7. Bg5 h6 8. Bh4 g5
9. Bg3 Ng4 10. O-O f5 11. exf5 Bxf5 12. Bxf5 Rxf5 13. Ne4 Nd7 14. c4 Ndf6
15. Nfd2 Nxe4 16. Nxe4 Nf6 17. Nxf6+ Qxf6 18. b4 Rf8 19. f3 e4 20. c5 Qxa1
21. Qxa1 Bxa1 22. Rxa1 exf3 23. cxd6 f2+ 24. Bxf2 Rxf2 25. dxc7 Rd2 26. Rc1 Rc8
27. d6 Rxd6 28. a4 Rd7 29. b5 Rdxc7 30. a5 Rxc1+ 0-1
```

---

### Further Reading

- [Pirc Defense](https://www.chess.com/openings/Pirc-Defense)
- [Battery](https://www.chess.com/terms/battery-chess)
- [Checkmate Patterns](https://www.chess.com/terms/checkmate-chess)
