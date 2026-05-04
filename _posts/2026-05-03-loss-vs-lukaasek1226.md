---
layout: post
title: "Loss vs lukaasek1226 (1225)"
date: 2026-05-03 14:00:00 +1000
---

<style>
figure { margin: 1.5em 0 2em; }
figcaption { font-style: italic; color: #555; margin-top: 0.5em; }
</style>

**Opening:** King's Indian Defence, c5 variation | **Result:** 1-0 (Resignation) | **Time Control:** 14 days/move (Daily) | **Rated** | **Event:** ForEverOne 2026, Round 1

[View on Chess.com](https://www.chess.com/game/daily/963158503)

<iframe id="15043229" allowtransparency="true" frameborder="0" style="width:100%;border:none;" src="https://www.chess.com/emboard?id=15043229"></iframe><script nonce="chesscom-diagram">window.addEventListener("message",e=>{e['data']&&"15043229"===e['data']['id']&&document.getElementById(`${e['data']['id']}`)&&(document.getElementById(`${e['data']['id']}`).style.height=`${e['data']['frameHeight']+37}px`)})</script>

---

### Game Overview

This game was a bit of a disaster. I tried a different variation on the King's Indian Defence, pushing c5 rather than e5, which is not a variation I'm very familiar with. I failed to play it correctly and my opponent ended up promoting a pawn and completely crushing me. Similarly to my first game against this opponent in the tournament, they played remarkably accurately for someone at the 1200 rating range with 95.4% accuracy.

---

### The Opening (Moves 1-8)

<figure>
  <img src="{{ '/assets/images/2026-05-03-game1/move10.png' | relative_url }}" alt="After 5...O-O">
  <figcaption>After 5...O-O: King's Indian setup. White has the big centre.</figcaption>
</figure>

**1. d4 Nf6 2. c4 g6 3. Nc3 Bg7 4. e4 d6 5. Be2 O-O 6. h4 h5 7. Bg5 c5 8. d5**

The opening goes pretty much as normal with the King's Indian. For this game I was referring to the master database which is accessible from within the daily game UI on chess.com. I looked at the c5 line and thought it could be interesting as a way to deal with the massive pawn centre that White had achieved. I played c5 and then went for b5, inviting White to take.

<figure>
  <img src="{{ '/assets/images/2026-05-03-game1/move15.png' | relative_url }}" alt="After 8. d5">
  <figcaption>After 8. d5: Centre locked. Queenside play begins.</figcaption>
</figure>

---

### The Queenside Exchange (Moves 8-12)

**8...b5 9. cxb5 a6 10. a4 axb5 11. axb5 Rxa1 12. Qxa1**

White allowed me to take back on b5, then they took on b5 inviting me to exchange rooks on a1. In this position I should have recognised that I'd opened the door on the queenside. There was a passed pawn on the fifth rank and a queen ready to support it, so I needed to deal with this threat before attacking in the centre.

<figure>
  <img src="{{ '/assets/images/2026-05-03-game1/move21.png' | relative_url }}" alt="After 11. axb5">
  <figcaption>After 11. axb5: Passed pawn on b5. A-file open.</figcaption>
</figure>

---

### The Centre Goes Wrong (Moves 13-14)

<figure>
  <img src="{{ '/assets/images/2026-05-03-game1/move26.png' | relative_url }}" alt="After 13...Ne5">
  <figcaption>After 13...Ne5: Trying to fight in the centre.</figcaption>
</figure>

**13. Nf3 Ne5 14. Nxe5 dxe5**

Instead of dealing with the queenside threat I played Ne5 to control the centre. What I didn't calculate was that this invites White to take with their own knight, forcing a reply of taking back with the d6 pawn, which breaks open the pawn chain from e7 to c5.

<figure>
  <img src="{{ '/assets/images/2026-05-03-game1/move28.png' | relative_url }}" alt="After 14...dxe5">
  <figcaption>After 14...dxe5: Pawn chain broken. White up a pawn at +3.6.</figcaption>
</figure>

At that point White is up a pawn with a +3.6 evaluation. They're completely winning already by move 14.

---

### The Queenside Crumbles (Moves 15-26)

**15. O-O Nh7 16. Be3 f5 17. Bxc5 fxe4 18. Qa7 Rf7 19. b6**

<figure>
  <img src="{{ '/assets/images/2026-05-03-game1/move37.png' | relative_url }}" alt="After 19. b6">
  <figcaption>After 19. b6: Passed pawn marching. Queen supporting.</figcaption>
</figure>

I tried to complicate things somewhat to slow down the promotion, but there were too many pieces and some of my own pieces were in very awkward, cramped positions. The knight I placed on h7 to attack the bishop on g5 and my g7 bishop had very little activity. With a bit more time I could have gotten these pieces coordinated and formed my own attack, but my queenside defence crumbled before I had a chance to get organised.

**19...e6 20. Qa8 exd5 21. Nxd5 Qd7 22. Ba6 Bf8 23. Bxc8 Qd8 24. Bxf8 Nxf8 25. b7 Kg7 26. b8=Q**

<figure>
  <img src="{{ '/assets/images/2026-05-03-game1/move43.png' | relative_url }}" alt="After 22. Ba6">
  <figcaption>After 22. Ba6: Black's pieces cramped. Bishop eyes c8.</figcaption>
</figure>

White's bishop came to a6 targeting my bishop on c8, and the b-pawn kept marching. After eliminating my bishops, the b-pawn promoted.

<figure>
  <img src="{{ '/assets/images/2026-05-03-game1/move51.png' | relative_url }}" alt="After 26. b8=Q">
  <figcaption>After 26. b8=Q: Promotion. Two queens for White.</figcaption>
</figure>

---

### The End (Moves 26-32)

**26...Qxh4 27. Qxe5+ Kh6 28. Qh8+ Kg5 29. f4+ Rxf4 30. Nxf4 Qxf4 31. Qd5+ Qe5 32. Qdxe5+**

<figure>
  <img src="{{ '/assets/images/2026-05-03-game1/move63.png' | relative_url }}" alt="After 32. Qdxe5+">
  <figcaption>After 32. Qdxe5+: Black resigns.</figcaption>
</figure>

With two queens on the board there's nothing to do. I resigned.

---

### Engine Review

An incredibly accurate game by my opponent: 95.4% accuracy. Similarly to our first game in this tournament, not a single move that wasn't rated "Best" or "Excellent" for the entire game. Very interesting to see a player at 1225 play this well.

The position was already +3.6 for White by move 14 after the pawn chain broke open. From there it was a matter of time.

---

### Reflections

**What went well:**

- Not much to celebrate here. I tried something new which is at least worth doing from a learning perspective.

**What to work on:**

- If I'm going to play the c5 variation of the King's Indian Defence, I need to be ready to play on the queenside and not treat it the same way I would when playing the e5 variation. With c5, the action is on the queenside and that's where my attention needs to be.
- After the rook exchange on a1, I needed to recognise the passed pawn threat immediately and deal with it before trying anything in the centre.
- Piece coordination was poor. The knight on h7, the bishop on g7, and the rook on f8 were all cramped and doing very little. Getting these pieces active should have been the priority.

---

*Full PGN:*

```
1. d4 Nf6 2. c4 g6 3. Nc3 Bg7 4. e4 d6 5. Be2 O-O 6. h4 h5 7. Bg5 c5 8. d5 b5 9.
cxb5 a6 10. a4 axb5 11. axb5 Rxa1 12. Qxa1 Nbd7 13. Nf3 Ne5 14. Nxe5 dxe5 15.
O-O Nh7 16. Be3 f5 17. Bxc5 fxe4 18. Qa7 Rf7 19. b6 e6 20. Qa8 exd5 21. Nxd5 Qd7
22. Ba6 Bf8 23. Bxc8 Qd8 24. Bxf8 Nxf8 25. b7 Kg7 26. b8=Q Qxh4 27. Qxe5+ Kh6
28. Qh8+ Kg5 29. f4+ Rxf4 30. Nxf4 Qxf4 31. Qd5+ Qe5 32. Qdxe5+ 1-0
```

---

### Further Reading

- [King's Indian Defence: c5 vs e5](https://www.chess.com/forum/view/chess-openings/kings-indian-defense-e5-vs-c5-push)
- [Passed Pawns](https://www.chess.com/terms/passed-pawn)
