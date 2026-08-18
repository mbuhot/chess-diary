---
layout: post
title: "August 18 Rapid Session: Opening the Centre"
date: 2026-08-18 14:00:00 +1000
---

<style>
figure { margin: 1.5em 0 2em; }
figcaption { font-style: italic; color: #555; margin-top: 0.5em; }
table { width: 100%; border-collapse: collapse; margin: 1.5em 0; font-size: 0.9em; }
th, td { border: 1px solid #ddd; padding: 6px 10px; text-align: center; }
th { background-color: #f5f5f5; }
td.comment { text-align: left; }
</style>

**Time Control:** 10 min (Rapid) | **Games:** 5 | **Record:** 4W / 0D / 1L

---

### Overview

Five rapid games, four wins, and my rating went from 835 to 857. The theme was the centre. In three of the five games I had a Pirc setup as Black and answered with **e5**. In two of them White captured and the centre opened up, and those were the two cleanest wins of the session.

The highlight is the last game, where I scored 93.5% accuracy with no mistakes and no blunders. I played the queen trade line, White's king never reached safety, and the game ended with a discovered check on the d-file and a resignation on move 24.

---

### All Games

<table>
<tr><th>#</th><th></th><th>Color</th><th>Opponent</th><th>Result</th><th>Moves</th><th>Comment</th></tr>
<tr><td>1</td><td>⚔️</td><td>Black</td><td>ofek4587 (822)</td><td>1-0</td><td>32</td><td class="comment">Loss. Left my bishop on e4 in front of White's queen and fell apart from there.</td></tr>
<tr><td>2</td><td>🏳️</td><td>White</td><td>supremo_kiero (829)</td><td>1-0</td><td>32</td><td class="comment"><strong>Comeback.</strong> Down a bishop after 21.Bb7, then 31.Qxf7+ frightened his king off the diagonal and won his queen.</td></tr>
<tr><td>3</td><td>🏳️</td><td>Black</td><td>EdwinPro69 (814)</td><td>0-1</td><td>17</td><td class="comment">Same e5 break as the last game. 10...Qh4+ and 11...Qxe4 collected a knight, then 12.b3 dropped a rook.</td></tr>
<tr><td>4</td><td>🏳️</td><td>White</td><td>Mufaro_Sibanda (813)</td><td>1-0</td><td>51</td><td class="comment">Bishop and queen battery on h7, then 23.Bg6+ skewered the king to the rook on e8.</td></tr>
<tr><td>5</td><td>🏳️</td><td>Black</td><td>Kuchura_Victor (845)</td><td>0-1</td><td>24</td><td class="comment"><strong>Best game.</strong> 93.5% accuracy. Queen trade, White's king stuck in the centre, discovered check on the d-file.</td></tr>
</table>

---

### Game 1: Loss vs ofek4587 (822) as Black

<figure>
  <img src="{{ '/assets/images/2026-08-18/ofek4587_move29.png' | relative_url }}" alt="Position after 15.Qxe3, Black to play">
  <figcaption>After 15.Qxe3: the bishop on e4 sits directly in front of the white queen.</figcaption>
</figure>

**15...Rc8 16.Qxe4 f5 17.Qd5+**

I played this one quite poorly. The bishop went to e4 on move 12, White answered **13.Qe2** to line the queen up on the e-file, and once the minor pieces came off on e3 the bishop was attacked with nothing defending it. Instead of moving it I played **15...Rc8**. Stockfish had me better by three and a half pawns before that move and four pawns worse after it. From there it fell apart: the queen came to d5 with check, my pawns started dropping, and White mated on g5 on move 32.

---

### Game 2: Win vs supremo_kiero (829) as White

<figure>
  <img src="{{ '/assets/images/2026-08-18/supremo_kiero_move60.png' | relative_url }}" alt="Position after 30...Qxa2, White to play">
  <figcaption>After 30...Qxa2: the black queen has left the kingside and the knight on d6 covers f7.</figcaption>
</figure>

**31.Qxf7+ Kh7 32.Qxa2**

I was down a piece and looking like I was going to lose, so I had to try for some crazy counterplay, and it worked. **31.Qxf7+** was the threatening move. The knight on d6 covers f7, so the king could not take, but the queen on a2 was on the same diagonal and could. He was scared into a defensive retreat with **31...Kh7** instead, not realising the recapture was there. That left his own queen hanging on a2, I played **32.Qxa2**, and he resigned immediately.

The main mistake I made in that game was hanging the bishop on b7. I must have calculated the move order wrong. If Black takes the bishop first I come out an exchange up, but if Black takes the rook first he is up a bishop, which is exactly what happened after **21...Rxd2 22.Rxd2 Qxb7**. Rather than playing the bishop to b7 I needed to trigger the rook exchange myself and play on a pawn up.

---

### Game 3: Win vs EdwinPro69 (814) as Black

<figure>
  <img src="{{ '/assets/images/2026-08-18/edwinpro69_move19.png' | relative_url }}" alt="Position after 10.Bc4, Black to play">
  <figcaption>After 10.Bc4: the knight on e4 has no defender and h4 is open to my queen.</figcaption>
</figure>

**10...Qh4+ 11.Kf1 Qxe4 12.b3 Bxa1**

White spent the opening pushing pawns, **2.d4**, **4.d5** and **5.f4**, which gave me a lead in development. Then I got the same central break I play in the last game of this session: **6...e5 7.fxe5 dxe5 8.Nxe5 Nxe4**. This opponent recaptured with **9.Nxe4**, which is the recapture Stockfish wants, and after **9...Bxe5** the position was only about a pawn in my favour.

**10.Bc4** was the move that lost it. It left the knight on e4 undefended and gave my queen the check on h4. White answered **11.Kf1**, and **11...Qxe4** picked up the knight. He then played **12.b3**, hanging the rook on a1 to my bishop on the long diagonal. It was cleanup duty from there, and he resigned on move 17.

---

### Game 4: Win vs Mufaro_Sibanda (813) as White

<figure>
  <img src="{{ '/assets/images/2026-08-18/mufaro_sibanda_move44.png' | relative_url }}" alt="Position after 22...Kf7, White to play">
  <figcaption>After 22...Kf7: the king and the rook on e8 share the h5-e8 diagonal.</figcaption>
</figure>

**23.Bg6+ Ke7 24.Bxe8 Kxe8 25.Rg8+**

Black also spent time on pawn moves in the opening but did get the king castled. As soon as it was there I set up the bishop and queen battery pointing at h7 with **10.Qe2** and **12.Qe4**, threatening mate. Black pushed the pawns in front of the king to stop it, and I grabbed one with **13.Bxh6**. Then I pushed my own h-pawn to attack g6.

The fatal mistake was **22...Kf7**, putting the king on the same diagonal as the rook on e8. **23.Bg6+** skewered them and won the exchange, and his other rook was boxed in on a8 doing nothing. In the end I pushed the passed pawn down the g-file, which forced him to give up his bishop for it, then activated my king and cleaned up his queenside pawns. He resigned on move 51 with mate in three on the board.

---

### Game 5: Win vs Kuchura_Victor (845) as Black

This was the best game of the session for me. I had a feeling my opponent didn't quite know how to play against the Pirc Defense.

**1.e4 d6 2.Nc3 Nf6 3.Bc4 g6 4.d3 Bg7 5.f4 O-O 6.Nf3**

<figure>
  <img src="{{ '/assets/images/2026-08-18/kuchura_victor_move11.png' | relative_url }}" alt="Position after 6.Nf3, Black to play">
  <figcaption>After 6.Nf3: a standard Pirc setup with White's pawn on f4.</figcaption>
</figure>

**6...e5 7.fxe5 dxe5 8.Nxe5**

On move six I pushed **6...e5**. At first glance the e5 pawn is under-defended: it is attacked twice, by the f4 pawn and the knight on f3, and directly defended once by the d6 pawn. Stockfish calls the push an inaccuracy and prefers **6...c5**, but opening the centre is the whole point of how I want to play this position, so I will wear that one as a badge of honour.

<figure>
  <img src="{{ '/assets/images/2026-08-18/kuchura_victor_move15.png' | relative_url }}" alt="Position after 8.Nxe5, Black to play">
  <figcaption>After 8.Nxe5: White is a pawn up and my knight on f6 is loose.</figcaption>
</figure>

**8...Nxe4 9.dxe4 Qxd1+ 10.Kxd1 Bxe5**

This is the line I have been playing. I sacrifice the knight to take the pawn on e4, and then recapture White's knight on e5 with the bishop from g7. In games like this one where White hasn't castled yet, it gives Black a great position with a nice open centre where the white king can be attacked by the queen and the rook.

I chose the variation that triggers the queen trade early, because it forces White to either put the knight back on d1, wasting time, or move the king and lose the right to castle. He took with **10.Kxd1**. That was already the wrong choice: Stockfish rates **10.Nxd1** at a quarter of a pawn and the king recapture at nearly a full pawn for Black.

<figure>
  <img src="{{ '/assets/images/2026-08-18/kuchura_victor_move20.png' | relative_url }}" alt="Position after 10...Bxe5, White to play">
  <figcaption>After 10...Bxe5: material is level, the white king is on d1 and cannot castle.</figcaption>
</figure>

**11.Bd2**

<figure>
  <img src="{{ '/assets/images/2026-08-18/kuchura_victor_move21.png' | relative_url }}" alt="Position after 11.Bd2, Black to play">
  <figcaption>After 11.Bd2: White develops the bishop and connects the rooks.</figcaption>
</figure>

**11...Bg4+ 12.Be2 Bxe2+ 13.Kxe2 Nc6**

I wasn't ahead in material, but I felt like I had the better position, so I was comfortable trading the light-squared bishops. The trade also pulled the king out to e2, further into the centre.

**14.Nd5**

<figure>
  <img src="{{ '/assets/images/2026-08-18/kuchura_victor_move27.png' | relative_url }}" alt="Position after 14.Nd5, Black to play">
  <figcaption>After 14.Nd5: the knight jumps into the middle and the d-file is still open.</figcaption>
</figure>

**14...Rad8 15.c4 Nd4+ 16.Kd3 c6**

**15.c4** was White's first big mistake, and it cost about two pawns of evaluation. It gave me **15...Nd4+**, hopping the knight in with check, safe because the c-pawn had left c2. **16.Kd3** stepped the king onto the file my rook was already sitting on, and **16...c6** kicked the knight on d5.

<figure>
  <img src="{{ '/assets/images/2026-08-18/kuchura_victor_move32.png' | relative_url }}" alt="Position after 16...c6, White to play">
  <figcaption>After 16...c6: the white king on d3 shares the d-file with my rook on d8.</figcaption>
</figure>

**17.Nc3**

<figure>
  <img src="{{ '/assets/images/2026-08-18/kuchura_victor_move33.png' | relative_url }}" alt="Position after 17.Nc3, Black to play">
  <figcaption>After 17.Nc3: only my knight on d4 blocks the d-file.</figcaption>
</figure>

**17...Nf3+ 18.Ke3 Nxd2**

**17.Nc3** was the second mistake, and it allowed the discovered check. Hopping the knight from d4 to f3 opened the d-file, and my rook on d8 gave check to the king on d3. Behind the king on d2 stood the bishop, skewered.

White could have blocked the check with the knight, which would have meant sacrificing it. Like a lot of players in my rating range, he moved the king instead with **18.Ke3**, and **18...Nxd2** took the bishop off. The d2 square was safely guarded by my rook on d8.

<figure>
  <img src="{{ '/assets/images/2026-08-18/kuchura_victor_move36.png' | relative_url }}" alt="Position after 18...Nxd2, White to play">
  <figcaption>After 18...Nxd2: the bishop is gone and the knight sits next to the king.</figcaption>
</figure>

**19.Rad1**

<figure>
  <img src="{{ '/assets/images/2026-08-18/kuchura_victor_move37.png' | relative_url }}" alt="Position after 19.Rad1, Black to play">
  <figcaption>After 19.Rad1: my knight on d2 is pinned to the rook on d8.</figcaption>
</figure>

**19...Nxc4+ 20.Kf3 Nxb2 21.Rc1**

White tried to pin my knight to my rook, but the knight left the pin with check on **19...Nxc4+**. Two moves later it took the b2 pawn as well.

<figure>
  <img src="{{ '/assets/images/2026-08-18/kuchura_victor_move41.png' | relative_url }}" alt="Position after 21.Rc1, Black to play">
  <figcaption>After 21.Rc1: my bishop on e5 and the knight on c3 share the a1-h8 diagonal.</figcaption>
</figure>

**21...Rd3+ 22.Ke2 Bxc3 23.Rhd1 Rxd1 24.Rxd1**

My dark-squared bishop collected the knight on c3. If White recaptures with the rook he is down a further exchange, so instead he brought the other rook in from h1 with **23.Rhd1**. I was more than happy to trade. After **24.Rxd1** I can take with the knight, and if the king recaptures I am up a rook, a bishop and two pawns. He resigned before I could play it.

<figure>
  <img src="{{ '/assets/images/2026-08-18/kuchura_victor_move47.png' | relative_url }}" alt="Position after 24.Rxd1, Black to play">
  <figcaption>After 24.Rxd1: 24...Nxd1 is coming and White resigned.</figcaption>
</figure>

93.5% accuracy for me against 78.3% for my opponent, with a game rating of 1650 versus 1300. Three great moves, ten best moves, no mistakes and no blunders. The only move of mine the engine dislikes is **6...e5**. White was given four mistakes.

If White wanted to avoid the queen trade he needed to recapture on e4 with the knight from c3, **9.Nxe4**. That keeps the pawn on d3 and leaves White with well placed pieces in the centre, worth about a pawn. The last mistake the engine flags is **21.Rc1**. The evaluation there is already around seven pawns for Black, so perhaps everything was losing, but if he wanted to hang on a little longer he could have traded the rooks, moved the knight to safety, and finally activated the rook on h1.

---

### Reflections

**What went well:**

- Playing the opening as Black and triggering the central trades early. I have normally been trying to reach a locked centre because a kingside pawn storm is fun to play, but it is very tricky to play well. Simply opening the centre and preventing the opponent from castling is a nice aggressive way to handle it.
- Games 3, 4 and 5 all felt solid. I made well considered moves and kept up the pressure until my opponent made the mistake.
- The blunders were not too bad overall. I dropped a bishop in game 1 and another in game 2, and in the second case I still made the comeback.

**What to work on:**

- Move order when a piece is under attack. The bishop on b7 in game 2 came from calculating the order wrong. Triggering the rook exchange first leaves me a pawn up instead of a bishop down.
- Noticing when my own piece is undefended in front of an enemy queen. In game 1 White put the queen behind my bishop on move 13 and collected it on move 16, and I played **15...Rc8** as if nothing was happening.

---

*Full PGN of Game 5:*

```
1. e4 d6 2. Nc3 Nf6 3. Bc4 g6 4. d3 Bg7 5. f4 O-O 6. Nf3 e5 7. fxe5 dxe5 8. Nxe5
Nxe4 9. dxe4 Qxd1+ 10. Kxd1 Bxe5 11. Bd2 Bg4+ 12. Be2 Bxe2+ 13. Kxe2 Nc6 14. Nd5
Rad8 15. c4 Nd4+ 16. Kd3 c6 17. Nc3 Nf3+ 18. Ke3 Nxd2 19. Rad1 Nxc4+ 20. Kf3
Nxb2 21. Rc1 Rd3+ 22. Ke2 Bxc3 23. Rhd1 Rxd1 24. Rxd1 0-1
```

---

### Further Reading

- [Pirc Defense](https://www.chess.com/openings/Pirc-Defense)
- [Discovered Check](https://www.chess.com/terms/discovered-check-chess)
- [Skewer](https://www.chess.com/terms/skewer-chess)
