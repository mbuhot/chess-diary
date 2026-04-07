---
layout: post
title: "Puzzle: Pin and Win"
date: 2026-04-07 14:00:00 +1000
---

<style>
figure { margin: 1.5em 0 2em; }
figcaption { font-style: italic; color: #555; margin-top: 0.5em; }
</style>

**Puzzle:** [#1907994](https://www.chess.com/puzzles/problem/1907994) | **Theme:** Pin, Queen Trap | **Rating:** 1835 | **Pass Rate:** 67.1%

<iframe id="14860085" allowtransparency="true" frameborder="0" style="width:100%;border:none;" src="https://www.chess.com/emboard?id=14860085"></iframe><script nonce="chesscom-diagram">window.addEventListener("message",e=>{e['data']&&"14860085"===e['data']['id']&&document.getElementById(`${e['data']['id']}`)&&(document.getElementById(`${e['data']['id']}`).style.height=`${e['data']['frameHeight']+37}px`)})</script>

---

I really enjoyed this puzzle because it was challenging and showed me a new way to think about pins, specifically about why candidate moves that look similar can lead to very different outcomes.

<figure>
  <img src="{{ '/assets/images/2026-04-07-puzzle1/start.png' | relative_url }}" alt="Starting position">
  <figcaption>Puzzle position. White to move: how to win Black's queen?</figcaption>
</figure>

The hint is that Black has blundered and White can win a queen. There's only one check available, Ndc7+, but it can immediately be taken by the queen and I can't see a continuation down that line that leads anywhere. So I think we can ignore checks on the king for now.

The thing I noticed is that if I could just get rid of the knight on f3, then I could pin the queen to the king by moving the bishop from e2 to h5. The bishop would attack the queen, pinning it to the king, while being supported by the White queen on d1. A very promising avenue. The question is: where to move the knight on f3?

Looking at all the candidate moves, the knight could go back to g1, over to d2, d4, take on e5, take on g5, or even hop to h4. So many choices, and depending on Black's response the pin may or may not be available. What we need is a move that leaves White in an excellent position whether Black takes the knight, moves the queen, or even moves the king. Usually that means moving into a position where there are multiple threats.

The most logical candidates for me were **Nxg5** and **Nxe5**, both quite forcing because they attack the queen. I found it very hard to convince myself which one was the better move.

---

### The Solution: Nxg5

<figure>
  <img src="{{ '/assets/images/2026-04-07-puzzle1/nxg5.png' | relative_url }}" alt="After 10. Nxg5">
  <figcaption>After 10. Nxg5: Attacks the queen. If fxg5, the pin is coming.</figcaption>
</figure>

**10. Nxg5** looks good because yes, the knight can be taken with the f-pawn, and that's actually what we want the opponent to do so we can pin the queen and win it. But we have to consider: what if they don't take the knight?

If Black plays **Qf8** or **Qg7**, those are both pretty bad because they allow Nxe6 with tempo attacking the queen. The queen either has to come back to the problematic f7 square where it will be pinned, or potentially down to e6, which allows Nxc7+ forking the king and rook. So Nxg5 is looking good against those retreats.

What about **Qd7**? That line goes: Nxe6 (taking the bishop), and Black's best response is apparently Qxe6 taking back the knight. However, that puts the queen on a different rank to the vulnerable pawn on c7, so we can take c7 with check, triple forking the rook, king, and queen. We win the queen next turn.

And if Black doesn't take the knight on e6 with the queen, say instead defending c7 with **Rc8**, then White has a beautiful check with Bh5+. The only move for Black is to block the check with the queen, leading right back to the puzzle outcome we were going for: winning Black's queen.

After **10...fxg5 11. Bh5**, the queen is pinned and lost.

<figure>
  <img src="{{ '/assets/images/2026-04-07-puzzle1/bh5.png' | relative_url }}" alt="After 11. Bh5">
  <figcaption>After 10...fxg5 11. Bh5: The pin. Queen is trapped against the king.</figcaption>
</figure>

---

### Why Not Nxe5?

This is where I picked up something really valuable from this puzzle. At first glance, **10. Nxe5** looks very similar to Nxg5. It attacks the queen. If it's taken by either pawn (fxe5 or dxe5), we're good: we get the pin on the queen next turn and win it. But what if it's taken by the knight?

After **10. Nxe5 Nxe5 11. Bh5**, Black plays **Ng6**, interposing itself between the bishop and the queen from a nicely defended position. The attack on the queen fizzles out completely.

<figure>
  <img src="{{ '/assets/images/2026-04-07-puzzle1/ng6_interpose.png' | relative_url }}" alt="After Ng6 interposition">
  <figcaption>Alternative: 10. Nxe5 Nxe5 11. Bh5 Ng6. The knight blocks the pin. Attack over.</figcaption>
</figure>

In all honesty I didn't even see that line until after I'd solved the puzzle and checked with the analysis, trying to understand why Nxg5 was so much better than Nxe5. The knight on g6 interposes perfectly, blocking the diagonal. This is the key lesson from the puzzle.

---

### Takeaway

There are at least three ways to deal with a pin: take the attacking piece, move the more valuable piece that's causing the pin, or interpose. Being aware of the interposing option is what's going to help me in positions like this in future. Knowing that Black might be trying to get a piece onto g6 to block the pin would immediately make me see that Nxe5 allows exactly that, while Nxg5 doesn't.

For a rated puzzle like this one, you have a reasonable chance of finding the correct move using your immediate gut instinct or intuition. Nxg5 was the obvious move. But the pass rate of just 67% on an 1835-rated puzzle shows that many players probably immediately saw Nxe5 instead. That's also a logical, intuitive move. If you want to actually increase your puzzle rating and get better, you have to really convince yourself that you found the best move and understood the best response. This is what makes puzzle training valuable. It's not just so that you see your number go up. It's that you practise the skills that will improve calculation, pattern recognition, and the ability to read the board. That's why I'm really enjoying puzzles at the moment and looking to reach a puzzle rating of 2100.

One interesting thing about these higher-rated puzzles is that not every line guarantees the outcome implied by the hint. There are lines where Black can save the queen but loses a piece and a rook instead, leaving them in a completely losing position. It's a little bit unsatisfying from a puzzle point of view when the moves aren't forcing enough to guarantee the hinted result, but I think the thing to keep in mind is that lines that leave the opponent in a completely losing position can be discounted. Being down eight points in material means it's a line the puzzle assumes won't be played.

---

### Further Reading

- [Pin in Chess](https://www.chess.com/terms/pin-chess)
- [The Power of a Pin](https://www.chess.com/article/view/the-power-of-a-pin)
- [Trapped Piece](https://www.chess.com/terms/trapped-piece-chess)
