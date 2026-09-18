<!-- nv-language-navigation:start -->
🌐 [English](../../../provenance.md) | [Français](../../../provenance.fr.md) · [NV Laboratory](../README.md)

<details>
<summary>🌐 Language · 34</summary>

[العربية](../../ar/docs/provenance.md) · [বাংলা](../../bn/docs/provenance.md) · [简体中文](../../zh/docs/provenance.md) · [Čeština](../../cs/docs/provenance.md) · **Dansk** · [Nederlands](../../nl/docs/provenance.md) · [English](../../../provenance.md) · [Filipino](../../fil/docs/provenance.md) · [Suomi](../../fi/docs/provenance.md) · [Français](../../../provenance.fr.md) · [Deutsch](../../de/docs/provenance.md) · [Ελληνικά](../../el/docs/provenance.md) · [हिन्दी](../../hi/docs/provenance.md) · [Magyar](../../hu/docs/provenance.md) · [Bahasa Indonesia](../../id/docs/provenance.md) · [Italiano](../../it/docs/provenance.md) · [日本語](../../ja/docs/provenance.md) · [한국어](../../ko/docs/provenance.md) · [मराठी](../../mr/docs/provenance.md) · [فارسی](../../fa/docs/provenance.md) · [Polski](../../pl/docs/provenance.md) · [Português](../../pt/docs/provenance.md) · [ਪੰਜਾਬੀ](../../pa/docs/provenance.md) · [Română](../../ro/docs/provenance.md) · [Русский](../../ru/docs/provenance.md) · [Español](../../es/docs/provenance.md) · [Kiswahili](../../sw/docs/provenance.md) · [Svenska](../../sv/docs/provenance.md) · [தமிழ்](../../ta/docs/provenance.md) · [ไทย](../../th/docs/provenance.md) · [Türkçe](../../tr/docs/provenance.md) · [Українська](../../uk/docs/provenance.md) · [اردو](../../ur/docs/provenance.md) · [Tiếng Việt](../../vi/docs/provenance.md)

[Translation policy](../../README.md)

</details>
<!-- nv-language-navigation:end -->

<!-- nv-translation-notice:start -->
> Maskinassisteret oversættelse fra engelsk. Tekniske navne, kommandoer, URL'er og originale lovtekster er bevaret. Native-speaker anmeldelse er velkommen; se den engelske reference, hvis ordlyden er uklar.
<!-- nv-translation-notice:end -->

<a id="provenance-changes-and-licensing"></a>
# Herkomst, ændringer og licensering

Denne revision beskriver kandidaterne udarbejdet den **2026-09-18**. Applikationskilder forbliver private; de offentlige fortegnelser indeholder filnavne og hashes, ikke kildekode. Se [meddelelser om fuld komponent](../THIRD_PARTY_NOTICES.md).

<a id="nvidia-profile-inspector--nv-tools-fork"></a>
## NVIDIA Profile Inspector – NV Tools Fork

Reference: Orbmu2k/nvidiaProfileInspector commit `592d962cca8827efe8859461a84267755595064a`; kandidat eksekverbar version 3.0.2.3. Reference-commit og fork's assembly-version er forskellige identifikatorer; ingen upstream-udgivelsesversion udledes af fork-versionen.

Den rene ledsagers 157 kilde-/ressourcefiler blev sammenlignet med denne commit: 2 byte-identiske, 134 adskiller sig kun i linjeafslutninger eller UTF-8 BOM, 11 modificerede, 10 fraværende ved den sammenlignede opstrømssti. "Tilføjet" er i forhold til denne sti og er ikke i sig selv et bevis på det oprindelige forfatterskab.

[Komplet fil/hash sammenligning](../../../provenance/nvpi-source-provenance.json).

