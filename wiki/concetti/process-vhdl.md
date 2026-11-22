---
tipo: concetto
importanza_esame: alta
prerequisiti: ["assegnazione-concorrente", "delta-cycle"]
fonti_pdf: ["5-Descrizione Comportamentale.pdf#page=2", "5-Descrizione Comportamentale.pdf#page=3", "5-Descrizione Comportamentale.pdf#page=4", "5-Descrizione Comportamentale.pdf#page=5", "5-Descrizione Comportamentale.pdf#page=10"]
---

# Process

## Definizione · [[5-Descrizione Comportamentale.pdf#page=2|p. 2]]–[[5-Descrizione Comportamentale.pdf#page=5|5]], [[5-Descrizione Comportamentale.pdf#page=10|10]]

Il **process** è uno statement concorrente che contiene **solo istruzioni sequenziali**, eseguite nell'ordine in cui sono scritte. Struttura:

```vhdl
label: PROCESS (segnale_1, ..., segnale_n)      -- label e sensitivity list facoltative
  -- parte dichiarativa: tipi, sottotipi, costanti, variabili, procedure, function (locali)
BEGIN
  -- process body: istruzioni sequenziali
END PROCESS label;
```

Regole:

| Aspetto | Regola |
|---|---|
| contenuto | solo statement sequenziali; `<=` è lecito ed è sequenziale; assegnazioni condizionate/selezionate solo con VHDL 2008 |
| ciclo di vita | esegue il body e **riparte dall'inizio**, come un loop infinito, sospendendosi su una sensitivity list o su un `WAIT` |
| inizializzazione | a $0 + 0\delta$ si eseguono **tutti** i process finché non si sospendono |
| visibilità | vede tutto ciò che è dichiarato nell'architecture; le sue dichiarazioni sono locali |
| comunicazione | **solo tramite segnali**: niente variabili condivise fra process, niente segnali dichiarati dentro un process |

## Derivazioni

### Derivazione — cosa succede all'inizializzazione · [[5-Descrizione Comportamentale.pdf#page=5|p. 5]]
**Fonte:** regole della fase di inizializzazione.
> 🧩 Derivazione mia: applico le regole al process di p. 13 (`tmp <= x; y <= NOT tmp;`, sensibile a `x`).

1. A $0 + 0\delta$ i segnali prendono il valore iniziale (per `std_logic` senza valore esplicito, il default `'U'`).
2. Il process viene eseguito **una volta** anche senza eventi su `x`: schedula `tmp ← x` e `y ← NOT tmp` (con i valori iniziali) per $0 + 1\delta$, poi si sospende alla fine.
3. Da lì in poi si riattiva solo sugli eventi di `x`.

**Conseguenza:** anche un process puramente reattivo produce transazioni al tempo 0; ed è per questo che le assegnazioni concorrenti, «equivalenti a process», sono valutate all'inizio (come nell'esempio dei delta di [[delta-cycle]]).

### Derivazione — perché le variabili non si condividono · [[5-Descrizione Comportamentale.pdf#page=10|p. 10]]
**Fonte:** regola data senza motivazione.
> 🧩 Derivazione mia.

Due process sono concorrenti: il simulatore li esegue in un ordine qualsiasi all'interno dello stesso delta. Se condividessero una variabile (aggiornata **subito**, vedi [[variabili-e-segnali]]), il valore letto dall'uno dipenderebbe da quale process il simulatore ha eseguito prima: il risultato non sarebbe deterministico. I segnali, aggiornati tutti insieme al delta successivo, non hanno questo problema: per questo sono l'unico canale fra process.

## Spiegazione

Un process è una **macchina che dorme e si sveglia**: si sveglia su un evento (sensitivity list o `WAIT`), esegue in tempo di simulazione **nullo** tutte le istruzioni fino alla sospensione, e solo allora i segnali assegnati cambiano (un delta dopo, o dopo l'`AFTER`). Dal punto di vista dell'architecture è un blocco hardware fra gli altri, in parallelo con assegnazioni, istanze e altri process.

## Perché importa

Tutta la logica sequenziale (flip-flop, registri, contatori, FSM) e tutti i testbench si scrivono con process. Gli errori più comuni (sensitivity list incompleta, uso di segnali come variabili) nascono dal non avere chiaro questo ciclo di vita.

## Connessioni

- [[wait-e-sensitivity-list]] — come si sospende e si riattiva
- [[variabili-e-segnali]], [[assegnazione-sequenziale]] — tempificazione nel body
- [[istruzioni-sequenziali]] — cosa si può scrivere nel body
- [[assegnazione-concorrente]] — equivale a un process
- [[delta-cycle]] — quando hanno effetto le assegnazioni

## Fonti · [[5-Descrizione Comportamentale.pdf#page=2|p. 2]]–[[5-Descrizione Comportamentale.pdf#page=5|5]], [[5-Descrizione Comportamentale.pdf#page=10|10]]

- [[descrizione-comportamentale-lezione]]

_Aggiornato: 2026-11-22 — creazione_
