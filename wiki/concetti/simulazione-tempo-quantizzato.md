---
tipo: concetto
importanza_esame: media
prerequisiti: []
fonti_pdf: ["4-Tecniche di simulazione e ritardi.pdf#page=1", "4-Tecniche di simulazione e ritardi.pdf#page=2", "4-Tecniche di simulazione e ritardi.pdf#page=3", "4-Tecniche di simulazione e ritardi.pdf#page=4"]
---

# Simulazione a tempo quantizzato

## Definizione · [[4-Tecniche di simulazione e ritardi.pdf#page=1|p. 1]]–[[4-Tecniche di simulazione e ritardi.pdf#page=4|4]]

Tecnica di simulazione dell'hardware in cui il **tempo avanza a passi di ampiezza fissa** $T_{SAMPLE}$ (passo di quantizzazione). A ogni passo il simulatore campiona gli ingressi e ricalcola il valore di **tutti** i nodi, ispezionando il circuito rappresentato come **netlist tabulare**: una riga per gate (funzione, identificativi delle gate d'ingresso, valore d'uscita), ordinate in modo da rispettare la dipendenza funzionale.

| | |
|---|---|
| **Vantaggi** | semplice senza ritardi (simulazione funzionale, 0-delay); simula anche grandezze continue discretizzate (Spice) |
| **Svantaggi** | non si adatta alla dinamica del sistema; difficile gestire i ritardi delle porte; il passo deve essere minore delle costanti di tempo del circuito → costo computazionale alto |
| **Ottimizzazioni** | scope della variazione di un nodo; passo variabile |

## Derivazioni

### Derivazione — la colonna T = 0 della netlist · [[4-Tecniche di simulazione e ritardi.pdf#page=2|p. 2]]
**Fonte:** tabella con i valori, senza calcolo. Ingressi `a = b = 0`.

| Gate | Funzione | Calcolo | Valore |
|---|---|---|---|
| 1 | Buffer(A) | a | 0 |
| 2 | Buffer(B) | b | 0 |
| 3 | Not(2) | NOT 0 | 1 |
| 4 | Not(1) | NOT 0 | 1 |
| 5 | And(3, 1) | 1 AND 0 | 0 |
| 6 | And(4, 2) | 1 AND 0 | 0 |
| 7 | Or(5, 6) | 0 OR 0 | 0 |

L'ordine delle righe è un **ordine topologico**: ogni gate compare dopo quelle che la pilotano, quindi una sola passata dall'alto in basso basta a calcolare tutto.

### Derivazione — le colonne T = 2 e T = 5 · [[4-Tecniche di simulazione e ritardi.pdf#page=3|p. 3]]
**Fonte:** valori dati; ingressi dalla figura: `a` sale a 2 (e scende a 6), `b` sale a 5.

| Gate | T = 2 (a = 1, b = 0) | T = 5 (a = 1, b = 1) |
|---|---|---|
| 1 | 1 | 1 |
| 2 | 0 | 1 |
| 3 = NOT 2 | 1 | 0 |
| 4 = NOT 1 | 0 | 0 |
| 5 = 3 AND 1 | 1 AND 1 = 1 | 0 AND 1 = 0 |
| 6 = 4 AND 2 | 0 AND 0 = 0 | 0 AND 1 = 0 |
| 7 = 5 OR 6 | 1 | 0 |

**Che circuito è:** $z = a\,\overline{b} + \overline{a}\,b = a \oplus b$, uno XOR. Verifica: T = 0 (0, 0) → 0; T = 2 (1, 0) → 1; T = 5 (1, 1) → 0. ✓
> 🧩 Derivazione mia: l'espressione di `z` ricavata dalla netlist.

**Costo:** a ogni $T_{SAMPLE}$ si ricalcolano tutte e 7 le righe, anche quando gli ingressi non cambiano (ad es. fra t = 3 e t = 4): è lo spreco che la simulazione ad eventi evita.

## Spiegazione

Il tempo quantizzato è il modo «ingenuo» di simulare: si fotografa il circuito a intervalli regolari. Funziona bene se interessa solo la funzione logica (0-delay) o per i simulatori analogici come Spice, dove le grandezze variano con continuità. Per i circuiti digitali con ritardi diventa inefficiente: per vedere un ritardo di 1 ns serve un passo più piccolo di 1 ns, e la maggior parte dei passi non cambia nulla.

## Perché importa

È il termine di confronto che motiva la simulazione ad eventi usata dai simulatori VHDL; tipica domanda d'orale: vantaggi e svantaggi delle due tecniche.

## Connessioni

- [[simulazione-ad-eventi]] — l'alternativa usata dai simulatori VHDL
- [[delta-cycle]] — come un simulatore ad eventi gestisce i ritardi nulli

## Fonti · [[4-Tecniche di simulazione e ritardi.pdf#page=1|p. 1]]–[[4-Tecniche di simulazione e ritardi.pdf#page=4|4]]

- [[tecniche-di-simulazione-lezione]]

_Aggiornato: 2026-11-22 — creazione_
