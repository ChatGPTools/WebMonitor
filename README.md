# WebMonitor

## Introduzione
WebMonitor è uno strumento Python potente e flessibile progettato per aiutarti a tenere traccia delle modifiche nelle pagine web di tuo interesse. Utilizzando tecniche di differenziazione testuale e richieste HTTP, WebMonitor può rilevare automaticamente le modifiche al contenuto di una pagina web e salvare queste modifiche in file di testo, permettendoti di mantenere un archivio delle modifiche nel tempo.

## Caratteristiche
- **Monitoraggio Automatico**: Configura WebMonitor per controllare le modifiche a una o più pagine web a intervalli regolari.
- **Salvataggio Differenze**: Salva solo le modifiche tra la versione corrente e l'ultima versione controllata, rendendo semplice vedere cosa è cambiato.
- **Configurazione Flessibile**: Scegli l'intervallo di tempo tra i controlli e la cartella di destinazione per i file di log.
- **Interfaccia Utente Semplice**: Grazie alla sua interfaccia grafica, configurare e utilizzare WebMonitor è estremamente semplice anche per chi non ha esperienza di programmazione.
- **Notifiche in Tempo Reale**: Ricevi log delle modifiche in tempo reale direttamente nell'interfaccia dell'applicazione.

## Requisiti
- Python 3.6+
- Moduli Python: `requests`, `tkinter`, `hashlib`, `difflib`, `threading`

## Installazione
1. Clona questo repository o scarica il codice sorgente.
2. Assicurati di avere Python 3.6 o versioni successive installato sul tuo sistema.
3. Installa le dipendenze necessarie utilizzando pip:
   
```bash
pip install requests
```

Nota: `tkinter` è incluso nella maggior parte delle installazioni standard di Python.

## Utilizzo
1. Avvia `WebMonitor` eseguendo lo script Python:
   
```bash
python webmonitor.py
```

2. Inserisci l'URL della pagina da monitorare, l'intervallo di tempo tra i controlli e seleziona la cartella dove desideri salvare i log delle modifiche.
3. Clicca su "Avvia Monitoraggio" per iniziare a monitorare la pagina. I file di log verranno salvati nella cartella specificata ogni volta che viene rilevata una modifica.

## Contribuire
Sei interessato a migliorare WebMonitor? Le pull request sono benvenute! Per modifiche maggiori, ti preghiamo di aprire prima un'issue per discutere cosa vorresti cambiare.

## Licenza
Distribuito sotto la licenza MIT. Vedi `LICENSE` per più informazioni.
