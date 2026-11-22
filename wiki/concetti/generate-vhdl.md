---
tipo: concetto
importanza_esame: alta
prerequisiti: ["istanziazione-componenti"]
fonti_pdf: ["3-Descrizione Strutturale.pdf#page=26", "3-Descrizione Strutturale.pdf#page=27"]
---

# Costrutti GENERATE

## Definizione · [[3-Descrizione Strutturale.pdf#page=26|p. 26]]

Il costrutto **generate** istanzia **iterativamente** un insieme di statement concorrenti. Serve per i blocchi fatti di un blocco più semplice ripetuto molte volte (un sommatore carry-ripple, una porta che opera su word, …). Due forme:

```vhdl
label : FOR identifier IN range GENERATE
  concurrent_statements;
END GENERATE [label];

label : IF (boolean_expression) GENERATE
  concurrent_statements;
END GENERATE [label];
```

- dentro un generate può stare **qualsiasi statement concorrente** (istanze, assegnazioni, process);
- `ELSE` ed `ELSIF` con il generate si possono usare solo dal **VHDL 2008**.

## Derivazioni

### Derivazione — le 8 AND generate dal ciclo · [[3-Descrizione Strutturale.pdf#page=27|p. 27]]
**Fonte:** codice e figura, senza la lista delle istanze.

```vhdl
G1 : FOR n IN 7 DOWNTO 0 GENERATE
  and_gate : and02 PORT MAP( a0 => sig1(n), a1 => sig2(n), y => z(n));
END GENERATE G1;
```

| n | Istanza | a0 | a1 | y |
|---|---|---|---|---|
| 7 | `G1(7).and_gate` | sig1(7) | sig2(7) | z(7) |
| 6 | `G1(6).and_gate` | sig1(6) | sig2(6) | z(6) |
| … | … | … | … | … |
| 0 | `G1(0).and_gate` | sig1(0) | sig2(0) | z(0) |

Il range `7 DOWNTO 0` contiene 8 valori, quindi 8 istanze. Il nome dell'istanza è unico perché comprende l'indice del ciclo. Risultato: `z = sig1 AND sig2` bit a bit.

![[vhdl-3-p27-for-generate-and.png]]
*Le 8 porte AND: in figura il bus d'uscita si chiama `sig3`, nel codice `z`.*

**Verifica:** lo stesso circuito si ottiene con una sola assegnazione dataflow `z <= sig1 AND sig2;` (operatore logico su vettori, word gate): il generate serve quando il blocco ripetuto è un **componente**, non un operatore.

### Derivazione — perché il nibble comparator si presta al generate · [[3-Descrizione Strutturale.pdf#page=27|p. 27]]
**Fonte:** la slide introduce il nibble comparator nella pagina del `FOR GENERATE`, ma il codice mostrato è quello delle AND.
> 🧩 Derivazione mia, dall'interfaccia della slide (ingressi `gt`, `eq`, `lt` del «previous» stadio).

L'interfaccia ha gli ingressi di cascata «previous greater, equal, less than»: il comparatore si costruisce come **catena di 4 stadi da 1 bit**, ciascuno dei quali riceve il verdetto dello stadio precedente e lo aggiorna con il proprio bit. Una catena di stadi identici è proprio il caso d'uso del `FOR … GENERATE` (l'architecture si chiama infatti `iterative` nel testbench). Il tempo di risposta dipende da quanti stadi deve attraversare l'informazione: è l'origine del worst case e del best case nel [[testbench]].

## Spiegazione

`FOR … GENERATE` è un ciclo che **replica hardware**, non un ciclo eseguito nel tempo: tutte le istanze esistono contemporaneamente. `IF … GENERATE` include o esclude statement a seconda di una condizione statica (tipicamente su un generic o sull'indice del ciclo, ad es. per trattare diversamente il primo o l'ultimo stadio di una catena).

## Perché importa

Registri a N bit, sommatori ripple-carry, comparatori iterativi, banchi di flip-flop: ogni struttura regolare parametrica (con un generic per la larghezza) si scrive con il generate.

## Connessioni

- [[istanziazione-componenti]] — il generate ripete istanze
- [[generics-vhdl]] — il range del ciclo dipende spesso da un generic
- [[nibble-comparator]] — struttura iterativa
- [[operatori-vhdl]] — l'alternativa dataflow con gli operatori su vettori

## Fonti · [[3-Descrizione Strutturale.pdf#page=26|p. 26]]–[[3-Descrizione Strutturale.pdf#page=27|27]]

- [[descrizione-strutturale-lezione]]

_Aggiornato: 2026-11-22 — creazione_
