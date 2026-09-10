<!-- nv-language-navigation:start -->
🌐 [English](../../../provenance.md) | [Français](../../../provenance.fr.md) · [NV Laboratory](../README.md)

<details>
<summary>🌐 Language · 34</summary>

[العربية](../../ar/docs/provenance.md) · [বাংলা](../../bn/docs/provenance.md) · [简体中文](../../zh/docs/provenance.md) · [Čeština](../../cs/docs/provenance.md) · [Dansk](../../da/docs/provenance.md) · [Nederlands](../../nl/docs/provenance.md) · [English](../../../provenance.md) · [Filipino](../../fil/docs/provenance.md) · [Suomi](../../fi/docs/provenance.md) · [Français](../../../provenance.fr.md) · [Deutsch](../../de/docs/provenance.md) · [Ελληνικά](../../el/docs/provenance.md) · [हिन्दी](../../hi/docs/provenance.md) · [Magyar](../../hu/docs/provenance.md) · [Bahasa Indonesia](../../id/docs/provenance.md) · **Italiano** · [日本語](../../ja/docs/provenance.md) · [한국어](../../ko/docs/provenance.md) · [मराठी](../../mr/docs/provenance.md) · [فارسی](../../fa/docs/provenance.md) · [Polski](../../pl/docs/provenance.md) · [Português](../../pt/docs/provenance.md) · [ਪੰਜਾਬੀ](../../pa/docs/provenance.md) · [Română](../../ro/docs/provenance.md) · [Русский](../../ru/docs/provenance.md) · [Español](../../es/docs/provenance.md) · [Kiswahili](../../sw/docs/provenance.md) · [Svenska](../../sv/docs/provenance.md) · [தமிழ்](../../ta/docs/provenance.md) · [ไทย](../../th/docs/provenance.md) · [Türkçe](../../tr/docs/provenance.md) · [Українська](../../uk/docs/provenance.md) · [اردو](../../ur/docs/provenance.md) · [Tiếng Việt](../../vi/docs/provenance.md)

[Translation policy](../../README.md)

</details>
<!-- nv-language-navigation:end -->

<!-- nv-translation-notice:start -->
> Traduzione assistita da macchina dall'inglese. Nomi tecnici, comandi, URL e testi legali originali vengono conservati. È gradita la recensione da parte di madrelingua; consultare il riferimento inglese se la formulazione non è chiara.
<!-- nv-translation-notice:end -->

<a id="provenance-changes-and-licensing"></a>
# Provenienza, modifiche e licenza

Questo audit descrive i candidati preparati il **2026-09-09**. Le origini delle applicazioni rimangono private; gli inventari pubblici contengono nomi di file e hash, non codice sorgente. Vedi [avvisi relativi ai componenti completi](../THIRD_PARTY_NOTICES.md).

<a id="nvidia-profile-inspector--nv-tools-fork"></a>
## NVIDIA Profile Inspector – NV Tools Fork

Riferimento: Orbmu2k/nvidiaProfileInspector commit `592d962cca8827efe8859461a84267755595064a`; versione eseguibile candidata 3.0.2.3. Il commit di riferimento e la versione dell'assembly di fork sono identificatori diversi; nessuna versione di rilascio upstream viene dedotta dalla versione fork.

I 157 file sorgente/risorsa del compagno pulito sono stati confrontati con quel commit: 2 identici in byte, 134 diversi solo nelle terminazioni di riga o nella BOM UTF-8, 11 modificati, 10 assenti nel percorso upstream confrontato. "Aggiunto" è relativo a quel percorso e non è di per sé una prova della paternità originale.

[Confronto completo di file/hash](../../../provenance/nvpi-source-provenance.json).

| Zona | Lavoro ereditato | Contributo Fork |
| --- | --- | --- |
| Editor del profilo | Modello di profilo, importazione/esportazione, associazioni di applicazioni e dati di riferimento | Integrazione con Screen e il launcher di strumenti esterni |
| NVAPI | Interoperabilità DRS di Orbmu2k | Interoperabilità relativa al colore/display, restrizioni al caricamento nativo della produzione e rimozione simulata |
| Visualizza servizi | API Windows/NVIDIA come interfacce esterne | DisplayInfoService, DisplayConfigurationService, DisplaySettingsBackend |
| interfaccia utente | Risorse, tavolozze e icone WPF upstream | Finestre di dialogo sullo schermo, conferma di 15 secondi, stato/rilettura e layout della barra degli strumenti |
| Lanciatore | Shell dell'app esistente | Ricerca e avvio RasterPulse installati separatamente protetti |
| Imballaggio | MIT a monte | Compagno autonomo pulito, programma di installazione/disinstallazione separato, avvisi conservati |

La mappa della fonte pubblica include percorsi di soluzioni/risorse per la tracciabilità; quei file non sono distribuiti come sorgente. Sono esclusi i test di sviluppo, le interfacce mock e il vecchio binario combinato NVPI/RasterPulse.

