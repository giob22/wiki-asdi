---
tipo: concetto
importanza_esame: alta
prerequisiti: ["oggetti-vhdl", "operatori-vhdl"]
fonti_pdf: ["2-Descrizione Dataflow.pdf#page=1", "2-Descrizione Dataflow.pdf#page=2", "2-Descrizione Dataflow.pdf#page=3"]
---

# Descrizione dataflow

## Definizione · [[2-Descrizione Dataflow.pdf#page=1|p. 1]]–[[2-Descrizione Dataflow.pdf#page=3|3]] · [[2-Descrizione Dataflow.pdf#page=2|p. 2]]

La **descrizione dataflow** è il livello di astrazione VHDL in cui un circuito è descritto assegnando a ogni segnale il valore di un'**espressione**: il circuito è visto come una combinazione di porte elementari, a cui corrispondono gli operatori del linguaggio (`and`, `or`, `xor`, …). Si usa tipicamente per i **circuiti combinatori**. I costrutti sono le tre **assegnazioni concorrenti** di segnale:

| Assegnazione | Forma | Scelta della waveform |
|---|---|---|
| incondizionata | `s <= espressione;` | fissa |
| condizionata | `s <= w1 WHEN c1 ELSE … ELSE wn;` | if-then-else, con priorità |
| selezionata | `WITH sel SELECT s <= w1 WHEN caso1, …;` | case, casi esclusivi |

**Espressioni**: combinano operandi (segnali, costanti, variabili) con operatori; **non si mescolano segnali e variabili**. I relazionali vogliono operandi dello stesso tipo e danno un `boolean`; gli aritmetici valgono sui tipi numerici; i logici valgono anche su vettori, bit a bit (**word gate**); l'utente può definire operatori e farne l'overloading. Le priorità sono in [[operatori-vhdl]].

## Derivazioni

### Derivazione — perché il dataflow descrive logica combinatoria · [[2-Descrizione Dataflow.pdf#page=4|p. 4]]
**Fonte:** «le assegnazioni concorrenti sono attivate ogni volta che c'è una variazione in uno dei segnali da cui dipende il segnale assegnato».
> 🧩 Derivazione mia, dalla regola di attivazione della slide.

1. Un'assegnazione concorrente `s <= f(a, b, c)` viene rivalutata a **ogni** variazione di `a`, `b` o `c`.
2. Quindi `s` è sempre uguale a `f` calcolata sugli ingressi **attuali** (a meno del ritardo).
3. Un'uscita che dipende solo dai valori attuali degli ingressi è per definizione una **rete combinatoria**.

**Eccezione:** se il segnale compare anche a destra (ad es. `tmp <= d WHEN cond ELSE tmp`, il flip-flop di [[attributi-vhdl]]), l'uscita dipende dal proprio valore precedente e la descrizione ha **memoria**.

## Spiegazione

Il dataflow sta a metà fra la descrizione **strutturale** (componenti e collegamenti) e quella **comportamentale** (process e codice sequenziale): si scrivono equazioni, come in un'algebra booleana, e il sintetizzatore ne ricava le porte. Ogni assegnazione è un pezzo di hardware sempre attivo; l'ordine in cui le assegnazioni compaiono nell'architecture non conta (vedi [[assegnazione-concorrente]]).

## Perché importa

È lo stile più diretto per sommatori, multiplexer, decoder, buffer tristate: le reti combinatorie del corso si scrivono così. All'esame di progetto le parti combinatorie di un sistema sono quasi sempre in dataflow.

## Connessioni

- [[assegnazione-concorrente]] — il meccanismo comune alle tre assegnazioni
- [[assegnazione-condizionata]], [[assegnazione-selezionata]] — le assegnazioni con scelta
- [[operatori-vhdl]] — gli operatori delle espressioni
- [[half-adder]], [[buffer-tristate]], [[multiplexer]] — gli esempi della lezione

## Fonti · [[2-Descrizione Dataflow.pdf#page=1|p. 1]]–[[2-Descrizione Dataflow.pdf#page=4|4]]

- [[descrizione-dataflow-lezione]]

_Aggiornato: 2026-11-22 — creazione_
