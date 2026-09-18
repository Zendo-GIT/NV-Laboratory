<!-- nv-language-navigation:start -->
🌐 [English](../../../support.md) | [Français](../../../support.fr.md) · [NV Laboratory](../README.md)

<details>
<summary>🌐 Language · 34</summary>

[العربية](../../ar/docs/support.md) · [বাংলা](../../bn/docs/support.md) · [简体中文](../../zh/docs/support.md) · [Čeština](../../cs/docs/support.md) · [Dansk](../../da/docs/support.md) · [Nederlands](../../nl/docs/support.md) · [English](../../../support.md) · [Filipino](../../fil/docs/support.md) · [Suomi](../../fi/docs/support.md) · [Français](../../../support.fr.md) · [Deutsch](../../de/docs/support.md) · [Ελληνικά](../../el/docs/support.md) · [हिन्दी](../../hi/docs/support.md) · [Magyar](../../hu/docs/support.md) · [Bahasa Indonesia](../../id/docs/support.md) · [Italiano](../../it/docs/support.md) · [日本語](../../ja/docs/support.md) · [한국어](../../ko/docs/support.md) · [मराठी](../../mr/docs/support.md) · [فارسی](../../fa/docs/support.md) · [Polski](../../pl/docs/support.md) · [Português](../../pt/docs/support.md) · [ਪੰਜਾਬੀ](../../pa/docs/support.md) · [Română](../../ro/docs/support.md) · [Русский](../../ru/docs/support.md) · [Español](../../es/docs/support.md) · [Kiswahili](../../sw/docs/support.md) · **Svenska** · [தமிழ்](../../ta/docs/support.md) · [ไทย](../../th/docs/support.md) · [Türkçe](../../tr/docs/support.md) · [Українська](../../uk/docs/support.md) · [اردو](../../ur/docs/support.md) · [Tiếng Việt](../../vi/docs/support.md)

[Translation policy](../../README.md)

</details>
<!-- nv-language-navigation:end -->

<!-- nv-translation-notice:start -->
> Maskinassisterad översättning från engelska. Tekniska namn, kommandon, URL:er och ursprungliga lagtexter bevaras. Recension av modersmål är välkommen; konsultera den engelska referensen om formuleringen är otydlig.
<!-- nv-translation-notice:end -->

<a id="compatibility-and-troubleshooting"></a>
# Kompatibilitet och felsökning

Dessa är de förberedda kandidaterna, inte en certifieringsmatris för alla kombinationer av Windows, GPU, förare och spel.

| Verktyg | Windows / körtid | Hårdvara/externt beroende | Verksamhet som kräver vård |
| --- | --- | --- | --- |
| NVPI fork 3.0.2.3 | Windows 10/11 x64, .NET Framework 4.8 | Kompatibel NVIDIA drivrutin/skärm | Profil skriver och visar förhandsvisningar |
| NVDriverForge 0.1.4 | Windows 10 byggd 19041+ / 11 x64; .NET/WPF ingår | Kompatibelt NVIDIA drivrutinspaket | Förhöjd installation, avancerade inställningar, tillval NVENC |
| NVMFG Unlock40 0.2.3 | Windows 10/11 x64; .NET/WPF ingår, Framework 4.8 hjälpare | RTX 40, kvalificerat DLSS FG-spel och fäst leverantör | Native in-game patchning, global profiljournal, SDK speluppdateringar |
| NVRasterPulse 0.2 | Windows 10/11 x64, .NET Framework 4.8 | RTSS installerat; springer efter kepsar | RTSS per körbara profiländringar |

Inget ARM64-paket är förberett. Display/API-tillgänglighet och gamla Windows-versioner kan begränsa enskilda funktioner. Ingen universell minimiversion av NVIDIA eller RTSS har uppfunnits. Den exakta NVMFG-leverantörens hash finns i [härkomst](provenance.md).

<a id="before-reporting-a-bug"></a>
## Innan du rapporterar ett fel

