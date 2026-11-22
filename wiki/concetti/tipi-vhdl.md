---
tipo: concetto
importanza_esame: alta
prerequisiti: ["oggetti-vhdl"]
fonti_pdf: ["1-Principali elementi sintattici VHDL.pdf#page=8", "1-Principali elementi sintattici VHDL.pdf#page=10", "1-Principali elementi sintattici VHDL.pdf#page=13"]
---

# Tipi in VHDL

## Definizione · [[1-Principali elementi sintattici VHDL.pdf#page=8|p. 8]]

Il VHDL è un linguaggio **fortemente tipizzato** (strongly typed): ogni oggetto ha un tipo e si possono combinare solo oggetti di tipi compatibili. Il linguaggio offre tipi base e permette di definirne di nuovi:

- **scalari**: `boolean`, `character`, `bit`, `real`, `integer`, tipi fisici (`time`), tipi enumerazione;
- **composti**: **array** ([[array-vhdl]]) e **record** ([[record-vhdl]]).

### Interi · [[1-Principali elementi sintattici VHDL.pdf#page=10|p. 10]]

- Un tipo intero è un intervallo di interi entro un range.
- `integer` è predefinito nella libreria `std`: il range dipende dall'implementazione ma deve includere almeno $[-2147483647,\ +2147483647]$ (almeno 32 bit).
- Specificando il range si riduce il numero di bit: `SIGNAL myint : integer range -10 TO 15;` occupa 5 bit.
- Sottotipi predefiniti: `natural` (da 0) e `positive` (da 1), vedi [[subtype-vhdl]].

### Enumerazione · [[1-Principali elementi sintattici VHDL.pdf#page=13|p. 13]]

- Un tipo enumerazione è un insieme **ordinato** di valori elencati uno per uno, tutti distinti; lo stesso nome può comparire in enumerazioni diverse.
- Il **primo** valore elencato è il default (il valore iniziale implicito di un oggetto di quel tipo).
- Esempio della slide: `TYPE stato IS ('q0', 'q1', 'q2', 'q3')` definisce una logica a quattro valori, con default `'q0'`.

> ⚠️ Contraddizione: un letterale tra apici contiene un solo carattere; per nomi come `q0` la forma corretta è `TYPE stato IS (q0, q1, q2, q3);`. Con caratteri singoli la forma tra apici è lecita, come in `TYPE qit IS ('0', '1', 'Z', 'X');`.

## Derivazioni

### Derivazione — 5 bit per `integer range -10 TO 15` · [[1-Principali elementi sintattici VHDL.pdf#page=10|p. 10]]
**Fonte:** la slide dà il risultato (5 bit) senza passaggi.
**Si parte da:** il range contiene valori negativi, quindi serve una rappresentazione con segno in complemento a 2; con $n$ bit si rappresenta $[-2^{n-1},\ 2^{n-1}-1]$.

| $n$ | Intervallo rappresentabile | Contiene −10 e 15? |
|---|---|---|
| 4 | $[-8,\ 7]$ | no |
| 5 | $[-16,\ 15]$ | sì |

Il minimo è $n = 5$.
**Verifica:** 15 = `01111` (massimo positivo con 5 bit) e −10 = `10110` (complemento a 2 di `01010`: inverto i bit, `10101`, e sommo 1).
**Ipotesi:** il sintetizzatore usa il complemento a 2 per i range con negativi; per un range solo positivo (ad es. `0 TO 15`) basterebbero 4 bit senza segno.

### Derivazione — perché «almeno 32 bit» · [[1-Principali elementi sintattici VHDL.pdf#page=10|p. 10]]
**Fonte:** range minimo $\pm 2147483647$ dato senza calcolo.

$$
\begin{aligned}
2^{31} - 1 &= 2147483647 && \text{massimo positivo in complemento a 2 su 32 bit} \\
-(2^{31} - 1) &= -2147483647 && \text{lo standard non richiede } -2^{31}
\end{aligned}
$$

Con 31 bit il massimo sarebbe $2^{30} - 1 = 1073741823$: non basta, quindi servono almeno 32 bit.

## Spiegazione

«Fortemente tipizzato» significa che il compilatore non converte i tipi in automatico: un `bit` non è un `std_logic`, un `std_logic_vector` non è un numero, un nuovo tipo array non è compatibile con `bit_vector` anche se ha la stessa forma (vedi [[subtype-vhdl]]). Per passare da un tipo a un altro servono funzioni di conversione o casting espliciti ([[signed-unsigned]]).

Il range di un intero non è solo un controllo: per la sintesi stabilisce **quanti fili** servono. Un `integer` senza range è implementato con 32 bit; restringerlo al necessario risparmia hardware.

I tipi enumerazione sono il modo naturale di descrivere gli **stati** di una macchina a stati: si scrivono i nomi degli stati e lo strumento sceglie la codifica.

## Perché importa

Ogni dichiarazione di segnale o porta richiede un tipo, e quasi tutti gli errori di compilazione dei principianti sono errori di tipo. La scelta del range degli interi e del tipo enumerazione per gli stati ritorna nel progetto di macchine sequenziali.

## Connessioni

- [[std-logic]] — il tipo a 9 valori usato al posto di `bit` nei design sintetizzabili
- [[signed-unsigned]] — tipi numerici su vettori di bit e conversioni
- [[subtype-vhdl]] — `natural`, `positive` e sottoinsiemi di un tipo
- [[array-vhdl]], [[record-vhdl]] — i tipi composti
- [[attributi-vhdl]] — `'LEFT`, `'POS`, `'SUCC`, … su tipi scalari ed enumerazioni

## Fonti · [[1-Principali elementi sintattici VHDL.pdf#page=8|p. 8]], [[1-Principali elementi sintattici VHDL.pdf#page=10|10]], [[1-Principali elementi sintattici VHDL.pdf#page=13|13]]

- [[elementi-sintattici-vhdl-lezione]]

_Aggiornato: 2026-11-22 — creazione_
