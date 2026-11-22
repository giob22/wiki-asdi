---
tipo: concetto
importanza_esame: alta
prerequisiti: ["oggetti-vhdl", "descrizione-dataflow"]
fonti_pdf: ["2-Descrizione Dataflow.pdf#page=4", "2-Descrizione Dataflow.pdf#page=5", "2-Descrizione Dataflow.pdf#page=6"]
---

# Assegnazione concorrente di segnale

## Definizione · [[2-Descrizione Dataflow.pdf#page=4|p. 4]]–[[2-Descrizione Dataflow.pdf#page=5|5]]

Un'**assegnazione concorrente** è un'assegnazione di segnale (`<=`) scritta nel corpo di un'`architecture`, fuori da ogni process; quelle dentro un `process` si chiamano **sequenziali**. Proprietà:

- si **attiva ogni volta che varia uno dei segnali da cui dipende** il segnale assegnato;
- nel corpo di un'architecture sono **concorrenti fra loro** tutte le assegnazioni di segnale (incondizionate, condizionate, selezionate), tutte le istanziazioni di blocchi e tutti i process;
- il **target** può essere un segnale semplice (`S`), indicizzato (`a(5)`), una slice (`a(5 downto 0)`) o un aggregato;
- ce ne sono tre tipi: **incondizionata** (waveform fissa), **condizionata** (if-then-else, [[assegnazione-condizionata]]), **selezionata** (case, [[assegnazione-selezionata]]).

```vhdl
S <= NOT ((A XOR B) AND C);
S <= A XOR B;
S(0) <= A(0) XOR B(0);
S(3 downto 0) <= A(3 downto 0) XOR B(3 downto 0);
S(1) & S(0) <= A(1 downto 0) XOR B(1 downto 0);
```

> ⚠️ Contraddizione: `S(1) & S(0)` non è un target valido (la concatenazione è un'espressione, non un nome di segnale); la forma corretta è l'aggregato `(S(1), S(0)) <= …`.

## Derivazioni

### Derivazione — tabella di verità di `S <= NOT ((A XOR B) AND C)` · [[2-Descrizione Dataflow.pdf#page=4|p. 4]]
**Fonte:** espressione data come esempio, senza valori.

| A | B | C | A XOR B | (A XOR B) AND C | S |
|---|---|---|---|---|---|
| 0 | 0 | 0 | 0 | 0 | 1 |
| 0 | 0 | 1 | 0 | 0 | 1 |
| 0 | 1 | 0 | 1 | 0 | 1 |
| 0 | 1 | 1 | 1 | 1 | **0** |
| 1 | 0 | 0 | 1 | 0 | 1 |
| 1 | 0 | 1 | 1 | 1 | **0** |
| 1 | 1 | 0 | 0 | 0 | 1 |
| 1 | 1 | 1 | 0 | 0 | 1 |

`S` è 0 solo quando `C = 1` e `A ≠ B`. L'assegnazione dipende da `A`, `B`, `C`: è questa la lista dei segnali che la riattivano.

### Derivazione — XOR su vettori e slice · [[2-Descrizione Dataflow.pdf#page=5|p. 5]]
**Fonte:** quattro assegnazioni senza valori. Esempio con `A = "1100"`, `B = "1010"` (indici `3 downto 0`).

| Bit | 3 | 2 | 1 | 0 |
|---|---|---|---|---|
| A | 1 | 1 | 0 | 0 |
| B | 1 | 0 | 1 | 0 |
| A XOR B | 0 | 1 | 1 | 0 |

- `S(3 downto 0) <= A(3 downto 0) XOR B(3 downto 0)` dà `S = "0110"`: l'operatore logico su vettori lavora **bit a bit** (word gate), cioè sono 4 porte XOR in parallelo.
- `S(0) <= A(0) XOR B(0)` è una sola porta: `0 XOR 0 = 0`.
- Il target aggregato `(S(1), S(0))` riceve i due bit di `A(1 downto 0) XOR B(1 downto 0) = "10"`: `S(1) = 1`, `S(0) = 0`.

### Derivazione — l'ordine delle assegnazioni non conta · [[2-Descrizione Dataflow.pdf#page=6|p. 6]]
**Fonte:** half adder con `Sum` prima di `Carry`.
> 🧩 Derivazione mia: scambiando le due righe dell'half adder (`Carry <= A AND B;` prima di `Sum <= A XOR B;`) il circuito non cambia, perché ogni assegnazione è un blocco hardware indipendente che si attiva sulle variazioni dei propri ingressi, non una istruzione eseguita in sequenza.

## Spiegazione

L'assegnazione concorrente non è un'istruzione «eseguita una volta»: è la descrizione di un **collegamento permanente** fra un'espressione e un segnale, come una porta logica saldata sulla scheda. Per questo:

- non ha senso chiedersi quale assegnazione venga «prima»;
- ogni segnale dovrebbe avere **una sola** assegnazione concorrente (due assegnazioni allo stesso segnale sono due driver in conflitto);
- un'assegnazione concorrente equivale a un process sensibile a tutti i segnali che legge (vedi le equivalenze in [[assegnazione-condizionata]] e [[assegnazione-selezionata]]).

## Perché importa

Capire la concorrenza è il salto mentale principale per chi viene dai linguaggi di programmazione: è la base di tutte le descrizioni dataflow e strutturali, e della semantica della simulazione.

## Connessioni

- [[descrizione-dataflow]] — lo stile di descrizione fatto di assegnazioni concorrenti
- [[assegnazione-condizionata]], [[assegnazione-selezionata]] — le altre due forme
- [[oggetti-vhdl]] — solo i segnali si assegnano in modo concorrente
- [[operatori-vhdl]] — operatori logici bit a bit su vettori
- [[half-adder]] — esempio di assegnazione incondizionata

## Fonti · [[2-Descrizione Dataflow.pdf#page=4|p. 4]]–[[2-Descrizione Dataflow.pdf#page=6|6]]

- [[descrizione-dataflow-lezione]]

_Aggiornato: 2026-11-22 — creazione_
