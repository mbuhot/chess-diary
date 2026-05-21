---
layout: post
title: "Win vs FakeBeil91 (1387)"
date: 2026-05-20 14:00:00 +1000
---

<style>
figure { margin: 1.5em 0 2em; }
figcaption { font-style: italic; color: #555; margin-top: 0.5em; }
</style>

**Opening:** Queen's Gambit (D06) | **Result:** 1-0 (Resignation) | **Time Control:** 14 days/move (Daily) | **Rated** | **Event:** ForEverOne 2026, Round 1

[View on Chess.com](https://www.chess.com/game/daily/961333139)

<iframe id="15148867" allowtransparency="true" frameborder="0" style="width:100%;border:none;" src="https://www.chess.com/emboard?id=15148867"></iframe><script nonce="chesscom-diagram">window.addEventListener("message",e=>{e['data']&&"15148867"===e['data']['id']&&document.getElementById(`${e['data']['id']}`)&&(document.getElementById(`${e['data']['id']}`).style.height=`${e['data']['frameHeight']+37}px`)});</script>

---

### Game Overview

A pretty straightforward game where my opponent lost material after walking into a discovered attack, and then later was vulnerable to a pawn fork. These two mistakes put them in a losing position and they resigned after 23 moves.

---

### The Opening (Moves 1-7)

**1. d4 d5 2. c4 c5 3. dxc5 d4 4. Nf3 Nc6 5. e3 dxe3**

<figure>
  <img src="{{ '/assets/images/2026-05-20-game1/move10.png' | relative_url }}" alt="After 5...dxe3">
  <figcaption>After 5...dxe3: Pawn recapture. Queen trade incoming.</figcaption>
</figure>

With plenty of time between moves, I tried a slightly different opening: the Queen's Gambit with d4 d5, c4 c5. Quite early on my opponent allowed a queen exchange which I was fairly happy to take.

**6. Qxd8+ Nxd8**

<figure>
  <img src="{{ '/assets/images/2026-05-20-game1/move12.png' | relative_url }}" alt="After 6...Nxd8">
  <figcaption>After 6...Nxd8: Knight retreats. Development delayed.</figcaption>
</figure>

The queen trade forced that knight back to the eighth rank to recapture my queen, delaying Black's development and letting me get the rest of my pieces into good positions.

**7. Bxe3 Nc6 8. a3 Bf5 9. Be2 e6 10. Nc3 a6 11. Rd1 Nf6**

By move 14 things are looking pretty good. I did delay castling, however castling after the queens are traded off isn't such a priority and I've already gotten one rook on an open centre file.

---

### The Discovered Attack (Moves 12-14)

**12. Nd4 Bxc5**

<figure>
  <img src="{{ '/assets/images/2026-05-20-game1/move23.png' | relative_url }}" alt="After 12. Nd4">
  <figcaption>After 12. Nd4: Knight centralised. Bishop on e3 behind it.</figcaption>
</figure>

Black's mistake was Bishop takes c5. It walks into Nxf5 with a discovered attack on c5. The knight on d4 was sitting in front of the bishop on e3, and when the knight moves to f5 it uncovers the bishop's attack on the c5 square. Black can't save both pieces and ends up down a bishop.

**13. Nxf5 Bxe3 14. Nxe3 O-O**

<figure>
  <img src="{{ '/assets/images/2026-05-20-game1/move25.png' | relative_url }}" alt="After 13. Nxf5">
  <figcaption>After 13. Nxf5: Discovered attack on c5.</figcaption>
</figure>

After the dust settles, I've got both knights and a bishop against Black's two knights. Up a full piece.

<figure>
  <img src="{{ '/assets/images/2026-05-20-game1/move28.png' | relative_url }}" alt="After 14...O-O">
  <figcaption>After 14...O-O: Up a bishop. Position settled.</figcaption>
</figure>

---

### Doubling Rooks and the Pawn Advance (Moves 15-21)

**15. f3 Ne5 16. Kf2 Rac8 17. Rd2 h6 18. Rhd1**

<figure>
  <img src="{{ '/assets/images/2026-05-20-game1/move35.png' | relative_url }}" alt="After 18. Rhd1">
  <figcaption>After 18. Rhd1: Rooks doubled on the d-file.</figcaption>
</figure>

I doubled up my rooks on the d-file and started looking for a way to convert the advantage.

**18...Rc7 19. f4 Nc6 20. b4 Rfc8 21. b5 Na7**

<figure>
  <img src="{{ '/assets/images/2026-05-20-game1/move41.png' | relative_url }}" alt="After 21. b5">
  <figcaption>After 21. b5: Pawn chases the knight.</figcaption>
</figure>

I kicked Black's knight with my pawn, chasing it back up the board. Black makes a mistake putting the knight on a7.

<figure>
  <img src="{{ '/assets/images/2026-05-20-game1/move42.png' | relative_url }}" alt="After 21...Na7">
  <figcaption>After 21...Na7: Knight stuck on the rim.</figcaption>
</figure>

---

### The Fork (Moves 22-23)

**22. Rd8+ Kh7 23. b6**

Two moves later, I'm able to get my pawn to b6 forking the knight on a7 and the rook sitting on c7. Black resigns.

<figure>
  <img src="{{ '/assets/images/2026-05-20-game1/move45.png' | relative_url }}" alt="After 23. b6">
  <figcaption>After 23. b6: Fork. Knight and rook both attacked.</figcaption>
</figure>

Looking at the position, I think there was a chance for Black to play on and still only be down a piece. After Rxd8, Rxd8, Rc8, Rxc8, Nxc8, the rooks are traded off and the knight escapes. However there aren't many pieces left for Black to work with in that case, and it would still be a winning position for White.

---

### Engine Review

84.4% accuracy for me versus 75.8% for my opponent. Game rating of 1750 for me versus 1100 for my opponent. No blunders, no mistakes, and no misses for me. One inaccuracy. Three inaccuracies and two mistakes for my opponent.

The engine says dxe3 was the first mistake for Black as it allowed the queen trade, which was the best response. It leaves White with better development and up a pawn.

The main mistake for Black however was Bishop takes c5, with Nxf5 being the best response. The discovered attack wins the bishop and there's no way for Black to avoid it.

The engine confirms that with best play Black can hold onto the material balance with just a piece down, but it leaves both players with two knights and White with the extra bishop. It's a +5 advantage to White at the point Black resigns.

---

### Reflections

**What went well:**

- Trying a new opening with the Queen's Gambit. The early queen trade was good for White and I was happy to take it.
- Spotting the discovered attack with Nxf5 after Black played Bxc5. The knight uncovers the bishop's diagonal and wins material.
- Converting the advantage cleanly with doubled rooks and a pawn fork to finish the game.

**What to work on:**

- I could have played the knight and rook fork a move earlier. I didn't notice it until after I had submitted my move. It was fine in this case because I was still able to play it a move later, but I need to always be looking for tactics.

---

*Full PGN:*

```
1. d4 d5 2. c4 c5 3. dxc5 d4 4. Nf3 Nc6 5. e3 dxe3 6. Qxd8+ Nxd8 7. Bxe3 Nc6 8.
a3 Bf5 9. Be2 e6 10. Nc3 a6 11. Rd1 Nf6 12. Nd4 Bxc5 13. Nxf5 Bxe3 14. Nxe3 O-O
15. f3 Ne5 16. Kf2 Rac8 17. Rd2 h6 18. Rhd1 Rc7 19. f4 Nc6 20. b4 Rfc8 21. b5
Na7 22. Rd8+ Kh7 23. b6 1-0
```

---

### Further Reading

- [Queen's Gambit](https://www.chess.com/openings/Queens-Gambit)
- [Discovered Attack](https://www.chess.com/terms/discovered-attack-chess)
- [Fork in Chess](https://www.chess.com/terms/fork-chess)
