---
tipo: concetto
importanza_esame: alta
prerequisiti: ["entity-architecture", "assegnazione-concorrente"]
fonti_pdf: ["3-Descrizione Strutturale.pdf#page=1", "3-Descrizione Strutturale.pdf#page=2", "3-Descrizione Strutturale.pdf#page=4"]
---

# Descrizione strutturale e gerarchia

## Definizione · [[3-Descrizione Strutturale.pdf#page=1|p. 1]]–[[3-Descrizione Strutturale.pdf#page=2|2]], [[3-Descrizione Strutturale.pdf#page=4|4]]

La **descrizione strutturale** definisce la funzionalità di un circuito in termini di **componenti e loro interconnessione**. Un sistema è un **albero di moduli**: il **top-level module** (radice) istanzia e collega altri moduli, che a loro volta ne istanziano altri, fino a moduli elementari (atomici). Ogni modulo ha un'interfaccia (**entity**, con i suoi **port**) e un'implementazione (**architecture**); un modulo si può usare come componente di un altro o come top-level.

Gli ingredienti, tutti visti nella Lezione 3:

| Ingrediente | Dove si scrive | Pagina |
|---|---|---|
| entity e port | dichiarazione di entity | [[entity-architecture]], [[port-vhdl]] |
| parametri | `GENERIC` nell'entity | [[generics-vhdl]] |
| prototipo del blocco usato | `COMPONENT` nella parte dichiarativa | [[component-binding]] |
| scelta dell'architecture | `FOR … USE ENTITY …` | [[component-binding]] |
| istanze e collegamenti | `label : comp PORT MAP (…)` nel corpo | [[istanziazione-componenti]] |
| fili interni | `SIGNAL` nella parte dichiarativa | [[entity-architecture]] |
| istanze ripetute | `FOR/IF … GENERATE` | [[generate-vhdl]] |

**Significato hardware**: istanziare un modulo e collegarlo equivale a prendere un integrato (ad es. della serie 74) e collegarne i piedini con dei fili.

## Derivazioni

### Derivazione — la porta complessa vista come struttura · [[3-Descrizione Strutturale.pdf#page=24|p. 24]]
**Fonte:** l'architettura `concurrent` di `porta_complessa`, data come insieme di assegnazioni.
> 🧩 Derivazione mia: leggo le quattro assegnazioni come quattro porte collegate da tre fili interni.

| Assegnazione | Porta | Ingressi | Uscita |
|---|---|---|---|
| `w <= NOT a AFTER 12 NS` | NOT | a | w (filo interno) |
| `x <= a AND b AFTER 12 NS` | AND | a, b | x (filo interno) |
| `y <= c AND w AFTER 12 NS` | AND | c, w | y (filo interno) |
| `z <= x OR y AFTER 12 NS` | OR | x, y | z (port) |

I segnali `w`, `x`, `y` dichiarati nella parte dichiarativa sono proprio i fili che collegano le porte: è una struttura a 4 blocchi descritta con assegnazioni invece che con istanze di componenti (le slide lo usano per mostrare la differenza di timing, vedi [[assegnazione-concorrente]]).

## Spiegazione

La descrizione strutturale è il «disegno dello schema elettrico» in forma testuale: si scelgono i blocchi, si dichiarano i fili e si collegano. Si presta alla **progettazione gerarchica**: si descrivono e verificano i blocchi piccoli, poi li si compone. Una stessa architecture può mescolare stili: istanze di componenti, assegnazioni concorrenti e process convivono nel corpo, perché sono tutti statement concorrenti.

## Perché importa

È lo stile con cui si costruiscono i sistemi complessi del corso per **composizione** di macchine notevoli (contatori, registri, mux, unità di controllo), ed è lo stile del testbench, che istanzia il DUT.

## Connessioni

- [[entity-architecture]], [[port-vhdl]], [[generics-vhdl]] — l'interfaccia dei moduli
- [[component-binding]], [[istanziazione-componenti]] — come si usano i moduli
- [[generate-vhdl]] — strutture regolari
- [[testbench]] — un modulo che istanzia il DUT
- [[descrizione-dataflow]] — l'altro stile visto finora

## Fonti · [[3-Descrizione Strutturale.pdf#page=1|p. 1]]–[[3-Descrizione Strutturale.pdf#page=2|2]], [[3-Descrizione Strutturale.pdf#page=4|4]], [[3-Descrizione Strutturale.pdf#page=24|24]]

- [[descrizione-strutturale-lezione]]

_Aggiornato: 2026-11-22 — creazione_
