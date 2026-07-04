---
layout: post
title: "Blitz Session 1: A Textbook Greek Gift"
date: 2026-07-04 15:00:00 +1000
---

<style>
figure { margin: 1.5em 0 2em; }
figcaption { font-style: italic; color: #555; margin-top: 0.5em; }
table { width: 100%; border-collapse: collapse; margin: 1.5em 0; font-size: 0.9em; }
th, td { border: 1px solid #ddd; padding: 6px 10px; text-align: center; }
th { background-color: #f5f5f5; }
</style>

**Time Control:** 5 min (Blitz) | **Games:** 5 | **Record:** 4W / 0D / 1L

---

### Overview

Five games of 5-minute blitz. Four wins and one loss, and my rating drifted up into the high 590s by the last game.

The loss came first, against Satchatch in a Pirc where I was fine out of the opening and then hung a piece in the middlegame. After that it was four wins in a row. One of them barely counts: aragon-9440 abandoned the game after five moves. The other three were all cases of the opponent handing me the initiative. SANNSTAR threw a bishop at f7 on move four with nothing to back it up, and I just kept the extra piece and converted. Argopo pushed an early queen to f3, I got a comfortable position, and a long scrappy game ended with my a-pawn promoting and a queen-and-rook mate.

The one I want to write up is the win against manuragh112. It's the cleanest Greek Gift I've ever landed: bishop takes h7, knight comes to g5 with check, queen to h5, and mate a few moves later. The opponent actually sped up their own defeat by walking a knight back into a pawn capture that gave me the pawn I needed to finish.

---

### All Games

<table>
<thead>
<tr><th>#</th><th></th><th>Color</th><th>Opponent</th><th>Opening</th><th>Result</th><th>Moves</th><th>Rating</th></tr>
</thead>
<tbody>
<tr><td>1</td><td>🏳️</td><td>Black</td><td>Satchatch (572)</td><td>Pirc Defence</td><td>Loss (resignation)</td><td>29</td><td>567</td></tr>
<tr><td>2</td><td>🏳️</td><td>White</td><td>aragon-9440 (555)</td><td>Alekhine's Defence</td><td>Win (abandoned)</td><td>5</td><td>575</td></tr>
<tr><td>3</td><td>🏳️</td><td>Black</td><td>SANNSTAR (550)</td><td>Pirc / Modern</td><td>Win (resignation)</td><td>34</td><td>583</td></tr>
<tr><td>4</td><td>⚔️</td><td>White</td><td>manuragh112 (576)</td><td>Irregular (1...a5)</td><td>Win (checkmate)</td><td>15</td><td>591</td></tr>
<tr><td>5</td><td>⚔️</td><td>Black</td><td>Argopo (590)</td><td>Pirc Defence</td><td>Win (checkmate)</td><td>48</td><td>599</td></tr>
</tbody>
</table>

---

### Highlight: Win vs manuragh112 (576) as White

<iframe id="15352814" allowtransparency="true" frameborder="0" style="width:100%;border:none;" src="https://www.chess.com/emboard?id=15352814"></iframe><script nonce="chesscom-diagram">window.addEventListener("message",e=>{e['data']&&"15352814"===e['data']['id']&&document.getElementById(`${e['data']['id']}`)&&(document.getElementById(`${e['data']['id']}`).style.height=`${e['data']['frameHeight']+37}px`)})</script>

This one barely felt like a game. Black spent the opening shuffling pawns and their queen around the edge of the board while I built a big centre and pointed everything at the kingside.

**1. e4 a5 2. d4 c6 3. Nf3 Qb6 4. Bd3 e6 5. O-O Nf6 6. Nc3 Bb4 7. a3 Bxc3 8. bxc3 O-O 9. e5 Nd5**

The pieces did all the talking. **1...a5** and **3...Qb6** are just lost tempi, and by the time Black castled I had both bishops, the centre, and a lead in development. **7...Bxc3 8. bxc3** handed me the bishop pair and doubled my c-pawns, but those doubled pawns propped up a huge centre and I was happy to take them. The engine already had me somewhere around five points ahead here.

The move that mattered was **9. e5**. It kicks the knight off f6, and once that knight leaves, nobody is guarding h7.

<figure>
  <img src="{{ '/assets/images/2026-07-04/manuragh112_move18.png' | relative_url }}" alt="Position after 9...Nd5, White to move">
  <figcaption>After 9...Nd5: the f6 knight has stepped aside and h7 is undefended.</figcaption>
</figure>

**10. Bxh7+ Kxh7 11. Ng5+ Kg8 12. Qh5**

This is the Greek Gift in its textbook form. The bishop gives itself up on h7 to drag the king out, the knight jumps to g5 with check, and the queen swings to h5. The king scuttles back to g8, and now the threat is simply Qh7 mate. There's no piece anywhere near the black king to help. Stockfish calls it mate in seven from here.

**12...Nf6**

Black tries to plug the h7 square by bringing the knight back to f6. The problem is what it walks into.

<figure>
  <img src="{{ '/assets/images/2026-07-04/manuragh112_move24.png' | relative_url }}" alt="Position after 12...Nf6, White to move">
  <figcaption>After 12...Nf6: the knight blocks h7 but sits on a square my e5 pawn covers.</figcaption>
</figure>

**13. exf6 Rd8 14. Qxf7+ Kh8 15. Qxg7#**

**13. exf6** is the whole point. My pawn takes the knight, and now that pawn sits on f6 guarding g7. That's the square the queen needs. Black's **13...Rd8** does nothing about the mate, **14. Qxf7+** drives the king to h8, and **15. Qxg7#** finishes it: the queen lands on g7 protected by the f6 pawn, and the king has no square. Bringing the knight to f6 didn't just fail to defend, it gifted me the exact pawn that delivered mate.

<figure>
  <img src="{{ '/assets/images/2026-07-04/manuragh112_move29.png' | relative_url }}" alt="Checkmate after 15.Qxg7#">
  <figcaption>Checkmate. The queen on g7 is defended by the f6 pawn.</figcaption>
</figure>

---

### Reflections

**What went well:**

- Landed the Greek Gift cleanly against manuragh112. Knight off f6, bishop takes h7, knight to g5, queen to h5, and the mate followed on its own.
- Four wins from five, and I punished passive play in three of them. Slow openings, an early queen sortie, and an unsound bishop sacrifice all handed me the initiative.
- Recognised the pattern the moment the f6 knight moved. That's the whole trick with the Greek Gift: it lives or dies on whether the defender can cover h7, and once **9. e5** chased the knight away, nobody could.

**What to work on:**

- The Satchatch loss was even until I blundered. Stockfish had the position roughly level through the opening, and then **13...Nce4** just dropped a piece. That's a blitz mistake: I moved a knight to a square I hadn't checked. Slow down for one second before committing a piece, even with the clock ticking.
- Convert cleaner when I'm winning. The Argopo game was a win but a messy one, full of inaccuracies on both sides and several faster finishes that I walked past before the a-pawn finally promoted. Being up material isn't a reason to stop calculating.

---

### Further Reading

- [Greek Gift Sacrifice](https://www.chess.com/terms/greek-gift-chess)
- [The Principles of the Opening](https://www.chess.com/article/view/the-principles-of-the-opening)
