---
tipo: concetto
importanza_esame: alta
prerequisiti: ["descrizione-dataflow", "descrizione-strutturale"]
fonti_pdf: ["5-Descrizione Comportamentale.pdf#page=1", "5-Descrizione Comportamentale.pdf#page=2", "5-Descrizione Comportamentale.pdf#page=15"]
---

# Descrizione comportamentale (behavioral)

## Definizione · [[5-Descrizione Comportamentale.pdf#page=1|p. 1]]–[[5-Descrizione Comportamentale.pdf#page=2|2]]

La **descrizione comportamentale** definisce la funzionalità di un circuito (combinatorio o sequenziale) descrivendone il **comportamento** con un algoritmo: conta *cosa fa*, non *come è implementato*. Il costrutto fondamentale è il **process** ([[process-vhdl]]), che contiene istruzioni **sequenziali** (assegnazioni, `IF`, `CASE`, `LOOP`) ma, nel suo insieme, è uno statement **concorrente** come gli altri dell'architecture.

I tre stili visti finora a confronto:

| Stile | Costrutti | Pensiero |
|---|---|---|
| dataflow | assegnazioni concorrenti | equazioni logiche |
| strutturale | component, port map, generate | schema elettrico |
| comportamentale | process, variabili, istruzioni sequenziali | algoritmo |

## Derivazioni

### Derivazione — un'assegnazione concorrente è un process · [[5-Descrizione Comportamentale.pdf#page=15|p. 15]]
**Fonte:** i due frammenti «sono equivalenti».

| Concorrente | Process equivalente |
|---|---|
| `a <= b;` nell'architecture | `PROCESS (b) BEGIN a <= b; END PROCESS;` |

Perché: un'assegnazione concorrente si attiva a ogni evento sui segnali che legge (qui `b`); il process con `b` nella sensitivity list fa lo stesso: si esegue una volta per evento su `b` e poi si sospende. È la stessa equivalenza già vista nella Lezione 2 per le assegnazioni condizionate (`IF`) e selezionate (`CASE`), vedi [[assegnazione-condizionata]] e [[assegnazione-selezionata]].

## Spiegazione · Introduzione [[1-Introduzione al corso ASDi.pdf#page=6|p. 6]]

Il comportamentale è lo stile più vicino alla programmazione: si possono usare variabili, cicli, condizioni annidate. Due avvertenze (la prima dal PDF di introduzione al corso, la seconda da questa lezione):

- una descrizione comportamentale **potrebbe non essere sintetizzabile** (ad es. un process con `WAIT FOR 4ns`): è lo stile dei **testbench** e dei modelli «placeholder» di componenti di cui non si conosce ancora la struttura;
- la semantica **non è quella del C**: le assegnazioni di segnale in un process hanno effetto solo alla sospensione ([[assegnazione-sequenziale]], [[variabili-e-segnali]]).

## Perché importa

Macchine a stati, contatori, registri e testbench si scrivono quasi sempre con process: è lo stile che si userà di più nei progetti del corso.

## Connessioni

- [[process-vhdl]], [[wait-e-sensitivity-list]] — il costrutto e la sua attivazione
- [[variabili-e-segnali]], [[assegnazione-sequenziale]] — la tempificazione dentro un process
- [[istruzioni-sequenziali]], [[assert-vhdl]] — le istruzioni del process body
- [[descrizione-dataflow]], [[descrizione-strutturale]] — gli altri stili

## Fonti · [[5-Descrizione Comportamentale.pdf#page=1|p. 1]]–[[5-Descrizione Comportamentale.pdf#page=2|2]], [[5-Descrizione Comportamentale.pdf#page=15|15]]

- [[descrizione-comportamentale-lezione]]

_Aggiornato: 2026-11-22 — creazione_
