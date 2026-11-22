---
tipo: fonte
titolo: "VHDL Strutturale"
file_raw: "vhdl/3-Descrizione Strutturale.pdf"
pagine: "1-31"
data_ingest: 2026-11-22
formato: slide-pdf
argomenti: [entity, architecture, port, modi, generics, component, binding, istanziazione, port map, assegnazione concorrente, generate, testbench]
---

# VHDL Strutturale

## Sommario · [[3-Descrizione Strutturale.pdf#page=1|p. 1]]–[[3-Descrizione Strutturale.pdf#page=31|31]]

Terza lezione sul VHDL (slide v1.1): come si descrive un design come **gerarchia di moduli**. Introduce entity (interfaccia: port con nome, tipo e modo `IN`/`OUT`/`BUFFER`/`INOUT`; generics con default e priorità di risoluzione, esempio di ROM parametrica) e architecture (più architecture per un'entity, parte dichiarativa con tipi, costanti, segnali, component e configurazioni, corpo fatto di statement concorrenti). Spiega il **binding** (component come prototipo virtuale, `FOR … USE ENTITY lib.entity(arch)`), l'**istanziazione** con `PORT MAP`/`GENERIC MAP` posizionali e nominali (esempi con porte `inv`/`nand2` e con la ROM), l'assegnazione di segnale come statement concorrente che schedula transazioni (porta AOI; due architecture della stessa porta complessa con tempi 24 e 36 ns), i costrutti **generate** (`FOR`/`IF`, 8 porte AND) e i **testbench** (nibble comparator: DUT, stimoli, tabella delle uscite con worst e best case).

## Punti chiave

1. Un sistema è un albero di moduli con un top-level; ogni modulo = entity (interfaccia) + architecture (implementazione).
2. L'entity è la parte formale: i segnali effettivi si collegano all'istanziazione (come i piedini di un integrato della serie 74).
3. Port: nome, tipo (solo segnali compatibili), modo; `inout` solo nella top-level, `buffer` da evitare.
4. Generics: parametri costanti; valore da default dell'entity < component < istanza; vanno sempre risolti.
5. Più architecture per la stessa entity; parte dichiarativa locale, corpo di statement concorrenti; i port si usano rispettando il modo.
6. Component = prototipo virtuale; il binding (`FOR ALL : comp USE ENTITY …`) sceglie entity e architecture.
7. Istanziazione: statement concorrente con label unica; associazione posizionale (conta l'ordine) o nominale.
8. Un'assegnazione di segnale, a ogni evento a destra, calcola il nuovo valore e schedula una transazione secondo il suo timing.
9. Due architecture con la stessa funzione booleana possono avere tempi diversi (24 ns contro 36 ns).
10. `FOR`/`IF … GENERATE` replicano statement concorrenti; niente `ELSE`/`ELSIF` prima del VHDL 2008.
11. Il testbench è un'entity senza port che istanzia il DUT, applica stimoli e (eventualmente) verifica le uscite.

## Concetti introdotti

- [[descrizione-strutturale]]
- [[entity-architecture]]
- [[port-vhdl]]
- [[generics-vhdl]]
- [[component-binding]]
- [[istanziazione-componenti]]
- [[generate-vhdl]]
- [[testbench]]
- aggiornato: [[assegnazione-concorrente]]
- entità: [[porta-aoi]], [[rom]], [[nibble-comparator]]

## Domande aperte

- Molti refusi nel codice delle slide (segnalati con ⚠️ nel testo di studio): generics dentro `PORT`, `;` prima della `)`, `TYPE … :` invece di `IS`, apici mancanti in `std_ulogic`, `SIGANL`, ordine `PORT MAP`/`GENERIC MAP` e `:=` nel `GENERIC MAP`, `END AOI;` mancante, `i1 AND i2 OR i3` senza parentesi, nomi incoerenti nel testbench, doppi apici mancanti, `gnd` non inizializzato.
- Il testo della slide sul testbench parla di 5, 15, 50, 60 ns mentre tabella e codice usano 500, 1500, 5000, 6000 ns.
- La slide del `FOR GENERATE` presenta il nibble comparator ma mostra il codice di 8 porte AND; l'architecture `iterative` del comparatore non è nelle slide.
- La slide del binding di p. 21 rimanda a «slide 7» per il default `width = 32`: è la p. 9 del PDF.

## Domande da esame

- Cosa descrivono entity e architecture? Perché per un'entity possono esistere più architecture?
- Quali sono i modi dei port e cosa si può fare con ciascuno dentro l'architecture? Perché è sconsigliato `buffer`?
- Cosa sono i generics, dove si specificano e quale valore prevale?
- Differenza fra component declaration e configuration specification; cos'è il binding?
- Associazione posizionale e nominale nel `PORT MAP`: pro e contro.
- Perché due architecture con la stessa funzione booleana possono avere tempi diversi? Spiega le forme d'onda della porta complessa.
- A cosa serve il costrutto `GENERATE`? Differenza fra `FOR` e `IF GENERATE`.
- Cos'è un testbench? Perché non ha port? Come si scelgono gli stimoli (worst case / best case)?

_Aggiornato: 2026-11-22 — creazione_
