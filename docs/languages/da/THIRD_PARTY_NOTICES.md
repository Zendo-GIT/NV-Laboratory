<!-- nv-language-navigation:start -->
🌐 [English](../../../THIRD_PARTY_NOTICES.md) | [Français](../fr/THIRD_PARTY_NOTICES.md) · [NV Laboratory](README.md)

<details>
<summary>🌐 Language · 34</summary>

[العربية](../ar/THIRD_PARTY_NOTICES.md) · [বাংলা](../bn/THIRD_PARTY_NOTICES.md) · [简体中文](../zh/THIRD_PARTY_NOTICES.md) · [Čeština](../cs/THIRD_PARTY_NOTICES.md) · **Dansk** · [Nederlands](../nl/THIRD_PARTY_NOTICES.md) · [English](../../../THIRD_PARTY_NOTICES.md) · [Filipino](../fil/THIRD_PARTY_NOTICES.md) · [Suomi](../fi/THIRD_PARTY_NOTICES.md) · [Français](../fr/THIRD_PARTY_NOTICES.md) · [Deutsch](../de/THIRD_PARTY_NOTICES.md) · [Ελληνικά](../el/THIRD_PARTY_NOTICES.md) · [हिन्दी](../hi/THIRD_PARTY_NOTICES.md) · [Magyar](../hu/THIRD_PARTY_NOTICES.md) · [Bahasa Indonesia](../id/THIRD_PARTY_NOTICES.md) · [Italiano](../it/THIRD_PARTY_NOTICES.md) · [日本語](../ja/THIRD_PARTY_NOTICES.md) · [한국어](../ko/THIRD_PARTY_NOTICES.md) · [मराठी](../mr/THIRD_PARTY_NOTICES.md) · [فارسی](../fa/THIRD_PARTY_NOTICES.md) · [Polski](../pl/THIRD_PARTY_NOTICES.md) · [Português](../pt/THIRD_PARTY_NOTICES.md) · [ਪੰਜਾਬੀ](../pa/THIRD_PARTY_NOTICES.md) · [Română](../ro/THIRD_PARTY_NOTICES.md) · [Русский](../ru/THIRD_PARTY_NOTICES.md) · [Español](../es/THIRD_PARTY_NOTICES.md) · [Kiswahili](../sw/THIRD_PARTY_NOTICES.md) · [Svenska](../sv/THIRD_PARTY_NOTICES.md) · [தமிழ்](../ta/THIRD_PARTY_NOTICES.md) · [ไทย](../th/THIRD_PARTY_NOTICES.md) · [Türkçe](../tr/THIRD_PARTY_NOTICES.md) · [Українська](../uk/THIRD_PARTY_NOTICES.md) · [اردو](../ur/THIRD_PARTY_NOTICES.md) · [Tiếng Việt](../vi/THIRD_PARTY_NOTICES.md)

[Translation policy](../README.md)

</details>
<!-- nv-language-navigation:end -->

<!-- nv-translation-notice:start -->
> Maskinassisteret oversættelse fra engelsk. Tekniske navne, kommandoer, URL'er og originale lovtekster er bevaret. Native-speaker anmeldelse er velkommen; se den engelske reference, hvis ordlyden er uklar.
<!-- nv-translation-notice:end -->

<a id="third-party-notices-and-credits"></a>
# Tredjeparts meddelelser og krediteringer

Indledende revision: 2026-09-09; NVDriverForge 0.1.3 og herkomstopdatering: 2026-09-10. **En komponents licens dækker denne komponent, ikke hele suiten.** Applikationskilden forbliver privat. Meddelelser om ophavsret og tilladelser bevares ordret; denne tabel er et indeks, ikke en erstatning for dem. "Ekstern" betyder ikke fordelt i applikationsaktiverne.

