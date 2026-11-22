---
tipo: concetto
importanza_esame: alta
prerequisiti: ["istanziazione-componenti", "entity-architecture"]
fonti_pdf: ["3-Descrizione Strutturale.pdf#page=28", "3-Descrizione Strutturale.pdf#page=29", "3-Descrizione Strutturale.pdf#page=30", "3-Descrizione Strutturale.pdf#page=31"]
---

# Testbench

## Definizione · [[3-Descrizione Strutturale.pdf#page=28|p. 28]]

Un **testbench** è una design unit VHDL che serve a verificare funzionamento e tempificazione di un progetto. Fa tre cose:

1. dichiara e istanzia il blocco da testare (**DUT**, design under test);
2. applica una sequenza opportuna di **stimoli**;
3. **verifica** che le uscite siano corrette secondo le specifiche.

È un'entity **senza port** (nessun ingresso né uscita), perché nessun altro blocco la istanzia. Il testbench più semplice applica solo gli stimoli e lascia all'utente il controllo delle uscite.

![[vhdl-3-p28-testbench-nibble-comparator.png]]
*Il testbench del nibble comparator: generatori su `a` e `b`, ingressi di cascata fissati, uscite osservate.*

## Derivazioni

### Derivazione — struttura del testbench del nibble comparator · [[3-Descrizione Strutturale.pdf#page=29|p. 29]]–[[3-Descrizione Strutturale.pdf#page=30|30]]
**Fonte:** codice completo.

| Parte | Codice | Ruolo |
|---|---|---|
| entity vuota | `ENTITY nibble_comparator_tb IS END …;` | nessun port |
| component | `COMPONENT comp4 …` | prototipo del DUT |
| binding | `FOR a1 : comp4 USE ENTITY WORK.nibble_comparator(iterative);` | l'istanza `a1` usa l'architecture `iterative` |
| segnali | `a, b`, `eql, lss, gtr, gnd`, `vdd := '1'` | fili verso il DUT |
| DUT | `a1: comp4 PORT MAP (a, b, gnd, vdd, gnd, gtr, eql, lss);` | ingressi di cascata a «uguale» |
| stimoli | `a2: a <= "0000", "1111" AFTER 0500 NS, …;` e `a3: b <= …` | forme d'onda: un'unica assegnazione con più valori, ciascuno con il suo istante |

Gli stimoli sono assegnazioni concorrenti con **una waveform di più elementi**: `a <= v0, v1 AFTER t1, v2 AFTER t2, …` programma tutti i cambi di `a` in una volta sola, a istanti assoluti dall'inizio della simulazione.

> ⚠️ Contraddizione: `gnd` è dichiarato `std_logic` senza valore iniziale, quindi in simulazione vale `'U'` (non `'0'`); andrebbe scritto `SIGNAL gnd : std_logic := '0';`. Nella tabella delle uscite le uscite partono comunque da `'0'`.

### Derivazione — verifica dei casi di test · [[3-Descrizione Strutturale.pdf#page=30|p. 30]]–[[3-Descrizione Strutturale.pdf#page=31|31]]
**Fonte:** commenti del codice (risultato atteso) e tabella delle uscite (risultato simulato).
**Si parte da:** il confronto parte dal bit più significativo: il primo bit diverso decide.

| t (ns) | a | b | Primo bit diverso (da sinistra) | Atteso | Uscite in tabella | Ritardo |
|---|---|---|---|---|---|---|
| 0 | 0000 | 0000 | nessuno | a = b | eql → '1' a 5 | 5 |
| 500 | 1111 | 1110 | bit 0 (ultimo) | a > b | gtr '1' a 544, eql '0' a 548 | 48 (worst) |
| 1500 | 1110 | 1111 | bit 0 | a < b | gtr '0' a 1544, lss '1' a 1548 | 48 (worst) |
| 2500 | 1110 | 1100 | bit 1 | a > b | lss '0' a 2533, gtr '1' a 2537 | 37 |
| 3500 | 1010 | 1100 | bit 2 | a < b | gtr '0' a 3522, lss '1' a 3526 | 26 |
| 4000 | 0000 | 1111 | bit 3 | a < b | nessun cambio (era già a < b) | — |
| 4500 | 1111 | 1111 | nessuno | a = b | eql '1' a 4544, lss '0' a 4548 | 48 (worst) |
| 5000 | 0000 | 1111 | bit 3 (primo) | a < b | eql '0' a 5011, lss '1' a 5015 | 15 (best) |
| 5500 | 0000 | 0000 | nessuno | a = b | lss '0' a 5544, eql '1' a 5548 | 48 |
| 6000 | 1111 | 0000 | bit 3 | a > b | (fuori tabella) | best |

**Lettura:** la catena va dallo stadio del bit 0 a quello del bit 3, che dà l'uscita. Lo stadio del bit più significativo diverso decide, gli stadi sopra di lui (bit uguali) ripetono il verdetto. Più il bit decisivo è a destra, più stadi deve attraversare il verdetto e più lungo è il ritardo: 15 ns se decide il bit 3 («l'ultimo stadio decide»), 26 ns per il bit 2, 37 ns per il bit 1, 48 ns se decide il bit 0 o se i nibble sono uguali (tutti gli stadi). Ogni stadio in più da attraversare aggiunge 11 ns.
> 🧩 Derivazione mia: la regola «+11 ns per stadio» si ricava dalle differenze della tabella (48 − 37 = 37 − 26 = 26 − 15 = 11); la direzione della catena (dal bit 0 al bit 3) è l'unica compatibile con «best case: l'ultimo stadio decide».

**Coerenza dei commenti:** i commenti `a > b (worst case)` ecc. sono il verdetto atteso dopo che la nuova coppia è stata applicata. Il test scambia `a` e `b` (500 ns e 1500 ns) per sollecitare entrambe le uscite.

## Spiegazione

Il testbench è un modulo **solo di simulazione**: non viene sintetizzato, per questo può usare costrutti non sintetizzabili come i ritardi `AFTER` assoluti. Scegliere bene gli stimoli conta quanto scrivere il DUT: qui ogni pattern è pensato per un caso preciso (uguaglianza, decisione sul primo, secondo, terzo o quarto bit), così da misurare il caso peggiore e il migliore.

## Perché importa

L'esame di progetto chiede **progetto + implementazione VHDL + simulazione**: ogni modulo va accompagnato da un testbench che ne mostri il funzionamento.

## Connessioni

- [[istanziazione-componenti]] — istanziazione del DUT con associazione posizionale
- [[component-binding]] — scelta dell'architecture `iterative`
- [[nibble-comparator]] — il DUT dell'esempio
- [[generate-vhdl]] — struttura iterativa che spiega i ritardi

## Fonti · [[3-Descrizione Strutturale.pdf#page=28|p. 28]]–[[3-Descrizione Strutturale.pdf#page=31|31]]

- [[descrizione-strutturale-lezione]]

_Aggiornato: 2026-11-22 — creazione_
