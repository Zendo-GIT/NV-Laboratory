<!-- nv-language-navigation:start -->
🌐 [English](../../../development.md) | [Français](../../../development.fr.md) · [NV Laboratory](../README.md)

<details>
<summary>🌐 Language · 34</summary>

[العربية](../../ar/docs/development.md) · [বাংলা](../../bn/docs/development.md) · [简体中文](../../zh/docs/development.md) · [Čeština](../../cs/docs/development.md) · [Dansk](../../da/docs/development.md) · [Nederlands](../../nl/docs/development.md) · [English](../../../development.md) · [Filipino](../../fil/docs/development.md) · [Suomi](../../fi/docs/development.md) · [Français](../../../development.fr.md) · [Deutsch](../../de/docs/development.md) · [Ελληνικά](../../el/docs/development.md) · [हिन्दी](../../hi/docs/development.md) · [Magyar](../../hu/docs/development.md) · [Bahasa Indonesia](../../id/docs/development.md) · [Italiano](../../it/docs/development.md) · [日本語](../../ja/docs/development.md) · [한국어](../../ko/docs/development.md) · [मराठी](../../mr/docs/development.md) · [فارسی](../../fa/docs/development.md) · [Polski](../../pl/docs/development.md) · [Português](../../pt/docs/development.md) · [ਪੰਜਾਬੀ](../../pa/docs/development.md) · [Română](../../ro/docs/development.md) · [Русский](../../ru/docs/development.md) · [Español](../../es/docs/development.md) · [Kiswahili](../../sw/docs/development.md) · **Svenska** · [தமிழ்](../../ta/docs/development.md) · [ไทย](../../th/docs/development.md) · [Türkçe](../../tr/docs/development.md) · [Українська](../../uk/docs/development.md) · [اردو](../../ur/docs/development.md) · [Tiếng Việt](../../vi/docs/development.md)

[Translation policy](../../README.md)

</details>
<!-- nv-language-navigation:end -->

<!-- nv-translation-notice:start -->
> Maskinassisterad översättning från engelska. Tekniska namn, kommandon, URL:er och ursprungliga lagtexter bevaras. Recension av modersmål är välkommen; konsultera den engelska referensen om formuleringen är otydlig.
<!-- nv-translation-notice:end -->

<a id="repository-architecture-and-maintenance"></a>
# Förvarsarkitektur och underhåll

NV Laboratory är ett offentligt **nav för dokumentation och binär distribution**. Den innehåller ingen applikationskälla. De fyra projekten behåller separata byggträd, versioner, identiteter och releasetillgångar. Deras privata utvecklingshistorik importeras inte till detta Git-förråd.

<a id="layout"></a>
## Layout

| Plats | Syfte |
| --- | --- |
| README.md / README.fr.md | Engelska/franska ingångar |
| Fyra projektmappar | Kompletta guider och tillämpliga originalmeddelanden |
| docs | Nedladdningar, kompatibilitet, härkomst, utveckling och utgivningsförfarande |
| docs/releases.json | Reviderad kandidat/release metadata, storlekar och hash |
| handlingar/härkomst | Fil/hash jämförelser; ingen applikationskod |
| licenser | Delade fullständiga texter från tredje part och översättarkrediter för installatörer |
| tillgångar | Befintliga granskade UI-förhandsvisningar och deras ursprung |
| .github | Utfärda formulär och validering av skrivskyddad dokumentation |
| verktyg/validate_repository.py | Standard-bibliotekets publikationsgräns och länkkontroller |

Engelska förblir standard GitHub README. Befintliga angränsande `.fr.md`-länkar förblir giltiga. Ytterligare översättningar speglar dokumentationen under `docs/languages/<code>`; språkväljaren håller samma sida när du byter språk. Katalogen `docs/languages/catalog.json` registrerar alla 34 språk och källfingeravtryck. GitHub väljer inte automatiskt ett README efter webbläsarspråk. Se [språkindex och översättningspolicy](../../README.md).

<a id="application-technologies"></a>
## Applikationstekniker

| Program | Privat teknik | Distribution |
| --- | --- | --- |
| NVPI fork | C#, WPF, .NET Framework 4.8, NVAPI/Windows interop | Komplett bärbar mapp och separat Inno Setup |
| NVDriverForge | C#, WPF, .NET 8; inbyggd C++ bootstrap; 7-Zip process | Fristående bärbar EXE och Setup |
| NVMFG Unlock40 | C#/WPF .NET 8, Framework 4.8-hjälpare, C++20/MASM/MinHook-motor | Bärbart träd och installation |
| NVRasterPulse | C#/WPF Framework 4.8; RTSS profil/reload integration; infödd bootstrap | Bärbart träd och installation |

Den här offentliga kassan kan inte bygga om applikationerna. Automatiska "Source code"-arkiv är hub-ögonblicksbilder. Uppströms källlänkar representerar inte den exakta privata modifierade källan. Den offentliga CI validerar endast detta arkiv.

<a id="local-checks"></a>
## Lokala kontroller

Från förvarsroten:

```text
python tools/validate_repository.py
```

Python 3.10 eller nyare är tillräckligt. Kontrollen läser filer, lokala Markdown-länkar, obligatoriska meddelanden/RTSS-länkar, release-metadata och publiceringsgränser. Den kör inte programvaran, installerar inte beroenden eller kontaktar ett nätverk.

GitHub-arbetsflödet kör samma kontroll med skrivskyddad innehållsbehörighet vid push, pull-begäran eller manuell sändning. Checkout är fäst vid en granskad commit och kvarstår inte autentiseringsuppgifter. Inget release- eller distributionsjobb är konfigurerat.

<a id="maintain-the-boundary"></a>
## Behåll gränsen

Uppdatera den engelska referensen, franska guider och berörda översättningar tillsammans. Håll innehållsliga ändringar åtskilda från jämförelser med endast formatering. Spela in faktiska kandidathaschar, uppströms commit-referenser och licenser; sluta aldrig en licens från ett projekts popularitet.

Använd nya versioner av releasetillgångar och granska ändrade binärfiler, arkiv och inbäddade meddelanden på nytt. Bevara privata säkerhetskopior utanför det här arkivet. Använd inte ett offentligt arbetsflöde för att importera privat programkälla eller lokala byggmappar.

Tester som är lämpliga för en funktionell applikationsändring körs i det privata projektet. Kör inte drivrutinsinstallationsprogram igen och skriv inte riktiga profiler för en dokumentationsuppdatering. [Manuell frigöringsprocedur](releasing.md).
