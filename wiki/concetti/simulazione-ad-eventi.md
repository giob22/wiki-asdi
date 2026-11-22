---
tipo: concetto
importanza_esame: alta
prerequisiti: ["simulazione-tempo-quantizzato"]
fonti_pdf: ["4-Tecniche di simulazione e ritardi.pdf#page=1", "4-Tecniche di simulazione e ritardi.pdf#page=5", "4-Tecniche di simulazione e ritardi.pdf#page=6", "4-Tecniche di simulazione e ritardi.pdf#page=7"]
---

# Simulazione ad eventi

## Definizione · [[4-Tecniche di simulazione e ritardi.pdf#page=1|p. 1]], [[4-Tecniche di simulazione e ritardi.pdf#page=5|5]]–[[4-Tecniche di simulazione e ritardi.pdf#page=7|7]]

Tecnica di simulazione in cui il circuito si valuta **solo quando si verifica un evento**, cioè quando cambia il valore di un nodo; il tempo avanza per incrementi **variabili**, da un evento al successivo. Senza eventi la rete è stabile e non c'è nulla da calcolare. Il circuito è rappresentato come **linked list**: ogni gate è un nodo con i campi In1, In2 (puntatori alle gate che la pilotano), Fnc (funzione) e Out (valore d'uscita).

| | |
|---|---|
| **Vantaggi** | simulazione veloce dei circuiti digitali: i simulatori VHDL sono **event driven**; segue la dinamica del sistema |
| **Svantaggi** | più difficile da implementare |

## Derivazioni

### Derivazione — propagazione degli eventi nel circuito con ritardi di 12 ns · [[4-Tecniche di simulazione e ritardi.pdf#page=6|p. 6]]
**Fonte:** figura con forme d'onda, frecce causa-effetto e intervalli «Reacting»; il testo descrive solo il primo passo.

![[vhdl-4-p6-simulazione-ad-eventi.png]]
*Circuito, forme d'onda e attività delle porte.*

Circuito: `g1` NOT (a → w), `g2` AND (a, b → x), `g3` AND (c, w → y), `g4` OR (x, y → z); ritardo 12 ns per porta; `b = c = 1`.

| t (ns) | Evento | Porte attivate (fan-out) | Nuovi eventi schedulati |
|---|---|---|---|
| 0 | a: 1→0 | g1, g2 | w: 0→1 a 12, x: 1→0 a 12 |
| 12 | w: 0→1, x: 1→0 | g3 (da w), g4 (da x) | y: 0→1 a 24, z: 1→0 a 24 |
| 24 | y: 0→1, z: 1→0 | g4 (da y) | z: 0→1 a 36 |
| 36 | z: 0→1 | nessuna (z è un'uscita) | — |

Gli intervalli «Reacting» della figura corrispondono alle righe: g1 e g2 lavorano fra 0 e 12, g3 fra 12 e 24, g4 due volte (12–24 e 24–36). **Il simulatore tocca solo 4 istanti** (0, 12, 24, 36), contro i 37 passi che servirebbero a un simulatore a tempo quantizzato con passo 1 ns per coprire lo stesso intervallo.
> 🧩 Derivazione mia: la tabella evento per evento e il confronto con il tempo quantizzato; è lo stesso circuito della porta complessa di [[assegnazione-concorrente]], dove si spiega anche il glitch di `z`.

## Spiegazione

Il simulatore ad eventi mantiene una **coda di eventi futuri** ordinata per tempo: estrae il prossimo, aggiorna il segnale, rivaluta **solo** le porte nel fan-out del segnale cambiato e inserisce in coda i nuovi eventi che ne derivano. La linked list serve proprio a trovare in fretta il fan-out. Il VHDL è definito su questo modello: le assegnazioni concorrenti si «attivano» sugli eventi dei segnali che leggono, e le transazioni sono gli elementi della coda (vedi [[modello-tempificazione-vhdl]]).

## Perché importa

È il modello con cui il simulatore che si usa nel corso esegue ogni descrizione VHDL: capire la propagazione evento per evento serve per leggere le forme d'onda e spiegare ritardi, glitch e delta cycle.

## Connessioni

- [[simulazione-tempo-quantizzato]] — la tecnica a confronto
- [[modello-tempificazione-vhdl]] — transazioni ed eventi
- [[delta-cycle]] — eventi a ritardo nullo
- [[assegnazione-concorrente]] — attivazione sugli eventi
- [[attributi-vhdl]] — `'EVENT`, `'LAST_EVENT`, …

## Fonti · [[4-Tecniche di simulazione e ritardi.pdf#page=1|p. 1]], [[4-Tecniche di simulazione e ritardi.pdf#page=5|5]]–[[4-Tecniche di simulazione e ritardi.pdf#page=7|7]]

- [[tecniche-di-simulazione-lezione]]

_Aggiornato: 2026-11-22 — creazione_
