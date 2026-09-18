<!-- nv-language-navigation:start -->
🌐 [English](../../../../NVRasterPulse/README.md) | [Français](../../../../NVRasterPulse/README.fr.md) · [NV Laboratory](../README.md)

<details>
<summary>🌐 Language · 34</summary>

[العربية](../../ar/NVRasterPulse/README.md) · [বাংলা](../../bn/NVRasterPulse/README.md) · [简体中文](../../zh/NVRasterPulse/README.md) · [Čeština](../../cs/NVRasterPulse/README.md) · [Dansk](../../da/NVRasterPulse/README.md) · [Nederlands](../../nl/NVRasterPulse/README.md) · [English](../../../../NVRasterPulse/README.md) · [Filipino](../../fil/NVRasterPulse/README.md) · [Suomi](../../fi/NVRasterPulse/README.md) · [Français](../../../../NVRasterPulse/README.fr.md) · [Deutsch](../../de/NVRasterPulse/README.md) · [Ελληνικά](../../el/NVRasterPulse/README.md) · [हिन्दी](../../hi/NVRasterPulse/README.md) · [Magyar](../../hu/NVRasterPulse/README.md) · [Bahasa Indonesia](../../id/NVRasterPulse/README.md) · **Italiano** · [日本語](../../ja/NVRasterPulse/README.md) · [한국어](../../ko/NVRasterPulse/README.md) · [मराठी](../../mr/NVRasterPulse/README.md) · [فارسی](../../fa/NVRasterPulse/README.md) · [Polski](../../pl/NVRasterPulse/README.md) · [Português](../../pt/NVRasterPulse/README.md) · [ਪੰਜਾਬੀ](../../pa/NVRasterPulse/README.md) · [Română](../../ro/NVRasterPulse/README.md) · [Русский](../../ru/NVRasterPulse/README.md) · [Español](../../es/NVRasterPulse/README.md) · [Kiswahili](../../sw/NVRasterPulse/README.md) · [Svenska](../../sv/NVRasterPulse/README.md) · [தமிழ்](../../ta/NVRasterPulse/README.md) · [ไทย](../../th/NVRasterPulse/README.md) · [Türkçe](../../tr/NVRasterPulse/README.md) · [Українська](../../uk/NVRasterPulse/README.md) · [اردو](../../ur/NVRasterPulse/README.md) · [Tiếng Việt](../../vi/NVRasterPulse/README.md)

[Translation policy](../../README.md)

</details>
<!-- nv-language-navigation:end -->

<!-- nv-translation-notice:start -->
> Traduzione assistita da macchina dall'inglese. Nomi tecnici, comandi, URL e testi legali originali vengono conservati. È gradita la recensione da parte di madrelingua; consultare il riferimento inglese se la formulazione non è chiara.
<!-- nv-translation-notice:end -->

<a id="nvrasterpulse"></a>
# NVRasterPulse

**Limiti FPS per applicazione tramite RivaTuner Statistics Server.**

