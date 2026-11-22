---
tipo: fonte
titolo: "VHDL Dataflow"
file_raw: "vhdl/2-Descrizione Dataflow.pdf"
pagine: "1-12"
data_ingest: 2026-11-22
formato: slide-pdf
argomenti: [espressioni, operatori, assegnazione concorrente, assegnazione incondizionata, assegnazione condizionata, assegnazione selezionata, buffer tristate, multiplexer, half adder]
---

# VHDL Dataflow

## Sommario · [[2-Descrizione Dataflow.pdf#page=1|p. 1]]–[[2-Descrizione Dataflow.pdf#page=12|12]]

Seconda lezione sul VHDL (slide v1.2): come si descrive un sistema digitale con lo stile **dataflow**. Riprende espressioni e operatori (priorità, tipi a cui si applicano relazionali, aritmetici e logici, word gate, concatenazione, overloading), poi introduce l'**assegnazione concorrente** di segnale: dove si scrive, quando si attiva (a ogni variazione di un segnale da cui dipende), cosa è concorrente in un'architecture, quali target ammette. Presenta le tre forme: **incondizionata** (half adder), **condizionata** `WHEN … ELSE` (buffer tristate, mux 2:1 con abilitazione tristate e ritardi; process equivalente con `IF`) e **selezionata** `WITH … SELECT` (casi esaustivi ed esclusivi; process equivalente con `CASE`), e chiude confrontando le ultime due.

## Punti chiave

1. In un'espressione non si mescolano segnali e variabili.
2. Relazionali: stesso tipo, risultato `boolean`; aritmetici: tipi numerici; logici: anche su vettori (word gate); `&` crea array; overloading possibile.
3. Le assegnazioni concorrenti stanno nell'architecture e si attivano a ogni variazione dei segnali da cui dipendono; quelle nei process sono sequenziali.
4. Assegnazioni, istanziazioni di blocchi e process in un'architecture sono tutti concorrenti fra loro.
5. Target: segnale, elemento, slice, aggregato.
6. Tre forme: incondizionata, condizionata (if-then-else), selezionata (case).
7. Condizionata: condizioni sovrapponibili, conta l'ordine, `ELSE` finale obbligatorio; equivale a un process con `IF` e `WAIT` sui segnali delle clausole.
8. Selezionata: casi esaustivi (o `OTHERS`) e mutuamente esclusivi; equivale a un process con `CASE`.
9. Se le condizioni sono esclusive, condizionata e selezionata sono equivalenti.

## Concetti introdotti

- [[descrizione-dataflow]]
- [[assegnazione-concorrente]]
- [[assegnazione-condizionata]]
- [[assegnazione-selezionata]]
- aggiornato: [[operatori-vhdl]]
- entità: [[half-adder]], [[buffer-tristate]], [[multiplexer]]

## Domande aperte

- Refusi delle slide: outline con «assegnazione concorrente» ripetuto, target `S(1) & S(0)` (va scritto come aggregato), `condizione_(n-2)`, apice mancante in `'1`, `END IF` mancante nel process equivalente, «condizionata» al posto di «selezionata» nella slide del `CASE`.
- La tabella delle priorità di questa lezione non riporta gli operatori di shift e `xnor`, presenti nella Lezione 1.

## Domande da esame

- Cos'è una descrizione dataflow e per quali circuiti si usa?
- Quando si attiva un'assegnazione concorrente? Cosa è concorrente nel corpo di un'architecture?
- Differenza fra assegnazione condizionata e selezionata; quando sono equivalenti?
- Scrivi il process equivalente di un'assegnazione condizionata e di una selezionata: cosa va nella sensitivity list?
- Descrivi un buffer tristate e un mux 2:1 con abilitazione tristate; perché conta l'ordine delle condizioni?
- Perché in un `WITH … SELECT` su `std_logic` serve `OTHERS`?

_Aggiornato: 2026-11-22 — creazione_
