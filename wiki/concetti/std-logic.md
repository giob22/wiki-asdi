---
tipo: concetto
importanza_esame: alta
prerequisiti: ["tipi-vhdl"]
fonti_pdf: ["1-Principali elementi sintattici VHDL.pdf#page=9"]
---

# bit, std_logic e std_logic_vector

## Definizione · [[1-Principali elementi sintattici VHDL.pdf#page=9|p. 9]]

- `bit` è il tipo a due valori `'0'` e `'1'`; `bit_vector` è un array di `bit`.
- `std_logic` è il tipo logico **a 9 valori** del package [[ieee-std-logic-1164]]; `std_logic_vector` è un array di `std_logic`. Si usano al posto di `bit` e `bit_vector` perché un circuito reale ha anche stati diversi da alto e basso (alta impedenza, valore sconosciuto, …).

| Valore | Significato | Valore | Significato |
|---|---|---|---|
| `'U'` | uninitialized | `'W'` | weak unknown |
| `'X'` | unknown (forte) | `'L'` | weak low |
| `'0'` | low (forte) | `'H'` | weak high |
| `'1'` | high (forte) | `'-'` | don't care |
| `'Z'` | high impedance | | |

`STD_LOGIC` e `STD_LOGIC_VECTOR` sono **obbligatori nei design sintetizzabili**.

```vhdl
SIGNAL s1 : std_logic;
SIGNAL s2 : std_logic_vector(7 DOWNTO 0);   -- 8 "fili", s2(7) è il bit più a sinistra
```

## Derivazioni

### Derivazione — quanti fili ha `s2` · [[1-Principali elementi sintattici VHDL.pdf#page=9|p. 9]]
**Fonte:** «segnale composto da 8 fili», dato senza conto.

Il range `7 DOWNTO 0` contiene gli indici 7, 6, 5, 4, 3, 2, 1, 0: sono $7 - 0 + 1 = 8$ elementi, quindi 8 segnali `std_logic`. Con `DOWNTO` l'indice più alto sta a sinistra, la convenzione naturale per un numero binario in cui il bit 7 è il più significativo.
**Verifica:** `s2'LENGTH` = 8 (vedi [[attributi-vhdl]]).

## Spiegazione

I nove valori si leggono a gruppi:

- **forti**: `'0'`, `'1'` e `'X'` (conflitto tra due driver forti, valore indeterminato);
- **deboli**: `'L'`, `'H'` e `'W'`, come un resistore di pull-down o pull-up, che un driver forte può sovrastare;
- **`'Z'`**: alta impedenza, uscita di un buffer tri-state spento;
- **`'U'`**: non inizializzato, il valore iniziale di default di un segnale `std_logic` in simulazione: vederlo in una forma d'onda vuol dire che il segnale non è mai stato assegnato;
- **`'-'`**: don't care, utile per dire al sintetizzatore che un valore non importa.

> 📚 Fonte esterna: la lettura per gruppi (forti/deboli) e il significato di `'U'` come default seguono lo standard IEEE 1164; le slide danno solo l'elenco dei valori.

Rispetto a `bit`, `std_logic` permette di **vedere i problemi** in simulazione: un segnale mai assegnato resta `'U'`, due driver in conflitto danno `'X'`.

## Perché importa

È il tipo che si usa per porte e segnali di **ogni** design del corso, perché è quello richiesto dagli strumenti di sintesi. `bit` compare negli esempi didattici più semplici.

## Connessioni

- [[ieee-std-logic-1164]] — il package che definisce il tipo
- [[signed-unsigned]] — danno un peso numerico ai bit di un vettore di `std_logic`
- [[tipi-vhdl]] — `std_logic` è un tipo enumerazione di 9 caratteri
- [[array-vhdl]] — `std_logic_vector` è un array

## Fonti · [[1-Principali elementi sintattici VHDL.pdf#page=9|p. 9]]

- [[elementi-sintattici-vhdl-lezione]]

_Aggiornato: 2026-11-22 — creazione_
