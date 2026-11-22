---
tipo: entità
categoria: dispositivo
---

# Half adder (semisommatore)

## Cos'è · [[2-Descrizione Dataflow.pdf#page=6|p. 6]]

Rete combinatoria che somma due bit `A` e `B` e produce la somma `Sum` e il riporto `Carry`. In dataflow è l'esempio dell'assegnazione incondizionata:

```vhdl
ARCHITECTURE dataflow OF HalfAdder IS
BEGIN
  Sum   <= A XOR B;
  Carry <= A AND B;
END ARCHITECTURE dataflow;
```

### Derivazione — tabella di verità e controllo aritmetico
> 🧩 Derivazione mia: tabella ricavata dalle due espressioni della slide.

| A | B | Sum = A XOR B | Carry = A AND B | A + B = 2·Carry + Sum |
|---|---|---|---|---|
| 0 | 0 | 0 | 0 | 0 |
| 0 | 1 | 1 | 0 | 1 |
| 1 | 0 | 1 | 0 | 1 |
| 1 | 1 | 0 | 1 | 2 |

L'ultima colonna verifica che `Carry Sum` letto come numero binario di 2 bit è proprio la somma aritmetica `A + B`.

## Come si usa nel corso

Esempio di descrizione dataflow (Lezione 2); è il mattone del full adder e dei sommatori a più bit, che compaiono nelle descrizioni strutturali.

## Concetti correlati

- [[assegnazione-concorrente]] — le due assegnazioni incondizionate, indipendenti dall'ordine
- [[descrizione-dataflow]]

## Fonti

- [[descrizione-dataflow-lezione]]

_Aggiornato: 2026-11-22 — creazione_
