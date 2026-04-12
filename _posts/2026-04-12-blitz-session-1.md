---
layout: post
title: "Blitz Session 1: Learning the Hard Way"
date: 2026-04-12 14:00:00 +1000
---

<style>
figure { margin: 1.5em 0 2em; }
figcaption { font-style: italic; color: #555; margin-top: 0.5em; }
table { width: 100%; border-collapse: collapse; margin: 1.5em 0; font-size: 0.9em; }
th, td { border: 1px solid #ddd; padding: 6px 10px; text-align: center; }
th { background-color: #f5f5f5; }
</style>

**Time Control:** 5 min (Blitz) | **Games:** 6 | **Record:** 3W / 0D / 3L

---

### Overview

My first blitz session on the blog. At this rating level there's generally one key moment where the tide swings for one player or the other, so for each game I've picked out the turning point. The losses all came from specific blunders I can learn from, and the wins came from spotting tactics and converting material advantages.

---

### All Games

<table>
<tr><th>#</th><th></th><th>Color</th><th>Opponent</th><th>Result</th><th>Moves</th><th>Opening</th></tr>
<tr><td>1</td><td>⚔️</td><td>White</td><td>Macvaldr (536)</td><td>0-1</td><td>26</td><td>d4 e5</td></tr>
<tr><td>2</td><td>🏳️</td><td>Black</td><td>nisash321 (529)</td><td>1-0</td><td>27</td><td>e4 d6</td></tr>
<tr><td>3</td><td>⚔️</td><td>White</td><td>Noobimpe (496)</td><td>1-0</td><td>24</td><td>Colle</td></tr>
<tr><td>4</td><td>⏳</td><td>Black</td><td>Ucupppppppo (514)</td><td>1-0</td><td>27</td><td>e4 d6 KID</td></tr>
<tr><td>5</td><td>⚔️</td><td>White</td><td>Fredly65 (477)</td><td>1-0</td><td>36</td><td>Colle</td></tr>
<tr><td>6</td><td>⏳</td><td>White</td><td>jerm5006 (484)</td><td>1-0</td><td>41</td><td>d4 d5</td></tr>
</table>

---

### Game 1: Loss vs Macvaldr (536) as White

<iframe id="14889943" allowtransparency="true" frameborder="0" style="width:100%;border:none;" src="https://www.chess.com/emboard?id=14889943"></iframe><script nonce="chesscom-diagram">window.addEventListener("message",e=>{e['data']&&"14889943"===e['data']['id']&&document.getElementById(`${e['data']['id']}`)&&(document.getElementById(`${e['data']['id']}`).style.height=`${e['data']['frameHeight']+37}px`)})</script>

I won the exchange early (Bxa8 on move 9) and was up a rook for two pawns for most of the game. The position was actually slightly in my favour right up until move 21. After **20...Qxe3+**, I needed to deal with the check.

<figure>
  <img src="{{ '/assets/images/2026-04-12/macvaldr_move40.png' | relative_url }}" alt="After 20...Qxe3+">
  <figcaption>After 20...Qxe3+: Qf2 invites a queen trade. Rf2 loses the game.</figcaption>
</figure>

I played **21. Rf2** but the correct move was **Qf2**, which would have invited a queen trade or kept the tension. Black could have taken the pawn on f4, leaving a sharp position, but the engine still favours White since I'm up a rook for two pawns. Instead, after Rf2 the h-pawn marched down the board and I got mated on move 26.

---

### Game 2: Loss vs nisash321 (529) as Black

<iframe id="14889947" allowtransparency="true" frameborder="0" style="width:100%;border:none;" src="https://www.chess.com/emboard?id=14889947"></iframe><script nonce="chesscom-diagram">window.addEventListener("message",e=>{e['data']&&"14889947"===e['data']['id']&&document.getElementById(`${e['data']['id']}`)&&(document.getElementById(`${e['data']['id']}`).style.height=`${e['data']['frameHeight']+37}px`)})</script>

There was a slight advantage for Black up until move 15. White's bishop was on g5 and I needed to kick it. The correct move was **f6**, attacking the bishop without allowing it into my position. Instead I played **15...h6**, and White punished it immediately.

<figure>
  <img src="{{ '/assets/images/2026-04-12/nisash321_move31.png' | relative_url }}" alt="After 16. Be7">
  <figcaption>After 16. Be7: Bishop forks the queen on d6 and rook on e8. Wrong pawn.</figcaption>
</figure>

**16. Be7** forked my queen and rook. The queen had to move, and I was down a full queen after Bxd6. Pushing the wrong pawn to kick a bishop is such a common mistake. The h-pawn looks natural but it actually opens the door for the bishop to step forward into your position rather than retreat.

---

### Game 3: Win vs Noobimpe (496) as White

<iframe id="14889953" allowtransparency="true" frameborder="0" style="width:100%;border:none;" src="https://www.chess.com/emboard?id=14889953"></iframe><script nonce="chesscom-diagram">window.addEventListener("message",e=>{e['data']&&"14889953"===e['data']['id']&&document.getElementById(`${e['data']['id']}`)&&(document.getElementById(`${e['data']['id']}`).style.height=`${e['data']['frameHeight']+37}px`)})</script>

A Colle-style opening, queen trade on move 8, then a Nc7+ fork winning the rook on move 15. I was only up by about a pawn for most of the game after the trades settled. The knockout came when Black played **20...a5** and I used en passant to take back.

<figure>
  <img src="{{ '/assets/images/2026-04-12/noobimpe_move41.png' | relative_url }}" alt="After 21. bxa6 e.p.">
  <figcaption>After 21. bxa6 e.p.: Protected passed pawn. a7, a8=Q+, Ra7#.</figcaption>
</figure>

**21. bxa6** en passant gave me a protected passed pawn that just steamrolled: a7, a8=Q+ and then Ra7# checkmate. A clean finish.

---

### Game 4: Loss vs Ucupppppppo (514) as Black

<iframe id="14889955" allowtransparency="true" frameborder="0" style="width:100%;border:none;" src="https://www.chess.com/emboard?id=14889955"></iframe><script nonce="chesscom-diagram">window.addEventListener("message",e=>{e['data']&&"14889955"===e['data']['id']&&document.getElementById(`${e['data']['id']}`)&&(document.getElementById(`${e['data']['id']}`).style.height=`${e['data']['frameHeight']+37}px`)})</script>

This was embarrassing. I fumbled the opening and fell for the Nxf7 fork. It's not quite the Fried Liver (that's specifically in the Italian/Two Knights), but it's a very similar idea: the knight attacks on f7 supported by the bishop on c4, forking the queen and rook.

<figure>
  <img src="{{ '/assets/images/2026-04-12/ucupppppppo_move10.png' | relative_url }}" alt="After 5...Bg7">
  <figcaption>After 5...Bg7: Nxf7 is coming. Bishop on c4 supports everything.</figcaption>
</figure>

Instead of fianchettoing my bishop to g7, I needed to interpose a pawn on the bishop's diagonal so it doesn't defend the knight when it takes on f7. One simple pawn push was all it took to stop this opening trap. If I had played accurately, I would have come out of the opening with a slight advantage since White would have wasted time moving their bishop and knight multiple times.

Interestingly, there was a chance to recover. On move 10, after White played Bb3, I could have played **Nd3+**. After Kf1, **Qf5** threatens checkmate on f2 and the only way for White to save it is to trade queens and allow Black to take the bishop on c1, leaving material roughly equal. Instead I played b6 and never recovered. Lost on time.

---

### Game 5: Win vs Fredly65 (477) as White

<iframe id="14889957" allowtransparency="true" frameborder="0" style="width:100%;border:none;" src="https://www.chess.com/emboard?id=14889957"></iframe><script nonce="chesscom-diagram">window.addEventListener("message",e=>{e['data']&&"14889957"===e['data']['id']&&document.getElementById(`${e['data']['id']}`)&&(document.getElementById(`${e['data']['id']}`).style.height=`${e['data']['frameHeight']+37}px`)})</script>

Black made a positional mistake pushing their f and g pawns, exposing the king. After **10...g5**, I missed a mate in 2.

<figure>
  <img src="{{ '/assets/images/2026-04-12/fredly65_move20.png' | relative_url }}" alt="After 10...g5">
  <figcaption>After 10...g5: Qh5+ Qf7# was available. Mate in 2.</figcaption>
</figure>

**Qh5+** forces the king to either e7 or f8, and **Qf7#** is checkmate in both cases. That would have been a really nice 11-move game. As it happened, the real win came when I was able to play **Qxb7**, infiltrating Black's position.

<figure>
  <img src="{{ '/assets/images/2026-04-12/fredly65_move45.png' | relative_url }}" alt="After 23. Qxb7">
  <figcaption>After 23. Qxb7: Infiltration. Taking pieces and simplifying.</figcaption>
</figure>

There were potentially faster ways to win that didn't involve trading the queen, but I was down to less than one minute on the clock and I just wanted simplification and a straightforward win, especially after already losing a few games this session. My rooks delivered checkmate on the back rank on move 36.

---

### Game 6: Win vs jerm5006 (484) as White

<iframe id="14889959" allowtransparency="true" frameborder="0" style="width:100%;border:none;" src="https://www.chess.com/emboard?id=14889959"></iframe><script nonce="chesscom-diagram">window.addEventListener("message",e=>{e['data']&&"14889959"===e['data']['id']&&document.getElementById(`${e['data']['id']}`)&&(document.getElementById(`${e['data']['id']}`).style.height=`${e['data']['frameHeight']+37}px`)})</script>

A comeback story and probably a result of time pressure on my opponent. Black gave up their bishop for my knight early (Bxf3 on move 3) and played well, eroding the pawns around my king. On move 28, they actually had mate in six. After I offered a queen trade, I was down to rooks and a bishop against similar pieces but far more pawns for my opponent.

I thought the only way I was going to have any chance was to activate my rooks, infiltrate on the seventh rank, win some pawns, and cause problems. Which is what I did.

<figure>
  <img src="{{ '/assets/images/2026-04-12/jerm5006_move62.png' | relative_url }}" alt="After 31...Bb4">
  <figcaption>After 31...Bb4: Rh8+ skewers the king and rook on a8. Missed it.</figcaption>
</figure>

Unfortunately I missed a chance to win my opponent's rook. After **31...Bb4**, I could have played **Rh8+** skewering the king and rook on a8. As it turned out, I was able to win several pawns, give several checks, and cause enough problems for my opponent to lose on time.

---

### Reflections

**What went well:**

- Spotting the en passant finish in the Noobimpe game.
- Practical time management decision in the Fredly65 game: trading queens and simplifying rather than searching for a faster win.
- Activating rooks on the seventh rank to create problems in the jerm5006 comeback.

**What to work on:**

- **Qf2 not Rf2**: When defending a check, consider which piece should do the blocking. The queen on f2 invites a trade when you're up material. The rook on f2 does nothing.
- **h6 vs f6 to kick bishops**: Think about where the bishop can go after being kicked. h6 opened the door for Be7. f6 forces a retreat.
- **Opening traps**: The Nxf7 fork supported by the bishop on c4 is a pattern I keep falling for. I need to block the bishop's diagonal with a pawn before fianchettoing.
- **Look for checkmates**: Qh5+ Qf7# was sitting there for a beautiful 11-move win.

---

### Further Reading

- [En Passant](https://www.chess.com/terms/en-passant)
- [Fork in Chess](https://www.chess.com/terms/fork-chess)
- [Skewer](https://www.chess.com/terms/skewer-chess)
