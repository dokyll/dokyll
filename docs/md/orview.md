# Dokyll a colpo d'occhio

Dokyll è un generatore di siti statici leggero che trasforma i tuoi progetti in pagine web pronte da pubblicare.

È pensato per essere semplice, veloce e facilmente estendibile.

## Cosa fa

- Costruisce siti statici da una struttura di progetto
- Converte i file in pagine web
- Organizza automaticamente i contenuti
- Gestisce più progetti
- Funziona da linea di comando

## Come funziona

Dokyll legge una cartella progetto e genera un sito statico a partire dai suoi file.

Esempio:

```bash
dokyll build-pages mio-sito
```

Il comando elabora il progetto e crea `mio-sito.dok`, la build di Dokyll.
Con questo file il sito è pronto per essere pubblicato.

## Perché usarlo

- Leggero e veloce
- Utilizzabile offline
- Facile da estendere
- Adatto a siti statici
- Semplice da usare da terminale
- Nessun liminte di dimensioni, file o altro.

## Usi interessanti

Dokyll non si limita ai siti web: può costruire qualsiasi progetto basato su file.

Un esempio è una build di tipo [Read the Docs](https://readthedocs.org).
La struttura tipica è:

```text
📄 .readthedocs.yaml
📁 docs
    📄 conf.py
    📄 index.rst
```

Dokyll prende tutti i file presenti nella cartella e li include nella build finale, mantenendo la struttura originale.

Questo significa che la build contiene esattamente gli stessi file del progetto, pronti per essere distribuiti o elaborati da altri strumenti.