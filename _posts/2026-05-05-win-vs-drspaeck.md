---
layout: post
title: "Win vs DrSpaeck (1047)"
date: 2026-05-05 20:00:00 +1000
---

<style>
figure { margin: 1.5em 0 2em; }
figcaption { font-style: italic; color: #555; margin-top: 0.5em; }
</style>

**Opening:** Pirc Defence | **Result:** 0-1 (Checkmate) | **Time Control:** 3 days/move (Daily) | **Rated** | **Event:** 91st Chess.com Daily Tournament (1001-1200), Round 1

[View on Chess.com](https://www.chess.com/game/daily/965815413)

<iframe id="15053645" allowtransparency="true" frameborder="0" style="width:100%;border:none;" src="https://www.chess.com/emboard?id=15053645"></iframe><script nonce="chesscom-diagram">window.addEventListener("message",e=>{e['data']&&"15053645"===e['data']['id']&&document.getElementById(`${e['data']['id']}`)&&(document.getElementById(`${e['data']['id']}`).style.height=`${e['data']['frameHeight']+37}px`)});</script>

---

### Game Overview

A very satisfying win. I picked up a piece early in the game with a fork, then had a nice tactic to win the queen with a discovered attack from my fianchettoed bishop, and finally delivered a clean checkmate. All in all a very satisfying game and a good example of tactics training paying off.

---

### The Opening (Moves 1-7)

**1. e4 d6 2. Nc3 g6 3. d4 Bg7 4. Bc4 Nf6 5. Qf3 Nc6 6. Nge2 O-O**

The first six moves were fairly standard Pirc Defence. However, I think my opponent made a mistake by bringing their queen out too early with Qf3. It didn't cause any immediate problems, but it left the queen exposed.

**7. d5**

<figure>
  <img src="{{ '/assets/images/2026-05-05-game4/move13.png' | relative_url }}" alt="After 7. d5">
  <figcaption>After 7. d5: Blunder. Creates the Ne5 fork.</figcaption>
</figure>

Technically the mistake was when White pushed the d5 pawn to attack my knight. That's what created the weakness on the e5 square that allowed the fork.

**7...Ne5**

<figure>
  <img src="{{ '/assets/images/2026-05-05-game4/move14.png' | relative_url }}" alt="After 7...Ne5">
  <figcaption>After 7...Ne5: Fork on the queen and bishop.</figcaption>
</figure>

Ne5 forks the queen on f3 and the bishop on c4. White has to choose which piece to save.

---

### Winning the Queen (Moves 8-12)

**8. Qe3 Nxc4 9. Qd4 Ne5 10. Bf4 Nfg4 11. O-O Nf3+**

<figure>
  <img src="{{ '/assets/images/2026-05-05-game4/move22.png' | relative_url }}" alt="After 11...Nf3+">
  <figcaption>After 11...Nf3+: Discovered attack wins the queen.</figcaption>
</figure>

I was really happy to see the knight fork sacrifice that wins the queen with a discovered attack from the bishop on g7. There's been a recent game where I missed opportunities to use my fianchettoed bishop like this, but it's a very powerful weapon when it can be used to discover attack a piece after making a move. And what better piece to win than a queen.

This move also has the nice side effect of breaking open White's castle when White takes the checking knight. The king is exposed and I've got a clear Qg5 move to deliver a check and start thinking about checkmate.

**12. gxf3 Bxd4**

<figure>
  <img src="{{ '/assets/images/2026-05-05-game4/move24.png' | relative_url }}" alt="After 12...Bxd4">
  <figcaption>After 12...Bxd4: Queen won. Up massive material.</figcaption>
</figure>

---

### The Attack (Moves 13-21)

**13. Nxd4 Ne5 14. b3 e6 15. Bxe5 dxe5 16. Nde2 exd5 17. exd5 Qg5+**

<figure>
  <img src="{{ '/assets/images/2026-05-05-game4/move34.png' | relative_url }}" alt="After 17...Qg5+">
  <figcaption>After 17...Qg5+: Check. King exposed.</figcaption>
</figure>

With the queen and the open g-file to work with, I started the attack. Qg5+ delivers check and the king is now very exposed.

**18. Ng3 f5 19. Kh1 f4 20. Nge4 Qh5 21. Nd2 Bh3**

<figure>
  <img src="{{ '/assets/images/2026-05-05-game4/move42.png' | relative_url }}" alt="After 21...Bh3">
  <figcaption>After 21...Bh3: Pieces closing in on the castled king.</figcaption>
</figure>

My pieces were closing in. I had the bishop, rook and queen all near the king, but White had done a good job of protecting some key squares and stopping me from delivering checkmate immediately. I was waiting for a chance to play Qxf3 or if needed use my rook on the g-file to clear out some space.

---

### The Checkmate (Moves 22-25)

**22. Rg1 Rf5 23. Nb5 Rd8 24. Ne4 Qxf3+**

<figure>
  <img src="{{ '/assets/images/2026-05-05-game4/move48.png' | relative_url }}" alt="After 24...Qxf3+">
  <figcaption>After 24...Qxf3+: Mate in one.</figcaption>
</figure>

White then made a critical error moving the knight from d2, which was guarding the f3 square, giving me a path to checkmate. Qxf3+ with check, and the only move is Rg2 which allows Qxg2 mate.

**25. Rg2 Qxg2#**

<figure>
  <img src="{{ '/assets/images/2026-05-05-game4/move50.png' | relative_url }}" alt="After 25...Qxg2#">
  <figcaption>After 25...Qxg2#: Checkmate.</figcaption>
</figure>

---

### Engine Review

A nice high accuracy game: 91.4% for me versus 76.3% for my opponent. Game rating of 1850 for me versus 1300 for my opponent. No blunders, no mistakes, no inaccuracies for me. One blunder, one mistake and one inaccuracy for my opponent.

The engine agrees that d5 was the main blunder, which enabled Ne5. The evaluation goes to -4.6 the moment the fork happens. Qf3 was an inaccuracy but not losing yet, although it does put White in the dangerous position of potentially getting forked.

Nf3+ was the best move: the discovered attack that wins the queen. What's really surprising is just how decisively the engine rates the game as lost once the first blunder is made. You might think that being down a piece early in the game is a disadvantage but not a decisive loss, but in this case the evaluation went straight to around -5 after winning the bishop, and stays there after also winning the queen. Even castling into the fork is only rated a "good" move, not an inaccuracy or mistake. The artificial coach comment was something like: "Uh-oh, they just dropped a queen, but you were winning anyway, so whatever." There really isn't room for mistakes at this level.

---

### Reflections

**What went well:**

- Great opening. Seeing the Ne5 fork on the queen and bishop and exploiting the early queen development.
- The Nf3+ discovered attack winning the queen through the fianchettoed bishop on g7. Really great to see tactics puzzle training paying off and not rushing into moves on autopilot.
- The checkmate was clean. I didn't need to promote a pawn, just coordinate my pieces and attack.

**What to work on:**

- Not much to improve on here according to the engine. I could have skipped Rf5 and gone straight for Rd8 to pressure the knights in the centre. That might have meant checkmate slightly sooner, but ultimately this game was lost by my opponent's mistakes, so as long as I'm spotting them and exploiting them I'm happy with that.

---

*Full PGN:*

```
1. e4 d6 2. Nc3 g6 3. d4 Bg7 4. Bc4 Nf6 5. Qf3 Nc6 6. Nge2 O-O 7. d5 Ne5 8. Qe3
Nxc4 9. Qd4 Ne5 10. Bf4 Nfg4 11. O-O Nf3+ 12. gxf3 Bxd4 13. Nxd4 Ne5 14. b3 e6
15. Bxe5 dxe5 16. Nde2 exd5 17. exd5 Qg5+ 18. Ng3 f5 19. Kh1 f4 20. Nge4 Qh5 21.
Nd2 Bh3 22. Rg1 Rf5 23. Nb5 Rd8 24. Ne4 Qxf3+ 25. Rg2 Qxg2# 0-1
```

---

### Further Reading

- [Pirc Defence](https://www.chess.com/openings/Pirc-Defense)
- [Discovered Attack](https://www.chess.com/terms/discovered-attack-chess)
- [Fork in Chess](https://www.chess.com/terms/fork-chess)
