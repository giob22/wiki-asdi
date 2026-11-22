---
tipo: entità
categoria: dispositivo
---

# Porta XOR (a 2, 3 e N ingressi)

## Cos'è · Simulazione [[4-Tecniche di simulazione e ritardi.pdf#page=2|p. 2]]–[[4-Tecniche di simulazione e ritardi.pdf#page=3|3]] · Comportamentale [[5-Descrizione Comportamentale.pdf#page=23|p. 23]], [[5-Descrizione Comportamentale.pdf#page=25|25]]

Lo XOR (OR esclusivo) di più bit vale 1 quando il numero di ingressi a 1 è **dispari** (funzione di parità). Nel corso compare in tre forme:

| Dove | Forma | Come è descritta |
|---|---|---|
| Lezione 4 | XOR a 2 ingressi | netlist di buffer, NOT, AND, OR: $z = a\,\overline{b} + \overline{a}\,b$ (esempio di simulazione a tempo quantizzato) |
| Lezione 5 | `XOR_3` | `CASE` sugli 8 valori dell'ingresso a 3 bit (tabella di verità) |
| Lezione 5 | `XOR_N` | `FOR LOOP` che conta i bit a 1 e ne prende il resto modulo 2; N è un generic |

Le derivazioni (tabella dello XOR a 3 ingressi, traccia del loop per N = 4) sono in [[istruzioni-sequenziali]]; quella della netlist in [[simulazione-tempo-quantizzato]].

## Come si usa nel corso

Esempio ricorrente di funzione combinatoria descritta in stili diversi: netlist di porte, tabella di verità con `CASE`, algoritmo con un ciclo. Anche la somma dell'half adder (Lezione 2) è uno XOR: `Sum <= A XOR B`.

## Concetti correlati

- [[istruzioni-sequenziali]], [[simulazione-tempo-quantizzato]], [[half-adder]], [[generics-vhdl]]

## Fonti

- [[tecniche-di-simulazione-lezione]]
- [[descrizione-comportamentale-lezione]]

_Aggiornato: 2026-11-22 — creazione_
