---
tipo: entità
categoria: standard
---

# Package IEEE numeric_std

## Cos'è · [[1-Principali elementi sintattici VHDL.pdf#page=11|p. 11]]–[[1-Principali elementi sintattici VHDL.pdf#page=12|12]]

Package della libreria `IEEE` che definisce i tipi **`signed`** (complemento a 2) e **`unsigned`** (binario naturale) su vettori di `std_logic`, gli operatori aritmetici su di essi (anche con tipi misti: `natural`, `integer`, `std_logic`) e le funzioni di conversione **`to_integer`**, **`to_signed`**, **`to_unsigned`**. Usa [[ieee-std-logic-1164]], che va importato insieme:

```vhdl
library ieee;
use ieee.std_logic_1164.all;
use ieee.numeric_std.all;
```

## Come si usa nel corso

Serve ogni volta che un vettore di bit va trattato come numero: indici di memorie (la ROM della Lezione 1 usa `to_integer(unsigned(address))`), contatori, sommatori.

## Concetti correlati

- [[signed-unsigned]] — tipi, conversioni e casting
- [[operatori-vhdl]] — somma e sottrazione con tipi misti
- [[array-vhdl]] — indicizzazione di array con un indirizzo convertito

## Fonti

- [[elementi-sintattici-vhdl-lezione]]

_Aggiornato: 2026-11-22 — creazione_
