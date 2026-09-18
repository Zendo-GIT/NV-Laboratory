<!-- nv-language-navigation:start -->
🌐 [English](../../../support.md) | [Français](../../../support.fr.md) · [NV Laboratory](../README.md)

<details>
<summary>🌐 Language · 34</summary>

[العربية](../../ar/docs/support.md) · [বাংলা](../../bn/docs/support.md) · [简体中文](../../zh/docs/support.md) · [Čeština](../../cs/docs/support.md) · [Dansk](../../da/docs/support.md) · **Nederlands** · [English](../../../support.md) · [Filipino](../../fil/docs/support.md) · [Suomi](../../fi/docs/support.md) · [Français](../../../support.fr.md) · [Deutsch](../../de/docs/support.md) · [Ελληνικά](../../el/docs/support.md) · [हिन्दी](../../hi/docs/support.md) · [Magyar](../../hu/docs/support.md) · [Bahasa Indonesia](../../id/docs/support.md) · [Italiano](../../it/docs/support.md) · [日本語](../../ja/docs/support.md) · [한국어](../../ko/docs/support.md) · [मराठी](../../mr/docs/support.md) · [فارسی](../../fa/docs/support.md) · [Polski](../../pl/docs/support.md) · [Português](../../pt/docs/support.md) · [ਪੰਜਾਬੀ](../../pa/docs/support.md) · [Română](../../ro/docs/support.md) · [Русский](../../ru/docs/support.md) · [Español](../../es/docs/support.md) · [Kiswahili](../../sw/docs/support.md) · [Svenska](../../sv/docs/support.md) · [தமிழ்](../../ta/docs/support.md) · [ไทย](../../th/docs/support.md) · [Türkçe](../../tr/docs/support.md) · [Українська](../../uk/docs/support.md) · [اردو](../../ur/docs/support.md) · [Tiếng Việt](../../vi/docs/support.md)

[Translation policy](../../README.md)

</details>
<!-- nv-language-navigation:end -->

<!-- nv-translation-notice:start -->
> Machineondersteunde vertaling uit het Engels. Technische namen, commando's, URL's en originele juridische teksten blijven behouden. Recensie door native speakers is welkom; raadpleeg de Engelse referentie als de formulering onduidelijk is.
<!-- nv-translation-notice:end -->

<a id="compatibility-and-troubleshooting"></a>
# Compatibiliteit en probleemoplossing

Dit zijn de voorbereide kandidaten, geen certificeringsmatrix voor alle Windows-, GPU-, coureur- en spelcombinaties.

| Gereedschap | Windows / runtime | Hardware / externe afhankelijkheid | Operaties die zorg nodig hebben |
| --- | --- | --- | --- |
| NVPI fork 3.0.2.3 | Windows 10/11 x64, .NET Framework 4.8 | Compatibel NVIDIA-stuurprogramma/display | Profiel schrijft en geeft voorbeelden weer |
| NVDriverForge 0.1.4 | Windows 10 gebouwd 19041+ / 11 x64; .NET/WPF inbegrepen | Compatibel NVIDIA driverpakket | Verhoogde installatie, geavanceerde instellingen, optionele NVENC |
| NVMFG Unlock40 0.2.3 | Windows 10/11x64; .NET/WPF inbegrepen, Framework 4.8-helpers | RTX 40, in aanmerking komende DLSS FG-game en vastgezette provider | Native in-game patching, wereldwijd profiellogboek, SDK-game-updates |
| NVRasterPulse 0.2 | Windows 10/11 x64, .NET Framework 4.8 | RTSS geïnstalleerd; rennen voor petten | RTSS per uitvoerbare profielwijzigingen |

Er is geen ARM64-pakket voorbereid. Beschikbaarheid van display/API en oude Windows-versies kunnen individuele functies beperken. Er is geen universele minimumversie van NVIDIA of RTSS uitgevonden. De exacte hash van de NVMFG-provider bevindt zich in [herkomst](provenance.md).

<a id="before-reporting-a-bug"></a>
## Voordat u een bug rapporteert

Identificeer het exacte uitvoerbare bestand/de exacte versie die u hebt geopend. Een eerder geïnstalleerd exemplaar is niet noodzakelijkerwijs de versie van een nieuw gedownloade ZIP. Leg de reproductiestappen, het verwachte resultaat en het daadwerkelijke resultaat vast. Voor weergave-/beperkingsproblemen vermeldt u de gameversie, het vernieuwen van het scherm, de FG/V-Sync/VRR-status en eventuele andere limiters of overlays.

