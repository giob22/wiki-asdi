---
tipo: concetto
importanza_esame: media
prerequisiti: ["entity-architecture"]
fonti_pdf: ["3-Descrizione Strutturale.pdf#page=14", "3-Descrizione Strutturale.pdf#page=15", "3-Descrizione Strutturale.pdf#page=16", "3-Descrizione Strutturale.pdf#page=17"]
---

# Component e binding

## Definizione · [[3-Descrizione Strutturale.pdf#page=14|p. 14]]–[[3-Descrizione Strutturale.pdf#page=17|17]]

Per usare un'entity descritta altrove (nella libreria corrente `work` o in un'altra design library), un'architecture deve:

1. **dichiarare un component** nella parte dichiarativa: è un **prototipo**, un **blocco virtuale**, con port (ed eventualmente generics) uguali a quelli dell'entity, ma senza dire quale architecture verrà usata;
2. fare il **binding**: associare il component a una entity e a una sua architecture. Si fa con una **configuration specification** nella parte dichiarativa (poco usata) oppure nella statement part, all'istanziazione.

```vhdl
COMPONENT nome_componente PORT (dichiarazione dei porti)
  GENERIC (dichiarazione dei generics);
FOR ALL | elenco di label : nome_componente
  USE ENTITY nome_libreria.nome_entity(nome_architecture);
```

## Derivazioni

### Derivazione — lettura del binding delle porte `n1` e `n2` · [[3-Descrizione Strutturale.pdf#page=17|p. 17]]
**Fonte:** codice dato senza commento riga per riga.

```vhdl
COMPONENT n1 PORT (i1: IN BIT; o1: OUT BIT); END COMPONENT;
COMPONENT n2 PORT (i1, i2: IN BIT; o1: OUT BIT); END COMPONENT;
FOR ALL : n1 USE ENTITY WORK.inv (single_delay);
FOR ALL : n2 USE ENTITY WORK.nand2 (single_delay);
```

| Riga | Significato |
|---|---|
| `COMPONENT n1 …` | prototipo con un ingresso e un'uscita: la forma di un invertitore |
| `COMPONENT n2 …` | prototipo con due ingressi e un'uscita: la forma di una porta a 2 ingressi |
| `FOR ALL : n1 USE ENTITY WORK.inv (single_delay)` | **tutte** le istanze di `n1` usano l'entity `inv` della libreria `work`, con l'architecture `single_delay` |
| `FOR ALL : n2 USE ENTITY WORK.nand2 (single_delay)` | tutte le istanze di `n2` sono NAND a 2 ingressi, architecture `single_delay` |

`ALL` si può sostituire con un elenco di label (`FOR g0, g1 : n1 USE …`) per scegliere architecture diverse per istanze diverse dello stesso component. I nomi dei port del component (`i1`, `o1`) devono corrispondere a quelli dell'entity collegata.

## Spiegazione

Component e binding separano **cosa** serve (un blocco con questa interfaccia) da **quale** implementazione usare. Il component è la «piedinatura» che il progettista mette nello schema; il binding sceglie il pezzo vero dal magazzino (la libreria). Grazie a questo meccanismo si può cambiare l'architecture di un componente (ad es. da una versione comportamentale a una strutturale) senza toccare il codice che lo istanzia.

## Perché importa

Le descrizioni strutturali e i testbench dichiarano sempre i component che usano; il binding esplicito serve quando un'entity ha più architecture (come il `nibble_comparator(iterative)` del testbench, vedi [[testbench]]).

## Connessioni

- [[entity-architecture]] — un'entity può avere più architecture
- [[istanziazione-componenti]] — l'uso del component nel corpo
- [[generics-vhdl]] — il component può ridefinire i default dei generics
- [[descrizione-strutturale]]

## Fonti · [[3-Descrizione Strutturale.pdf#page=14|p. 14]]–[[3-Descrizione Strutturale.pdf#page=17|17]]

- [[descrizione-strutturale-lezione]]

_Aggiornato: 2026-11-22 — creazione_
