<!-- nv-language-navigation:start -->
🌐 [English](../../../../NVMFG-Unlock40/README.md) | [Français](../../../../NVMFG-Unlock40/README.fr.md) · [NV Laboratory](../README.md)

<details>
<summary>🌐 Language · 34</summary>

[العربية](../../ar/NVMFG-Unlock40/README.md) · [বাংলা](../../bn/NVMFG-Unlock40/README.md) · [简体中文](../../zh/NVMFG-Unlock40/README.md) · [Čeština](../../cs/NVMFG-Unlock40/README.md) · [Dansk](../../da/NVMFG-Unlock40/README.md) · [Nederlands](../../nl/NVMFG-Unlock40/README.md) · [English](../../../../NVMFG-Unlock40/README.md) · [Filipino](../../fil/NVMFG-Unlock40/README.md) · [Suomi](../../fi/NVMFG-Unlock40/README.md) · [Français](../../../../NVMFG-Unlock40/README.fr.md) · [Deutsch](../../de/NVMFG-Unlock40/README.md) · [Ελληνικά](../../el/NVMFG-Unlock40/README.md) · [हिन्दी](../../hi/NVMFG-Unlock40/README.md) · [Magyar](../../hu/NVMFG-Unlock40/README.md) · [Bahasa Indonesia](../../id/NVMFG-Unlock40/README.md) · **Italiano** · [日本語](../../ja/NVMFG-Unlock40/README.md) · [한국어](../../ko/NVMFG-Unlock40/README.md) · [मराठी](../../mr/NVMFG-Unlock40/README.md) · [فارسی](../../fa/NVMFG-Unlock40/README.md) · [Polski](../../pl/NVMFG-Unlock40/README.md) · [Português](../../pt/NVMFG-Unlock40/README.md) · [ਪੰਜਾਬੀ](../../pa/NVMFG-Unlock40/README.md) · [Română](../../ro/NVMFG-Unlock40/README.md) · [Русский](../../ru/NVMFG-Unlock40/README.md) · [Español](../../es/NVMFG-Unlock40/README.md) · [Kiswahili](../../sw/NVMFG-Unlock40/README.md) · [Svenska](../../sv/NVMFG-Unlock40/README.md) · [தமிழ்](../../ta/NVMFG-Unlock40/README.md) · [ไทย](../../th/NVMFG-Unlock40/README.md) · [Türkçe](../../tr/NVMFG-Unlock40/README.md) · [Українська](../../uk/NVMFG-Unlock40/README.md) · [اردو](../../ur/NVMFG-Unlock40/README.md) · [Tiếng Việt](../../vi/NVMFG-Unlock40/README.md)

[Translation policy](../../README.md)

</details>
<!-- nv-language-navigation:end -->

<!-- nv-translation-notice:start -->
> Traduzione assistita da macchina dall'inglese. Nomi tecnici, comandi, URL e testi legali originali vengono conservati. È gradita la recensione da parte di madrelingua; consultare il riferimento inglese se la formulazione non è chiara.
<!-- nv-translation-notice:end -->

<a id="nvmfg-unlock40"></a>
# NVMFG Unlock40

**NVIDIA Multi Frame Generation sperimentale per GeForce RTX 40, con un controller centrale e scelte per gioco.**

