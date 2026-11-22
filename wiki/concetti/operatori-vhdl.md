---
tipo: concetto
importanza_esame: media
prerequisiti: ["tipi-vhdl", "array-vhdl"]
fonti_pdf: ["1-Principali elementi sintattici VHDL.pdf#page=33", "1-Principali elementi sintattici VHDL.pdf#page=34", "1-Principali elementi sintattici VHDL.pdf#page=35", "1-Principali elementi sintattici VHDL.pdf#page=36", "1-Principali elementi sintattici VHDL.pdf#page=37", "1-Principali elementi sintattici VHDL.pdf#page=38", "1-Principali elementi sintattici VHDL.pdf#page=39"]
---

# Operatori del VHDL

## Definizione · [[1-Principali elementi sintattici VHDL.pdf#page=33|p. 33]]

Classi di operatori in **ordine di priorità** (dalla più alta); le parentesi cambiano l'ordine.

| Classe | Operatori | Significato |
|---|---|---|
| vari | `**` `abs` `not` | esponenziazione, valore assoluto, negazione |
| moltiplicativi | `*` `/` `mod` `rem` | prodotto, divisione, modulo, resto |
| di segno | `+` `-` | segno |
| di addizione | `+` `-` `&` | somma, differenza, **concatenazione** |
| di shift | `sll` `srl` `sla` `sra` `rol` `ror` | shift logici, aritmetici, rotazioni |
| relazionali | `=` `/=` `<` `<=` `>` `>=` | confronti (`/=` è «diverso») |
| logici | `and` `or` `nand` `nor` `xor` `xnor` | operazioni bit a bit |

## Derivazioni

### Derivazione — esponenziazione, valore assoluto, prodotto, divisione, modulo · [[1-Principali elementi sintattici VHDL.pdf#page=34|p. 34]]–[[1-Principali elementi sintattici VHDL.pdf#page=35|35]]
**Fonte:** risultati nei commenti del codice.

| Espressione | Passaggi | Risultato |
|---|---|---|
| `2 ** 8` | $2^8 = 2\cdot2\cdot2\cdot2\cdot2\cdot2\cdot2\cdot2$ | 256 |
| `4 ** (-2)` | $4^{-2} = 1/4^2 = 1/16$ | 0.0625 (solo con base reale) |
| `ABS(-14)` | $\lvert -14\rvert$ | 14 |
| `2 * 8` | | 16 |
| `4.0 / (-8.0)` | $4/(-8) = -1/2$ | −0.5 |
| `9 MOD 7` | $9 = 1\cdot 7 + 2$ | 2 |

> ⚠️ Contraddizione: nelle slide `C` è `Integer`, ma $4^{-2} = 0.0625$ non è un intero: per gli interi l'esponente deve essere non negativo e il valore si ottiene solo con una base reale (`4.0 ** (-2)`). Allo stesso modo `X := 4; Y := -8;` con `X`, `Y` di tipo `Real` vanno scritti `4.0` e `-8.0`: il VHDL non converte da solo un letterale intero in reale.

> 📚 Fonte esterna (standard IEEE 1076): `mod` e `rem` differiscono solo con operandi negativi: il risultato di `rem` ha il segno dell'operando **sinistro**, quello di `mod` il segno del **destro**. Esempio: `(-9) rem 7 = -2`, `(-9) mod 7 = 5`; con operandi positivi coincidono (`9 rem 7 = 9 mod 7 = 2`).

### Derivazione — gli shift di `A = 1011` · [[1-Principali elementi sintattici VHDL.pdf#page=37|p. 37]]
**Fonte:** risultati dati senza passaggi.
**Si parte da:** `sll` fa entrare `0` da destra; `sla` fa entrare da destra una copia del bit meno significativo; `rol` fa rientrare da destra il bit uscito a sinistra. Uno shift di $n$ è $n$ shift di 1.

