---
tipo: entità
categoria: dispositivo
---

# Buffer tristate

## Cos'è · [[2-Descrizione Dataflow.pdf#page=8|p. 8]]

Buffer con un ingresso di abilitazione: quando è abilitato l'uscita copia l'ingresso, altrimenti è in **alta impedenza** (`'Z'`), cioè elettricamente scollegata. In VHDL si descrive con un'assegnazione condizionata:

```vhdl
ARCHITECTURE dataflow OF TriStateBuffer IS
BEGIN
  BufOut <= BufIn WHEN Enable = '1'
            ELSE 'Z';
END ARCHITECTURE dataflow;
```

| Enable | BufOut |
|---|---|
| '1' | BufIn |
| altro | 'Z' |

(Nella slide manca l'apice di chiusura di `'1'`.)

## Come si usa nel corso

Primo esempio di assegnazione condizionata (Lezione 2) e, combinato con un multiplexer, del mux 2:1 con uscita tristate (`en` = abilitazione della tristate). Le uscite tristate servono quando più dispositivi pilotano lo stesso filo (un bus): uno alla volta è abilitato, gli altri sono in `'Z'`.

## Concetti correlati

- [[assegnazione-condizionata]], [[assegnazione-selezionata]] — le due scritture equivalenti
- [[std-logic]] — il valore `'Z'`
- [[multiplexer]] — il mux con abilitazione tristate

## Fonti

- [[descrizione-dataflow-lezione]]

_Aggiornato: 2026-11-22 — creazione_
