<!-- nv-language-navigation:start -->
🌐 [English](../../../releasing.md) | [Français](../../../releasing.fr.md) · [NV Laboratory](../README.md)

<details>
<summary>🌐 Language · 34</summary>

[العربية](../../ar/docs/releasing.md) · [বাংলা](../../bn/docs/releasing.md) · [简体中文](../../zh/docs/releasing.md) · [Čeština](../../cs/docs/releasing.md) · [Dansk](../../da/docs/releasing.md) · [Nederlands](../../nl/docs/releasing.md) · [English](../../../releasing.md) · [Filipino](../../fil/docs/releasing.md) · [Suomi](../../fi/docs/releasing.md) · [Français](../../../releasing.fr.md) · [Deutsch](../../de/docs/releasing.md) · [Ελληνικά](../../el/docs/releasing.md) · [हिन्दी](../../hi/docs/releasing.md) · [Magyar](../../hu/docs/releasing.md) · [Bahasa Indonesia](../../id/docs/releasing.md) · **Italiano** · [日本語](../../ja/docs/releasing.md) · [한국어](../../ko/docs/releasing.md) · [मराठी](../../mr/docs/releasing.md) · [فارسی](../../fa/docs/releasing.md) · [Polski](../../pl/docs/releasing.md) · [Português](../../pt/docs/releasing.md) · [ਪੰਜਾਬੀ](../../pa/docs/releasing.md) · [Română](../../ro/docs/releasing.md) · [Русский](../../ru/docs/releasing.md) · [Español](../../es/docs/releasing.md) · [Kiswahili](../../sw/docs/releasing.md) · [Svenska](../../sv/docs/releasing.md) · [தமிழ்](../../ta/docs/releasing.md) · [ไทย](../../th/docs/releasing.md) · [Türkçe](../../tr/docs/releasing.md) · [Українська](../../uk/docs/releasing.md) · [اردو](../../ur/docs/releasing.md) · [Tiếng Việt](../../vi/docs/releasing.md)

[Translation policy](../../README.md)

</details>
<!-- nv-language-navigation:end -->

<!-- nv-translation-notice:start -->
> Traduzione assistita da macchina dall'inglese. Nomi tecnici, comandi, URL e testi legali originali vengono conservati. È gradita la recensione da parte di madrelingua; consultare il riferimento inglese se la formulazione non è chiara.
<!-- nv-translation-notice:end -->

<a id="publishing-and-releases"></a>
# Pubblicazioni e rilasci

L'archivio pubblico è **Zendo-GIT/NV-Laboratory**. Le modifiche alla documentazione vengono riviste, confermate e inviate dal manutentore con **GitHub Desktop**. Un commit locale non carica file. I pacchetti binari sono risorse di rilascio GitHub separate; non appartengono mai all'elenco delle modifiche Git.

<a id="documentation-updates"></a>
## Aggiornamenti della documentazione

1. Aprire la cartella **NV-Laboratory** in GitHub Desktop.
2. Esamina la documentazione, gli avvisi, le immagini, i metadati JSON e il validatore della documentazione.
3. Esegui `python tools/validate_repository.py` da quella cartella.
4. Applica le modifiche riviste, quindi utilizza **Push origin**. Controlla il risultato delle Azioni.
5. Conserva l'identità pubblica dell'autore **禅堂 Zendo (RevoluSound Team)** e l'indirizzo GitHub `noreply` dell'account.

Non selezionare mai l'area di lavoro di sviluppo padre, la directory di controllo privata o la directory degli allegati binari. [Impegna la privacy della posta elettronica](https://docs.github.com/en/account-and-profile/how-tos/email-preferences/setting-your-commit-email-address).

<a id="independent-application-releases"></a>
## Rilasci di applicazioni indipendenti

| Strumento | Etichetta | Politica della versione |
| --- | --- | --- |
| NVIDIA Profile Inspector – NV Tools Fork | nvpi-v3.0.2.3 | Versione esistente dell'applicazione in quattro parti; la revisione 2 dell'installazione ha il proprio nome file |
| NVDriverForge | nvdriverforge-v0.1.3 | Schema 0.x esistente; gli aggiornamenti con versione preservano i pacchetti precedenti |
| NVMFG Unlock40 | nvmfg-unlock40-v0.1.1 | Candidato UI2 identificato da hash esatti senza inventare una nuova versione dell'applicazione |
| NVRasterPulse | nvrasterpulse-v0.1 | Versione esistente in due parti |

Il manutentore può pubblicare direttamente o autorizzare un assistente a pubblicare le risorse controllate. La pubblicazione è esplicita; nessun flusso di lavoro crea una versione su ciascun commit.

1. Esaminare l'attuale rapporto pre-pubblicazione, le origini dei file binari, le licenze e i valori SHA-256.
2. Crea una bozza per il tag dello strumento, prendendo di mira il commit dell'hub rivisto. Includere le note di rilascio specifiche della versione preparate.
3. Allega solo le risorse di configurazione/portatili di quella versione, `Licenses-and-Credits.zip` e `SHA256SUMS.txt`.
4. Verifica compatibilità, installazione, dipendenze, modifiche e limiti noti. Mantieni RTSS in primo piano per NVRasterPulse.
5. Pubblica, verifica gli URL, le dimensioni e gli hash delle risorse pubbliche e registra la data di pubblicazione effettiva in `docs/releases.json`.
6. Aggiorna le pagine di download e le traduzioni, quindi conferma/inserisci le modifiche in GitHub Desktop.

I collegamenti ai tag per progetto evitano di inviare gli utenti a un altro strumento tramite un collegamento `releases/latest` condiviso. Gli archivi automatici **Source code** di GitHub contengono questo hub di documentazione. Le origini delle applicazioni rimangono private. Gli avvisi sui componenti originali rimangono intatti e un rilascio non risolve la riserva documentata NVIDIA SDK di NVMFG.

<a id="integrity-and-storage"></a>
## Integrità e conservazione

Non sostituire mai silenziosamente i byte binari pubblicati. Utilizza una nuova versione esplicita o una revisione del programma di installazione con nuovi hash. I sidecar legali integrano gli avvisi incorporati. NVDriverForge 0.1.3 portatile è di 141.760.351 byte, superiore al normale limite di file Git di 100 MiB di GitHub. Gli allegati di rilascio evitano di inserire file binari o Git LFS in questo hub. [Guida per file di grandi dimensioni GitHub](https://docs.github.com/en/repositories/working-with-files/managing-large-files/about-large-files-on-github).

La segnalazione privata delle vulnerabilità deve essere abilitata nelle impostazioni di sicurezza del repository. Verificarne la disponibilità prima di indirizzarvi segnalazioni sensibili; [SECURITY.md](../SECURITY.md) fornisce un fallback che non espone i dettagli della vulnerabilità.

[Scarica il catalogo](downloads.md) · [Documentazione sulla versione GitHub](https://docs.github.com/en/repositories/releasing-projects-on-github/managing-releases-in-a-repository)
