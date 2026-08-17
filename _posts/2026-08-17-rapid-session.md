---
layout: post
title: "August 17 Rapid Session: Attacking Chess"
date: 2026-08-17 12:00:00 +1000
---

<style>
figure { margin: 1.5em 0 2em; }
figcaption { font-style: italic; color: #555; margin-top: 0.5em; }
table { width: 100%; border-collapse: collapse; margin: 1.5em 0; font-size: 0.9em; }
th, td { border: 1px solid #ddd; padding: 6px 10px; text-align: center; }
th { background-color: #f5f5f5; }
td.comment { text-align: left; }
</style>

**Time Control:** 10 min (Rapid) | **Games:** 6 | **Record:** 5W / 0D / 1L

---

### Overview

Six rapid games, five wins, and my rating went from 811 to 835. The theme running through the session was attacking chess, especially with the white pieces: quick development, taking space in the centre, and being willing to give up a piece to tear open the king.

The wins came from the initiative. Most of these games were around 70% accuracy, and Stockfish confirms it: the evaluation swung wildly in almost every game. Three of the wins came from positions where I was clearly worse or outright lost, and in the maguin710 game my opponent had a forced mate in 10 on the board and missed it twice. Keeping pieces pointed at the enemy king turned out to be worth more than avoiding mistakes.

---

### All Games

<table>
<tr><th>#</th><th></th><th>Color</th><th>Opponent</th><th>Result</th><th>Moves</th><th>Comment</th></tr>
<tr><td>1</td><td>⚔️</td><td>White</td><td>Fabioar79 (811)</td><td>1-0</td><td>25</td><td class="comment">Gave up a bishop on f6 to strip the king, won a rook on g8, mated with Qxg7#.</td></tr>
<tr><td>2</td><td>⚔️</td><td>Black</td><td>maguin710 (773)</td><td>0-1</td><td>47</td><td class="comment"><strong>Comeback.</strong> My Bxh2+ backfired and handed White mate in 10; White missed it twice and I mated on h2 instead.</td></tr>
<tr><td>3</td><td>🏳️</td><td>Black</td><td>islapunk (835)</td><td>0-1</td><td>22</td><td class="comment"><strong>Comeback.</strong> 10...f6 left my queen there for the taking on the a2-g8 diagonal, White missed it twice, then Qxe5+ collected the a1 rook.</td></tr>
<tr><td>4</td><td>⚔️</td><td>White</td><td>ElijahWinter (847)</td><td>0-1</td><td>26</td><td class="comment">Loss. Up around six pawns for twenty moves, then 23.f3 and 24.g4 opened my own king and I was mated on g2.</td></tr>
<tr><td>5</td><td>🏳️</td><td>White</td><td>2Tou (790)</td><td>1-0</td><td>27</td><td class="comment">Space with e5, wrecked the kingside with Bxh6, then a rook lift to h4 harvested h6, h7 and a8.</td></tr>
<tr><td>6</td><td>⚔️</td><td>Black</td><td>Silkysmooth31 (827)</td><td>0-1</td><td>54</td><td class="comment"><strong>Comeback.</strong> Dropped a bishop and was losing until 28.Qc4, then a king hunt to g5 and a winning rook endgame.</td></tr>
</table>

---

### Game 1: Win vs Fabioar79 (811) as White

<figure>
  <img src="{{ '/assets/images/2026-08-17/fabioar79_move18.png' | relative_url }}" alt="Position after 9...f6, White to play">
  <figcaption>After 9...f6: the bishop on g5 is attacked and Black's king is still in the centre.</figcaption>
</figure>

**10.Bxf6 gxf6 11.Qxf6 Rg8 12.Nd5 Bg7 13.Qe6 a4 14.O-O-O Ra5 15.Bxc6+ bxc6 16.Nxe7 Qxe7 17.Qxg8+**

Black handed me the bishop pair on move 4 with **4...Bxf3**, and after **5.Qxf3** I had a queen on f3 pointing at f7 while he spent moves on **5...a5** and **6...c6**. When **9...f6** hit my bishop I took it and followed with **11.Qxf6**, giving up the bishop to open the f-file and the diagonals around a king still sitting on e8. Stockfish rates the capture as a blunder that hands Black the advantage, and it says **12...Nxd5** was the refutation. Instead Black played **12...Bg7**, and the decisive moment was **13...a4**: a rook pawn push on the far side of the board while my queen sat on e6 and every one of my pieces was aimed at his king. Two moves later **15.Bxc6+** and **16.Nxe7** stripped the defenders and **17.Qxg8+** won the rook. The finish was **23.Rhg1** hitting the queen on g2, **24.Rxg2** and **25.Qxg7#**.

---

### Game 2: Win vs maguin710 (773) as Black

<figure>
  <img src="{{ '/assets/images/2026-08-17/maguin710_move36.png' | relative_url }}" alt="Position after 18...Be6, White to play with mate in 10 available">
  <figcaption>After 18...Be6: White has a forced mate in 10 starting with 19.Bb2+.</figcaption>
</figure>

**19.Bb2+ Kg8 20.Rg7+ Kf8 21.Qxb7 Nd7 22.Rf1+ Nf6 23.Rxf6+ Kxg7**

White gave me a pawn with **3.d5 Nxe4** and another with **5.f4 Nxd5**, so I was two pawns up out of the opening with a normal fianchetto setup. He kept throwing material at my king anyway, **13.Bxg6 fxg6** and then **16.Rf7**, and I decided to answer in kind with **16...Bxh2+**. That one was a mistake. After **17.Kxh2 Qh4+ 18.Kg1 Be6** the engine has White mating in 10, starting with **19.Bb2+**. He found the first two moves of it, then played **21.Qxb7** when **21.Rf1+** was mate in seven. He got a second chance after **26...Qxe2** and played **27.Bc1+** instead of **27.Qf4+**. Once **29.Rf2** let my queen in with **29...Qd1+** I was back on top, took the c4 pawn with **31...Bxc4**, and traded queens with **33...Qxf4+**. The rooks came off two moves later and left me a rook and bishop against his bishop: the c-pawn, the a-pawn and finally the g-pawn all fell, and **47...Rh2#** finished it.

---

### Game 3: Win vs islapunk (835) as Black

<figure>
  <img src="{{ '/assets/images/2026-08-17/islapunk_move25.png' | relative_url }}" alt="Position after 13.Ng5, Black to play">
  <figcaption>After 13.Ng5: the knight hits f7 and h7, and the a1 rook is bare on the long diagonal.</figcaption>
</figure>

**13...fxg5 14.Bxe5 Qxe5+ 15.Qe2 Qxa1+ 16.Qd1 Qxd1+ 17.Kxd1**

A Pirc setup where I castled early and let White push **6.e5**. My **10...f6** was the worst move of my session: it opened the a2-g8 diagonal and **11.Bc4** would have won my queen on d5 on the spot. White played **11.Bf4** instead, then missed **12.Bc4** as well, and after **12...Nxe5** he went for **13.Ng5**. That was the decisive moment. His knight left f3 while his rook on a1 was undefended on the a1-h8 diagonal with my bishop on g7 and my queen able to reach e5 with check. **14...Qxe5+** picked up the rook two moves later, queens came off, and a rook and a bishop up I traded down until he resigned after **22...Rxe8**.

---

### Game 4: Loss vs ElijahWinter (847) as White

<figure>
  <img src="{{ '/assets/images/2026-08-17/elijahwinter_move44.png' | relative_url }}" alt="Position after 22...Rg8, White to play">
  <figcaption>After 22...Rg8: White is winning by about six pawns with the black king stuck on e8.</figcaption>
</figure>

**23.f3 Qe2 24.g4 Qxf3 25.Rd2 Rxg4+ 26.Rg2 Qxg2#**

The one loss, and it was the game I was winning most comfortably. Black brought the queen out on move 3 and then to b4, and by move 10 the engine had me up nearly ten pawns after **10.dxc6 Rb8**. I collected the d-pawn and f-pawn with **15.Nxf6+ gxf6 16.Qxf6** and **17.Qxd6**, and I was still up six pawns at move 22 with his king stranded on e8. Then I pushed the pawns in front of my own king. **23.f3** let his queen into e2, and **24.g4** opened the g-file straight onto my king with his rook already on g8. **24...Qxf3** and **25...Rxg4+** were both forced wins from there, and **26...Qxg2#** ended it. Everything I did to his king in the other five games, I did to my own here in two moves.

---

### Game 5: Win vs 2Tou (790) as White

<figure>
  <img src="{{ '/assets/images/2026-08-17/2tou_move32.png' | relative_url }}" alt="Position after 16...Bc7, White to play">
  <figcaption>After 16...Bc7: Black's kingside pawns are shattered and the h-file is the target.</figcaption>
</figure>

**17.Re4 Qd8 18.Rh4 d6 19.Rxh6 dxe5 20.Rxh7 Qf6 21.Qd2 Bf5 22.Qh6+ Qxh6 23.Rxh6 Bxd3 24.Rh8+ Ke7 25.Rxa8**

This was the cleanest attacking game of the six. I took the centre with **8.e5**, which chased the knight to g4 and then h6, and **11.Bxh6 gxh6** shattered the pawns in front of his king. **13.Nf6+** forced the king to f8 and **14.Nxe8** won the exchange. The decisive idea was the rook lift: **16.Re1**, **17.Re4** and **18.Rh4**, swinging the rook across to the file where his pawns were broken. **19.Rxh6** and **20.Rxh7** ate both of them, the queen trade on h6 changed nothing, and **24.Rh8+** followed by **25.Rxa8** picked up the rook in the corner. He resigned after **27.Re1**.

---

### Game 6: Win vs Silkysmooth31 (827) as Black

<figure>
  <img src="{{ '/assets/images/2026-08-17/silkysmooth31_move55.png' | relative_url }}" alt="Position after 28.Qc4, Black to play">
  <figcaption>After 28.Qc4: f2 is loose and the white king has no cover.</figcaption>
</figure>

**28...Qxf2+ 29.Kh3 Qh2+ 30.Kg4 f5+ 31.Kg5 Qxg3+ 32.Rg4 Qxg4+ 33.Qxg4 fxg4**

White opened **1.h4** and **2.Rh3**, so I developed normally and took the centre with **6...e5**. My queen went pawn hunting with **13...Qxh4** and **14...Qxe4+**, then **17...Qf4** dropped my bishop to **18.Bxg4**, which left White a piece up for two pawns and better for the next ten moves. **28.Qc4** was the decisive moment, taking the queen away from his own king with my rook already on d2. **28...Qxf2+** started a king hunt that dragged him from g2 to g5 in four moves, and the engine had mate in four at the end of it with **32...Qe3+**. I took the rook with **32...Qxg4+** instead, which traded queens and left me the exchange and three pawns up. That was still winning: my rooks ate the queenside, the g-pawn ran, and **54...Rg1#** was mate.

---

### Reflections

**What went well:**

- Sacrificing to open the king. **10.Bxf6** against Fabioar79 gave up a bishop to strip the pawns off his king, and **11.Bxh6** against 2Tou broke the kingside pawns for the same reason. Both games were over quickly afterwards.
- The rook lift. **17.Re4** and **18.Rh4** in the 2Tou game is the pattern I want to repeat: break the pawns, then bring the rook to the file where the holes are.
- Playing on in bad positions. Three of the five wins came after the engine had me losing: a forced mate for maguin710, a queen for islapunk, and a piece up for Silkysmooth31.
- Development and space in the centre. In every white game I had my pieces out and a pawn on e5 or d5 while my opponent was still shuffling.

**What to work on:**

- Finishing when mate is on the board. **32...Qe3+** was mate in four against Silkysmooth31 and I took a rook instead. It still won, and it cost me twenty extra moves.
- Pawn moves in front of my own king. **23.f3** and **24.g4** against ElijahWinter threw away a six pawn advantage in two moves. When I am that far ahead there is no reason to touch the pawns around my king.
- Choosing which sacrifice to play. **16...Bxh2+** against maguin710 was the one that handed the opponent a forced mate. The attacking instinct is working; the calculation behind it needs to catch up.

---

### Further Reading

- [Sacrifice](https://www.chess.com/terms/chess-sacrifice)
- [Rook Lift](https://www.chess.com/terms/rook-lift-chess)
- [What Is The Initiative?](https://www.chess.com/article/view/what-is-the-initiative)
