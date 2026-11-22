---
tipo: concetto
importanza_esame: bassa
prerequisiti: []
fonti_pdf: ["1-Principali elementi sintattici VHDL.pdf#page=2", "1-Principali elementi sintattici VHDL.pdf#page=5"]
---

# Elementi lessicali e identificatori del VHDL

## Definizione · [[1-Principali elementi sintattici VHDL.pdf#page=2|p. 2]]–[[1-Principali elementi sintattici VHDL.pdf#page=5|5]]

Gli **elementi lessicali** sono i «mattoni» con cui si scrive un sorgente VHDL: commenti, numeri, caratteri, stringhe, bit string e identificatori. Le regole fondamentali:

- il VHDL **non distingue maiuscole e minuscole**, né negli identificatori né nelle parole chiave;
- il testo è in **formato libero**: un'istruzione può occupare più righe e spazi, tabulazioni e a capo sono equivalenti;
- un **commento** inizia con `--` in qualunque punto della riga e finisce a fine riga.

| Elemento | Forma | Esempi |
|---|---|---|
| intero | cifre, eventuale esponente | `0`, `1`, `987E6` |
| reale | con punto decimale | `0.0`, `0.5`, `2.71E-9` |
| carattere | un carattere ASCII tra apici | `'A'`, `'a'`, `'"'`, `' '` |
| stringa | caratteri tra doppi apici; `""` per inserire `"` | `"Io sono una stringa"` |
| bit string | `B"…"`, `O"…"`, `X"…"`, con `_` facoltativi | `B"1010110"`, `O"126"`, `X"56"` |
| identificatore | lettera iniziale, poi lettere, cifre, `_` non consecutivi | `overflow`, `signal_1` |

Un **identificatore** non può essere una parola riservata (`BEGIN`, `COMPONENT`, `ARCHITECTURE`, …) e gli underscore contano: `questo_segnale` ≠ `questosegnale`.

## Derivazioni

### Derivazione — 86 in binario, ottale ed esadecimale · [[1-Principali elementi sintattici VHDL.pdf#page=4|p. 4]]
**Fonte:** le tre bit string sono date senza conversione, con il numero di bit di ciascuna.
**Si parte da:** il valore di una cifra in base $b$ in posizione $k$ vale $c_k\,b^k$.

| Notazione | Cifre | Valore | Bit |
|---|---|---|---|
| `B"1010110"` | 1·64 + 0·32 + 1·16 + 0·8 + 1·4 + 1·2 + 0·1 | 64 + 16 + 4 + 2 = 86 | 7 (una per cifra binaria) |
| `O"126"` | 1·64 + 2·8 + 6·1 | 64 + 16 + 6 = 86 | 9 (3 bit per cifra ottale: `001 010 110`) |
| `X"56"` | 5·16 + 6·1 | 80 + 6 = 86 | 8 (4 bit per cifra esadecimale: `0101 0110`) |

**Verifica:** le tre espansioni in bit danno lo stesso numero con zeri iniziali diversi: `1010110`, `001010110`, `01010110`.
**Perché la lunghezza cambia:** la bit string ottale produce sempre un multiplo di 3 bit e quella esadecimale un multiplo di 4, anche se le cifre iniziali sono zeri. Se la si assegna a un vettore, la lunghezza deve coincidere con quella del vettore.

### Derivazione — la stringa con le virgolette · [[1-Principali elementi sintattici VHDL.pdf#page=3|p. 3]]
**Fonte:** `"Io sono la stringa ""stringa"" e voi? "` è data con il suo contenuto.

| Nel sorgente | Nella stringa |
|---|---|
| `"` iniziale e finale | delimitatori, non fanno parte del contenuto |
| `""` | un solo carattere `"` |

Quindi il contenuto è `Io sono la stringa "stringa" e voi? ` (con lo spazio finale), lungo 36 caratteri: ogni `""` del sorgente conta come un carattere.

## Spiegazione

Le regole lessicali sono quasi tutte «permissive» (case insensitive, formato libero), con due eccezioni da ricordare: gli underscore negli identificatori sono significativi e non possono essere consecutivi, e le bit string hanno una lunghezza che dipende dalla base usata. Le slide scrivono le parole chiave in maiuscolo solo per leggibilità.

Il commento `--` vale fino a fine riga: non esiste un commento su più righe, quindi un blocco si commenta riga per riga.

## Perché importa

Le bit string si usano di continuo per inizializzare vettori e memorie (vedi la ROM di [[array-vhdl]], scritta con `x"0"` … `x"f"`). Sbagliare il numero di bit di una costante esadecimale o ottale rispetto al vettore di destinazione è un errore di compilazione frequente.

## Connessioni

- [[tipi-vhdl]] — numeri e caratteri sono valori di tipi scalari (`integer`, `real`, `character`)
- [[array-vhdl]] — stringhe e bit string sono array (di caratteri e di bit)
- [[oggetti-vhdl]] — gli identificatori danno il nome agli oggetti

## Fonti · [[1-Principali elementi sintattici VHDL.pdf#page=2|p. 2]]–[[1-Principali elementi sintattici VHDL.pdf#page=5|5]]

- [[elementi-sintattici-vhdl-lezione]]

_Aggiornato: 2026-11-22 — creazione_
