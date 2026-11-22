---
tipo: entità
categoria: dispositivo
---

# Multiplexer

## Cos'è · [[2-Descrizione Dataflow.pdf#page=8|p. 8]]

Rete combinatoria che porta in uscita uno fra più ingressi, scelto da un ingresso di **selezione**. Il mux 2:1 ha due ingressi dati (`in_0`, `in_1`) e un bit di selezione (`sel`). La slide ne descrive uno su un bit con **abilitazione tristate** e ritardo di propagazione `Tpd`:

```vhdl
mux_out <= 'Z'  AFTER Tpd WHEN en = '0' ELSE
           in_0 AFTER Tpd WHEN sel = '0' ELSE
           in_1 AFTER Tpd;
```

| en | sel | mux_out |
|---|---|---|
| 0 | – | 'Z' |
| 1 | 0 | in_0 |
| 1 | 1 | in_1 |

È «un mux con selezione `sel` la cui uscita è l'ingresso primario di una tristate controllata da `en`»: la lettura passo-passo e il ruolo dell'ordine delle condizioni sono in [[assegnazione-condizionata]].

## Come si usa nel corso

Esempio di assegnazione condizionata con priorità (Lezione 2). Il multiplexer è anche il circuito che corrisponde a un'[[assegnazione-selezionata]] e uno dei componenti «notevoli» che si compongono nei sistemi più grandi.

## Concetti correlati

- [[assegnazione-condizionata]], [[assegnazione-selezionata]]
- [[buffer-tristate]] — lo stadio di uscita
- [[array-vhdl]] — una ROM è, dal punto di vista funzionale, un mux che sceglie fra costanti

## Fonti

- [[descrizione-dataflow-lezione]]

_Aggiornato: 2026-11-22 — creazione_