<a id="nvdriverforge"></a>
## NVDriverForge

Applicazione C#/.NET 8/WPF indipendente; il flusso di lavoro rivolto all'utente è in parte ispirato a NVCleanstall. Nel payload di produzione non è stata identificata alcuna origine/binario NVCleanstall. Non è rappresentato come fork di tale applicazione proprietaria.

Il lavoro del progetto originale include analisi/selezione dei componenti, processi di installazione protetti, backup e ripristino delle transazioni, download del catalogo NVIDIA, controlli degli aggiornamenti, spiegazioni localizzate, flussi di lavoro avanzati/NVENC opzionali e bootstrap del programma di installazione.

Componenti ereditati/adattati: quattro tavolozze di temi NVPI, riferimento esteso all'interfaccia DRS NVAPI e il compagno MIT NVPI opzionale separatamente. L'interfaccia utente di selezione della preimpostazione Custom NV e l'integrazione delle transazioni nella lista consentita appartengono a NVDriverForge; la preimpostazione non è una raccomandazione ufficiale NVIDIA.

7-Zip 26.03, .NET/WPF 8.0.31 e Inno Setup rimangono componenti esterni non modificati utilizzati secondo i propri termini. keylase I dati NVENC non sono incorporati; viene scelto e controllato un commit esatto quando l'utente richiede un download compatibile. Non è stata stabilita alcuna licenza di ridistribuzione per tali dati a monte.

<a id="nvmfg-unlock40"></a>
## NVMFG Unlock40

NVMFG Unlock40 è stato sviluppato in modo indipendente da 禅堂 Zendo (RevoluSound Team). Il manutentore ha utilizzato RTX40MFG-Unlock per il confronto e il perfezionamento. L'applicazione nel suo insieme non viene presentata come fork. Questa distinzione non rimuove i crediti per i componenti condivisi/adattati nel livello nativo corrente.

Riferimento di confronto: dashdogy/RTX40MFG-Unlock, Michael Robles, MIT, commit `4e776d068f91b4a665425542bb005dd57cc3d891`. L'albero privato del motore nativo contiene 48 file confrontati: 35 differenze di sola formattazione, 4 file modificati e 9 assenti nel percorso di riferimento. [Confronto completo](../../../provenance/nvmfg-source-provenance.json).

File ereditati modificati: `entry_detour.h`, `patcher.cpp`, `temporal_interval_trace.cpp`, `temporal_interval_trace.h`. Percorsi aggiuntivi includono `game_selection.*`, `ngx_bootstrap.*`, `ngx_capability.h`, `presentation_tracker.h`, `vsync_observer.*` e una licenza upstream mantenuta.

Unità C++ di produzione: patcher, midpoint_fix, dlssg_provider_policy, entry_detour, nvidia_mfg_policy, temporal_interval_trace, ngx_bootstrap, game_selection e vsync_observer; più il gruppo entry_detour e il buffer/gancio/trampolino/HDE64 MinHook. Il frontend ReShade ereditato, le risorse shim legacy e le destinazioni CMake inutilizzate non fanno parte di questa raccolta di produzione.

I componenti di corrispondenza riguardano la politica di patching/fornitore e il lavoro temporale; i loro avvisi di copyright e autorizzazione rimangono intatti. Il coordinamento centrale di NGX/bootstrap/controller, la gestione di V-Sync per gioco, la diagnostica della sessione e il flusso di lavoro di backup/applicazione Windows/SDK sono lavori di progetto di 禅堂 Zendo (RevoluSound Team). I conteggi sopra descrivono file, inclusi file di terze parti e inutilizzati, non una percentuale di paternità o la cronologia dell'idea di uno dei due progetti.

L'helper adatta NvapiDrsWrapper e NativeArrayHelper di NVPI in un assieme separato, con la logica del profilo creato dal progetto. È escluso il vecchio percorso simulato di sviluppo. Le tavolozze della famiglia condivisa provengono da NVPI.

Riferimento MinHook: `8fda4f5481fed5797dc2651cd91e238e9b3928c6`; il sottoinsieme compilato ereditato non presenta modifiche locali funzionali nel confronto. Intestazioni di integrazione Streamline: 2.12; licenza di intestazione aperta verificata su v2.12.0. Origine intestazione NGX: NVIDIA/DLSS commit `a291cc7d2cc642a51566f3dfd5376f635cd1b284`.

Motore candidato SHA-256: `0E7FC0277C88B22095B622F6A3CB292EC0C14F7A0253D392502257B75E548890`.

Provider richiesto SHA-256 in engine.json: `C64928FDB7C48A57722EA8EEF2662171EDC323473ADEA66C29A206A23F1A2BED`. Una famiglia di provider 310.9 segnalata non è intercambiabile con questo hash esatto. Non è inclusa alcuna DLL o modello del provider.

