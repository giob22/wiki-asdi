---
tipo: concetto
importanza_esame: alta
prerequisiti: ["oggetti-vhdl", "tipi-vhdl"]
fonti_pdf: ["3-Descrizione Strutturale.pdf#page=2", "3-Descrizione Strutturale.pdf#page=3", "3-Descrizione Strutturale.pdf#page=10", "3-Descrizione Strutturale.pdf#page=11", "3-Descrizione Strutturale.pdf#page=12", "3-Descrizione Strutturale.pdf#page=13", "3-Descrizione Strutturale.pdf#page=18"]
---

# Entity e architecture

## Definizione · [[3-Descrizione Strutturale.pdf#page=2|p. 2]]–[[3-Descrizione Strutturale.pdf#page=5|5]], [[3-Descrizione Strutturale.pdf#page=10|10]]–[[3-Descrizione Strutturale.pdf#page=13|13]], [[3-Descrizione Strutturale.pdf#page=18|18]]

Ogni modulo VHDL è descritto da due parti:

- **entity**: l'**interfaccia** del modulo, cioè i port (nome, modo, tipo, vedi [[port-vhdl]]) ed eventualmente i generics ([[generics-vhdl]]). È la **parte formale**: i segnali effettivi si collegano all'istanziazione;
- **architecture**: una particolare **implementazione** del modulo, cioè il legame fra ingressi e uscite. Per la stessa entity possono esistere **più architecture** (livelli di astrazione o di dettaglio diversi): all'istanziazione si sceglie quale usare (binding, [[component-binding]]).

L'architecture ha due parti:

| Parte | Dove | Contiene |
|---|---|---|
| **dichiarativa** | fra `IS` e `BEGIN` | tipi, costanti, segnali interni, funzioni e procedure, component, specifiche di configurazione |
| **corpo** (architecture body) | fra `BEGIN` e `END` | statement concorrenti: istanze di componenti, assegnazioni di segnale, process |

```vhdl
ARCHITECTURE nome_architettura OF nome_entita IS
  -- dichiarazioni: TYPE, CONSTANT, SIGNAL, funzioni, COMPONENT, FOR ... USE ...
BEGIN
  -- statement concorrenti
END nome_architettura;
```

Regole del corpo: i port si usano come segnali rispettandone il modo (un `IN` si legge soltanto, un `OUT` si scrive soltanto); un segnale è «scritto» se sta a sinistra di un'assegnazione. Le dichiarazioni sono **locali** al modulo; i segnali dichiarati sono i **fili** che collegano i blocchi del corpo.

## Derivazioni

### Derivazione — leggere l'entity AOI · [[3-Descrizione Strutturale.pdf#page=23|p. 23]]
**Fonte:** esempio completo di entity + architecture.

| Riga | Parte | Cosa dice |
|---|---|---|
| `LIBRARY ieee; USE ieee.std_logic_1164.ALL;` | contesto | rende visibili `std_logic` e i suoi operatori |
| `ENTITY AOI IS PORT (i1, i2, i3 : IN std_logic; O1 : OUT std_logic)` | entity | 3 ingressi, 1 uscita |
| `ARCHITECTURE dataflow OF AOI IS` | architecture | un'implementazione di nome `dataflow` dell'entity `AOI` |
| `BEGIN o1 <= NOT(i1 AND i2 OR i3) AFTER 3ns;` | corpo | una sola assegnazione concorrente: AND-OR-INVERT con ritardo 3 ns |

Nel corpo `o1` è scritto (sta a sinistra) e `i1`, `i2`, `i3` sono letti: coerente con i modi `OUT` e `IN`. Il nome `O1` dell'entity e `o1` del corpo coincidono perché il VHDL non è case sensitive. Vedi [[porta-aoi]] per i refusi del codice.

### Derivazione — due architecture per la stessa entity · [[3-Descrizione Strutturale.pdf#page=24|p. 24]]
**Fonte:** `concurrent` e `single_assignment` di `porta_complessa`.

Le due architecture condividono la stessa entity (`a, b, c : IN`, `z : OUT`) e quindi sono intercambiabili per chi istanzia il modulo: la prima usa tre segnali interni dichiarati nella parte dichiarativa, la seconda nessuno. Il confronto dei tempi è in [[assegnazione-concorrente]].

## Spiegazione

La separazione **interfaccia / implementazione** permette di scrivere un modulo «dall'esterno» (cosa entra, cosa esce) e decidere dopo come realizzarlo, anche in più modi: una versione comportamentale veloce da simulare, una strutturale vicina all'hardware. Chi usa il modulo vede solo l'entity.

## Perché importa

È la prima cosa da scrivere per ogni modulo di ogni progetto; all'esame di progetto la definizione corretta delle entity (porte, modi, tipi) è il punto di partenza.

## Connessioni

- [[port-vhdl]] — i terminali dell'entity
- [[generics-vhdl]] — i parametri dell'entity
- [[component-binding]] — scelta dell'architecture fra più disponibili
- [[descrizione-strutturale]] — composizione di moduli
- [[oggetti-vhdl]] — costanti e segnali dichiarati nella parte dichiarativa

## Fonti · [[3-Descrizione Strutturale.pdf#page=2|p. 2]]–[[3-Descrizione Strutturale.pdf#page=5|5]], [[3-Descrizione Strutturale.pdf#page=10|10]]–[[3-Descrizione Strutturale.pdf#page=13|13]], [[3-Descrizione Strutturale.pdf#page=18|18]], [[3-Descrizione Strutturale.pdf#page=23|23]]–[[3-Descrizione Strutturale.pdf#page=24|24]]

- [[descrizione-strutturale-lezione]]

_Aggiornato: 2026-11-22 — creazione_
