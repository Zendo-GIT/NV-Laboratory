<!-- nv-language-navigation:start -->
🌐 [English](../../../../NVDriverForge/README.md) | [Français](../../../../NVDriverForge/README.fr.md) · [NV Laboratory](../README.md)

<details>
<summary>🌐 Language · 34</summary>

[العربية](../../ar/NVDriverForge/README.md) · [বাংলা](../../bn/NVDriverForge/README.md) · [简体中文](../../zh/NVDriverForge/README.md) · [Čeština](../../cs/NVDriverForge/README.md) · [Dansk](../../da/NVDriverForge/README.md) · [Nederlands](../../nl/NVDriverForge/README.md) · [English](../../../../NVDriverForge/README.md) · [Filipino](../../fil/NVDriverForge/README.md) · [Suomi](../../fi/NVDriverForge/README.md) · [Français](../../../../NVDriverForge/README.fr.md) · [Deutsch](../../de/NVDriverForge/README.md) · [Ελληνικά](../../el/NVDriverForge/README.md) · [हिन्दी](../../hi/NVDriverForge/README.md) · [Magyar](../../hu/NVDriverForge/README.md) · [Bahasa Indonesia](../../id/NVDriverForge/README.md) · **Italiano** · [日本語](../../ja/NVDriverForge/README.md) · [한국어](../../ko/NVDriverForge/README.md) · [मराठी](../../mr/NVDriverForge/README.md) · [فارسی](../../fa/NVDriverForge/README.md) · [Polski](../../pl/NVDriverForge/README.md) · [Português](../../pt/NVDriverForge/README.md) · [ਪੰਜਾਬੀ](../../pa/NVDriverForge/README.md) · [Română](../../ro/NVDriverForge/README.md) · [Русский](../../ru/NVDriverForge/README.md) · [Español](../../es/NVDriverForge/README.md) · [Kiswahili](../../sw/NVDriverForge/README.md) · [Svenska](../../sv/NVDriverForge/README.md) · [தமிழ்](../../ta/NVDriverForge/README.md) · [ไทย](../../th/NVDriverForge/README.md) · [Türkçe](../../tr/NVDriverForge/README.md) · [Українська](../../uk/NVDriverForge/README.md) · [اردو](../../ur/NVDriverForge/README.md) · [Tiếng Việt](../../vi/NVDriverForge/README.md)

[Translation policy](../../README.md)

</details>
<!-- nv-language-navigation:end -->

<!-- nv-translation-notice:start -->
> Traduzione assistita da macchina dall'inglese. Nomi tecnici, comandi, URL e testi legali originali vengono conservati. È gradita la recensione da parte di madrelingua; consultare il riferimento inglese se la formulazione non è chiara.
<!-- nv-translation-notice:end -->

<a id="nvdriverforge"></a>
# NVDriverForge

**Prepara un'installazione del driver NVIDIA con scelte chiare dei componenti e impostazioni opzionali.**

