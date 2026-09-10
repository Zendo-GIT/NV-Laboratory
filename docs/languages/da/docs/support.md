<!-- nv-language-navigation:start -->
🌐 [English](../../../support.md) | [Français](../../../support.fr.md) · [NV Laboratory](../README.md)

<details>
<summary>🌐 Language · 34</summary>

[العربية](../../ar/docs/support.md) · [বাংলা](../../bn/docs/support.md) · [简体中文](../../zh/docs/support.md) · [Čeština](../../cs/docs/support.md) · **Dansk** · [Nederlands](../../nl/docs/support.md) · [English](../../../support.md) · [Filipino](../../fil/docs/support.md) · [Suomi](../../fi/docs/support.md) · [Français](../../../support.fr.md) · [Deutsch](../../de/docs/support.md) · [Ελληνικά](../../el/docs/support.md) · [हिन्दी](../../hi/docs/support.md) · [Magyar](../../hu/docs/support.md) · [Bahasa Indonesia](../../id/docs/support.md) · [Italiano](../../it/docs/support.md) · [日本語](../../ja/docs/support.md) · [한국어](../../ko/docs/support.md) · [मराठी](../../mr/docs/support.md) · [فارسی](../../fa/docs/support.md) · [Polski](../../pl/docs/support.md) · [Português](../../pt/docs/support.md) · [ਪੰਜਾਬੀ](../../pa/docs/support.md) · [Română](../../ro/docs/support.md) · [Русский](../../ru/docs/support.md) · [Español](../../es/docs/support.md) · [Kiswahili](../../sw/docs/support.md) · [Svenska](../../sv/docs/support.md) · [தமிழ்](../../ta/docs/support.md) · [ไทย](../../th/docs/support.md) · [Türkçe](../../tr/docs/support.md) · [Українська](../../uk/docs/support.md) · [اردو](../../ur/docs/support.md) · [Tiếng Việt](../../vi/docs/support.md)

[Translation policy](../../README.md)

</details>
<!-- nv-language-navigation:end -->

<!-- nv-translation-notice:start -->
> Maskinassisteret oversættelse fra engelsk. Tekniske navne, kommandoer, URL'er og originale lovtekster er bevaret. Native-speaker anmeldelse er velkommen; se den engelske reference, hvis ordlyden er uklar.
<!-- nv-translation-notice:end -->

<a id="compatibility-and-troubleshooting"></a>
# Kompatibilitet og fejlfinding

Disse er de forberedte kandidater, ikke en certificeringsmatrix for alle Windows, GPU, driver og spilkombinationer.

| Værktøj | Windows / køretid | Hardware / ekstern afhængighed | Operationer, der kræver pleje |
| --- | --- | --- | --- |
| NVPI fork 3.0.2.3 | Windows 10/11 x64, .NET Framework 4.8 | Kompatibel NVIDIA driver/skærm | Profil skriver og viser forhåndsvisninger |
| NVDriverForge 0.1.2 | Windows 10 build 19041+ / 11 x64; .NET/WPF inkluderet | Kompatibel NVIDIA driverpakke | Forhøjet installation, avancerede indstillinger, valgfri NVENC |
| NVMFG Unlock40 0.1.1 | Windows 10/11 x64; .NET/WPF inkluderet, Framework 4.8 hjælpere | RTX 40, kvalificeret DLSS FG-spil og fastgjort udbyder | Native in-game patching, global profiljournal, SDK spilopdateringer |
| NVRasterPulse 0.1 | Windows 10/11 x64, .NET Framework 4.8 | RTSS installeret; løber efter kasketter | RTSS pr. eksekverbare profilændringer |

Ingen ARM64-pakke er forberedt. Display/API tilgængelighed og gamle Windows versioner kan begrænse individuelle funktioner. Ingen universel minimumsversion af NVIDIA eller RTSS er opfundet. Den nøjagtige NVMFG-udbyder-hash er i [herkomst](provenance.md).

