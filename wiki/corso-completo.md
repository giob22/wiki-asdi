# Architettura dei Sistemi Digitali — corso completo

Testo unico di studio del corso (LM Ingegneria Informatica, UNINA, a.a. 2026-27, Proff. Nicola Mazzocca e Alessandra De Benedictis; esame: elaborato di gruppo, esercizio di progetto in aula (VHDL e simulazione), prova orale). Contiene **solo ciò che sta nei PDF del corso**, nell'ordine delle slide: definizioni, formule, esempi, figure e le dimostrazioni svolte a mano dal docente. I passaggi che le slide saltano sono ricostruiti in una riga dove servono a seguire il discorso; le derivazioni estese, i grafici aggiuntivi e gli esercizi stanno nelle pagine concetto ed esercizio, richiamate in fondo a ogni lezione («Approfondimenti nel wiki»).

**Come leggerlo.** Il riferimento al PDF compare solo nel titolo di ogni sezione (`p. N` apre la pagina). Le equazioni numerate sono quelle delle slide di ciascuna lezione. Il PDF di una lezione si genera con `python output/crea_pdf.py N` (file in `output/pdf/`); il sito di studio si genera da questo file con `python output/crea_sito.py`.

## Indice

| # | Lezione | PDF sorgente |
|---|---|---|
| 1 | [[#Lezione 1 — VHDL: principali elementi sintattici\|VHDL: principali elementi sintattici]] | 1-Principali elementi sintattici VHDL.pdf |
| 2 | [[#Lezione 2 — VHDL: descrizione Dataflow\|VHDL: descrizione Dataflow]] | 2-Descrizione Dataflow.pdf |
| 3 | [[#Lezione 3 — VHDL: descrizione strutturale\|VHDL: descrizione strutturale]] | 3-Descrizione Strutturale.pdf |

<!-- Ogni lezione è una sezione «## Lezione N — titolo» (trattino lungo): diventa la pagina lezione-N.html del sito.

## Lezione N — Titolo

*Fonte: file.pdf (N pagine, slide + appunti a mano alle p. ...).*

### Primo argomento · [[file.pdf#page=2|p. 2]], [[file.pdf#page=3|3]]

- Definizione...

$$y(t) = x(t) \ast h(t) \tag{1}$$

![[file-p3-descrizione.png]]
*Didascalia della figura.*

*Approfondimenti nel wiki: [[concetto-a]], [[concetto-b]]*
-->

## Lezione 1 — VHDL: principali elementi sintattici

*Fonte: 1-Principali elementi sintattici VHDL.pdf, 39 pagine (slide «Il VHDL come linguaggio», v1.0).*

### Roadmap · [[1-Principali elementi sintattici VHDL.pdf#page=1|p. 1]]

Elementi lessicali, identificatori, oggetti (costanti, segnali, variabili), tipi (interi, physical, floating, enumerazione, …), array e record, aliasing, subtype, attributi, operatori.

### Elementi lessicali · [[1-Principali elementi sintattici VHDL.pdf#page=2|p. 2]]–[[1-Principali elementi sintattici VHDL.pdf#page=4|4]]

- Il VHDL **non è case sensitive** (a differenza del C), né per gli identificatori né per le parole chiave: `ingresso = INGRESSO = INgrESso`, `Architecture = aRCHITECTURE = aRcHiTeCtURe`.
- **Formato libero**: un'istruzione può essere spezzata su più righe; spazi, tabulazioni e ritorni a capo sono trattati allo stesso modo.
- **Commenti**: iniziano in un punto qualsiasi della riga con due trattini consecutivi e finiscono a fine riga; il simulatore li ignora del tutto.

```vhdl
-- io sono un commento e vengo ignorato!
```

- **Numeri**: interi (`integer`) o reali (`real`).

```vhdl
0    1    987E6        -- numeri interi
0.0  0.5  2.71E-9      -- numeri reali
```

- **Caratteri**: caratteri ASCII tra apici: `'A'  'a'  '"'  ' '`.
- **Stringhe**: array di caratteri tra doppi apici; per mettere `"` dentro una stringa si scrive `""`.

```vhdl
"Io sono una stringa"                       -- stringa
"Io sono la stringa ""stringa"" e voi? "    -- è la sequenza: Io sono la stringa "stringa" e voi?
```

- **Bit string**: notazione binaria, ottale o esadecimale; gli underscore `_` separano le cifre in gruppi e il simulatore li ignora. Il numero 86 si può scrivere:
  - `B"1010110"` — stringa di 7 bit;
  - `O"126"` — 3 cifre ottali (9 bit);
  - `X"56"` — 2 cifre esadecimali (8 bit).
- Il numero di bit su cui è rappresentato 86 è diverso nei tre casi.

### Identificatori · [[1-Principali elementi sintattici VHDL.pdf#page=5|p. 5]]

- Sono nomi definiti dal programmatore per identificare oggetti VHDL, ad es. `overflow`, `signal_1`.
- Non si possono usare le parole riservate (`BEGIN`, `COMPONENT`, `ARCHITECTURE`, …); nelle slide le parole chiave sono in maiuscolo, anche se il VHDL non è case sensitive.
- Un identificatore lecito inizia con una lettera ed è composto da lettere, cifre e underscore `_` **non consecutivi**.
- Gli underscore sono significativi: `questo_segnale` non è `questosegnale`.

### Oggetti: costanti, variabili, segnali · [[1-Principali elementi sintattici VHDL.pdf#page=6|p. 6]]–[[1-Principali elementi sintattici VHDL.pdf#page=7|7]]

- Un **oggetto** è un'entità VHDL con un nome (identificatore unico), un tipo e un valore che appartiene all'insieme dei valori leciti del tipo.
- Tre classi di oggetti:
  1. **Costante** (`CONSTANT`): inizializzata con un valore alla definizione, non più modificabile.
  2. **Variabile** (`VARIABLE`): il valore può cambiare dopo la definizione; si usa **solo nei corpi sequenziali** (`process`). Appena definita deve avere un valore, assegnato esplicitamente (un valore del tipo o un'espressione) o implicitamente (default fissato dallo standard).
  3. **Segnale** (`SIGNAL`): connette moduli fra loro; lecito **solo nei corpi concorrenti** (`architecture`). Anche un segnale ha un valore iniziale, esplicito o implicito.

```vhdl
CONSTANT delay : Time := 5 ns;
```

| Classe | Scopo |
|---|---|
| costanti | parametri fissi di un design |
| variabili | informazione temporanea o stato nei process |
| segnali | collegamenti hardware |

### Tipi · [[1-Principali elementi sintattici VHDL.pdf#page=8|p. 8]]

- Il VHDL è **fortemente tipizzato** (strongly typed).
- Offre diversi tipi base e permette di definire tipi propri, scalari o compositi.
- Tipi scalari: ad es. `Boolean`, `Character`, `Bit`, `Real`. Tipi composti: **array** e **record**.

#### bit e std_logic · [[1-Principali elementi sintattici VHDL.pdf#page=9|p. 9]]

- `bit` ha due valori, `'0'` e `'1'`; `bit_vector` è un array di bit.
- Nei sistemi digitali servono anche stati diversi da alto e basso (alta impedenza, sconosciuto): perciò si usano `std_logic` e `std_logic_vector` al posto di `bit` e `bit_vector`.

| Valore | Significato |
|---|---|
| `'U'` | uninitialized |
| `'X'` | unknown |
| `'0'` | low |
| `'1'` | high |
| `'Z'` | high impedance |
| `'W'` | weak unknown |
| `'L'` | weak low |
| `'H'` | weak high |
| `'-'` | don't care |

```vhdl
SIGNAL s1 : std_logic;
SIGNAL s2 : std_logic_vector(7 DOWNTO 0);   -- segnale composto da 8 "fili"
```

- `STD_LOGIC` e `STD_LOGIC_VECTOR` sono definiti nella libreria `IEEE.std_logic_1164` e sono **obbligatori nei design sintetizzabili**.

#### Interi · [[1-Principali elementi sintattici VHDL.pdf#page=10|p. 10]]

- Un tipo intero è un intervallo di interi entro un range specifico.
- Il tipo predefinito `integer` sta nella libreria standard (`std`); il suo intervallo dipende dall'implementazione, ma lo standard richiede che includa almeno da −2147483647 a +2147483647 (almeno 32 bit).

```vhdl
SIGNAL myint : integer;
myint <= 5;
```

- Per ridurre i bit con cui è implementato un integer si specifica il range: a `myint` vengono assegnati i bit necessari a rappresentare i numeri da −10 a 15, cioè **5 bit**.

```vhdl
SIGNAL myint : integer range -10 TO 15;
```

- `integer` ha due sottotipi: `positive` (da 1) e `natural` (da 0).

#### signed e unsigned · [[1-Principali elementi sintattici VHDL.pdf#page=11|p. 11]]

- I bit di uno `std_logic_vector` hanno tutti lo stesso "peso"; per dare un'interpretazione numerica (ogni bit pesa secondo la sua posizione) si usano i tipi `signed` e `unsigned`.
- Sono definiti nel package `numeric_std`; per usarli si importa anche `std_logic_1164`, perché `numeric_std` lo usa.

```vhdl
library ieee;
use ieee.std_logic_1164.all;
use ieee.numeric_std.all;
....
signal sig  : signed(2 downto 0);
signal sig1 : unsigned(2 downto 0);
....
sig  <= "101";   -- sig  = -3
sig1 <= "101";   -- sig1 = 5
```

> ⚠️ Contraddizione: la slide scrive «sig1 <= "101" (sig=5)»; il valore 5 è quello di `sig1`, non di `sig`.

- Nelle operazioni di somma e sottrazione si possono «mescolare» i tipi:

| Operazione | Operando sinistro | Operando destro | Risultato |
|---|---|---|---|
| `+` e `-` | unsigned | unsigned | unsigned |
| | unsigned | natural | unsigned |
| | natural | unsigned | unsigned |
| | signed | signed | signed |
| | signed | integer | signed |
| | integer | signed | signed |
| | unsigned | std_logic | unsigned |
| | std_logic | unsigned | unsigned |
| | signed | std_logic | signed |
| | std_logic | signed | signed |

#### Conversioni e casting fra tipi · [[1-Principali elementi sintattici VHDL.pdf#page=12|p. 12]]

- `numeric_std` definisce **funzioni** per convertire signed/unsigned in integer e viceversa: `to_integer`, `to_signed`, `to_unsigned`.
- signed/unsigned e `std_logic_vector` si convertono l'uno nell'altro con un **type casting**.

![[vhdl-1-p12-conversioni-tra-tipi.png]]
*A sinistra le funzioni di `numeric_std` (`to_signed(i,size)`, `to_unsigned(i,size)`, `to_integer(s)`, `to_integer(u)`), a destra i type casting (`signed(slv)`, `unsigned(slv)`, `std_logic_vector(s)`, `std_logic_vector(u)`).*

#### Tipo enumerazione · [[1-Principali elementi sintattici VHDL.pdf#page=13|p. 13]]

- È un insieme ordinato di identificatori, tutti distinti; lo stesso identificatore può comparire in tipi enumerazione diversi.
- `TYPE stato IS ('q0', 'q1', 'q2', 'q3')` definisce un nuovo tipo di logica multivalore: `stato` è l'identificatore del tipo, `'q0'`, `'q1'`, `'q2'`, `'q3'` sono gli elementi (definiti per enumerazione), `'q0'` è il valore di default.

> ⚠️ Contraddizione: tra apici può stare un solo carattere (`'0'`, `'Z'`); con nomi di più caratteri gli elementi si scrivono senza apici: `TYPE stato IS (q0, q1, q2, q3);`.

### Array · [[1-Principali elementi sintattici VHDL.pdf#page=14|p. 14]]–[[1-Principali elementi sintattici VHDL.pdf#page=15|15]]

- Un array è una collezione di elementi indicizzati, tutti dello stesso tipo; è un tipo fondamentale del VHDL.
- Può essere monodimensionale (vettore) o multidimensionale.

```vhdl
TYPE myArrayT IS ARRAY (7 DOWNTO 0) of std_logic;
TYPE myType   IS ARRAY (1 to 4, 1 to 4) of bit;
```

- **Constrained**: i limiti degli indici sono fissati nel tipo. **Unconstrained**: i limiti si fissano quando si dichiara un oggetto di quel tipo.

```vhdl
TYPE Vector IS ARRAY(7 DOWNTO 0) of std_logic;          -- constrained
SIGNAL v : Vector;
TYPE VectorT IS ARRAY (INTEGER range <>) of std_logic;  -- unconstrained
SIGNAL v : VectorT (5 downto -5);
```

> ⚠️ Contraddizione: nella slide è scritto `ARAY`; la parola chiave è `ARRAY`.

- Un elemento si indica con nome e indici: `a(1)`, `b(1, 1)`. Una **slice** di elementi contigui di un array monodimensionale si indica con un range: `a(8 TO 15)` è un vettore di 8 elementi di `a`.
- Dato `TYPE c IS ARRAY (1 TO 4) of bit;`, si assegna un oggetto di tipo `c` con la notazione **posizionale** o con l'**associazione per nome** (l'ordine non conta); le due si possono mescolare, con `others` per tutti gli elementi non specificati.

```vhdl
segnale_c <= ('1','0','1','1');                          -- posizionale
segnale_c <= (1 => '1', 3 => '1', 4 => '1', 2 => '0');   -- per nome
segnale_c <= (1 => '1', 2 => '0', 3 => '1', 4 => '1');
segnale_c <= ('1', 2 => '0', OTHERS => '1');             -- mista, con others
```

#### Esempio: una ROM · [[1-Principali elementi sintattici VHDL.pdf#page=16|p. 16]]

```vhdl
library ieee;
use ieee.std_logic_1164.all;
use ieee.numeric_std.all;
entity ROM is
    port(
        address : in  std_logic_vector(3 downto 0);
        dout    : out std_logic_vector(3 downto 0)
    );
end entity ROM;
architecture RTL of ROM is
    type MEMORY_16_4 is array (0 to 15) of std_logic_vector(3 downto 0);
    constant ROM_16_4 : MEMORY_16_4 := (
        x"0", x"1", x"2", x"3", x"4", x"5", x"6", x"7",
        x"8", x"9", x"a", x"b", x"c", x"d", x"e", x"f"
    );
begin
    main : process(address)
    begin
        dout <= ROM_16_4(to_integer(unsigned(address)));
    end process main;
end architecture RTL;
```

- L'indice dell'array deve essere un intero tra 0 e 15; `address` è uno `std_logic_vector`, quindi va prima convertito (casting) in `unsigned` e poi in intero.

#### Slice, assegnazioni e concatenazione · [[1-Principali elementi sintattici VHDL.pdf#page=17|p. 17]]

```vhdl
TYPE qit IS ('0', '1', 'Z', 'X');
TYPE qit_nibble IS ARRAY (3 DOWNTO 0) OF qit;
TYPE qit_byte   IS ARRAY (7 DOWNTO 0) OF qit;
TYPE qit_word   IS ARRAY (15 DOWNTO 0) OF qit;
TYPE qit_4by8   IS ARRAY (3 DOWNTO 0, 0 TO 7) OF qit;
TYPE qit_nibble_by_8 IS ARRAY (0 TO 7) OF qit_nibble;
SIGNAL sq1  : qit;
SIGNAL sq4  : qit_nibble;
SIGNAL sq8  : qit_byte;
SIGNAL sq16 : qit_word;
SIGNAL sq_4_8 : qit_4by8;
SIGNAL sq_nibble_8 : qit_nibble_by_8;

sq8 <= sq16(11 DOWNTO 4);                    -- estrae una slice di 8 bit da sq16
sq16(15 DOWNTO 12) <= sq4;                   -- assegna una slice di 4 bit di sq16
sq1 <= sq_4_8(0, 7);                         -- estrae un bit da sq_4_8
sq4 <= sq_nibble_8(2);                       -- assegna il 3° nibble di sq_nibble_8 a sq4
sq8 <= sq8(0) & sq8(7 DOWNTO 1);             -- shift a destra di sq8
sq4 <= sq8(2) & sq8(3) & sq8(4) & sq8(5);    -- concatenazione di alcuni bit di sq8 in un nibble
```

#### Array indicizzato da un tipo discreto: tabella di verità · [[1-Principali elementi sintattici VHDL.pdf#page=18|p. 18]]

- Un tipo discreto (ad es. `qit`) può fare da indice di un array; qui una costante implementa la tabella di verità di una NAND a logica `qit`.

```vhdl
TYPE qit IS ('0', '1', 'Z', 'X');
TYPE qit_2d IS ARRAY (qit, qit) OF qit;
ENTITY nand2_q IS
  PORT (i1, i2 : IN qit; o1 : OUT qit);
END nand2_q;
--
ARCHITECTURE average_delay OF nand2_q IS
  CONSTANT qit_nand2_table : qit_2d := (
  --  '0'  '1'  'Z'  'X'
    ('1', '1', '1', '1'),   -- '0'
    ('1', '0', '0', 'X'),   -- '1'
    ('1', '0', '0', 'X'),   -- 'Z'
    ('1', 'X', 'X', 'X'));  -- 'X'
BEGIN
  o1 <= qit_nand2_table (i1, i2) AFTER 5ns;
END average_delay;
```

### Record · [[1-Principali elementi sintattici VHDL.pdf#page=19|p. 19]]–[[1-Principali elementi sintattici VHDL.pdf#page=21|21]]

- Un record è una collezione di elementi anche di tipo diverso; ci si riferisce a un elemento con il suo identificatore (`oggetto.campo`). Come per gli array, si usa la notazione posizionale o l'associazione per nome.

```vhdl
TYPE a_new_record_type IS RECORD
  id1, id2      : type_1;
  id3           : array_type_2;
  id4, id5, id6 : record_type_3;
END RECORD;

VARIABLE example_1 : a_new_record_type;
...
instr_1.id1 := elem_type_1;
instr_1.id2 := elem_type_1;
instr_1.id3 := elem_array_type_2;
```

- Un record è utile, ad es., per rappresentare il formato e la codifica di un'istruzione di un processore:

```vhdl
TYPE opcode IS (sta, lda, add, sub, and, nop, jmp, jsr);
TYPE mode IS RANGE 0 TO 3
TYPE address IS BIT_VECTOR (10 DOWNTO 0);
TYPE instruction_format IS RECORD
  opc : opcode;
  mde : mode;
  adr : address;
END RECORD;

SIGNAL instr : instruction_format := (nop, 0, "00000000000");
instr.opc <= lda;
instr.mde <= 2;
instr.adr <= "00011110000";
instr <= (lda, 2, "00011110000");
```

- Una costante di tipo record si scrive con i valori degli elementi tra parentesi, nell'ordine della definizione del record.
- Un segnale di tipo record si assegna un elemento alla volta oppure tutto insieme.

> ⚠️ Contraddizione: il codice delle slide ha alcuni refusi: la variabile è dichiarata come `example_1` ma usata come `instr_1`; `and` è una parola riservata e non può essere un valore del tipo `opcode`; manca il `;` dopo `RANGE 0 TO 3`; un tipo array si dichiara con `ARRAY (10 DOWNTO 0) OF BIT` (oppure come `SUBTYPE address IS BIT_VECTOR (10 DOWNTO 0)`).

### Aliasing · [[1-Principali elementi sintattici VHDL.pdf#page=22|p. 22]]

- La dichiarazione `alias` dà un nome alternativo a un oggetto o a una sua parte, per riferirvisi più comodamente; è solo un renaming e non definisce un nuovo oggetto.

```vhdl
VARIABLE instr : BIT_VECTOR(31 DOWNTO 0);
ALIAS op_code : BIT_VECTOR(7 DOWNTO 0) IS instr(31 DOWNTO 24);   -- gli 8 bit più significativi di instr
```

- Uso tipico: nomi simbolici per i bit di un registro di stato.

```vhdl
ALIAS c_flag : BIT IS flag_register(3);
ALIAS v_flag : BIT IS flag_register(2);
ALIAS n_flag : BIT IS flag_register(1);
ALIAS z_flag : BIT IS flag_register(0);
```

### Subtype · [[1-Principali elementi sintattici VHDL.pdf#page=23|p. 23]]–[[1-Principali elementi sintattici VHDL.pdf#page=24|24]]

1. Un subtype usa un sottoinsieme dei valori di un tipo: `SUBTYPE digits IS character RANGE '0' to '9';`
2. Un subtype rende constrained un array unconstrained, fissando i limiti degli indici:

```vhdl
SUBTYPE id   IS string(1 TO 20);
SUBTYPE word IS bit_vector(31 DOWNTO 0);
```

- Subtype numerici predefiniti:

```vhdl
SUBTYPE natural  IS integer RANGE 0 TO highest_integer;
SUBTYPE positive IS integer RANGE 1 TO highest_integer;
```

- Un subtype è **completamente compatibile** con il suo tipo base: `SUBTYPE compatible_nibble_bits IS BIT_VECTOR (3 DOWNTO 0);` è compatibile con `BIT_VECTOR`. Invece il **nuovo tipo** `TYPE nibble_bits IS ARRAY (3 DOWNTO 0) OF BIT;` **non** è compatibile con `BIT_VECTOR`.

### Attributi · [[1-Principali elementi sintattici VHDL.pdf#page=25|p. 25]]

- Molti oggetti VHDL (tipi enumerativi e discreti, tipi array, segnali, …) possono avere informazioni aggiuntive associate tramite **attributi**.
- Esistono molti attributi predefiniti per tipi, array e segnali; altri li può definire l'utente (raramente).
- Per descrivere i sistemi gli attributi si usano poco; utili `'event` e `'stable`. Un'applicazione molto utile è dare **direttive al sintetizzatore** (rimuovi la gerarchia, tratta come black box, …).
- Il Navabi tratta in dettaglio gli attributi dei tipi scalari, discreti, degli array e dei segnali.
- Si accede a un attributo con l'apice `'` (tick): `obj'attr` è l'attributo `attr` dell'oggetto `obj`.

#### Attributi dei range · [[1-Principali elementi sintattici VHDL.pdf#page=26|p. 26]]

```vhdl
T'left    -- limite sinistro di T
T'right   -- limite destro di T
T'low     -- limite inferiore di T (l'elemento "minore")
T'high    -- limite superiore di T

TYPE T1 IS RANGE(0 to 10);      -- ascending range
T'left = T'low = 0;
T'right = T'high = 10;

TYPE T2 IS RANGE(10 downto 0);  -- descending range
T'left = T'high = 10;
T'right = T'low = 0;
```

> ⚠️ Contraddizione: nella slide il commento di `T'left` dice «l'elemento definito più a destra» e quello di `T'right` «analogamente a sinistra»: è il contrario (`'left` è il limite scritto a sinistra nella dichiarazione). La riga `T'left = T'high = = 10` ha un `=` di troppo.

#### Attributi di un tipo enumerativo · [[1-Principali elementi sintattici VHDL.pdf#page=27|p. 27]]

```vhdl
TYPE qit IS ('0', '1', 'Z', 'X');
SUBTYPE tit IS qit RANGE '0' TO 'Z';
```

| Attributo | Descrizione | Esempio | Risultato |
|---|---|---|---|
| `'BASE` | tipo base | `tit'BASE` | `qit` |
| `'LEFT` | limite sinistro del tipo o subtype | `tit'LEFT` / `qit'LEFT` | `'0'` / `'0'` |
| `'RIGHT` | limite destro del tipo o subtype | `tit'RIGHT` / `qit'RIGHT` | `'Z'` / `'X'` |
| `'HIGH` | limite superiore del tipo o subtype | `INTEGER'HIGH` / `tit'HIGH` | grande / `'Z'` |
| `'LOW` | limite inferiore del tipo o subtype | `POSITIVE'LOW` / `qit'LOW` | `1` / `'0'` |
| `'POS(V)` | posizione del valore V nel tipo base | `qit'POS('Z')` / `tit'POS('X')` | `2` / `3` |
| `'VAL(P)` | valore alla posizione P nel tipo base | `qit'VAL(3)` / `tit'VAL(3)` | `'X'` / `'X'` |
| `'SUCC(V)` | valore dopo V nel tipo base | `tit'SUCC('Z')` | `'X'` |
| `'PRED(V)` | valore prima di V nel tipo base | `tit'PRED('1')` | `'0'` |
| `'LEFTOF(V)` | valore a sinistra di V nel tipo base | `tit'LEFTOF('1')` / `tit'LEFTOF('0')` | `'0'` / errore |
| `'RIGHTOF(V)` | valore a destra di V nel tipo base | `tit'RIGHTOF('1')` / `tit'RIGHTOF('Z')` | `'Z'` / `'X'` |

#### Attributi degli array · [[1-Principali elementi sintattici VHDL.pdf#page=28|p. 28]]

```vhdl
TYPE qit_4by8 IS ARRAY (3 DOWNTO 0, 0 TO 7) OF qit;
SIGNAL sq_4_8 : qit_4by8;
```

| Attributo | Descrizione | Esempio | Risultato |
|---|---|---|---|
| `'LEFT` | limite sinistro | `sq_4_8'LEFT(1)` | 3 |
| `'RIGHT` | limite destro | `sq_4_8'RIGHT` / `sq_4_8'RIGHT(2)` | 0 / 7 |
| `'HIGH` | limite superiore | `sq_4_8'HIGH(2)` | 7 |
| `'LOW` | limite inferiore | `sq_4_8'LOW(2)` | 0 |
| `'RANGE` | range | `sq_4_8'RANGE(2)` / `sq_4_8'RANGE(1)` | `0 TO 7` / `3 DOWNTO 0` |
| `'REVERSE_RANGE` | range rovesciato | `sq_4_8'REVERSE_RANGE(2)` / `sq_4_8'REVERSE_RANGE(1)` | `7 DOWNTO 0` / `0 TO 3` |
| `'LENGTH` | lunghezza | `sq_4_8'LENGTH` | 4 |

Il numero tra parentesi è la dimensione dell'array (senza numero si intende la prima). Nella slide `'LOW(2)` è scritto `'LOWS(2)`.

#### Attributi dei segnali · [[1-Principali elementi sintattici VHDL.pdf#page=29|p. 29]]–[[1-Principali elementi sintattici VHDL.pdf#page=31|31]]

Per `SIGNAL s1 : BIT;` (colonna T/E: **EV** = basato sugli eventi, **TR** = basato sulle transazioni; «Kind» dice se l'attributo è un segnale o un valore):

| Attributo | T/E | Esempio | Kind | Tipo | Descrizione |
|---|---|---|---|---|---|
| `'DELAYED` | – | `s1'DELAYED(5 NS)` | SIGNAL | come s1 | copia di s1 ritardata di 5 ns; senza parametro o con 0, ritardata di un delta. Equivale a un ritardo TRANSPORT di s1 |
| `'STABLE` | EV | `s1'STABLE(5 NS)` | SIGNAL | BOOLEAN | TRUE se s1 non è cambiato negli ultimi 5 ns; senza parametro o con 0, TRUE se s1 non è cambiato nel tempo di simulazione corrente |
| `'EVENT` | EV | `s1'EVENT` | valore | BOOLEAN | TRUE per il ciclo di simulazione (delta) in cui s1 cambia |
| `'LAST_EVENT` | EV | `s1'LAST_EVENT` | valore | TIME | tempo trascorso dall'ultimo cambio di valore di s1; 0 se `s1'EVENT` è TRUE |
| `'LAST_VALUE` | EV | `s1'LAST_VALUE` | valore | come s1 | valore di s1 prima dell'evento più recente |
| `'QUIET` | TR | `s1'QUIET(5 NS)` | SIGNAL | BOOLEAN | TRUE se su s1 non c'è stata nessuna transazione negli ultimi 5 ns; senza parametro o con 0, nel ciclo di simulazione corrente |
| `'ACTIVE` | TR | `s1'ACTIVE` | valore | BOOLEAN | TRUE per il ciclo di simulazione in cui s1 ha avuto una transazione |
| `'LAST_ACTIVE` | TR | `s1'LAST_ACTIVE` | valore | TIME | tempo trascorso dall'ultima transazione su s1; 0 se `s1'ACTIVE` è TRUE |
| `'TRANSACTION` | TR | `s1'TRANSACTION` | SIGNAL | BIT | segnale che commuta a ogni transazione su s1 |

![[vhdl-1-p31-attributi-segnale-forme-d-onda.png]]
*Un esempio con un segnale: transazioni su s1 a 15, 30, 45 e 60 ns (riquadri grigi), di cui solo quelle a 30 ns (0→1) e 45 ns (1→0) cambiano il valore, cioè sono eventi. Sotto, l'andamento di ciascun attributo.*

#### Esempio: fronte di discesa del clock · [[1-Principali elementi sintattici VHDL.pdf#page=32|p. 32]]

- Uso tipico degli attributi dei segnali: riconoscere il fronte attivo di un clock. Flip-flop D attivo sul fronte di discesa:

```vhdl
ENTITY brief_d_flip_flop IS
  PORT (d, c : IN BIT; q : OUT BIT);
END brief_d_flip_flop;
--
ARCHITECTURE falling_edge OF brief_d_flip_flop IS
  SIGNAL tmp : BIT;
BEGIN
  tmp <= d WHEN (c = '0' AND NOT c'STABLE) ELSE tmp;
  q <= tmp AFTER 8 NS;
END falling_edge;
```

### Operatori · [[1-Principali elementi sintattici VHDL.pdf#page=33|p. 33]]

Classi di operatori, in ordine di priorità (le parentesi cambiano l'ordine):

| Classe | Operatori |
|---|---|
| vari | `**` `abs` `not` |
| moltiplicativi | `*` `/` `mod` `rem` |
| di segno | `+` `-` |
| di addizione | `+` `-` `&` |
| di shift | `sll` `srl` `sla` `sra` `rol` `ror` |
| relazionali | `=` `/=` `<` `<=` `>` `>=` |
| logici | `and` `or` `nand` `nor` `xor` `xnor` |

#### Operatori vari e moltiplicativi · [[1-Principali elementi sintattici VHDL.pdf#page=34|p. 34]]–[[1-Principali elementi sintattici VHDL.pdf#page=35|35]]

- `**` esponenziazione, `ABS` valore assoluto; `*` moltiplicazione, `/` divisione, `mod` modulo, `rem` resto.

```vhdl
VARIABLE A,B,C : Integer;
A := 2; B := 8;
C := A ** B;      -- C = 2 ** 8 = 256
A := 4; B := -2;
C := A ** B;      -- C = 4 ** (-2) = 1 / (4**2) = 0.0625
A := -14;
C := ABS (A);     -- C = 14

VARIABLE X,Y,Z : Real;
A := 2; B := 8;
C := A * B;       -- C = 2 * 8 = 16
X := 4; Y := -8;
Z := X / Y;       -- Z = 4 / (-8) = -0.5
A := 9; B := 7;
C := A MOD B;     -- C = 9 mod 7 = 2
```

> ⚠️ Contraddizione: con `C` di tipo `Integer` il risultato 0.0625 non è rappresentabile: per gli interi l'esponente deve essere non negativo; il valore 0.0625 si ottiene con una base reale (`4.0 ** (-2)`). Allo stesso modo, con `X` e `Y` di tipo `Real` si scrive `X := 4.0; Y := -8.0;`.

#### Operatori di addizione · [[1-Principali elementi sintattici VHDL.pdf#page=36|p. 36]]

- `+` addizione, `-` sottrazione, `&` concatenamento.

```vhdl
VARIABLE A,B,C : Integer;
A := 2; B := 8;
C := A + B;       -- C = 2 + 8 = 10

SIGNAL sq4 : std_logic_vector(3 DOWNTO 0);
SIGNAL sq8 : std_logic_vector(7 DOWNTO 0);
sq4 <= sq8(2) & sq8(3) & sq8(4) & sq8(5);
```

#### Operatori di shift · [[1-Principali elementi sintattici VHDL.pdf#page=37|p. 37]]

- `sll` shift left logical, `srl` shift right logical, `sla` shift left arithmetic, `sra` shift right arithmetic, `rol` rotate left logical, `ror` rotate right logical.

```vhdl
variable A, C : BIT_VECTOR(3 downto 0);
A := ('1','0','1','1');
C := A sll 1;     -- ('0','1','1','0')
C := A sll 3;     -- ('1','0','0','0')
C := A sla 1;     -- ('0','1','1','1')
C := A sla 3;     -- ('1','1','1','1')
C := A rol 1;     -- ('0','1','1','1')
C := A rol 2;     -- ('1','1','0','1')
```

> ⚠️ Contraddizione: `1011 rol 2` dà `1110`, non `1101` (`1101` è `1011 ror 1`).

#### Operatori relazionali · [[1-Principali elementi sintattici VHDL.pdf#page=38|p. 38]]

- `=` uguaglianza, `/=` diseguaglianza, `<` minore, `<=` minore o uguale, `>` maggiore, `>=` maggiore o uguale.

```vhdl
variable A : REAL := 100.0;
variable B : BIT_VECTOR(7 downto 0) := ('0','0','0','0','0','0','0','0');
variable C, D : BIT_VECTOR(1 to 0);
A /= 342.54                                   -- True
A = 100.0                                     -- True
B /= ('1','0','0','0','0','0','0','0')        -- True
C = D                                         -- True
A > 42.54                                     -- True
A >= 100.0                                    -- True
B < ('1','0','0','0','0','0','0','0')         -- True
C <= B                                        -- True
```

#### Operatori logici · [[1-Principali elementi sintattici VHDL.pdf#page=39|p. 39]]

- `and`, `or`, `nand`, `nor`, `xor`, `xnor`, `not`.

```vhdl
variable A, B, C, D, Y : BIT := '1';
Y := (A AND (B XNOR C)) NOR D;
```

*Approfondimenti nel wiki: [[elementi-lessicali-vhdl]], [[oggetti-vhdl]], [[tipi-vhdl]], [[std-logic]], [[signed-unsigned]], [[array-vhdl]], [[record-vhdl]], [[alias-vhdl]], [[subtype-vhdl]], [[attributi-vhdl]], [[operatori-vhdl]]*

## Lezione 2 — VHDL: descrizione Dataflow

*Fonte: 2-Descrizione Dataflow.pdf, 12 pagine (slide «VHDL Dataflow», v1.2).*

### Roadmap · [[2-Descrizione Dataflow.pdf#page=1|p. 1]]

Come si descrive in VHDL la struttura di un sistema digitale con una descrizione di tipo **data-flow**: espressioni e operatori, assegnazione concorrente, assegnazione condizionata, assegnazione selezionata, esempi.

> ⚠️ Contraddizione: nell'outline della slide «assegnazione concorrente» compare due volte; la quarta voce è l'assegnazione selezionata.

### Espressioni e operatori · [[2-Descrizione Dataflow.pdf#page=2|p. 2]]–[[2-Descrizione Dataflow.pdf#page=3|3]]

- A un segnale, a una variabile o a una costante si può associare il risultato di un'**espressione** che coinvolge altri valori; **non si possono mischiare segnali e variabili**.
- Un'espressione combina operandi (valori di segnali, costanti, variabili) tramite operatori, come negli altri linguaggi di programmazione.
- Operatori predefiniti in ordine di priorità decrescente (le parentesi cambiano l'ordine di valutazione):

| Priorità | Operatori |
|---|---|
| più alta | `**` `abs` `not` |
| | `*` `/` `mod` `rem` |
| | `+` `-` (segno) |
| | `+` `-` `&` |
| | `=` `/=` `<` `<=` `>` `>=` |
| più bassa | `and` `or` `nand` `nor` `xor` |

- **Relazionali** (`=`, `/=` diverso, `<`, `<=`, `>`, `>=`): si applicano a elementi dello **stesso tipo** e producono un `boolean`.
- **Aritmetici** (`**` elevamento a potenza, `abs`, `*`, `/`, `mod`, `rem` resto, `+`, `-`): solo sui tipi numerici (integer, floating point, physical); danno un valore dello stesso tipo (oppure overflow e underflow).
- **Logici** (`and`, `or`, `nand`, `nor`, `xor`, `not`): su `bit`, `std_logic` e `boolean`, ma anche su `bit_vector` e `std_logic_vector` (**word gate**).
- `&` concatena più oggetti ottenendo un array.
- L'utente può definire nuovi operatori e fare **overloading** di quelli esistenti.

### Assegnazione concorrente · [[2-Descrizione Dataflow.pdf#page=4|p. 4]]–[[2-Descrizione Dataflow.pdf#page=5|5]]

- Le assegnazioni di segnale **concorrenti** stanno nel corpo di un'`architecture`; quelle nel corpo di un `process` si chiamano **sequenziali**.
- Un'assegnazione concorrente si **attiva ogni volta che varia uno dei segnali da cui dipende** il segnale assegnato:

```vhdl
S <= NOT ((A XOR B) AND C);
```

- Nel corpo di un'architecture sono **concorrenti fra loro**: tutte le assegnazioni di segnale (incondizionate, condizionate, selezionate), tutte le istanziazioni di blocchi, tutti i process.
- Il **target** di un'assegnazione può essere un segnale semplice, un segnale indicizzato (`a(5)`), una slice (`a(5 downto 0)`) o un segnale aggregato (`a(5) & a(2)`). Il simbolo di assegnazione fra segnali è `<=`.

```vhdl
S <= A XOR B;
S(0) <= A(0) XOR B(0);
S(3 downto 0) <= A(3 downto 0) XOR B(3 downto 0);
S(1) & S(0) <= A(1 downto 0) XOR B(1 downto 0);
```

> ⚠️ Contraddizione: la concatenazione `S(1) & S(0)` non può fare da target; un target aggregato si scrive come aggregato: `(S(1), S(0)) <= A(1 downto 0) XOR B(1 downto 0);`.

- Tre tipi di assegnazioni concorrenti fra segnali:
  1. **incondizionata**: la waveform assegnata al segnale è fissa;
  2. **condizionata**: la waveform è scelta con un costrutto if-then-else;
  3. **selezionata**: la waveform è scelta con un costrutto di tipo case.

### Assegnazione incondizionata · [[2-Descrizione Dataflow.pdf#page=6|p. 6]]

Un'espressione che coinvolge diverse forme d'onda è semplicemente assegnata a un segnale. Esempio, un half adder:

```vhdl
ARCHITECTURE dataflow OF HalfAdder IS
BEGIN
  Sum   <= A XOR B;
  Carry <= A AND B;
END ARCHITECTURE dataflow;
```

### Assegnazione condizionata · [[2-Descrizione Dataflow.pdf#page=7|p. 7]]–[[2-Descrizione Dataflow.pdf#page=9|9]]

```vhdl
segnale <= waveform_1 WHEN condizione_1 ELSE
           waveform_2 WHEN condizione_2 ELSE
           ...
           waveform_(n-1) WHEN condizione_(n-2) ELSE
           waveform_n;
```

- Sceglie la waveform da assegnare al segnale target (fra `waveform_1` … `waveform_n`) a seconda di quale condizione booleana è verificata.
- Le condizioni possono **sovrapporsi**: in tal caso l'**ordine di valutazione** (dalla prima fino all'`ELSE` finale) è decisivo.
- Deve terminare con un `ELSE` senza condizione.

> ⚠️ Contraddizione: con `n` waveform le condizioni sono `n-1`, quindi l'ultima è `condizione_(n-1)`, non `condizione_(n-2)`.

**Buffer tristate** con segnale di abilitazione `Enable`: quando `Enable` è alto `BufOut` prende `BufIn`, altrimenti il valore tristate `'Z'`.

```vhdl
ARCHITECTURE dataflow OF TriStateBuffer IS
BEGIN
  BufOut <= BufIn WHEN Enable = '1
            ELSE 'Z';
END ARCHITECTURE dataflow;
```

> ⚠️ Contraddizione: nella slide manca l'apice di chiusura: la condizione è `Enable = '1'`.

**Multiplexer 2 a 1 su un bit con abilitazione tristate**: è un mux con ingresso di selezione `sel`, la cui uscita è l'ingresso di una tristate controllata da `en`; l'esempio contiene anche i ritardi di propagazione `Tpd`.

```vhdl
mux_out <= 'Z'  AFTER Tpd WHEN en = '0' ELSE
           in_0 AFTER Tpd WHEN sel = '0' ELSE
           in_1 AFTER Tpd;
```

- Un'assegnazione condizionata è un'**abbreviazione di un process** con assegnazioni di segnali sotto condizioni `IF … THEN`; `[sensitivity_list]` è l'insieme dei segnali da cui dipendono le clausole:

```vhdl
PROCESS
  IF condition_1 THEN
    segnale <= waveform_1;
  ELSIF condition_2 THEN
    segnale <= waveform_2;
  ELSIF ...
  ELSE
    segnale <= waveform_n;
  WAIT [sensitivity_list];
END PROCESS;
```

> ⚠️ Contraddizione: nel process della slide manca `END IF;` prima del `WAIT`.

### Assegnazione selezionata · [[2-Descrizione Dataflow.pdf#page=10|p. 10]]–[[2-Descrizione Dataflow.pdf#page=11|11]]

```vhdl
WITH segnale_di_selezione SELECT
  segnale <= waveform_1 WHEN caso_1,
             waveform_2 WHEN caso_2,
             ...
             waveform_n WHEN caso_n;
```

- Sceglie la waveform da assegnare al segnale target a seconda del **valore** (`caso_1` … `caso_n`) assunto dal segnale di selezione.
- I casi devono essere **esaustivi** (a meno di usare un caso `OTHERS`) e **mutuamente esclusivi** (non possono sovrapporsi).
- È un'abbreviazione di un process con le assegnazioni in un costrutto `CASE`; la sensitivity list del `WAIT` contiene tutti i segnali usati nelle forme d'onda e nell'espressione del segnale di selezione:

```vhdl
PROCESS
  CASE segnale_di_selezione IS
    WHEN caso_1 => s <= waveform_1;
    WHEN caso_2 => s <= waveform_2;
    ...
    WHEN caso_n => s <= waveform_n;
  END CASE;
  WAIT [ sensitivity_list ];
END PROCESS;
```

> ⚠️ Contraddizione: la slide scrive «una assegnazione condizionata è un'abbreviazione per un processo … CASE»: si tratta dell'assegnazione **selezionata**. Nel process equivalente il target `s` è il `segnale` dell'assegnazione.

### Confronto fra assegnazioni · [[2-Descrizione Dataflow.pdf#page=12|p. 12]]

| | Condizionata (`WHEN … ELSE`) | Selezionata (`WITH … SELECT`) |
|---|---|---|
| casi | non mutuamente esclusivi | mutuamente esclusivi |
| valutazione | sequenziale: la prima condizione vera determina l'assegnazione | nessun ordine di scansione, confronti «in parallelo» |

- Se tutti i casi di un'assegnazione condizionata sono mutuamente esclusivi, il costrutto è equivalente a un'assegnazione selezionata.

*Approfondimenti nel wiki: [[descrizione-dataflow]], [[assegnazione-concorrente]], [[assegnazione-condizionata]], [[assegnazione-selezionata]], [[operatori-vhdl]], [[half-adder]], [[buffer-tristate]], [[multiplexer]]*

## Lezione 3 — VHDL: descrizione strutturale

*Fonte: 3-Descrizione Strutturale.pdf, 31 pagine (slide «VHDL Strutturale», v1.1).*

### Roadmap · [[3-Descrizione Strutturale.pdf#page=1|p. 1]]

Descrizione di un design digitale: entity e architecture, binding di architecture ed entity, istanziazione di componenti, parametrizzazione del design con i generics, assegnazione concorrente, costrutti generate.

### Entity e architecture · [[3-Descrizione Strutturale.pdf#page=2|p. 2]]

- Un sistema digitale si progetta come un insieme di **moduli organizzati gerarchicamente in un albero**: un modulo più esterno (**top-level module**, la radice) istanzia e collega altri moduli, che a loro volta ne istanziano altri, fino a moduli «elementari» (atomici).
- Ogni modulo (design entity, design module) ha un insieme di terminali di I/O (**ports**) che formano la sua interfaccia con il mondo.
- In VHDL un modulo può essere usato come **componente** o come **top-level module** del design.
- Ogni modulo è descritto da due parti:
  - una **entity**: l'interfaccia del modulo (segnali di ingresso/uscita e altri parametri, i generics);
  - una **architecture**: il funzionamento del sistema, cioè il legame fra i pin di ingresso e di uscita.

### Entity · [[3-Descrizione Strutturale.pdf#page=3|p. 3]]–[[3-Descrizione Strutturale.pdf#page=5|5]]

- La dichiarazione di entity dichiara gli «oggetti» (segnali di I/O ed eventuali generics) usabili nell'implementazione:
  - specifica il componente in termini dei suoi **port**: nome, tipo e direzione (**mode**);
  - può specificare **costanti** (i generics) che controllano struttura e comportamento dell'entity.

```vhdl
ENTITY component_name
  dichiarazione del nome, del tipo e del modo di tutti i porti
  (opzionale) dichiarazione del nome, del tipo e del valore dei generics
END component_name;
```

- La dichiarazione di entity è la **parte formale**: specifica tipi e modi dei port (e dei generics). I segnali effettivamente collegati (e il valore attuale dei generics) si specificano **all'istanziazione**: lì si stabilisce la corrispondenza fra port e segnali, e i segnali sono i **parametri effettivi**.
- Dentro l'architecture si usano i nomi dei port per riferirsi ai segnali che verranno collegati.
- **Significato hardware**: istanziare un modulo e specificarne i collegamenti equivale a usare un componente (ad es. un integrato della serie 74) e collegarne i piedini con dei fili (segnali), collegando così più componenti fra loro.

```vhdl
ENTITY nome_entita IS
  PORT (
    nome_segnale_1 : modo_segnale_1 tipo_segnale_1;
    nome_segnale_2 : modo_segnale_2 tipo_segnale_2;
    ...
    nome_segnale_N : modo_segnale_N tipo_segnale_N;
    nome_generic_1 : tipo_generic_1 [:= valore_generic_1];
    ...
    nome_generic_M : tipo_generic_M [:= valore_generic_M] );
END nome_entita;

ENTITY nome_entita IS
  PORT (
    nome_segnale_1 : modo_segnale_1 tipo_segnale_1;
    nome_segnale_2 : modo_segnale_2 tipo_segnale_2;
    ...
    nome_segnale_N : modo_segnale_N tipo_segnale_N;
  );
END nome_entita;
```

- Il nome dell'entity è `nome_entita`; per ogni port i = 1…N: `nome_segnale_i` è il nome dell'i-esimo segnale, `modo_i` il modo di interazione con l'esterno (`IN`, `OUT`, `INOUT`, `BUFFER`), `tipo_segnale_i` il tipo, cioè l'insieme dei valori che il segnale può assumere in ogni istante (analogo al tipo di una variabile software).

> ⚠️ Contraddizione: nel primo schema i generics compaiono dentro `PORT (…)`: vanno dichiarati in una clausola `GENERIC (…);` separata, prima di `PORT` (come nell'esempio della ROM). Nel secondo schema l'ultimo port non deve terminare con `;` prima della `)`.

### Port · [[3-Descrizione Strutturale.pdf#page=6|p. 6]]–[[3-Descrizione Strutturale.pdf#page=7|7]]

- Ogni port ha un **nome**, un **tipo** e un **modo**.
- Il tipo è l'insieme di valori che qualunque segnale connesso al port può assumere: se un port è `std_logic`, tutti i segnali collegati devono essere `std_logic`.
- A un port si possono collegare **solo segnali**, di tipo compatibile con quello del port (il VHDL è strong-typed).
- Il **modo** fissa la direzione in cui i dati passano fra modulo e mondo esterno. Quattro modi:
  - **IN**: il port è solo un ingresso; il circuito che lo pilota (driver) è esterno all'entità;
  - **OUT**: il port è un'uscita e il driver è interno; il valore di un pin `OUT` **non può essere letto** dentro l'entità;
  - **BUFFER**: port di uscita il cui valore **può anche essere letto** dentro l'entità;
  - **INOUT**: il segnale si usa sia come ingresso sia come uscita (ad es. un bus dati bidirezionale).
- È consigliabile usare `inout` solo nella top-level entity e **non usare** il modo `buffer`.

```vhdl
ENTITY nome_entita IS PORT (
  A : IN bit;
  B : IN bit_vector(0 to 3);
  Z : OUT bit );
```

![[vhdl-3-p7-modi-dei-port.png]]
*I modi dei port: con `out` il valore riletto all'interno passa da un segnale interno (`W_OUTPUT`); con `buffer` si rilegge direttamente l'uscita (`OUTPUT`); `inout` (`BIDIR`) è un terminale bidirezionale.*

### Generics · [[3-Descrizione Strutturale.pdf#page=8|p. 8]]–[[3-Descrizione Strutturale.pdf#page=9|9]]

- I generics si specificano nell'interfaccia di un'entity e **parametrizzano la descrizione**: rispetto al numero di bit di ingressi e uscite, esplicitando caratteristiche del timing (tempi di propagazione, …), definendo parametri fisici del modulo (capacità dei nodi di ingresso o uscita, dipendenza dalla temperatura, …).
- Il valore di un generic va specificato in almeno uno di questi modi:
  1. come **valore di default** nella dichiarazione di entity (sempre raccomandato, per assicurare che il componente sia sintetizzabile e simulabile);
  2. nella **dichiarazione del component**;
  3. nell'**istanziazione del component**.
- Se se ne usano più d'uno vale quello a **priorità maggiore**: il caso 3 sovrascrive gli altri, e così via.
- Come generics si possono usare solo quantità **costanti** (classe constant) o **espressioni statiche** (che coinvolgono solo costanti).
- Esempio: una **ROM** come classe di entity che differiscono nei parametri della struttura; due generics fissano i bit del data bus e dell'address bus, e la ROM memorizza $2^{depth}$ word di `width` bit.

```vhdl
ENTITY rom IS
  GENERIC( width : positive := 32;
           depth : positive := 4);
  PORT(
    enable  : IN std_logic;
    address : IN std_logic_vector(depth-1 downto 0);
    data    : OUT std_logic_vector(width-1 downto 0) );
END rom;
```

- Se non c'è un valore di default, i valori effettivi vanno dati nella dichiarazione o nell'istanziazione: alla fine i generics **devono essere risolti**.

### Architecture · [[3-Descrizione Strutturale.pdf#page=10|p. 10]]–[[3-Descrizione Strutturale.pdf#page=12|12]]

- L'interfaccia definisce come il modulo interagisce con il mondo esterno; un'architecture descrive **una particolare implementazione** del modulo.
- Per una stessa interfaccia possono esistere **più architecture**: ognuna descrive lo stesso modulo da punti di vista (livelli di astrazione) o livelli di dettaglio diversi; all'istanziazione bisogna allora scegliere il **binding**.
- Un'architecture ha due parti: una **parte dichiarativa**, dove si definiscono gli oggetti usati nella descrizione (tipi, segnali, costanti, component, …), e un **corpo** (architecture body), la descrizione vera e propria, che usa i segnali e i generics dell'interfaccia e gli oggetti dichiarati.

```vhdl
ARCHITECTURE identifier OF entity_name IS
  dichiarazioni iniziali                          -- parte dichiarativa
BEGIN
  Specifica del componente in funzione degli
  ingressi, dei parametri fisici e degli altri parametri.   -- architecture body
END identifier;

ARCHITECTURE nome_architettura OF nome_entita IS
  dichiarazioni dei tipi usati
  definizione delle costanti
  dichiarazioni dei segnali interni al modulo
  definizione di funzioni o procedure
  dichiarazioni dei componenti
  specificazione della configurazione dei componenti (binding)
BEGIN
  statement concorrente
  ...
  statement concorrente
END nome_architettura;
```

#### Parte dichiarativa: tipi, segnali e costanti · [[3-Descrizione Strutturale.pdf#page=13|p. 13]]

```vhdl
TYPE nome_tipo : definizione_tipo;                           -- dichiarazione di tipo
CONSTANT nome_costante : tipo_costante := valore_costante;   -- dichiarazione di costante
SIGNAL nome_segnale : tipo_segnale [:= valore_iniziale];      -- dichiarazione di segnali
```

- Tutte le dichiarazioni sono **locali al modulo**.
- Tipi e costanti rendono la descrizione più leggibile e manutenibile.
- I segnali «istanziano» dei **fili** che collegano fra loro i blocchi logici dell'architecture body, comunque siano descritti (assegnazioni, istanziazione di blocchi, process, …).

```vhdl
TYPE std_ulogic IS ( U , X , 0 , -- indefinito, pi  driver, 0 logico,
     1 , Z , W , L , H , - );    -- 1 logico, weak X, 0, 1, don t care
CONSTANT t_clock : time := 10ns;
SIGNAL in0 : std_ulogic :=  1 ;
SIGANL in1 : bit;
```

> ⚠️ Contraddizione: nel codice della slide mancano gli apici (`'U', 'X', '0', …`, `:= '1'`), la dichiarazione di tipo si scrive `TYPE nome_tipo IS definizione_tipo;` e `SIGANL` sta per `SIGNAL`. Il commento «pi driver» è «più driver»: `'X'` indica un conflitto fra più driver.

#### Parte dichiarativa: component e binding · [[3-Descrizione Strutturale.pdf#page=14|p. 14]]

- Le **dichiarazioni di componenti** definiscono le interfacce delle design entity usate; le **specificazioni di configurazione** fissano, per ogni istanza di un component, quale architecture usare.
- La dichiarazione di un component è simile alla definizione di un'entity: stesse informazioni per i segnali (nome, modo, tipo) e per i generics (nome, tipo, valore).

```vhdl
COMPONENT nome_componente PORT (dichiarazione dei porti)
  GENERIC (dichiarazione dei generics);                  -- dichiarazioni di componenti
FOR ALL | elenco di label : nome_componente
  USE ENTITY nome_libreria.nome_entity(nome_architecture);   -- specificazione della configurazione

COMPONENT n1 PORT (i1: IN BIT;
                   o1: OUT BIT);
END COMPONENT;
FOR ALL : n1 USE ENTITY WORK.inv (single_delay);
```

### Binding · [[3-Descrizione Strutturale.pdf#page=15|p. 15]]–[[3-Descrizione Strutturale.pdf#page=17|17]]

- Un'architecture può usare entità descritte separatamente e disponibili nella libreria corrente (`work`) o in altre librerie (design libraries).
- L'architecture deve dichiarare un **component**: un «prototipo» del blocco da istanziare, un **blocco virtuale**, che prima di essere istanziato va mappato su un blocco specifico per definirne il comportamento ingresso-uscita.
- La component declaration specifica i port (ed eventualmente i generics), ma **non** quale architecture body verrà istanziato.
- Nella parte dichiarativa (prima di `BEGIN`) ci sono la **component declaration** (interfaccia del componente da istanziare) e la **configuration specification** (il binding: quale architecture si usa nelle varie istanze; poco usata).
- Nella statement part (dopo `BEGIN`) ci sono le **istanziazioni** dei componenti (il binding si può fare anche lì).

```vhdl
ARCHITECTURE nome_architettura OF nome_entita IS
  dichiarazioni di componenti
  binding dei component con le architectures
BEGIN
  statement concorrente
  instanziazione dei componenti
END nome_architettura;

ARCHITECTURE nome_architettura OF nome_entita IS
  COMPONENT n1 PORT (i1: IN BIT; o1: OUT BIT); END COMPONENT;
  COMPONENT n2 PORT (i1, i2: IN BIT; o1: OUT BIT); END COMPONENT;
  FOR ALL : n1 USE ENTITY WORK.inv (single_delay);
  FOR ALL : n2 USE ENTITY WORK.nand2 (single_delay);
BEGIN
```

### Architecture body · [[3-Descrizione Strutturale.pdf#page=18|p. 18]]

- Il corpo dell'architecture è composto da **statement concorrenti** (istanziazione di un componente, assegnazione di un segnale, definizione di un process, …).
- Nel corpo i port si usano come segnali, rispettandone il modo: un `IN` si può solo leggere, un `OUT` si può solo scrivere. Un segnale è **scritto** se sta a sinistra di un'assegnazione.

### Istanziazione di un componente · [[3-Descrizione Strutturale.pdf#page=19|p. 19]]–[[3-Descrizione Strutturale.pdf#page=22|22]]

- L'istanziazione è uno **statement concorrente**, sempre «attivo»: quando c'è un evento su un port di ingresso, il componente si attiva e reagisce secondo il suo comportamento I/O, generando eventi sulle uscite.
- Segnali e costanti si assegnano a port e generics **ordinatamente** secondo la definizione (**associazione posizionale**) o con un'**associazione esplicita per nome** (**nominale**).
- Ogni istanza richiede una **label** diversa: la label è il nome del blocco logico e distingue le istanze della stessa entity.
- Con l'associazione nominale l'ordine è ininfluente; con quella posizionale bisogna rispettare l'ordine di dichiarazione dei port.

```vhdl
nome_label: nome_componente
  PORT MAP (segnale_1, segnale_2, ..., segnale_N)
  GENERIC MAP (valore_1, valore_2, ..., valore_M);            -- istanziazione con assegnazione posizionale

nome_label: nome_componente
  PORT MAP (nome_segnale_1 => segnale_1, ..., nome_segnale_N => segnale_N)
  GENERIC MAP (nome_generic_1 := valore_1, ..., nome_generic_M := valore_M);   -- istanziazione con assegnazione nominale
```

> ⚠️ Contraddizione: `GENERIC MAP` va scritto **prima** di `PORT MAP` (come nell'esempio della ROM qui sotto) e l'associazione per nome usa `=>` anche nel `GENERIC MAP`, non `:=`. Lo stesso vale per la component declaration, dove `GENERIC (…)` precede `PORT (…)`.

#### Esempio con generics · [[3-Descrizione Strutturale.pdf#page=21|p. 21]]

```vhdl
COMPONENT rom
  GENERIC (width : positive := 8;
           depth : positive := 4);
  PORT (
    enable  : IN std_logic;
    address : IN std_logic_vector(depth-1 downto 0);
    data    : OUT std_logic_vector(width-1 downto 0) );
END COMPONENT;

rom_0 : rom GENERIC MAP (16, 4) PORT MAP ( );                       -- rom di 16 word di 16 bit
rom_1 : rom PORT MAP ( );                                           -- rom di 16 word di 8 bit
rom_2 : rom GENERIC MAP (depth => 5, width => 32) PORT MAP ( );     -- rom di 32 word di 32 bit
```

- In `rom_0` il valore 16 sovrascrive `width = 8` della dichiarazione del component, che a sua volta aveva sovrascritto il default `width = 32` dell'entity.

#### Altri esempi di istanziazione · [[3-Descrizione Strutturale.pdf#page=22|p. 22]]

```vhdl
COMPONENT n1 PORT (i1: IN BIT; o1: OUT BIT); END COMPONENT;
COMPONENT n2 PORT (i1, i2: IN BIT; o1: OUT BIT); END COMPONENT;
FOR ALL : n1 USE ENTITY WORK.inv(single_delay);
FOR ALL : n2 USE ENTITY WORK.nand2 (single_delay);
BEGIN
  g0 : n1 PORT MAP (a, im1);                          -- associazione posizionale
  g1 : n1 PORT MAP (i1 => b, o1 => im2);              -- nominale nello stesso ordine
  g2 : n2 PORT MAP (o1 => im3, i2 => im2, i1 => a);   -- nominale in ordine diverso
  g3 : n2 PORT MAP (a, gt, im4);                      -- associazione posizionale
```

### Assegnazione di un segnale · [[3-Descrizione Strutturale.pdf#page=23|p. 23]]–[[3-Descrizione Strutturale.pdf#page=25|25]]

- Come l'istanziazione, anche un'assegnazione di segnale è uno statement concorrente, sempre «attivo». Quando c'è un evento su uno dei segnali a destra:
  1. si calcola il valore del segnale a sinistra secondo l'espressione;
  2. si **schedula una transazione** sul segnale di uscita secondo il timing dell'assegnazione.

```vhdl
-- Descrizione Data-Flow di una porta complessa AOI
LIBRARY ieee;
USE ieee.std_logic_1164.ALL;
ENTITY AOI IS PORT (
  i1 : IN std_logic;
  i2 : IN std_logic;
  i3 : IN std_logic;
  O1 : OUT std_logic );
--
ARCHITECTURE dataflow OF AOI IS
BEGIN
  o1 <= NOT(i1 AND i2 OR i3) AFTER 3ns;
END dataflow;
```

> ⚠️ Contraddizione: manca `END AOI;` alla fine dell'entity, e `i1 AND i2 OR i3` va scritto con le parentesi, `(i1 AND i2) OR i3`: in VHDL operatori logici diversi non si mescolano senza parentesi.

- Qual è la differenza fra le due architetture seguenti?

```vhdl
ENTITY porta_complessa IS
  PORT ( a, b, c : IN std_logic;
         z : OUT std_logic);
END porta_complessa ;
--
ARCHITECTURE concurrent OF porta_complessa IS
  SIGNAL w, x, y : std_logic ;
BEGIN
  w <= NOT a AFTER 12 NS;
  x <= a AND b AFTER 12 NS;
  y <= c AND w AFTER 12 NS;
  z <= x OR y AFTER 12 NS;
END concurrent;
---
ARCHITECTURE single_assignment OF porta_complessa IS
BEGIN
  z <= (a AND b) or (c AND (NOT a)) AFTER 36 NS;
END single_assignment;
```

- Le due architetture hanno lo **stesso comportamento funzionale** (la stessa funzione booleana) ma **tempificazioni diverse**: una variazione di `c` produce un'(eventuale) variazione di `z` dopo **24 ns** nella prima architettura e dopo **36 ns** nella seconda.

![[vhdl-3-p25-porta-complessa-forme-d-onda.png]]
*Architettura `concurrent`: `a` scende a 0 ns con `b = c = 1`; `w` sale e `x` scende a 12 ns, `y` sale a 24 ns; `z` scende a 24 ns e torna alto a 36 ns.*

### Costrutti iterativi: generate · [[3-Descrizione Strutturale.pdf#page=26|p. 26]]–[[3-Descrizione Strutturale.pdf#page=27|27]]

- Spesso un blocco logico è composto da un solo blocco più semplice istanziato molte volte (un sommatore carry-ripple, una porta logica che opera su word, …). Il costrutto **generate** istanzia iterativamente un insieme di blocchi, con un `FOR` o con un `IF`:

```vhdl
label : FOR identifier IN range GENERATE
  concurrent_statements;
END GENERATE [label];

label : IF (boolean_expression) GENERATE
  concurrent_statements;
END GENERATE [label];
```

- In un generate si può includere **qualsiasi statement concorrente**. Non si possono usare `ELSE` o `ELSIF` con il generate prima del VHDL 2008.
- Un **nibble comparator** segnala se il numero rappresentato da una stringa `a` di 4 bit (nibble) è maggiore, minore o uguale a quello rappresentato da una stringa `b`. Interfaccia (nel PDF, sotto il riquadro del codice):

```vhdl
LIBRARY ieee;
USE ieee.std_logic_1164.ALL;
ENTITY nibble_comparator IS
  PORT ( a, b : IN std_logic_vector(3 DOWNTO 0);    -- a and b data inputs
         gt, eq, lt : IN std_logic;                 -- previous greater, equal, less than
         a_gt_b,                                    -- a > b
         a_eq_b,                                    -- a = b
         a_lt_b : OUT std_logic);                   -- a < b
END nibble_comparator;
```

- Esempio di `FOR … GENERATE`: 8 porte AND, una per bit.

```vhdl
ARCHITECTURE test OF test IS
  COMPONENT and02 PORT(
    a0 : IN std_logic;
    a1 : IN std_logic;
    y  : OUT std_logic);
  END COMPONENT and02;
BEGIN
  G1 : FOR n IN 7 DOWNTO 0 GENERATE
    and_gate:and02 PORT MAP( a0 => sig1(n), a1 => sig2(n), y => z(n));
  END GENERATE G1;
END test;
```

![[vhdl-3-p27-for-generate-and.png]]
*Le 8 istanze di `and02` generate dal ciclo: il bit n di `sig1` e di `sig2` entra nella n-esima porta, la cui uscita va nel bit n del bus d'uscita (chiamato `z` nel codice e `sig3` nella figura).*

### Testbench · [[3-Descrizione Strutturale.pdf#page=28|p. 28]]–[[3-Descrizione Strutturale.pdf#page=31|31]]

- Per verificare funzionamento e tempificazione di un progetto VHDL si usano i **testbench**. Un testbench è una design unit che:
  - dichiara e istanzia il blocco da testare (**design under test, DUT**);
  - applica una sequenza opportuna di **stimoli**;
  - **verifica** che le uscite siano corrette secondo le specifiche.
- È un'entità **senza ingressi né uscite**, perché nessun altro blocco la istanzia.
- Il testbench più semplice applica la sequenza degli ingressi senza verificarne l'esattezza: le uscite le controlla l'utente.

![[vhdl-3-p28-testbench-nibble-comparator.png]]
*Il testbench `test_bench (input_output)`: generatori di forme d'onda su `a(3:0)` e `b(3:0)`, ingressi di cascata `gt`, `eq`, `lt` fissati, uscite `a_gt_b`, `a_eq_b`, `a_lt_b` osservate.*

```vhdl
LIBRARY ieee;
USE ieee.std_logic_1164.ALL;
--
ENTITY nibble_comparator_tb IS
END nibble_comparator;
--
ARCHITECTURE input_output OF nibble_comparator_test_bench IS
  COMPONENT comp4 PORT (a, b : IN std_logic_vector (3 DOWNTO 0);
    a_gt_b, a_eq_b, a_lt_b : IN std_logic;
    a_gt_b_out, a_eq_b_out, a_lt_b_out : OUT std_logic);
  END COMPONENT;
  FOR a1 : comp4 USE ENTITY WORK.nibble_comparator(iterative);
  SIGNAL a, b : std_logic_vector (3 DOWNTO 0);
  SIGNAL eql, lss, gtr, gnd : std_logic;
  SIGNAL vdd : std_logic := '1';
BEGIN
  -- istanziazione del DUT
  a1: comp4 PORT MAP (a, b, gnd, vdd, gnd, gtr, eql, lss);
  -- applicazione dei segnali su a2
  a2: a <= "0000",                 -- a = b (steady state)
           "1111" AFTER 0500 NS,   -- a > b (worst case)
           "1110" AFTER 1500 NS,   -- a < b (worst case)
           "1110" AFTER 2500 NS,   -- a > b (need bit 1 info)
           "1010" AFTER 3500 NS,   -- a < b (need bit 2 info)
           "0000" AFTER 4000 NS,   -- a < b (steady state, prepare for next)
           "1111" AFTER 4500 NS,   -- a = b (worst case)
           "0000" AFTER 5000 NS,   -- a < b (need bit 3 only, best case)
           "0000" AFTER 5500 NS,   -- a = b (worst case)
           "1111" AFTER 6000 NS;   -- a > b (need bit 3 only, best case)
  -- applicazione dei segnali su a3
  a3 : b <= "0000",                -- a = b (steady state)
            "1110" AFTER 0500 NS,  -- a > b (worst case)
            "1111" AFTER 1500 NS,  -- a < b (worst case)
            "1100" AFTER 2500 NS,  -- a > b (need bit 1 info)
            "1100" AFTER 3500 NS,  -- a < b (need bit 2 info)
            "1111" AFTER 4000 NS,  -- a < b (steady state, prepare for next)
            "1111" AFTER 4500 NS,  -- a = b (worst case)
            "1111" AFTER 5000 NS,  -- a < b (need bit 3 only, best case)
            0000" AFTER 5500 NS,   -- a = b (worst case)
            0000" AFTER 6000 NS;   -- a > b (need bit 3 only, best case)
END input_output;
```

> ⚠️ Contraddizione: i nomi non tornano (`ENTITY nibble_comparator_tb` chiusa da `END nibble_comparator`, architecture di `nibble_comparator_test_bench`); nelle ultime due righe di `b` manca il doppio apice iniziale. `gnd` è uno `std_logic` senza valore iniziale, quindi in simulazione vale `'U'` e non `'0'`: va dichiarato `SIGNAL gnd : std_logic := '0';`.

| TIME (ns) | a(3:0) | b(3:0) | gtr | eql | lss |
|---|---|---|---|---|---|
| 0 | "0000" | "0000" | '0' | '0' | '0' |
| 5 | … | … | … | '1' | … |
| 500 | "1111" | "1110" | … | … | … |
| 544 | … | … | '1' | … | … |
| 548 | … | … | … | '0' | … |
| 1500 | "1110" | "1111" | … | … | … |
| 1544 | … | … | '0' | … | … |
| 1548 | … | … | … | … | '1' |
| 2500 | … | "1100" | … | … | … |
| 2533 | … | … | … | … | '0' |
| 2537 | … | … | '1' | … | … |
| 3500 | "1010" | … | … | … | … |
| 3522 | … | … | '0' | … | … |
| 3526 | … | … | … | … | '1' |
| 4000 | "0000" | "1111" | … | … | … |
| 4500 | "1111" | … | … | … | … |
| 4544 | … | … | … | '1' | … |
| 4548 | … | … | … | … | '0' |
| 5000 | "0000" | … | … | … | … |
| 5011 | … | … | … | '0' | … |
| 5015 | … | … | … | … | '1' |
| 5500 | … | "0000" | … | … | … |
| 5544 | … | … | … | … | '0' |
| 5548 | … | … | … | '1' | … |
| 6000 | "1111" | … | … | … | … |

- Nella tabella i puntini indicano che un segnale ha lo stesso valore dell'istante precedente.
- Dall'istante 0 fino a 5 ns non c'è attività e tutti gli ingressi sono bassi; da lì in poi, a intervalli regolari, si applicano nuovi test pattern.
- Agli istanti 500 e 1500 ns ci sono i **worst case** (propagazione attraverso tutti gli stadi): 48 ns.
- Agli istanti 5000 e 6000 ns ci sono i **best case** (decide l'ultimo stadio): 15 ns.
- Si testano le varie condizioni scambiando l'ingresso `a` con `b`, per sollecitare tutto il modulo.

> ⚠️ Contraddizione: il testo della slide indica gli istanti come «5 ns, 15 ns, 50 ns, 60 ns» e i pattern «ogni 10 ns», mentre tabella e codice usano 500, 1500, 5000, 6000 ns con pattern ogni 500–1000 ns; qui si seguono la tabella e il codice.

*Approfondimenti nel wiki: [[descrizione-strutturale]], [[entity-architecture]], [[port-vhdl]], [[generics-vhdl]], [[component-binding]], [[istanziazione-componenti]], [[generate-vhdl]], [[testbench]], [[assegnazione-concorrente]], [[porta-aoi]], [[rom]], [[nibble-comparator]]*
