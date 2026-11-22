---
tipo: concetto
importanza_esame: media
prerequisiti: ["process-vhdl", "testbench"]
fonti_pdf: ["5-Descrizione Comportamentale.pdf#page=27"]
---

# ASSERT

## Definizione · [[5-Descrizione Comportamentale.pdf#page=27|p. 27]]

L'istruzione **`ASSERT`** controlla una condizione durante la simulazione e, se è **falsa**, fa riportare un messaggio dal simulatore. Si usa sia come statement **sequenziale** (in un process) sia **concorrente** (nell'architecture).

```vhdl
ASSERT condition REPORT messagge SEVERITY severity_level;
```

- il messaggio compare quando vale `NOT(condition)`;
- `severity_level` è `NOTE`, `WARNING`, `ERROR` o `FAILURE` e può fermare o meno la simulazione.

## Derivazioni

### Derivazione — un testbench che verifica da solo · [[5-Descrizione Comportamentale.pdf#page=27|p. 27]]
**Fonte:** sintassi dell'`ASSERT`; il testbench del nibble comparator (Lezione 3) controllava le uscite «a occhio».
> 🧩 Derivazione mia: come si aggiunge la verifica automatica a uno dei casi di test di [[testbench]].

```vhdl
PROCESS
BEGIN
  WAIT FOR 600 NS;                        -- dopo il pattern applicato a 500 ns (a = 1111, b = 1110)
  ASSERT gtr = '1' AND eql = '0' AND lss = '0'
    REPORT "errore: atteso a > b a 500 ns"
    SEVERITY ERROR;
  WAIT;
END PROCESS;
```

Il controllo si fa a 600 ns, dopo il ritardo massimo del comparatore (48 ns): se le uscite non sono quelle attese, il simulatore stampa il messaggio. È il terzo compito del testbench elencato nella Lezione 3: **verificare** che le uscite siano corrette.

## Spiegazione

L'`ASSERT` trasforma il testbench da generatore di stimoli a strumento di verifica: invece di leggere le forme d'onda, si scrivono le aspettative e il simulatore segnala solo le violazioni. `ERROR` e `FAILURE` servono per i guasti veri, `NOTE` e `WARNING` per messaggi informativi (ad es. «fine dei test»).

## Perché importa

Utile nei testbench dei progetti d'esame per mostrare che il DUT rispetta le specifiche.

## Connessioni

- [[testbench]] — il luogo naturale degli assert
- [[process-vhdl]], [[wait-e-sensitivity-list]] — assert sequenziali nei process con `WAIT`

## Fonti · [[5-Descrizione Comportamentale.pdf#page=27|p. 27]]

- [[descrizione-comportamentale-lezione]]

_Aggiornato: 2026-11-22 — creazione_
