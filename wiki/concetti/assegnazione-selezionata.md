---
tipo: concetto
importanza_esame: alta
prerequisiti: ["assegnazione-concorrente", "assegnazione-condizionata"]
fonti_pdf: ["2-Descrizione Dataflow.pdf#page=10", "2-Descrizione Dataflow.pdf#page=11", "2-Descrizione Dataflow.pdf#page=12"]
---

# Assegnazione selezionata (`WITH … SELECT`)

## Definizione · [[2-Descrizione Dataflow.pdf#page=10|p. 10]]–[[2-Descrizione Dataflow.pdf#page=11|11]]

L'**assegnazione selezionata** è un'assegnazione concorrente che sceglie la waveform in base al **valore** di un segnale di selezione, come un costrutto case:

```vhdl
WITH segnale_di_selezione SELECT
  segnale <= waveform_1 WHEN caso_1,
             waveform_2 WHEN caso_2,
             ...
             waveform_n WHEN caso_n;
```

- i casi devono essere **esaustivi** (coprire tutti i valori del segnale di selezione), a meno di usare `OTHERS`;
- i casi devono essere **mutuamente esclusivi**;
- è un'abbreviazione di un process con un `CASE` seguito da `WAIT` sui segnali delle waveform e dell'espressione di selezione.

**Confronto con l'assegnazione condizionata** · [[2-Descrizione Dataflow.pdf#page=12|p. 12]]:

| | Condizionata | Selezionata |
|---|---|---|
| casi | possono sovrapporsi | mutuamente esclusivi |
| valutazione | sequenziale, vince la prima vera | nessun ordine, confronti «in parallelo» |
| equivalenza | se le condizioni sono esclusive diventa una selezionata | — |

## Derivazioni

### Derivazione — perché servono `OTHERS` con `std_logic` · [[2-Descrizione Dataflow.pdf#page=10|p. 10]]
**Fonte:** «i casi devono essere esaustivi (a meno che non si usi un caso OTHERS)».
> 🧩 Derivazione mia, dalla regola della slide e dai 9 valori di [[std-logic]].

Un selettore `sel : std_logic` può assumere 9 valori (`'U'`, `'X'`, `'0'`, `'1'`, `'Z'`, `'W'`, `'L'`, `'H'`, `'-'`). Elencare solo `'0'` e `'1'` copre 2 valori su 9: i casi non sono esaustivi e la descrizione è errata. Con `OTHERS` per l'ultimo caso si coprono i 7 valori restanti.

Per un selettore `std_logic_vector(1 downto 0)` i valori possibili sono $9^2 = 81$: i quattro casi «binari» `"00"`, `"01"`, `"10"`, `"11"` non bastano mai senza `OTHERS`.

### Derivazione — il buffer tristate riscritto con `WITH … SELECT` · [[2-Descrizione Dataflow.pdf#page=12|p. 12]]
**Fonte:** «se tutti i casi di un'assegnazione condizionata sono mutuamente esclusivi, il costrutto è equivalente a un'assegnazione selezionata».
> 🧩 Derivazione mia: applico l'equivalenza al buffer tristate della slide p. 8.

L'unica condizione di `BufOut <= BufIn WHEN Enable = '1' ELSE 'Z';` è `Enable = '1'` e l'`ELSE` copre il resto: i due casi sono esclusivi, quindi

```vhdl
WITH Enable SELECT
  BufOut <= BufIn WHEN '1',
            'Z'   WHEN OTHERS;
```

Il mux con abilitazione tristate, invece, ha condizioni su **due segnali diversi** (`en` e `sel`): non c'è un unico segnale di selezione, quindi per riscriverlo con `WITH … SELECT` bisognerebbe selezionare sulla concatenazione `en & sel` ed elencare le combinazioni.

### Derivazione — process equivalente · [[2-Descrizione Dataflow.pdf#page=11|p. 11]]
**Fonte:** schema generale.

| Parte del `WITH … SELECT` | Parte del process |
|---|---|
| `WITH segnale_di_selezione SELECT` | `CASE segnale_di_selezione IS` |
| `waveform_k WHEN caso_k` | `WHEN caso_k => segnale <= waveform_k;` |
| (attivazione concorrente) | `WAIT` sui segnali delle waveform e della selezione |

> ⚠️ Contraddizione: la slide p. 11 attribuisce l'equivalenza con il `CASE` all'«assegnazione condizionata»; è l'assegnazione **selezionata** (la condizionata corrisponde all'`IF`).

## Spiegazione

Il `WITH … SELECT` descrive una **tabella**: per ogni valore del selettore, cosa va in uscita. Non c'è priorità perché i casi non si sovrappongono, e in hardware corrisponde a un unico multiplexer pilotato dal segnale di selezione. È la forma naturale per mux, decoder, tabelle di verità e uscite di macchine a stati.

## Perché importa

È la seconda assegnazione con scelta del dataflow; capire quando usare l'una o l'altra (priorità sì/no, un selettore o più condizioni) è una domanda tipica e una scelta ricorrente nei progetti.

## Connessioni

- [[assegnazione-condizionata]] — la forma con priorità; equivalente se i casi sono esclusivi
- [[assegnazione-concorrente]] — è una delle tre forme
- [[multiplexer]] — il circuito che un `WITH … SELECT` descrive
- [[std-logic]] — perché i casi «binari» non bastano

## Fonti · [[2-Descrizione Dataflow.pdf#page=10|p. 10]]–[[2-Descrizione Dataflow.pdf#page=12|12]]

- [[descrizione-dataflow-lezione]]

_Aggiornato: 2026-11-22 — creazione_
