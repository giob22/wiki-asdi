---
tipo: entità
categoria: standard
---

# Package IEEE std_logic_1164

## Cos'è · [[1-Principali elementi sintattici VHDL.pdf#page=9|p. 9]], [[1-Principali elementi sintattici VHDL.pdf#page=11|11]]

Package della libreria `IEEE` che definisce i tipi **`std_logic`** (logica a 9 valori: `'U'`, `'X'`, `'0'`, `'1'`, `'Z'`, `'W'`, `'L'`, `'H'`, `'-'`) e **`std_logic_vector`**, obbligatori nei design sintetizzabili. Si importa con:

```vhdl
library ieee;
use ieee.std_logic_1164.all;
```

## Come si usa nel corso

È importato in testa a ogni design: le porte e i segnali si dichiarano `std_logic` / `std_logic_vector`. Va importato anche quando si usa [[ieee-numeric-std]], che si appoggia su di esso.

## Concetti correlati

- [[std-logic]] — i nove valori e il loro significato
- [[signed-unsigned]] — tipi numerici costruiti su `std_logic`

## Fonti

- [[elementi-sintattici-vhdl-lezione]]

_Aggiornato: 2026-11-22 — creazione_
