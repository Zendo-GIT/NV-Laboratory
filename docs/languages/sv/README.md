<!-- nv-language-navigation:start -->
🌐 [English](../../../README.md) | [Français](../../../README.fr.md) · [NV Laboratory](README.md)

<details>
<summary>🌐 Language · 34</summary>

[العربية](../ar/README.md) · [বাংলা](../bn/README.md) · [简体中文](../zh/README.md) · [Čeština](../cs/README.md) · [Dansk](../da/README.md) · [Nederlands](../nl/README.md) · [English](../../../README.md) · [Filipino](../fil/README.md) · [Suomi](../fi/README.md) · [Français](../../../README.fr.md) · [Deutsch](../de/README.md) · [Ελληνικά](../el/README.md) · [हिन्दी](../hi/README.md) · [Magyar](../hu/README.md) · [Bahasa Indonesia](../id/README.md) · [Italiano](../it/README.md) · [日本語](../ja/README.md) · [한국어](../ko/README.md) · [मराठी](../mr/README.md) · [فارسی](../fa/README.md) · [Polski](../pl/README.md) · [Português](../pt/README.md) · [ਪੰਜਾਬੀ](../pa/README.md) · [Română](../ro/README.md) · [Русский](../ru/README.md) · [Español](../es/README.md) · [Kiswahili](../sw/README.md) · **Svenska** · [தமிழ்](../ta/README.md) · [ไทย](../th/README.md) · [Türkçe](../tr/README.md) · [Українська](../uk/README.md) · [اردو](../ur/README.md) · [Tiếng Việt](../vi/README.md)

[Translation policy](../README.md)

</details>
<!-- nv-language-navigation:end -->

<!-- nv-translation-notice:start -->
> Maskinassisterad översättning från engelska. Tekniska namn, kommandon, URL:er och ursprungliga lagtexter bevaras. Recension av modersmål är välkommen; konsultera den engelska referensen om formuleringen är otydlig.
<!-- nv-translation-notice:end -->

<a id="nv-laboratory"></a>
# NV Laboratory

**NV Tools av 禅堂 Zendo (RevoluSound Team).** Fyra oberoende Windows-verktyg för NVIDIA-drivrutinsprofiler, drivrutinsinstallation, experimentella ramgränser för Multi Frame Generation och RTSS.

[Skaffa verktygen](docs/downloads.md) · [Installation](docs/installation.md) · [Kompatibilitet och hjälp](docs/support.md) · [Krediter och licenser](THIRD_PARTY_NOTICES.md)

