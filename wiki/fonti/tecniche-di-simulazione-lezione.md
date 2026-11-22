---
tipo: fonte
titolo: "Tecniche di simulazione e ritardi"
file_raw: "vhdl/4-Tecniche di simulazione e ritardi.pdf"
pagine: "1-16"
data_ingest: 2026-11-22
formato: slide-pdf
argomenti: [simulazione a tempo quantizzato, simulazione ad eventi, netlist, linked list, delta cycle, transazioni, eventi, ritardi inertial, ritardi transport]
---

# Tecniche di simulazione e ritardi

## Sommario · [[4-Tecniche di simulazione e ritardi.pdf#page=1|p. 1]]–[[4-Tecniche di simulazione e ritardi.pdf#page=16|16]]

Quarta lezione sul VHDL: come funziona un simulatore. Confronta la **simulazione a tempo quantizzato** (passo fisso, netlist tabulare, esempio 0-delay di uno XOR con la tabella dei valori a T = 0, 2, 5; vantaggi, svantaggi, ottimizzazioni) con la **simulazione ad eventi** (si valuta solo quando un nodo cambia; propagazione con ritardi di 12 ns; rappresentazione a linked list), che è quella dei simulatori VHDL. Introduce i **delta cycle** (ritardo nullo, tempo $x_1 T + x_2\delta$, esempio a tre segnali, «paradosso» dell'oscillazione a tempo fermo), il **modello di tempificazione** VHDL (transazione = (value, time), evento = transazione che cambia il valore; esempio della porta complessa) e i ritardi **inertial** e **transport** (reti RC, filtraggio degli impulsi brevi, figura di confronto).

## Punti chiave

1. Tempo quantizzato: passo fisso, ricalcolo di tutta la netlist a ogni passo; semplice ma non si adatta alla dinamica e costa molto con i ritardi.
2. Simulazione ad eventi: si valuta solo sugli eventi; veloce, più difficile da implementare; è il modello dei simulatori VHDL.
3. Un'assegnazione senza ritardo scade dopo un delta; il delta non è tempo reale.
4. Assegnazioni combinatorie a ritardo nullo si risolvono in più delta allo stesso istante; un anello con inversione oscilla in delta senza far avanzare il tempo.
5. Ogni assegnazione genera una transazione (value, time), con il valore calcolato subito; se il valore cambia è un evento.
6. Inertial: ritardo + filtro degli impulsi brevi; transport: propaga tutto.

## Concetti introdotti

- [[simulazione-tempo-quantizzato]]
- [[simulazione-ad-eventi]]
- [[delta-cycle]]
- [[modello-tempificazione-vhdl]]
- [[ritardi-inertial-transport]]
- collegato: [[assegnazione-concorrente]] (stesso esempio della porta complessa)

## Domande aperte

- **La slide afferma che un ritardo senza parola chiave è `TRANSPORT`: per lo standard il default è `INERTIAL`.** Da chiarire con i docenti (o da prendere come refuso).
- Il testo della slide del delta (p. 8) ha perso i simboli δ nell'estrazione (`x1T+x2`): la forma è $x_1 T + x_2\delta$.
- La figura inertial/transport non è in scala: i tempi esatti degli impulsi non sono ricavabili.
- La linked list di p. 7 collega le gate in modo non del tutto coerente con la netlist di p. 2 (gli ingressi degli invertitori sembrano scambiati): si è riportata la struttura dei campi, non i collegamenti.

## Domande da esame

- Confronta simulazione a tempo quantizzato e ad eventi: principio, vantaggi, svantaggi.
- Cos'è un delta cycle? Perché serve? Simula `a <= '1'; b <= NOT a; c <= NOT b;` delta per delta.
- Spiega il «paradosso» `x <= y; y <= NOT x;`.
- Cos'è una transazione? Differenza fra transazione ed evento.
- Differenza fra ritardo inertial e transport; quale è il default in VHDL? Disegna l'uscita per un impulso più corto del ritardo.

_Aggiornato: 2026-11-22 — creazione_
