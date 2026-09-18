<!-- nv-language-navigation:start -->
🌐 [English](../../../installation.md) | [Français](../../../installation.fr.md) · [NV Laboratory](../README.md)

<details>
<summary>🌐 Language · 34</summary>

[العربية](../../ar/docs/installation.md) · [বাংলা](../../bn/docs/installation.md) · [简体中文](../../zh/docs/installation.md) · [Čeština](../../cs/docs/installation.md) · [Dansk](../../da/docs/installation.md) · [Nederlands](../../nl/docs/installation.md) · [English](../../../installation.md) · [Filipino](../../fil/docs/installation.md) · [Suomi](../../fi/docs/installation.md) · [Français](../../../installation.fr.md) · [Deutsch](../../de/docs/installation.md) · [Ελληνικά](../../el/docs/installation.md) · [हिन्दी](../../hi/docs/installation.md) · [Magyar](../../hu/docs/installation.md) · [Bahasa Indonesia](../../id/docs/installation.md) · **Italiano** · [日本語](../../ja/docs/installation.md) · [한국어](../../ko/docs/installation.md) · [मराठी](../../mr/docs/installation.md) · [فارسی](../../fa/docs/installation.md) · [Polski](../../pl/docs/installation.md) · [Português](../../pt/docs/installation.md) · [ਪੰਜਾਬੀ](../../pa/docs/installation.md) · [Română](../../ro/docs/installation.md) · [Русский](../../ru/docs/installation.md) · [Español](../../es/docs/installation.md) · [Kiswahili](../../sw/docs/installation.md) · [Svenska](../../sv/docs/installation.md) · [தமிழ்](../../ta/docs/installation.md) · [ไทย](../../th/docs/installation.md) · [Türkçe](../../tr/docs/installation.md) · [Українська](../../uk/docs/installation.md) · [اردو](../../ur/docs/installation.md) · [Tiếng Việt](../../vi/docs/installation.md)

[Translation policy](../../README.md)

</details>
<!-- nv-language-navigation:end -->

<!-- nv-translation-notice:start -->
> Traduzione assistita da macchina dall'inglese. Nomi tecnici, comandi, URL e testi legali originali vengono conservati. È gradita la recensione da parte di madrelingua; consultare il riferimento inglese se la formulazione non è chiara.
<!-- nv-translation-notice:end -->

<a id="installation-guide"></a>
# Guida all'installazione

Inizia con [Download](downloads.md), che registra lo stato di pubblicazione e i nomi esatti delle risorse. Si tratta di strumenti separati: installa solo quelli che ti servono.

> **Per NVRasterPulse, installare [RTSS di Guru3D](https://www.guru3d.com/download/rtss-rivatuner-statistics-server-download/) prima di aprire il gestore profili.**
> RTSS deve essere eseguito per applicare i limiti; non è incluso in NV Tools.

| Strumento | Edizione installata | Edizione portatile | Prerequisito principale |
| --- | --- | --- | --- |
| NVIDIA Profile Inspector – NV Tools Fork | NVPI-CustomNV-3.0.2.3-Setup-r2.exe | Estrai NVPI ZIP completo | Driver NVIDIA e .NET Framework 4.8 |
| NVDriverForge | NVDriverForge-Setup.exe | NVDriverForge.exe, tempo di esecuzione incluso | Pacchetto driver originale NVIDIA compatibile per le operazioni di installazione |
| NVMFG Unlock40 | NVMFGUnlock40-0.2.3-Setup-x64.exe | Estrai lo ZIP NVMFG completo, conserva le sottocartelle | RTX 40, DLSS FG esistente, provider esatto e helper .NET Framework 4.8 |
| NVRasterPulse | NVRasterPulse-0.2-win-x64-Setup.exe | Estrai RP ZIP completo | RTSS e .NET Framework 4.8 |

<a id="download-verify-install"></a>
## Scarica, verifica, installa

1. Sulla Release pubblicata prescelta, scaricare il relativo asset applicativo denominato, avvisi ZIP e SHA256SUMS.txt.
2. Utilizza [Esempio SHA-256](downloads.md#sha-256), con il nome file effettivamente scaricato.
3. Per l'installazione, seguire il normale programma di installazione. Per ZIP portatile, estrai tutto in una nuova cartella scrivibile locale; non eseguire dall'interno dello ZIP.
4. Apri l'EXE dell'applicazione. Conservare i file di licenza/configurazione/dati allegati.
5. Leggi le istruzioni per l'uso dello strumento prima di abilitare le impostazioni o le operazioni di sistema.

I binari attuali non sono firmati. Un hash corrispondente conferma i byte attesi; non è un certificato di sicurezza o compatibilità. Non disabilitare le protezioni di sicurezza Windows solo per sopprimere un avviso.

L'installazione di NVDF o del suo compagno opzionale NVPI è separata dall'installazione di un driver GPU. Il compagno NVPI mantiene il nome dell'installazione interna esistente. Il suo pulsante RasterPulse rialzato richiede un'installazione protetta a livello di sistema; altre copie di RP possono essere aperte tramite le proprie scorciatoie.

NVMFG è sperimentale e ha [riserva di licenza NVIDIA SDK documentata](provenance.md). Non è incluso alcun driver NVIDIA, provider/modello NGX o runtime del gioco Streamline. I download selezionati di SDK e gli aggiornamenti dei giochi sono operazioni esplicite separate.

<a id="language-and-updates"></a>
## Lingua e aggiornamenti

Utilizzare il selettore di 34 lingue del README per la documentazione. NVDF, NVMFG e RP hanno la propria impostazione dell'interfaccia utente in 34 lingue; NVPI mantiene il supporto linguistico esistente. Alcune stringhe tecniche dell'installatore ricadono nell'inglese.

Conserva l'identità di installazione di uno strumento durante l'aggiornamento. Chiudilo prima e conserva i backup. Per NVMFG, chiudi i giochi interessati e risolvi il ripristino del profilo in sospeso. Per gli aggiornamenti portatili, utilizzare una nuova cartella anziché combinare le versioni.

<a id="removing-a-tool"></a>
## Rimozione di uno strumento

La disinstallazione di un'applicazione non annulla automaticamente le sue impostazioni.

- **NVPI:** ripristina i profili/impostazioni di visualizzazione previsti prima della rimozione, se necessario.
- **NVDF:** utilizza prima il ripristino se desideri ripristinare le modifiche avanzate/NVENC. Uninstall lascia il driver grafico, le impostazioni e i backup.
- **NVMFG:** chiudi i giochi, disabilita/esci dal controller, risolvi il ripristino NVIDIA e ripristina i backup del gioco SDK desiderati prima della rimozione.
- **RP:** rimuovere prima le sostituzioni del limitatore previste. Uninstall non cancella i cappucci RTSS salvati né rimuove RTSS.

Consulta ciascun [guida al progetto](../README.md#projects) per le posizioni esatte dei dati e le limitazioni oppure [supporto](support.md) se un passaggio di ripristino non riesce.
