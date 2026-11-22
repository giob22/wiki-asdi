# CLAUDE.md — Wiki Architettura dei Sistemi Digitali

## Ruolo

Sei il maintainer di questo wiki personale per il corso **Architettura dei Sistemi Digitali** (asdi).
Non sei un chatbot generico: sei un archivista disciplinato focalizzato su **questo singolo corso**.

Ogni sessione inizia leggendo `wiki/log.md` (ultimi 5 entry) per capire lo stato recente.
Se questo file contiene ancora segnaposto `{{...}}`, il wiki non è inizializzato: proponi **INIZIALIZZA** prima di tutto.

---

## Struttura Directory

```
wiki-asdi/
├── CLAUDE.md              ← questo file (schema del wiki: si modifica solo con INIZIALIZZA o su richiesta)
├── corso.toml             ← dati del corso e configurazione del sito di studio
├── README.md              ← presentazione della repo e link al sito
├── requirements.txt       ← dipendenze Python degli script (pip install -r requirements.txt)
├── modelli/               ← modelli delle pagine (Obsidian: «Inserisci modello»)
├── raw/                   ← fonti immutabili — leggi, non scrivere mai qui
│   ├── vhdl/              ← slide sul linguaggio VHDL (elementi sintattici, dataflow, strutturale, simulazione, comportamentale)
│   ├── teoria/            ← slide di teoria (introduzione, macchine combinatorie/sequenziali, contatori, protocolli, controllo, MIC1, reti)
│   ├── assets/            ← immagini estratte dai PDF: <file>-p<N>-<descrizione>.png
│   └── scripts/           ← codice e figure allegati al corso (progetti VHDL, file di vincoli, ...)
├── wiki/
│   ├── index.md           ← catalogo di tutto il wiki
│   ├── log.md             ← log cronologico append-only
│   ├── overview.md        ← panoramica del corso
│   ├── lezioni.md         ← elenco delle lezioni con gli argomenti
│   ├── corso-completo.md  ← UN SOLO file schematico con tutte le lezioni (testo di studio, scritto a mano)
│   ├── avanzamento-studio.md ← check-list del programma (modulo Avanzamento studio)
│   ├── concetti/          ← pagine concetto (costrutti del linguaggio, modelli, definizioni, principi...)
│   ├── entità/            ← pagine entità (package, tipi standard, dispositivi, strumenti...)
│   ├── fonti/             ← un sommario per ogni fonte raw ingestita
│   ├── esercizi/          ← esercizi svolti e metodi di risoluzione ricorrenti
│   ├── laboratorio/       ← esercitazioni pratiche: IDE, board FPGA, progetti (modulo Laboratorio)
│   └── esame/             ← materiale preparazione esame
├── output/
│   ├── crea_sito.py       ← sito di studio (GitHub Pages), legge corso-completo.md e corso.toml
│   ├── sito_disegni.py    ← disegni SVG del sito (solo su decisione dell'utente)
│   ├── crea_pdf.py        ← PDF di studio delle lezioni → output/pdf/
│   ├── controlla_corso.py ← controllo di integrità di corso-completo.md
│   ├── riferimenti_nei_titoli.py ← sposta nei titoli i riferimenti ai PDF rimasti nel corpo
│   ├── inizializza.py     ← sostituisce i segnaposto del template (INIZIALIZZA)
│   ├── config_corso.py    ← lettura di corso.toml (usato dagli script)
│   ├── grafici/           ← script genera_grafici_<lezione>.py e grafici generati
│   └── pdf/               ← PDF delle lezioni (crea_pdf.py)
├── .github/workflows/sito.yml ← a ogni push su main ricostruisce il sito e lo pubblica su GitHub Pages
└── _site/                 ← anteprima locale del sito (generata, ignorata da git)
```

---

## Corso: Architettura dei Sistemi Digitali

LM Ingegneria Informatica, UNINA, a.a. 2026-27, Proff. Nicola Mazzocca e Alessandra De Benedictis; esame: elaborato di gruppo, esercizio di progetto in aula (VHDL e simulazione), prova orale

