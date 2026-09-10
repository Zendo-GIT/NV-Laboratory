<!-- nv-language-navigation:start -->
🌐 [English](../../../../NVMFG-Unlock40/README.md) | [Français](../../../../NVMFG-Unlock40/README.fr.md) · [NV Laboratory](../README.md)

<details>
<summary>🌐 Language · 34</summary>

[العربية](../../ar/NVMFG-Unlock40/README.md) · [বাংলা](../../bn/NVMFG-Unlock40/README.md) · [简体中文](../../zh/NVMFG-Unlock40/README.md) · [Čeština](../../cs/NVMFG-Unlock40/README.md) · [Dansk](../../da/NVMFG-Unlock40/README.md) · **Nederlands** · [English](../../../../NVMFG-Unlock40/README.md) · [Filipino](../../fil/NVMFG-Unlock40/README.md) · [Suomi](../../fi/NVMFG-Unlock40/README.md) · [Français](../../../../NVMFG-Unlock40/README.fr.md) · [Deutsch](../../de/NVMFG-Unlock40/README.md) · [Ελληνικά](../../el/NVMFG-Unlock40/README.md) · [हिन्दी](../../hi/NVMFG-Unlock40/README.md) · [Magyar](../../hu/NVMFG-Unlock40/README.md) · [Bahasa Indonesia](../../id/NVMFG-Unlock40/README.md) · [Italiano](../../it/NVMFG-Unlock40/README.md) · [日本語](../../ja/NVMFG-Unlock40/README.md) · [한국어](../../ko/NVMFG-Unlock40/README.md) · [मराठी](../../mr/NVMFG-Unlock40/README.md) · [فارسی](../../fa/NVMFG-Unlock40/README.md) · [Polski](../../pl/NVMFG-Unlock40/README.md) · [Português](../../pt/NVMFG-Unlock40/README.md) · [ਪੰਜਾਬੀ](../../pa/NVMFG-Unlock40/README.md) · [Română](../../ro/NVMFG-Unlock40/README.md) · [Русский](../../ru/NVMFG-Unlock40/README.md) · [Español](../../es/NVMFG-Unlock40/README.md) · [Kiswahili](../../sw/NVMFG-Unlock40/README.md) · [Svenska](../../sv/NVMFG-Unlock40/README.md) · [தமிழ்](../../ta/NVMFG-Unlock40/README.md) · [ไทย](../../th/NVMFG-Unlock40/README.md) · [Türkçe](../../tr/NVMFG-Unlock40/README.md) · [Українська](../../uk/NVMFG-Unlock40/README.md) · [اردو](../../ur/NVMFG-Unlock40/README.md) · [Tiếng Việt](../../vi/NVMFG-Unlock40/README.md)

[Translation policy](../../README.md)

</details>
<!-- nv-language-navigation:end -->

<!-- nv-translation-notice:start -->
> Machineondersteunde vertaling uit het Engels. Technische namen, commando's, URL's en originele juridische teksten blijven behouden. Recensie door native speakers is welkom; raadpleeg de Engelse referentie als de formulering onduidelijk is.
<!-- nv-translation-notice:end -->

<a id="nvmfg-unlock40"></a>
# NVMFG Unlock40

**Experimentele NVIDIA Multi Frame Generation voor GeForce RTX 40, met een centrale controller en keuzes per game.**

