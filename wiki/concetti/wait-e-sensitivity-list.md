---
tipo: concetto
importanza_esame: alta
prerequisiti: ["process-vhdl"]
fonti_pdf: ["5-Descrizione Comportamentale.pdf#page=6", "5-Descrizione Comportamentale.pdf#page=7", "5-Descrizione Comportamentale.pdf#page=8", "5-Descrizione Comportamentale.pdf#page=9"]
---

# WAIT e sensitivity list

## Definizione · [[5-Descrizione Comportamentale.pdf#page=6|p. 6]]–[[5-Descrizione Comportamentale.pdf#page=9|9]]

Un process si sospende e si riattiva in uno di due modi **alternativi** (non si possono usare insieme nello stesso process):

| Template | Attivazione | Sospensione |
|---|---|---|
| **sensitivity list** `PROCESS (s1, …, sn)` | evento su un segnale della lista (e una volta all'inizializzazione) | alla fine del body |
| **istruzioni `WAIT`** | eseguito al tempo 0 | a ogni `WAIT`; riprende quando la condizione del `WAIT` è verificata |

Forme del `WAIT` (istruzione sequenziale, solo nel process body):

| Forma | Esempio | Significato |
|---|---|---|
| `WAIT FOR tempo;` | `WAIT FOR 4ns;` | sospende per 4 ns |
| `WAIT ON lista;` | `WAIT ON s1, s2, clk;` | fino a un evento su `s1`, `s2` o `clk` |
| `WAIT UNTIL condizione;` | `WAIT UNTIL (clk'EVENT and clk = '1');` | fino al fronte 0→1 di `clk` |
| `WAIT;` | `WAIT;` | per sempre |

**Equivalenza:** una sensitivity list equivale a `WAIT ON` sugli stessi segnali **in fondo** al process.

## Derivazioni

### Derivazione — perché il `WAIT ON` va in fondo · [[5-Descrizione Comportamentale.pdf#page=9|p. 9]]
**Fonte:** l'equivalenza è data senza motivazione.

| Momento | `PROCESS (a, b)` | `PROCESS … WAIT ON a, b;` in fondo | `WAIT ON a, b;` in cima |
|---|---|---|---|
| inizializzazione | esegue il body, si sospende alla fine | esegue il body, si sospende al `WAIT` | si sospende subito senza eseguire nulla |
| evento su `a` | riesegue il body | riprende dopo il `WAIT`, ricomincia dall'inizio, esegue il body | esegue il body e torna al `WAIT` |

Solo con il `WAIT` **in fondo** il comportamento coincide anche all'inizializzazione, dove i process con sensitivity list «vengono comunque eseguiti una volta».
> 🧩 Derivazione mia, dalle regole di inizializzazione di p. 5 e di p. 9.

### Derivazione — il process senza sensitivity list e senza `WAIT` · [[5-Descrizione Comportamentale.pdf#page=7|p. 7]]
**Fonte:** «un process esegue tutte le istruzioni e poi le ripete, come in un loop infinito»; il loop si sospende solo con un `WAIT`.
> 🧩 Derivazione mia: è il caso dei process delle slide p. 18 e p. 19 della lezione.

Senza sensitivity list e senza `WAIT` il process non si sospende mai: ricomincia subito dall'inizio, all'infinito, sempre al tempo 0. Le assegnazioni di segnale (che hanno effetto solo alla sospensione) non avvengono mai e il tempo di simulazione non avanza: i simulatori segnalano l'errore. Ogni process deve avere o una sensitivity list o almeno un `WAIT`.

## Spiegazione

La sensitivity list è comoda per descrivere logica che reagisce ai segnali (combinatoria: tutti gli ingressi letti; sequenziale: clock e reset). Il `WAIT` dà più controllo e si usa soprattutto nei **testbench**, per scandire il tempo (`WAIT FOR 10 ns;`) o fermare il process alla fine (`WAIT;`). `WAIT UNTIL clk'EVENT AND clk = '1'` descrive il fronte di salita, come l'attributo `'EVENT` visto in [[attributi-vhdl]].

## Perché importa

Una sensitivity list incompleta fa sì che la simulazione differisca dall'hardware sintetizzato; un process senza sospensione blocca il simulatore. Sono fra gli errori più frequenti nei progetti.

## Connessioni

- [[process-vhdl]] — ciclo di vita del process
- [[attributi-vhdl]] — `'EVENT` per il fronte di clock
- [[testbench]] — uso tipico dei `WAIT FOR`
- [[assegnazione-sequenziale]] — le assegnazioni hanno effetto alla sospensione

## Fonti · [[5-Descrizione Comportamentale.pdf#page=6|p. 6]]–[[5-Descrizione Comportamentale.pdf#page=9|9]]

- [[descrizione-comportamentale-lezione]]

_Aggiornato: 2026-11-22 — creazione_
