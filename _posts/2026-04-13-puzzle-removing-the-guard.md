---
layout: post
title: "Puzzle: Removing the Guard"
date: 2026-04-13 14:00:00 +1000
---

<style>
figure { margin: 1.5em 0 2em; }
figcaption { font-style: italic; color: #555; margin-top: 0.5em; }
</style>

**Puzzle:** [#2563042](https://www.chess.com/puzzles/problem/2563042) | **Theme:** Removing the Guard, Counterattack

<iframe id="14896297" allowtransparency="true" frameborder="0" style="width:100%;border:none;" src="https://www.chess.com/emboard?id=14896297"></iframe><script nonce="chesscom-diagram">window.addEventListener("message",e=>{e['data']&&"14896297"===e['data']['id']&&document.getElementById(`${e['data']['id']}`)&&(document.getElementById(`${e['data']['id']}`).style.height=`${e['data']['frameHeight']+37}px`)})</script>

---

I found this puzzle very challenging because I wasn't able to apply the standard "checks, captures, threats" approach to find the solution. It required a different kind of thinking.

<figure>
  <img src="{{ '/assets/images/2026-04-13-puzzle2/start.png' | relative_url }}" alt="Puzzle position after Ne3">
  <figcaption>After 1. Ne3: Black to move. How to make progress?</figcaption>
</figure>

The key idea is that Black is trying to get a checkmate, but first needs to eliminate the defender of the d3 square. The White queen on b5 is currently guarding d3. If we could dislodge that queen, the Black queen could come to d3, check the king, push it back to the first rank, and then bring in the rook to c1 for checkmate.

So how do you get the queen off b5 without sacrificing your own pieces? You could put your rook on b7 and the queen would take it, which would certainly get it off the square. You'd be able to check on d3, but it wouldn't lead to mate. The queen alone isn't quite enough.

---

### The Solution: Rc5

The move to consider is to attack the queen with the rook, but on the fifth rank.

<figure>
  <img src="{{ '/assets/images/2026-04-13-puzzle2/rc5.png' | relative_url }}" alt="After 1...Rc5">
  <figcaption>After 1...Rc5: Attacking the queen. Removing the guard of d3.</figcaption>
</figure>

**1...Rc5** puts the question to the White queen. If the queen takes the rook with **Qxc5**, Black recaptures with the queen, leaving Black up a queen against a rook and knight. Black should be winning from there.

But the stronger response from White is **2. Rd1**, counter-attacking the Black queen.

<figure>
  <img src="{{ '/assets/images/2026-04-13-puzzle2/rd1.png' | relative_url }}" alt="After 2. Rd1">
  <figcaption>After 2. Rd1: Counter-attack. White threatens to trade queens.</figcaption>
</figure>

If Black takes the White queen with **2...Rxb5**, White retakes with **Rxd4** and it's just a queen trade, roughly equal. That's not good enough. Instead, Black has to see that they can take the White rook with check.

**2...Qxd1+ 3. Nxd1 Rxb5**

White recaptures with the knight, and then Black takes the White queen. The result is a rook versus a knight: a decisive advantage.

<figure>
  <img src="{{ '/assets/images/2026-04-13-puzzle2/rxb5.png' | relative_url }}" alt="After 3...Rxb5">
  <figcaption>After 3...Rxb5: Rook vs knight. Black is winning.</figcaption>
</figure>

---

### My Attempt

My attempted solution was incorrect. I tried to play Rd7 to support the queen, and then Qd2, which is a good idea except White has a very strong counter-attack with Rd1 that neutralises Black's attack before it gets a chance to check. I missed that counter-attack.

---

### Takeaway

The thing that made this puzzle very difficult for me is that I was looking for checks and the solution doesn't start with a check. It starts with removing the guard. In other puzzles this usually looks like trapping a piece, but here the queen isn't trapped. It does have squares it can go to, but by doing so it no longer guards d3, which would then lead to a winning position for Black. The puzzle requires seeing the idea of a check on d3, then working backwards to understand how to remove the guard with Rc5, and then calculating that every line from there leaves Black winning at least a rook.

The other lesson I'm taking from this is about counter-attacks. Not only do we have to look at checks, captures, and threats, but also counter-attacks, which are always the strongest form of defence. When I tried Rd7 and Qd2, I failed to anticipate White's Rd1 counter-attacking my queen. Recognising when your opponent can counter-attack before your own plan gets going is something I need to get better at.

---

### Further Reading

- [Removing the Defender](https://www.chess.com/terms/removing-the-defender-chess)
- [Deflection](https://www.chess.com/terms/deflection-chess)
- [Counterattack](https://www.chess.com/article/view/counterattack)
