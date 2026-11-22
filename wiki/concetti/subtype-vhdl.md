---
tipo: concetto
importanza_esame: media
prerequisiti: ["tipi-vhdl", "array-vhdl"]
fonti_pdf: ["1-Principali elementi sintattici VHDL.pdf#page=23", "1-Principali elementi sintattici VHDL.pdf#page=24"]
---

# Subtype in VHDL

## Definizione · [[1-Principali elementi sintattici VHDL.pdf#page=23|p. 23]]–[[1-Principali elementi sintattici VHDL.pdf#page=24|24]]

Un **subtype** è un sottoinsieme dei valori di un tipo esistente (il **tipo base**), con cui resta **completamente compatibile**. Si usa:

1. per restringere i valori: `SUBTYPE digits IS character RANGE '0' to '9';`
2. per rendere **constrained** un array unconstrained, fissandone i limiti: `SUBTYPE id IS string(1 TO 20);`, `SUBTYPE word IS bit_vector(31 DOWNTO 0);`

Subtype numerici predefiniti:

```vhdl
SUBTYPE natural  IS integer RANGE 0 TO highest_integer;
SUBTYPE positive IS integer RANGE 1 TO highest_integer;
```

**Subtype contro nuovo tipo:**

```vhdl
SUBTYPE compatible_nibble_bits IS BIT_VECTOR (3 DOWNTO 0);   -- compatibile con BIT_VECTOR
TYPE    nibble_bits            IS ARRAY (3 DOWNTO 0) OF BIT; -- NON compatibile con BIT_VECTOR
```

## Derivazioni

### Derivazione — perché `nibble_bits` non è compatibile · [[1-Principali elementi sintattici VHDL.pdf#page=24|p. 24]]
**Fonte:** la slide afferma la non compatibilità senza spiegarla.

| Dichiarazione | Cosa crea | Tipo base | Assegnabile a/da `BIT_VECTOR`? |
|---|---|---|---|
| `SUBTYPE compatible_nibble_bits IS BIT_VECTOR (3 DOWNTO 0)` | un vincolo su un tipo esistente | `BIT_VECTOR` | sì, è lo stesso tipo con i limiti fissati |
| `TYPE nibble_bits IS ARRAY (3 DOWNTO 0) OF BIT` | un **tipo nuovo** | sé stesso | no: il VHDL è fortemente tipizzato e due tipi distinti non si mescolano, anche se hanno la stessa struttura |

**Conseguenza:** un segnale `nibble_bits` non si può collegare a una porta `bit_vector(3 downto 0)` senza una conversione esplicita, mentre un `compatible_nibble_bits` sì.

## Spiegazione

`TYPE` crea sempre un tipo nuovo e incompatibile con tutti gli altri; `SUBTYPE` aggiunge solo un vincolo (un range, i limiti di un array) a un tipo che c'è già. Quando serve un vettore di dimensione fissa da riusare (una «word», un indirizzo) conviene il subtype, così gli oggetti restano compatibili con `bit_vector` o `std_logic_vector` e con le funzioni di libreria.

`natural` e `positive` sono subtype di `integer`: un `natural` si somma senza problemi a un `integer`.

## Perché importa

La distinzione `TYPE`/`SUBTYPE` spiega molti errori di compilazione («tipo incompatibile» tra due vettori apparentemente uguali) ed è una domanda classica sulla tipizzazione forte.

## Connessioni

- [[tipi-vhdl]] — tipizzazione forte, `integer`, `natural`, `positive`
- [[array-vhdl]] — array constrained e unconstrained
- [[attributi-vhdl]] — `'BASE` restituisce il tipo base di un subtype; gli attributi enumerativi lavorano sul tipo base

## Fonti · [[1-Principali elementi sintattici VHDL.pdf#page=23|p. 23]]–[[1-Principali elementi sintattici VHDL.pdf#page=24|24]]

- [[elementi-sintattici-vhdl-lezione]]

_Aggiornato: 2026-11-22 — creazione_
