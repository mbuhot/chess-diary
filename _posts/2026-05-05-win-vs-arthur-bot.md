---
layout: post
title: "Win vs Arthur Bot (1700)"
date: 2026-05-05 18:00:00 +1000
---

<style>
figure { margin: 1.5em 0 2em; }
figcaption { font-style: italic; color: #555; margin-top: 0.5em; }
</style>

**Opening:** Benoni Defence | **Result:** 1-0 (Checkmate) | **Time Control:** Untimed (Bot) | **Unrated**

[View on Chess.com](https://www.chess.com/game/computer/1274630983)

<iframe id="15049701" allowtransparency="true" frameborder="0" style="width:100%;border:none;" src="https://www.chess.com/emboard?id=15049701"></iframe><script nonce="chesscom-diagram">window.addEventListener("message",e=>{e['data']&&"15049701"===e['data']['id']&&document.getElementById(`${e['data']['id']}`)&&(document.getElementById(`${e['data']['id']}`).style.height=`${e['data']['frameHeight']+37}px`)});</script>

---

### Game Overview

A bot match against Arthur, a 1700-rated bot I'd been struggling to beat without assistance for a long time. Equal to the most challenging bot I've beaten. The game turned on move 22 where I checked the king with a rook in front of the queen, winning the queen, and from there it was a matter of converting.

---

### The Opening (Moves 1-14)

**1. d4 c5 2. d5 Nf6 3. e4 Nxe4 4. Bd3 Nf6 5. Nf3 d6 6. O-O Bd7 7. Bf4 e5 8. dxe6 Bxe6**

<figure>
  <img src="{{ '/assets/images/2026-05-05-game3/move15.png' | relative_url }}" alt="After 8. dxe6">
  <figcaption>After 8. dxe6: En passant. Centre opens up.</figcaption>
</figure>

Black tried a Benoni structure with c5, then grabbed my e-pawn with Nxe4. I won it back immediately with Bd3 and continued developing. When Black pushed e5 I took en passant with dxe6, opening up the position.

**9. Nc3 Qe7 10. Re1 c4 11. Be4 Nc6 12. Bxc6+ bxc6 13. Nd4 Rb8 14. Nxe6 fxe6**

<figure>
  <img src="{{ '/assets/images/2026-05-05-game3/move27.png' | relative_url }}" alt="After 14. Nxe6">
  <figcaption>After 14. Nxe6: Knight takes bishop. Winning material.</figcaption>
</figure>

I traded my bishop for the knight on c6 with check, doubling Black's pawns, then jumped the knight into d4 eyeing the bishop on e6. After Nxe6 I won the bishop, and Black's king is stuck in the centre with a wrecked pawn structure.

---

### The Key Move (Moves 15-23)

**15. b3 Kd7 16. Ne4 Nxe4 17. Rxe4 g5 18. Bg3 Bg7 19. Rxc4 Rbf8 20. c3 d5 21. Rb4 Bxc3 22. Rb7+**

<figure>
  <img src="{{ '/assets/images/2026-05-05-game3/move43.png' | relative_url }}" alt="After 22. Rb7+">
  <figcaption>After 22. Rb7+: Check in front of the queen. Key move.</figcaption>
</figure>

This was the key move. With the rook on b4 and Black's queen on e7, I was able to check the king by sliding the rook to b7. The king has to move and the queen is lost.

**22...Kd8 23. Rxe7 Kxe7**

From here I was up a queen for a rook and just needed to clean up.

---

### Converting (Moves 24-56)

**24. Rc1 d4 25. Be5 c5 26. Bxh8 Rxh8 27. Rxc3 dxc3 28. Qc2 c4 29. Qxc3 Rf8 30. Qxc4**

I traded down pieces and mopped up Black's remaining pawns. Once I had a clean material advantage I pushed my queenside pawns.

**30...Rf7 31. b4 h5 32. b5 Kf6 33. a4 Rd7 34. f3 Ke7 35. a5 Kf7 36. b6 axb6 37. axb6 Rb7 38. Qc6 Re7 39. b7 Re8 40. Qc7+ Re7 41. Qxe7+ Kxe7 42. b8=Q**

<figure>
  <img src="{{ '/assets/images/2026-05-05-game3/move83.png' | relative_url }}" alt="After 42. b8=Q">
  <figcaption>After 42. b8=Q: Promotion. Mopping up.</figcaption>
</figure>

The b-pawn marched all the way to promotion. I was happy to sacrifice the queen for the last rook because the pawn was unstoppable.

**42...Kf7 43. Kf2 Ke7 44. Ke3 g4 45. fxg4 hxg4 46. Ke4 Kd7 47. Ke5 g3 48. hxg3 Kc6 49. Kxe6 Kc5 50. Qc7+ Kb5 51. Kd5 Ka4 52. Kc4 Ka3 53. Kc3 Ka2 54. Kc2 Ka3 55. Qf4 Ka2 56. Qa4#**

<figure>
  <img src="{{ '/assets/images/2026-05-05-game3/move111.png' | relative_url }}" alt="After 56. Qa4#">
  <figcaption>After 56. Qa4#: Checkmate.</figcaption>
</figure>

---

### Engine Review

75.5% accuracy for me versus 69.4% for Arthur. Game rating of 1350 for me versus 500 for Arthur. Not the cleanest game on either side, with 2 blunders and 3 mistakes from me and 3 blunders and 5 mistakes from Arthur, but a win is a win against a 1700 bot.

---

### Reflections

**What went well:**

- Spotting the Rb7+ check in front of the queen was the decisive moment.
- Pushing the b-pawn to promotion was clean.

**What to work on:**

- The opening and middlegame were messy. Reducing the blunder count even against bots is good practice.

---

*Full PGN:*

```
1. d4 c5 2. d5 Nf6 3. e4 Nxe4 4. Bd3 Nf6 5. Nf3 d6 6. O-O Bd7 7. Bf4 e5 8. dxe6
Bxe6 9. Nc3 Qe7 10. Re1 c4 11. Be4 Nc6 12. Bxc6+ bxc6 13. Nd4 Rb8 14. Nxe6 fxe6
15. b3 Kd7 16. Ne4 Nxe4 17. Rxe4 g5 18. Bg3 Bg7 19. Rxc4 Rbf8 20. c3 d5 21. Rb4
Bxc3 22. Rb7+ Kd8 23. Rxe7 Kxe7 24. Rc1 d4 25. Be5 c5 26. Bxh8 Rxh8 27. Rxc3 dxc3
28. Qc2 c4 29. Qxc3 Rf8 30. Qxc4 Rf7 31. b4 h5 32. b5 Kf6 33. a4 Rd7 34. f3 Ke7
35. a5 Kf7 36. b6 axb6 37. axb6 Rb7 38. Qc6 Re7 39. b7 Re8 40. Qc7+ Re7 41. Qxe7+
Kxe7 42. b8=Q Kf7 43. Kf2 Ke7 44. Ke3 g4 45. fxg4 hxg4 46. Ke4 Kd7 47. Ke5 g3
48. hxg3 Kc6 49. Kxe6 Kc5 50. Qc7+ Kb5 51. Kd5 Ka4 52. Kc4 Ka3 53. Kc3 Ka2 54.
Kc2 Ka3 55. Qf4 Ka2 56. Qa4# 1-0
```
