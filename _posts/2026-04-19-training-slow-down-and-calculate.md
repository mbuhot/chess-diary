---
layout: post
title: "Training Session: Slow Down and Calculate"
date: 2026-04-19 14:00:00 +1000
---

<style>
figure { margin: 1.5em 0 2em; }
figcaption { font-style: italic; color: #555; margin-top: 0.5em; }
</style>

**Format:** Training Session vs Wendy (1500 bot) | **Games:** 2 | **Record:** 1W / 1L

---

### What I'm Practising

I've been working on deliberately slowing down and vocalising my thinking during games. The approach is simple: for every move, ask two questions. First, what's the most active move for me that creates problems for my opponent, improves my position, or advances my plan? Second, what is my opponent's best response?

I think my puzzle training is starting to pay off here. To correctly solve high-level puzzles, you need to calculate what potential responses the opponent could have that would thwart your ideas, or find tactics that win material or deliver checkmate. By doing that successfully in game two (and unsuccessfully in game one), I'm proving to myself that I can win games against the advanced bots on chess.com. But it does require slowing down.

---

### Game 1: Loss vs Wendy (Colle-Zukertort)

[View on Chess.com](https://www.chess.com/game/computer/1136298963)

This game started well. I played a Colle-Zukertort and was making engine-best moves through move 10, building up a 4.3 evaluation advantage with an extra pawn. The thinking process was working: I identified b5 as a likely mistake from Black, checked for threats, didn't find any, and took the free pawn. On move 10, a4 was the engine's top choice and I found it.

The trouble started when Black's queen invaded on c3. My thinking immediately switched from "how do I consolidate my advantage" to "how do I trap this queen." I spent moves 11-14 chasing it around my position with Rb1, O-O, Nc4, Rb3, and I actually succeeded. By move 14, the queen was cornered on a1 with very few escape squares.

<figure>
  <img src="{{ '/assets/images/2026-04-19-training/g1_qa1.png' | relative_url }}" alt="After 14...Qa1">
  <figcaption>After 14...Qa1: Queen cornered. The chase was over, but I didn't realise it.</figcaption>
</figure>

This is where I failed to ask the second question: what is my opponent's best response? The queen was already dealt with. I should have reset my thinking and looked at the whole board. Instead, the momentum of the chase carried me into **15. Ra3**, and I completely missed that Black's dark-squared bishop on f8 was staring right at that square.

<figure>
  <img src="{{ '/assets/images/2026-04-19-training/g1_bxa3.png' | relative_url }}" alt="After 15...Bxa3">
  <figcaption>After 15...Bxa3: Tunnel vision. I was so focused on the queen I forgot to check if my rook was safe.</figcaption>
</figure>

I resigned here. The position was still playable (the queen was still stuck and there were ideas like Nb6 forking the rook on a8), but I wanted to stop and recognise the thinking failure rather than play on.

**The lesson:** recognise when the job is done and pivot. The queen was cornered. Mission accomplished. Time to look at the whole board again. And before every move, even an attacking one: can anything take my piece on this square?

---

### Game 2: Win vs Wendy (Colle-Zukertort)

[View on Chess.com](https://www.chess.com/game/computer/1136577269)

Same opening, completely different result. 87.5% accuracy, no blunders, game rating of 1800. This time I maintained the thinking process throughout.

The opening followed a similar path but Black took on d4 instead of pushing c4. After the exchanges I ended up with the bishop pair and a clear plan to attack the castled king. On move 12, I spotted the Bxh7+ sacrifice idea but correctly decided I wasn't ready for it. Only two pieces in the attack isn't enough. Instead of rushing in, I improved my position with Rae1 and planned a rook lift.

On move 14, Black played d4 and I caught myself: "I wasn't considering Black's best move. I was only considering knight moves." That moment of self-awareness was important. I recovered with Re4, keeping the e5 pawn defended while staying active.

The strongest stretch came on moves 15-18. I calculated a multi-move sequence: exf6 to vacate e5, then f4 threatening fxe5 with a discovered double attack on the queen from both the pawn and the rook.

<figure>
  <img src="{{ '/assets/images/2026-04-19-training/g2_f4.png' | relative_url }}" alt="After 17. f4">
  <figcaption>After 17. f4: Calculated fxe5 with a discovered double attack on the queen.</figcaption>
</figure>

I checked Black's responses: g5 actually helps me, queen retreats leave the d4 pawn blocking the dangerous diagonal, and blocking with Bf5 allows a pin. This was proper calculation: my move, their best response, my follow-up.

When Black offered a queen trade on h6, I took it because I'd already calculated the resulting endgame: passed e-pawn, doubled h-pawns for Black, and my bishop pair would dominate.

<figure>
  <img src="{{ '/assets/images/2026-04-19-training/g2_qxh6.png' | relative_url }}" alt="After 19. Qxh6">
  <figcaption>After 19. Qxh6: Trading queens with a clear endgame plan.</figcaption>
</figure>

From there I had a multi-step plan: push e6 to win the bishop, trade rooks because I'm up material, push b5 to kick the knight off the defence of d4, take d4 with check, then promote. I executed it move by move, checking for knight forks at each step since that was the only way to lose.

The endgame technique worked. Bc4+ with tempo, c3 to kick the knight, then a clean pawn march to promotion.

<figure>
  <img src="{{ '/assets/images/2026-04-19-training/g2_bf3mate.png' | relative_url }}" alt="40. Bf3#">
  <figcaption>40. Bf3#: Bishop delivers checkmate. King trapped by its own pawns.</figcaption>
</figure>

---

### Reflections

The contrast between these two games is the whole point. In game 1, I played well for 14 moves, then got tunnel vision on one idea and blundered. In game 2, I maintained broad awareness throughout, kept asking "what's my opponent's best response," had contingency plans, and checked piece safety on every move.

**What went well:**

- Slowing down and thinking out loud. Vocalising my reasoning forced me to consider more options and catch potential problems.
- Asking "what is my opponent's best response" before committing to a move. This is the puzzle training paying off.
- Knowing when an attack isn't ready (the Bxh7+ sacrifice) and choosing to improve the position instead.
- Planning multiple moves ahead in the endgame and executing the plan step by step.

**What to work on:**

- Recognising when a task is complete and resetting my thinking. In game 1 the queen was already cornered but I kept chasing.
- Before every move, ask: "can anything take my piece on this square?" This one check would have saved me in game 1.

---

### Further Reading

- [How to Improve Your Calculation](https://www.chess.com/article/view/calculation)
- [The Art of Calculation in Chess](https://www.chess.com/blog/OnlineChessTeacher/the-art-of-calculation-in-chess-how-to-improve-your-thinking-process)
- [Candidate Moves](https://www.chess.com/lessons/candidate-moves)
- [Deliberate Practice in Chess](https://www.chess.com/forum/view/general/getting-better-at-chess-by-deliberate-practice)
