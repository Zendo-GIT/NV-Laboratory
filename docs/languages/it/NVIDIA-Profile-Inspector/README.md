<!-- nv-language-navigation:start -->
🌐 [English](../../../../NVIDIA-Profile-Inspector/README.md) | [Français](../../../../NVIDIA-Profile-Inspector/README.fr.md) · [NV Laboratory](../README.md)

<details>
<summary>🌐 Language · 34</summary>

[العربية](../../ar/NVIDIA-Profile-Inspector/README.md) · [বাংলা](../../bn/NVIDIA-Profile-Inspector/README.md) · [简体中文](../../zh/NVIDIA-Profile-Inspector/README.md) · [Čeština](../../cs/NVIDIA-Profile-Inspector/README.md) · [Dansk](../../da/NVIDIA-Profile-Inspector/README.md) · [Nederlands](../../nl/NVIDIA-Profile-Inspector/README.md) · [English](../../../../NVIDIA-Profile-Inspector/README.md) · [Filipino](../../fil/NVIDIA-Profile-Inspector/README.md) · [Suomi](../../fi/NVIDIA-Profile-Inspector/README.md) · [Français](../../../../NVIDIA-Profile-Inspector/README.fr.md) · [Deutsch](../../de/NVIDIA-Profile-Inspector/README.md) · [Ελληνικά](../../el/NVIDIA-Profile-Inspector/README.md) · [हिन्दी](../../hi/NVIDIA-Profile-Inspector/README.md) · [Magyar](../../hu/NVIDIA-Profile-Inspector/README.md) · [Bahasa Indonesia](../../id/NVIDIA-Profile-Inspector/README.md) · **Italiano** · [日本語](../../ja/NVIDIA-Profile-Inspector/README.md) · [한국어](../../ko/NVIDIA-Profile-Inspector/README.md) · [मराठी](../../mr/NVIDIA-Profile-Inspector/README.md) · [فارسی](../../fa/NVIDIA-Profile-Inspector/README.md) · [Polski](../../pl/NVIDIA-Profile-Inspector/README.md) · [Português](../../pt/NVIDIA-Profile-Inspector/README.md) · [ਪੰਜਾਬੀ](../../pa/NVIDIA-Profile-Inspector/README.md) · [Română](../../ro/NVIDIA-Profile-Inspector/README.md) · [Русский](../../ru/NVIDIA-Profile-Inspector/README.md) · [Español](../../es/NVIDIA-Profile-Inspector/README.md) · [Kiswahili](../../sw/NVIDIA-Profile-Inspector/README.md) · [Svenska](../../sv/NVIDIA-Profile-Inspector/README.md) · [தமிழ்](../../ta/NVIDIA-Profile-Inspector/README.md) · [ไทย](../../th/NVIDIA-Profile-Inspector/README.md) · [Türkçe](../../tr/NVIDIA-Profile-Inspector/README.md) · [Українська](../../uk/NVIDIA-Profile-Inspector/README.md) · [اردو](../../ur/NVIDIA-Profile-Inspector/README.md) · [Tiếng Việt](../../vi/NVIDIA-Profile-Inspector/README.md)

[Translation policy](../../README.md)

</details>
<!-- nv-language-navigation:end -->

<!-- nv-translation-notice:start -->
> Traduzione assistita da macchina dall'inglese. Nomi tecnici, comandi, URL e testi legali originali vengono conservati. È gradita la recensione da parte di madrelingua; consultare il riferimento inglese se la formulazione non è chiara.
<!-- nv-translation-notice:end -->

<a id="nvidia-profile-inspector--nv-tools-fork"></a>
# NVIDIA Profile Inspector – NV Tools Fork

