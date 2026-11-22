---
tipo: concetto
importanza_esame: alta
prerequisiti: ["simulazione-ad-eventi", "modello-tempificazione-vhdl"]
fonti_pdf: ["4-Tecniche di simulazione e ritardi.pdf#page=8", "4-Tecniche di simulazione e ritardi.pdf#page=9", "4-Tecniche di simulazione e ritardi.pdf#page=10"]
---

# Delta cycle

## Definizione · [[4-Tecniche di simulazione e ritardi.pdf#page=8|p. 8]]

Un'assegnazione senza ritardo (`w <= NOT a;`) ha ritardo 0, cioè equivale a `w <= NOT a AFTER 0ns;`. La transazione è schedulata per lo **stesso istante** ma viene eseguita nel **ciclo di simulazione successivo**: il **delta cycle** ($\delta$). Il tempo di simulazione è quindi una coppia

$$t = x_1\,T + x_2\,\delta$$

dove $T$ è un tempo reale (ns, ms, s) e $\delta$ conta i cicli di simulazione, che **non corrispondono a tempo reale**: un miliardo di delta non fanno un femtosecondo. Il delta serve solo a **ordinare** gli eventi che avvengono nello stesso istante.

## Derivazioni

### Derivazione — `a`, `b`, `c` in tre delta · [[4-Tecniche di simulazione e ritardi.pdf#page=9|p. 9]]
**Fonte:** sequenza degli eventi e tabella; qui il perché di ogni passo.

```vhdl
SIGNAL a, b, c : BIT := '0';
a <= '1';
b <= NOT a;
c <= NOT b;
```

| Ciclo | Valori all'inizio (a b c) | Assegnazioni valutate | Transazioni per il delta successivo |
|---|---|---|---|
| 0 ns + 0δ | 0 0 0 | all'inizializzazione si valutano tutte: `a ← 1`, `b ← NOT 0 = 1`, `c ← NOT 0 = 1` | a: 0→1, b: 0→1, c: 0→1 |
| 0 ns + 1δ | 1 1 1 | eventi su a, b, c → si rivalutano `b` (legge a) e `c` (legge b): `b ← NOT 1 = 0`, `c ← NOT 1 = 0` | b: 1→0, c: 1→0 |
| 0 ns + 2δ | 1 0 0 | eventi su b, c → si rivaluta `c` (legge b): `c ← NOT 0 = 1` | c: 0→1 |
| 0 ns + 3δ | 1 0 1 | evento su c, ma nessuno legge c | nessuna → fine |

**Verifica:** il valore finale è quello che darebbe un circuito combinatorio senza ritardi: `a = 1`, `b = NOT a = 0`, `c = NOT b = 1`. I valori intermedi (b = 1 a 1δ, c = 0 a 2δ) sono «glitch» di durata zero, visibili solo nella lista dei delta.

![[vhdl-4-p9-delta-cycles.png]]
*Le transazioni nei tre delta, tutte a 0 ns.*

### Derivazione — il «paradosso» di `x <= y; y <= NOT x;` · [[4-Tecniche di simulazione e ritardi.pdf#page=10|p. 10]]
**Fonte:** la slide afferma che `x` e `y` oscillano senza che il tempo avanzi.

| Ciclo | x | y | Valutazione | Prossimo evento |
|---|---|---|---|---|
| 0δ | 0 | 0 | `x ← y = 0` (nessun cambio), `y ← NOT 0 = 1` | y: 0→1 |
| 1δ | 0 | 1 | evento su y → `x ← 1` | x: 0→1 |
| 2δ | 1 | 1 | evento su x → `y ← 0` | y: 1→0 |
| 3δ | 1 | 0 | evento su y → `x ← 0` | x: 1→0 |
| 4δ | 0 | 0 | come a 0δ: il ciclo ricomincia | … |

L'anello `x → y → x` contiene un'inversione e nessun ritardo: ogni delta produce un nuovo evento e la coda non si svuota mai, quindi il tempo reale resta a 0 ns. Lo stato si ripete ogni 4 delta.
> 📚 Fonte esterna: i simulatori reali si fermano con un errore dopo un numero massimo di delta per istante (iteration limit); le slide non lo dicono.

## Spiegazione

Il delta risolve un problema: in un circuito senza ritardi molti segnali cambiano «nello stesso istante», ma in un ordine causale preciso (prima `a`, poi `b`, poi `c`). Il simulatore conserva quest'ordine con i delta, senza far avanzare il tempo. Un anello combinatorio con un numero dispari di inversioni non ha punto di equilibrio: senza ritardi oscilla in delta all'infinito, con un ritardo diventerebbe un oscillatore ad anello.

## Perché importa

Le assegnazioni senza `AFTER` sono la norma nei design sintetizzabili: tutto ciò che accade nel simulatore «a tempo zero» è scandito da delta. Capirli serve per leggere le simulazioni e per non stupirsi di segnali che sembrano aggiornarsi «in ritardo» di un ciclo nei process.

## Connessioni

- [[modello-tempificazione-vhdl]] — transazioni con ritardo nullo
- [[simulazione-ad-eventi]] — la coda di eventi ordinata per (tempo, delta)
- [[attributi-vhdl]] — `'EVENT` è vero per un solo delta; `'DELAYED` senza parametro ritarda di un delta
- [[assegnazione-concorrente]]

## Fonti · [[4-Tecniche di simulazione e ritardi.pdf#page=8|p. 8]]–[[4-Tecniche di simulazione e ritardi.pdf#page=10|10]]

- [[tecniche-di-simulazione-lezione]]

_Aggiornato: 2026-11-22 — creazione_
