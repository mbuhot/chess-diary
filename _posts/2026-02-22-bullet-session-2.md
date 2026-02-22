---
layout: post
title: "Bullet Session 2: Surprise Checkmates"
date: 2026-02-22 12:00:00
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
table {
  width: 100%;
  border-collapse: collapse;
  margin: 1.5em 0;
  font-size: 0.9em;
}
th, td {
  border: 1px solid #ddd;
  padding: 6px 10px;
  text-align: center;
}
th {
  background-color: #f5f5f5;
}
</style>

**Time Control:** 2 min + 1 sec increment (Bullet) | **Games:** 5 | **Record:** 3W / 2L

---

### Overview

Second bullet session. Shorter one tonight, just five games. Both losses were on time, which is still my biggest weakness in bullet. The three wins were all checkmates though, including an 11-move checkmate out of the opening that I didn't even see coming until it was on the board.

---

### All Games

<table>
<thead>
<tr><th>#</th><th></th><th>Color</th><th>Opponent</th><th>Result</th><th>Moves</th><th>My Acc</th><th>Rating</th></tr>
</thead>
<tbody>
<tr><td>1</td><td>⏳</td><td>Black</td><td>miruortigas (356)</td><td>Loss (time)</td><td>27</td><td>49.7</td><td>314</td></tr>
<tr><td>2</td><td>⚔️</td><td>Black</td><td>Kkelio (330)</td><td>Win (checkmate)</td><td>22</td><td>73.7</td><td>327</td></tr>
<tr><td>3</td><td>⏳</td><td>White</td><td>jhonnywalkerprime (359)</td><td>Loss (time)</td><td>22</td><td>60.4</td><td>316</td></tr>
<tr><td>4</td><td>⚔️</td><td>White</td><td>cha764 (292)</td><td>Win (checkmate)</td><td>28</td><td>77.0</td><td>327</td></tr>
<tr><td>5</td><td>⚔️</td><td>Black</td><td>nmeixler (341)</td><td>Win (checkmate)</td><td>11</td><td><strong>95.8</strong></td><td>339</td></tr>
</tbody>
</table>

---

### Highlight: Win vs cha764 (292) as White

<iframe id="14621631" allowtransparency="true" frameborder="0" style="width:100%;border:none;" src="https://www.chess.com/emboard?id=14621631"></iframe><script nonce="chesscom-diagram">window.addEventListener("message",e=>{e['data']&&"14621631"===e['data']['id']&&document.getElementById(`${e['data']['id']}`)&&(document.getElementById(`${e['data']['id']}`).style.height=`${e['data']['frameHeight']+37}px`)})</script>

I played the Zukertort Opening, my current favourite as White. By move 11 things were looking pretty standard. There was a trade of a knight for Black's light-squared bishop, and I took back with my queen, putting it on that file where it can potentially be dangerous. We traded some pieces on e5 and I was left with queen, knight, and two rooks. Sometimes having bishops to open up the king's castle is handy, but with a queen and two rooks I felt I could make something happen.

**1. d4 d5 2. Nf3 Nc6 3. e3 Nf6 4. Bd3 Bg4 5. O-O e6 6. h3 Bxf3 7. Qxf3 Bd6 8. Nd2 O-O 9. b3 Qe7 10. Bb2 e5 11. dxe5 Bxe5 12. Bxe5 Nxe5 13. Qe2 c5 14. f4 Nxd3 15. Qxd3 b6 16. Rf3 a6 17. Rg3 g6 18. h4 Nh5 19. Rg5**

<figure>
  <img src="{{ '/assets/images/2026-02-22/cha764_move37.png' | relative_url }}" alt="After 19. Rg5">
  <figcaption>After 19. Rg5: The rook invades on g5, pinning the g6 pawn against the king. The h-pawn is ready to advance.</figcaption>
</figure>

**19...Nf6 20. h5 b5 21. hxg6 fxg6 22. Kf2 c4 23. Qe2 cxb3 24. axb3 Kg7 25. Rh1**

I brought my king forward to f2, which let me swing the a1-rook over to the h-file. The key idea was exploiting the pin on Black's g6 pawn. After **21. hxg6 fxg6**, I had **Rg5** pinning things down and **Rh1** doubling on the h-file.

<figure>
  <img src="{{ '/assets/images/2026-02-22/cha764_move49.png' | relative_url }}" alt="After 25. Rh1">
  <figcaption>After 25. Rh1: Both rooks and the queen are aimed at the kingside. Black's king has nowhere to hide.</figcaption>
</figure>

**25...h5 26. Rhxh5 Nxh5 27. Qxh5 Kf6 28. Qxg6# 1-0**