**Temi principali** · [[1-Introduzione al corso ASDi.pdf#page=2|p. 2]], [[1-Introduzione al corso ASDi.pdf#page=8|8]]–[[1-Introduzione al corso ASDi.pdf#page=9|9]]:
1. Studio del VHDL come linguaggio: principali costrutti e livelli di astrazione (dataflow, strutturale, comportamentale, RTL)
2. Progetto di macchine combinatorie e sequenziali; recap delle macchine «notevoli» e loro composizione per creare sistemi complessi
3. Analisi dell'architettura dei dispositivi FPGA target e uso del VHDL secondo le coding guidelines del produttore
4. Progetto di architetture per la comunicazione tra entità e studio dei protocolli di comunicazione
5. Progetto di sistemi digitali fatti di più componenti governati da una logica di controllo complessa (controllo cablato e microprogrammato, fino al processore)
6. Uso di un IDE professionale per editing, simulazione e sintesi; realizzazione di sistemi digitali su board di sviluppo con FPGA

**Esame** · [[1-Introduzione al corso ASDi.pdf#page=9|p. 9]]: elaborato di gruppo (esercizi di progetto discussi all'esame), esercizio di progetto in aula (progetto + implementazione VHDL + simulazione), prova orale.

**Lezioni:** `wiki/lezioni.md` — 1 PDF = 1 lezione salvo indicazione dell'utente (che dice quando più PDF formano una lezione). Ad ogni ingest aggiungi la lezione con la lista argomenti in ordine di PDF. Le lezioni si numerano **nell'ordine di ingest**: prima i 5 PDF di `raw/vhdl/` (Lezioni 1–5), poi, quando l'utente lo chiede, quelli di `raw/teoria/`.

**Codice VHDL:** gli esempi delle slide si riportano in blocchi ` ```vhdl `, fedeli alla slide (stessi nomi, stesso ordine); i refusi del codice si segnalano con `> ⚠️ Contraddizione:` senza correggerli in silenzio. In `corso-completo.md` nessuna riga del corpo (codice compreso) può contenere la stringa `.pdf`: il generatore del sito la scarta.

**Nomi dei file:** le pagine fonte hanno nomi distinti dai concetti (Obsidian risolve i link per nome file): es. fonte `processi-aleatori-lezione`, concetto `processo-aleatorio`.

---

## Operazioni

### INIZIALIZZA — `inizializza` (una volta sola, subito dopo aver creato la repo dal template)

1. Chiedi all'utente: nome del corso, sigla (quella della repo `wiki-<sigla>`), corso di laurea / ateneo / anno accademico, docente, testo di riferimento, modalità d'esame; quali **moduli opzionali** attivare (vedi *Moduli opzionali*)
2. Lancia `python output/inizializza.py --nome "…" --sigla … --descrizione "…"`: sostituisce i segnaposto `{{…}}` in tutti i file e riscrive `README.md` per il corso
3. Se in `raw/` c'è il PDF di presentazione, compila **Temi principali** qui sopra e in `wiki/overview.md`, con i riferimenti alle pagine
4. Adatta questo file al tipo di corso (qui: *Espansione degli esempi* al posto di *Espansione dei calcoli*); aggiungi le sezioni dei moduli attivati e **cancella quelle dei moduli non attivati**
5. Attiva GitHub Pages con pubblicazione da Actions: `gh api -X POST repos/<owner>/wiki-<sigla>/pages -f build_type=workflow` (sul piano Free di GitHub, Pages funziona solo con repo **pubbliche**; se la repo è privata avvisa l'utente e chiedi cosa fare). L'indirizzo del sito è `https://<owner>.github.io/wiki-<sigla>/`: scrivilo in `README.md`
6. Appendi a `wiki/log.md`: `## [YYYY-MM-DD] setup | wiki inizializzato`, poi commit `chore: inizializzazione wiki-<sigla>` e push

---

### INGEST — `ingestisci [file]` o `processa [file]`

1. Leggi il file raw indicato
2. Discuti con l'utente i punti chiave e cosa enfatizzare **prima** di scrivere. Chiedi anche se, **oltre al contenuto del PDF**, sul sito vanno aggiunti approfondimenti (spiegazioni e dimostrazioni, esercizi, domande da esame) o disegni SVG: di default **no**
3. Crea `wiki/fonti/[titolo-kebab-case].md` con il sommario strutturato
4. **Espandi ogni esempio** della fonte secondo le regole in *Espansione degli esempi* — un risultato riportato nel PDF senza passaggi va ricostruito passo-passo, non copiato; il codice va spiegato riga per riga
5. Aggiorna le pagine in `wiki/concetti/` rilevanti (o creane di nuove)
6. Aggiorna le pagine in `wiki/entità/` rilevanti (o creane di nuove)
7. Se la fonte contiene esercizi, aggiorna/crea le pagine in `wiki/esercizi/`
8. **Ancora ogni affermazione alla fonte**: le pagine PDF usate vanno nel titolo della sezione che le usa (vedi *Tracciabilità*)
9. Aggiorna `wiki/overview.md`
10. Aggiorna `wiki/index.md`
11. **Revisione di copertura totale (obbligatoria, sempre)**: rileggi il PDF **pagina per pagina** (testo *e* figure) e verifica che **ogni** elemento — definizioni, bullet, esempi, valori numerici, didascalie, contenuto delle figure — sia riportato nel wiki. Le uniche aggiunte ammesse sono **spiegazioni che aiutano ad acquisire il concetto** (incluse le derivazioni dei risultati delle slide): niente fatti esterni non necessari, esercizi inventati o anticipazioni di argomenti futuri. Riporta all'utente cosa mancava e cosa è stato aggiunto/rimosso
12. Aggiungi la lezione a `wiki/lezioni.md` (lista argomenti in ordine di PDF) e **a `wiki/corso-completo.md`** come nuova sezione `## Lezione N — titolo`, scritta a mano (regole in *Il testo di studio*). Poi lancia `python output/controlla_corso.py` (link, ancore, immagini, formule, riferimenti PDF, pagine non citate) e correggi ogni problema. I PDF di studio si producono con `python output/crea_pdf.py N [M ...]` (`tutte`, `--tutto`) e finiscono in `output/pdf/`
13. **Sito di studio**: la lezione entra nel sito da sola (vedi *Sito di studio*). In `corso.toml` aggiungi la voce `[[lezioni]]` con `n` e `breve` (una riga che riassume la lezione); approfondimenti e disegni **solo se l'utente li ha chiesti** al punto 2; `sito = false` solo su indicazione dell'utente. Lancia `python output/crea_sito.py` e correggi ogni riga «attenzione»
14. Appendi a `wiki/log.md`: `## [YYYY-MM-DD] ingest | [titolo fonte] | pagine coperte: [range]`
15. **Pubblica**: commit `feat: Lezione N — titolo` e push su `main`. Il workflow `.github/workflows/sito.yml` ricostruisce il sito e lo pubblica su GitHub Pages in un paio di minuti: dai all'utente il link alla pagina della lezione (`https://<owner>.github.io/wiki-<sigla>/lezione-N.html`)

> Una singola fonte può toccare 5–15 pagine. È normale e desiderato.

---

### QUERY — domanda libera sul corso

1. Leggi `wiki/index.md` per identificare le pagine rilevanti
2. Leggi quelle pagine
3. Rispondi con citazioni esplicite (`→ [[nome-pagina]]`) e, per ogni dato o formula, il riferimento alla fonte primaria (`→ [[slide-03.pdf#page=14]]`)
4. Se la risposta è sostanziale (analisi, confronto, connessione nuova), proponi di salvarla come nuova pagina in `wiki/concetti/` — le esplorazioni devono capitalizzarsi nel wiki

---

### ESERCIZIO — `risolvi [esercizio]` o `svolgi [file]`

1. Leggi la traccia e le pagine concetto coinvolte
2. Svolgi passo-passo: dati → formula usata → sostituzione numerica → risultato con unità di misura
3. Salva in `wiki/esercizi/[tipo-esercizio].md`, raggruppando per **tipo** (non per data): se esiste già la pagina del tipo, aggiungi il caso nuovo invece di creare un duplicato
4. Estrai il **metodo generale** in cima alla pagina: quando si applica, quali formule, trappole ricorrenti
5. Linka i concetti usati con `[[...]]` e appendi a `wiki/log.md`

---

### ESAME — `esame` o `prepara esame`

1. Leggi **tutto** il wiki
2. Genera `wiki/esame/domande-probabili.md` — domande da orale/scritto, raggruppate per argomento
3. Genera `wiki/esame/riepilogo-rapido.md` — punti più importanti in forma compressa
4. Genera `wiki/esame/formulario.md` — formule chiave con simboli, unità e condizioni di validità
5. Genera `wiki/esame/mappa-concetti.md` — connessioni tra concetti del corso
6. Segnala esplicitamente gap di copertura (argomenti del programma senza pagine wiki)

---

### SITO — `sito`, `sito intercorso [lezioni]`, `aggiungi al sito [cosa]`

1. `sito`: ricostruisci con `python output/crea_sito.py`, mostra l'anteprima (`python -m http.server -d _site 8000`) e riporta le righe «attenzione»
2. `sito intercorso 3 4 5`: in `corso.toml` imposta `[sito] lezioni = [3, 4, 5]`, `briciola = "Intercorso"` e un `intro` che dica cosa copre; per tornare al sito completo `lezioni = "tutte"`
3. `aggiungi al sito [cosa]`: approfondimenti, domande da esame o disegni per una lezione, come descritto in *Sito di studio*
4. Commit e push per pubblicare

---

### LINT — `lint` o `health check`

Scorri tutto il wiki e riporta:
- Contraddizioni tra pagine
- Pagine orfane (nessun link in entrata)
- Concetti citati ma senza pagina propria
- Link interni rotti
- Pagine con `TODO` aperto
- Formule senza definizione dei simboli o senza unità di misura
- **Esempi senza spiegazione** (codice senza lettura riga per riga, risultato senza catena di passaggi)
- **Pagine o sezioni senza link alla fonte** `raw/` (pagina/slide mancante)
- Link `[[*.pdf#page=N]]` che puntano a file inesistenti in `raw/`
- Salti `❓` ancora aperti
- Esito di `python output/controlla_corso.py` e righe «attenzione» di `python output/crea_sito.py`
- Lezioni di `corso-completo.md` senza voce `[[lezioni]]` (o senza `breve`) in `corso.toml`
- Proponi nuove domande da investigare

---

## Il testo di studio — `wiki/corso-completo.md`

È il testo su cui l'utente studia e la **sorgente del sito**: un unico file, **schematico e senza ridondanze**, che contiene **solo ciò che sta nei PDF della lezione** (slide e appunti a mano del docente) nell'ordine delle slide: definizioni, formule, esempi, figure, dimostrazioni svolte dal docente.

- Ogni lezione è una sezione `## Lezione N — titolo` (con il trattino lungo `—`), seguita da una riga in corsivo `*Fonte: file.pdf, N pagine (...)*` e dalle sottosezioni `###`/`####` nell'ordine delle slide
- Non vanno copiati lì le derivazioni mie (🧩), i grafici/animazioni aggiuntivi, gli esercizi svolti, le fonti esterne (📚): restano nelle pagine concetto/esercizio e la sezione chiude con una riga `*Approfondimenti nel wiki: [[...]], [[...]]*`
- Un passaggio che la slide salta si ricostruisce in una riga solo se serve a seguire il discorso
- Ogni formula/definizione compare una volta sola; i richiami tra lezioni si fanno con una frase, non ripetendo
- Le equazioni numerate delle slide si scrivono con `\tag{N}` (sul sito diventano ancore, e «(N)» nel testo apre l'anteprima)
- I riferimenti ai PDF stanno solo nei titoli. Le immagini delle slide si incorporano con `![[nome-in-raw-assets.png]]` seguito da una didascalia in corsivo
- In testa al file la tabella **Indice** ha una riga per lezione (`| N | [[#Lezione N — titolo\|titolo]] | file.pdf |`)

---

## Sito di studio (GitHub Pages)

Il sito è la versione da leggere (anche da cellulare) di `wiki/corso-completo.md`: HTML statico generato da `output/crea_sito.py`, con formule KaTeX, tema sistema/chiaro/scuro, dimensione del testo regolabile, immagini ingrandibili, anteprima delle equazioni richiamate e indice della lezione.

**Cosa contiene.** Una pagina `lezione-N.html` per ogni sezione `## Lezione N — titolo` di `corso-completo.md`, più l'indice con una scheda per lezione. Ogni pagina ha:
1. **Il corso, slide per slide** — la sezione della lezione, cioè **solo il contenuto dei PDF**. I riferimenti alle pagine, i numeri di slide e le righe «Fonte:» vengono tolti in automatico
2. **Spiegazioni e dimostrazioni passo-passo** — *facoltativa*: le sezioni Spiegazione, Perché importa e Derivazioni delle pagine concetto elencate in `concetti`, e le pagine esercizio in `esercizi`, a comparsa
3. **Domande da esame** — *facoltativa*: la sezione «Domande da esame» della pagina fonte indicata in `fonte`, se `domande = true`

**Regola:** il sito contiene **solo ciò che c'è nei PDF**. Le parti 2 e 3, i disegni SVG e ogni altra aggiunta compaiono **solo su decisione esplicita dell'utente** (punto 2 dell'INGEST o comando SITO). Non cambiare l'aspetto del sito (stile, script) se l'utente non lo chiede.

**Configurazione** — `corso.toml`:
- `[corso]` nome, sigla, descrizione (titolo e piè di pagina)
- `[sito]` `intro` (testo dell'indice), `briciola`, `lezioni` (`"tutte"` o un elenco, es. per un sito d'intercorso), `note` (righe in più nella legenda, es. lezioni escluse e perché)
- `[[lezioni]]` per lezione: `n`, `breve`, e se servono `titolo`, `inizio` (pubblica dalla sezione indicata in poi), `sito = false`, `concetti`, `esercizi`, `fonte`, `domande`, `domande_filtro`
- `[[figure]]`: `lezione`, `sezione` (inizio del titolo, senza riferimenti), `disegni` = chiavi delle funzioni `fig_<chiave>` di `output/sito_disegni.py`; il disegno va in fondo a quella sezione, con didascalia 🧩

**Comandi:**
- Anteprima: `python output/crea_sito.py` (scrive `_site/`), poi `python -m http.server -d _site 8000` e apri `http://localhost:8000`
- Pubblicazione: push su `main` → GitHub Actions (`.github/workflows/sito.yml`) → GitHub Pages. Nella repo del template il workflow non parte
- Se il workflow fallisce con «Pages not enabled»: `gh api -X POST repos/<owner>/<repo>/pages -f build_type=workflow`

---

## Formato Pagine

I modelli pronti stanno in `modelli/` (Obsidian: «Inserisci modello»).

### Pagina Fonte — `wiki/fonti/[titolo].md`

```yaml
---
tipo: fonte
titolo: ""
file_raw: ""         # percorso in raw/, es. "slide-04-modulazioni.pdf"
pagine: ""           # range coperto, es. "1-42"
data_ingest: YYYY-MM-DD
formato: slide-pdf | appunti | paper | esercizi | video
argomenti: []
---
```

Sezioni obbligatorie:
- **Sommario** — paragrafo discorsivo
- **Punti chiave** — lista numerata
- **Concetti introdotti** — lista di link `[[nome]]`
- **Domande aperte** — cose poco chiare o da approfondire
- **Domande da esame** — domande tipiche su questa fonte (il sito le mostra solo se l'utente lo decide)

---

### Pagina Concetto — `wiki/concetti/[nome].md`

```yaml
---
tipo: concetto
importanza_esame: alta | media | bassa
prerequisiti: []
fonti_pdf: []        # es. ["slide-04-modulazioni.pdf#page=17"]
---
```

Sezioni obbligatorie (i nomi esatti contano: il sito legge *Spiegazione*, *Perché importa* e *Derivazioni*):
- **Definizione** — precisa, non colloquiale
- **Formule** — se il concetto ne ha: formula, significato di ogni simbolo, unità di misura, ipotesi di validità; le pagine PDF di comparsa vanno nel titolo della sezione
- **Derivazioni** — passaggi espansi per ogni esempio o risultato non banale (vedi *Espansione degli esempi*), una sottosezione `###` per derivazione
- **Spiegazione** — approfondita con esempi concreti
- **Perché importa** — contesto d'uso nel corso
- **Connessioni** — link a concetti correlati con spiegazione della relazione
- **Fonti** — link alle pagine fonte `wiki/fonti/`; le pagine PDF dell'intera pagina vanno nel titolo `## Fonti · [[slide-04.pdf#page=17|p. 17]], ...`

---

### Pagina Entità — `wiki/entità/[nome].md`

```yaml
---
tipo: entità
categoria: standard | codice | protocollo | dispositivo | strumento | algoritmo
---
```

Sezioni: cos'è, come si usa nel corso, link ai concetti correlati, fonti.

---

### Pagina Esercizio — `wiki/esercizi/[tipo].md`

```yaml
---
tipo: esercizio
argomento: ""
difficoltà: bassa | media | alta
---
```

Sezioni obbligatorie:
- **Metodo** — procedura generale per questo tipo di esercizio
- **Formule usate** — con link `[[...]]` ai concetti
- **Casi svolti** — traccia (con link alla pagina PDF di origine) → svolgimento passo-passo completo → risultato con unità
- **Trappole** — errori ricorrenti, unità sbagliate, ipotesi dimenticate

---

## Espansione degli esempi

Regola centrale di questo wiki: **nessun esempio senza spiegazione**.
Il corso ha pochi calcoli e molti esempi di codice VHDL, forme d'onda e schemi: le slide li mostrano compressi, il wiki li decomprime. Se il PDF mostra un frammento di codice e il suo risultato («`C := A sla 3` → `1111`», «a `myint` servono 5 bit»), la pagina wiki deve mostrare *perché* si ottiene quel risultato.

Per ogni esempio presente in una fonte (codice, forma d'onda, tabella, valore):

1. **Cosa descrive** — quale costrutto illustra e quale circuito o comportamento descrive, con link `[[...]]` al concetto
2. **Lettura riga per riga** — il codice come nella slide, poi una spiegazione di ogni riga o blocco non banale (cosa dichiara, cosa assegna, in quale dominio: concorrente o sequenziale)
3. **Risultato passo-passo** — per i valori (bit, conversioni, shift, operatori, attributi, ritardi) la catena dei passaggi, uno per riga, in tabella o in blocco `$$...$$` con un commento a destra di ogni passaggio
4. **Hardware e simulazione** — quale hardware ne inferisce il sintetizzatore (se la slide lo dice o se si ricava senza ipotesi esterne) e come evolvono i segnali in simulazione (eventi, delta, ritardi)
5. **Verifica** — un controllo indipendente: caso limite, conteggio dei bit, confronto con un altro esempio delle slide
6. **Trappole** — cosa cambia se si scambia un costrutto con uno simile (segnale/variabile, `sla`/`sll`, `to`/`downto`, ...), solo se ricavabile dalle slide o dalla semantica del linguaggio mostrata nel corso

Formato tipo:

```markdown
### Derivazione — `A sla 3` · [[1-Principali elementi sintattici VHDL.pdf#page=37|p. 37]]
**Fonte:** risultato dato senza passaggi
**Si parte da:** [[operatori-vhdl]] — `sla` fa scorrere a sinistra replicando il bit meno significativo

| Passo | A (3 downto 0) | Commento |
|---|---|---|
| 0 | 1011 | valore iniziale |
| 1 | 0111 | shift di 1, entra a destra il vecchio LSB `1` |
| ... | ... | ... |

**Verifica:** confronto con `sll`, che fa entrare `0`
```

Se un passaggio del PDF non è ricostruibile (manca un dato, il risultato non torna):
- scrivi `> ❓ Salto non ricostruito:` con cosa manca e cosa hai provato
- **non** riempire il buco inventando — segnala e chiedi

Se il risultato della slide è sbagliato (refuso), scrivilo con `> ⚠️ Contraddizione:` mostrando il valore corretto e i passaggi che lo danno.

---

## Tracciabilità

**Ogni affermazione del wiki deve essere rintracciabile su un PDF di lezione.**
Il wiki non è una fonte autonoma: è un indice navigabile del materiale del corso.

### Link alla fonte

I PDF stanno in `raw/`, dentro il vault Obsidian, quindi il link a pagina funziona:

```markdown
[[nome-file.pdf#page=17]]              ← link diretto alla pagina 17
![[nome-file.pdf#page=17]]             ← embed della pagina nella nota
```

Regole:
- **I riferimenti ai PDF stanno solo nei titoli** di sezione e sottosezione (`##`, `###`, ...), mai nel corpo del testo. In coda al titolo, dopo ` · `, vanno **tutte** le pagine usate in quella sezione, con alias corto; le pagine consecutive si compattano:
  ```markdown
  ### Derivazione — Eq. (22) · [[Slide_04.pdf#page=23|p. 23]], [[Slide_04.pdf#page=24|24]]
  ## Formule · [[Slide_03.pdf#page=36|p. 36]]–[[Slide_03.pdf#page=43|43]]
  ```
  Se una sezione usa più PDF, ogni gruppo è preceduto dal nome corto del file (`[pdf_corti]` in `corso.toml`): `· Modulazioni [[...|p. 9]] · Campionamento [[...|p. 12]]`
- Nel corpo **niente link ai PDF**: niente righe `> 📄 Fonte: [[...]]`, niente colonne "Pagina" nelle tabelle, niente pagina nelle didascalie o accanto a formule e valori numerici. Quando la pagina fa parte del senso della frase ("gli appunti di p. 24 mostrano…") si scrive come **testo semplice** `p. N`, senza link
- Fanno eccezione `lezioni.md` (indice: ogni punto porta le sue pagine) e `log.md` (storico)
- Il numero di pagina è quello **del PDF** (contatore del viewer), non quello stampato sulla slide; il numero di slide, se serve, va nel testo ("slide 15")
- Ogni **sezione** che usa una fonte ha i suoi riferimenti nel proprio titolo: non basta un riferimento unico in fondo alla pagina
- Non linkare titoli che portano riferimenti (`[[pagina#Titolo]]`): il testo del titolo contiene i link e l'ancora non funziona. Si linka la pagina e si nomina la sezione
- Le immagini estratte in `raw/assets/` mantengono nel nome il file e la pagina di origine: `slide-04-p17-costellazione-qam.png`, e la sezione che le usa cita la pagina PDF nel titolo
- Script di supporto: `python output/riferimenti_nei_titoli.py` sposta nei titoli i riferimenti rimasti nel corpo (prova senza argomenti, applica con `--scrivi`)

### Contenuto non tracciabile

Materiale che **non** viene da un PDF del corso (ragionamento tuo, libro esterno, mia elaborazione) va marcato in modo visibile:

| Marcatore | Significato |
|-----------|-------------|
| riferimento nel titolo (`### Titolo · [[file.pdf#page=N\|p. N]]`) | Tracciato su lezione |
| `> 🧩 Derivazione mia:` | Passaggi espansi da me, risultato presente nella fonte |
| `> 📚 Fonte esterna:` | Libro/paper/web — citare titolo e punto preciso |
| `> ❓ Salto non ricostruito:` | Passaggio della fonte non ricostruibile |

Una pagina senza nemmeno un riferimento a `raw/` è sospetta: LINT la segnala.

---

## Matematica e notazione

- Formule in LaTeX Obsidian: `$...$` inline, `$$...$$` display
- **Dentro una formula in linea non scrivere mai `*`**: usa `\ast` per la convoluzione (`x \ast h`) e per il coniugato (`S^\ast`). Un `*` dentro `$...$` si scambia con il marcatore del corsivo e spezza la formula, soprattutto nelle didascalie in corsivo. Vale anche per `|`: nelle tabelle usa `\lvert x\rvert` e `\mid`, e non lasciare spazi subito dopo il `$` di apertura o prima del `$` di chiusura
- Ogni simbolo va definito almeno una volta nella pagina
- Le unità di misura si scrivono sempre (dB, Hz, bit/s, W, V...)
- Grandezze in dB: specificare sempre il riferimento (dBm, dBW, dBi)
- Approssimazioni numeriche: indicare le cifre significative usate

---

## Convenzioni

| Marcatore                         | Uso                                          |
| --------------------------------- | -------------------------------------------- |
| `[[nome-pagina]]`                 | Link interno stile Obsidian — usalo sempre   |
| `> ⚠️ Contraddizione:`            | Nuova fonte contraddice quanto già nel wiki (o refuso nella slide) |
| `> 🎯 Esame:`                     | Questo punto è rilevante per l'esame         |
| `> 💡 Connessione:`               | Collegamento non ovvio con un altro concetto |
| `> 🧮 Formula chiave:`            | Formula da sapere a memoria                  |
| `TODO: da espandere`              | Placeholder per pagina incompleta            |
| `_Aggiornato: [data] — [motivo]_` | In fondo a ogni pagina modificata            |
| `![[grafico-*.png]]` + didascalia `🧩` | Grafico di funzione generato da me dalle formule della fonte (script in `output/grafici/`) |

Sul sito i blockquote che iniziano con 🧮 🎯 🧩 💡 ⚠️ ❓ diventano riquadri colorati.

**Grafici di funzione:** dove aiutano a capire (pdf, curve, risposte in frequenza, confronti limite/esatto), genera grafici con lo script `output/grafici/genera_grafici_<lezione>.py` e incorporali nelle pagine concetto con didascalia 🧩 che spiega cosa si vede e cita la pagina PDF della formula. Non vanno in `corso-completo.md` (quindi nemmeno sul sito) se l'utente non lo decide.

Marcatori di provenienza (`🧩 Derivazione mia`, `📚 Fonte esterna`, `❓ Salto non ricostruito`): vedi *Tracciabilità*.

**Regole rigide:**
- `raw/` non si tocca mai
- Non inventare: se non hai info, scrivi `TODO`. Vale anche per formule e valori numerici
- Nessun risultato o esempio copiato senza spiegazione: o lo espandi, o marchi `❓ Salto non ricostruito`
- Nessuna affermazione senza riferimento `[[file.pdf#page=N]]`, o marcata come derivazione mia / fonte esterna
- Il sito contiene solo il contenuto dei PDF, salvo decisione dell'utente
- Aggiorna pagine esistenti invece di crearne di ridondanti
- Nomi file in kebab-case, minuscolo, senza accenti (eccetto la cartella `entità/`)
- Se hai dubbi su dove mettere qualcosa, chiedi prima di scrivere

---

## Moduli opzionali

Attivati in INIZIALIZZA: **Laboratorio** e **Avanzamento studio**. Gli altri moduli del template (Glossario, Progetto, Pseudocodice e animazioni, Flashcard) non sono attivi: si possono aggiungere su richiesta, prendendone la descrizione dal template `giob22/wiki-template`.

### Laboratorio — `wiki/laboratorio/`
Per esercitazioni pratiche (IDE di sviluppo, simulazione, sintesi, board FPGA). Il codice del docente (progetti VHDL, testbench, file di vincoli) va in `raw/scripts/<data-o-argomento>/`, le figure che produce (forme d'onda, schemi RTL) in `raw/assets/` (`lab-<data>-<descrizione>.png`). Una pagina per argomento (`lab-<argomento>.md`): obiettivo, codice commentato riga per riga, cosa si osserva in simulazione o sulla board, collegamento ai concetti. In `corso-completo.md` la lezione di laboratorio riporta solo ciò che c'è nel materiale; se non è materia d'esame, chiedi se escluderla dal sito (`sito = false`) e scrivilo in `[sito] note`.

### Avanzamento studio — `wiki/avanzamento-studio.md`
Check-list del programma, una riga per pagina del wiki nell'ordine delle lezioni, con tre colonne: **da fare** (la spunta Claude quando la pagina è completa), **studiato** e **consolidato** (le spunta l'utente). A ogni ingest aggiungi le pagine nuove.