<a id="before-reporting-a-bug"></a>
## Før du rapporterer en fejl

Identificer den nøjagtige eksekverbare/version, du åbnede. En tidligere installeret kopi er ikke nødvendigvis versionen af ​​en nyligt downloadet ZIP. Registrer reproduktionstrinene, forventet resultat og faktisk resultat. For renderings-/begrænsningsproblemer skal du inkludere spilversion, skærmopdatering, FG/V-Sync/VRR-tilstand og enhver anden limiter eller overlay.

Brug [fejlform](https://github.com/Zendo-GIT/NV-Laboratory/issues/new?template=bug-report.yml). Vedhæft aldrig en hel privat udviklingsmappe, driverarkiv, model, spil-DLL, registreringsdump eller ugennemgået logsamling.

| Problem | Første kontrol |
| --- | --- |
| Forkert applikationsversion | Bekræft EXE-identitet og frigiv hash; luk den ældre kopi før udskiftning. |
| Runtime/startfejl | Installer påkrævet Framework 4.8 eller behold alle medfølgende bærbare undermapper. |
| UAC annulleret | Prøv kun den tilsigtede handling igen; annullering er ikke vellykket installation. |
| Hash/signatur uoverensstemmelse | Stop med at bruge den kandidat og få de forventede officielle bytes. |
| NVPI farve/tilstand afvist | Vend tilbage og brug en kombination, der understøttes af det aktuelle display/driver. |
| NVDF sikkerhedskopiering eller gendannelsesfejl | Bevar beskyttet job og RECOVERY.txt; slet ikke journalen eller fremtving modstridende skrivninger. |
| NVMFG afventende indstillinger | Løs gendannelse med lukkede spil, og bevar ændringer fra andre værktøjer. |
| RP-hætten har ingen effekt | Kør RTSS, identificer den rigtige spil-EXE, inspicér hook-tilstand og konkurrerende grænser. |
| RP hætten fortsætter efter fjernelse | Undersøg RTSS Global; ændringer i fjernelse kun lokal begrænser tilsidesætter. |

<a id="logs-and-privacy"></a>
## Logfiler og privatliv

| Værktøj | Lokale data til gennemgang, ikke upload engros |
| --- | --- |
| NVDF | `%LOCALAPPDATA%\NVDriverForge`; beskyttede job `%PROGRAMDATA%\NVDriverForge\Jobs` |
| NVMFG | `%LOCALAPPDATA%\RtxMfg`; sikkerhedskopier `%LOCALAPPDATA%\NvidiaStreamlineMaintenance\Backups`; `Sessions` ved siden af EXE |
| RP | `%LOCALAPPDATA%\NVRasterPulse`; `Backups\RTSS` under det |
| NVPI | Dine valgte eksporter og den viste fejl; ingen opfundet universel log-sti |

Fjern kontonavne, hjemmemapper, spilbiblioteksstier, enhedsidentifikatorer, tokens og ikke-relaterede vinduer fra den tekst/billeder, du deler. Opbevar originalerne privat til gendannelse. Offentlige spørgsmål er synlige for alle.

For en sårbarhed, farlig privilegeret adfærd eller utilsigtet destruktiv handling skal du følge [SECURITY.md](../SECURITY.md) i stedet for at offentliggøre detaljer.

<a id="what-has-been-verified"></a>
## Hvad er verificeret

Til hub-forberedelse blev der kørt statisk nyttelast/ZIP/hash/metadata-scanninger og dokumentationstjek. Eksisterende private applikationsopbygning/enhed/UI-tests er historiske, daterede beviser. Ingen driverinstallation, skærmændring, live RTSS-drift eller spilbenchmark blev udført som en del af denne forberedelse.

"Opdaget", "skrevet", "genindlæst", "tilgængelig kapacitet" og "målt i spil" er forskellige resultater. Rapporter, hvilken du har observeret.
