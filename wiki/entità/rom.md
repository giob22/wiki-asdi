---
tipo: entità
categoria: dispositivo
---

# ROM (memoria a sola lettura)

## Cos'è · Sintassi [[1-Principali elementi sintattici VHDL.pdf#page=16|p. 16]] · Strutturale [[3-Descrizione Strutturale.pdf#page=9|p. 9]], [[3-Descrizione Strutturale.pdf#page=21|21]]

Memoria il cui contenuto è fisso: dato un indirizzo, restituisce la word memorizzata. Nel corso compare due volte:

| Lezione | Versione | Come è descritta |
|---|---|---|
| 1 | ROM 16×4 (`ROM_16_4`) | costante array di 16 `std_logic_vector(3 downto 0)`, letta con `to_integer(unsigned(address))` |
| 3 | ROM parametrica (`rom`) | entity con generics `width` (bit per word) e `depth` (bit di indirizzo): $2^{depth}$ word di `width` bit |

```vhdl
ENTITY rom IS
  GENERIC( width : positive := 32;
           depth : positive := 4);
  PORT(
    enable  : IN std_logic;
    address : IN std_logic_vector(depth-1 downto 0);
    data    : OUT std_logic_vector(width-1 downto 0) );
END rom;
```

Le istanze della Lezione 3 (`rom_0`: 16×16, `rom_1`: 16×8, `rom_2`: 32×32) sono calcolate passo-passo in [[generics-vhdl]]; la lettura della ROM 16×4 (che restituisce il proprio indirizzo) è in [[array-vhdl]].

## Come si usa nel corso

Esempio di costante array e conversione di tipo (Lezione 1) e di parametrizzazione con i generics (Lezione 3). Le memorie ritornano nella parte di teoria (microprogrammazione, livello microarchitetturale).

## Concetti correlati

- [[array-vhdl]], [[signed-unsigned]], [[generics-vhdl]], [[istanziazione-componenti]]

## Fonti

- [[elementi-sintattici-vhdl-lezione]]
- [[descrizione-strutturale-lezione]]

_Aggiornato: 2026-11-22 — creazione_
