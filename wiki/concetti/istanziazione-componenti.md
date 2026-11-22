---
tipo: concetto
importanza_esame: alta
prerequisiti: ["component-binding", "port-vhdl"]
fonti_pdf: ["3-Descrizione Strutturale.pdf#page=19", "3-Descrizione Strutturale.pdf#page=20", "3-Descrizione Strutturale.pdf#page=21", "3-Descrizione Strutturale.pdf#page=22"]
---

# Istanziazione di componenti (`PORT MAP`, `GENERIC MAP`)

## Definizione · [[3-Descrizione Strutturale.pdf#page=19|p. 19]]–[[3-Descrizione Strutturale.pdf#page=20|20]]

L'**istanziazione** crea una copia di un component nel corpo dell'architecture e ne collega i port a segnali effettivi (e i generics a valori). È uno **statement concorrente**, sempre attivo: quando arriva un evento su un port d'ingresso il componente reagisce e genera eventi sulle uscite. Ogni istanza ha una **label** unica, il nome del blocco logico.

| Associazione | Forma | Ordine |
|---|---|---|
| **posizionale** | `PORT MAP (s1, s2, …)` | conta: segue l'ordine di dichiarazione dei port |
| **nominale** | `PORT MAP (port1 => s1, port2 => s2, …)` | non conta |

```vhdl
nome_label : nome_componente
  GENERIC MAP (valore_1, ..., valore_M)
  PORT MAP (segnale_1, ..., segnale_N);                          -- posizionale

nome_label : nome_componente
  GENERIC MAP (nome_generic_1 => valore_1, ...)
  PORT MAP (nome_segnale_1 => segnale_1, ...);                   -- nominale
```

> ⚠️ Contraddizione: le slide scrivono `PORT MAP` prima di `GENERIC MAP` e usano `:=` nel `GENERIC MAP` nominale; la sintassi corretta è quella qui sopra (prima `GENERIC MAP`, poi `PORT MAP`, sempre `=>`), come nell'esempio della ROM delle slide stesse.

## Derivazioni

### Derivazione — i collegamenti di `g0`…`g3` · [[3-Descrizione Strutturale.pdf#page=22|p. 22]]
**Fonte:** quattro istanze con un commento sul tipo di associazione.
**Si parte da:** `n1` ha port `(i1, o1)`; `n2` ha port `(i1, i2, o1)` in quest'ordine.

| Istanza | Codice | i1 | i2 | o1 |
|---|---|---|---|---|
| g0 (inv) | `n1 PORT MAP (a, im1)` | a | — | im1 |
| g1 (inv) | `n1 PORT MAP (i1 => b, o1 => im2)` | b | — | im2 |
| g2 (nand) | `n2 PORT MAP (o1 => im3, i2 => im2, i1 => a)` | a | im2 | im3 |
| g3 (nand) | `n2 PORT MAP (a, gt, im4)` | a | gt | im4 |

Ne segue lo schema: `im2 = NOT b` (g1), `im3 = NOT(a AND im2) = NOT(a AND NOT b)` (g2), `im1 = NOT a` (g0), `im4 = NOT(a AND gt)` (g3). Il segnale `im2` collega l'uscita di g1 all'ingresso di g2: è così che i segnali fanno da fili.
> 🧩 Derivazione mia: le espressioni di `im1`…`im4` seguono dal binding di [[component-binding]] (`n1` = invertitore, `n2` = NAND).

### Derivazione — associazione posizionale nel testbench · [[3-Descrizione Strutturale.pdf#page=29|p. 29]]
**Fonte:** `a1: comp4 PORT MAP (a, b, gnd, vdd, gnd, gtr, eql, lss);`

| Posizione | Port di `comp4` | Segnale | Significato |
|---|---|---|---|
| 1, 2 | `a`, `b` | a, b | i nibble da confrontare |
| 3 | `a_gt_b` (IN) | gnd | «stadio precedente: maggiore» = 0 |
| 4 | `a_eq_b` (IN) | vdd | «stadio precedente: uguale» = 1 |
| 5 | `a_lt_b` (IN) | gnd | «stadio precedente: minore» = 0 |
| 6, 7, 8 | `a_gt_b_out`, `a_eq_b_out`, `a_lt_b_out` | gtr, eql, lss | uscite osservate |

Gli ingressi di cascata a «uguale» dicono al comparatore che i bit più significativi (inesistenti) sono pari: il risultato dipende solo dai 4 bit. Vedi [[nibble-comparator]].

## Spiegazione

L'associazione posizionale è compatta ma fragile: se cambia l'ordine dei port nell'entity, i collegamenti si scambiano senza errori di compilazione (se i tipi coincidono). L'associazione nominale è più lunga ma robusta e leggibile, ed è quella da preferire nei progetti. Ogni istanza è hardware in parallelo con tutto il resto: l'ordine delle istanze nel corpo non conta.

## Perché importa

È il costrutto con cui si compone ogni sistema del corso e si istanzia il DUT nei testbench.

## Connessioni

- [[component-binding]] — dichiarazione del component e scelta dell'architecture
- [[generics-vhdl]] — `GENERIC MAP` e priorità dei valori
- [[port-vhdl]] — modi e tipi dei port da collegare
- [[generate-vhdl]] — istanziazioni ripetute
- [[assegnazione-concorrente]] — anche l'assegnazione è uno statement concorrente

## Fonti · [[3-Descrizione Strutturale.pdf#page=19|p. 19]]–[[3-Descrizione Strutturale.pdf#page=22|22]], [[3-Descrizione Strutturale.pdf#page=29|29]]

- [[descrizione-strutturale-lezione]]

_Aggiornato: 2026-11-22 — creazione_
