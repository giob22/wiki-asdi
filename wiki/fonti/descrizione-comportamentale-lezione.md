---
tipo: fonte
titolo: "VHDL Comportamentale"
file_raw: "vhdl/5-Descrizione Comportamentale.pdf"
pagine: "1-27"
data_ingest: 2026-11-22
formato: slide-pdf
argomenti: [process, sensitivity list, wait, variabili, assegnazione sequenziale, if, case, for loop, while loop, assert]
---

# VHDL Comportamentale

## Sommario · [[5-Descrizione Comportamentale.pdf#page=1|p. 1]]–[[5-Descrizione Comportamentale.pdf#page=27|27]]

Quinta lezione sul VHDL (slide v1.1): lo stile **comportamentale**. Il **process** è uno statement concorrente che contiene istruzioni sequenziali; ha sensitivity list facoltativa, parte dichiarativa locale e body. Le slide descrivono l'inizializzazione della simulazione (tutti i process eseguiti fino alla sospensione), i due template alternativi (sensitivity list o `WAIT`), le forme del `WAIT` e l'equivalenza fra sensitivity list e `WAIT ON` in fondo, la visibilità e la comunicazione solo tramite segnali. Il cuore della lezione è la **tempificazione**: le variabili si aggiornano subito, i segnali alla sospensione (esempi `s_temp`/`v_temp`, `tmp`, `x_sig` nell'`IF`); nell'assegnazione sequenziale vale l'ultima assegnazione e un segnale della sensitivity list può riattivare il process. Chiudono le istruzioni sequenziali (`IF`, `CASE` con la XOR a 3 ingressi, `FOR LOOP` con la XOR a N bit, `WHILE`, `EXIT`/`NEXT`) e l'`ASSERT`.

## Punti chiave

1. Il process descrive un comportamento in modo algoritmico; è concorrente verso l'esterno e sequenziale al suo interno.
2. All'inizializzazione tutti i process (e le assegnazioni concorrenti) vengono eseguiti fino alla sospensione.
3. Sensitivity list o `WAIT`, mai entrambi; la sensitivity list equivale a `WAIT ON` in fondo al process.
4. `WAIT FOR`, `WAIT ON`, `WAIT UNTIL`, `WAIT`.
5. Un process comunica solo con segnali; niente variabili condivise, niente segnali dichiarati nel process.
6. Variabile `:=` immediata; segnale `<=` schedulato (almeno un delta dopo).
7. Le assegnazioni di segnale in un process hanno effetto alla sospensione; vale l'ultima; possono riattivare il process.
8. Con i segnali la semantica non è quella del C (l'`IF` legge il valore vecchio).
9. `IF` per casi con priorità, `CASE` per casi esclusivi (qualsiasi tabella di verità), `FOR`/`WHILE` con `EXIT`/`NEXT`.
10. `ASSERT condizione REPORT messaggio SEVERITY livello` segnala `NOT(condizione)`.

## Concetti introdotti

- [[descrizione-comportamentale]]
- [[process-vhdl]]
- [[wait-e-sensitivity-list]]
- [[variabili-e-segnali]]
- [[assegnazione-sequenziale]]
- [[istruzioni-sequenziali]]
- [[assert-vhdl]]
- entità: [[porta-xor]]

## Domande aperte

- Refusi del codice (segnalati con ⚠️): `;` dopo la sensitivity list nello schema, `in`/`out` usati come nomi, process senza sensitivity list né `WAIT` (p. 18–19), `END process_example`, apici mancanti, `END IF` che chiude un `CASE`, `OF Function_3`, `CASE` su intero senza `OTHERS`.
- La slide p. 13 contiene, nascosto sotto il riquadro, un secondo listato (`ingr`, `tmp`, `out`): nel wiki si è riportato solo quello visibile.
- La slide p. 11 riporta nell'intestazione «Corso di Calcolatori Elettronici 2»: è materiale riusato da un altro corso.

## Domande da esame

- Cos'è un process? Perché è uno statement concorrente pur contenendo istruzioni sequenziali?
- Cosa succede all'inizializzazione di una simulazione VHDL?
- Differenza fra process con sensitivity list e process con `WAIT`; perché non si possono usare insieme? A cosa equivale la sensitivity list?
- Differenza fra variabile e segnale dentro un process: spiega gli esempi `s_temp`/`v_temp` e quello dell'`IF` su `x_sig`.
- Cosa succede se un segnale è assegnato due volte nello stesso process?
- Quando si usa `IF` e quando `CASE`? Scrivi una XOR a 3 ingressi con il `CASE` e una a N bit con un `FOR LOOP`.
- A cosa serve l'`ASSERT` e quali livelli di severità esistono?

_Aggiornato: 2026-11-22 — creazione_
