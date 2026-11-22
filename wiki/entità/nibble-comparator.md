---
tipo: entità
categoria: dispositivo
---

# Nibble comparator

## Cos'è · [[3-Descrizione Strutturale.pdf#page=27|p. 27]]–[[3-Descrizione Strutturale.pdf#page=31|31]]

Blocco che segnala se il numero rappresentato da un nibble `a` (4 bit) è **maggiore**, **minore** o **uguale** a quello rappresentato da un nibble `b`. Ha anche tre ingressi di cascata, il verdetto di uno stadio «precedente», per poter comporre comparatori più larghi.

```vhdl
ENTITY nibble_comparator IS
  PORT ( a, b : IN std_logic_vector(3 DOWNTO 0);   -- a and b data inputs
         gt, eq, lt : IN std_logic;                -- previous greater, equal, less than
         a_gt_b,                                   -- a > b
         a_eq_b,                                   -- a = b
         a_lt_b : OUT std_logic);                  -- a < b
END nibble_comparator;
```

Nel testbench l'architecture usata si chiama `iterative`: una catena di stadi da 1 bit. Gli ingressi di cascata sono collegati a «uguale» (`gt = lt = 0`, `eq = 1`), così il verdetto dipende solo dai 4 bit.

### Tempi di risposta misurati
Dalla tabella del testbench: 15 ns se decide il bit più significativo (best case), poi +11 ns per ogni stadio da attraversare, fino a 48 ns se decide il bit 0 o se `a = b` (worst case). Il calcolo è in [[testbench]].

## Come si usa nel corso

È il DUT dell'esempio di testbench (Lezione 3) e un esempio di struttura iterativa adatta al `GENERATE`.

## Concetti correlati

- [[testbench]], [[generate-vhdl]], [[istanziazione-componenti]]

## Fonti

- [[descrizione-strutturale-lezione]]

_Aggiornato: 2026-11-22 — creazione_