**Punto di licenza eccezionale:** la licenza completa NVIDIA RTX SDK, versione 14 marzo 2024, contiene una restrizione della sezione 4(d) relativa al superamento delle limitazioni tecniche. L'audit non stabilisce l'autorizzazione per questo utilizzo. Mantenere la licenza del motore MIT, essere gratuito o osservare altre modifiche non risolve tale condizione separata. La preparazione del candidato non costituisce un nulla osta legale. La breve intestazione originale è integrata con la licenza completa; il suo testo Windows-1252 viene fornito anche come UTF-8 leggibile, mantenendo i byte originali.

<a id="nvrasterpulse"></a>
## NVRasterPulse

Gestore profilo RTSS indipendente sviluppato nel repository derivato da NVPI. Le risorse/tavolozze dell'interfaccia utente MIT ereditate e l'origine del progetto rimangono accreditate. L'app di produzione utilizza esplicitamente la licenza MIT fornita.

Lavoro del progetto: analisi/scritture precise del profilo RTSS e codifica frazionaria, backup, rimozione dell'override, bridge di ricarica, rilevamento dei prerequisiti, interfaccia utente compatta, ciclo di vita del vassoio, controlli di avvio e localizzazione. RTSS esegue la limitazione effettiva.

Non è inclusa alcuna sorgente RTSS, hook DLL, SDK o programma di installazione. Il bridge richiama l'esportazione in un'installazione RTSS esistente selezionata dall'utente. Nessun pacchetto driver NVIDIA, limitatore sperimentale nativo, Framepacer, runtime MinHook, ReShade o DLSS in questo pacchetto.

<a id="assets-generated-data-and-tools"></a>
## Asset, dati generati e strumenti

[Crediti patrimoniali](../assets/README.md) identifica le anteprime dell'interfaccia esistente e il selettore di configurazione NVPI. I valori fittizi in essi contenuti sono etichettati. Non viene copiata alcuna risorsa di gioco/Nexus, profilo personale, ICC privato, logo aziendale NVIDIA o file di caratteri.

I nomi di compatibilità dei giochi generati ed ereditati in NVMFG sono un aiuto per il rilevamento, non una prova di test. I cataloghi di installazione generati sono accreditati in [avvisi del traduttore](../../../../licenses/INSTALLER-TRANSLATORS.md). I record di build generati con percorsi assoluti rimangono privati.

Gli strumenti di compilazione privati includono gli script di controllo .NET SDK/MSBuild, Visual Studio C++/MASM, Windows SDK, PowerShell, Inno Setup e Python. I loro compilatori, intestazioni, test runner e risorse di debug non vengono distribuiti. La versione statica CRT rimane soggetta ai termini della toolchain applicabili di Microsoft.

<a id="scope-of-verification"></a>
## Ambito di verifica

L'audit locale ha inventariato tutti i file nelle tre radici di sviluppo escludendo i database di oggetti Git e le destinazioni delle directory collegate. Sono stati scansionati i documenti/le fonti attive; le costruzioni storiche sono state inventariate ed escluse. Gli ZIP selezionati e i payload correnti sono stati scansionati e sottoposti ad hashing; i bundle .NET sono stati decompressi per un'ulteriore ispezione. L'audit iniziale non ha eseguito alcun prodotto, programma di installazione, gioco, processo RTSS o driver.

La successiva revisione 2 della configurazione NVPI corregge la selezione autonoma della lingua utilizzando i controlli Inno condivisi e il bootstrap. Gli apparecchi privati ​​chiaro/scuro hanno verificato la navigazione con mouse e tastiera e tutti i 34 codici linguistici espliciti. Il selettore di configurazione effettivo è stato aperto su un desktop privato mai visualizzato e annullato prima dell'installazione. I suoi sette file applicativi e lo ZIP portatile sono invariati. NVDriverForge 0.1.3 include il compagno corretto e inoltra ancora `/LANG`.

NVDriverForge 0.1.3 è stato completato il 10/09/2026. Il suo rapporto di verifica privata registra 366 test applicativi, 118 controlli complementari, 32 controlli di installazione, 156 confronti nativi e 34 casi di inoltro della lingua. La correzione della selezione dei componenti protetti è stata riprodotta rispetto a un pacchetto di driver originale senza modificarne il carico utile o installare il driver. Questi sono risultati datati del team di prodotto, non test rieseguiti da questo aggiornamento della documentazione o prova di un'installazione corretta del driver reale.

Questo aggiornamento dell'hub non modifica alcun codice dell'applicazione funzionale. I test di build/unità/UI di applicazioni precedenti rimangono prove storiche datate. Non si tratta di un completo reverse engineering di ogni codice binario di terze parti o di una garanzia contro ogni possibile modello segreto.
