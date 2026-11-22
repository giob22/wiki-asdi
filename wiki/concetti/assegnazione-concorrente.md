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

### Cosa succede a ogni evento · [[3-Descrizione Strutturale.pdf#page=23|p. 23]]

Quando c'è un evento su uno dei segnali a destra dell'assegnazione: (1) si calcola il nuovo valore del segnale a sinistra; (2) si **schedula una transazione** su quel segnale secondo il timing dell'assegnazione (ad es. `AFTER 3ns`). Come l'istanziazione di un componente, l'assegnazione è sempre «attiva».

### Derivazione — stessa funzione, tempi diversi · [[3-Descrizione Strutturale.pdf#page=24|p. 24]]–[[3-Descrizione Strutturale.pdf#page=25|25]]
**Fonte:** due architecture di `porta_complessa` e la figura delle forme d'onda; la slide dà solo «24 ns contro 36 ns» per una variazione di `c`.

```vhdl
-- concurrent                              -- single_assignment
w <= NOT a AFTER 12 NS;                    z <= (a AND b) or (c AND (NOT a)) AFTER 36 NS;
x <= a AND b AFTER 12 NS;
y <= c AND w AFTER 12 NS;
z <= x OR y AFTER 12 NS;
```

**Stessa funzione:** sostituendo i fili, $z = x + y = a\,b + c\,w = a\,b + c\,\overline{a}$, che è l'espressione di `single_assignment`.

**Variazione di `c`** (percorso più corto): `c` → `y` (12 ns) → `z` (12 ns) = **24 ns** nella prima; 36 ns fissi nella seconda.

**La figura** (`a` scende da 1 a 0 a $t = 0$, con `b = c = 1`):

| t (ns) | Evento | Calcolo | Transazione schedulata |
|---|---|---|---|
| 0 | `a`: 1→0 | `w = NOT 0 = 1`, `x = 0 AND 1 = 0` | `w ← 1` e `x ← 0` a 12 |
| 12 | `w`: 0→1, `x`: 1→0 | `y = c AND w = 1`; `z = x OR y = 0 OR 0 = 0` (y è ancora 0) | `y ← 1` a 24, `z ← 0` a 24 |
| 24 | `y`: 0→1, `z`: 1→0 | `z = x OR y = 0 OR 1 = 1` | `z ← 1` a 36 |
| 36 | `z`: 0→1 | — | — |

![[vhdl-3-p25-porta-complessa-forme-d-onda.png]]
*Forme d'onda dell'architecture `concurrent`.*

Prima e dopo, `z` vale 1 (con `a = 1, b = 1` vale $a\,b = 1$; con `a = 0, c = 1` vale $c\,\overline{a} = 1$), ma fra 24 e 36 ns scende a 0: è un **glitch** (alea statica), dovuto al fatto che `x` si spegne 12 ns prima che `y` si accenda. Con `single_assignment` il valore calcolato a $t = 0$ è ancora 1, quindi non si schedula nessun cambio e il glitch non c'è.
> 🧩 Derivazione mia: la tabella evento per evento e la spiegazione del glitch; la figura della slide mostra il fenomeno senza commentarlo.

**Sanity check:** i tempi della figura (12, 24, 36) sono multipli del ritardo di 12 ns di ciascuna assegnazione.

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

## Fonti · Dataflow [[2-Descrizione Dataflow.pdf#page=4|p. 4]]–[[2-Descrizione Dataflow.pdf#page=6|6]] · Strutturale [[3-Descrizione Strutturale.pdf#page=23|p. 23]]–[[3-Descrizione Strutturale.pdf#page=25|25]]

- [[descrizione-dataflow-lezione]]
- [[descrizione-strutturale-lezione]] — transazioni schedulate, confronto dei tempi di due architecture

_Aggiornato: 2026-11-22 — Lezione 3: schedulazione delle transazioni, porta complessa e glitch_