| Komponent / originalt projekt | Forfatter | Officiel side, arkiv eller download | Licens/meddelelse | Brug i NV Tools | Ændringer |
| --- | --- | --- | --- | --- | --- |
| NVIDIA Profile Inspector | Orbmu2k; Copyright 2016 | [Depot](https://github.com/Orbmu2k/nvidiaProfileInspector), [downloads](https://github.com/Orbmu2k/nvidiaProfileInspector/releases) | [MIT](../../../NVIDIA-Profile-Inspector/LICENSE) | Hele NVPI fork; NVDF-temaer/udvidet grænsefladereference; NVMFG indpakning/styles; RP UI-ressourcer | Fork displaytjenester, transaktioner og launcher; tema/kontrol integration og wrapper tilpasninger |
| RTX40MFG-Unlock | Michael Robles / dashdogy; Copyright 2026 | [Depot](https://github.com/dashdogy/RTX40MFG-Unlock), [downloads](https://github.com/dashdogy/RTX40MFG-Unlock/releases) | [MIT](../../../NVMFG-Unlock40/LICENSES/RTX40MFG-Unlock-MIT.txt) | Sammenligning/forfiningsreference og delte/tilpassede NVMFG-native komponenter; selvstændigt udviklet applikation | Central indlæsning, NGX/controller koordinering, per-spil/V-Sync integration og diagnostik |
| MinHook, fastgjort 8fda4f5 | Tsuda Kageyu; Copyright 2009–2017 | [Depot](https://github.com/TsudaKageyu/minhook), [fastgjort kilde](https://github.com/TsudaKageyu/minhook/tree/8fda4f5481fed5797dc2651cd91e238e9b3928c6) | [BSD 2-klausul meddelelse](../../../NVMFG-Unlock40/LICENSES/MinHook.txt) | Statisk kompileret i NVMFG-motor | Inkluderet delmængde uændret bortset fra tekstformatering mod den nedarvede kopi |
| Hacker Disassembler Engine (HDE64) | Vyacheslav Patkov; Copyright 2008–2009 | [MinHook's kildesamling](https://github.com/TsudaKageyu/minhook/tree/8fda4f5481fed5797dc2651cd91e238e9b3928c6/src/hde) | [Fuldstændige MinHook/HDE-meddelelser](../../../NVMFG-Unlock40/LICENSES/MinHook.txt) | MinHook dekoder i NVMFG | Ingen funktionelle ændringer identificeret; HDE32-meddelelse bevares, selvom produktionen bruger HDE64 |
| Streamline 2.12 integrationsoverskrifter | NVIDIA Corporation; Copyright 2023 | [Depot](https://github.com/NVIDIA-RTX/Streamline), [downloads](https://github.com/NVIDIA-RTX/Streamline/releases) | [MIT for kvalificerede overskrifter](../../../NVMFG-Unlock40/LICENSES/Streamline-MIT.txt) | Kompilerer NVMFG Streamline integration | Overskrifter ikke ændret; ingen runtime DLL i applikationspakken |
| NVIDIA NGX / DLSS SDK overskrifter | NVIDIA Corporation | [Fastgjort lager](https://github.com/NVIDIA/DLSS/tree/a291cc7d2cc642a51566f3dfd5376f635cd1b284), [SDK](https://developer.nvidia.com/rtx/dlss) | [NVIDIA RTX SDK vilkår](../../../NVMFG-Unlock40/LICENSES/NVIDIA-RTX-SDK.txt), [overskriftsmeddelelse](../../../NVMFG-Unlock40/LICENSES/NGX-Header-Notice.txt) | Kompilerer NVMFG NGX integration | Overskrifter ikke ændret; ingen NGX-model/udbyder medfølger; uløst begrænsning beskrevet nedenfor |
| .NET runtime 8.0.31 (NVDF) / 8.0.30 (NVMFG) | .NET Foundation, Microsoft og bidragydere | [Kilde](https://github.com/dotnet/runtime), [downloads](https://dotnet.microsoft.com/en-us/download/dotnet/8.0) | [MIT](../../../licenses/third-party/Microsoft-NET-LICENSE.txt) og [fuldstændige tredjepartsmeddelelser](../../../licenses/third-party/Microsoft-NET-THIRD-PARTY-NOTICES.txt) | Selvstændig NVDF og NVMFG app/agent | Runtime uændret |
| WPF / Windows Desktop Runtime 8.0.31 (NVDF) / 8.0.30 (NVMFG) | .NET Foundation, Microsoft og bidragydere | [Kilde](https://github.com/dotnet/wpf), [downloads](https://dotnet.microsoft.com/en-us/download/dotnet/8.0) | [MIT](../../../licenses/third-party/Microsoft-WPF-LICENSE.txt), runtime-meddelelser ovenfor | NVDF og NVMFG brugergrænseflader | Ramme uændret; applikations-UI forfattet/tilpasset separat |
| .NET Framework 4.8 | Microsoft | [Officiel runtime download](https://dotnet.microsoft.com/en-us/download/dotnet-framework/net48) | Microsoft platform/runtime vilkår; ydre | NVPI, RP og NVMFG profilhjælpere | Ingen; ingen installationsprogram eller ramme-DLL omfordelt af denne hub |
| 7-Zip 26.03 x64 | Igor Pavlov; Copyright 1999–2026 | [Site/downloads](https://www.7-zip.org/download.html), [nøjagtigt kildearkiv](https://github.com/ip7z/7zip/releases/download/26.03/7z2603-src.tar.xz) | [Fuld meddelelse](../../../licenses/third-party/7-Zip.txt), [LGPL 2.1-or-later](../../../licenses/third-party/LGPL-2.1.txt), BSD portioner og unRAR begrænsning | NVDF indlejrer umodificeret 7z.exe/7z.dll og kører CLI som en separat proces | Ingen ændringer |
| Inno Setup 7.1.0 | Jordan Russell, Martijn Laan og bidragydere | [Site/downloads](https://jrsoftware.org/isinfo.php), [kilde](https://github.com/jrsoftware/issrc) | [Original Inno Setup-licens](../../../licenses/third-party/Inno-Setup.txt) | Installationsmotorer og genererede afinstallationsprogrammer | Motor/kompilator uændret; projektmanuskripter, branding og native focus håndtering tilpasset |
| Inno Setup oversættelseskataloger | Navngivne originale oversættere | [Officiel samling](https://jrsoftware.org/files/istrans/) | Inno/katalog-meddelelser og [komplette header-kreditter](../../../licenses/INSTALLER-TRANSLATORS.md) | Delte 34-sprogede kataloger for alle fire installatører, inklusive NVPI setup revision 2 | Nøgler, ID'er, skrifttyper, teknisk engelsk fallback; projektforfattede forhåndsvisningskataloger, hvor det er nødvendigt |
| Microsoft Visual C++ runtime / Windows SDK support | Microsoft | [Visuelle Studio værktøjer](https://visualstudio.microsoft.com/downloads/), [omfordelingsvilkårsindeks](https://learn.microsoft.com/en-us/visualstudio/releases/2022/redistribution) | Microsoft værktøjskæde/runtime vilkår; ikke MIT af denne tabel | Statisk frigivelse af CRT i native engine/bootstrap binære filer; installerede Windows API'er | Ingen runtime kildeændringer; ingen compiler, SDK eller debug runtime distribueret |
| RivaTuner Statistics Server (RTSS) | Unwinder | [Officiel Guru3D download](https://www.guru3d.com/download/rtss-rivatuner-statistics-server-download/) | Leverandørvilkår; ingen omfordelingstilladelse udledt af "freeware" | Nødvendig ekstern begrænser til RP; installeret UpdateProfiles eksport | Ingen RTSS kode/binær modificeret eller bundtet; RP skriver valgte profilnøgler |
| NVIDIA driver / NVAPI / NVML | NVIDIA Corporation | [Driver downloads](https://www.nvidia.com/en-us/drivers/), [NVAPI](https://developer.nvidia.com/nvapi), [NVML](https://developer.nvidia.com/management-library-nvml) | NVIDIA driver/SDK vilkår; ydre | Installerede native grænseflader og eksplicitte downloads af originale drivere | Ingen NVIDIA DLL i hub-aktiver; NVDF's valgfri NVENC-operation ændrer brugervalgte installerede DLL'er |
| NVIDIA NGX udbyder/modeller og Streamline runtime | NVIDIA Corporation | [DLSS SDK](https://developer.nvidia.com/rtx/dlss), [Streamline frigives](https://github.com/NVIDIA-RTX/Streamline/releases) | Komponentspecifikke NVIDIA termer, adskilt fra MIT overskrifter | Eksterne spil-/driverkomponenter brugt af NVMFG; SDK hentes kun på forespørgsel | NVMFG anvender eksperimentelle adfærdsændringer i hukommelsen; SDK spilkopier kan opdateres med backup |
| keylase/nvidia-patch | keylase og bidragydere | [Depot](https://github.com/keylase/nvidia-patch), [Windows data](https://github.com/keylase/nvidia-patch/tree/master/win) | Omfordelingslicens er ikke etableret ved denne revision | Ekstern valgfri NVDF NVENC katalog/patch data, hentet fra én fastgjort commit pr. valg | Ingen opstrømskilde-, patcher- eller patchdata kopieret til hub-/applikationsaktiverne |
| NVCleanstall | TechPowerUp | [Officiel side/download](https://www.techpowerup.com/download/techpowerup-nvcleanstall/) | Proprietær distribution; ingen tilladelse til kilde/binær omfordeling udledt | Workflow og option inspiration til NVDF | Ingen importeret kilde eller binær; ikke en fork eller en runtime-afhængighed |

<a id="obligations-and-boundaries"></a>
## Forpligtelser og grænser

**MIT komponenter:** beholder copyright, tilladelsestekst og ansvarsfraskrivelse med kopier. Deres licens kræver ikke offentliggørelse af ændret kilde. Det oprindelige forfatterskab bevares, selv når applikationskilden vedligeholdes privat.

**MinHook/HDE:** bevarer meddelelser, betingelser og ansvarsfraskrivelser i binær dokumentation. Den samlede kombinerede meddelelse gives.

**7-Zip:** bevar LGPL/BSD/unRAR meddelelser og giv adgang til den nøjagtige umodificerede kilde. Kildearkivet er linket ovenfor sammen med hele LGPL. unRAR-begrænsningen gælder for den relevante dekompressionskode; dette er ikke en generel MIT-afhængighed. Se forfatterens [distribution ofte stillede spørgsmål](https://www.7-zip.org/faq.html).

**Inno Setup:** bevar påkrævet motorophavsret/websidemeddelelser og marker kildeændringer, hvor det er relevant. Den umodificerede motors kreditter forbliver hos installatører. Tilpassede kataloger bevarer originale kildemeddelelser; navne er indekseret her.

**NVIDIA-materiale:** MIT-licensen til Streamline-integrationsheadere dækker ikke alle SDK-filer. Dens meddelelse adskiller eksplicit Nsight Perf SDK-materiale; at materialet ikke anvendes i dette produktionsmål. NGX-headerne er under NVIDIA's proprietære RTX SDK-vilkår. Deres fulde tekst er blevet tilføjet, med en [original-byte kopi](../../../NVMFG-Unlock40/LICENSES/NVIDIA-RTX-SDK.original.txt). Afsnit 4(d)'s begrænsning vedrørende tekniske begrænsninger forbliver uløst til brug for NVMFG. Der udledes ingen bekræftende tilladelse fra en anden mods eksistens.

**Eksterne ukendte/proprietære komponenter:** RTSS, NVCleanstall, NVIDIA drivere, modeller og keylase patchdata er ikke bundtet i de forberedte hub-aktiver. Links identificerer deres faktiske ejere. En brugerudløst download genlicenserer ikke en komponent.

Værktøjerne bruger Windows-leverede API'er og skrifttyper. Ingen Windows SDK/compiler/font-fil er kopieret til dette Git-lager. Byggeværktøjer og private tests er uden for distribution. Kørselsinterne komponentmeddelelser forbliver i den komplette Microsoft-meddelelsesfil i stedet for at blive gentildelt til udgiveren.

<a id="publisher-contributions"></a>
## Forlags bidrag

禅堂 Zendo (RevoluSound Team) bevarer det originale applikationsarbejde, tilpasninger og dokumentation beskrevet i [herkomstvejledning](docs/provenance.md). [NVPI](NVIDIA-Profile-Inspector/README.md), [NVDF](NVDriverForge/README.md), [NVMFG](NVMFG-Unlock40/README.md) og [RP](NVRasterPulse/README.md) skelner hver især nedarvet arbejde fra ændringer.

Uafhængige projekter; ingen tilknytning til, sponsorering af eller officiel godkendelse fra NVIDIA Corporation eller de anførte upstream-forfattere er underforstået.
