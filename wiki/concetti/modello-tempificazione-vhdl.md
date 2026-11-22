---
tipo: concetto
importanza_esame: alta
prerequisiti: ["assegnazione-concorrente", "simulazione-ad-eventi"]
fonti_pdf: ["4-Tecniche di simulazione e ritardi.pdf#page=11", "4-Tecniche di simulazione e ritardi.pdf#page=12", "4-Tecniche di simulazione e ritardi.pdf#page=13", "4-Tecniche di simulazione e ritardi.pdf#page=14"]
---

# Il modello di tempificazione VHDL: transazioni ed eventi

## Definizione · [[4-Tecniche di simulazione e ritardi.pdf#page=11|p. 11]]–[[4-Tecniche di simulazione e ritardi.pdf#page=13|13]]

In VHDL moduli, assegnazioni e process evolvono **concorrentemente**: l'ordine in cui sono scritti è indifferente. Ogni assegnazione di segnale aggiunge una **transazione** sul segnale target:

- una transazione è una coppia **(value, time)**;
- `value` è il valore da assegnare, **calcolato nell'istante in cui si genera la transazione**;
- `time` è dopo quanto tempo il valore sarà assegnato (il ritardo dell'`AFTER`, oppure 0, cioè un delta).

Quando la transazione scade e il valore **cambia** il segnale si ha un **evento**; se il valore è uguale a quello attuale si ha una **semplice transazione**.

## Derivazioni

### Derivazione — la transazione (1, 12 ns) · [[4-Tecniche di simulazione e ritardi.pdf#page=13|p. 13]]
**Fonte:** «se a = 1 → 0 @ 0 s, `w <= NOT a AFTER 12 NS;` genera una transazione di valore (1, 12ns)».

1. A $t = 0$ c'è un evento su `a` (1→0): l'assegnazione, che legge `a`, si attiva.
2. Si calcola subito il valore: `NOT a = NOT 0 = 1` → `value = 1`.
3. Il ritardo è `AFTER 12 NS` → `time = 12 ns`: la transazione è **(1, 12 ns)**.
4. A $t = 12$ ns `w` passa da 0 a 1: il valore cambia, quindi è un **evento**, e attiva a sua volta le assegnazioni che leggono `w`.

**Verifica di «value calcolato subito»:** se `a` tornasse a 1 a $t = 5$ ns, la transazione già schedulata conserverebbe il valore 1 calcolato a $t = 0$; ne verrebbe aggiunta una nuova (0, 12 ns) per $t = 17$ ns. Come le due interagiscano dipende dal tipo di ritardo ([[ritardi-inertial-transport]]).
> 🧩 Derivazione mia, dalla definizione di transazione della slide.

### Derivazione — la catena di transazioni della descrizione data-flow · [[4-Tecniche di simulazione e ritardi.pdf#page=14|p. 14]]
**Fonte:** figura con le forme d'onda per `a` 1→0 a 0 ns, `b` sempre alto (e `c` alto, come nella figura).

![[vhdl-4-p14-forme-d-onda.png]]
*Le frecce collegano ogni evento alla transazione che genera.*

| t (ns) | Evento | Transazioni generate (value, time) | Evento o solo transazione? |
|---|---|---|---|
| 0 | a: 1→0 | W ← (1, 12), X ← (0, 12) | — |
| 12 | W: 0→1, X: 1→0 | Y ← (1, 12) [c AND W], Z ← (0, 12) [X OR Y con Y = 0] | entrambe eventi |
| 24 | Y: 0→1, Z: 1→0 | Z ← (1, 12) [X OR Y con Y = 1] | evento |
| 36 | Z: 0→1 | — | — |

**Transazione senza evento** (🧩 variante mia): con `c = 0`, a $t = 12$ l'evento su `W` riattiva l'assegnazione di `Y`, che produce `(0, 12)`; ma `Y` vale già 0, quindi a $t = 24$ c'è una transazione e non un evento, e nessuna assegnazione a valle si riattiva.

## Spiegazione

Il modello transazione/evento è il motore del simulatore ad eventi: le transazioni sono gli elementi della coda; solo quelle che cambiano un valore (eventi) svegliano altre assegnazioni. Il fatto che il valore sia calcolato **al momento dell'attivazione** e applicato **dopo il ritardo** è ciò che rende possibile modellare i ritardi di propagazione: la porta «vede» gli ingressi di adesso e mostra il risultato più tardi.

## Perché importa

Serve per spiegare qualsiasi forma d'onda di simulazione e per capire gli attributi basati su eventi e transazioni (`'EVENT` contro `'ACTIVE`, `'STABLE` contro `'QUIET`).

## Connessioni

- [[assegnazione-concorrente]] — chi genera le transazioni
- [[simulazione-ad-eventi]] — come vengono elaborate
- [[delta-cycle]] — transazioni con ritardo nullo
- [[ritardi-inertial-transport]] — cosa succede a transazioni ravvicinate
- [[attributi-vhdl]] — attributi EV e TR

## Fonti · [[4-Tecniche di simulazione e ritardi.pdf#page=11|p. 11]]–[[4-Tecniche di simulazione e ritardi.pdf#page=14|14]]

- [[tecniche-di-simulazione-lezione]]

_Aggiornato: 2026-11-22 — creazione_