**Un fork indipendente da [NVIDIA Profile Inspector di Orbmu2k](https://github.com/Orbmu2k/nvidiaProfileInspector), con controlli display aggiunti.** Nome del progetto precedente: **NVPI Custom**.

[Stato di download e rilascio](../docs/downloads.md#nvidia-profile-inspector) · [Installazione](#installation) · [Controcorrente e cambiamenti](#upstream-and-changes) · [Licenza](../../../../NVIDIA-Profile-Inspector/LICENSE)

<a id="overview"></a>
## Panoramica

L'applicazione modifica i profili del driver NVIDIA, comprese le impostazioni per applicazione. Questo fork aggiunge anche un editor **Schermo** per il display Windows attivo: risoluzione, frequenza di aggiornamento, impostazioni del colore di output, HDR e associazioni dei profili ICC/WCS installati.

Esiste per portare i relativi controlli di visualizzazione nell'editor del profilo e per rendere più chiari i risultati di anteprima, conferma e ripristino. Non stabilisce nuove funzionalità hardware.

Il primo candidato è **3.0.2.3**, utilizzando la build complementare autonoma ripulita dal 9 settembre 2026. Il suo eseguibile esistente rimane `nvidiaProfileInspector.exe`; il programma di installazione e alcune etichette interne dicono ancora `NVPI Custom NV`. Il titolo pubblico sopra identifica fork senza modificare l'identità di installazione o fingere che sia la versione ufficiale di Orbmu2k.

<a id="features"></a>
## Caratteristiche

- Navigazione dei profili upstream esistenti, associazioni di applicazioni, modifiche delle impostazioni e importazione/esportazione dei profili.
- Finestra di dialogo **Schermata** per visualizzazione, modalità, Hz, RGB/YCbCr, profondità colore, gamma e colorimetria.
- Windows Controllo HDR e selezione associazione ICC/WCS installata.
- Un'anteprima di visualizzazione di 15 secondi con **Mantieni**/**Ripristina** e ripristino del timeout.
- Rilettura delle modifiche alla modalità/HDR e agli errori di ripristino segnalati.
- Reporting separato di HDR, SDR con ACM/WCG e profondità del colore del segnale.
- Un launcher NVRasterPulse per una copia idonea installata separatamente.

<a id="compatibility"></a>
## Compatibilità

| Requisito | Dettagli |
| --- | --- |
| Sistema | Windows 10/11 x64 con un driver NVIDIA compatibile |
| Durata | [.NET Framework 4.8](https://dotnet.microsoft.com/en-us/download/dotnet-framework/net48), fornito da Windows o installato separatamente |
| Autorizzazioni | L'editor richiede l'accesso come amministratore quando viene aperto |
| Visualizza | Le modalità effettive e le combinazioni di colori dipendono da GPU, driver, display, cavo e API Windows |
| Strumenti opzionali | NVRasterPulse per gestione limiti RTSS; né esso né RTSS sono necessari per l'editor dello schermo |
| Lingue | Configurazione: selettore di 34 lingue. L'editor mantiene il supporto linguistico esistente. |

Non esiste un driver universale minimo verificato o una matrice di supporto per ogni GPU. Le scelte bpc disponibili nella finestra di dialogo sono richieste, non combinazioni certificate. I moderni controlli HDR e il vecchio fallback Windows hanno funzionalità diverse.

<a id="installation"></a>
## Installazione

1. Apri [pagina di download](../docs/downloads.md#nvidia-profile-inspector) e controlla lo stato della pubblicazione.
2. Scarica il programma di installazione o la risorsa portatile e confronta il suo SHA-256 con il manifest della versione.
3. Per la configurazione, esegui `NVPI-CustomNV-3.0.2.3-Setup-r2.exe`, seleziona una lingua e segui il programma di installazione. Crea il proprio collegamento e programma di disinstallazione.
4. Per il portatile, estrai lo ZIP completo in una nuova cartella scrivibile. Conserva `Reference.xml`, la configurazione EXE e tutti gli avvisi accanto all'eseguibile.
5. Avvia `nvidiaProfileInspector.exe`.

L'installazione del solo editor non applica un profilo né installa un driver GPU. Il compagno si installa separatamente, non assume il controllo delle associazioni `.nip` e non abilita l'avvio all'accesso. I file binari esistenti non sono firmati.

<a id="usage"></a>
## Utilizzo

**Revisione 2 del programma di installazione** aggiunge lo stesso selettore di 34 lingue native degli altri strumenti, con navigazione tramite mouse/tastiera, aspetto chiaro/scuro e cancellazione. La scelta riguarda l'impostazione; non traduce l'editor NVPI. Un argomento `/LANG=fr` esplicito o una modalità silenziosa ignora la selezione per i chiamanti che forniscono già una lingua.

**Profili conducente:** seleziona un profilo, esporta un backup, quindi modifica solo le impostazioni desiderate e applicale. Le associazioni delle applicazioni determinano quale gioco riceve un profilo. Un valore memorizzato non è la prova che ogni driver o gioco lo utilizzi.

**Controlli di visualizzazione:** apri lo **Schermo**, scegli la visualizzazione e i valori richiesti, quindi avvia l'anteprima. Controlla l'immagine prima di scegliere **Conserva** entro 15 secondi. Utilizza **Ripristina**, chiudi la conferma o lasciala scadere per richiedere il ripristino. Leggi qualsiasi messaggio di errore: una chiamata API riuscita da sola non è prova del ripristino.

Una selezione ICC modifica un'associazione al profilo installato; non genera, calibra o ridistribuisce un file ICC. HDR, ACM/WCG, RGB/YCbCr e bpc descrivono diversi aspetti della pipeline. Non viene fornito alcun nuovo interruttore ACM indipendente.

**NVRasterPulse:** il pulsante della barra degli strumenti accetta un'installazione a livello di sistema registrata separatamente sotto Programmi con proprietà e autorizzazioni protette. Una copia portatile o un percorso scrivibile/collegato dall'utente potrebbe essere rifiutato da questo launcher elevato. In tal caso, apri NVRasterPulse utilizzando la propria scorciatoia. [Installare RTSS separatamente](https://www.guru3d.com/download/rtss-rivatuner-statistics-server-download/) per utilizzare NVRasterPulse.

<a id="screenshots"></a>
## Schermate

![Selettore lingua revisione 2 configurazione NVPI](../../../../assets/screenshots/nvpi-setup-r2-language.png)

Selettore di configurazione attuale in francese, catturato durante un test isolato e poi annullato. Questo mostra il programma di installazione; l'editor mantiene la sua interfaccia e la finestra di dialogo dello schermo.

<a id="update-and-uninstall"></a>
## Aggiorna e disinstalla

Chiudere l'editor prima dell'aggiornamento. Conserva i profili esportati e scarica la nuova Release fork; installa sulla stessa identità complementare o estrai file portatili in una nuova cartella. Non mescolare un vecchio `Reference.xml` con un nuovo eseguibile. La soppressione del controllo degli aggiornamenti upstream in bundle appartiene a questo fork.

Per una copia installata, utilizzare Windows **Installed apps** e il relativo programma di disinstallazione. Per il portatile, chiudilo e rimuovi la cartella estratta quando le tue esportazioni sono sicure. La rimozione dell'editor **non** annulla le modifiche al profilo conducente, le preferenze di visualizzazione, NVRasterPulse o RTSS. Ripristina le impostazioni desiderate prima della rimozione.

<a id="known-limitations"></a>
## Limitazioni note

- La conferma di 15 secondi non è un cane da guardia per ogni incidente del conducente, perdita di potenza o spegnimento forzato.
- Alcune combinazioni di colore/profondità/aggiornamento restituiscono `NVAPI_NOT_SUPPORTED`.
- La rilettura del software non misura la profondità di bit del pannello, la precisione del colore o la latenza.
- Le impostazioni dello schermo influiscono sul display corrente del Windows; questa finestra di dialogo non crea preimpostazioni di visualizzazione per gioco.
- Nessuna garanzia di prestazioni, anti-cheat o compatibilità universale HDR.

<a id="troubleshooting"></a>
## Risoluzione dei problemi

| Sintomo | Azione |
| --- | --- |
| Errore di runtime all'avvio | Controlla gli aggiornamenti di Windows e .NET Framework 4.8; utilizzare il pacchetto completo. |
| Modalità di visualizzazione richiesta rifiutata | Ripristina e testa una modalità offerta da Windows/NVIDIA per quel display. Leggere l'errore esatto ed evitare ripetuti cambiamenti ciechi. |
| HDR o il colore ritorna allo stato precedente | Controllare se un'altra operazione non è riuscita e ha attivato il ripristino; distinguere HDR da ACM. |
| Il pulsante NVRasterPulse rifiuta un percorso | Avvia la propria scorciatoia; questo pulsante richiede un'installazione protetta a livello di sistema. |
| Una modifica rimane dopo la disinstallazione | Ripristinare il profilo NVIDIA esportato o le impostazioni di visualizzazione Windows previste; la disinstallazione non è un ripristino delle impostazioni. |

Vedere [guida di supporto condivisa](../docs/support.md) prima di inviare i registri.

<a id="faq"></a>
## Domande frequenti

**Questo è il software NVIDIA ufficiale o la build ufficiale di Orbmu2k?** No. È un fork indipendente; l'autore upstream e la licenza MIT rimangono accreditati.

**NVDriverForge richiede questo editor?** No. La preimpostazione Custom NV opzionale di NVDriverForge utilizza la propria integrazione. L'installazione dell'editor è una scelta separata.

**RTSS è obbligatorio per questo fork?** No. RTSS è obbligatorio per il limitatore FPS di NVRasterPulse, non per la modifica del profilo o dello schermo.

**Dov'è l'origine?** L'origine dell'applicazione modificata viene mantenuta privatamente. Vengono forniti l'avviso MIT e il repository upstream; MIT non richiede la pubblicazione dell'origine modificata.

<a id="upstream-and-changes"></a>
## Controcorrente e cambiamenti

A monte: [Orbmu2k/nvidiaProfileInspector](https://github.com/Orbmu2k/nvidiaProfileInspector), commit di riferimento `592d962cca8827efe8859461a84267755595064a`. [Download originali](https://github.com/Orbmu2k/nvidiaProfileInspector/releases).

Ereditato: editor di profili, interoperabilità NVAPI, dati di riferimento, risorse dell'interfaccia utente e temi. 禅堂 Zendo (RevoluSound Team) ha aggiunto o adattato servizi di visualizzazione, transazioni HDR/ICC, conferma/rilettura di 15 secondi, layout della barra degli strumenti e comportamento di lancio di RasterPulse. Il compagno pulito esclude simulazioni di sviluppo/punti di ingresso di test, utilizza un launcher esterno protetto e fornisce un programma di installazione separato. Il vecchio pacchetto di sviluppo combinato NVPI/RasterPulse non è il candidato in questo hub.

[Provenienza dettagliata del file](../docs/provenance.md) · [Avviso fork originale](../../../../NVIDIA-Profile-Inspector/LICENSES/ORIGINAL-FORK-NOTICE.txt)

<a id="credits-and-license"></a>
## Crediti e licenza

Diritto d'autore (c) 2016 Orbmu2k. Il [Licenza MIT](../../../../NVIDIA-Profile-Inspector/LICENSE) fornito viene mantenuto. Adattamenti e confezionamento: 禅堂 Zendo (RevoluSound Team). Il programma di installazione utilizza Inno Setup; Windows e .NET Framework rimangono esterni. [Avvisi completi applicabili](LICENSES/README.md).

Indipendente da, non sponsorizzato e non ufficialmente approvato da NVIDIA Corporation. I marchi rimangono dei rispettivi proprietari.