| Område | Nedarvet arbejde | Fork bidrag |
| --- | --- | --- |
| Profil redaktør | Profilmodel, import/eksport, applikationstilknytninger og referencedata | Integration med Screen og den eksterne værktøjsstarter |
| NVAPI | Orbmu2k's DRS-interop | Farve/skærm-relateret interoperabilitet, native-loading-restriktioner for produktion og falsk fjernelse |
| Vis tjenester | Windows/NVIDIA API'er som eksterne grænseflader | DisplayInfoService, DisplayConfigurationService, DisplaySettingsBackend |
| UI | Upstream WPF ressourcer, paletter og ikoner | Skærmdialoger, 15 sekunders bekræftelse, status/tilbagelæsning og værktøjslinjelayout |
| Launcher | Eksisterende app-skal | Beskyttet separat installeret RasterPulse-opslag og start |
| Emballage | MIT opstrøms | Ren selvstændig ledsager, separat installatør/afinstallationsprogram, bevarede meddelelser |

Det offentlige kildekort inkluderer løsnings-/ressourcestier til sporbarhed; disse filer distribueres ikke som kilde. Udviklingstest, mock-grænseflader og den gamle kombinerede NVPI/RasterPulse-binære er udelukket.

<a id="nvdriverforge"></a>
## NVDriverForge

Uafhængig C#/.NET 8/WPF-applikation; den brugervendte arbejdsgang er delvist inspireret af NVCleanstall. Ingen NVCleanstall-kilde/binær blev identificeret i produktionsnyttelasten. Det er ikke repræsenteret som en fork af den proprietære applikation.

Oprindeligt projektarbejde inkluderer komponentanalyse/udvælgelse, beskyttede installationsjob, sikkerhedskopier og gendannelse af transaktioner, NVIDIA-katalogdownloads, opdateringstjek, lokaliserede forklaringer, valgfri avancerede/NVENC-arbejdsgange og installations-bootstrap.

Nedarvede/tilpassede komponenter: fire NVPI-temapaletter, udvidet NVAPI DRS-interfacereference og den separat valgfrie MIT NVPI-ledsager. Custom NV-forudindstillingens valg-UI og tilladelseslistede transaktionsintegration tilhører NVDriverForge; forudindstillingen er ikke en officiel NVIDIA-anbefaling.

7-Zip 26.03, .NET/WPF 8.0.31 og Inno Setup forbliver uændrede eksterne komponenter, der bruges under deres egne betingelser. keylase NVENC data er ikke indlejret; én nøjagtig commit vælges og kontrolleres, når brugeren anmoder om en kompatibel download. Der blev ikke etableret nogen omfordelingslicens for disse opstrømsdata.

<a id="nvmfg-unlock40"></a>
## NVMFG Unlock40

NVMFG Unlock40 blev udviklet uafhængigt af 禅堂 Zendo (RevoluSound Team). Vedligeholderen brugte RTX40MFG-Unlock til sammenligning og forfining. Ansøgningen som helhed præsenteres ikke som dens fork. Denne sondring fjerner ikke krediteringer for delte/tilpassede komponenter i det aktuelle oprindelige lag.

Sammenligningsreference: dashdogy/RTX40MFG-Unlock, Michael Robles, MIT, commit `4e776d068f91b4a665425542bb005dd57cc3d891`. Det private native-motortræ indeholder 48 sammenlignede filer: 35 kun formateringsforskelle, 4 modificerede filer og 9 fraværende på referencestien. [Fuldstændig sammenligning](../../../provenance/nvmfg-source-provenance.json).

Ændrede nedarvede filer: `entry_detour.h`, `patcher.cpp`, `temporal_interval_trace.cpp`, `temporal_interval_trace.h`. Yderligere stier omfatter `game_selection.*`, `ngx_bootstrap.*`, `ngx_capability.h`, `presentation_tracker.h`, `vsync_observer.*` og en bibeholdt upstream-licens.

