"""Inizializza una repo creata dal template wiki: sostituisce i segnaposto e riscrive README.md per il corso.

Uso:  python output/inizializza.py --nome "Trasmissione dei Segnali Digitali" --sigla tsd \
          --descrizione "LM Ingegneria Informatica, UNINA, a.a. 2026-27, docente ..., esame orale"

Segnaposto sostituiti in CLAUDE.md, corso.toml e wiki/*.md: {{NOME_CORSO}}, {{SIGLA}}, {{DESCRIZIONE}}.
I segnaposto dei modelli Obsidian ({{date}}, {{title}}) restano. Lo script si rifiuta di ripartire su una repo
già inizializzata (nessun segnaposto rimasto) se non si passa --forza.
"""
import argparse
import re
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
FILE = [ROOT / "CLAUDE.md", ROOT / "corso.toml", *sorted((ROOT / "wiki").rglob("*.md"))]


def toml_str(s):
    return s.replace("\\", "\\\\").replace('"', '\\"')


def proprietario_repo():
    """(owner, repo) dal remote origin, se è su GitHub."""
    try:
        url = subprocess.run(["git", "remote", "get-url", "origin"], cwd=ROOT, capture_output=True, text=True,
                             check=True).stdout.strip()
    except (OSError, subprocess.CalledProcessError):
        return None, None
    m = re.search(r"github\.com[:/]([^/]+)/([^/]+?)(?:\.git)?$", url)
    return (m.group(1), m.group(2)) if m else (None, None)


README = """# Wiki {nome}

Wiki personale del corso **{nome}**{descr}. Lo mantiene Claude Code secondo lo schema in [CLAUDE.md](CLAUDE.md);
si consulta con Obsidian (la cartella della repo è il vault) e, da cellulare, sul sito di studio.

**Sito di studio:** {sito}

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
"""


def main():
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--nome", required=True, help="nome completo del corso")
    ap.add_argument("--sigla", required=True, help="sigla breve, minuscola (nome della repo: wiki-<sigla>)")
    ap.add_argument("--descrizione", default="", help="corso di laurea, ateneo, anno, docente, testo, esame")
    ap.add_argument("--forza", action="store_true", help="riscrivi anche se la repo sembra già inizializzata")
    a = ap.parse_args()

    sigla = a.sigla.strip().lower()
    if not re.fullmatch(r"[a-z0-9][a-z0-9-]*", sigla):
        raise SystemExit("La sigla deve contenere solo lettere minuscole, cifre e trattini (es. tsd, asi, ml-2)")
    if not a.forza and not any("{{NOME_CORSO}}" in p.read_text(encoding="utf-8") for p in FILE if p.exists()):
        raise SystemExit("Nessun segnaposto {{NOME_CORSO}} trovato: la repo sembra già inizializzata (usa --forza)")

    descr = a.descrizione.strip() or "TODO: corso di laurea, ateneo, anno accademico, docente, testo, modalità d'esame"
    cambiati = []
    for p in FILE:
        if not p.exists():
            continue
        s = p.read_text(encoding="utf-8")
        toml = p.suffix == ".toml"
        n = (s.replace("{{NOME_CORSO}}", toml_str(a.nome) if toml else a.nome)
              .replace("{{SIGLA}}", sigla)
              .replace("{{DESCRIZIONE}}", toml_str(descr) if toml else descr))
        if n != s:
            p.write_text(n, encoding="utf-8", newline="\n")
            cambiati.append(p.relative_to(ROOT).as_posix())

    owner, repo = proprietario_repo()
    repo = repo or f"wiki-{sigla}"
    sito = f"https://{owner}.github.io/{repo}/" if owner else f"https://<owner>.github.io/{repo}/"
    (ROOT / "README.md").write_text(README.format(nome=a.nome, descr=f" ({a.descrizione.strip()})" if a.descrizione.strip() else "",
                                                  sito=sito), encoding="utf-8", newline="\n")
    cambiati.append("README.md")

    print("File aggiornati:", ", ".join(cambiati))
    print("Sito (dopo aver attivato GitHub Pages):", sito)
    if owner:
        print(f"Per attivare Pages:  gh api -X POST repos/{owner}/{repo}/pages -f build_type=workflow")


if __name__ == "__main__":
    main()
