---
layout: post
title: "Win vs DrBarbarossa (321)"
date: 2026-02-22 14:00:00 +1000
---

<style>
figure { margin: 1.5em 0 2em; }
figcaption { font-style: italic; color: #555; margin-top: 0.5em; }
</style>

**Opening:** King's Indian Defence | **Result:** 0-1 (Checkmate in 13) | **Time Control:** 2 min + 1 sec (Bullet) | **Rated**

[View on Chess.com](https://www.chess.com/game/165038272316)

<iframe id="14622511" allowtransparency="true" frameborder="0" style="width:100%;border:none;" src="https://www.chess.com/emboard?id=14622511"></iframe><script nonce="chesscom-diagram">window.addEventListener("message",e=>{e['data']&&"14622511"===e['data']['id']&&document.getElementById(`${e['data']['id']}`)&&(document.getElementById(`${e['data']['id']}`).style.height=`${e['data']['frameHeight']+37}px`)})</script>

---

### Game Overview

Classic 300 Elo bullet. I played the King's Indian Defence against d4. We locked up the centre and White pushed an awful lot of pawns without putting much thought into king safety, which is becoming a pattern I see at this rating. On move 8 I made the thematic **...f5** pawn break. White traded pawns but neglected development, and I punished it with a queen checkmate on move 13.

---

### The f5 Break and the Collapse (Moves 1-13)

**1. d4 Nf6 2. e3 g6 3. f3 Bg7 4. Nd2 O-O 5. g4 d6 6. Nh3 e5 7. d5 Ne8 8. e4 f5 9. gxf5 gxf5 10. exf5 Bxf5 11. Ne4 Bxe4 12. fxe4**

<figure>
  <img src="{{ '/assets/images/2026-02-22-game2/move23.png' | relative_url }}" alt="After 12. fxe4">
  <figcaption>After 12. fxe4: The f-file is wide open and the diagonal to the king is completely clear. White has no pieces defending the kingside.</figcaption>
</figure>

The position after **8...f5** is becoming one of my favourite positions to play. White's f-pawn and g-pawn had already advanced, so I was wondering if my opponent was counting properly: the f5 pawn is defended by both the bishop on c8 and the rook on f8.

We traded pawns and I got the last word, recapturing with the bishop on f5. White hopped their knight into e4 and I was happy to make that trade. Giving up the light-squared bishop invited them to take back with the f-pawn, clearing the f-file for my rook.

After **12. fxe4**, the diagonal from h4 to e1 is completely open. I brought my queen across with **12...Qh4+**. White blundered trying to block the check with **13. Nf2**, not realising my rook on f8 is already staring down that square.

**12...Qh4+ 13. Nf2 Qxf2# 0-1**

<figure>
  <img src="{{ '/assets/images/2026-02-22-game2/move26.png' | relative_url }}" alt="After 13...Qxf2#">
  <figcaption>After 13...Qxf2#: Checkmate. The queen takes the knight on f2, supported by the rook on f8. The king has nowhere to go.</figcaption>
</figure>

---

### Reflections

Another game where my opponent attacked too early and neglected king safety. Pushing f3, g4, e4 without castling left the king stranded in the centre with no defenders. The King's Indian setup keeps delivering these positions at this rating.

**What went well:**

- The thematic ...f5 break at the right moment, opening lines against the exposed king.
- Seeing the bishop trade as a way to clear the f-file.

**Engine notes:**

- The engine flags **7...Ne8** as a miss, suggesting **7...Nxd5** to grab the centre pawn. But in the King's Indian I have no desire to take those centre pawns. I want the centre to stay locked so I can focus on a kingside attack. Taking on d5 opens things up in a way that helps White more than me.
