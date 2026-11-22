# Overview — Architettura dei Sistemi Digitali

LM Ingegneria Informatica, UNINA, a.a. 2026-27, Proff. Nicola Mazzocca e Alessandra De Benedictis; esame: elaborato di gruppo, esercizio di progetto in aula (VHDL e simulazione), prova orale

## Obiettivi e programma · [[1-Introduzione al corso ASDi.pdf#page=2|p. 2]]–[[1-Introduzione al corso ASDi.pdf#page=9|9]]

**Obiettivi.** Dal punto di vista metodologico: progetto di sistemi digitali di complessità crescente, dai circuiti combinatori e sequenziali più semplici alle macchine ottenute per composizione ed estensione di circuiti noti, fino alle fasi di progetto di un processore. Dal punto di vista tecnologico: simulazione e sintesi delle architetture progettate, descritte con un linguaggio di descrizione dell'hardware (HDL), con ambienti di sviluppo commerciali e sintesi su dispositivi programmabili.

**Temi principali** (programma):
1. Studio del VHDL come linguaggio: principali costrutti e livelli di astrazione (dataflow, strutturale, comportamentale, RTL)
2. Progetto di macchine combinatorie e sequenziali; recap delle macchine «notevoli» e loro composizione per creare sistemi complessi
3. Analisi dell'architettura dei dispositivi FPGA target e uso del VHDL secondo le coding guidelines del produttore
4. Progetto di architetture per la comunicazione tra entità e studio dei protocolli di comunicazione
5. Progetto di sistemi digitali fatti di più componenti governati da una logica di controllo complessa
6. Uso di un IDE professionale per editing, simulazione e sintesi; realizzazione di sistemi digitali su board di sviluppo con FPGA

**Esame:** elaborato di gruppo (esercizi di progetto svolti durante il corso e discussi all'esame), esercizio di progetto in aula (progetto + implementazione VHDL + simulazione), prova orale.

**Materiale:** slide dei docenti, documentazione ufficiale del produttore dell'IDE e degli FPGA, progetti VHDL completi di esempio; board di sviluppo con FPGA distribuite ai gruppi tra ottobre e novembre; esercitazioni in aula.

Elenco lezioni → [[lezioni]] · Testo di studio → [[corso-completo]]

## Argomenti coperti nel wiki

| Area | Pagine | Stato |
|---|---|---|
| VHDL: elementi del linguaggio (L1) | [[elementi-lessicali-vhdl]], [[oggetti-vhdl]], [[tipi-vhdl]], [[std-logic]], [[signed-unsigned]], [[array-vhdl]], [[record-vhdl]], [[alias-vhdl]], [[subtype-vhdl]], [[attributi-vhdl]], [[operatori-vhdl]] | completo |
| VHDL: stile dataflow (L2) | [[descrizione-dataflow]], [[assegnazione-concorrente]], [[assegnazione-condizionata]], [[assegnazione-selezionata]] | completo |
| VHDL: stile strutturale (L3) | [[descrizione-strutturale]], [[entity-architecture]], [[port-vhdl]], [[generics-vhdl]], [[component-binding]], [[istanziazione-componenti]], [[generate-vhdl]], [[testbench]] | completo |
| VHDL: simulazione e ritardi (L4) | [[simulazione-tempo-quantizzato]], [[simulazione-ad-eventi]], [[delta-cycle]], [[modello-tempificazione-vhdl]], [[ritardi-inertial-transport]] | completo |
| VHDL: stile comportamentale (L5) | [[descrizione-comportamentale]], [[process-vhdl]], [[wait-e-sensitivity-list]], [[variabili-e-segnali]], [[assegnazione-sequenziale]], [[istruzioni-sequenziali]], [[assert-vhdl]] | completo |
| Teoria: macchine, protocolli, controllo, processore | — | da ingerire (`raw/teoria/`) |

## Filo logico

Le Lezioni 1–5 (cartella `raw/vhdl/`) costruiscono il **VHDL come linguaggio**. La Lezione 1 dà il vocabolario: oggetti (costanti, variabili, segnali), tipi (soprattutto `std_logic` e `signed`/`unsigned`), tipi composti, attributi e operatori. Le Lezioni 2, 3 e 5 presentano i tre **stili di descrizione**, cioè i livelli di astrazione citati nell'introduzione al corso: **dataflow** (assegnazioni concorrenti: equazioni), **strutturale** (entity/architecture, component, port map, generate: schema elettrico, con il testbench per la verifica) e **comportamentale** (process e istruzioni sequenziali: algoritmo). La Lezione 4 spiega **come il simulatore esegue** tutto questo: simulazione ad eventi, transazioni ed eventi, delta cycle, ritardi inertial e transport. È la chiave per capire la differenza fra segnali e variabili nei process (Lezione 5) e le forme d'onda che si vedono in simulazione (glitch della porta complessa nella Lezione 3, attributi dei segnali nella Lezione 1).

## Argomenti mancanti / da ingerire

- I PDF di `raw/teoria/` non sono ancora ingestiti: introduzione al corso (usata finora solo per obiettivi, programma ed esame), macchine combinatorie e sequenziali con i costrutti VHDL, progetto di contatori, protocolli di comunicazione, controllo cablato e microprogrammato, interfaccia seriale, livello microarchitetturale (MIC1), reti di interconnessione e Omega network.
- Dal programma: architettura degli FPGA target, coding guidelines del produttore, uso dell'IDE (simulazione e sintesi) e board di sviluppo (il manuale della Nexys Video è collegato in `raw/vhdl/ManualeNexysVideoDigilent.url`).
