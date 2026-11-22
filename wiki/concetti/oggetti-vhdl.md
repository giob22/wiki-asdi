---
tipo: concetto
importanza_esame: alta
prerequisiti: ["elementi-lessicali-vhdl"]
fonti_pdf: ["1-Principali elementi sintattici VHDL.pdf#page=6", "1-Principali elementi sintattici VHDL.pdf#page=7"]
---

# Oggetti VHDL: costanti, variabili, segnali

## Definizione · [[1-Principali elementi sintattici VHDL.pdf#page=6|p. 6]]–[[1-Principali elementi sintattici VHDL.pdf#page=7|7]]

Un **oggetto** è un'entità VHDL con un **nome** (identificatore unico), un **tipo** e un **valore** che appartiene ai valori leciti del tipo. Le classi di oggetti sono tre:

| Classe | Parola chiave | Dove si usa | Modificabile | Scopo |
|---|---|---|---|---|
| costante | `CONSTANT` | ovunque | no, solo inizializzata | parametri fissi del design |
| variabile | `VARIABLE` | solo nei corpi sequenziali (`process`) | sì | informazione temporanea o stato nei process |
| segnale | `SIGNAL` | solo nei corpi concorrenti (`architecture`) | sì | collegamenti hardware tra moduli |

Variabili e segnali hanno sempre un valore iniziale: esplicito (un valore o un'espressione nella dichiarazione) oppure implicito, fissato dallo standard.

```vhdl
CONSTANT delay : Time := 5 ns;
```

## Derivazioni

### Derivazione — lettura della dichiarazione di costante · [[1-Principali elementi sintattici VHDL.pdf#page=6|p. 6]]
**Fonte:** esempio dato senza commento.

| Parte | Significato |
|---|---|
| `CONSTANT` | classe dell'oggetto |
| `delay` | identificatore |
| `: Time` | tipo (fisico: un tempo) |
| `:= 5 ns` | valore iniziale, obbligatorio per una costante; `ns` è l'unità |

Il simbolo `:=` è l'assegnazione di un valore iniziale (e, nei process, l'assegnazione di variabile); i segnali si assegnano invece con `<=`, come negli esempi di [[array-vhdl]] e [[record-vhdl]].

## Spiegazione

La distinzione importante è tra **variabile** e **segnale**:

- il **segnale** modella un filo: esiste nel corpo concorrente di un'architettura e collega i moduli; si assegna con `<=`;
- la **variabile** è un contenitore locale del codice sequenziale di un process, dove serve per valori intermedi o per lo stato; si assegna con `:=`.

Le slide di questa lezione fissano *dove* si usano e *a cosa servono*. Come e quando un'assegnazione prende effetto in simulazione (segnali aggiornati dopo un delta, variabili subito) è un argomento delle lezioni sulla simulazione e sulla descrizione comportamentale.

La **costante** è il modo per dare un nome a un parametro del progetto (un ritardo, una dimensione, il contenuto di una ROM): il valore si scrive una volta e non cambia.

## Perché importa

Ogni descrizione VHDL dichiara oggetti: scegliere la classe sbagliata (una variabile fuori da un process, un segnale usato come appoggio temporaneo dentro un process) è un errore sia di compilazione sia di progetto. È una domanda tipica d'orale.

## Connessioni

- [[tipi-vhdl]] — ogni oggetto ha un tipo, e il VHDL è fortemente tipizzato
- [[attributi-vhdl]] — i segnali hanno attributi propri (`'EVENT`, `'STABLE`, …) che le variabili non hanno
- [[array-vhdl]] — la ROM è una costante di tipo array

## Fonti · [[1-Principali elementi sintattici VHDL.pdf#page=6|p. 6]]–[[1-Principali elementi sintattici VHDL.pdf#page=7|7]]

- [[elementi-sintattici-vhdl-lezione]]

_Aggiornato: 2026-11-22 — creazione_
