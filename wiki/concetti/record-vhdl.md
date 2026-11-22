---
tipo: concetto
importanza_esame: media
prerequisiti: ["tipi-vhdl", "array-vhdl"]
fonti_pdf: ["1-Principali elementi sintattici VHDL.pdf#page=19", "1-Principali elementi sintattici VHDL.pdf#page=20", "1-Principali elementi sintattici VHDL.pdf#page=21"]
---

# Record in VHDL

## Definizione · [[1-Principali elementi sintattici VHDL.pdf#page=19|p. 19]]

Un **record** è una collezione di elementi (campi) **anche di tipo diverso**, ciascuno con un nome. Si accede a un campo con `oggetto.campo`; come per gli array, un valore si scrive con la notazione posizionale (nell'ordine dei campi) o per nome.

```vhdl
TYPE a_new_record_type IS RECORD
  id1, id2      : type_1;
  id3           : array_type_2;
  id4, id5, id6 : record_type_3;
END RECORD;
```

## Derivazioni

### Derivazione — il formato di un'istruzione · [[1-Principali elementi sintattici VHDL.pdf#page=20|p. 20]]–[[1-Principali elementi sintattici VHDL.pdf#page=21|21]]
**Fonte:** codice dato con due commenti generali.

| Riga | Cosa dichiara |
|---|---|
| `TYPE opcode IS (sta, lda, add, sub, and, nop, jmp, jsr)` | enumerazione degli 8 codici operativi |
| `TYPE mode IS RANGE 0 TO 3` | intero a 4 valori: modo di indirizzamento |
| `TYPE address IS BIT_VECTOR (10 DOWNTO 0)` | indirizzo a 11 bit |
| `TYPE instruction_format IS RECORD opc; mde; adr END RECORD` | l'istruzione: codice + modo + indirizzo |
| `SIGNAL instr : instruction_format := (nop, 0, "00000000000")` | valore iniziale posizionale: `opc = nop`, `mde = 0`, `adr` = 11 zeri |
| `instr.opc <= lda; instr.mde <= 2; instr.adr <= "00011110000";` | assegnazione campo per campo |
| `instr <= (lda, 2, "00011110000");` | stessa assegnazione, tutta insieme |

**Verifica:** l'aggregato `(lda, 2, "00011110000")` rispetta l'ordine dei campi (`opc`, `mde`, `adr`) e la lunghezza: `"00011110000"` ha 11 caratteri, come `10 DOWNTO 0`. In binario `00011110000` = 128 + 64 + 32 + 16 = 240.

> ⚠️ Contraddizione: nel codice delle slide `and` è usato come valore di `opcode`, ma è una parola riservata (operatore logico) e non può esserlo; manca il `;` dopo `RANGE 0 TO 3`; `TYPE address IS BIT_VECTOR (10 DOWNTO 0)` va scritto `SUBTYPE address IS BIT_VECTOR (10 DOWNTO 0)` (o come nuovo array `ARRAY (10 DOWNTO 0) OF BIT`). Nel primo esempio la variabile è dichiarata `example_1` ma usata come `instr_1`.

## Spiegazione

Il record raggruppa informazioni eterogenee che viaggiano insieme. L'esempio delle slide è il più tipico: il **formato di un'istruzione** di un processore, dove ogni campo ha un tipo diverso (un codice simbolico, un piccolo intero, un vettore di bit). Scrivere `instr.opc` invece di `instr(15 downto 11)` rende il codice leggibile e controllato dal compilatore.

## Perché importa

Torna quando si descrivono processori e unità di controllo (formato delle istruzioni, microistruzioni con più campi) e, in generale, per raggruppare i segnali di un bus.

## Connessioni

- [[array-vhdl]] — l'altro tipo composto, stessa notazione per gli aggregati
- [[alias-vhdl]] — l'alternativa per dare nomi ai campi di un vettore di bit
- [[tipi-vhdl]] — enumerazioni e interi usati come tipi dei campi

## Fonti · [[1-Principali elementi sintattici VHDL.pdf#page=19|p. 19]]–[[1-Principali elementi sintattici VHDL.pdf#page=21|21]]

- [[elementi-sintattici-vhdl-lezione]]

_Aggiornato: 2026-11-22 — creazione_
