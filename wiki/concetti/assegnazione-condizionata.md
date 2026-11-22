---
tipo: concetto
importanza_esame: alta
prerequisiti: ["assegnazione-concorrente"]
fonti_pdf: ["2-Descrizione Dataflow.pdf#page=7", "2-Descrizione Dataflow.pdf#page=8", "2-Descrizione Dataflow.pdf#page=9", "2-Descrizione Dataflow.pdf#page=12"]
---

# Assegnazione condizionata (`WHEN … ELSE`)

## Definizione · [[2-Descrizione Dataflow.pdf#page=7|p. 7]]

L'**assegnazione condizionata** è un'assegnazione concorrente che sceglie la waveform da assegnare al segnale target in base a quale **condizione booleana** è vera, come un if-then-else:

```vhdl
segnale <= waveform_1 WHEN condizione_1 ELSE
           waveform_2 WHEN condizione_2 ELSE
           ...
           waveform_n;
```

- le condizioni **possono sovrapporsi**: conta l'**ordine** di valutazione, dalla prima all'`ELSE` finale; vince la prima condizione vera;
- termina con un `ELSE` **senza condizione**;
- è un'abbreviazione di un process con `IF … ELSIF … ELSE` seguito da `WAIT` sui segnali da cui dipendono le clausole · [[2-Descrizione Dataflow.pdf#page=9|p. 9]].

## Derivazioni

### Derivazione — tabella del buffer tristate · [[2-Descrizione Dataflow.pdf#page=8|p. 8]]
**Fonte:** `BufOut <= BufIn WHEN Enable = '1' ELSE 'Z';` con la spiegazione a parole.

| Enable | BufOut |
|---|---|
| '1' | BufIn |
| qualsiasi altro valore | 'Z' |

Con `std_logic` «qualsiasi altro valore» comprende '0' ma anche 'U', 'X', …: l'`ELSE` finale copre tutto ciò che non soddisfa la condizione. Vedi [[buffer-tristate]].

### Derivazione — il mux 2:1 con abilitazione tristate · [[2-Descrizione Dataflow.pdf#page=8|p. 8]]
**Fonte:** codice e descrizione a parole («mux la cui uscita è l'ingresso di una tristate controllata da en»).

```vhdl
mux_out <= 'Z'  AFTER Tpd WHEN en = '0' ELSE
           in_0 AFTER Tpd WHEN sel = '0' ELSE
           in_1 AFTER Tpd;
```

| en | sel | Condizione vera per prima | mux_out (dopo Tpd) |
|---|---|---|---|
| 0 | – | `en = '0'` | 'Z' |
| 1 | 0 | `sel = '0'` | in_0 |
| 1 | 1 | nessuna → `ELSE` | in_1 |

**La priorità fa il lavoro:** la seconda condizione non controlla `en`; è l'ordine a garantire che `sel` conti solo quando `en = '1'`. Scrivere prima `sel = '0'` e poi `en = '0'` darebbe un circuito diverso (con `en = '0'` e `sel = '0'` l'uscita sarebbe `in_0` invece di `'Z'`).
**Ritardo:** ogni ramo ha `AFTER Tpd`: qualunque ramo venga scelto, l'uscita cambia `Tpd` dopo la variazione degli ingressi.

### Derivazione — il process equivalente del mux · [[2-Descrizione Dataflow.pdf#page=9|p. 9]]
**Fonte:** regola generale; la sensitivity list è «l'insieme dei segnali da cui dipendono le clausole».
> 🧩 Derivazione mia: applico lo schema della slide al mux.

```vhdl
PROCESS
BEGIN
  IF en = '0' THEN
    mux_out <= 'Z' AFTER Tpd;
  ELSIF sel = '0' THEN
    mux_out <= in_0 AFTER Tpd;
  ELSE
    mux_out <= in_1 AFTER Tpd;
  END IF;
  WAIT ON en, sel, in_0, in_1;
END PROCESS;
```

La sensitivity list contiene i segnali delle **condizioni** (`en`, `sel`) e quelli delle **waveform** (`in_0`, `in_1`): se ne mancasse uno, una sua variazione non aggiornerebbe l'uscita.

## Spiegazione

Il `WHEN … ELSE` è il costrutto concorrente con **priorità**: le condizioni si leggono in ordine e la prima vera decide. In hardware corrisponde a una catena di multiplexer, in cui la prima condizione comanda il mux più vicino all'uscita.
> 🧩 Derivazione mia (corrispondenza con l'hardware): ogni `WHEN c ELSE` è un mux 2:1 che sceglie fra la sua waveform e il resto della catena.

Quando le condizioni sono **mutuamente esclusive** la priorità non serve e il costrutto equivale a un'[[assegnazione-selezionata]] · [[2-Descrizione Dataflow.pdf#page=12|p. 12]].

## Perché importa

È il modo più naturale di scrivere buffer tristate, mux con abilitazione, logica di priorità (encoder con priorità). Nei progetti d'esame è frequente; l'errore tipico è dimenticare che l'ordine delle condizioni cambia il circuito.

## Connessioni

- [[assegnazione-concorrente]] — è una delle tre forme
- [[assegnazione-selezionata]] — l'alternativa senza priorità
- [[buffer-tristate]], [[multiplexer]] — gli esempi della slide
- [[std-logic]] — il valore `'Z'` di alta impedenza

## Fonti · [[2-Descrizione Dataflow.pdf#page=7|p. 7]]–[[2-Descrizione Dataflow.pdf#page=9|9]], [[2-Descrizione Dataflow.pdf#page=12|12]]

- [[descrizione-dataflow-lezione]]

_Aggiornato: 2026-11-22 — creazione_
