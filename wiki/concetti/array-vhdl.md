---
tipo: concetto
importanza_esame: alta
prerequisiti: ["tipi-vhdl", "std-logic"]
fonti_pdf: ["1-Principali elementi sintattici VHDL.pdf#page=14", "1-Principali elementi sintattici VHDL.pdf#page=15", "1-Principali elementi sintattici VHDL.pdf#page=16", "1-Principali elementi sintattici VHDL.pdf#page=17", "1-Principali elementi sintattici VHDL.pdf#page=18"]
---

# Array in VHDL

## Definizione · [[1-Principali elementi sintattici VHDL.pdf#page=14|p. 14]]–[[1-Principali elementi sintattici VHDL.pdf#page=15|15]] · [[1-Principali elementi sintattici VHDL.pdf#page=18|p. 18]]

Un **array** è una collezione di elementi **dello stesso tipo**, indicizzati. Può essere:

- **monodimensionale** (vettore) o **multidimensionale**: `ARRAY (1 to 4, 1 to 4) of bit`;
- **constrained**, se i limiti degli indici sono fissati nel tipo: `TYPE Vector IS ARRAY(7 DOWNTO 0) of std_logic;`
- **unconstrained**, se i limiti si fissano quando si dichiara l'oggetto: `TYPE VectorT IS ARRAY (INTEGER range <>) of std_logic;` e poi `SIGNAL v : VectorT (5 downto -5);`

Accesso:

| Forma | Significato |
|---|---|
| `a(1)`, `b(1, 1)` | un elemento |
| `a(8 TO 15)` | **slice**: 8 elementi contigui di un array monodimensionale |
| `('1','0','1','1')` | aggregato **posizionale** |
| `(1 => '1', 3 => '1', 4 => '1', 2 => '0')` | aggregato **per nome** (ordine libero) |
| `('1', 2 => '0', OTHERS => '1')` | aggregato misto; `others` copre gli elementi non nominati |
| `x & y` | concatenazione |

L'indice può essere di **qualsiasi tipo discreto**, anche un tipo enumerazione: `TYPE qit_2d IS ARRAY (qit, qit) OF qit;`.

## Derivazioni

### Derivazione — gli aggregati di `segnale_c` · [[1-Principali elementi sintattici VHDL.pdf#page=15|p. 15]]
**Fonte:** quattro assegnazioni date senza il valore risultante; `TYPE c IS ARRAY (1 TO 4) of bit;`.

| Aggregato | (1) | (2) | (3) | (4) |
|---|---|---|---|---|
| `('1','0','1','1')` | 1 | 0 | 1 | 1 |
| `(1 => '1', 3 => '1', 4 => '1', 2 => '0')` | 1 | 0 | 1 | 1 |
| `(1 => '1', 2 => '0', 3 => '1', 4 => '1')` | 1 | 0 | 1 | 1 |
| `('1', 2 => '0', OTHERS => '1')` | 1 (posizionale) | 0 (per nome) | 1 (others) | 1 (others) |

Tutte e quattro assegnano lo stesso valore `1011`: le slide mostrano quattro modi di scrivere la stessa cosa.

### Derivazione — slice, concatenazioni e «shift» · [[1-Principali elementi sintattici VHDL.pdf#page=17|p. 17]]
**Fonte:** assegnazioni commentate solo a parole.
**Si parte da:** in un'assegnazione fra array gli elementi si accoppiano **per posizione**, da sinistra a destra, non per indice.

| Istruzione | Accoppiamento elemento per elemento |
|---|---|
| `sq8 <= sq16(11 DOWNTO 4)` | `sq8(7)←sq16(11)`, `sq8(6)←sq16(10)`, …, `sq8(0)←sq16(4)` |
| `sq16(15 DOWNTO 12) <= sq4` | `sq16(15)←sq4(3)`, …, `sq16(12)←sq4(0)` |
| `sq1 <= sq_4_8(0, 7)` | riga 0 (l'ultima, perché il range è `3 DOWNTO 0`), colonna 7 (l'ultima di `0 TO 7`) |
| `sq4 <= sq_nibble_8(2)` | `sq_nibble_8` ha indici `0 TO 7`: l'elemento 2 è il **terzo** nibble |
| `sq4 <= sq8(2) & sq8(3) & sq8(4) & sq8(5)` | `sq4(3)←sq8(2)`, `sq4(2)←sq8(3)`, `sq4(1)←sq8(4)`, `sq4(0)←sq8(5)`: i bit 5…2 di `sq8` in **ordine invertito** |

Il caso `sq8 <= sq8(0) & sq8(7 DOWNTO 1)`, con un valore di esempio:

| | 7 | 6 | 5 | 4 | 3 | 2 | 1 | 0 |
|---|---|---|---|---|---|---|---|---|
| prima | 1 | 0 | 1 | 1 | 0 | 0 | 0 | **1** |
| dopo | **1** | 1 | 0 | 1 | 1 | 0 | 0 | 0 |

I bit 7…1 scendono di una posizione e il vecchio bit 0 rientra in posizione 7.
> 🧩 Derivazione mia: la slide la chiama «shift a destra», ma il bit uscente rientra dall'altra parte: è una **rotazione** a destra (come `ror 1`, vedi [[operatori-vhdl]]). Uno shift logico vero si scriverebbe `'0' & sq8(7 DOWNTO 1)`.

### Derivazione — la ROM 16×4 restituisce l'indirizzo · [[1-Principali elementi sintattici VHDL.pdf#page=16|p. 16]]
**Fonte:** codice dato senza dire cosa calcola.

| Riga | Cosa fa |
|---|---|
| `type MEMORY_16_4 is array (0 to 15) of std_logic_vector(3 downto 0)` | 16 parole da 4 bit |
| `constant ROM_16_4 : MEMORY_16_4 := (x"0", …, x"f")` | la parola $k$ vale $k$ (in esadecimale) |
| `main : process(address)` | il process si riattiva quando cambia `address` |
| `dout <= ROM_16_4(to_integer(unsigned(address)))` | legge la parola di indice `address` (conversioni in [[signed-unsigned]]) |

Poiché la parola $k$ contiene $k$, si ha sempre `dout = address`: è una ROM d'esempio il cui contenuto rende facile verificare la lettura in simulazione. Con un'altra costante la stessa architettura realizza una funzione qualsiasi da 4 a 4 bit.

### Derivazione — la NAND a 4 valori · [[1-Principali elementi sintattici VHDL.pdf#page=18|p. 18]]
**Fonte:** tabella data senza lettura.
**Si parte da:** `qit_nand2_table(i1, i2)`: il primo indice (`i1`) sceglie la **riga**, il secondo (`i2`) la **colonna**.

| `i1` \ `i2` | '0' | '1' | 'Z' | 'X' |
|---|---|---|---|---|
| '0' | 1 | 1 | 1 | 1 |
| '1' | 1 | 0 | 0 | X |
| 'Z' | 1 | 0 | 0 | X |
| 'X' | 1 | X | X | X |

Letture:
- un ingresso a `'0'` forza l'uscita a `'1'` qualunque sia l'altro (riga e colonna `'0'`), come nella NAND booleana;
- `'Z'` si comporta come `'1'` (righe `'1'` e `'Z'` uguali): un ingresso flottante è letto come alto;
- con un ingresso `'X'` e l'altro non a `'0'` l'uscita è `'X'`: non si può sapere.
- la tabella è simmetrica, come deve essere per una porta commutativa.

`AFTER 5ns` assegna `o1` con un ritardo di 5 ns: l'architettura si chiama `average_delay` perché modella il ritardo medio della porta.

## Spiegazione

Gli array sono ovunque: `std_logic_vector` e `bit_vector` sono array, una stringa è un array di caratteri, una memoria è un array di vettori. Le cose da padroneggiare sono la direzione del range (`TO` crescente, `DOWNTO` decrescente), l'accoppiamento **posizionale** nelle assegnazioni fra array (non per indice) e gli aggregati, in particolare `others` (l'idioma `(others => '0')` azzera un vettore di qualunque lunghezza).

Usare una costante array come **tabella** (ROM, tabella di verità) è il modo di descrivere una funzione combinatoria elencandone i valori invece di scriverne l'espressione.

## Perché importa

Memorie, registri a più bit, banchi di registri e tabelle di verità sono array: la ROM della slide è lo schema di ogni memoria a sola lettura che si scriverà nei progetti.

## Connessioni

- [[signed-unsigned]] — conversione dell'indirizzo per indicizzare la ROM
- [[subtype-vhdl]] — un subtype rende constrained un array unconstrained
- [[attributi-vhdl]] — `'LEFT`, `'RANGE`, `'LENGTH` degli array
- [[operatori-vhdl]] — `&` e gli operatori di shift
- [[record-vhdl]] — l'altro tipo composto, con elementi di tipi diversi

## Fonti · [[1-Principali elementi sintattici VHDL.pdf#page=14|p. 14]]–[[1-Principali elementi sintattici VHDL.pdf#page=18|18]]

- [[elementi-sintattici-vhdl-lezione]]

_Aggiornato: 2026-11-22 — creazione_
