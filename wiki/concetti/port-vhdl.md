---
tipo: concetto
importanza_esame: alta
prerequisiti: ["entity-architecture"]
fonti_pdf: ["3-Descrizione Strutturale.pdf#page=6", "3-Descrizione Strutturale.pdf#page=7", "3-Descrizione Strutturale.pdf#page=18"]
---

# Port e modi dei port

## Definizione · [[3-Descrizione Strutturale.pdf#page=6|p. 6]]–[[3-Descrizione Strutturale.pdf#page=7|7]]

Un **port** è un terminale dell'interfaccia di un'entity, con **nome**, **tipo** e **modo**. Il tipo fissa i valori che ogni segnale collegato può assumere; si collegano **solo segnali**, di tipo compatibile. Il **modo** fissa la direzione dei dati:

| Modo | Driver | Si legge dentro? | Si scrive dentro? | Uso |
|---|---|---|---|---|
| `IN` | esterno | sì | no | ingresso |
| `OUT` | interno | **no** | sì | uscita |
| `BUFFER` | interno | sì | sì | uscita rileggibile (sconsigliato) |
| `INOUT` | interno ed esterno | sì | sì | bus bidirezionale (solo nella top-level) |

Raccomandazione delle slide: `inout` solo nella top-level entity, **mai** il modo `buffer`.

![[vhdl-3-p7-modi-dei-port.png]]
*Con `out` l'uscita si rilegge tramite un segnale interno (`W_OUTPUT`); con `buffer` si rilegge l'uscita stessa; `inout` è un terminale bidirezionale.*

## Derivazioni

### Derivazione — come rileggere un'uscita senza `buffer` · [[3-Descrizione Strutturale.pdf#page=7|p. 7]] · [[3-Descrizione Strutturale.pdf#page=18|p. 18]]
**Fonte:** la figura (prima riga) mostra un segnale interno `W_OUTPUT` riportato indietro, ma la slide non scrive il codice.
> 🧩 Derivazione mia: il codice che corrisponde alla figura.

```vhdl
ARCHITECTURE rtl OF esempio IS
  SIGNAL w_output : std_logic;            -- filo interno, leggibile e scrivibile
BEGIN
  w_output <= f(input, w_output);         -- la logica usa il valore interno
  output   <= w_output;                   -- il port OUT è solo scritto
END rtl;
```

`output` (modo `OUT`) compare solo a sinistra, come richiesto da p. 18; la retroazione passa da `w_output`. Così si ottiene il comportamento del `BUFFER` senza usarlo. (`f` sta per la logica del blocco ovale della figura.)

### Derivazione — il port `B` dell'esempio · [[3-Descrizione Strutturale.pdf#page=7|p. 7]]
**Fonte:** `B : IN bit_vector(0 to 3);`

Il range `0 to 3` è **crescente**: `B` ha 4 fili e il bit più a sinistra è `B(0)`. Se lo si collega a un segnale `bit_vector(3 downto 0)`, l'accoppiamento è posizionale (vedi [[array-vhdl]]): `B(0)` riceve il bit 3 del segnale. Per questo nei progetti si usa di norma una sola convenzione, `downto`.

## Spiegazione

Il modo è un contratto sulla direzione del segnale: il compilatore rifiuta la lettura di un `OUT` e la scrittura di un `IN`. Il `BUFFER` è sconsigliato perché impone vincoli a chi collega il port (in VHDL-93 un `buffer` si può collegare solo a un altro `buffer`), mentre il segnale interno ottiene lo stesso effetto senza vincoli. `INOUT` serve per i pin bidirezionali dell'FPGA, quindi ha senso solo al livello più alto.
> 📚 Fonte esterna (IEEE 1076-1993): la restrizione sul collegamento dei port `buffer`, che motiva il consiglio della slide.

## Perché importa

Errori di modo (leggere un `OUT`) sono fra i più comuni nei progetti; il pattern «segnale interno + assegnazione al port» si usa in ogni contatore e registro che deve rileggere la propria uscita.

## Connessioni

- [[entity-architecture]] — i port fanno parte dell'entity e si usano nel corpo
- [[istanziazione-componenti]] — all'istanziazione i port si collegano ai segnali effettivi
- [[std-logic]] — tipo usuale dei port nei design sintetizzabili
- [[buffer-tristate]] — l'uscita in `'Z'` dei port bidirezionali

## Fonti · [[3-Descrizione Strutturale.pdf#page=6|p. 6]]–[[3-Descrizione Strutturale.pdf#page=7|7]], [[3-Descrizione Strutturale.pdf#page=18|18]]

- [[descrizione-strutturale-lezione]]

_Aggiornato: 2026-11-22 — creazione_
