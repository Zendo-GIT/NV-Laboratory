<!-- nv-language-navigation:start -->
🌐 [English](../../../THIRD_PARTY_NOTICES.md) | [Français](../fr/THIRD_PARTY_NOTICES.md) · [NV Laboratory](README.md)

<details>
<summary>🌐 Language · 34</summary>

[العربية](../ar/THIRD_PARTY_NOTICES.md) · [বাংলা](../bn/THIRD_PARTY_NOTICES.md) · [简体中文](../zh/THIRD_PARTY_NOTICES.md) · [Čeština](../cs/THIRD_PARTY_NOTICES.md) · [Dansk](../da/THIRD_PARTY_NOTICES.md) · [Nederlands](../nl/THIRD_PARTY_NOTICES.md) · [English](../../../THIRD_PARTY_NOTICES.md) · [Filipino](../fil/THIRD_PARTY_NOTICES.md) · [Suomi](../fi/THIRD_PARTY_NOTICES.md) · [Français](../fr/THIRD_PARTY_NOTICES.md) · [Deutsch](../de/THIRD_PARTY_NOTICES.md) · [Ελληνικά](../el/THIRD_PARTY_NOTICES.md) · [हिन्दी](../hi/THIRD_PARTY_NOTICES.md) · [Magyar](../hu/THIRD_PARTY_NOTICES.md) · [Bahasa Indonesia](../id/THIRD_PARTY_NOTICES.md) · [Italiano](../it/THIRD_PARTY_NOTICES.md) · [日本語](../ja/THIRD_PARTY_NOTICES.md) · [한국어](../ko/THIRD_PARTY_NOTICES.md) · [मराठी](../mr/THIRD_PARTY_NOTICES.md) · [فارسی](../fa/THIRD_PARTY_NOTICES.md) · [Polski](../pl/THIRD_PARTY_NOTICES.md) · [Português](../pt/THIRD_PARTY_NOTICES.md) · [ਪੰਜਾਬੀ](../pa/THIRD_PARTY_NOTICES.md) · [Română](../ro/THIRD_PARTY_NOTICES.md) · [Русский](../ru/THIRD_PARTY_NOTICES.md) · [Español](../es/THIRD_PARTY_NOTICES.md) · [Kiswahili](../sw/THIRD_PARTY_NOTICES.md) · **Svenska** · [தமிழ்](../ta/THIRD_PARTY_NOTICES.md) · [ไทย](../th/THIRD_PARTY_NOTICES.md) · [Türkçe](../tr/THIRD_PARTY_NOTICES.md) · [Українська](../uk/THIRD_PARTY_NOTICES.md) · [اردو](../ur/THIRD_PARTY_NOTICES.md) · [Tiếng Việt](../vi/THIRD_PARTY_NOTICES.md)

[Translation policy](../README.md)

</details>
<!-- nv-language-navigation:end -->

<!-- nv-translation-notice:start -->
> Maskinassisterad översättning från engelska. Tekniska namn, kommandon, URL:er och ursprungliga lagtexter bevaras. Recension av modersmål är välkommen; konsultera den engelska referensen om formuleringen är otydlig.
<!-- nv-translation-notice:end -->

<a id="third-party-notices-and-credits"></a>
# Meddelanden och krediter från tredje part

Inledande revision: 2026-09-09; NVDriverForge 0.1.3 och härkomstuppdatering: 2026-09-10. **En komponents licens täcker den komponenten, inte hela sviten.** Programkällan förblir privat. Upphovsrätts- och tillståndsmeddelanden behålls ordagrant; denna tabell är ett index, inte en ersättning för dem. "Extern" betyder inte fördelad i applikationstillgångarna.