[Scarica 0.1.1 e stato](../docs/downloads.md#nvmfg-unlock40) · [Installazione](#installation) · [A monte](#upstream-and-modifications) · [Licenze](LICENSES/README.md)

<a id="overview-and-purpose"></a>
## Panoramica e scopo

NVMFG Unlock40 è un'applicazione sviluppata in modo indipendente da 禅堂 Zendo (RevoluSound Team). Combina un controller Windows, un livello nativo, un helper del profilo e la gestione del gioco/Streamline SDK. Si rivolge ai giochi che già integrano NVIDIA DLSS Frame Generation e runtime NVIDIA compatibili.

[RTX40MFG-Unlock](https://github.com/dashdogy/RTX40MFG-Unlock) è stato consultato per confrontare e perfezionare il lavoro. L'attuale livello nativo contiene componenti condivisi e adattati, accreditati individualmente di seguito. Questo riferimento non rende l'intera applicazione NVMFG un fork di quel progetto.

Esiste per coordinare centralmente il comportamento sperimentale di MFG, ricordare le scelte specifiche del gioco e mantenere visibili gli aggiornamenti e i backup di runtime. Non aggiunge DLSS Frame Generation a ogni gioco né converte un'implementazione FSR arbitraria.

Il candidato preparato è **0.1.1**, inclusa la correzione visiva dell'elenco SDK registrata internamente come UI2. La versione pubblica rimane 0.1.1; i suoi hash esatti distinguono questo candidato dalle build locali più vecchie.

<a id="features"></a>
## Caratteristiche

- Controllo centrale di attivazione/disattivazione e avvio opzionale del vassoio Windows.
- Selezione per gioco tra Dynamic MFG, impostazioni del gioco e moltiplicatori fissi supportati.
- Scelte ricordate separate per gli stati di attivazione/disattivazione V-Sync osservati.
- Dynamic utilizza la modalità di NVIDIA; viene sospeso quando V-Sync è disattivato, con una scelta di gioco/fissa separata.
- Guida al menu di gioco ed esclusioni persistenti; i giochi senza DLSS FG mantengono il controllo.
- Scoperta di giochi, selezione della cartella principale, ricerca, raggruppamento e rimozione senza eliminare i file di gioco.
- Streamline Download/importazione di SDK, cache locale verificata, selezione esplicita, backup e ripristino per gioco.
- Verifica del provider nativo, diagnostica per sessione, journal del profilo globale e ripristino in presenza di conflitti.
- 34 lingue di interfaccia e quattro temi.

Disattivare FG nel gioco lo mantiene disattivato. Le scelte fisse da 2x a 6x dipendono dal gioco/menu/runtime; non sono una promessa che ogni combinazione funzioni. Il controller osserva V-Sync e non imposta V-Sync o VRR per l'utente.

<a id="compatibility"></a>
## Compatibilità

| Requisito | Dettagli |
| --- | --- |
| Sistema | Windows 10/11 x64 |
| GPU | GeForce RTX 40 destinazione; nessuna richiesta di compatibilità universale GPU |
| Gioco | Integrazione NVIDIA DLSS Frame Generation esistente e runtime supportato; nessuna certificazione di compatibilità anti-cheat |
| Fornitore | Il candidato è associato al provider SHA-256 documentato in [provenienza](../docs/provenance.md); gli hash sconosciuti vengono rifiutati |
| Durata | .NET 8/WPF 8.0.30 in bundle per app/agente; .NET Framework 4.8 per gli helper dei profili |
| Autorizzazioni | Accesso amministratore per le operazioni del controller/profilo |
| Rete | Richiesto per i download ufficiali SDK selezionati; SDKs compatibile importato può essere memorizzato nella cache locale |
| Binari esterni | Il driver NVIDIA, il provider/modelli NGX e i runtime dei giochi Streamline non sono inclusi in bundle |

Un'etichetta di versione da sola non è sufficiente: driver, hash del provider, integrazione del gioco e moduli effettivamente caricati contano. Processi protetti o incompatibili possono rifiutare il sequestro. L'applicazione non è progettata per eludere le protezioni anti-cheat.

<a id="installation"></a>
## Installazione

1. Leggi [stato del candidato e nota di licenza](../docs/downloads.md#nvmfg-unlock40).
2. Scarica `NVMFGUnlock40-0.1.1-Setup-x64.exe` o `NVMFGUnlock40-0.1.1-Portable-x64.zip` quando la sua versione sarà disponibile.
3. Controllare SHA-256 e conservare gli avvisi allegati. Installa .NET Framework 4.8 se Windows non lo fornisce già.
4. Esegui il programma di installazione o estrai l'**intero** ZIP portatile in una cartella locale scrivibile.
5. Avvia `NVMFGUnlock40.exe`; mantenere `agent`, `driver`, `engine` e `Licenses` nel layout fornito.

La cartella denominata `driver` contiene helper dello spazio utente, non un driver del kernel. Non copiare solo l'EXE principale o sostituire l'hash del provider per forzare la compatibilità. Gli EXE correnti non sono firmati.

<a id="usage"></a>
## Utilizzo

1. Inizia con il controller disabilitato. Aggiungi un gioco o una cartella principale e scegli le installazioni effettive.
2. Controlla le impostazioni MFG di ciascun gioco. Rispondi a ciò che offre il suo menu; la risposta viene memorizzata per gioco.
3. Scegli Dynamic o l'impostazione di gioco a livello globale, quindi modifica le scelte idonee per gioco secondo necessità.
4. Abilita il controller solo quando intendi utilizzarlo. Può modificare temporaneamente sei impostazioni globali del profilo NVIDIA, con un journal di ripristino.
5. Avvia un gioco idoneo e abilita il proprio DLSS Frame Generation. Seguire qualsiasi richiesta per la scelta V-Sync-off.
6. Utilizza le esclusioni per i giochi che non desideri gestire. La rimozione di un gioco registra un'esclusione e ne preserva i file/backup.
7. Al termine, utilizzare il flusso completo di chiusura/disattivazione e ripristino dell'applicazione.

La chiusura della finestra principale può lasciare il controller nel vassoio. Una DLL già caricata in un gioco rimane lì finché il gioco non esce; disabilitare il controller non è una garanzia di scarico. Chiudi i giochi interessati prima della manutenzione o degli aggiornamenti.

**Streamline SDKs:** nella pagina NVIDIA SDK, scarica una versione ufficiale o importa un SDK locale compatibile. L'importazione memorizza una copia verificata; **Use this version** lo seleziona e **Uninstall** rimuove la copia memorizzata nella cache. Le DLL Streamline mancanti possono essere integrate da un NVIDIA SDK ufficiale, con la fonte mostrata. Questo non scarica/sostituisce un modello NGX. Chiudi il gioco, seleziona l'aggiornamento del gioco desiderato e conserva il backup originale. Per ripristinare i file di gioco, utilizza il ripristino del backup, non il pulsante Uninstall della cache.

<a id="screenshots"></a>
## Schermate

![Anteprima dell'elenco NVMFG SDK](../../../../assets/screenshots/nvmfg-0.1.1-sdk-preview.png)

Rendering dell'interfaccia inglese 0.1.1 esistente con un esempio di inventario SDK. Non è un elenco delle versioni attuali o la prova di un gioco in esecuzione. [Provenienza dell'immagine](../assets/README.md).

<a id="update-and-uninstall"></a>
## Aggiorna e disinstalla

Chiudi i giochi interessati. Disattiva/esci da NVMFG e risolvi qualsiasi ripristino delle impostazioni NVIDIA in sospeso prima dell'aggiornamento. Installa il prossimo Setup con l'identità esistente, oppure estrai il nuovo portatile in una nuova cartella; conservare stato/backup.

Prima della disinstallazione, ripristina i backup SDK del gioco desiderati e le impostazioni NVIDIA tramite l'applicazione, quindi chiudi i giochi ed esci dal controller. Utilizzare Windows **Installed apps** per la configurazione o rimuovere la cartella portatile chiusa dopo aver conservato i file necessari. Non eliminare manualmente un journal di ripristino attivo per sbloccare l'installazione.

I backup locali del runtime del gioco utilizzano `%LOCALAPPDATA%\NvidiaStreamlineMaintenance\Backups`. Impostazioni MFG/dati SDK utilizzano `%LOCALAPPDATA%\RtxMfg`; l'output della sessione si trova in `Sessions` accanto all'applicazione. Questi file possono contenere percorsi di gioco. Non pubblicarli senza revisioni.

<a id="known-limitations"></a>
## Limitazioni note

- Le patch native sperimentali possono causare arresti anomali o artefatti visivi; nella cronologia dello sviluppo viene registrato un arresto anomalo Bodycam irrisolto.
- I test di rendering controllati non sono certificazioni per ogni gioco, driver o anti-cheat.
- I fotogrammi generati non creano nuovi campioni di input; questo hub non promette alcuna latenza misurata o miglioramento delle prestazioni.
- Più strumenti/overlay per la generazione di frame potrebbero entrare in conflitto. L'applicazione segnala i moduli osservati senza dimostrare ogni scenario di coesistenza.
- Il manifest di compatibilità è un aiuto per il rilevamento, non un elenco di giochi completamente testati.
- I termini completi di NVIDIA SDK e la restrizione di limitazione tecnica non risolta rimangono documentati in [provenienza](../docs/provenance.md).

<a id="troubleshooting"></a>
## Risoluzione dei problemi

| Sintomo | Azione |
| --- | --- |
| Fornitore non supportato | Conserva i file originali verificati. Segnalare le versioni del driver/provider e l'errore; non ignorare il controllo dell'hash. |
| Nessun FG DLSS nel gioco | Seleziona quella risposta e lascia il controllo del gioco; questo strumento non può produrre tale integrazione. |
| Arresti anomali/artefatti del gioco | Esci dal gioco, disabilita NVMFG, utilizza il backup di runtime originale del gioco se è stato modificato e segnala i dettagli riproducibili. |
| Elenco SDK o download non disponibile | Aggiorna e controlla la fonte ufficiale; una versione memorizzata nella cache/importata deve comunque superare la convalida. |
| Il ripristino NVIDIA in sospeso blocca l'uscita/l'aggiornamento | Utilizzare il ripristino e conservare il diario; i conflitti non devono essere sovrascritti ciecamente. |
| Un gioco rimosso non viene riscoperto | La sua esclusione è persistente. Aggiungilo esplicitamente quando vuoi che venga gestito nuovamente. |

[Guida al supporto condiviso](../docs/support.md) spiega cosa includere in un report.

<a id="faq"></a>
## Domande frequenti

**Include DLL o modelli NVIDIA?** Non è incluso alcun driver, provider/modello NGX o runtime Streamline. I download espliciti di SDK provengono da NVIDIA.

**Dynamic funziona con V-Sync spento?** È sospeso in quello stato. Scegli l'impostazione di gioco o un moltiplicatore fisso idoneo per lo stato separato di quel gioco.

**Si tratta di un pacchetto ReShade/OptiScaler/FSR?** No. Questi non sono compilati o spediti come parte di questo pacchetto di produzione.

**I sorgenti modificati sono pubblici?** No. Vengono forniti i pacchetti compilati e i crediti/licenze richiesti. Ciò non elimina i diritti o le restrizioni di terzi.

<a id="upstream-and-modifications"></a>
## A monte e modifiche

Riferimento di confronto e componenti nativi condivisi: **RTX40MFG-Unlock di Michael Robles / dashdogy**, commit di riferimento `4e776d068f91b4a665425542bb005dd57cc3d891`, MIT. [Deposito](https://github.com/dashdogy/RTX40MFG-Unlock) · [Download originali](https://github.com/dashdogy/RTX40MFG-Unlock/releases).

Il confronto delle fonti identifica patch condivise, gestione provider/policy, correzioni temporali e componenti di deviazione basati su MinHook. Gli avvisi MIT e BSD vengono conservati. Il confronto completo include anche i file esterni al target di produzione.

L'applicazione desktop, il controller e il flusso di lavoro di gestione di SDK sono sviluppati da 禅堂 Zendo (RevoluSound Team). Il lavoro del progetto include il caricamento centrale, l'integrazione del bootstrap NGX, la selezione del provider verificato, il coordinamento del gioco/V-Sync e la diagnostica della sessione. La guida sulla provenienza separa quell'opera dalle componenti condivise; il solo confronto dei file non stabilisce quando uno degli autori ha avuto l'idea.

L'helper del profilo adatta il wrapper MIT NVAPI da Profile Inspector di Orbmu2k. [Provenienza dettagliata e ambito dei componenti](../docs/provenance.md).

<a id="credits-and-license"></a>
## Crediti e licenza

Michael Robles; Orbmu2k; Collaboratori di Tsuda Kageyu e HDE; NVIDIA Corporation; Microsoft e collaboratori; Inno Setup autori e traduttori. Sviluppo, integrazioni e packaging dell'applicazione: 禅堂 Zendo (RevoluSound Team).

[autorizzazione di condivisione del pacchetto compilato esistente](../../../../NVMFG-Unlock40/LICENSE) e tutti gli [licenze dei componenti](LICENSES/README.md) vengono conservati. Le autorizzazioni MIT per il codice upstream sono distinte dai termini NVIDIA SDK. Nessuna licenza generale li sostituisce.

Indipendente da, non sponsorizzato e non ufficialmente approvato da NVIDIA Corporation. Tutti i marchi citati rimangono di proprietà dei rispettivi proprietari.
