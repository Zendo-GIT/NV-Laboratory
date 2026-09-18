<!-- nv-language-navigation:start -->
🌐 [English](../../../support.md) | [Français](../../../support.fr.md) · [NV Laboratory](../README.md)

<details>
<summary>🌐 Language · 34</summary>

[العربية](../../ar/docs/support.md) · [বাংলা](../../bn/docs/support.md) · [简体中文](../../zh/docs/support.md) · [Čeština](../../cs/docs/support.md) · [Dansk](../../da/docs/support.md) · [Nederlands](../../nl/docs/support.md) · [English](../../../support.md) · [Filipino](../../fil/docs/support.md) · [Suomi](../../fi/docs/support.md) · [Français](../../../support.fr.md) · [Deutsch](../../de/docs/support.md) · [Ελληνικά](../../el/docs/support.md) · [हिन्दी](../../hi/docs/support.md) · [Magyar](../../hu/docs/support.md) · [Bahasa Indonesia](../../id/docs/support.md) · **Italiano** · [日本語](../../ja/docs/support.md) · [한국어](../../ko/docs/support.md) · [मराठी](../../mr/docs/support.md) · [فارسی](../../fa/docs/support.md) · [Polski](../../pl/docs/support.md) · [Português](../../pt/docs/support.md) · [ਪੰਜਾਬੀ](../../pa/docs/support.md) · [Română](../../ro/docs/support.md) · [Русский](../../ru/docs/support.md) · [Español](../../es/docs/support.md) · [Kiswahili](../../sw/docs/support.md) · [Svenska](../../sv/docs/support.md) · [தமிழ்](../../ta/docs/support.md) · [ไทย](../../th/docs/support.md) · [Türkçe](../../tr/docs/support.md) · [Українська](../../uk/docs/support.md) · [اردو](../../ur/docs/support.md) · [Tiếng Việt](../../vi/docs/support.md)

[Translation policy](../../README.md)

</details>
<!-- nv-language-navigation:end -->

<!-- nv-translation-notice:start -->
> Traduzione assistita da macchina dall'inglese. Nomi tecnici, comandi, URL e testi legali originali vengono conservati. È gradita la recensione da parte di madrelingua; consultare il riferimento inglese se la formulazione non è chiara.
<!-- nv-translation-notice:end -->

<a id="compatibility-and-troubleshooting"></a>
# Compatibilità e risoluzione dei problemi

Questi sono i candidati preparati, non una matrice di certificazione per tutte le combinazioni Windows, GPU, driver e gioco.

| Strumento | Windows/tempo di esecuzione | Dipendenza hardware/esterna | Operazioni che necessitano di cure |
| --- | --- | --- | --- |
| NVPI fork 3.0.2.3 | Windows 10/11 x64, .NET Framework 4.8 | Driver/display NVIDIA compatibile | Il profilo scrive e visualizza le anteprime |
| NVDriverForge 0.1.4 | Windows 10 build 19041+ / 11x64; .NET/WPF incluso | Pacchetto driver NVIDIA compatibile | Installazione elevata, impostazioni avanzate, NVENC opzionale |
| NVMFG Unlock40 0.2.3 | Windows 10/11x64; .NET/WPF incluso, helper Framework 4.8 | RTX 40, gioco FG DLSS idoneo e provider bloccato | Patch native nel gioco, diario del profilo globale, aggiornamenti del gioco SDK |
| NVRasterPulse 0.2 | Windows 10/11 x64, .NET Framework 4.8 | RTSS installato; correre per i tappi | RTSS modifiche al profilo eseguibile |

Nessun pacchetto ARM64 è preparato. La disponibilità di display/API e le vecchie versioni di Windows possono limitare le singole funzionalità. Non è stata inventata alcuna versione minima universale NVIDIA o RTSS. L'hash esatto del provider NVMFG è in [provenienza](provenance.md).

<a id="before-reporting-a-bug"></a>
## Prima di segnalare un bug

