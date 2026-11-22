---
tipo: concetto
importanza_esame: alta
prerequisiti: ["process-vhdl"]
fonti_pdf: ["5-Descrizione Comportamentale.pdf#page=20", "5-Descrizione Comportamentale.pdf#page=21", "5-Descrizione Comportamentale.pdf#page=22", "5-Descrizione Comportamentale.pdf#page=23", "5-Descrizione Comportamentale.pdf#page=24", "5-Descrizione Comportamentale.pdf#page=25", "5-Descrizione Comportamentale.pdf#page=26"]
---

# Istruzioni sequenziali: IF, CASE, FOR, WHILE

## Definizione · [[5-Descrizione Comportamentale.pdf#page=20|p. 20]]–[[5-Descrizione Comportamentale.pdf#page=26|26]]

Dentro un process si usano istruzioni di controllo come in un linguaggio di programmazione:

| Istruzione | Quando usarla | Note |
|---|---|---|
| `IF … THEN … ELSIF … ELSE … END IF;` | casi **non** mutuamente esclusivi, con **priorità** | `ELSIF` ed `ELSE` facoltativi |
| `CASE sel IS WHEN … => … END CASE;` | casi **mutuamente esclusivi** | i casi devono essere esaustivi, altrimenti `WHEN OTHERS`; implementa qualsiasi tabella di verità |
| `FOR i IN range LOOP … END LOOP;` | numero di iterazioni fissato | `i` è una costante nel loop e non esiste fuori |
| `WHILE cond LOOP … END LOOP;` | finché vale una condizione | |
| `EXIT` / `NEXT` | in `FOR` e `WHILE` | `EXIT` esce dal loop, `NEXT` passa alla prossima iterazione |

Sono le versioni sequenziali dell'assegnazione condizionata (`IF`) e selezionata (`CASE`) della descrizione dataflow.

## Derivazioni

### Derivazione — la tabella della XOR a 3 ingressi · [[5-Descrizione Comportamentale.pdf#page=23|p. 23]]
**Fonte:** i valori del `CASE` sono dati senza spiegazione.
**Si parte da:** lo XOR di più bit vale 1 se il numero di bit a 1 è **dispari**.

| x | bit a 1 | Parità | y |
|---|---|---|---|
| 000 | 0 | pari | 0 |
| 001 | 1 | dispari | 1 |
| 010 | 1 | dispari | 1 |
| 011 | 2 | pari | 0 |
| 100 | 1 | dispari | 1 |
| 101 | 2 | pari | 0 |
| 110 | 2 | pari | 0 |
| 111 | 3 | dispari | 1 |

Tutti gli 8 valori della slide sono corretti. Il `WHEN OTHERS => y <= 'X'` copre le combinazioni con valori `std_logic` diversi da `'0'` e `'1'` (`"0Z1"`, `"UUU"`, …): sono $9^3 - 2^3 = 729 - 8 = 721$ casi, che danno uscita «sconosciuta». Vedi [[porta-xor]].

### Derivazione — la XOR a N bit con il `FOR LOOP` · [[5-Descrizione Comportamentale.pdf#page=25|p. 25]]
**Fonte:** codice dato; qui la traccia con N = 4, x = "1011".

| Passo | i | x(i) | cnt |
|---|---|---|---|
| inizio | — | — | 0 |
| 1 | 0 | 1 | 1 |
| 2 | 1 | 1 | 2 |
| 3 | 2 | 0 | 2 |
| 4 | 3 | 1 | 3 |

$3 \bmod 2 = 1$ → `y <= '1'`. Verifica: $1 \oplus 0 \oplus 1 \oplus 1 = 1$ ✓.

**Perché `cnt` è una variabile:** viene letta subito dopo ogni incremento; con un segnale ogni `cnt <= cnt + 1` leggerebbe sempre il valore iniziale e conterebbe al massimo 1 (vedi [[variabili-e-segnali]]).
**Il loop è hardware:** con N fissato dal generic, il sintetizzatore «srotola» il ciclo in N stadi; `i` è una costante per ogni copia.
> 🧩 Derivazione mia: la traccia e le due osservazioni.

> ⚠️ Contraddizione: nel codice della slide l'architecture è `OF Function_3` (l'entity è `XOR_N`), mancano gli apici dei letterali e `CASE (cnt MOD 2)` su un `INTEGER` richiede `WHEN OTHERS` per essere esaustivo; nella XOR a 3 ingressi il `CASE` è chiuso da `END IF`.

### Derivazione — IF con priorità contro CASE · [[5-Descrizione Comportamentale.pdf#page=21|p. 21]]–[[5-Descrizione Comportamentale.pdf#page=22|22]]
**Fonte:** «IF quando i casi non sono mutuamente esclusivi e si vuole una priorità; CASE quando lo sono».
> 🧩 Derivazione mia: esempio con due richieste `r1`, `r2`.

```vhdl
IF r1 = '1' THEN g <= "01";        -- r1 ha priorità
ELSIF r2 = '1' THEN g <= "10";
ELSE g <= "00";
END IF;
```

Con `r1 = r2 = '1'` entrambe le condizioni sono vere: vince la prima (`g = "01"`). Con un `CASE` sulla concatenazione `r1 & r2` bisognerebbe elencare esplicitamente `"11"` e decidere cosa farne: lo stesso circuito, ma la priorità va scritta a mano.

## Spiegazione

Le istruzioni sequenziali danno l'espressività di un linguaggio di programmazione, ma descrivono comunque hardware: un `IF` diventa una catena di multiplexer con priorità, un `CASE` un multiplexer comandato dal selettore, un `FOR` con limiti costanti N copie di una struttura. Un `WHILE` con un numero di iterazioni non noto a priori in genere non è sintetizzabile e si usa nei testbench.

## Perché importa

Macchine a stati (`CASE` sullo stato), decodifiche, priorità, contatori di bit: sono le istruzioni con cui si scrive la logica nei process dei progetti.

## Connessioni

- [[process-vhdl]] — il contenitore delle istruzioni sequenziali
- [[assegnazione-condizionata]], [[assegnazione-selezionata]] — gli equivalenti concorrenti di `IF` e `CASE`
- [[variabili-e-segnali]] — contatori e risultati intermedi
- [[generics-vhdl]] — N fissato dal generic
- [[porta-xor]] — gli esempi della lezione

## Fonti · [[5-Descrizione Comportamentale.pdf#page=20|p. 20]]–[[5-Descrizione Comportamentale.pdf#page=26|26]]

- [[descrizione-comportamentale-lezione]]

_Aggiornato: 2026-11-22 — creazione_
