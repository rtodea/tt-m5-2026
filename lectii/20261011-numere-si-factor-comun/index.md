# Probleme din Aritmetică de Artur Bălăuca: Numere și Factor comun

Culegere: `culegeri/artur-balauca-artimetica-clasa-a-v-a/atptcde-00-19.PDF` (p18) și `atptcde-20-35.PDF` (p20)

## 72/p18: Etapa locală, Botoșani, 2006

### a) $\overline{ab} + \overline{bc} + \overline{ca} = \overline{abc}$

Determinați numerele naturale de forma $\overline{abc}$, în baza 10, știind că $\overline{ab} + \overline{bc} + \overline{ca} = \overline{abc}$.

**Rezolvare:**

Partea stângă este $11(a + b + c)$ (ca la 43/p16), deci:

$$
11a + 11b + 11c = 100a + 10b + c \Rightarrow b + 10c = 89a
$$

Cum $b + 10c \leq 9 + 90 = 99$, avem $89a \leq 99$, deci $a = 1$:

$$
b + 10c = 89 \Rightarrow c = 8,\ b = 9
$$

Numărul este $\overline{abc} = 198$. Verificare: $19 + 98 + 81 = 198$.

### b) Produs de două numere consecutive

Arătați că numărul $n = \underbrace{11\ldots1}_{2006 \text{ ori}}\underbrace{22\ldots2}_{2006 \text{ ori}}$ se poate scrie ca un produs de două numere naturale consecutive.

**Rezolvare:**

Notăm $R = \underbrace{11\ldots1}_{2006 \text{ ori}}$. Atunci $\underbrace{22\ldots2}_{2006} = 2R$ și:

$$
n = R \cdot 10^{2006} + 2R = R \cdot (10^{2006} + 2)
$$

Dar $10^{2006} = \underbrace{99\ldots9}_{2006} + 1 = 9R + 1$, deci:

$$
n = R \cdot (9R + 3) = 3R \cdot (3R + 1)
$$

$$
n = \underbrace{33\ldots3}_{2006 \text{ ori}} \cdot \underbrace{33\ldots34}_{2006 \text{ cifre}}
$$

## 4/p20: $a + b + c$ se divide cu 369

Se dau numerele: $a = 1 + 2 + 3 + \ldots + 9$; $b = 11 + 22 + 33 + \ldots + 99$; $c = 111 + 222 + 333 + \ldots + 999$. Fără a efectua adunarea să se arate că numărul $a + b + c$ se divide cu 369.

**Rezolvare:**

Dăm factor comun:

$$
b = 11 \cdot (1 + 2 + \ldots + 9) = 11 \cdot a, \qquad c = 111 \cdot (1 + 2 + \ldots + 9) = 111 \cdot a
$$

$$
a + b + c = a \cdot (1 + 11 + 111) = 45 \cdot 123 = (9 \cdot 5) \cdot (3 \cdot 41) = (9 \cdot 41) \cdot 15 = 369 \cdot 15
$$

## 6/p20: Calcul cu factor comun

Calculați: $4a + 18b + 15c + 18d$, știind că $2a + 3b = 50$ și $4b + 5c + 6d = 120$.

**Rezolvare:**

Despărțim $18b = 6b + 12b$:

$$
4a + 18b + 15c + 18d = (4a + 6b) + (12b + 15c + 18d) = 2 \cdot (2a + 3b) + 3 \cdot (4b + 5c + 6d)
$$

$$
= 2 \cdot 50 + 3 \cdot 120 = 100 + 360 = 460
$$

## 11/p20: Produs de trei numere consecutive

Să se scrie numărul $n = (2001^3 - 2001^2) + (2001^2 - 2001)$ ca produsul a trei numere naturale consecutive.

**Rezolvare:**

$$
n = 2001^3 - 2001 = 2001 \cdot (2001^2 - 1) = 2001 \cdot (2001 - 1) \cdot (2001 + 1)
$$

$$
n = 2000 \cdot 2001 \cdot 2002
$$

(Am folosit $a^2 - b^2 = (a - b)(a + b)$ de la 1/p19.)

## 10/p20: Puteri cu factor comun

Calculați: $(3^7 - 3^6) \cdot (3^6 - 3^5) \cdot (3^5 - 3^4) : (3^5)^3$.

**Rezolvare:**

Scoatem factor comun din fiecare paranteză:

$$
3^7 - 3^6 = 3^6 \cdot (3 - 1) = 2 \cdot 3^6, \quad 3^6 - 3^5 = 2 \cdot 3^5, \quad 3^5 - 3^4 = 2 \cdot 3^4
$$

$$
2 \cdot 3^6 \cdot 2 \cdot 3^5 \cdot 2 \cdot 3^4 : 3^{15} = 2^3 \cdot 3^{15} : 3^{15} = 8
$$
