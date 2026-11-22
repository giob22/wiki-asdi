---
tipo: concetto
importanza_esame: alta
prerequisiti: ["tipi-vhdl", "array-vhdl", "oggetti-vhdl"]
fonti_pdf: ["1-Principali elementi sintattici VHDL.pdf#page=25", "1-Principali elementi sintattici VHDL.pdf#page=26", "1-Principali elementi sintattici VHDL.pdf#page=27", "1-Principali elementi sintattici VHDL.pdf#page=28", "1-Principali elementi sintattici VHDL.pdf#page=29", "1-Principali elementi sintattici VHDL.pdf#page=30", "1-Principali elementi sintattici VHDL.pdf#page=31", "1-Principali elementi sintattici VHDL.pdf#page=32"]
---

# Attributi in VHDL

## Definizione · [[1-Principali elementi sintattici VHDL.pdf#page=25|p. 25]]

Un **attributo** è un'informazione aggiuntiva associata a un oggetto VHDL (tipo scalare o discreto, array, segnale, …). Si legge con l'apice (*tick*): `obj'attr`. Ci sono molti attributi **predefiniti** per tipi, array e segnali; l'utente può definirne altri (raro). Per descrivere i sistemi se ne usano pochi (`'EVENT`, `'STABLE`); un uso molto utile è dare **direttive al sintetizzatore** (rimuovi la gerarchia, tratta come black box, …). Il Navabi li tratta in dettaglio.

### Attributi dei range · [[1-Principali elementi sintattici VHDL.pdf#page=26|p. 26]]

| Attributo | Significato |
|---|---|
| `T'LEFT` | limite scritto a sinistra nella dichiarazione |
| `T'RIGHT` | limite scritto a destra |
| `T'LOW` | limite minore |
| `T'HIGH` | limite maggiore |

### Attributi dei tipi enumerativi · [[1-Principali elementi sintattici VHDL.pdf#page=27|p. 27]]

`'BASE`, `'LEFT`, `'RIGHT`, `'HIGH`, `'LOW`, `'POS(V)` (posizione di V), `'VAL(P)` (valore in posizione P), `'SUCC(V)` / `'PRED(V)` (successivo / precedente), `'LEFTOF(V)` / `'RIGHTOF(V)` (a sinistra / a destra). `'POS`, `'VAL`, `'SUCC`, `'PRED`, `'LEFTOF`, `'RIGHTOF` lavorano **nel tipo base**.

### Attributi degli array · [[1-Principali elementi sintattici VHDL.pdf#page=28|p. 28]]

`'LEFT(n)`, `'RIGHT(n)`, `'HIGH(n)`, `'LOW(n)`, `'RANGE(n)`, `'REVERSE_RANGE(n)`, `'LENGTH(n)`, dove `n` è la dimensione (default 1).

### Attributi dei segnali · [[1-Principali elementi sintattici VHDL.pdf#page=29|p. 29]]–[[1-Principali elementi sintattici VHDL.pdf#page=30|30]]