Produktions C++ enheder: patcher, midpoint_fix, dlssg_provider_policy, entry_detour, nvidia_mfg_policy, temporal_interval_trace, ngx_bootstrap, game_selection og vsync_observer; plus entry_detour samling og MinHook buffer/krog/trampolin/HDE64. Den nedarvede ReShade-frontend, ældre shim-ressourcer og ubrugte CMake-mål er ikke en del af denne produktionskompilering.

De matchende komponenter dækker patching/udbyderpolitik og tidsmæssigt arbejde; deres copyright- og tilladelsesmeddelelser forbliver intakte. Den centrale NGX/bootstrap/controllerkoordinering, V-Sync-håndtering per spil, sessionsdiagnostik og Windows-applikation/SDK/backup-workflow er projektarbejde af 禅堂 Zendo (RevoluSound Team). Ovenstående tællinger beskriver filer, inklusive tredjeparts- og ubrugte filer, ikke en forfatterskabsprocent eller kronologien af ​​nogen af ​​projekternes idé.

Hjælperen tilpasser NVPI's NvapiDrsWrapper og NativeArrayHelper til en separat samling med projektautoriseret profillogik. Den gamle udviklingsmock-sti er udelukket. Delte familiepaletter stammer fra NVPI.

MinHook reference: `8fda4f5481fed5797dc2651cd91e238e9b3928c6`; den nedarvede kompilerede delmængde har ingen funktionelle lokale ændringer i sammenligningen. Streamline integrationsoverskrifter: 2.12; åben header-licens bekræftet på v2.12.0. NGX headerkilde: NVIDIA/DLSS commit `a291cc7d2cc642a51566f3dfd5376f635cd1b284`.

Kandidatmotor SHA-256: `C793770D329B99CD9C5C640317CE435BFE353CA2868E36CF5DCD4D5295EFAE13`.

Nødvendig udbyder SHA-256 i engine.json: `C64928FDB7C48A57722EA8EEF2662171EDC323473ADEA66C29A206A23F1A2BED`. En rapporteret 310.9-udbyderfamilie er ikke udskiftelig med denne nøjagtige hash. Ingen udbyder-DLL eller model er inkluderet.

**Udestående licenspunkt:** den fulde NVIDIA RTX SDK-licens, version 14. marts 2024, indeholder en sektion 4(d)-begrænsning, der er relevant for at omgå tekniske begrænsninger. Revisionen fastslår ikke tilladelse til denne anvendelse. At beholde MIT-motorlicensen, være gratis eller observere andre mods løser ikke denne separate betingelse. Kandidatforberedelse er ikke en juridisk godkendelse. Den originale korte overskriftsmeddelelse er suppleret med den fulde licens; dens Windows-1252-tekst leveres også som læsbar UTF-8, med originale bytes bibeholdt.

Den oprindelige sammenligning blev genberegnet for 0.2.3: de samme 48 filer og klassifikationer. Siden den forrige revision er `game_selection.cpp`, `game_selection.h` og `patcher.cpp` ændret for observationer af aktivitet/kapacitet. Nye biblioteks-, diagnosticerings-, præference-, opdaterings- og udvælgelsesarbejdsgange hører til vedligeholdelsesapplikationen. Komponentlicenser og den påkrævede udbyder-hash er uændret.

<a id="nvrasterpulse"></a>
## NVRasterPulse

Uafhængig RTSS-profilmanager udviklet i det NVPI-afledte lager. De nedarvede MIT UI-ressourcer/-paletter og projektets oprindelse forbliver krediteret. Produktionsappen bruger eksplicit den medfølgende MIT-licens.

Projektarbejde: præcis RTSS-profilparsing/skrivning og fraktioneret kodning, sikkerhedskopiering, fjernelse af tilsidesættelse, genindlæsningsbro, forudsætningsdetektering, kompakt brugergrænseflade, bakkelivscyklus, opstartskontroller og lokalisering. RTSS udfører faktisk begrænsning.

