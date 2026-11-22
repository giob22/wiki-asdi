# wiki-template

Template per i wiki dei corsi (LLM wiki mantenuto da Claude Code, vault Obsidian, sito di studio su GitHub Pages).
Ricavato da `wiki-tsd`: stesso schema `CLAUDE.md`, stessi file di indicizzazione, stesso sito.

## Nuovo wiki in 4 passi

1. Crea la repo dal template (pubblica se vuoi il sito su GitHub Pages col piano Free):

   ```bash
   gh repo create wiki-<sigla> --template giob22/wiki-template --public --clone
   ```

2. Copia i PDF del corso in `raw/` e apri la cartella con Claude Code.
3. Scrivi `inizializza`: Claude chiede i dati del corso, lancia `output/inizializza.py`, compila i temi del
   programma, sceglie con te i moduli opzionali, attiva GitHub Pages e fa il primo commit.
4. Per ogni lezione: `ingestisci raw/<file>.pdf`. Claude aggiorna il wiki, aggiunge la lezione a
   `wiki/corso-completo.md` e, al push, il sito si aggiorna da solo.

## Cosa c'è dentro

| Percorso | A cosa serve |
|---|---|
| `CLAUDE.md` | schema del wiki: ruolo, operazioni (INIZIALIZZA, INGEST, QUERY, ESERCIZIO, ESAME, SITO, LINT), formato delle pagine, espansione dei calcoli, tracciabilità sui PDF, convenzioni, moduli opzionali |
| `wiki/index.md`, `log.md`, `overview.md`, `lezioni.md`, `corso-completo.md` | file di indicizzazione e testo di studio |
| `wiki/concetti/`, `entità/`, `fonti/`, `esercizi/`, `esame/` | cartelle delle pagine |
| `modelli/` | modelli delle pagine per Obsidian («Inserisci modello») |
| `corso.toml` | dati del corso e configurazione del sito |
| `output/crea_sito.py`, `sito_disegni.py` | sito di studio (stile, tema chiaro/scuro, KaTeX, anteprima delle equazioni) |
| `output/crea_pdf.py` | PDF di studio delle lezioni (Chrome/Edge headless) |
| `output/controlla_corso.py`, `riferimenti_nei_titoli.py` | controlli di integrità e riferimenti ai PDF nei titoli |
| `output/inizializza.py` | sostituisce i segnaposto `{{NOME_CORSO}}`, `{{SIGLA}}`, `{{DESCRIZIONE}}` |
| `.github/workflows/sito.yml` | a ogni push su `main` ricostruisce il sito e lo pubblica su Pages (non parte nella repo template) |
| `.obsidian/` | vault pronto: temi, plugin (Spaced Repetition, Mind Map, Code Files), modelli |

## Il sito

Una pagina per ogni sezione `## Lezione N — titolo` di `wiki/corso-completo.md`, quindi **solo il contenuto dei
PDF**. Spiegazioni e dimostrazioni passo-passo, domande da esame e disegni SVG si aggiungono per lezione in
`corso.toml`, solo quando lo decidi. Per un sito d'intercorso basta `[sito] lezioni = [3, 4, 5]`.

```bash
pip install -r requirements.txt
python output/crea_sito.py               # genera _site/
python -m http.server -d _site 8000      # anteprima su http://localhost:8000
```
