---
layout: post
title: "Analysing My Recent Losses"
date: 2026-03-19 12:00:00 +1000
---

<style>
figure { margin: 1.5em 0 2em; }
figcaption { font-style: italic; color: #555; margin-top: 0.5em; }
table { width: 100%; border-collapse: collapse; margin: 1.5em 0; font-size: 0.9em; }
th, td { border: 1px solid #ddd; padding: 6px 10px; text-align: center; }
th { background-color: #f5f5f5; }
</style>

I've been losing a lot lately and I wanted to understand why. Instead of reviewing each game individually, I ran all 7 of my recent losses through Stockfish at depth 18 and looked for patterns. The results are pretty revealing.

---

### The Numbers

Seven games, a mix of rapid, blitz, and bullet. Here's the damage:

<table>
<tr><th>#</th><th>Opponent</th><th>Time Control</th><th>Blunders</th><th>Inaccuracies & Mistakes</th></tr>
<tr><td>1</td><td>737knight</td><td>10 min</td><td>3</td><td>8</td></tr>
<tr><td>2</td><td>VanDerTuesel</td><td>2+1 Bullet</td><td>1</td><td>5</td></tr>
<tr><td>3</td><td>ramaa-2</td><td>2+1 Bullet</td><td>1</td><td>2</td></tr>
<tr><td>4</td><td>heythere111222</td><td>2+1 Bullet</td><td>2</td><td>11</td></tr>
<tr><td>5</td><td>Jah-Rastafarii</td><td>10 min</td><td>1</td><td>2</td></tr>
<tr><td>6</td><td>Valet22600</td><td>10 min</td><td>5</td><td>6</td></tr>
<tr><td>7</td><td>ali1872637</td><td>3+2 Blitz</td><td>1</td><td>8</td></tr>
</table>

14 blunders across 7 games, plus plenty of smaller inaccuracies and mistakes. The real question is: what kind of errors am I making?

---

### Pattern 1: Not Seeing Available Captures

This is the biggest one. In 30% of my blunders, the engine's best move was a simple capture that I didn't play. In some cases, the same capture was available for multiple consecutive moves and I never played it.

**Game 3 vs ramaa-2: dxe5 available for 3 moves straight**

<figure>
  <img src="{{ '/assets/images/2026-03-19/game3_ply15.png' | relative_url }}" alt="Game 3: dxe5 missed">
  <figcaption>Before 8. Be4??: Arrow shows dxe5, winning a free knight.</figcaption>
</figure>

Black played **7...Nxe5** and I just... didn't take back. My d-pawn could have captured on e5 for free. Instead I played **Be4**, putting my bishop on a square where it's attacked by both the d5 pawn and the f6 knight. Black took it immediately with dxe4. Then after trading knights, I played **Qxg4** taking a pawn, but the knight recaptured and I lost my queen too. Bishop and queen gone in three moves. I lost in 10.

**Game 4 vs heythere111222: Bxg7 available for 4 moves straight**

<figure>
  <img src="{{ '/assets/images/2026-03-19/game4_ply17.png' | relative_url }}" alt="Game 4: Bxg7 missed">
  <figcaption>Before 9. c4??: Arrow shows Bxg7. Both bishops attack each other, but it's only an equal trade if White takes first.</figcaption>
</figure>

My position was already losing out of the opening. **8. d5** was bad, pushing a pawn into a position where it gets captured immediately. Then **9. c4** left my bishop on d3 hanging after the knight recaptured on d5 and hopped to b4. The trade **Bxg7 Kxg7** was the engine's top choice on moves 9, 10, 11, and 12, but I never took it. By move 15 I played **h4**, which allowed Black to push **e4**, forking my bishop on d3 and knight on f3. The position was already close to lost, but that fork sealed it.

**Game 1 vs 737knight: Bxh8 in the endgame**

<figure>
  <img src="{{ '/assets/images/2026-03-19/game1_ply72.png' | relative_url }}" alt="Game 1: Bxh8 missed">
  <figcaption>Before 36...Bg7??: Arrow shows Bxh8, winning the hanging rook for nothing.</figcaption>
</figure>

This one hurts. I was in a drawn position and my opponent's rook on h8 was completely hanging. My bishop on d4 could have just taken it. Instead I played Bg7, landing one square short of the rook. Almost certainly a mouse slip: the bishop went along the right diagonal but stopped on g7 instead of h8. One square away from winning a whole rook. Two moves later I got a second chance: after **38. Rb7+**, my bishop on g2 could have taken the rook with **Bxb7**. I played Ke6 instead. Two chances to win a rook with a bishop capture, missed both.

---

### Pattern 2: Queen Safety

15% of my blunders were queen moves. The worst:

**Game 5 vs Jah-Rastafarii: Queen walks into a knight**

<figure>
  <img src="{{ '/assets/images/2026-03-19/game5_ply23.png' | relative_url }}" alt="Game 5: Qd4 blunder">
  <figcaption>Before 12. Qd4??: Arrow shows the safe retreat Qe2. Qd4 gets taken by Nxd4.</figcaption>
</figure>

The position was roughly equal. I played **12. Qd4** and Black immediately took it with **Nxd4**. Game over. The engine wanted **Qe2**, developing the queen to a safe square that also supports the centre. Instead I put my queen on the one square where it could be captured.

**Game 7 vs ali1872637: Queen shuffling while a favourable trade sits on the board**

<figure>
  <img src="{{ '/assets/images/2026-03-19/game7_ply35.png' | relative_url }}" alt="Game 7: Nxd7 missed">
  <figcaption>Before 18. Qg3??: Knight on e5 and bishop on d7 highlighted. Nxd7 starts a favourable trade sequence.</figcaption>
</figure>

My knight on e5 was attacking Black's bishop on d7. The engine says **Nxd7** on moves 17 and 18. It's not winning material outright since Black recaptures with the queen, but the full line is Nxd7 Qxd7 Rxe8+ Rxe8: it trades down and removes Black's active rook with a check, simplifying into a much more manageable position. Instead I moved my queen from f3 to g3, then to h3, then back to g3. Three queen moves while a favourable exchange sat on the board.

**Game 7 vs ali1872637: Wrong capture**

<figure>
  <img src="{{ '/assets/images/2026-03-19/game7_ply47.png' | relative_url }}" alt="Game 7: Qxf5 missed">
  <figcaption>Before 24. Bxd4??: Arrow shows Qxf5. The knight on e5 is doomed, so grab the bishop as compensation.</figcaption>
</figure>

On move 24, my knight on e5 was under attack from the queen, pawn, and rook. It was going to die regardless. I played Bxd4 trying to defend it, but that was the wrong instinct. The engine says **Qxf5**: accept the knight is lost and grab Black's bishop as compensation. After the follow-up trades it would be a rook and bishop each with Black up two pawns. Still losing, but the game goes on. Instead, Bxd4 took a pawn while my knight got captured for nothing, and the position fell apart.

---

### Pattern 3: Ignoring Opponent Threats

**Game 6 vs Valet22600: Failing to convert a winning position**

I was up a piece in this game and needed to keep my king safe to convert the win. Instead I made it worse.

<figure>
  <img src="{{ '/assets/images/2026-03-19/game6_ply35.png' | relative_url }}" alt="Game 6: Nf3 needed">
  <figcaption>Before 18. g3??: Knight on d2 and target square f3 highlighted. Nf3 keeps the kingside solid.</figcaption>
</figure>

The engine says **Nf3** here, developing the knight to a square where it defends and keeps the kingside solid. Instead I played g3, weakening the pawn structure in front of my king. After g3, Black's best move is **Rxg3+!**, a rook sacrifice that rips open the kingside: fxg3 Qxg3+ Kh1 Qxh3+ and the attack is devastating. Black missed this and played Qe5 instead.

<figure>
  <img src="{{ '/assets/images/2026-03-19/game6_ply37.png' | relative_url }}" alt="Game 6: Still Nf3">
  <figcaption>Before 19. Rac1??: Same highlights. Nf3 is still the key defensive move.</figcaption>
</figure>

Even after Black missed the rook sacrifice, the engine still says **Nf3**. Instead I played **Rac1**, a move that does nothing to address the weak kingside. That took me from +4.2 to mate in 7. Black didn't play accurately either, and the eval drifted back to +0.9 in my favour. But then I played **g4**, allowing **Rxg4+** which forced me to exchange my queen for a rook. From there it was over.

---

### Pattern 4: Missed Tactics

**Game 2 vs VanDerTuesel: Missed Nxd4+ capture with check**

<figure>
  <img src="{{ '/assets/images/2026-03-19/game2_ply36.png' | relative_url }}" alt="Game 2: Nxd4+ fork">
  <figcaption>Before 18...Rc4??: Knight on e6 and bishop on d4 highlighted. Nxd4+ captures the bishop with check.</figcaption>
</figure>

This was a bullet game and I was in a time scramble: 10 seconds on my clock versus my opponent's minute. I was winning (-5.0 eval) but the clock was the real enemy. On move 15, White's knight on b5 was hanging and I could have taken it, but I played **Rac8** instead. Three moves later, my knight on e6 could have played **Nxd4+**, capturing the bishop and giving check to the king on c2. The c3 pawn can't recapture because it's pinned to the king by my rook on c8. After Kd1, the knight hops to b3 attacking the rook on a1. White has to move the rook, and I've won a bishop for nothing. The full line is Nxd4+ Kd1 Nb3 Ra3 Ra8. Instead I played Rc4, which did nothing useful. The next move I missed **Bxa4+**, winning a pawn with check. The point of these missed tactics is the same: I'm not scanning for checks and captures before I move, and I'm not noticing when pins create opportunities.

---

### The Verdict

My suspicion was right: these are mostly simple blunders. Looking at the data:

- **72% of blunders happened in playable positions.** These aren't positions where I was already lost. These are positions where the game was still competitive and I threw it away.
- **30% of blunders had a simple capture as the best move.** I'm not scanning the board for captures before I move.
- **The middlegame is my weakest phase** (50% of blunders). My openings are okay, but once the position gets complicated I start missing things.

---

### What I'm Going to Work On

One thing. Just one thing, because if I fix this it addresses most of these patterns:

**Before every move, check all captures.**

Can I take something? Can they take something? If the answer to either question is yes, I need to evaluate whether that changes my plan. Games 1, 2, 3, 4, and 7 all featured positions where I had a winning capture and didn't see it. That's 5 out of 7 games where checking for captures would have changed the result.

I need to always be asking myself: "What is my opponent threatening?" Games 5 and 6 were lost because I ignored threats. In Game 5 the knight was attacking my queen. In Game 6 the queen was threatening checkmate. Both times I played a move that had nothing to do with the threat.

---

### Further Reading

- [3 Tips To Avoid Blunders](https://www.chess.com/article/view/3-tips-to-avoid-blunders)
- [The Truth About Checks, Captures, Threats](https://www.chess.com/blog/GaborHorvath/the-truth-about-checks-captures-threats)
- [How to Stop Blunders: The Ultimate Grandmaster Guide](https://www.chess.com/blog/Avetik_ChessMood/how-to-stop-blunders-the-ultimate-grandmaster-guide)
