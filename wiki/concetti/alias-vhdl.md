---
tipo: concetto
importanza_esame: bassa
prerequisiti: ["array-vhdl"]
fonti_pdf: ["1-Principali elementi sintattici VHDL.pdf#page=22"]
---

# Alias in VHDL

## Definizione · [[1-Principali elementi sintattici VHDL.pdf#page=22|p. 22]]

La dichiarazione **`ALIAS`** dà un nome alternativo a un oggetto o a una sua parte, per riferirvisi più comodamente. È solo un **renaming**: non crea nessun nuovo oggetto, quindi leggere o scrivere l'alias significa leggere o scrivere la parte originale.

```vhdl
VARIABLE instr : BIT_VECTOR(31 DOWNTO 0);
ALIAS op_code : BIT_VECTOR(7 DOWNTO 0) IS instr(31 DOWNTO 24);

ALIAS c_flag : BIT IS flag_register(3);
ALIAS v_flag : BIT IS flag_register(2);
ALIAS n_flag : BIT IS flag_register(1);
ALIAS z_flag : BIT IS flag_register(0);
```

## Derivazioni

### Derivazione — quali bit sono `op_code` · [[1-Principali elementi sintattici VHDL.pdf#page=22|p. 22]]
**Fonte:** «op_code è l'alias degli 8 bit più significativi di instr».

`instr(31 DOWNTO 24)` contiene gli indici 31, 30, …, 24: $31 - 24 + 1 = 8$ bit, i più a sinistra (più significativi) di un vettore `31 DOWNTO 0`. L'accoppiamento è posizionale: `op_code(7)` è `instr(31)`, …, `op_code(0)` è `instr(24)`. La lunghezza dichiarata dell'alias (8) coincide con quella della slice.

## Spiegazione

Gli alias servono a rendere leggibile un codice che lavora su campi di vettori: invece di `instr(31 DOWNTO 24)` si scrive `op_code`, invece di `flag_register(3)` si scrive `c_flag` (carry). I quattro alias delle slide danno un nome ai flag di un registro di stato: carry (C), overflow (V), negativo (N), zero (Z).

## Perché importa

È uno strumento di leggibilità: utile nel progetto di processori e unità di controllo, dove si estraggono campi da istruzioni e registri.

## Connessioni

- [[array-vhdl]] — l'alias si riferisce a slice ed elementi di array
- [[record-vhdl]] — alternativa: definire un record con campi nominati

## Fonti · [[1-Principali elementi sintattici VHDL.pdf#page=22|p. 22]]

- [[elementi-sintattici-vhdl-lezione]]

_Aggiornato: 2026-11-22 — creazione_