Gebruik de [bug-formulier](https://github.com/Zendo-GIT/NV-Laboratory/issues/new?template=bug-report.yml). Voeg nooit een volledige privé-ontwikkelingsmap, driverarchief, model, game-DLL, registerdump of niet-beoordeelde logverzameling toe.

| Probleem | Eerste controles |
| --- | --- |
| Verkeerde applicatieversie | Bevestig de EXE-identiteit en geef de hash vrij; sluit het oudere exemplaar voordat u het vervangt. |
| Runtime-/opstartfout | Installeer het vereiste Framework 4.8 of bewaar alle meegeleverde draagbare submappen. |
| UAC geannuleerd | Probeer alleen de beoogde handeling opnieuw; annulering is geen succesvolle installatie. |
| Hash/handtekening komt niet overeen | Stop met het gebruik van die kandidaat en verkrijg de verwachte officiële bytes. |
| NVPI kleur/modus afgewezen | Keer terug en gebruik een combinatie die wordt ondersteund door het daadwerkelijke beeldscherm/stuurprogramma. |
| NVDF back-up- of herstelfout | Behoud beschermde taak en RECOVERY.txt; Wis het journaal niet en forceer geen conflicterende schrijfbewerkingen. |
| NVMFG-instellingen in behandeling | Los het herstel op terwijl games gesloten zijn, waarbij de wijzigingen van andere tools behouden blijven. |
| RP-dop heeft geen effect | Voer RTSS uit, identificeer de echte game-EXE, inspecteer de hook-status en concurrerende limieten. |
| RP-dop blijft zitten na verwijdering | Inspecteer RTSS Wereldwijd; Door het verwijderen worden alleen lokale limiteroverschrijvingen gewijzigd. |

NVDriverForge biedt een voorbeeld van een lokaal JSON-rapport; NVMFG biedt een diagnose aan in Over. Geef de voorkeur aan deze gefilterde rapporten boven een compleet logarchief en bekijk ze voordat u ze deelt. Een herstelblokkering gerapporteerd op NVMFG 0.1.1 heeft nog steeds geen vastgestelde oorzaak; het dagboek bijhoudt en eventuele beschikbare foutcodes registreert. NVRasterPulse 0.2 biedt configuratiediagnostiek in het actiemenu, zonder FPS te meten.

<a id="logs-and-privacy"></a>
## Logboeken en privacy

| Gereedschap | Lokale gegevens om te beoordelen, niet om groothandel te uploaden |
| --- | --- |
| NVDF | `%LOCALAPPDATA%\NVDriverForge`; beschermde banen `%PROGRAMDATA%\NVDriverForge\Jobs` |
| NVMFG | `%LOCALAPPDATA%\RtxMfg`; back-ups `%LOCALAPPDATA%\NvidiaStreamlineMaintenance\Backups`; `Sessions` naast de EXE |
| RP | `%LOCALAPPDATA%\NVRasterPulse`; `Backups\RTSS` eronder |
| NVPI | Uw gekozen exports en de weergegeven fout; geen uitgevonden universeel logpad |

Verwijder accountnamen, thuismappen, gamebibliotheekpaden, apparaat-ID's, tokens en niet-gerelateerde vensters uit de tekst/afbeeldingen die u deelt. Bewaar de originelen privé voor herstel. Publieke kwesties zijn voor iedereen zichtbaar.

Voor een kwetsbaarheid, gevaarlijk geprivilegieerd gedrag of onbedoelde destructieve bewerking volgt u [SECURITY.md](../SECURITY.md) in plaats van details openbaar te plaatsen.

<a id="what-has-been-verified"></a>
## Wat is geverifieerd

Ter voorbereiding van de hub werden statische payload/ZIP/hash/metadata-scans en documentatiecontroles uitgevoerd. Bestaande privéapplicatie-build/unit/UI-tests zijn historisch, gedateerd bewijsmateriaal. Als onderdeel van deze voorbereiding zijn er geen stuurprogramma-installatie, weergavewijziging, live RTSS-bewerking of gamebenchmark uitgevoerd.

“Gedetecteerd”, “geschreven”, “herladen”, “beschikbare capaciteit” en “gemeten in het spel” zijn verschillende resultaten. Vermeld welke je hebt waargenomen.