Due famiglie: quelli basati sugli **eventi** (EV: il segnale **cambia valore**) e quelli basati sulle **transazioni** (TR: il segnale **riceve un'assegnazione**, anche con lo stesso valore).

| Attributo | Famiglia | È un | Tipo | Significato |
|---|---|---|---|---|
| `s'DELAYED(t)` | – | segnale | come s | copia di s ritardata di t (TRANSPORT); senza t, di un delta |
| `s'STABLE(t)` | EV | segnale | BOOLEAN | TRUE se s non è cambiato negli ultimi t; senza t, nel tempo corrente |
| `s'EVENT` | EV | valore | BOOLEAN | TRUE nel ciclo (delta) in cui s cambia |
| `s'LAST_EVENT` | EV | valore | TIME | tempo dall'ultimo cambio di valore (0 se `s'EVENT`) |
| `s'LAST_VALUE` | EV | valore | come s | valore di s prima dell'ultimo evento |
| `s'QUIET(t)` | TR | segnale | BOOLEAN | TRUE se nessuna transazione negli ultimi t; senza t, nel ciclo corrente |
| `s'ACTIVE` | TR | valore | BOOLEAN | TRUE nel ciclo in cui s ha una transazione |
| `s'LAST_ACTIVE` | TR | valore | TIME | tempo dall'ultima transazione (0 se `s'ACTIVE`) |
| `s'TRANSACTION` | TR | segnale | BIT | commuta a ogni transazione su s |

## Derivazioni

### Derivazione — `'LEFT`, `'RIGHT`, `'LOW`, `'HIGH` su range crescenti e decrescenti · [[1-Principali elementi sintattici VHDL.pdf#page=26|p. 26]]
**Fonte:** i risultati sono dati senza regola.

| Tipo | Range | `'LEFT` | `'RIGHT` | `'LOW` | `'HIGH` |
|---|---|---|---|---|---|
| `T1` | `0 to 10` | 0 | 10 | 0 | 10 |
| `T2` | `10 downto 0` | 10 | 0 | 0 | 10 |

**Regola:** `'LEFT`/`'RIGHT` dipendono da **come è scritto** il range; `'LOW`/`'HIGH` solo dai **valori**. Coincidono a coppie (`LEFT=LOW`, `RIGHT=HIGH`) per i range crescenti e si scambiano per quelli decrescenti.

> ⚠️ Contraddizione: i commenti della slide invertono sinistra e destra («`T'left`: l'elemento definito più a destra»); la tabella qui sopra segue gli esempi numerici della slide stessa, che sono corretti.

### Derivazione — la tabella degli attributi di `qit` e `tit` · [[1-Principali elementi sintattici VHDL.pdf#page=27|p. 27]]
**Fonte:** tabella di risultati.
**Si parte da:** `TYPE qit IS ('0', '1', 'Z', 'X')` assegna le posizioni 0, 1, 2, 3 nell'ordine di scrittura; `SUBTYPE tit IS qit RANGE '0' TO 'Z'` contiene le posizioni 0–2.

| Posizione | 0 | 1 | 2 | 3 |
|---|---|---|---|---|
| valore | '0' | '1' | 'Z' | 'X' |
| in `tit`? | sì | sì | sì | no |

| Esempio | Ragionamento | Risultato |
|---|---|---|
| `tit'BASE` | tipo da cui è derivato il subtype | `qit` |
| `tit'LEFT`, `qit'LEFT` | primo valore scritto in entrambi | '0', '0' |
| `tit'RIGHT`, `qit'RIGHT` | ultimo del subtype / del tipo | 'Z', 'X' |
| `INTEGER'HIGH` | massimo dell'implementazione, almeno $2^{31}-1$ | «grande» |
| `tit'HIGH` | range crescente: `HIGH = RIGHT` | 'Z' |
| `POSITIVE'LOW` | `positive` parte da 1 | 1 |
| `qit'LOW` | range crescente: `LOW = LEFT` | '0' |
| `qit'POS('Z')` | 'Z' è in posizione 2 | 2 |
| `tit'POS('X')` | 'X' non è in `tit`, ma `'POS` lavora nel tipo base | 3 |
| `qit'VAL(3)`, `tit'VAL(3)` | posizione 3 del tipo base | 'X', 'X' |
| `tit'SUCC('Z')` | dopo la posizione 2 c'è la 3 (nel tipo base) | 'X' |
| `tit'PRED('1')` | prima della posizione 1 c'è la 0 | '0' |
| `tit'LEFTOF('1')` | a sinistra della posizione 1 | '0' |
| `tit'LEFTOF('0')` | non c'è nulla a sinistra della posizione 0 | errore |
| `tit'RIGHTOF('1')`, `tit'RIGHTOF('Z')` | posizioni 2 e 3 | 'Z', 'X' |

**Verifica:** su un range crescente `'SUCC` e `'RIGHTOF` coincidono (così come `'PRED` e `'LEFTOF`): la tabella lo conferma con `'1'` → `'Z'`.

### Derivazione — gli attributi di `sq_4_8` · [[1-Principali elementi sintattici VHDL.pdf#page=28|p. 28]]
**Fonte:** tabella di risultati; `TYPE qit_4by8 IS ARRAY (3 DOWNTO 0, 0 TO 7) OF qit`.
**Si parte da:** dimensione 1 = `3 DOWNTO 0` (righe), dimensione 2 = `0 TO 7` (colonne); senza numero si intende la dimensione 1.

| Esempio | Dimensione | Ragionamento | Risultato |
|---|---|---|---|
| `'LEFT(1)` | `3 DOWNTO 0` | limite scritto a sinistra | 3 |
| `'RIGHT` | `3 DOWNTO 0` | limite a destra | 0 |
| `'RIGHT(2)` | `0 TO 7` | limite a destra | 7 |
| `'HIGH(2)` | `0 TO 7` | massimo | 7 |
| `'LOW(2)` | `0 TO 7` | minimo | 0 |
| `'RANGE(2)`, `'RANGE(1)` | — | il range così come è scritto | `0 TO 7`, `3 DOWNTO 0` |
| `'REVERSE_RANGE(2)`, `'REVERSE_RANGE(1)` | — | stesso range percorso al contrario | `7 DOWNTO 0`, `0 TO 3` |
| `'LENGTH` | `3 DOWNTO 0` | $3 - 0 + 1$ | 4 |

**Verifica:** `sq_4_8'LENGTH(2)` darebbe $7 - 0 + 1 = 8$; $4 \times 8 = 32$ elementi in tutto. (Nella slide `'LOW(2)` è scritto `'LOWS(2)`.)

### Derivazione — lettura delle forme d'onda degli attributi di `s1` · [[1-Principali elementi sintattici VHDL.pdf#page=31|p. 31]]
**Fonte:** figura senza commento.

![[vhdl-1-p31-attributi-segnale-forme-d-onda.png]]
*Transazioni su s1 a 15, 30, 45, 60 ns; solo a 30 (0→1) e 45 (1→0) il valore cambia.*

**Si parte da:** s1 vale '0' fino a 30 ns, '1' da 30 a 45, '0' dopo. Transazione = assegnazione; evento = transazione che cambia il valore.

| t (ns) | 15 | 30 | 45 | 60 |
|---|---|---|---|---|
| transazione? | sì | sì | sì | sì |
| evento? | no (0→0) | sì (0→1) | sì (1→0) | no (0→0) |

Da qui ogni riga della figura:

| Attributo | Andamento | Perché |
|---|---|---|
| `s1'DELAYED(5NS)` | alto da 35 a 50 ns | s1 traslato di 5 ns |
| `s1'STABLE` | FALSE solo nel delta di 30 e 45 | conta solo gli eventi |
| `s1'EVENT` | impulsi a 30 e 45 | eventi |
| `s1'LAST_EVENT` | 10, 15, 20, 25 a t = 10…25; 0 a 30; 5, 10 a 35, 40; 0 a 45; 5, 10, 15 a 50, 55, 60 | si azzera a ogni evento e poi cresce col tempo; a 10 ns vale 10, quindi l'evento precedente è a 0 ns |
| `s1'LAST_VALUE` | '0' fino a 45, poi '1' | a 30 il valore precedente era '0', a 45 era '1' |
| `s1'QUIET(5NS)` | FALSE in [15, 20), [30, 35), [45, 50), [60, 65) | conta le **transazioni**: si spegne per 5 ns dopo ognuna |
| `s1'ACTIVE` | impulsi a 15, 30, 45, 60 | transazioni |
| `s1'LAST_ACTIVE` | 10 a 10 ns; 0 a 15; 5, 10 a 20, 25; 0 a 30; …; 0 a 60 | si azzera a ogni transazione |
| `s1'TRANSACTION` | commuta a 15, 30, 45, 60 | un cambio per transazione |

**Il confronto che conta:** a 15 e 60 ns c'è una transazione senza evento: `QUIET`, `ACTIVE`, `LAST_ACTIVE` e `TRANSACTION` reagiscono, `STABLE`, `EVENT` e `LAST_EVENT` no.

### Derivazione — il flip-flop D sul fronte di discesa · [[1-Principali elementi sintattici VHDL.pdf#page=32|p. 32]]
**Fonte:** codice dato senza spiegazione riga per riga.

| Riga | Cosa fa |
|---|---|
| `PORT (d, c : IN BIT; q : OUT BIT)` | dato `d`, clock `c`, uscita `q` |
| `SIGNAL tmp : BIT` | memorizza lo stato del flip-flop |
| `tmp <= d WHEN (c = '0' AND NOT c'STABLE) ELSE tmp` | `NOT c'STABLE` è vero solo nell'istante in cui `c` cambia; `c = '0'` dice che è appena andato a 0: insieme individuano il **fronte di discesa**, e solo allora `tmp` prende `d`; altrimenti `tmp` conserva il suo valore |
| `q <= tmp AFTER 8 NS` | l'uscita segue lo stato con un ritardo di 8 ns (ritardo clock→uscita) |

**Verifica:** con `c` di tipo `BIT` gli unici valori sono '0' e '1', quindi «è appena cambiato ed è '0'» implica «era '1'»: è proprio il fronte 1→0. La condizione equivale a `c'EVENT AND c = '0'`.

## Spiegazione

Gli attributi sono «domande» che si fanno a un oggetto: quanti elementi ha un vettore (`'LENGTH`), qual è il suo range (`'RANGE`, utile nei cicli), se un segnale è appena cambiato (`'EVENT`). I più usati nel progetto sono `'EVENT` (fronte di clock), `'RANGE` e `'LENGTH` (codice indipendente dalla dimensione dei vettori).

La distinzione **evento / transazione** è la chiave degli attributi dei segnali: una transazione è ogni assegnazione schedulata sul segnale; diventa un evento solo se il valore cambia. In simulazione i process si risvegliano sugli eventi, non sulle semplici transazioni.

## Perché importa

`clk'EVENT AND clk = '1'` (o la sua variante sul fronte di discesa vista qui) è il modo di descrivere ogni elemento sincrono: flip-flop, registri, contatori, macchine a stati. La lettura delle forme d'onda di `'STABLE`, `'QUIET`, `'LAST_EVENT` è un tipico esercizio d'orale sulla semantica della simulazione.

## Connessioni

- [[oggetti-vhdl]] — gli attributi dei segnali esistono solo per i segnali
- [[array-vhdl]] — attributi degli array
- [[tipi-vhdl]], [[subtype-vhdl]] — attributi di tipi e subtype, tipo base
- [[operatori-vhdl]] — operatori relazionali e logici usati nelle condizioni sugli attributi

## Fonti · [[1-Principali elementi sintattici VHDL.pdf#page=25|p. 25]]–[[1-Principali elementi sintattici VHDL.pdf#page=32|32]]

- [[elementi-sintattici-vhdl-lezione]]

_Aggiornato: 2026-11-22 — creazione_