[Download 0.1.1 en status](../docs/downloads.md#nvmfg-unlock40) · [Installatie](#installation) · [Stroomopwaarts](#upstream-and-modifications) · [Licenties](LICENSES/README.md)

<a id="overview-and-purpose"></a>
## Overzicht en doel

NVMFG Unlock40 is een onafhankelijk ontwikkelde applicatie door 禅堂 Zendo (RevoluSound Team). Het combineert een Windows-controller, een native laag, een profielhelper en game/Streamline SDK-beheer. Het richt zich op games die NVIDIA DLSS Frame Generation en compatibele NVIDIA-runtimes al integreren.

[RTX40MFG-Unlock](https://github.com/dashdogy/RTX40MFG-Unlock) werd geraadpleegd om het werk te vergelijken en te verfijnen. De huidige native laag bevat gedeelde en aangepaste componenten, die hieronder afzonderlijk worden vermeld. Deze verwijzing maakt de gehele NVMFG-toepassing niet tot een fork van dat project.

Het is bedoeld om experimenteel MFG-gedrag centraal te coördineren, gamespecifieke keuzes te onthouden en runtime-updates en back-ups zichtbaar te houden. Het voegt DLSS Frame Generation niet toe aan elk spel en converteert geen willekeurige FSR-implementatie.

De voorbereide kandidaat is **0.1.1**, inclusief de visuele correctie uit de SDK-lijst die intern is vastgelegd als UI2. De openbare versie blijft 0.1.1; de exacte hashes onderscheiden deze kandidaat van oudere lokale builds.

<a id="features"></a>
## Kenmerken

- Centrale in-/uitschakelingsbediening en optionele Windows-lade opstarten.
- Selectie per spel tussen Dynamic MFG, de game-instelling en ondersteunde vaste vermenigvuldigers.
- Afzonderlijke onthouden keuzes voor waargenomen V-Sync aan/uit-statussen.
- Dynamic gebruikt de modus van NVIDIA; het wordt opgeschort wanneer V-Sync is uitgeschakeld, met een aparte in-game/vaste keuze.
- Spelmenubegeleiding en aanhoudende uitsluitingen; games zonder DLSS FG behouden de controle.
- Game-ontdekking, selectie van bovenliggende mappen, zoeken, groeperen en verwijderen zonder gamebestanden te verwijderen.
- Streamline SDK downloaden/importeren, geverifieerde lokale cache, expliciete selectie, back-up en herstel per game.
- Native providerverificatie, diagnostiek per sessie, globaal profiellogboek en conflictbewust herstel.
- 34 interfacetalen en vier thema's.

Als je FG in het spel uitschakelt, blijft het uit. Vaste keuzes van 2x tot en met 6x zijn afhankelijk van het spel/menu/looptijd; ze zijn geen belofte dat elke combinatie werkt. De controller observeert V-Sync en stelt V-Sync of VRR niet in voor de gebruiker.

<a id="compatibility"></a>
## Compatibiliteit

| Vereiste | Details |
| --- | --- |
| Systeem | Windows 10/11 x64 |
| GPU | GeForce RTX 40 doel; geen universele GPU-compatibiliteitsclaim |
| Spel | Bestaande NVIDIA DLSS Frame Generation-integratie en ondersteunde runtime; geen compatibiliteitscertificering tegen cheats |
| Aanbieder | Kandidaat is vastgemaakt aan de provider SHA-256 gedocumenteerd in [herkomst](../docs/provenance.md); onbekende hashes worden geweigerd |
| Looptijd | Gebundelde .NET 8/WPF 8.0.30 voor app/agent; .NET Framework 4.8 voor profielhelpers |
| Machtigingen | Beheerderstoegang voor de controller-/profielbewerkingen |
| Netwerk | Vereist voor geselecteerde officiële SDK-downloads; geïmporteerde compatibele SDKs kan lokaal in de cache worden opgeslagen |
| Externe binaire bestanden | NVIDIA-stuurprogramma, NGX-provider/-modellen en Streamline-gameruntimes zijn niet gebundeld |

Een versielabel alleen is onvoldoende: driver, provider-hash, game-integratie en feitelijk geladen modules zijn van belang. Beschermde of incompatibele processen kunnen bijlage weigeren. De applicatie is niet ontworpen om anti-cheat-beveiligingen te omzeilen.

<a id="installation"></a>
## Installatie

1. Lees de [kandidaatstatus en licentienota](../docs/downloads.md#nvmfg-unlock40).
2. Download `NVMFGUnlock40-0.1.1-Setup-x64.exe` of `NVMFGUnlock40-0.1.1-Portable-x64.zip` zodra de release beschikbaar is.
3. Controleer SHA-256 en bewaar de bijbehorende mededelingen. Installeer .NET Framework 4.8 als Windows dit nog niet biedt.
4. Voer Setup uit of pak de **volledige** draagbare ZIP uit naar een beschrijfbare lokale map.
5. Start `NVMFGUnlock40.exe`; houd `agent`, `driver`, `engine` en `Licenses` in de meegeleverde lay-out.

De map met de naam `driver` bevat helpers voor de gebruikersruimte, geen kernelstuurprogramma. Kopieer niet alleen de hoofd-EXE of vervang de hash van de provider om compatibiliteit te forceren. De huidige EXE's zijn niet ondertekend.

<a id="usage"></a>
## Gebruik

1. Begin met de controller uitgeschakeld. Voeg een game of een bovenliggende map toe en kies de daadwerkelijke installaties.
2. Bekijk de MFG-instellingen van elke game. Beantwoord wat het menu biedt; het antwoord wordt per spel opgeslagen.
3. Kies Dynamic of de algemene in-game-instelling en pas vervolgens indien nodig de in aanmerking komende keuzes per game aan.
4. Schakel de controller alleen in als u deze wilt gebruiken. Het kan tijdelijk zes algemene NVIDIA-profielinstellingen wijzigen, met een herstellogboek.
5. Start een in aanmerking komende game en schakel zijn eigen DLSS Frame Generation in. Volg elk verzoek om de V-Sync-uit-keuze.
6. Gebruik uitsluitingen voor games die je niet wilt beheren. Als u een game verwijdert, wordt een uitsluiting geregistreerd en blijven de bestanden/back-ups behouden.
7. Gebruik de volledige afsluit-/uitschakel- en herstelstroom van de toepassing wanneer u klaar bent.

Als u het hoofdvenster sluit, kan de controller in de lade blijven staan. Een DLL die al in een game is geladen, blijft daar totdat de game wordt afgesloten; het uitschakelen van de controller is geen losgarantie. Sluit de getroffen games vóór onderhoud of updates.

**Streamline SDKs:** download op de NVIDIA SDK-pagina een officiële versie of importeer een compatibele lokale SDK. Import slaat een geverifieerde kopie op; **Use this version** selecteert het en **Uninstall** verwijdert de in de cache opgeslagen kopie. Ontbrekende Streamline DLL's kunnen worden aangevuld met een officiële NVIDIA SDK, met de weergegeven bron. Hiermee wordt geen NGX-model gedownload/vervangen. Sluit het spel, selecteer de beoogde game-update en bewaar de originele back-up. Om gamebestanden terug te zetten, gebruik je de back-upherstelfunctie, niet de Uninstall-knop in de cache.

<a id="screenshots"></a>
## Schermafbeeldingen

![NVMFG SDK-lijstvoorbeeld](../../../../assets/screenshots/nvmfg-0.1.1-sdk-preview.png)

Bestaande Engelse 0.1.1-interfaceweergave met een voorbeeld SDK-inventaris. Het is geen actuele versielijst of bewijs van een actief spel. [Herkomst afbeelding](../assets/README.md).

<a id="update-and-uninstall"></a>
## Updaten en verwijderen

Sluit de betrokken games. Schakel NVMFG uit/af en los eventueel wachtend herstel van de NVIDIA-instellingen op voordat u bijwerkt. Installeer de volgende Setup met de bestaande identiteit, of pak de nieuwe portable uit in een nieuwe map; status/back-ups behouden.

Voordat u de installatie ongedaan maakt, herstelt u de gewenste SDK-back-ups en NVIDIA-instellingen via de applicatie, sluit u vervolgens de games en sluit u de controller af. Gebruik Windows **Installed apps** voor de installatie, of verwijder de gesloten draagbare map nadat u de benodigde bestanden hebt bewaard. Verwijder een actief hersteljournaal niet handmatig om de blokkering van Setup op te heffen.

Lokale game-runtime-back-ups gebruiken `%LOCALAPPDATA%\NvidiaStreamlineMaintenance\Backups`. MFG-instellingen/SDK gegevensgebruik `%LOCALAPPDATA%\RtxMfg`; sessie-uitvoer bevindt zich onder `Sessions` naast de applicatie. Deze bestanden kunnen spelpaden bevatten. Plaats ze niet ongeredigeerd.

<a id="known-limitations"></a>
## Bekende beperkingen

- Experimentele native patches kunnen crashes of visuele artefacten veroorzaken; een onopgeloste Bodycam-crash is vastgelegd in de ontwikkelingsgeschiedenis.
- Gecontroleerde renderertests vormen geen certificering voor elke game, driver of anti-cheat.
- Gegenereerde frames creëren geen nieuwe invoermonsters; deze hub belooft geen gemeten latentie of prestatiewinst.
- Hulpmiddelen/overlays voor het genereren van meerdere frames kunnen conflicteren. De applicatierapporten observeerden modules zonder elk co-existentiescenario te bewijzen.
- Het compatibiliteitsmanifest is een detectiehulpmiddel en geen lijst met volledig geteste games.
- De volledige NVIDIA SDK-voorwaarden en de onopgeloste technische beperking blijven gedocumenteerd in [herkomst](../docs/provenance.md).

<a id="troubleshooting"></a>
## Problemen oplossen

| Symptoom | Actie |
| --- | --- |
| Aanbieder niet ondersteund | Bewaar de originele geverifieerde bestanden. Rapporteer driver-/providerversies en de fout; omzeil de hash-check niet. |
| Geen DLSS FG in het spel | Selecteer dat antwoord en laat het spel onder controle; deze tool kan die integratie niet tot stand brengen. |
| Game crasht/artefacten | Sluit het spel af, schakel NVMFG uit, gebruik de originele runtime-back-up van het spel als deze is gewijzigd, en rapporteer reproduceerbare details. |
| SDK-lijst of download niet beschikbaar | Ververs en controleer de officiële bron; een in de cache opgeslagen/geïmporteerde versie moet nog steeds worden gevalideerd. |
| NVIDIA-herstel in behandeling blokkeert afsluiten/bijwerken | Gebruik herstel en bewaar het dagboek; conflicten mogen niet blindelings worden overschreven. |
| Een verwijderd spel wordt niet herontdekt | De uitsluiting ervan is hardnekkig. Voeg het expliciet toe als u wilt dat het opnieuw wordt beheerd. |

[Gedeelde ondersteuningsbegeleiding](../docs/support.md) legt uit wat u in een rapport moet opnemen.

<a id="faq"></a>
## Veelgestelde vragen

**Bevat het NVIDIA DLL's of modellen?** Er is geen driver, NGX provider/model of Streamline runtime inbegrepen. Expliciete SDK-downloads zijn afkomstig van NVIDIA.

**Werkt Dynamic als V-Sync uitgeschakeld is?** In die staat wordt het programma opgeschort. Kies de in-game-instelling of een in aanmerking komende vaste vermenigvuldiger voor de afzonderlijke status van dat spel.

**Is dit een ReShade/OptiScaler/FSR-pakket?** Nee. Deze worden niet samengesteld of verzonden als onderdeel van dit productiepakket.

**Zijn de gewijzigde bronnen openbaar?** Nee. Gecompileerde pakketten en vereiste credits/licenties worden verstrekt. Hiermee worden de rechten of beperkingen van derden niet opgeheven.

<a id="upstream-and-modifications"></a>
## Stroomopwaarts en wijzigingen

Vergelijkingsreferentie en gedeelde native componenten: **RTX40MFG-Unlock door Michael Robles / dashdogy**, referentiecommit `4e776d068f91b4a665425542bb005dd57cc3d891`, MIT. [Bewaarplaats](https://github.com/dashdogy/RTX40MFG-Unlock) · [Originele downloads](https://github.com/dashdogy/RTX40MFG-Unlock/releases).

De bronvergelijking identificeert gedeelde patching, provider/beleidsafhandeling, tijdelijke correcties en op MinHook gebaseerde omleidingscomponenten. Hun MIT- en BSD-kennisgevingen blijven behouden. De volledige vergelijking omvat ook bestanden buiten het productiedoel.

De desktopapplicatie, controller en SDK-beheerworkflow zijn ontwikkeld door 禅堂 Zendo (RevoluSound Team). Het projectwerk omvat centraal laden, NGX bootstrap-integratie, geverifieerde providerselectie, game/V-Sync-coördinatie en sessiediagnostiek. De herkomstgids scheidt dat werk van de gedeelde componenten; alleen uit een bestandsvergelijking blijkt niet wanneer een van de auteurs het idee had.

De profielhelper past de MIT NVAPI-wrapper aan van Orbmu2k's Profile Inspector. [Gedetailleerde herkomst en reikwijdte van de componenten](../docs/provenance.md).

<a id="credits-and-license"></a>
## Credits en licentie

Michael Robles; Orbmu2k; Tsuda Kageyu- en HDE-bijdragers; NVIDIA Corporation; Microsoft en bijdragers; Inno Setup auteurs en vertalers. Applicatieontwikkeling, integraties en verpakking: 禅堂 Zendo (RevoluSound Team).

De [bestaande machtiging voor het delen van gecompileerde pakketten](../../../../NVMFG-Unlock40/LICENSE) en alle [componentlicenties](LICENSES/README.md) blijven behouden. MIT-machtigingen voor upstream-code verschillen van NVIDIA SDK-termen. Geen enkele algemene licentie vervangt ze.

Onafhankelijk van, niet gesponsord door en niet officieel goedgekeurd door NVIDIA Corporation. Alle handelsmerken waarnaar wordt verwezen, blijven eigendom van hun eigenaren.