> **NVRasterPulse kräver RTSS.** Installera [RivaTuner Statistics Server från Guru3D](https://www.guru3d.com/download/rtss-rivatuner-statistics-server-download/) först. RTSS måste köras för att dess FPS-gränser ska fungera. Den laddas ner separat.

<a id="projects"></a>
## Projekt

| Projekt | Syfte | Version | Dokumentation | Ladda ner |
| --- | --- | --- | --- | --- |
| **NVIDIA Profile Inspector – NV Tools Fork** | NVIDIA drivrutinsprofilredigerare med tillagd display, färg, HDR och ICC/WCS kontroller. Tidigare NVPI Custom. | 3.0.2.3 | [Guide](NVIDIA-Profile-Inspector/README.md) | [Paket](docs/downloads.md#nvidia-profile-inspector) |
| **NVDriverForge** | Förbered och installera en original NVIDIA-drivrutin med guidade val, säkerhetskopior och återställning. | 0.1.4 | [Guide](NVDriverForge/README.md) | [Paket](docs/downloads.md#nvdriverforge) |
| **NVMFG Unlock40** | Experimentell RTX 40 MFG, beständigt spelbibliotek, diagnostik och Streamline SDK underhåll. | 0.2.3 | [Guide](NVMFG-Unlock40/README.md) | [Paket & status](docs/downloads.md#nvmfg-unlock40) |
| **NVRasterPulse** | Hantera RTSS FPS-gränser per program: diagnostik, förslag, paus, ångra och profildelning. | 0.2 | [Guide](NVRasterPulse/README.md) | [Paket](docs/downloads.md#nvrasterpulse) |

**Nedladdningar:** [nedladdningssida](docs/downloads.md) listar varje versions status, filer och SHA-256-värden. Experimentella funktioner och kompatibilitetsgränser beskrivs i projektguiderna.

<a id="start-here"></a>
## Börja här

1. Välj ett verktyg ovan. Var och en arbetar självständigt; att installera hela sviten är onödigt.
2. Läs dess krav och välj **Setup** för en installerad app eller **portabel** för en separat mapp.
3. När dess release publiceras, ladda ner den namngivna applikationstillgången, läs de medföljande meddelandena och jämför dess SHA-256.
4. Behåll säkerhetskopior innan du ändrar en drivrutin, skärminställning, NVIDIA-profil eller spelets körtid.

Dokumentation finns tillgänglig på samma 34 språk som NV-applikationerna genom väljaren överst i varje guide. GitHub väljer inte automatiskt ett README efter webbläsarspråk. Dokumentationsspråket och applikationens egna språkinställning är separata.

<a id="provenance-and-ownership"></a>
## Härkomst och ägande

Detta nav distribuerar dokumentation och kompilerade applikationer. Applikationens källkod underhålls privat. Uppströmsprojekt behåller sina författarskap och licenser; privat källdistribution ersätter inte dessa termer.

- Profile Inspector fork behåller Orbmu2k:s MIT-licens och identifieras uttryckligen som en fork.
- NVDriverForge har sina egna binära distributionsvillkor och inkluderar separat licensierade runtime/verktygskomponenter.
- NVMFG Unlock40 är en oberoende utvecklad applikation. RTX40MFG-Unlock konsulterades för jämförelse och förfining; delade inbyggda komponenter behåller sina MIT-krediter. Villkoren för MinHook och NVIDIA SDK förblir separata.
- NVRasterPulse behåller den medföljande MIT-licensen och krediterar det Profile Inspector-härledda användargränssnittet. RTSS är ett obligatoriskt externt program.

Se [komplett komponenttabell](THIRD_PARTY_NOTICES.md), [fil härkomst och ändringar](docs/provenance.md) och [licensens omfattning](../../../LICENSE).

<a id="other-projects--revolusound-team"></a>
## Andra projekt – RevoluSound Team

Dessa är separata audiomodprojekt, länkade här för att hjälpa dig att upptäcka lagets arbete.

| Spel | Projekt | Om |
| --- | --- | --- |
| Forza Horizon 6 | [Forza Horizon 6 Revolusound Team Pack](https://www.nexusmods.com/forzahorizon6/mods/56) | Ljudförändringar i fordonet omfattar motorer, avgaser, insug och turboeffekter. |
| Forza Horizon 5 | [Forza Horizon 5 Revolusound Team Pack 1.4.4 FINAL](https://www.nexusmods.com/forzahorizon5/mods/86) | Teamets senare FH5 fordonsljudpaket. |
| Forza Horizon 5 | [Forza Horizon 5.5 Zendo Revolusound Pack](https://www.nexusmods.com/forzahorizon5/mods/20) | Tidigare FH5-paket; dess Nexus-sida leder besökare till det senare teampaketet ovan. |

Titlar följer de länkade Nexus Mods-sidorna. Deras nedladdningar, krav, krediter och behörigheter finns kvar på Nexus Mods.

<a id="help-and-participation"></a>
## Hjälp och delaktighet

[Rapportera ett fel eller föreslå en funktion](https://github.com/Zendo-GIT/NV-Laboratory/issues) · [Bidrar](CONTRIBUTING.md) · [Säkerhetsrapporter](SECURITY.md) · [Ändringslogg](CHANGELOG.md)

För ett säkerhetsproblem, läs SECURITY.md innan du publicerar loggar eller tekniska detaljer. Privat rapportering måste aktiveras av underhållaren efter publicering av arkivet.

> **Oberoende samhällsprojekt.** NV Laboratory, NV Tools och dessa verktyg är inte anslutna till, sponsrade av eller officiellt godkända av NVIDIA Corporation. NVIDIA, GeForce, RTX, DLSS och andra produktnamn är varumärken som tillhör sina respektive ägare. Namn beskriver kompatibilitet och härkomst, inte officiell rekommendation.
