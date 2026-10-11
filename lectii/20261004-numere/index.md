# Probleme din Aritmetică de Artur Bălăuca: Numere

Culegere: `culegeri/artur-balauca-artimetica-clasa-a-v-a/atptcde-00-19.PDF`

## 10/p14: Numere de trei cifre cu cifra unităților 5

**a)** Câte numere naturale de trei cifre în baza 10 au cifra unităților egală cu 5? **b)** Dar care au cifrele distincte?

**Rezolvare:**

a) Numerele sunt de forma $\overline{ab5}$, cu $a \in \{1, 2, \ldots, 9\}$ (9 variante) și $b \in \{0, 1, \ldots, 9\}$ (10 variante):

$$
9 \cdot 10 = 90 \text{ numere}
$$

b) $a \neq 0$ și $a \neq 5$, deci 8 variante pentru $a$. Pentru $b$ rămân cele 10 cifre fără $a$ și fără $5$, deci 8 variante:

$$
8 \cdot 8 = 64 \text{ numere}
$$

## 13/p14: Cel mai mic număr cu suma cifrelor 2001

Să se găsească cel mai mic număr natural care are suma cifrelor egală cu 2001.

**Rezolvare:**

Ca numărul să fie cât mai mic, trebuie să aibă cât mai puține cifre, deci cât mai multe cifre de 9.

$$
2001 = 9 \cdot 222 + 3
$$

Avem nevoie de 222 de cifre de 9 și încă o cifră 3, pe care o punem în față (prima cifră cât mai mică):

$$
n = 3\underbrace{99\ldots9}_{222 \text{ cifre}}
$$

## 14/p14: Zece numere consecutive de forma $5n+1$

Suma a 10 numere naturale consecutive de forma $5n + 1$, $n$ număr natural, este egală cu 1235. Aflați numerele.

**Rezolvare:**

Numerele sunt $5n+1,\ 5(n+1)+1,\ \ldots,\ 5(n+9)+1$. Adunăm:

$$
5 \cdot (n + n+1 + \ldots + n+9) + 10 = 5 \cdot (10n + 45) + 10 = 50n + 235
$$

$$
50n + 235 = 1235 \Rightarrow 50n = 1000 \Rightarrow n = 20
$$

Numerele sunt: $101, 106, 111, 116, 121, 126, 131, 136, 141, 146$.

Verificare: $(101 + 146) \cdot 10 : 2 = 1235$.

## 43/p16: $\overline{ab} + \overline{bc} + \overline{ca} = 88$

Aflați numerele de forma $\overline{abc}$ în sistemul zecimal de numerație știind că $\overline{ab} + \overline{bc} + \overline{ca} = 88$.

**Rezolvare:**

Descompunem în baza 10:

$$
10a + b + 10b + c + 10c + a = 11a + 11b + 11c = 11(a+b+c) = 88 \Rightarrow a + b + c = 8
$$

Toate trei cifrele sunt prima cifră a unui număr de două cifre, deci $a, b, c \geq 1$. Numerele sunt:

- $a=1$: $116, 125, 134, 143, 152, 161$
- $a=2$: $215, 224, 233, 242, 251$
- $a=3$: $314, 323, 332, 341$
- $a=4$: $413, 422, 431$
- $a=5$: $512, 521$
- $a=6$: $611$

În total $6+5+4+3+2+1 = 21$ de numere.

## 44/p16: $\overline{ab} = a \cdot b + a + b$

Aflați numerele de forma $\overline{ab}$ scrise în baza 10 știind că $\overline{ab} = a \cdot b + a + b$.

**Rezolvare:**

$$
10a + b = a \cdot b + a + b \Rightarrow 9a = a \cdot b \Rightarrow a \cdot 9 = a \cdot b
$$

Cum $a \neq 0$, rezultă $b = 9$. Numerele sunt: $19, 29, 39, 49, 59, 69, 79, 89, 99$.

## 45/p16: $\overline{abc1} + \overline{abc} = 2003$

Să se afle numărul $\overline{abc}$ în baza 10 știind că $\overline{abc1} + \overline{abc} = 2003$.

**Rezolvare:**

$\overline{abc1} = 10 \cdot \overline{abc} + 1$, deci:

$$
10 \cdot \overline{abc} + 1 + \overline{abc} = 2003 \Rightarrow 11 \cdot \overline{abc} = 2002 \Rightarrow \overline{abc} = 182
$$

Verificare: $1821 + 182 = 2003$.

## 46/p16: Număr + răsturnatul = 888

Suma dintre un număr natural de trei cifre în baza zece, $\overline{abc}$, și răsturnatul său, $\overline{cba}$, este 888. Aflați numărul $\overline{abc}$.

**Rezolvare:**

$$
100a + 10b + c + 100c + 10b + a = 101(a+c) + 20b = 888
$$

Dacă $a + c \geq 9$, atunci $101(a+c) \geq 909 > 888$. Deci $a + c \leq 8$. Ultima cifră a lui $101(a+c) + 20b$ este ultima cifră a lui $a+c$, deci $a + c = 8$:

$$
808 + 20b = 888 \Rightarrow 20b = 80 \Rightarrow b = 4
$$

Cu $a + c = 8$ și $a, c \geq 1$: $147, 246, 345, 444, 543, 642, 741$.

(Dacă acceptăm $c = 0$, adică răsturnatul $048 = 48$, mai avem și $840$.)

## 71/p18: $7 \cdot \overline{ab} + \overline{ba} = \overline{abba} : 11 + 1$

Să se determine numerele de forma $\overline{ab}$ în baza zece care verifică egalitatea $7 \cdot \overline{ab} + \overline{ba} = \overline{abba} : 11 + 1$. _(Etapa județeană, Hunedoara, 2003)_

**Rezolvare:**

$$
\overline{abba} = 1000a + 100b + 10b + a = 1001a + 110b = 11 \cdot (91a + 10b)
$$

deci $\overline{abba} : 11 = 91a + 10b$. Partea stângă:

$$
7 \cdot (10a + b) + 10b + a = 71a + 17b
$$

Egalitatea devine:

$$
71a + 17b = 91a + 10b + 1 \Rightarrow 7b = 20a + 1
$$

Cum $7b \leq 63$, avem $a \leq 3$:

- $a = 1$: $7b = 21 \Rightarrow b = 3$ ✓
- $a = 2$: $7b = 41$ ✗
- $a = 3$: $7b = 61$ ✗

Deci $\overline{ab} = 13$. Verificare: $7 \cdot 13 + 31 = 122$ și $1331 : 11 + 1 = 121 + 1 = 122$.