Identifiera den exakta körbara filen/versionen du öppnade. En tidigare installerad kopia är inte nödvändigtvis versionen av en nyladdad ZIP. Registrera reproduktionsstegen, förväntat resultat och faktiskt resultat. För renderings-/begränsningsproblem, inkludera spelversion, skärmuppdatering, FG/V-Sync/VRR-tillstånd och alla andra begränsare eller överlägg.

Använd [buggform](https://github.com/Zendo-GIT/NV-Laboratory/issues/new?template=bug-report.yml). Bifoga aldrig en hel privat utvecklingsmapp, drivrutinsarkiv, modell, spel-DLL, registerdump eller ogranskad loggsamling.

| Problem | Första kontrollerna |
| --- | --- |
| Fel programversion | Bekräfta EXE-identitet och släpp hash; stäng den äldre kopian innan den byts ut. |
| Körtid/startfel | Installera nödvändig Framework 4.8 eller behåll alla medföljande bärbara undermappar. |
| UAC avbruten | Försök endast den avsedda åtgärden igen; installationen lyckades inte avbrytas. |
| Hash-/signaturfel matchar | Sluta använda den kandidaten och skaffa de förväntade officiella byten. |
| NVPI färg/läge avvisades | Gå tillbaka och använd en kombination som stöds av den faktiska displayen/drivrutinen. |
| NVDF säkerhetskopiering eller återställningsfel | Bevara skyddat jobb och RECOVERY.txt; radera inte journalen eller tvinga fram motstridiga skrivningar. |
| NVMFG väntande inställningar | Lös återställning med stängda spel, bevara ändringar från andra verktyg. |
| RP lock har ingen effekt | Kör RTSS, identifiera det riktiga spelets EXE, inspektera krokens status och konkurrerande gränser. |
| RP lock kvarstår efter borttagning | Inspektera RTSS Global; borttagningsändringar endast lokal limiter åsidosätter. |

NVDriverForge erbjuder en förhandsgranskbar lokal JSON-rapport; NVMFG erbjuder en diagnostik i About. Föredra dessa filtrerade rapporter framför ett komplett loggarkiv och inspektera dem innan de delar. En återställningsblockering som rapporterats på NVMFG 0.1.1 har fortfarande ingen fastställd orsak; bevara dess journal och registrera eventuella tillgängliga felkoder. NVRasterPulse 0.2 erbjuder konfigurationsdiagnostik i sin åtgärdsmeny, utan att mäta FPS.

<a id="logs-and-privacy"></a>
## Loggar och integritet

| Verktyg | Lokal data att granska, inte ladda upp i grossistledet |
| --- | --- |
| NVDF | `%LOCALAPPDATA%\NVDriverForge`; skyddade jobb `%PROGRAMDATA%\NVDriverForge\Jobs` |
| NVMFG | `%LOCALAPPDATA%\RtxMfg`; säkerhetskopior `%LOCALAPPDATA%\NvidiaStreamlineMaintenance\Backups`; `Sessions` bredvid EXE |
| RP | `%LOCALAPPDATA%\NVRasterPulse`; `Backups\RTSS` under den |
| NVPI | Din valda export och det visade felet; ingen uppfunnen universell loggbana |

Ta bort kontonamn, hemkataloger, sökvägar till spelbibliotek, enhetsidentifierare, tokens och orelaterade fönster från texten/bilderna du delar. Förvara originalen privat för återställning. Offentliga frågor är synliga för alla.

För en sårbarhet, farligt privilegierat beteende eller oavsiktlig destruktiv operation, följ [SECURITY.md](../SECURITY.md) istället för att publicera information offentligt.

<a id="what-has-been-verified"></a>
## Vad har verifierats

För navförberedelse kördes statiska nyttolast/ZIP/hash/metadataskanningar och dokumentationskontroller. Existerande privata applikationsbygg-/enhets-/UI-tester är historiska, daterade bevis. Ingen drivrutinsinstallation, visningsändring, live RTSS-drift eller spelbenchmark utfördes som en del av denna förberedelse.

"Upptäckt", "skriven", "omladdad", "kapacitet tillgänglig" och "mätt i spelet" är olika resultat. Rapportera vilken du observerade.
