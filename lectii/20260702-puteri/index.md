# Puteri

## Legenda tablei de șah

### Recapitulare tablă de șah

1. Sunt $8\times8 = 64$ pătrățele
2. Sunt numerotate ($1 \ldots 8 \times \texttt{a} \ldots \texttt{h}$)
3. `a1` e negru
4. albele stau pe rândurile 1-2, negrele pe rândurile 7-8
5. regina de alb ajunge pe alb

### Exploatarea puterilor lui 2

1. `a1` $\ldots$ $2^0 = 1$ (convenție)
2. `b1` $\ldots$ $2^1 = 2$
3. ...
64. `h8` $\ldots$ $2^{63}$

## Pătrate perfecte (1...15)

### Ultima cifră a pătratelor perfecte $\{0,1,4,5,6,9\}$

## Ultima cifră a unui număr

$u(a)$ --- ultima cifră a lui $a$

$$
a=192^{203}+703^{203}+457^{203}+368^{203}
$$

Observăm ciclurile (de câte 4).

$$
u(x^n) = u(x^{n \mod 4})
\\
$$
