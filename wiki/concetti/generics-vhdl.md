---
tipo: concetto
importanza_esame: alta
prerequisiti: ["entity-architecture", "istanziazione-componenti"]
fonti_pdf: ["3-Descrizione Strutturale.pdf#page=8", "3-Descrizione Strutturale.pdf#page=9", "3-Descrizione Strutturale.pdf#page=21"]
---

# Generics

## Definizione · [[3-Descrizione Strutturale.pdf#page=8|p. 8]]–[[3-Descrizione Strutturale.pdf#page=9|9]]

I **generics** sono parametri dichiarati nell'interfaccia di un'entity che **parametrizzano la descrizione**: numero di bit di ingressi e uscite, caratteristiche di timing (tempi di propagazione), parametri fisici (capacità dei nodi, dipendenza dalla temperatura). Sono **costanti**: un generic vale una quantità costante o un'espressione statica.

Il valore si fissa in almeno uno di tre punti; vince quello con priorità maggiore:

| Priorità | Dove | Nota |
|---|---|---|
| 1 (bassa) | default nella dichiarazione di **entity** | sempre raccomandato: componente sintetizzabile e simulabile |
| 2 | dichiarazione del **component** | sovrascrive il default dell'entity |
| 3 (alta) | **istanziazione** (`GENERIC MAP`) | sovrascrive tutto |

Senza default, il valore va dato nel component o nell'istanza: alla fine ogni generic **deve essere risolto**.

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

## Derivazioni

### Derivazione — dimensioni della ROM parametrica · [[3-Descrizione Strutturale.pdf#page=9|p. 9]]
**Fonte:** «la ROM memorizza $2^{depth}$ word di `width` bit».
**Si parte da:** `address` ha `depth` bit, quindi gli indirizzi distinti sono $2^{depth}$; ogni indirizzo seleziona una word di `width` bit.

Con i default dell'entity: `depth = 4` → `address(3 downto 0)`, $2^4 = 16$ word; `width = 32` → `data(31 downto 0)`. Capacità $16 \times 32 = 512$ bit.

### Derivazione — quale valore vince nelle tre istanze · [[3-Descrizione Strutturale.pdf#page=21|p. 21]]
**Fonte:** tre istanze commentate con le dimensioni risultanti.
**Si parte da:** default entity `width = 32, depth = 4`; component `width = 8, depth = 4`; poi l'eventuale `GENERIC MAP`.

| Istanza | GENERIC MAP | width | depth | Word = $2^{depth}$ | Commento slide |
|---|---|---|---|---|---|
| `rom_0` | `(16, 4)` posizionale: width ← 16, depth ← 4 | 16 (istanza) | 4 | 16 | 16 word di 16 bit ✓ |
| `rom_1` | nessuno | 8 (component) | 4 (component) | 16 | 16 word di 8 bit ✓ |
| `rom_2` | `(depth => 5, width => 32)` nominale | 32 (istanza) | 5 (istanza) | 32 | 32 word di 32 bit ✓ |

In `rom_0` l'associazione è **posizionale**: il primo valore va al primo generic dichiarato (`width`), il secondo a `depth`. In `rom_2` è **nominale**, quindi l'ordine `depth`, `width` non conta. Il default 32 dell'entity non è mai usato: il component lo sovrascrive sempre con 8.

## Spiegazione

I generics trasformano un modulo in una **famiglia** di moduli: si scrive una ROM, un registro o un contatore una volta sola e se ne istanziano versioni di larghezze diverse. Sono costanti risolte prima della simulazione/sintesi, quindi possono comparire nei range dei port (`depth-1 downto 0`) e nei costrutti `GENERATE`.

## Perché importa

I progetti d'esame richiedono spesso componenti di larghezza parametrica (registri a N bit, contatori modulo N); dare sempre un default nell'entity è la regola pratica che le slide raccomandano.

## Connessioni

- [[entity-architecture]] — i generics stanno nell'entity
- [[istanziazione-componenti]] — `GENERIC MAP` posizionale o nominale
- [[component-binding]] — il component può ridefinire i default
- [[generate-vhdl]] — i generics fissano il numero di istanze generate
- [[rom]] — l'esempio della lezione

## Fonti · [[3-Descrizione Strutturale.pdf#page=8|p. 8]]–[[3-Descrizione Strutturale.pdf#page=9|9]], [[3-Descrizione Strutturale.pdf#page=21|21]]

- [[descrizione-strutturale-lezione]]

_Aggiornato: 2026-11-22 — creazione_