| Komponent / originalprojekt | Författare | Officiell sida, arkiv eller nedladdning | Licens/meddelande | Använd i NV Tools | Ändringar |
| --- | --- | --- | --- | --- | --- |
| NVIDIA Profile Inspector | Orbmu2k; Copyright 2016 | [Förvar](https://github.com/Orbmu2k/nvidiaProfileInspector), [nedladdningar](https://github.com/Orbmu2k/nvidiaProfileInspector/releases) | [MIT](../../../NVIDIA-Profile-Inspector/LICENSE) | Hela NVPI fork; NVDF teman/extended interface referens; NVMFG omslag/stilar; RP UI-resurser | Fork visningstjänster, transaktioner och startprogram; tema/kontrollintegration och omslagsanpassningar |
| RTX40MFG-Unlock | Michael Robles / dashdogy; Copyright 2026 | [Förvar](https://github.com/dashdogy/RTX40MFG-Unlock), [nedladdningar](https://github.com/dashdogy/RTX40MFG-Unlock/releases) | [MIT](../../../NVMFG-Unlock40/LICENSES/RTX40MFG-Unlock-MIT.txt) | Jämförelse/förfiningsreferens och delade/anpassade NVMFG inbyggda komponenter; självständigt utvecklad applikation | Central laddning, NGX/kontrollerkoordination, per-game/V-Sync integration och diagnostik |
| MinHook, fäst 8fda4f5 | Tsuda Kageyu; Copyright 2009–2017 | [Förvar](https://github.com/TsudaKageyu/minhook), [fäst källa](https://github.com/TsudaKageyu/minhook/tree/8fda4f5481fed5797dc2651cd91e238e9b3928c6) | [BSD 2-klausul meddelande](../../../NVMFG-Unlock40/LICENSES/MinHook.txt) | Statiskt kompilerad till NVMFG-motor | Inkluderad delmängd oförändrad bortsett från textformatering mot den ärvda kopian |
| Hacker Disassembler Engine (HDE64) | Vyacheslav Patkov; Copyright 2008–2009 | [MinHook:s källsamling](https://github.com/TsudaKageyu/minhook/tree/8fda4f5481fed5797dc2651cd91e238e9b3928c6/src/hde) | [Fullständiga MinHook/HDE-meddelanden](../../../NVMFG-Unlock40/LICENSES/MinHook.txt) | MinHook avkodare i NVMFG | Inga funktionella förändringar identifierade; HDE32-meddelandet bibehålls även om produktionen använder HDE64 |
| Streamline 2.12 integrationshuvuden | NVIDIA Corporation; Copyright 2023 | [Förvar](https://github.com/NVIDIA-RTX/Streamline), [nedladdningar](https://github.com/NVIDIA-RTX/Streamline/releases) | [MIT för kvalificerade rubriker](../../../NVMFG-Unlock40/LICENSES/Streamline-MIT.txt) | Kompilerar NVMFG Streamline integration | Rubriker ej modifierade; ingen runtime DLL i applikationspaketet |
| NVIDIA NGX / DLSS SDK rubriker | NVIDIA Corporation | [Fäst förråd](https://github.com/NVIDIA/DLSS/tree/a291cc7d2cc642a51566f3dfd5376f635cd1b284), [SDK](https://developer.nvidia.com/rtx/dlss) | [NVIDIA RTX SDK villkor](../../../NVMFG-Unlock40/LICENSES/NVIDIA-RTX-SDK.txt), [rubrikmeddelande](../../../NVMFG-Unlock40/LICENSES/NGX-Header-Notice.txt) | Kompilerar NVMFG NGX integration | Rubriker ej modifierade; ingen NGX-modell/leverantör medföljer; olöst begränsning som beskrivs nedan |
| .NET runtime 8.0.31 (NVDF) / 8.0.30 (NVMFG) | .NET Foundation, Microsoft och bidragsgivare | [Källa](https://github.com/dotnet/runtime), [nedladdningar](https://dotnet.microsoft.com/en-us/download/dotnet/8.0) | [MIT](../../../licenses/third-party/Microsoft-NET-LICENSE.txt) och [fullständiga meddelanden från tredje part](../../../licenses/third-party/Microsoft-NET-THIRD-PARTY-NOTICES.txt) | Fristående NVDF och NVMFG app/agent | Körtid oförändrad |
| WPF / Windows Desktop Runtime 8.0.31 (NVDF) / 8.0.30 (NVMFG) | .NET Foundation, Microsoft och bidragsgivare | [Källa](https://github.com/dotnet/wpf), [nedladdningar](https://dotnet.microsoft.com/en-us/download/dotnet/8.0) | [MIT](../../../licenses/third-party/Microsoft-WPF-LICENSE.txt), körtidsmeddelanden ovan | NVDF och NVMFG användargränssnitt | Ramen oförändrad; applikationens användargränssnitt skapat/anpassat separat |
| .NET Framework 4.8 | Microsoft | [Officiell runtime nedladdning](https://dotnet.microsoft.com/en-us/download/dotnet-framework/net48) | Microsoft plattform/körningsvillkor; yttre | NVPI, RP och NVMFG profilhjälpare | Inga; ingen installationsprogram eller ram-DLL omdistribueras av denna hubb |
| 7-Zip 26.03 x64 | Igor Pavlov; Copyright 1999–2026 | [Webbplats/nedladdningar](https://www.7-zip.org/download.html), [exakt källarkiv](https://github.com/ip7z/7zip/releases/download/26.03/7z2603-src.tar.xz) | [Fullständigt meddelande](../../../licenses/third-party/7-Zip.txt), [LGPL 2.1-or-later](../../../licenses/third-party/LGPL-2.1.txt), BSD delar och unRAR begränsning | NVDF bäddar in omodifierad 7z.exe/7z.dll och kör CLI som en separat process | Inga ändringar |
| Inno Setup 7.1.0 | Jordan Russell, Martijn Laan och bidragsgivare | [Webbplats/nedladdningar](https://jrsoftware.org/isinfo.php), [källa](https://github.com/jrsoftware/issrc) | [Original Inno Setup licens](../../../licenses/third-party/Inno-Setup.txt) | Installationsmotorer och genererade avinstallatörer | Motor/kompilator oförändrad; projektmanus, branding och native focus-hantering anpassas |
| Inno Setup översättningskataloger | Namngivna originalöversättare | [Officiell samling](https://jrsoftware.org/files/istrans/) | Inno/katalogmeddelanden och [fullständiga rubriker](../../../licenses/INSTALLER-TRANSLATORS.md) | Delade 34-språkiga kataloger för alla fyra installatörer, inklusive NVPI setup version 2 | Nycklar, ID, typsnitt, tekniska engelska fallback; projektförfattade förhandsgranskningskataloger där det behövs |
| Microsoft Visual C++ runtime / Windows SDK-stöd | Microsoft | [Visual Studio verktyg](https://visualstudio.microsoft.com/downloads/), [omfördelningsvillkorsindex](https://learn.microsoft.com/en-us/visualstudio/releases/2022/redistribution) | Microsoft verktygskedja/körningsvillkor; inte MIT av denna tabell | Statisk frisättning CRT i inbyggda motor/bootstrap binärer; installerade Windows API:er | Inga ändringar av körtidskällan; ingen kompilator, SDK eller debug runtime distribuerad |
| RivaTuner Statistics Server (RTSS) | Unwinder | [Officiell Guru3D nedladdning](https://www.guru3d.com/download/rtss-rivatuner-statistics-server-download/) | Leverantörsvillkor; ingen omfördelningstillstånd härledd från "gratisprogram" | Erforderlig extern begränsare för RP; installerad UpdateProfiles export | Ingen RTSS-kod/binär modifierad eller buntad; RP skriver valda profilnycklar |
| NVIDIA drivrutin / NVAPI / NVML | NVIDIA Corporation | [Drivrutiner nedladdningar](https://www.nvidia.com/en-us/drivers/), [NVAPI](https://developer.nvidia.com/nvapi), [NVML](https://developer.nvidia.com/management-library-nvml) | NVIDIA-drivrutin/SDK-villkor; yttre | Installerade inbyggda gränssnitt och explicita nedladdningar av originaldrivrutiner | Ingen NVIDIA DLL i navtillgångar; NVDF:s valfria NVENC-operation modifierar användarvalda installerade DLL-filer |
| NVIDIA NGX leverantör/modeller och Streamline körtid | NVIDIA Corporation | [DLSS SDK](https://developer.nvidia.com/rtx/dlss), [Streamline släpps](https://github.com/NVIDIA-RTX/Streamline/releases) | Komponentspecifika NVIDIA-termer, skilda från MIT-rubriker | Externa spel-/drivrutinkomponenter som används av NVMFG; SDK hämtas endast på begäran | NVMFG tillämpar experimentella beteendeförändringar i minnet; SDK spelkopior kan uppdateras med backup |
| keylase/nvidia-patch | keylase och bidragsgivare | [Förvar](https://github.com/keylase/nvidia-patch), [Windows data](https://github.com/keylase/nvidia-patch/tree/master/win) | Omfördelningslicens har inte fastställts av denna revision | Extern valfri NVDF NVENC katalog-/patchdata, hämtad från en fäst commit per val | Ingen uppströmskälla, patcher eller patchdata kopieras till hubben/applikationstillgångarna |
| NVCleanstall | TechPowerUp | [Officiell sida/nedladdning](https://www.techpowerup.com/download/techpowerup-nvcleanstall/) | Proprietär distribution; ingen källa/binär omfördelningsbehörighet antogs | Arbetsflöde och tillvalsinspiration för NVDF | Ingen importerad källa eller binär; inte ett fork eller ett körtidsberoende |

<a id="obligations-and-boundaries"></a>
## Skyldigheter och gränser

**MIT-komponenter:** behåller upphovsrätt, tillståndstext och ansvarsfriskrivning med kopior. Deras licens kräver inte publicering av modifierad källa. Ursprungligt författarskap bevaras även när programkällan underhålls privat.

**MinHook/HDE:** bevara meddelandena, villkoren och friskrivningarna i binär dokumentation. Hela sammanlagda meddelandet tillhandahålls.

**7-Zip:** bevara LGPL/BSD/unRAR-meddelanden och ge tillgång till den exakta omodifierade källan. Källarkivet är länkat ovan, tillsammans med hela LGPL. unRAR-begränsningen gäller den relevanta dekompressionskoden; detta är inte ett generellt MIT-beroende. Se författarens [distribution FAQ](https://www.7-zip.org/faq.html).

**Inno Setup:** bevara obligatorisk upphovsrätt/webbplatsmeddelanden och markera källändringar där så är tillämpligt. Den omodifierade motorns krediter finns kvar hos installatörer. Anpassade kataloger behåller ursprungliga källmeddelanden; namn indexeras här.

**NVIDIA-material:** MIT-licensen för Streamline-integreringshuvuden täcker inte alla SDK-filer. Dess meddelande separerar uttryckligen Nsight Perf SDK-material; att materialet inte används i detta produktionsmål. NGX-huvudena är under NVIDIA:s egenutvecklade RTX SDK-villkor. Deras fullständiga text har lagts till, med en [original-byte kopia](../../../NVMFG-Unlock40/LICENSES/NVIDIA-RTX-SDK.original.txt). Avsnitt 4(d)s begränsning avseende tekniska begränsningar förblir olöst för NVMFG:s användning. Ingen bekräftande tillåtelse härleds från en annan mods existens.

**Externa okända/proprietära komponenter:** RTSS, NVCleanstall, NVIDIA drivrutiner, modeller och keylase patchdata är inte paketerade i de förberedda hubbtillgångarna. Länkar identifierar deras faktiska ägare. En användarutlöst nedladdning återlicensierar inte en komponent.

Verktygen använder API:er och typsnitt som tillhandahålls av Windows. Ingen Windows SDK/kompilator/font-fil kopieras till detta Git-förråd. Byggverktyg och privata tester är utanför distributionen. Körtidsinterna komponentmeddelanden finns kvar i hela Microsoft-meddelandefilen i stället för att omtilldelas till utgivaren.

<a id="publisher-contributions"></a>
## Förlagsbidrag

禅堂 Zendo (RevoluSound Team) behåller det ursprungliga applikationsarbetet, anpassningarna och dokumentationen som beskrivs i [härkomstguide](docs/provenance.md). [NVPI](NVIDIA-Profile-Inspector/README.md), [NVDF](NVDriverForge/README.md), [NVMFG](NVMFG-Unlock40/README.md) och [RP](NVRasterPulse/README.md) skiljer vart och ett ärvt arbete från ändringar.

Oberoende projekt; ingen anknytning till, sponsring av eller officiellt stöd från NVIDIA Corporation eller de listade uppströmsförfattarna antyds.
