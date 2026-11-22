---
tipo: concetto
importanza_esame: alta
prerequisiti: ["process-vhdl", "oggetti-vhdl", "delta-cycle"]
fonti_pdf: ["5-Descrizione Comportamentale.pdf#page=11", "5-Descrizione Comportamentale.pdf#page=12", "5-Descrizione Comportamentale.pdf#page=13", "5-Descrizione Comportamentale.pdf#page=14", "5-Descrizione Comportamentale.pdf#page=19"]
---

# Variabili e segnali in un process

## Definizione · [[5-Descrizione Comportamentale.pdf#page=11|p. 11]]

Dentro un process si possono usare **variabili** (`VARIABLE nome : tipo;`, assegnate con `:=`) per lo **stato** del sottosistema o per **risultati intermedi**. Segnali e variabili portano entrambi un'informazione ma hanno tempificazione opposta:

| | Segnale (`<=`) | Variabile (`:=`) |
|---|---|---|
| effetto | **schedula** una transazione: il nuovo valore arriva al più un delta dopo, mai subito | **immediato**: nessuna schedulazione |
| letto subito dopo nello stesso process | vecchio valore | nuovo valore |
| visibilità | tutta l'architecture, comunica fra process | locale al process |

## Derivazioni

### Derivazione — `s_temp` contro `v_temp` · [[5-Descrizione Comportamentale.pdf#page=12|p. 12]]
**Fonte:** due listati con commento a parole. Esempio numerico mio: `A` passa da 4 a 5 al tempo T, e prima valevano `s_temp = 5`, `Y_sig = 6` (situazione stabile con A = 4).

**Con il segnale** `process(A) … s_temp <= A + 1; Y_sig <= s_temp + 1;`:

| Quando | Cosa succede | s_temp | Y_sig |
|---|---|---|---|
| T (attivazione per evento su A) | `s_temp ← 6` schedulato; `Y_sig ← s_temp + 1 = 5 + 1 = 6` (vecchio `s_temp`) | 5 | 6 |
| T + δ | `s_temp` diventa 6; `Y_sig` riceve 6 (nessun cambio) | 6 | 6 |
| dopo | `s_temp` non è nella sensitivity list: il process **non si riattiva** | 6 | **6** (dovrebbe essere 7) |

**Con la variabile** `v_temp := A + 1; Y_var <= v_temp + 1;`:

| Quando | Cosa succede | v_temp | Y_var |
|---|---|---|---|
| T | `v_temp := 6` subito; `Y_var ← 6 + 1 = 7` schedulato | 6 | (6) |
| T + δ | `Y_var` diventa 7 | 6 | **7** ✓ |

È il senso del commento della slide: `Y_sig` «non assumerà mai il valore desiderato» $A + 2$, mentre `Y_var` sì.
> 🧩 Derivazione mia: i valori numerici dell'esempio.

### Derivazione — `tmp` segnale: nessuna variazione su `y` · [[5-Descrizione Comportamentale.pdf#page=13|p. 13]]
**Fonte:** passi descritti nella slide; qui in tabella. Stato iniziale `x = 1`, `tmp = 1`, `y = 0`; evento `x: 1→0` a T.

| Istante | Istruzione | Valore letto | Transazione |
|---|---|---|---|
| T | `tmp <= x;` | x = 0 | tmp: 1→0 a T + δ |
| T | `y <= NOT tmp;` | tmp = **1** (non ancora aggiornato) | y: 0→0 a T + δ (nessun evento) |
| T | `END PROCESS` | — | il process si sospende |
| T + δ | — | — | tmp = 0, y = 0 |

**Che circuito è:** dopo il transitorio, `y` dovrebbe essere `NOT x = 1`, ma resta 0 finché un nuovo evento su `x` non riattiva il process: `y` vale `NOT x` «in ritardo di un evento». Come nel caso precedente, il problema è che `tmp` è letto ma non sta nella sensitivity list.
> 🧩 Derivazione mia: il valore di regime e il confronto con il caso precedente.

### Derivazione — `tmp` variabile: risultato immediato · [[5-Descrizione Comportamentale.pdf#page=14|p. 14]]
**Fonte:** passi descritti nella slide.

| Istante | Istruzione | Effetto |
|---|---|---|
| T | `tmp := in;` | tmp = 0 subito |
| T | `out := NOT tmp;` | out = NOT 0 = 1 subito |

> ⚠️ Contraddizione: `in` e `out` sono parole riservate e non si possono usare come nomi. Inoltre `out` è una variabile locale: il suo valore non esce dal process; per vederlo fuori va assegnato a un segnale (`y <= NOT tmp;`).

### Derivazione — l'`IF` che non vede l'assegnazione · [[5-Descrizione Comportamentale.pdf#page=19|p. 19]]
**Fonte:** «se all'attivazione `x_sig = 0` si prende il ramo 2; con una variabile si eseguirebbe l'istruzione_1».

| | `x_sig` segnale | `x_var` variabile |
|---|---|---|
| `x <= '1'` / `x := '1'` | schedulato a +δ, ora vale ancora '0' | vale '1' subito |
| `IF x = '1'` | falso → **istruzione_2** | vero → **istruzione_1** |

## Spiegazione

Regola pratica: **una variabile è un valore di lavoro del process, un segnale è un filo**. Dentro un process si legge sempre il valore che i segnali avevano **all'attivazione**; i nuovi valori diventano visibili solo dopo la sospensione. Se si ha bisogno subito di un risultato intermedio, si usa una variabile.

## Perché importa

È la domanda d'orale più tipica sulla descrizione comportamentale e l'errore più comune nei progetti (risultati «in ritardo di un ciclo»).

## Connessioni

- [[assegnazione-sequenziale]] — le assegnazioni di segnale hanno effetto alla sospensione
- [[process-vhdl]] — perché le variabili non si condividono fra process
- [[delta-cycle]] — il «+δ» delle tabelle
- [[oggetti-vhdl]] — le tre classi di oggetti
- [[wait-e-sensitivity-list]] — riattivazione del process

## Fonti · [[5-Descrizione Comportamentale.pdf#page=11|p. 11]]–[[5-Descrizione Comportamentale.pdf#page=14|14]], [[5-Descrizione Comportamentale.pdf#page=19|19]]

- [[descrizione-comportamentale-lezione]]

_Aggiornato: 2026-11-22 — creazione_
