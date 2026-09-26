# Vizualizări

## Ce e aici

| Fișier | Ce e | Rulează acum? |
|---|---|---|
| `aria-triunghiului.html` | demo **interactiv** — tragi de vârfuri, ariile se recalculează | **da**, dublu-click pe fișier |
| `manim/aria_triunghiului.py` | scena **Manim** — sursa clipului | da |
| `manim/aria-triunghiului.mp4` | clipul randat, 720p, 35 s | **da**, e gata |
| `lib/` | JSXGraph 1.13.3, salvat local | — |

Demo-ul HTML nu are nevoie de internet și nu instalează nimic: JSXGraph e salvat în `lib/`,
deci merge și pe un laptop fără rețea, în timpul lecției.

## De ce două implementări ale aceleiași idei

Ca să se vadă diferența pe același conținut.

**Clipul Manim** demonstrează: înălțimea taie triunghiul în două triunghiuri dreptunghice,
fiecare rotit cu $180°$ umple exact cealaltă jumătate a dreptunghiului său, deci
aria $= b \cdot h : 2$. E o demonstrație, are o ordine, se privește.

**Demo-ul interactiv** nu demonstrează nimic — pune o întrebare. Tragi de $C$ de-a lungul
paralelei la bază și aria pur și simplu nu se mișcă, oricât ai deforma triunghiul. Nu poți
„privi" răspunsul; trebuie să-ți dai seama de ce.

Pentru Tomas, a doua variantă e aproape sigur cea care prinde. Prima e mai bună când vrei să
fixezi *de ce* e adevărată formula, după ce a văzut *că* e adevărată.

## Unealta potrivită pentru fiecare lucru

- **JSXGraph** — geometrie plană interactivă. Exact cazul nostru: puncte care se trag, lungimi
  și unghiuri care se recalculează, construcții. Open source, un singur fișier, fără build,
  fără server. Pentru lecțiile 1–3 din blocul de geometrie, asta e unealta.
- **Three.js** — intuiția ta e bună, dar e **prea devreme**. Three.js e WebGL 3D: pentru puncte,
  drepte și unghiuri în plan ar însemna să construiești de la zero ce-ți dă JSXGraph gata făcut.
  Unde chiar plătește: **capitolul de volume** (Litera p224–228) — desfășurarea cubului în plan,
  paralelipipedul dreptunghic, umplerea unei cutii cu cuburi unitate. Acolo 3D-ul e conținutul,
  nu decorul, iar o figură pe care o rotești cu mouse-ul face ce un desen pe tablă nu poate.
  Aș păstra Three.js pentru momentul ăla.
- **GeoGebra** — dacă vrei ceva interactiv în cinci minute, fără cod. Mai puțin control, dar
  zero efort. Bun pentru improvizat în timpul orei.
- **Manim** — narațiune vizuală liniară. Merită doar pentru ideile care au o *ordine* și pe
  care le reiei de mai multe ori, nu pentru explorare.
- **Motion Canvas** — alternativă la Manim, în TypeScript, cu editor și scrubbing în browser.
  Mai comod de iterat decât Manim dacă ajungem să facem mai multe clipuri.

## Clipul Manim

Randat: `manim/aria-triunghiului.mp4` — 720p30, 35 de secunde, 926 KB. Nu e nevoie să-l
regenerezi ca să-l vezi.

Mediul e instalat și funcțional pe mașina asta: **Manim Community v0.21.0**, într-un venv la
`~/.venvs/manim`. Ca să-l randezi din nou, după o modificare în `.py`:

```sh
cd propuneri/vizualizari/manim
~/.venvs/manim/bin/manim -qm aria_triunghiului.py AriaTriunghiului
```

`-qm` = 720p30 (rapid, ~40 s). Pentru 1080p60: `-qh`. Fișierul apare în
`media/videos/aria_triunghiului/…` — directorul `media/` e în `.gitignore`, doar mp4-ul final
e ținut în repo.

Scena folosește doar `Text(...)`, fără `MathTex`, deci **nu are nevoie de LaTeX** — asta scutește
o instalare de ~2 GB. Dacă vrei formule mai frumoase și instalezi LaTeX, `Text` se poate înlocui
cu `MathTex`.