| Operazione | Passo 1 | Passo 2 | Passo 3 | Slide | Esito |
|---|---|---|---|---|---|
| `A sll 1` | 0110 | | | 0110 | ✓ |
| `A sll 3` | 0110 | 1100 | 1000 | 1000 | ✓ |
| `A sla 1` | 0111 (entra l'LSB `1`) | | | 0111 | ✓ |
| `A sla 3` | 0111 | 1111 | 1111 | 1111 | ✓ |
| `A rol 1` | 0111 (rientra l'MSB `1`) | | | 0111 | ✓ |
| `A rol 2` | 0111 | 1110 (rientra lo `0`) | | 1101 | ✗ |

> ⚠️ Contraddizione: `1011 rol 2 = 1110`. Il valore della slide, `1101`, è `1011 ror 1` (o `rol 3`).

`srl` e `sra` sono i simmetrici verso destra: `1011 srl 1 = 0101`, `1011 sra 1 = 1101` (entra a sinistra una copia del bit più significativo, che per un numero con segno è il segno).

### Derivazione — i confronti · [[1-Principali elementi sintattici VHDL.pdf#page=38|p. 38]]
**Fonte:** otto confronti, tutti `True`, senza motivazione.

| Confronto | Perché è vero |
|---|---|
| `A /= 342.54`, `A = 100.0`, `A > 42.54`, `A >= 100.0` | `A` vale 100.0 |
| `B /= ('1','0',…,'0')` | `B` è tutto zeri, l'altro vettore ha un `1` in testa |
| `B < ('1','0',…,'0')` | confronto **lessicografico** da sinistra: il primo elemento è '0' contro '1', e `'0' < '1'` |
| `C = D` | `BIT_VECTOR(1 to 0)` è un range **vuoto** (1 > 0 con `to`): `C` e `D` sono vettori di lunghezza 0, quindi uguali |
| `C <= B` | un vettore vuoto è minore di qualsiasi vettore non vuoto nell'ordine lessicografico |

> 💡 Connessione: il confronto lessicografico fra vettori non è un confronto numerico: per confrontare numeri si usano [[signed-unsigned]].

### Derivazione — l'espressione logica con tutti gli ingressi a '1' · [[1-Principali elementi sintattici VHDL.pdf#page=39|p. 39]]
**Fonte:** `Y := (A AND (B XNOR C)) NOR D;` con `A = B = C = D = '1'`, risultato non dato.

$$
\begin{aligned}
B \text{ XNOR } C &= 1 \text{ XNOR } 1 = 1 && \text{XNOR vale 1 se gli ingressi sono uguali} \\
A \text{ AND } 1 &= 1 \text{ AND } 1 = 1 && \\
1 \text{ NOR } D &= \overline{1 + 1} = 0 && \text{NOR: negazione dell'OR}
\end{aligned}
$$

Quindi `Y = '0'`.

### Derivazione — concatenazione · [[1-Principali elementi sintattici VHDL.pdf#page=36|p. 36]]
**Fonte:** `sq4 <= sq8(2) & sq8(3) & sq8(4) & sq8(5);`

`&` mette in fila 4 elementi da un bit: il risultato è un vettore di 4 elementi, che si assegna per posizione a `sq4(3 DOWNTO 0)`: `sq4(3) = sq8(2)`, …, `sq4(0) = sq8(5)`. I bit 2…5 di `sq8` finiscono in `sq4` in ordine invertito rispetto a `sq8(5 DOWNTO 2)` (vedi [[array-vhdl]]).

## Spiegazione

Tre osservazioni d'uso:

- `&` (concatenazione) ha la stessa priorità di `+` e `-`: è un operatore «di addizione» sui vettori, molto usato per comporre bus e realizzare shift a mano;
- gli operatori di shift esistono per `bit_vector`; nella pratica, su vettori numerici, si usano le funzioni di [[ieee-numeric-std]] o la concatenazione;
- gli operatori logici lavorano bit a bit su vettori della stessa lunghezza.

> 📚 Fonte esterna (standard IEEE 1076): gli operatori logici hanno tutti la **stessa** priorità e non si possono mescolare senza parentesi: `a and b or c` è un errore, si scrive `(a and b) or c`. Per questo l'esempio della slide usa le parentesi.

## Perché importa

Le espressioni con operatori logici sono il cuore della descrizione dataflow dei circuiti combinatori; shift e concatenazione servono per registri a scorrimento e manipolazione di bus.

## Connessioni

- [[array-vhdl]] — concatenazione e slice
- [[signed-unsigned]] — aritmetica su vettori, somma con tipi misti
- [[attributi-vhdl]] — condizioni come `c = '0' AND NOT c'STABLE`
- [[std-logic]] — gli operatori logici sono definiti anche per `std_logic`

## Fonti · [[1-Principali elementi sintattici VHDL.pdf#page=33|p. 33]]–[[1-Principali elementi sintattici VHDL.pdf#page=39|39]]

- [[elementi-sintattici-vhdl-lezione]]

_Aggiornato: 2026-11-22 — creazione_