Ingen RTSS-kilde, hook-DLL, SDK eller installationsprogram er bundtet. Broen kalder eksporten i en eksisterende brugervalgt RTSS-installation. Ingen NVIDIA-driverpakke, native eksperimentel limiter, Framepacer, MinHook, ReShade eller DLSS runtime er i denne pakke.

<a id="assets-generated-data-and-tools"></a>
## Aktiver, genererede data og værktøjer

[Aktivkreditter](../assets/README.md) identificerer de eksisterende interface-forhåndsvisninger og NVPI-opsætningsvælgeren. De fiktive værdier i dem er mærket. Intet spil/Nexus-aktiv, personlig profil, privat ICC, firma NVIDIA-logo eller skrifttypefil er kopieret.

Genererede spilkompatibilitetsnavne nedarvet i NVMFG er en påvisningshjælp, ikke testbevis. Genererede installatørkataloger krediteres i [oversættermeddelelser](../../../../licenses/INSTALLER-TRANSLATORS.md). Genererede build-poster med absolutte stier forbliver private.

Private byggeværktøjer omfatter .NET SDK/MSBuild, Visual Studio C++/MASM, Windows SDK, PowerShell, Inno Setup og Python revisionsscripts. Deres compilere, headere, testløbere og fejlretningsaktiver distribueres ikke. Statisk frigivelse CRT forbliver under Microsoft's gældende værktøjskædevilkår.

<a id="scope-of-verification"></a>
## Omfang af verifikation

Den lokale revision inventerede alle filer i de tre udviklingsrødder, mens den ekskluderede Git-objektdatabaser og linkede mappemål. Aktiv kilde/dokumenter blev scannet; historiske bygninger blev inventaret og udelukket. Udvalgte ZIPs og aktuelle nyttelaster blev scannet og hashed; .NET bundterne blev dekomprimeret til yderligere inspektion. Den første revision kørte intet produkt, installationsprogram, spil, RTSS-proces eller driver.

Den senere NVPI-opsætningsrevision 2 løser selvstændigt sprogvalg ved hjælp af de delte Inno-kontroller og bootstrap. Lys/mørke private armaturer verificeret mus og tastatur navigation og alle 34 eksplicitte sprogkoder. Selve opsætningsvælgeren blev åbnet på et aldrig vist privat skrivebord og annulleret før installationen. Dens syv applikationsfiler og bærbare ZIP er uændrede. NVDriverForge 0.1.3 inkluderer den korrigerede ledsager og videresender stadig `/LANG`.

NVDriverForge 0.1.3 blev afsluttet 2026-09-10. Dens private verifikationsrapport registrerer 366 applikationstests, 118 ledsagende tjek, 32 opsætningstjek, 156 indfødte sammenligninger og 34 sprogvideresendelsessager. Den beskyttede komponentvalgsfix blev afspillet mod en original driverpakke uden at ændre dens nyttelast eller installere driveren. Disse er daterede produktteamresultater, ikke test genudført af denne dokumentationsopdatering eller bevis på en vellykket, rigtig driverinstallation.

Denne hub-opdatering ændrer ingen funktionel applikationskode. Tidligere applikationsopbygning/enhed/UI-test forbliver dateret historisk bevis. Dette er ikke fuld reverse engineering af enhver tredjeparts binær eller en garanti mod ethvert muligt hemmeligt mønster.

18. september 2026-opdatering: NVDriverForge 0.1.4 tilføjer parathedstjek, native profil backup, komponentvejledning, præferencer og kits, detaljerede resultater, lokal rapportering og applikationsopdateringer. NVRasterPulse 0.2 tilføjer konfigurationsdiagnostik, FPS-vejledning, pause/genoptag, fortryd, `.nvrp`-profiler og favoritter/skjuler, uden en ny limiter-motor. Individuelle vejledninger beskriver brug og begrænsninger. Statiske hub-tjek er adskilt fra applikationstestene, der er registreret i de private rapporter den 18. september; ingen driverinstallation, import af ægte profil eller latensmåling blev udført for denne hub.
