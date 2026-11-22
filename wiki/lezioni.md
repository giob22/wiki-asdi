# Lezioni — Architettura dei Sistemi Digitali

Elenco delle lezioni con gli argomenti del wiki. Per ogni lezione c'è **un punto per ogni pagina del wiki**, con una sintesi di cosa contiene e le pagine PDF da cui viene. I punti seguono l'ordine in cui l'argomento compare per la prima volta nel PDF.
Regola: 1 PDF = 1 lezione, salvo diversa indicazione (lezioni con più PDF vengono unite su richiesta).
Il testo di studio schematico di tutte le lezioni è [[corso-completo]], che è anche la sorgente del sito di studio; i PDF delle lezioni si creano con `output/crea_pdf.py` (cartella `output/pdf/`).

<!-- Formato di ogni lezione:

## Lezione N — Titolo
**PDF:** [[file.pdf]] (pp. 1–N) · **Fonte:** [[pagina-fonte]]

1. [[pagina]] — cosa contiene ([[file.pdf#page=2|p. 2]]–[[file.pdf#page=5|5]]).
2. ...

Esercizi collegati: [[...]]

---
-->

## Lezione 1 — VHDL: principali elementi sintattici
**PDF:** [[1-Principali elementi sintattici VHDL.pdf]] (pp. 1–39) · **Fonte:** [[elementi-sintattici-vhdl-lezione]]

1. [[elementi-lessicali-vhdl]] — case insensitivity, formato libero, commenti, numeri, caratteri, stringhe, bit string (86 in B/O/X), identificatori ([[1-Principali elementi sintattici VHDL.pdf#page=2|p. 2]]–[[1-Principali elementi sintattici VHDL.pdf#page=5|5]]).
2. [[oggetti-vhdl]] — costanti, variabili, segnali: dove si usano e a cosa servono ([[1-Principali elementi sintattici VHDL.pdf#page=6|p. 6]]–[[1-Principali elementi sintattici VHDL.pdf#page=7|7]]).
3. [[tipi-vhdl]] — tipizzazione forte, tipi scalari e composti, interi con range (5 bit per −10…15), enumerazioni ([[1-Principali elementi sintattici VHDL.pdf#page=8|p. 8]], [[1-Principali elementi sintattici VHDL.pdf#page=10|p. 10]], [[1-Principali elementi sintattici VHDL.pdf#page=13|p. 13]]).
4. [[std-logic]] — `bit` e `std_logic` a 9 valori, `std_logic_vector` ([[1-Principali elementi sintattici VHDL.pdf#page=9|p. 9]]).
5. [[signed-unsigned]] — peso numerico dei bit, tipi misti in somma/sottrazione, funzioni di conversione e casting ([[1-Principali elementi sintattici VHDL.pdf#page=11|p. 11]]–[[1-Principali elementi sintattici VHDL.pdf#page=12|12]]).
6. [[array-vhdl]] — array constrained/unconstrained, slice, aggregati, ROM 16×4, tabella di verità di una NAND a 4 valori ([[1-Principali elementi sintattici VHDL.pdf#page=14|p. 14]]–[[1-Principali elementi sintattici VHDL.pdf#page=18|18]]).
7. [[record-vhdl]] — record, formato di un'istruzione ([[1-Principali elementi sintattici VHDL.pdf#page=19|p. 19]]–[[1-Principali elementi sintattici VHDL.pdf#page=21|21]]).
8. [[alias-vhdl]] — alias di una slice e dei flag di un registro di stato ([[1-Principali elementi sintattici VHDL.pdf#page=22|p. 22]]).
9. [[subtype-vhdl]] — subtype, `natural`/`positive`, compatibilità subtype/nuovo tipo ([[1-Principali elementi sintattici VHDL.pdf#page=23|p. 23]]–[[1-Principali elementi sintattici VHDL.pdf#page=24|24]]).
10. [[attributi-vhdl]] — attributi di range, tipi enumerativi, array e segnali; forme d'onda; flip-flop sul fronte di discesa ([[1-Principali elementi sintattici VHDL.pdf#page=25|p. 25]]–[[1-Principali elementi sintattici VHDL.pdf#page=32|32]]).
11. [[operatori-vhdl]] — classi e priorità, esempi di aritmetica, shift, confronti, logica ([[1-Principali elementi sintattici VHDL.pdf#page=33|p. 33]]–[[1-Principali elementi sintattici VHDL.pdf#page=39|39]]).
12. [[vhdl]], [[ieee-std-logic-1164]], [[ieee-numeric-std]] — il linguaggio e i package IEEE ([[1-Principali elementi sintattici VHDL.pdf#page=9|p. 9]], [[1-Principali elementi sintattici VHDL.pdf#page=11|p. 11]]–[[1-Principali elementi sintattici VHDL.pdf#page=12|12]]).

---

## Lezione 2 — VHDL: descrizione Dataflow
**PDF:** [[2-Descrizione Dataflow.pdf]] (pp. 1–12) · **Fonte:** [[descrizione-dataflow-lezione]]

1. [[descrizione-dataflow]] — lo stile dataflow, espressioni e operatori, le tre assegnazioni concorrenti ([[2-Descrizione Dataflow.pdf#page=1|p. 1]]–[[2-Descrizione Dataflow.pdf#page=3|3]]).
2. [[operatori-vhdl]] — priorità, tipi degli operandi, word gate, overloading (aggiornata) ([[2-Descrizione Dataflow.pdf#page=2|p. 2]]–[[2-Descrizione Dataflow.pdf#page=3|3]]).
3. [[assegnazione-concorrente]] — attivazione, concorrenza nell'architecture, target, tre tipi ([[2-Descrizione Dataflow.pdf#page=4|p. 4]]–[[2-Descrizione Dataflow.pdf#page=5|5]]).
4. [[half-adder]] — assegnazione incondizionata ([[2-Descrizione Dataflow.pdf#page=6|p. 6]]).
5. [[assegnazione-condizionata]] — `WHEN … ELSE`, priorità, process equivalente con `IF` ([[2-Descrizione Dataflow.pdf#page=7|p. 7]]–[[2-Descrizione Dataflow.pdf#page=9|9]]).
6. [[buffer-tristate]], [[multiplexer]] — buffer tristate e mux 2:1 con abilitazione tristate e ritardi ([[2-Descrizione Dataflow.pdf#page=8|p. 8]]).
7. [[assegnazione-selezionata]] — `WITH … SELECT`, casi esaustivi ed esclusivi, process equivalente con `CASE`, confronto ([[2-Descrizione Dataflow.pdf#page=10|p. 10]]–[[2-Descrizione Dataflow.pdf#page=12|12]]).

---