> **Installa prima RTSS.** NVRasterPulse richiede [RivaTuner Statistics Server (RTSS), scaricato da Guru3D](https://www.guru3d.com/download/rtss-rivatuner-statistics-server-download/). RTSS deve essere in esecuzione per applicare i limiti. Nessun programma di installazione RTSS, hook DLL o SDK è in bundle.

[Scarica 0.2 e stato](../docs/downloads.md#nvrasterpulse) · [Installazione](#installation) · [Come funzionano i limiti](#usage) · [Licenza](../../../../NVRasterPulse/LICENSE)

<a id="overview-and-purpose"></a>
## Panoramica e scopo

NVRasterPulse è un'interfaccia Windows compatta per la gestione dei limiti dei frame RTSS in base al nome dell'eseguibile. RTSS esegue la limitazione. NVRasterPulse gestisce i valori del profilo corrispondente, i backup e le richieste di ricarica, con accesso al vassoio e scelte persistenti.

Esiste per rendere più semplice la modifica dei limiti esatti per gioco senza sostituire un intero profilo RTSS o disturbare le sue impostazioni di sovrapposizione. La versione **0.2** aggiunge la diagnostica della configurazione, un helper FPS, pausa, annullamento e condivisione del profilo.

<a id="features"></a>
## Caratteristiche

- Seleziona un'applicazione in esecuzione o aggiungine manualmente l'eseguibile.
- Salva i limiti FPS da 1 a 1000, con un massimo di tre cifre decimali.
- Codifica razionale esatta dei valori inseriti: 59.94 diventa 2997/50.
- Configurazione Front Edge Sync (`SyncLimiter=1`) con attesa attiva (`PassiveWait=0`).
- Aggiornamenti del profilo per eseguibile, backup automatici e scritture atomiche.
- Rimozione delle sostituzioni del limitatore mantenendo altri contenuti del profilo.
- Rilevamento dell'installazione di RTSS, selezione manuale del percorso e avvio/ricaricamento esplicito.
- Funzionamento del vassoio a istanza singola, avvio installato opzionale, 34 lingue e quattro temi.
- Separare le azioni normali di uscita e **Esci + RTSS**.

<a id="compatibility"></a>
## Compatibilità

| Requisito | Dettagli |
| --- | --- |
| Sistema | Windows 10/11 x64 |
| Durata | [.NET Framework 4.8](https://dotnet.microsoft.com/en-us/download/dotnet-framework/net48), installato separatamente se necessario |
| Software richiesto | RTSS con `RTSS.exe`, una directory `Profiles` corrispondente e supporto profilo/ricarica compatibile |
| GPU | La compatibilità RTSS determina il limitatore; questo gestore profili non richiede una particolare generazione RTX |
| Autorizzazioni | L'applicazione corrente richiede l'accesso come amministratore; la cartella del profilo RTSS selezionata deve essere accessibile |
| Giochi | Dipende dal supporto dell'hook RTSS e dalle restrizioni di ciascun gioco; nessuna garanzia anti-cheat |

Nessuna versione minima RTSS specifica è stata certificata per ogni funzione da questo audit dell'hub. Utilizza la distribuzione ufficiale corrente e segnala la versione esatta se una chiave/ricarica del profilo non funziona. RTSS installato ma arrestato supera il controllo di installazione; deve quindi essere avviato per la limitazione effettiva.

<a id="installation"></a>
## Installazione

1. **[Scarica e installa RTSS da Guru3D](https://www.guru3d.com/download/rtss-rivatuner-statistics-server-download/).**
2. Apri [Download di NVRasterPulse](../docs/downloads.md#nvrasterpulse) e controlla la disponibilità della versione.
3. Scarica `NVRasterPulse-0.2-win-x64-Setup.exe` o `NVRasterPulse-0.2-win-x64-portable.zip`, più gli avvisi/checksum.
4. Confronta SHA-256. Esegui il programma di installazione o estrai l'intero ZIP portatile in una cartella locale scrivibile.
5. Apri `NVRasterPulse.exe`. Se manca RTSS, utilizza **Scarica RTSS**, installalo, quindi **Controlla di nuovo** o seleziona `RTSS.exe` manualmente.
6. Avvia RTSS utilizzando la sua normale scorciatoia o il pulsante RTSS di NVRasterPulse se è arrestato.

La disattivazione del promemoria facoltativo non ignora il controllo dei prerequisiti. Un avvio silenzioso del vassoio Windows attende l'apertura della finestra principale prima di visualizzare questo controllo. La configurazione installa solo NVRasterPulse. I suoi EXE non sono firmati.

<a id="usage"></a>
## Utilizzo

1. Seleziona l'applicazione in esecuzione desiderata o accedi al file EXE del gioco.
2. Inserisci un limite compreso tra 1 e 1000 FPS, incluso un valore frazionario se necessario.
3. Salva e controlla il risultato riportato. NVRasterPulse aggiorna il profilo RTSS dell'eseguibile e richiede un ricaricamento.
4. Conferma che RTSS sia in esecuzione e verifica il comportamento nel gioco previsto.

I profili sono codificati dal **nome eseguibile**, come `Game.exe.cfg`. Due cartelle diverse contenenti `Game.exe` condividono lo stesso profilo RTSS; la memorizzazione del percorso completo non rimuove questa collisione.

Il salvataggio utilizza la sincronizzazione Front Edge e l'attesa attiva. L'attesa attiva può aumentare l'utilizzo di CPU. I campi `LimitTime` alternativi vengono neutralizzati. I commenti esistenti, le impostazioni di sovrapposizione e `EnableHooking=0` vengono conservati. Il profilo globale RTSS non viene modificato.

Utilizza l'azione cestino per rimuovere le sostituzioni del limitatore di NVRasterPulse. Non elimina l'intero profilo RTSS. Un limite ereditato da RTSS Global o da un altro strumento potrebbe comunque applicarsi in seguito.

**Chiusura e uscita:** la finestra principale può nascondersi nel vassoio. Normale **Esci** lascia RTSS in esecuzione e i limiti salvati intatti. **Esci + RTSS** richiede una chiusura normale del processo RTSS corrispondente nella sessione corrente, attende fino a otto secondi e non lo interrompe forzatamente. I limiti memorizzati rimangono in entrambi i casi.

La lingua e il tema vengono selezionati nell'app. L'avvio all'accesso Windows è facoltativo e destinato a una copia installata. Il pulsante delle informazioni spiega le azioni comuni.

<a id="diagnostics-and-profile-tools"></a>
## Strumenti di diagnostica e profilo

Apri il menu delle azioni per gli strumenti aggiuntivi. Conservano RTSS Global, impostazioni ed esclusioni di sovrapposizione.

**Diagnostica:** ispeziona i limiti locali/effettivi, RTSS arrestato, un eseguibile mancante, nessuna finestra rilevata, hook disabilitato, ereditarietà, limiti in pausa, impostazioni concorrenti e nomi di eseguibili duplicati. Questo controllo di sola lettura descrive la configurazione; non dimostra che un gioco sia agganciato da RTSS né misura il suo FPS.

**Assistente FPS:** seleziona il display e dichiara tu stesso VRR/G-Sync, V-Sync, Reflex e Frame Generation. La frequenza di aggiornamento arrotondata proviene da Windows. Se Reflex o Frame Generation è attivo o sconosciuto, non viene offerto alcun limite automatico. Per VRR con V-Sync attivato e Reflex/FG disattivato, l'euristica sottrae almeno 3 FPS o circa il 2% della frequenza di aggiornamento. Questo non è un ottimo misurato. L'applicazione del suggerimento riempie la bozza; **Salva** rimane un'azione separata.

**Pausa e riprendi:** sospende il limite del programma selezionato, quindi ripristina i campi limitatore precedenti. Le modifiche contrastanti apportate da un altro strumento impediscono un curriculum ambiguo. Nascondere una voce non ne mette in pausa il limite.

**Annulla:** ripristina l'ultima modifica ai sei campi limitatori gestiti per quel programma. C'è un livello; questo non ripristina tutto RTSS. I cambiamenti esterni contrastanti vengono rifiutati. I backup dei file rimangono separati.

**Condividi profili:** esporta i profili selezionati in un file `.nvrp`. L'importazione mostra un'anteprima e lascia i limiti esistenti deselezionati per impostazione predefinita. Il file contiene solo nomi, limiti e stati degli eseguibili, senza percorsi o script assoluti. Rivedi la tua selezione e fai domanda. Un errore I/O può lasciare alcuni profili già applicati; il risultato li identifica e ciascuno mantiene il suo annullamento. I nomi eseguibili identici si rivolgono ancora allo stesso profilo RTSS.

**Preferiti e voci nascoste:** blocca prima i programmi utili, nascondi le voci indesiderate e ripristinale nella finestra di dialogo dedicata. Queste scelte persistono. Un preferito chiuso non viene visualizzato come applicazione in esecuzione.

<a id="screenshots"></a>
## Schermate

![Anteprima della finestra principale di NVRasterPulse](../../../../assets/screenshots/nvrasterpulse-0.1-preview.png)

Rendering dell'interfaccia utente francese 0.1 esistente con nomi eseguibili di esempio e un valore 176 FPS. RTSS viene visualizzato interrotto; questa è un'illustrazione dell'interfaccia, non un limitatore di funzionamento o una misurazione della latenza. [Provenienza dell'immagine](../assets/README.md).

<a id="update-and-uninstall"></a>
## Aggiorna e disinstalla

Esci da NVRasterPulse, scarica e verifica la nuova versione, quindi esegui la configurazione o estrai il portatile in una nuova cartella. Conserva le impostazioni e i backup RTSS. Gli aggiornamenti RTSS sono separati e provengono da Guru3D.

Per rimuovere una copia installata, utilizzare Windows **Installed apps**. Per i dispositivi portatili, esci e rimuovi la cartella estratta quando i backup sono al sicuro. I limiti RTSS salvati non vengono rimossi disinstallando NVRasterPulse: rimuovere prima le sostituzioni del limitatore previste. RTSS ha il proprio programma di disinstallazione.

Stato locale: `%LOCALAPPDATA%\NVRasterPulse`. Backup automatici RTSS: `%LOCALAPPDATA%\NVRasterPulse\Backups\RTSS`. Una posizione `%LOCALAPPDATA%\RTSSProfileBridge` precedente potrebbe essere letta per la migrazione. Questi file possono contenere percorsi eseguibili personali e non devono essere pubblicati pubblicamente.

<a id="known-limitations"></a>
## Limitazioni note

- RTSS esegue il cap. Un valore salvato o una richiesta di ricarica riuscita non è un risultato del frame-time misurato.
- Gli eseguibili con lo stesso nome condividono un profilo.
- Un altro limitatore globale/per partita può influenzare il risultato; la disabilitazione dell'override locale non rimuove un limite ereditato.
- Un hook RTSS deliberatamente disabilitato rimane disabilitato.
- L'attesa attiva prevede un compromesso tra CPU e potenza.
- Nessun gioco universale, anti-cheat o convalida della latenza end-to-end.
- Il precedente motore limitatore sperimentale indipendente non è stato compilato o spedito.
- I backup automatici non implicano un'interfaccia di backup-ripristino completa con un solo clic.

<a id="troubleshooting"></a>
## Risoluzione dei problemi

| Sintomo | Azione |
| --- | --- |
| Il prerequisito RTSS rimane aperto | Seleziona l'`RTSS.exe` effettivo e la cartella dei profili corrispondente, quindi controlla di nuovo. |
| Limite salvato ma nessun effetto | Avvia RTSS; verificare il corretto profilo EXE/profilo del gioco, i permessi di hook e altri limitatori. |
| Il salvataggio fallisce | Controlla i permessi delle cartelle e conserva l'errore/backup visualizzato. |
| Il limite rimane dopo la rimozione | Ispezionare RTSS Global e altri strumenti; l'azione del cestino rimuove solo le sostituzioni del limitatore locale. |
| Due giochi ricevono lo stesso limite | Controlla se i nomi dei file eseguibili sono identici. |
| Esci + RTSS lascia RTSS aperto | Chiudi RTSS normalmente da solo; questo comando evita deliberatamente la terminazione forzata. |

Se si ripristina manualmente un backup RTSS, chiudere prima RTSS e conservare il profilo corrente prima di sostituirlo con il backup previsto. Ciò può sovrascrivere le modifiche del profilo non correlate; controllare il file e la data. [Supporto condiviso](../docs/support.md).

<a id="faq"></a>
## Domande frequenti

**Ho bisogno anche del postbruciatore MSI?** NVRasterPulse richiede RTSS; non dipende dall'applicazione Afterburner. Seguire le opzioni di installazione del distributore RTSS.

**Posso usarlo senza RTSS in esecuzione?** È possibile gestire i profili una volta rilevata un'installazione, ma RTSS deve essere eseguito per la limitazione.

**L'uscita o la disinstallazione rimuove i cappucci?** No. Rimuovere esplicitamente le sovrascritture del limitatore desiderate prima di rimuovere NVRasterPulse.

**È un fork di RTSS?** No. È un gestore di profili indipendente; non è incorporata alcuna sorgente o eseguibile RTSS.

<a id="upstream-modifications-and-credits"></a>
## A monte, modifiche e crediti

Il repository di sviluppo ha origine da [Orbmu2k's NVIDIA Profile Inspector](https://github.com/Orbmu2k/nvidiaProfileInspector). Le sue tavolozze/risorse dell'interfaccia utente MIT vengono accreditate. I servizi di gestione dei profili, la codifica delle frazioni, i backup, il bridge di ricarica RTSS, il comportamento del vassoio, la guida ai prerequisiti, le lingue e l'icona specifica dell'applicazione sono stati sviluppati/adattati da 禅堂 Zendo (RevoluSound Team).

RTSS è sviluppato da **Unwinder** e distribuito separatamente tramite Guru3D. NVRasterPulse chiama `UpdateProfiles` dalla DLL hook installata selezionata; nessun RTSS SDK o il binario hook vengono ridistribuiti. Il programma di installazione utilizza Inno Setup 7.1.0 non modificato con script/traduzioni adattati e un bootstrap del progetto.

[Provenienza completa](../docs/provenance.md) · [Tabella di terze parti](../THIRD_PARTY_NOTICES.md)

<a id="license"></a>
## Licenza

Il pacchetto distribuisce esplicitamente NVRasterPulse sotto il [Licenza MIT](../../../../NVRasterPulse/LICENSE) fornito, mantenendo il copyright (c) 2016 Orbmu2k. L'origine dell'applicazione viene mantenuta privatamente; MIT non richiede la pubblicazione della fonte modificata. RTSS e Windows/.NET rimangono soggetti alle proprie condizioni. [Avvisi completi](LICENSES/README.md).

Indipendente da NVIDIA Corporation, MSI e RTSS; non sponsorizzati o ufficialmente approvati da loro. I nomi dei prodotti rimangono marchi dei rispettivi proprietari.
