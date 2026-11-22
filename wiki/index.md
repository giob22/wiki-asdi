# Index — Architettura dei Sistemi Digitali

Catalogo di tutte le pagine del wiki. Formato: `- [[pagina]] — cosa contiene (importanza d'esame)`.
Si aggiorna a ogni ingest; i concetti si raggruppano per area del corso in grassetto.

## Overview
- [[overview]] — panoramica del corso, programma, copertura
- [[lezioni]] — elenco lezioni con gli argomenti in ordine di PDF
- [[avanzamento-studio]] — check-list del programma: da fare / studiato / consolidato
- [[corso-completo]] — il corso in un unico file schematico, nell'ordine delle slide (solo contenuto dei PDF; è la sorgente del sito di studio; PDF di studio con `output/crea_pdf.py`)

## Concetti

**Il VHDL come linguaggio**
- [[elementi-lessicali-vhdl]] — regole lessicali, bit string, identificatori (bassa)
- [[oggetti-vhdl]] — costanti, variabili, segnali (alta)
- [[tipi-vhdl]] — tipizzazione forte, interi con range, enumerazioni (alta)
- [[std-logic]] — `bit`, `std_logic` a 9 valori, `std_logic_vector` (alta)
- [[signed-unsigned]] — tipi numerici di `numeric_std`, conversioni e casting (alta)
- [[array-vhdl]] — array, slice, aggregati, ROM, tabelle di verità (alta)
- [[record-vhdl]] — record, formato di un'istruzione (media)
- [[alias-vhdl]] — alias (bassa)
- [[subtype-vhdl]] — subtype e compatibilità con il tipo base (media)
- [[attributi-vhdl]] — attributi di tipi, array e segnali; eventi e transazioni (alta)
- [[operatori-vhdl]] — classi di operatori, shift, confronti (media)

**Stili di descrizione: dataflow**
- [[descrizione-dataflow]] — lo stile dataflow e le sue assegnazioni (alta)
- [[assegnazione-concorrente]] — attivazione, concorrenza, target (alta)
- [[assegnazione-condizionata]] — `WHEN … ELSE` con priorità (alta)
- [[assegnazione-selezionata]] — `WITH … SELECT`, casi esclusivi (alta)

**Stili di descrizione: strutturale**
- [[descrizione-strutturale]] — gerarchia di moduli e composizione (alta)
- [[entity-architecture]] — interfaccia e implementazione di un modulo (alta)
- [[port-vhdl]] — port e modi `IN`/`OUT`/`BUFFER`/`INOUT` (alta)
- [[generics-vhdl]] — parametri dei moduli e loro priorità (alta)
- [[component-binding]] — component e scelta dell'architecture (media)
- [[istanziazione-componenti]] — `PORT MAP` e `GENERIC MAP` (alta)
- [[generate-vhdl]] — istanze ripetute con `FOR`/`IF GENERATE` (alta)
- [[testbench]] — verifica in simulazione, stimoli, worst/best case (alta)

## Entità

- [[vhdl]] — il linguaggio: definizione, livelli di astrazione, VHDL e Verilog (standard)
- [[ieee-std-logic-1164]] — package di `std_logic` (standard)
- [[ieee-numeric-std]] — package di `signed`/`unsigned` e conversioni (standard)
- [[half-adder]] — semisommatore in dataflow (dispositivo)
- [[buffer-tristate]] — buffer con uscita in alta impedenza (dispositivo)
- [[multiplexer]] — mux 2:1 con abilitazione tristate (dispositivo)
- [[porta-aoi]] — porta complessa AND-OR-INVERT (dispositivo)
- [[rom]] — ROM 16×4 e ROM parametrica (dispositivo)
- [[nibble-comparator]] — comparatore di nibble, DUT del testbench (dispositivo)

## Fonti

- [[elementi-sintattici-vhdl-lezione]] — Lezione 1: VHDL, principali elementi sintattici (39 pagine)
- [[descrizione-dataflow-lezione]] — Lezione 2: VHDL, descrizione dataflow (12 pagine)
- [[descrizione-strutturale-lezione]] — Lezione 3: VHDL, descrizione strutturale (31 pagine)

## Esercizi

_Nessun esercizio ancora._

## Laboratorio

_Nessuna pagina ancora._

## Esame

_Generato con l'operazione ESAME._
