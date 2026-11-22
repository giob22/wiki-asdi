---
tipo: fonte
titolo: "Il VHDL come linguaggio — principali elementi sintattici"
file_raw: "vhdl/1-Principali elementi sintattici VHDL.pdf"
pagine: "1-39"
data_ingest: 2026-11-22
formato: slide-pdf
argomenti: [elementi lessicali, identificatori, oggetti, tipi, std_logic, signed/unsigned, conversioni, enumerazioni, array, record, alias, subtype, attributi, operatori]
---

# Il VHDL come linguaggio — principali elementi sintattici

## Sommario · [[1-Principali elementi sintattici VHDL.pdf#page=1|p. 1]]–[[1-Principali elementi sintattici VHDL.pdf#page=39|39]]

Prima lezione sul VHDL come linguaggio (slide v1.0 del corso). Parte dalle regole lessicali (case insensitivity, formato libero, commenti, numeri, caratteri, stringhe, bit string) e dagli identificatori, introduce le tre classi di oggetti (costanti, variabili, segnali) e il sistema di tipi fortemente tipizzato: `bit` e `std_logic` a 9 valori, interi con range, `signed`/`unsigned` di `numeric_std` con le conversioni, enumerazioni. Passa poi ai tipi composti, array (constrained/unconstrained, slice, aggregati, una ROM, una tabella di verità indicizzata da un tipo enumerativo) e record (formato di un'istruzione), all'aliasing e ai subtype. Chiude con gli attributi (dei range, dei tipi enumerativi, degli array e dei segnali, con le forme d'onda di un esempio e un flip-flop sul fronte di discesa) e con gli operatori in ordine di priorità, ciascuno con esempi.

## Punti chiave

1. Il VHDL non è case sensitive, è a formato libero; i commenti vanno da `--` a fine riga.
2. Le bit string `B"…"`, `O"…"`, `X"…"` rappresentano lo stesso numero su un numero di bit diverso (86 → 7, 9, 8 bit).
3. Costanti (parametri), variabili (solo nei process, stato e valori temporanei), segnali (solo nelle architecture, collegamenti hardware).
4. Il VHDL è fortemente tipizzato; tipi scalari e composti (array, record).
5. `std_logic` / `std_logic_vector` (9 valori, package `std_logic_1164`) sono obbligatori nei design sintetizzabili.
6. Il range di un intero fissa i bit della sua implementazione (`-10 TO 15` → 5 bit).
7. `signed`/`unsigned` (package `numeric_std`) danno peso numerico ai bit; conversioni con funzioni da/verso `integer`, con casting da/verso `std_logic_vector`.
8. Array constrained/unconstrained, slice, aggregati posizionali, per nome e con `others`; una costante array realizza ROM e tabelle di verità.
9. Record: campi di tipi diversi, utile per il formato delle istruzioni.
10. `ALIAS` rinomina una parte di un oggetto senza crearne uno nuovo.
11. Un subtype è compatibile con il tipo base, un nuovo `TYPE` no.
12. Attributi: `'LEFT`/`'RIGHT`/`'LOW`/`'HIGH`, `'POS`/`'VAL`/`'SUCC`/…, `'RANGE`/`'LENGTH` degli array, attributi dei segnali basati su eventi e su transazioni; `NOT c'STABLE` per il fronte di clock.
13. Operatori in sette classi di priorità; shift logici, aritmetici e rotazioni; confronti lessicografici tra vettori.

## Concetti introdotti

- [[elementi-lessicali-vhdl]]
- [[oggetti-vhdl]]
- [[tipi-vhdl]]
- [[std-logic]]
- [[signed-unsigned]]
- [[array-vhdl]]
- [[record-vhdl]]
- [[alias-vhdl]]
- [[subtype-vhdl]]
- [[attributi-vhdl]]
- [[operatori-vhdl]]
- entità: [[vhdl]], [[ieee-std-logic-1164]], [[ieee-numeric-std]]

## Domande aperte

- Le slide numerano alcune pagine in modo non progressivo (ad es. tre slide «11»): i riferimenti del wiki usano il numero di pagina del PDF.
- Refusi nel codice delle slide, segnalati nelle pagine concetto: enumerazione `('q0', …)` tra apici, `ARAY`, `example_1`/`instr_1`, `and` come valore di enumerazione, `;` mancante, `TYPE address IS BIT_VECTOR`, `T'left = T'high = = 10`, `'LOWS(2)`, `4 ** (-2)` con interi, letterali interi assegnati a `Real`, `rol 2`, «sig=5».
- Il riferimento al Navabi per gli attributi: è il testo di riferimento del corso? Da chiedere/verificare.

## Domande da esame

- Quali sono le classi di oggetti in VHDL? Dove si può usare ciascuna e a cosa serve?
- Differenza tra `bit` e `std_logic`: quali sono i nove valori e perché `std_logic` è obbligatorio nei design sintetizzabili?
- Come si converte uno `std_logic_vector` in un intero? Perché servono due passaggi?
- Quanto vale `"101"` come `signed` e come `unsigned`?
- Quanti bit servono per un `integer range -10 TO 15`? Perché?
- Differenza tra array constrained e unconstrained; cos'è un aggregato e come si usa `others`.
- Differenza tra `TYPE` e `SUBTYPE` (compatibilità con il tipo base).
- Differenza tra evento e transazione; confronta `'STABLE` e `'QUIET`, `'EVENT` e `'ACTIVE`.
- Come si individua un fronte di clock con gli attributi dei segnali?
- Differenza tra `sll`, `sla` e `rol`: calcola `1011 sla 3` e `1011 rol 2`.

_Aggiornato: 2026-11-22 — creazione_
