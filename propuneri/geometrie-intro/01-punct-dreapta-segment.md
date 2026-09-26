# Punct, dreaptă, segment, semidreaptă. Numărare

> Lecția 1 din blocul de introducere în geometrie.
> Manual Litera/p178–187 · manual Corint/p140–144.
> Durată estimată: 60 min.

## Ce urmărim

Notațiile trebuie să intre în reflex în primele 15 minute, pentru că restul lecției se sprijină
pe ele. Partea care contează de fapt pentru concurs e a doua: **numărarea**.

## 1. Vocabularul (15 min)

Se desenează pe caiet, nu se dictează.

| Obiect | Notație | Cum arată |
|---|---|---|
| Punct | $A$, $B$, $M$ (majuscule) | un punct marcat |
| Dreaptă | $d$, sau $AB$ | linie fără capete, cu săgeți la ambele capete |
| Semidreaptă | $[AB$ — origine $A$, trece prin $B$ | are **un** capăt |
| Segment | $[AB]$ — capete $A$ și $B$ | are **două** capete |
| Lungimea segmentului | $AB$ (fără paranteze) | un număr |

Trei lucruri de spus apăsat, pentru că se greșesc constant:

1. **$[AB]$ este o mulțime de puncte. $AB$ este un număr.** Paranteza face diferența.
2. **$[AB$ și $[BA$ sunt semidrepte diferite** (origini diferite), dar **$[AB]$ și $[BA]$ sunt
   același segment.**
3. Prin **două** puncte distincte trece **o singură** dreaptă. Prin **un** punct trec o
   infinitate.

Puncte **coliniare** = situate pe aceeași dreaptă. Fiecare punct al unei drepte o taie în două
**semidrepte opuse** (manual Litera/p183).

## 2. Poziții relative (10 min)

Două drepte în plan: **concurente** (un punct comun) sau **paralele** (niciun punct comun), plus
cazul degenerat **identice**. Un punct față de o dreaptă: îi aparține sau nu.

De verificat că înțelege, nu doar că repetă: *„Două drepte distincte pot avea două puncte
comune?"* — Nu, pentru că prin două puncte trece o singură dreaptă, deci ar fi aceeași dreaptă.
Ăsta e primul raționament de tip demonstrație din lecție.

## 3. Numărarea — partea de concurs (25 min)

Aici stă valoarea lecției. Se construiește prin numărare efectivă, nu prin formulă dată de-a gata.

**Întrebarea:** pe o dreaptă se iau $n$ puncte distincte. Câte segmente se formează?

Se desenează și se numără, în ordine:

| $n$ puncte | Segmente | Cum le numeri |
|---|---|---|
| 2 | 1 | $AB$ |
| 3 | 3 | $AB, AC, BC$ |
| 4 | 6 | $3 + 2 + 1$ |
| 5 | 10 | $4 + 3 + 2 + 1$ |

Se vede tiparul: de la primul punct pleacă $n-1$ segmente, de la al doilea $n-2$ noi, ș.a.m.d.
Deci

$$
\text{nr. segmente} = (n-1) + (n-2) + \ldots + 2 + 1 = \frac{n(n-1)}{2}
$$

Suma $1 + 2 + \ldots + (n-1)$ o știe deja — e suma lui Gauss. Merită spus explicit că e aceeași
formulă, ca să vadă că geometria și aritmetica nu sunt sertare separate.

**Al doilea raționament, mai scurt:** un segment e dat de o pereche de puncte. Primul capăt se
alege în $n$ feluri, al doilea în $n-1$, dar fiecare segment a fost numărat de două ori
($AB$ și $BA$), deci $\dfrac{n(n-1)}{2}$.

**Varianta cu semidrepte:** pe aceeași dreaptă, fiecare dintre cele $n$ puncte generează
2 semidrepte, deci $2n$ semidrepte.

## Runda — 8 minute, cronometru pornit

Un punct pentru fiecare răspuns corect. Scorul se notează; adversarul e rezultatul de data
trecută, nimic altceva.

1. Câte segmente determină 6 puncte distincte pe o dreaptă?
2. Câte semidrepte determină aceleași 6 puncte?
3. Pe o dreaptă se iau niște puncte și se formează 28 de segmente. Câte puncte sunt?
4. Punctele $A$, $B$, $C$, $D$ sunt coliniare, în această ordine. Scrie toate segmentele care îl
   conțin pe $B$ ca punct interior.
5. Adevărat sau fals: $[MN] = [NM]$. Dar $[MN = [NM$?
6. Se consideră 5 puncte, oricare trei necoliniare. Câte drepte se pot trasa?

**Răspunsuri:** 1) 15 · 2) 12 · 3) 8, din $\frac{n(n-1)}{2} = 28$ · 4) $[AC]$, $[AD]$ ·
5) Adevărat pentru segmente, Fals pentru semidrepte · 6) 15 — aceeași formulă, altă figură.

Problema 6 e capcana utilă: formula nu depinde de faptul că punctele sunt pe o dreaptă, ci de
faptul că fiecare pereche dă exact un obiect.

## Temă

**Scris** (manual Litera/p182, p185, p187 — exercițiile de la „Exersăm, ne antrenăm, ne
dezvoltăm"): 4 exerciții alese de acolo, plus:

7. Câte segmente determină 12 puncte coliniare?
8. Pe o dreaptă se iau $n$ puncte. Se formează 45 de segmente. Află $n$.
9. $A$, $B$, $C$, $D$, $E$ sunt coliniare în această ordine. Câte dintre segmentele determinate
   de ele îl conțin pe $C$ în interior?

**Pe tabletă/telefon — [Euclidea](https://www.euclidea.xyz/), pachetul Alpha, nivelurile 1.1–1.3:**
*Angle of 60°*, *Perpendicular Bisector*, *Midpoint*. Fără explicații înainte — se descurcă
singur, asta e ideea. Scorul din joc (L și E) se notează, ca să aibă ce bate data viitoare.

## Note pentru Robert

- Dacă la problema 3 se blochează, nu-i da ecuația. Pune-l să încerce $n = 6$ (15 segmente, prea
  puțin), apoi $n = 8$. Căutarea prin încercări e o metodă legitimă și la concurs.
- Greșeala clasică la problema 4 e să scrie și $[AB]$ sau $[BC]$ — acolo $B$ e capăt, nu punct
  interior. Merită insistat, pentru că distincția capăt/interior revine la unghiuri.
- Dacă rămâne timp: *„Într-o clasă, fiecare elev dă mâna cu fiecare. Sunt 28 de strângeri de
  mână. Câți elevi?"* Aceeași problemă, îmbrăcată altfel. Legătura dintre cele două e exact ce
  se cere la concurs.

**Răspunsuri temă:** 7) 66 · 8) $n = 10$ · 9) **4** — un capăt trebuie ales dinaintea lui $C$
(2 variante: $A$ sau $B$), celălalt după $C$ (2 variante: $D$ sau $E$), deci $2 \cdot 2 = 4$:
$[AD]$, $[AE]$, $[BD]$, $[BE]$. Dacă nu vede înmulțirea, pune-l să le enumere — se convinge
singur și rămâne cu metoda.
