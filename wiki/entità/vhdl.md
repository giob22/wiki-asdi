---
tipo: entità
categoria: standard
---

# VHDL

## Cos'è · [[1-Introduzione al corso ASDi.pdf#page=4|p. 4]]–[[1-Introduzione al corso ASDi.pdf#page=7|7]]

Il **VHDL** (Very High Speed Integrated Circuits Hardware Description Language) è un **linguaggio di descrizione dell'hardware**: non descrive le operazioni che un esecutore deve svolgere, ma gli **elementi che costituiscono il circuito** che svolge l'elaborazione. È un linguaggio **concorrente** e una descrizione può essere fatta a diversi **livelli di astrazione**: dataflow, strutturale, comportamentale, RTL.

Insieme al Verilog è il linguaggio con cui si programmano sia gli ASIC sia gli FPGA: il Verilog (e il SystemVerilog) è preferito per gli ASIC e negli USA, il VHDL prevale nel campo degli FPGA e in Europa.

## Come si usa nel corso

È il linguaggio di tutto il corso: si studia come linguaggio (Lezioni 1–5, [[elementi-sintattici-vhdl-lezione]]) e si usa per descrivere, simulare e sintetizzare le macchine combinatorie e sequenziali progettate, fino all'esercizio di progetto d'esame (implementazione VHDL + simulazione).

Caratteristiche viste nella Lezione 1:
- non case sensitive, formato libero, commenti con `--` → [[elementi-lessicali-vhdl]]
- fortemente tipizzato → [[tipi-vhdl]]
- tre classi di oggetti: costanti, variabili, segnali → [[oggetti-vhdl]]

## Concetti correlati

- [[elementi-lessicali-vhdl]], [[oggetti-vhdl]], [[tipi-vhdl]], [[std-logic]], [[signed-unsigned]]
- [[array-vhdl]], [[record-vhdl]], [[alias-vhdl]], [[subtype-vhdl]], [[attributi-vhdl]], [[operatori-vhdl]]
- [[ieee-std-logic-1164]], [[ieee-numeric-std]] — i package IEEE standard

## Fonti

- [[elementi-sintattici-vhdl-lezione]]
- il PDF di introduzione al corso (`raw/teoria/`), non ancora ingestito: qui se ne usano solo le definizioni del linguaggio

_Aggiornato: 2026-11-22 — creazione_