I brought my rook up to h5, inviting Black to take it with their knight. Black took me up on the offer with **26...Nxh5**, and I recaptured with the queen: **27. Qxh5**. Black miscalculated and played **27...Kf6**, allowing **28. Qxg6#**.

<figure>
  <img src="{{ '/assets/images/2026-02-22/cha764_move55.png' | relative_url }}" alt="After 28. Qxg6#">
  <figcaption>After 28. Qxg6#: Checkmate. The queen on g6 covers all escape squares.</figcaption>
</figure>

According to the engine, this aggressive attack towards the end was actually fairly inaccurate. Stockfish rates **Rh1** and **Rh5** both as mistakes. But at this level it's working pretty well for me to keep using the strategy of throwing my major pieces in front of the king, looking for the weakness, and not being afraid to sacrifice or trade when it opens up the enemy king.

---

### Highlight: Win vs nmeixler (341) as Black

<iframe id="14621627" allowtransparency="true" frameborder="0" style="width:100%;border:none;" src="https://www.chess.com/emboard?id=14621627"></iframe><script nonce="chesscom-diagram">window.addEventListener("message",e=>{e['data']&&"14621627"===e['data']['id']&&document.getElementById(`${e['data']['id']}`)&&(document.getElementById(`${e['data']['id']}`).style.height=`${e['data']['frameHeight']+37}px`)})</script>

This game surprised even me as I was playing it. The first eight moves are a Pirc Defence, Classical Variation, where White was attacking early with a bishop and knight trying to pick off pawns near my king. I had recently brushed up on what to do about this with the Pirc/King's Indian setup, so I calmly hopped my knight up to g4, knowing I could take back the pawn that had advanced to e5 and was isolated.

**1. e4 d6 2. d4 Nf6 3. Nc3 g6 4. Nf3 Bg7 5. Bg5 O-O 6. e5 dxe5 7. dxe5 Qxd1+ 8. Nxd1 Ng4 9. Bxe7 Re8 10. Bg5 Nxe5 11. Bf4 Nxf3# 0-1**

<figure>
  <img src="{{ '/assets/images/2026-02-22/nmeixler_move18.png' | relative_url }}" alt="After 9...Re8">
  <figcaption>After 9...Re8: The rook lines up on the e-file. The bishop, rook, and knight are all focused on e5.</figcaption>
</figure>

White picked off the e7 pawn with **9. Bxe7**, and I saw a nice opportunity to line up my rook on the e-file with the bishop, pawn, and king all sitting there. I recently learned about a concept called focal squares, where multiple pieces are attacking the same square, and in this case my bishop on g7 and rook on e8 are both focused on e5. White retreated their bishop with **10. Bg5** and I took back with **10...Nxe5**. Material is equal at this point, but I have a nice threat: invite White to take my knight on e5, allowing me to recapture with my rook with check, winning the bishop on g5.

White saw through that plan and instead looked to attack my knight with **11. Bf4**. I thought: okay, I'll just grab the knight on f3, revealing a discovered check on the king. That would be a free piece for me. Little did I know that **11...Nxf3** is actually checkmate.

<figure>
  <img src="{{ '/assets/images/2026-02-22/nmeixler_move22.png' | relative_url }}" alt="After 11...Nxf3#">
  <figcaption>After 11...Nxf3#: Checkmate. Double check from the knight on f3 and the rook on e8. White's own pieces box the king in.</figcaption>
</figure>

This is a great example of attacking too early and neglecting king safety. White also failed to develop before attacking. I rarely try to learn gambits, tricks, and traps. They're fun to watch on YouTube, but as you improve your opponents will know how to defend against them, so I'd prefer to spend my time learning principles and fundamentals that will carry me through for longer. That said, it was really satisfying to get a checkmate out of the opening, partly because it was unexpected. I'll remember this one though, because I feel like it's a pretty easy mistake for people at my rating to make.

---

### Reflections

Five games is a lighter session, but the quality was there. Two time losses remind me I still need to work on my clock management. The three checkmates were all fun, especially the accidental one against nmeixler.

**What went well:**

- The Zukertort Opening is becoming a reliable choice as White. I'm getting comfortable with the middlegame plans.
- Recognising the focal squares concept in the nmeixler game and playing around e5.
- Aggressive kingside attacks with major pieces. Even if the engine disagrees, it's winning games at this rating.

**What to work on:**

- Time management. Both losses were on the clock, not the board.
- Accuracy in the attack. Throwing pieces at the king works at this level, but I should also look for the engine-approved continuations when I have time.

---

### Further Reading

- [The Most Underrated Skill in Chess: Focal Squares Explained](https://www.youtube.com/watch?v=1-G6lo942qc) by NM Robert Ramirez: The concept I used in the nmeixler game to coordinate my bishop and rook on e5.
