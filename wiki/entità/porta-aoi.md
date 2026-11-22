---
tipo: entità
categoria: dispositivo
---

# Porta complessa AOI (AND-OR-INVERT)

## Cos'è · [[3-Descrizione Strutturale.pdf#page=23|p. 23]]–[[3-Descrizione Strutturale.pdf#page=25|25]]

Porta complessa che calcola un AND, poi un OR, poi nega: `o1 = NOT((i1 AND i2) OR i3)`. Le slide la usano per mostrare che un'assegnazione di segnale è uno statement concorrente con il suo timing:

```vhdl
ENTITY AOI IS PORT (
  i1 : IN std_logic;
  i2 : IN std_logic;
  i3 : IN std_logic;
  O1 : OUT std_logic );
--
ARCHITECTURE dataflow OF AOI IS
BEGIN
  o1 <= NOT(i1 AND i2 OR i3) AFTER 3ns;
END dataflow;
```

> ⚠️ Contraddizione: manca `END AOI;` dopo la lista dei port, e in VHDL `i1 AND i2 OR i3` non è ammesso senza parentesi (operatori logici diversi hanno la stessa priorità): si scrive `NOT((i1 AND i2) OR i3)`.

### Derivazione — tabella di verità
> 🧩 Derivazione mia.

| i1 | i2 | i3 | i1 AND i2 | OR i3 | o1 |
|---|---|---|---|---|---|
| – | – | 1 | – | 1 | 0 |
| 1 | 1 | 0 | 1 | 1 | 0 |
| 0 | – | 0 | 0 | 0 | 1 |
| – | 0 | 0 | 0 | 0 | 1 |

`o1` vale 0 se `i3 = 1` oppure se `i1 = i2 = 1`; altrimenti 1. Ogni variazione di un ingresso che cambia il risultato si vede su `o1` dopo 3 ns.

La seconda porta complessa delle slide, `porta_complessa` (`z = (a AND b) OR (c AND NOT a)`), è analizzata in [[assegnazione-concorrente]].

## Come si usa nel corso

Esempio di entity con architecture dataflow (Lezione 3) e di assegnazione concorrente con ritardo.

## Concetti correlati

- [[entity-architecture]], [[assegnazione-concorrente]], [[operatori-vhdl]]

## Fonti

- [[descrizione-strutturale-lezione]]

_Aggiornato: 2026-11-22 — creazione_
