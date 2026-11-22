---
tipo: concetto
importanza_esame: alta
prerequisiti: ["std-logic", "tipi-vhdl"]
fonti_pdf: ["1-Principali elementi sintattici VHDL.pdf#page=11", "1-Principali elementi sintattici VHDL.pdf#page=12", "1-Principali elementi sintattici VHDL.pdf#page=16"]
---

# signed, unsigned e conversioni fra tipi

## Definizione · [[1-Principali elementi sintattici VHDL.pdf#page=11|p. 11]]–[[1-Principali elementi sintattici VHDL.pdf#page=12|12]]

I bit di uno `std_logic_vector` hanno tutti lo stesso «peso»: il vettore è solo un fascio di fili. I tipi **`signed`** e **`unsigned`** danno ai bit un peso secondo la posizione, cioè un **valore numerico**: `unsigned` è un binario naturale, `signed` è in complemento a 2. Sono definiti nel package [[ieee-numeric-std]], che a sua volta usa [[ieee-std-logic-1164]]: vanno importati entrambi.

```vhdl
library ieee;
use ieee.std_logic_1164.all;
use ieee.numeric_std.all;
signal sig  : signed(2 downto 0);
signal sig1 : unsigned(2 downto 0);
sig  <= "101";   -- sig  = -3
sig1 <= "101";   -- sig1 = 5
```

**Conversioni**:

| Da → a | Come | Tipo di operazione |
|---|---|---|
| integer → signed | `to_signed(i, size)` | funzione di `numeric_std` |
| integer → unsigned | `to_unsigned(i, size)` | funzione |
| signed → integer | `to_integer(s)` | funzione |
| unsigned → integer | `to_integer(u)` | funzione |
| std_logic_vector → signed | `signed(slv)` | type casting |
| std_logic_vector → unsigned | `unsigned(slv)` | type casting |
| signed → std_logic_vector | `std_logic_vector(s)` | type casting |
| unsigned → std_logic_vector | `std_logic_vector(u)` | type casting |

![[vhdl-1-p12-conversioni-tra-tipi.png]]
*Le conversioni fra integer, signed, unsigned e std_logic_vector: funzioni a sinistra, type casting a destra.*

**Tipi misti in somma e sottrazione**: `+` e `-` accettano `unsigned` con `unsigned`, `natural` o `std_logic` (risultato `unsigned`) e `signed` con `signed`, `integer` o `std_logic` (risultato `signed`), in entrambi gli ordini.

## Derivazioni

### Derivazione — `"101"` vale −3 come signed e 5 come unsigned · [[1-Principali elementi sintattici VHDL.pdf#page=11|p. 11]]
**Fonte:** i valori sono dati senza passaggi.
**Si parte da:** in un vettore `(n-1 downto 0)` il bit $k$ pesa $2^k$ se `unsigned`; se `signed` il bit più significativo pesa $-2^{n-1}$.

$$
\begin{aligned}
\text{unsigned}(101) &= 1\cdot 2^2 + 0\cdot 2^1 + 1\cdot 2^0 = 4 + 0 + 1 = 5 && \text{pesi tutti positivi} \\
\text{signed}(101) &= 1\cdot(-2^2) + 0\cdot 2^1 + 1\cdot 2^0 = -4 + 0 + 1 = -3 && \text{il bit 2 pesa } -4
\end{aligned}
$$

**Verifica:** in complemento a 2 il negato di `011` (= 3) è: inverto i bit, `100`, e sommo 1, `101`. Quindi `101` = −3. ✓

> ⚠️ Contraddizione: la slide commenta `sig1 <= "101"` con «(sig=5)»: il valore 5 è di `sig1`.

### Derivazione — l'indirizzo della ROM · [[1-Principali elementi sintattici VHDL.pdf#page=16|p. 16]]
**Fonte:** `dout <= ROM_16_4(to_integer(unsigned(address)));`, con la nota «prima casting in unsigned e poi in intero».

| Passo | Espressione | Tipo | Esempio con `address = "1010"` |
|---|---|---|---|
| 1 | `address` | `std_logic_vector(3 downto 0)` | `"1010"`, solo fili |
| 2 | `unsigned(address)` | `unsigned(3 downto 0)` (casting) | `1010` con pesi 8, 4, 2, 1 |
| 3 | `to_integer(...)` | `integer` (funzione) | 8 + 2 = 10 |
| 4 | `ROM_16_4(10)` | `std_logic_vector(3 downto 0)` | `x"a"` = `"1010"` |

**Perché due passaggi:** dalla figura non c'è una freccia diretta `std_logic_vector → integer`; si passa da `unsigned` (o `signed`), che dice come pesare i bit. Con `signed` lo stesso indirizzo varrebbe −6, fuori dal range 0–15 dell'array.

## Spiegazione

La regola pratica che si legge nella figura: tra **vettori** della stessa lunghezza (std_logic_vector, signed, unsigned) si passa con un **casting**, perché i bit restano gli stessi e cambia solo la loro interpretazione; da e verso **integer** serve una **funzione**, perché il valore va calcolato. Per questo `to_signed` e `to_unsigned` chiedono anche la dimensione `size`: un intero non dice di quanti bit deve essere il vettore.

## Perché importa

Contatori, sommatori, indirizzi di memoria: ogni volta che un vettore di bit va trattato come numero servono questi tipi e queste conversioni. L'esempio della ROM (indice di array calcolato da un indirizzo) è un pattern che ritorna in ogni memoria descritta in VHDL.

## Connessioni

- [[std-logic]] — il tipo base degli elementi di signed e unsigned
- [[ieee-numeric-std]] — il package che li definisce
- [[array-vhdl]] — l'esempio della ROM usa la conversione per indicizzare un array
- [[operatori-vhdl]] — `+` e `-` su tipi misti

## Fonti · [[1-Principali elementi sintattici VHDL.pdf#page=11|p. 11]]–[[1-Principali elementi sintattici VHDL.pdf#page=12|12]], [[1-Principali elementi sintattici VHDL.pdf#page=16|16]]

- [[elementi-sintattici-vhdl-lezione]]

_Aggiornato: 2026-11-22 — creazione_
