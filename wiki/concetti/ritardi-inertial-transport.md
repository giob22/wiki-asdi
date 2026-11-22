---
tipo: concetto
importanza_esame: alta
prerequisiti: ["modello-tempificazione-vhdl"]
fonti_pdf: ["4-Tecniche di simulazione e ritardi.pdf#page=15", "4-Tecniche di simulazione e ritardi.pdf#page=16"]
---

# Ritardi inertial e transport

## Definizione · [[4-Tecniche di simulazione e ritardi.pdf#page=15|p. 15]]

Le interconnessioni reali, per i parametri parassiti, si comportano come **reti RC** che filtrano gli impulsi troppo brevi rispetto alla costante di tempo RC. Il VHDL ha due modelli di ritardo:

| Modello | Parola chiave | Cosa fa |
|---|---|---|
| **inerziale** | `INERTIAL` | ritarda il segnale e **scarta gli impulsi** (0→1→0, 1→0→1) più brevi di una soglia: definisce sia il ritardo di propagazione sia la durata minima di un impulso per essere propagato |
| **transport** | `TRANSPORT` | ritarda il segnale e **propaga sempre** tutte le transazioni, comunque ravvicinate |

Secondo la slide i ritardi inertial sono poco usati e un ritardo senza parola chiave è `TRANSPORT`.

> ⚠️ Contraddizione: lo standard VHDL dice il contrario: senza parola chiave il ritardo è **inerziale** (con soglia uguale al ritardo); `TRANSPORT` va scritto esplicitamente. `y <= a AFTER 5 NS;` filtra quindi gli impulsi più corti di 5 ns.
> 📚 Fonte esterna: IEEE 1076 (dal VHDL-93 si può anche fissare una soglia diversa con `REJECT`, ad es. `y <= REJECT 2 NS INERTIAL a AFTER 5 NS;`).

![[vhdl-4-p15-rete-rc.png]]
*La rete RC che modella un'interconnessione.*

## Derivazioni

### Derivazione — lettura della figura inertial/transport · [[4-Tecniche di simulazione e ritardi.pdf#page=16|p. 16]]
**Fonte:** figura con `waveform`, `target1` (inertial 5 ns), `target2` (transport 5 ns) e la riga «Difference»; il testo non la commenta.

```vhdl
target1 <= INERTIAL  waveform AFTER 5 NS;
target2 <= TRANSPORT waveform AFTER 5 NS;
```

![[vhdl-4-p16-inertial-transport.png]]
*Impulsi di `waveform` più corti (<5) e più lunghi (>5) di 5 ns.*

| Impulso di `waveform` | Durata | `target2` (transport) | `target1` (inertial, soglia 5 ns) |
|---|---|---|---|
| 1° impulso alto (intorno a 10 ns) | < 5 ns | riprodotto 5 ns dopo | **scartato** |
| 2° impulso alto (intorno a 20–27 ns) | > 5 ns | riprodotto 5 ns dopo | riprodotto 5 ns dopo |
| impulso basso (intorno a 27–35 ns) | > 5 ns | riprodotto | riprodotto |
| 3° impulso alto (da circa 35 ns) | > 5 ns | riprodotto | riprodotto |
| breve impulso basso (intorno a 45 ns) | < 5 ns | riprodotto 5 ns dopo | **scartato**: `target1` resta alto |

La riga **Difference** segna i due intervalli in cui `target1` e `target2` differiscono: proprio dove `target2` riproduce un impulso corto che `target1` ha filtrato (intorno a 12–17 ns e a 50–53 ns).
> 🧩 Derivazione mia: tempi letti sulla scala della figura, che è approssimativa; la regola (corto → scartato solo dall'inerziale) è quella della slide p. 15.

### Derivazione — perché l'inerziale scarta l'impulso corto
> 🧩 Derivazione mia, dal modello transazione (value, time) di [[modello-tempificazione-vhdl]].

Impulso alto da $t_1$ a $t_2$ con $t_2 - t_1 < 5$ ns:
1. a $t_1$ si genera la transazione (1, $t_1 + 5$);
2. a $t_2$, prima che la prima scada, si genera (0, $t_2 + 5$);
3. **transport**: entrambe restano in coda → `target2` sale a $t_1 + 5$ e scende a $t_2 + 5$ (impulso riprodotto);
4. **inertial**: la nuova transazione cancella quella precedente ancora pendente con valore diverso → resta solo (0, $t_2 + 5$), e `target1`, già a 0, non cambia (impulso scartato).

Se invece $t_2 - t_1 > 5$ ns, la prima transazione è già scaduta quando arriva la seconda: i due modelli si comportano allo stesso modo.

## Spiegazione

Il ritardo inerziale modella una **porta reale**: un impulso troppo breve non riesce a caricare la capacità d'ingresso e non commuta l'uscita. Il transport modella una **linea di ritardo ideale** (un filo lungo) che trasmette tutto. Nei design sintetizzabili i ritardi `AFTER` vengono ignorati dal sintetizzatore: contano solo in simulazione (modelli, testbench).

## Perché importa

È una domanda classica: differenza fra i due modelli, quale è il default (attenzione al refuso della slide), come si comportano su un impulso corto.

## Connessioni

- [[modello-tempificazione-vhdl]] — transazioni e loro cancellazione
- [[attributi-vhdl]] — `s'DELAYED(t)` equivale a un ritardo TRANSPORT
- [[simulazione-ad-eventi]]
- [[assegnazione-concorrente]] — le assegnazioni con `AFTER`

## Fonti · [[4-Tecniche di simulazione e ritardi.pdf#page=15|p. 15]]–[[4-Tecniche di simulazione e ritardi.pdf#page=16|16]]

- [[tecniche-di-simulazione-lezione]]

_Aggiornato: 2026-11-22 — creazione_