Identifica l'esatto eseguibile/versione che hai aperto. Una copia installata in precedenza non è necessariamente la versione di uno ZIP appena scaricato. Registrare le fasi di riproduzione, il risultato previsto e il risultato effettivo. Per problemi di rendering/limitazione, includi la versione del gioco, l'aggiornamento del display, lo stato FG/V-Sync/VRR e qualsiasi altro limitatore o overlay.

Utilizzare [modulo bug](https://github.com/Zendo-GIT/NV-Laboratory/issues/new?template=bug-report.yml). Non allegare mai un'intera cartella di sviluppo privata, un archivio di driver, un modello, una DLL di gioco, un dump del registro o una raccolta di registri non revisionati.

| Problema | Primi controlli |
| --- | --- |
| Versione dell'applicazione errata | Conferma l'identità EXE e rilascia l'hash; chiudere la copia più vecchia prima della sostituzione. |
| Errore di runtime/avvio | Installa il Framework 4.8 richiesto o conserva tutte le sottocartelle portatili fornite. |
| UAC annullato | Riprovare solo l'operazione prevista; la cancellazione non ha avuto successo nell'installazione. |
| Mancata corrispondenza hash/firma | Smetti di usare quel candidato e ottieni i byte ufficiali attesi. |
| Colore/modalità NVPI rifiutata | Ripristina e utilizza una combinazione supportata dal display/driver effettivo. |
| Errore di backup o ripristino NVDF | Conserva lavoro protetto e RECOVERY.txt; non cancellare il diario né forzare scritture contrastanti. |
| Impostazioni NVMFG in sospeso | Risolvi il ripristino con i giochi chiusi, preservando le modifiche apportate da altri strumenti. |
| Il limite RP non ha alcun effetto | Esegui RTSS, identifica il vero EXE del gioco, controlla lo stato dell'hook e i limiti della concorrenza. |
| Il cappuccio RP persiste dopo la rimozione | Ispezionare RTSS Globale; la rimozione modifica solo il limitatore locale. |

NVDriverForge offre un report JSON locale visualizzabile in anteprima; NVMFG offre una diagnostica in Informazioni. Preferisci questi report filtrati a un archivio di log completo e controllali prima di condividerli. Un blocco del ripristino segnalato su NVMFG 0.1.1 non ha ancora una causa accertata; conservare il proprio diario e registrare eventuali codici di errore disponibili. NVRasterPulse 0.2 offre la diagnostica di configurazione nel suo menu azioni, senza misurare FPS.

<a id="logs-and-privacy"></a>
## Registri e privacy

| Strumento | Dati locali da rivedere, non caricare all'ingrosso |
| --- | --- |
| NVDF | `%LOCALAPPDATA%\NVDriverForge`; lavori protetti `%PROGRAMDATA%\NVDriverForge\Jobs` |
| NVMFG | `%LOCALAPPDATA%\RtxMfg`; backup `%LOCALAPPDATA%\NvidiaStreamlineMaintenance\Backups`; `Sessions` accanto all'EXE |
| RP | `%LOCALAPPDATA%\NVRasterPulse`; `Backups\RTSS` sotto di esso |
| NVPI | Le esportazioni scelte e l'errore visualizzato; nessun percorso log universale inventato |

Rimuovi nomi di account, directory home, percorsi della libreria di giochi, identificatori di dispositivi, token e finestre non correlate dal testo/immagini che condividi. Conservare gli originali in privato per il recupero. I problemi pubblici sono visibili a tutti.

Per una vulnerabilità, un comportamento privilegiato pericoloso o un'operazione distruttiva non intenzionale, segui [SECURITY.md](../SECURITY.md) invece di pubblicare i dettagli pubblicamente.

<a id="what-has-been-verified"></a>
## Cosa è stato verificato

Per la preparazione dell'hub, sono state eseguite scansioni statiche di payload/ZIP/hash/metadati e controlli della documentazione. I test di build/unità/interfaccia utente di applicazioni private esistenti sono prove storiche e datate. Come parte di questa preparazione non sono state eseguite installazioni di driver, modifiche al display, operazioni live di RTSS o benchmark di giochi.

"Rilevato", "scritto", "ricaricato", "capacità disponibile" e "misurato nel gioco" sono risultati diversi. Segnala quale hai osservato.