[Scarica 0.1.3 e stato](../docs/downloads.md#nvdriverforge) · [Installazione](#installation) · [Crediti](#credits-and-upstream) · [Licenza](../../../../NVDriverForge/LICENSE)

<a id="overview-and-purpose"></a>
## Panoramica e scopo

NVDriverForge ti guida attraverso un pacchetto driver NVIDIA originale: scegli il driver, ispeziona i suoi componenti, esamina le modifiche opzionali, quindi conferma l'installazione. Esiste per rendere comprensibili queste scelte e mantenere insieme l'installazione, le operazioni privilegiate e le informazioni di ripristino.

Si tratta di un'applicazione sviluppata in modo indipendente ispirata in parte al flusso di lavoro di NVCleanstall. Non include NVCleanstall né rivendica la parità completa delle funzionalità.

<a id="features"></a>
## Caratteristiche

- Ricerca e download NVIDIA Game Ready / Studio; rilevamento hotfix opzionale con fallback manuale.
- Analisi del pacchetto originale, hash, firme NVIDIA, manifest e voci INF compatibili.
- Selezione dei componenti con dipendenze e conservazione dei componenti sconosciuti.
- La versione 0.1.3 mantiene i componenti NVIDIA opzionali selezionati ignorabili ed esclude dal rilevamento solo i componenti verificati e non controllati. I runtime opzionali già attuali o inapplicabili non sono più forzati come componenti critici.
- Chiari riepiloghi degli errori di installazione e accesso a registri dettagliati in tutte le 34 lingue.
- Conferma esplicita dell'installazione, gestione temporanea protetta ed esportazione di pacchetti di archiviazione driver esistenti.
- Impostazioni avanzate opzionali, con controlli preliminari, journal e ripristino in funzione dei conflitti.
- Preimpostazione opzionale **Custom NV** con scelte denominate e spiegazioni, inclusa una selezione separata della forza SILK e controlli di compatibilità.
- Download opzionali della patch NVENC della versione esatta; vengono controllati il ​​commit di origine e i byte di destinazione.
- Un'installazione separata e opzionale di Profile Inspector fork dalla schermata Strumenti.
- Controlli opzionali degli aggiornamenti installati dall'utente, 34 lingue di interfaccia e quattro temi.

Le opzioni avanzate disponibili riguardano MPO, l'indicatore DLSS, Ansel, la sospensione audio NVIDIA, MSI, policy/priorità di interruzione, HDCP, avvio del contenitore del display e un servizio di telemetria legacy idoneo. Ognuno ha i propri prerequisiti ed effetti; questi non sono miglioramenti universali delle prestazioni.

<a id="compatibility"></a>
## Compatibilità

| Requisito | Dettagli |
| --- | --- |
| Sistema | Windows 10 build 19041 o successiva/Windows 11, x64 |
| GPU/driver | Pacchetto NVIDIA compatibile e hardware rilevato; la ricerca automatica del catalogo copre principalmente i modelli GeForce noti |
| Durata | .NET 8 / WPF 8.0.31 incluso nel pacchetto autonomo preparato |
| Privilegi | Configurazione normale dell'interfaccia utente/per utente; l'installazione del driver e le modifiche al sistema richiedono l'accesso come amministratore |
| Rete | Richiesto per la ricerca/download online di NVIDIA e per le richieste NVENC upstream esplicite; è possibile selezionare un driver originale locale |
| Strumenti inclusi | 7-Zip 26.03 non modificato, avvisi di runtime, compagno MIT Profile Inspector opzionale |
| Compagno facoltativo | .NET Framework 4.8 per Profile Inspector fork separato |

Nessuna versione minima arbitraria del driver copre tutte le funzionalità. La ricerca multi-GPU deve corrispondere a ogni GPU rilevato. I modelli non supportati/professionali possono richiedere la selezione manuale del driver. Il programma di installazione di NVIDIA rimane l'autorità finale per l'hardware/sistema operativo.

<a id="installation"></a>
## Installazione

1. Visita [download](../docs/downloads.md#nvdriverforge) e conferma che la release è pubblicata.
2. Scegli `NVDriverForge-Setup.exe` per l'installazione o `NVDriverForge.exe` per l'uso portatile.
3. Confronta SHA-256 con `SHA256SUMS.txt` della versione.
4. Esegui il programma di installazione per un'installazione per utente e un programma di disinstallazione standard oppure posiziona l'EXE portatile in una cartella scrivibile e aprilo.

Il portatile include il suo runtime e il suo programma di installazione opzionale. L'installazione di NVDriverForge non installa un driver GPU. I suoi EXE non sono attualmente firmati.

<a id="usage"></a>
## Utilizzo

1. **Driver:** scarica da NVIDIA o seleziona un EXE di installazione NVIDIA originale. Lasciamo finire l'analisi.
2. **Componenti:** esamina le descrizioni e le dipendenze richieste. I componenti sconosciuti vengono mantenuti.
3. **Modifiche:** lascia invariate le opzioni indesiderate. Leggi gli effetti e i compromessi prima di selezionare qualsiasi cosa.
4. **Recensione:** controlla il driver esatto, i componenti e le operazioni opzionali, quindi conferma l'installazione.
5. Accetta UAC solo per l'operazione scelta. Conservare le istruzioni di ripristino del lavoro protetto.
6. Se il nuovo driver necessita di un riavvio, seguire lo stato riportato. Le operazioni differite richiedono la ripresa esplicita dopo il riavvio.

Custom NV inizia invariato. Scegli singoli valori con nome o rivedi la preimpostazione fornita e le relative esclusioni. I suoi due campi interni informativi non sono scritti in modo indipendente. Le impostazioni vengono applicate solo nel flusso di lavoro del nuovo driver verificato, mai aprendo un'anteprima. Non è necessaria l'installazione dell'editor NVPI separato.

Il lavoro opzionale NVENC scarica i dati compatibili da un commit keylase bloccato. Altera due DLL dei driver e invalida le loro firme; può essere rifiutato da Windows, codificatori, DRM o anti-cheat. Nessun dato di questo tipo o DLL NVIDIA è incorporato in NVDriverForge. [Provenienza e limiti di licenza](../docs/provenance.md).

Le preferenze controllano la lingua, il tema e i controlli opzionali degli aggiornamenti installati dall'utente. Il portatile non crea l'attività di controllo in background installata. Gli strumenti e il ripristino sono separati dai quattro passaggi di installazione.

<a id="screenshots"></a>
## Schermate

![Anteprima della pagina del driver NVDriverForge](../../../../assets/screenshots/nvdriverforge-0.1.2-preview.png)

Rendering dell'interfaccia utente francese 0.1.2 esistente con dati di esempio; mantenuto come anteprima dell'interfaccia. Il driver 699.99 visualizzato è un dispositivo di prova, non una versione reale da scaricare. [Provenienza dell'immagine](../assets/README.md).

<a id="update-and-uninstall"></a>
## Aggiorna e disinstalla

Chiudi NVDriverForge, ottieni il prossimo pacchetto ufficiale e verificane l'hash. Utilizzare la stessa identità di installazione per un aggiornamento installato; sostituire un EXE portatile chiuso con quello nuovo. Mantieni le impostazioni e i lavori protetti.

Uninstall da Windows **Installed apps**. Rimuove l'app e la relativa attività di aggiornamento, non il driver NVIDIA. Impostazioni, registri e backup rimangono. Se lo si desidera, ripristinare le modifiche avanzate/NVENC tramite il flusso di ripristino documentato **prima** di rimuovere l'app. Il ripristino rifiuta le modifiche in conflitto da un altro strumento.

I dati locali si trovano in `%LOCALAPPDATA%\NVDriverForge`; i lavori protetti e le esportazioni di driver sono in `%PROGRAMDATA%\NVDriverForge\Jobs`. L'uso portatile crea anche dati locali. Un'esportazione dell'archivio driver non è un'immagine di sistema o un backup completo del profilo.

<a id="known-limitations"></a>
## Limitazioni note

- Nessuna aggiunta hardware/modifica INF, firme NVIDIA rigenerate, dimissioni compatibili con anti-cheat o accettazione automatica di avvisi senza firma.
- Nessuna rimozione completa di telemetria/pubblicità, esportazione di pacchetti ridotti o rollback completo automatico al driver precedente.
- L'installazione dei driver, il ripristino dell'avvio e le scritture dei profili opzionali non sono stati convalidati in modo completo sulle macchine reali dall'audit dell'hub.
- La rilettura del registro non è una prova degli effettivi effetti di HDCP, prestazioni o latenza.
- I controlli della firma utilizzano l'attendibilità Windows disponibile localmente; non viene effettuata la revoca online.
- Sono presenti 34 lingue, ma i test completi sui madrelingua/accessibilità rimangono incompleti.

<a id="troubleshooting"></a>
## Risoluzione dei problemi

| Sintomo | Azione |
| --- | --- |
| Catalogo online non disponibile | Seleziona un pacchetto originale da [Download dei driver NVIDIA](https://www.nvidia.com/en-us/drivers/). Non sostituire un modello GPU vicino. |
| Ricerca hotfix non disponibile | Utilizzare [Forum dei driver Game Ready di NVIDIA](https://www.nvidia.com/en-us/geforce/forums/game-ready-drivers/13/) e verificare il pacchetto effettivo. |
| L'installazione di NVIDIA non riesce | Leggere il riepilogo degli errori e aprire i registri dettagliati. I componenti opzionali già attuali o non applicabili rimangono ignorabili in 0.1.3. Le installazioni non riuscite non attivano modifiche facoltative o un flusso di successo/riavvio. |
| Errore di firma/hash/backup | Interrompere l'installazione e conservare l'errore; ottenere nuovamente il pacchetto originale se danneggiato. |
| Opzione non disponibile | Leggere il motivo dell'hardware, del componente o del driver di destinazione; mantenerlo invariato. |
| Riavvio o lavoro ancora in sospeso | Utilizzare le istruzioni di ripristino del lavoro e il curriculum esplicito; non cancellare il suo diario. |
| Ripristina il conflitto | Un altro stato è diverso dalla transazione registrata. Conservalo e richiedi aiuto invece di forzare un ripristino. |

Per i report, includere la versione dello strumento selezionato, Windows, GPU, driver e passaggi riproducibili; oscurare percorsi e dettagli personali dai registri. [Supporto](../docs/support.md).

<a id="faq"></a>
## Domande frequenti

**Il programma di installazione installa un driver grafico?** No. Ciò richiede l'analisi, la revisione, la conferma e il processo di installazione avanzata separati dell'applicazione.

**Ho bisogno di NVCleanstall o NVPI?** No. NVCleanstall è solo ispirazione. Il compagno Profile Inspector è un editor opzionale indipendente.

**Rende ogni driver NVIDIA più piccolo o più veloce?** No. Componenti e prerequisiti selezionati determinano cosa può cambiare; non viene promesso alcun guadagno misurato.

**Dove sono i sorgenti?** Il sorgente specifico dell'applicazione e i test privati vengono mantenuti separatamente. Questo hub fornisce documentazione, file binari e collegamenti a fonti di terze parti necessari per l'attribuzione/licenza.

<a id="credits-and-upstream"></a>
## Crediti e monte

Applicazione originale, flusso di lavoro, transazioni, localizzazione, bootstrap e adattamenti: 禅堂 Zendo (RevoluSound Team).

- [NVCleanstall / TechPowerUp](https://www.techpowerup.com/download/techpowerup-nvcleanstall/): ispirazione per il flusso di lavoro; nessuna fonte o binario importato.
- [NVIDIA Profile Inspector / Orbmu2k](https://github.com/Orbmu2k/nvidiaProfileInspector): temi MIT, riferimento interfaccia NVAPI esteso e fork confezionato separatamente.
- [7-Zip / Igor Pavlov](https://www.7-zip.org/): strumenti di estrazione non modificati.
- [Microsoft.NET](https://github.com/dotnet/runtime) e [WPF](https://github.com/dotnet/wpf): runtime in bundle.
- [Inno Setup](https://jrsoftware.org/isinfo.php): motore di installazione originale e traduzioni accreditate.
- [keylase/nvidia-patch](https://github.com/keylase/nvidia-patch): origine dati NVENC esterna opzionale; licenza di ridistribuzione non stabilita.
- [NVIDIA](https://www.nvidia.com/en-us/drivers/): download di driver esterni e librerie NVAPI/NVML installate.

[Tabella completa dei componenti](../THIRD_PARTY_NOTICES.md) · [Cambiamenti e provenienza](../docs/provenance.md)

<a id="license"></a>
## Licenza

[Autorizzazione di distribuzione binaria esistente](../../../../NVDriverForge/LICENSE) consente l'uso e la condivisione di eseguibili ufficiali non modificati con i relativi avvisi. I diritti di origine specifici dell'applicazione sono riservati. Non limita i diritti concessi dalle licenze separate di terze parti. [Avvisi completi](LICENSES/README.md).

Indipendente da NVIDIA Corporation, TechPowerUp e keylase; non sponsorizzati o ufficialmente approvati da loro. I nomi dei prodotti rimangono marchi dei rispettivi proprietari.
