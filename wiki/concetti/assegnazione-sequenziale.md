---
tipo: concetto
importanza_esame: alta
prerequisiti: ["process-vhdl", "variabili-e-segnali"]
fonti_pdf: ["5-Descrizione Comportamentale.pdf#page=15", "5-Descrizione Comportamentale.pdf#page=16", "5-Descrizione Comportamentale.pdf#page=17", "5-Descrizione Comportamentale.pdf#page=18"]
---

# Assegnazione sequenziale di segnale

## Definizione · [[5-Descrizione Comportamentale.pdf#page=15|p. 15]]–[[5-Descrizione Comportamentale.pdf#page=16|16]]

Un'assegnazione di segnale `<=` scritta dentro un process è **sequenziale**:

1. **ha effetto quando il process si sospende** (le transazioni sono schedulate durante l'esecuzione e applicate dopo);
2. se lo stesso segnale è assegnato più volte nello stesso process, **solo l'ultima assegnazione è valida**;
3. se il process assegna un segnale che sta nella sua sensitivity list, un evento su quel segnale può **riattivare** il process.

## Derivazioni

### Derivazione — `Y <= A * B; Y <= B;` · [[5-Descrizione Comportamentale.pdf#page=16|p. 16]]
**Fonte:** «solo l'ultima è valida».

Con `A = 3`, `B = 4` (valori miei): la prima istruzione schedula `Y ← 12` a +δ, la seconda schedula `Y ← 4` sempre a +δ, **sostituendo** la transazione precedente sullo stesso segnale per lo stesso istante. Alla sospensione `Y` diventa 4: la prima riga non ha alcun effetto.
> 🧩 Derivazione mia: valori numerici e spiegazione in termini di transazioni.

**Uso pratico** (🧩): questa regola permette di scrivere un valore di default all'inizio del process e sovrascriverlo solo in alcuni rami di un `IF`/`CASE`.

### Derivazione — il process che si riattiva da solo · [[5-Descrizione Comportamentale.pdf#page=16|p. 16]]
**Fonte:** codice con `B` sia letto (nella sensitivity list) sia assegnato.

```vhdl
PROCESS (A, B, C)
BEGIN
  X <= A + 1;
  Y <= A * B;
  Z <= C + X;
  B <= Z * C;
END PROCESS;
```
> 🧩 Derivazione mia: esempio numerico. Valori iniziali `A = 1, B = 1, C = 2, X = 0, Y = 0, Z = 0`; il process si esegue a T.

| Ciclo | Valori letti (A B C X Z) | Transazioni a fine ciclo | Riattivazione? |
|---|---|---|---|
| T | 1 1 2 0 0 | X ← 2, Y ← 1·1 = 1, Z ← 2 + 0 = 2, B ← 0·2 = 0 | B cambia (1→0) → sì |
| T + δ | 1 0 2 2 2 | X ← 2, Y ← 1·0 = 0, Z ← 2 + 2 = 4, B ← 2·2 = 4 | B cambia (0→4) → sì |
| T + 2δ | 1 4 2 2 4 | X ← 2, Y ← 1·4 = 4, Z ← 4, B ← 4·2 = 8 | B cambia (4→8) → sì |
| T + 3δ | 1 8 2 2 4 | X ← 2, Y ← 8, Z ← 4, B ← 4·2 = 8 | B non cambia → no |
| T + 4δ | — | Y diventa 8 | Y non è nella lista → fine |

`X` e `Z` sono letti con il valore **precedente** (non stanno nella sensitivity list) e `B` dipende da sé stesso attraverso `Z`: il process si riattiva tre volte in delta successivi, senza che il tempo avanzi, finché i valori non si stabilizzano su `X = 2, Z = 4, B = 8, Y = 8`.
**Verifica:** il punto fisso soddisfa tutte le equazioni: $X = A + 1 = 2$, $Z = C + X = 4$, $B = Z \cdot C = 8$, $Y = A \cdot B = 8$. Con un'equazione senza punto fisso (come `y <= NOT x` in anello) il process si riattiverebbe all'infinito, come il «paradosso» di [[delta-cycle]].

### Derivazione — due assegnazioni, stesso istante di scheduling · [[5-Descrizione Comportamentale.pdf#page=17|p. 17]]–[[5-Descrizione Comportamentale.pdf#page=18|18]]
**Fonte:** due process.

| Process | Schedulazione a T | `x` cambia a | `y` cambia a |
|---|---|---|---|
| `x <= a; y <= b;` | entrambe a T + δ, in sequenza | T + δ | T + δ (stesso istante) |
| `x <= a AFTER 10 NS; y <= b AFTER 6 NS;` | entrambe a T | T + 10 ns | T + 6 ns |

Nel secondo caso `y` cambia **4 ns prima** di `x` (10 − 6 = 4), anche se l'istruzione di `y` viene dopo: l'ordine sequenziale delle istruzioni decide l'ordine di schedulazione, non l'istante di applicazione.

> ⚠️ Contraddizione: il secondo process della slide non ha né sensitivity list né `WAIT`: così scritto non si sospende mai (vedi [[wait-e-sensitivity-list]]); per l'esempio va aggiunto ad es. `WAIT ON a, b;` in fondo.

## Spiegazione

Un process si comporta come se raccogliesse tutte le assegnazioni di segnale in una «lista della spesa» durante l'esecuzione e la consegnasse al simulatore alla sospensione. Ne seguono le tre regole: effetto alla sospensione, vince l'ultima, e i segnali letti nel process hanno sempre il valore dell'attivazione (vedi [[variabili-e-segnali]]).

## Perché importa

È il comportamento che rende i process adatti a descrivere registri e macchine a stati (tutti i segnali si aggiornano insieme, come sul fronte di clock), ma che produce errori se si ragiona come in C.

## Connessioni

- [[variabili-e-segnali]] — l'alternativa immediata
- [[process-vhdl]], [[wait-e-sensitivity-list]] — sospensione e riattivazione
- [[assegnazione-concorrente]] — la stessa assegnazione fuori da un process
- [[modello-tempificazione-vhdl]] — transazioni (value, time)

## Fonti · [[5-Descrizione Comportamentale.pdf#page=15|p. 15]]–[[5-Descrizione Comportamentale.pdf#page=18|18]]

- [[descrizione-comportamentale-lezione]]

_Aggiornato: 2026-11-22 — creazione_
