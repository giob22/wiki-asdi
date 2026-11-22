# Wiki Architettura dei Sistemi Digitali

Wiki personale del corso **Architettura dei Sistemi Digitali** (LM Ingegneria Informatica, UNINA, a.a. 2026-27, Proff. Nicola Mazzocca e Alessandra De Benedictis; esame: elaborato di gruppo, esercizio di progetto in aula (VHDL e simulazione), prova orale). Lo mantiene Claude Code secondo lo schema in [CLAUDE.md](CLAUDE.md);
si consulta con Obsidian (la cartella della repo è il vault) e, da cellulare, sul sito di studio.

**Sito di studio:** https://giob22.github.io/wiki-asdi/

## Come funziona

| Cartella / file | Contenuto |
|---|---|
| `raw/` | PDF delle lezioni e materiale del corso, mai modificati |
| `wiki/corso-completo.md` | testo di studio: tutte le lezioni, solo il contenuto dei PDF; è la sorgente del sito |
| `wiki/` | indice, log, panoramica, lezioni, pagine concetto / entità / fonte / esercizio, materiale d'esame |
| `corso.toml` | dati del corso e configurazione del sito (lezioni escluse, approfondimenti, disegni) |
| `output/` | script: sito (`crea_sito.py`), PDF di studio (`crea_pdf.py`), controlli, grafici |

Comandi per Claude: `ingestisci raw/<file>.pdf`, domande libere, `risolvi …`, `esame`, `sito`, `lint`.
A ogni ingest la nuova lezione va in `wiki/corso-completo.md` e, con il push su `main`, sul sito
(GitHub Actions → GitHub Pages).

## Script

```bash
pip install -r requirements.txt
python output/crea_sito.py                 # sito in _site/  (anteprima: python -m http.server -d _site 8000)
python output/crea_pdf.py 3                # PDF della lezione 3 in output/pdf/
python output/controlla_corso.py           # controllo di integrità di corso-completo.md
```
