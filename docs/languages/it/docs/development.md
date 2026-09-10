<!-- nv-language-navigation:start -->
🌐 [English](../../../development.md) | [Français](../../../development.fr.md) · [NV Laboratory](../README.md)

<details>
<summary>🌐 Language · 34</summary>

[العربية](../../ar/docs/development.md) · [বাংলা](../../bn/docs/development.md) · [简体中文](../../zh/docs/development.md) · [Čeština](../../cs/docs/development.md) · [Dansk](../../da/docs/development.md) · [Nederlands](../../nl/docs/development.md) · [English](../../../development.md) · [Filipino](../../fil/docs/development.md) · [Suomi](../../fi/docs/development.md) · [Français](../../../development.fr.md) · [Deutsch](../../de/docs/development.md) · [Ελληνικά](../../el/docs/development.md) · [हिन्दी](../../hi/docs/development.md) · [Magyar](../../hu/docs/development.md) · [Bahasa Indonesia](../../id/docs/development.md) · **Italiano** · [日本語](../../ja/docs/development.md) · [한국어](../../ko/docs/development.md) · [मराठी](../../mr/docs/development.md) · [فارسی](../../fa/docs/development.md) · [Polski](../../pl/docs/development.md) · [Português](../../pt/docs/development.md) · [ਪੰਜਾਬੀ](../../pa/docs/development.md) · [Română](../../ro/docs/development.md) · [Русский](../../ru/docs/development.md) · [Español](../../es/docs/development.md) · [Kiswahili](../../sw/docs/development.md) · [Svenska](../../sv/docs/development.md) · [தமிழ்](../../ta/docs/development.md) · [ไทย](../../th/docs/development.md) · [Türkçe](../../tr/docs/development.md) · [Українська](../../uk/docs/development.md) · [اردو](../../ur/docs/development.md) · [Tiếng Việt](../../vi/docs/development.md)

[Translation policy](../../README.md)

</details>
<!-- nv-language-navigation:end -->

<!-- nv-translation-notice:start -->
> Traduzione assistita da macchina dall'inglese. Nomi tecnici, comandi, URL e testi legali originali vengono conservati. È gradita la recensione da parte di madrelingua; consultare il riferimento inglese se la formulazione non è chiara.
<!-- nv-translation-notice:end -->

<a id="repository-architecture-and-maintenance"></a>
# Architettura e manutenzione del repository

NV Laboratory è un **hub pubblico di documentazione e distribuzione binaria**. Non contiene l'origine dell'applicazione. I quattro progetti mantengono alberi di build, versioni, identità e risorse di rilascio separati. La loro cronologia di sviluppo privata non viene importata in questo repository Git.

<a id="layout"></a>
## Disposizione

| Posizione | Scopo |
| --- | --- |
| README.md / README.fr.md | Punti di ingresso inglese/francese |
| Quattro cartelle di progetto | Guide complete e avvisi originali applicabili |
| documenti | Download, compatibilità, provenienza, procedura di sviluppo e rilascio |
| docs/releases.json | Metadati, dimensioni e hash del candidato/rilascio controllati |
| documenti/provenienza | Confronti file/hash; nessun codice dell'applicazione |
| licenze | Condivisione di testi completi di terze parti e crediti del traduttore installatore |
| beni | Anteprime dell'interfaccia utente riviste esistenti e relativa provenienza |
| .github | Emissione di moduli e convalida della documentazione di sola lettura |
| strumenti/validate_repository.py | Controlli dei limiti di pubblicazione e dei collegamenti della libreria standard |

L'inglese rimane il README GitHub predefinito. I collegamenti `.fr.md` adiacenti esistenti rimangono validi. Ulteriori traduzioni rispecchiano la documentazione in `docs/languages/<code>`; il selettore della lingua mantiene la stessa pagina quando si cambia lingua. Il catalogo `docs/languages/catalog.json` registra tutte le 34 lingue e le impronte digitali di origine. GitHub non seleziona automaticamente un README in base alla lingua del browser. Vedere [indice linguistico e politica di traduzione](../../README.md).

<a id="application-technologies"></a>
## Tecnologie applicative

| Programma | Tecnologia privata | Distribuzione |
| --- | --- | --- |
| NVPI fork | Interoperabilità C#, WPF, .NET Framework 4.8, NVAPI/Windows | Cartella portatile completa e Inno Setup separata |
| NVDriverForge | C#, WPF, .NET 8; bootstrap nativo C++; Processo 7-Zip | EXE portatile autonomo e installazione |
| NVMFG Unlock40 | C#/WPF .NET 8, helper Framework 4.8, motore C++20/MASM/MinHook | Albero e configurazione portatili |
| NVRasterPulse | C#/WPF Quadro 4.8; Integrazione profilo/ricarica RTSS; bootstrap nativo | Albero e configurazione portatili |

Questo checkout pubblico non può ricostruire le applicazioni. Gli archivi automatici "Source code" sono snapshot dell'hub. I collegamenti alla fonte upstream non rappresentano l'esatta fonte privata modificata. L'elemento della configurazione pubblico convalida solo questo repository.

<a id="local-checks"></a>
## Controlli locali

Dalla radice del repository:

```text
python tools/validate_repository.py
```

Python 3.10 o successivo è sufficiente. Il controllo legge file, collegamenti Markdown locali, avvisi richiesti/collegamenti RTSS, metadati di rilascio e limiti di pubblicazione. Non esegue il software, non installa dipendenze né contatta una rete.

Il flusso di lavoro GitHub esegue lo stesso controllo con l'autorizzazione dei contenuti di sola lettura su richiesta push, pull o invio manuale. Il checkout è bloccato su un commit controllato e non mantiene le credenziali. Non è configurato alcun processo di rilascio o distribuzione.

<a id="maintain-the-boundary"></a>
## Mantenere il confine

Aggiorna insieme il riferimento inglese, le guide francesi e le traduzioni interessate. Mantieni le modifiche sostanziali separate dai confronti di sola formattazione. Registrare gli hash candidati effettivi, i riferimenti ai commit upstream e le licenze; non dedurre mai una licenza dalla popolarità di un progetto.

Utilizza risorse di rilascio con nuove versioni e verifica nuovamente i file binari, gli archivi e gli avvisi incorporati modificati. Conserva i backup privati ​​all'esterno di questo repository. Non utilizzare un flusso di lavoro pubblico per importare l'origine dell'applicazione privata o le cartelle di build locali.

I test appropriati per una modifica funzionale dell'applicazione vengono eseguiti nel progetto privato. Non eseguire nuovamente i programmi di installazione dei driver né scrivere profili reali per un aggiornamento della documentazione. [Procedura di rilascio manuale](releasing.md).
