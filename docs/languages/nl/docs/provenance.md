<!-- nv-language-navigation:start -->
🌐 [English](../../../provenance.md) | [Français](../../../provenance.fr.md) · [NV Laboratory](../README.md)

<details>
<summary>🌐 Language · 34</summary>

[العربية](../../ar/docs/provenance.md) · [বাংলা](../../bn/docs/provenance.md) · [简体中文](../../zh/docs/provenance.md) · [Čeština](../../cs/docs/provenance.md) · [Dansk](../../da/docs/provenance.md) · **Nederlands** · [English](../../../provenance.md) · [Filipino](../../fil/docs/provenance.md) · [Suomi](../../fi/docs/provenance.md) · [Français](../../../provenance.fr.md) · [Deutsch](../../de/docs/provenance.md) · [Ελληνικά](../../el/docs/provenance.md) · [हिन्दी](../../hi/docs/provenance.md) · [Magyar](../../hu/docs/provenance.md) · [Bahasa Indonesia](../../id/docs/provenance.md) · [Italiano](../../it/docs/provenance.md) · [日本語](../../ja/docs/provenance.md) · [한국어](../../ko/docs/provenance.md) · [मराठी](../../mr/docs/provenance.md) · [فارسی](../../fa/docs/provenance.md) · [Polski](../../pl/docs/provenance.md) · [Português](../../pt/docs/provenance.md) · [ਪੰਜਾਬੀ](../../pa/docs/provenance.md) · [Română](../../ro/docs/provenance.md) · [Русский](../../ru/docs/provenance.md) · [Español](../../es/docs/provenance.md) · [Kiswahili](../../sw/docs/provenance.md) · [Svenska](../../sv/docs/provenance.md) · [தமிழ்](../../ta/docs/provenance.md) · [ไทย](../../th/docs/provenance.md) · [Türkçe](../../tr/docs/provenance.md) · [Українська](../../uk/docs/provenance.md) · [اردو](../../ur/docs/provenance.md) · [Tiếng Việt](../../vi/docs/provenance.md)

[Translation policy](../../README.md)

</details>
<!-- nv-language-navigation:end -->

<!-- nv-translation-notice:start -->
> Machineondersteunde vertaling uit het Engels. Technische namen, commando's, URL's en originele juridische teksten blijven behouden. Recensie door native speakers is welkom; raadpleeg de Engelse referentie als de formulering onduidelijk is.
<!-- nv-translation-notice:end -->

<a id="provenance-changes-and-licensing"></a>
# Herkomst, wijzigingen en licenties

Deze audit beschrijft de kandidaten die zijn voorbereid op **2026-09-18**. Applicatiebronnen blijven privé; de openbare inventarissen bevatten bestandsnamen en hashes, geen broncode. Zie [mededelingen over volledige componenten](../THIRD_PARTY_NOTICES.md).

<a id="nvidia-profile-inspector--nv-tools-fork"></a>
## NVIDIA Profile Inspector – NV Tools Fork

Referentie: Orbmu2k/nvidiaProfileInspector commit `592d962cca8827efe8859461a84267755595064a`; kandidaat-uitvoerbare versie 3.0.2.3. De referentiecommit en de assemblageversie van fork zijn verschillende identificatiegegevens; er wordt geen upstream-releaseversie afgeleid van de fork-versie.

De 157 bron-/bronbestanden van de schone metgezel werden vergeleken met die commit: 2 byte-identiek, 134 verschilden alleen in regeleindes of UTF-8 BOM, 11 gewijzigd, 10 afwezig op het vergeleken stroomopwaartse pad. “Toegevoegd” heeft betrekking op dat pad en is op zichzelf geen bewijs van origineel auteurschap.

[Volledige bestands-/hash-vergelijking](../../../provenance/nvpi-source-provenance.json).

| Gebied | Erfelijk werk | Fork bijdrage |
| --- | --- | --- |
| Profiel-editor | Profielmodel, import/export, applicatiekoppelingen en referentiegegevens | Integratie met Screen en de externe toollauncher |
| NVAPI | Orbmu2k's DRS-interoperabiliteit | Kleur/weergave-gerelateerde interoperabiliteit, productie-native laadbeperkingen en schijnverwijdering |
| Diensten weergeven | Windows/NVIDIA API's als externe interfaces | DisplayInfoService, DisplayConfigurationService, DisplaySettingsBackend |
| gebruikersinterface | Upstream WPF-bronnen, paletten en pictogrammen | Schermdialogen, 15-secondenbevestiging, status/teruglezen en werkbalkindeling |
| Lanceerder | Bestaande app-shell | Beschermd afzonderlijk geïnstalleerde RasterPulse opzoeken en starten |
| Verpakking | MIT stroomopwaarts | Schone zelfstandige metgezel, afzonderlijk installatie-/verwijderprogramma, bewaarde mededelingen |

De openbare bronkaart bevat oplossings-/bronpaden voor traceerbaarheid; die bestanden worden niet als bron gedistribueerd. Ontwikkelingstests, nep-interfaces en het oude gecombineerde binaire bestand NVPI/RasterPulse zijn uitgesloten.

<a id="nvdriverforge"></a>
## NVDriverForge

Onafhankelijke C#/.NET 8/WPF-applicatie; de gebruikersgerichte workflow is gedeeltelijk geïnspireerd door NVCleanstall. Er is geen NVCleanstall-bron/binair bestand geïdentificeerd in de productiepayload. Het wordt niet weergegeven als een fork van die eigen applicatie.

Het oorspronkelijke projectwerk omvat analyse/selectie van componenten, beveiligde installatietaken, back-ups en transactieherstel, NVIDIA-catalogusdownloads, updatecontroles, gelokaliseerde uitleg, optionele geavanceerde/NVENC-workflows en installer-bootstrap.

Overgenomen/aangepaste componenten: vier NVPI-themapaletten, uitgebreide NVAPI DRS-interfacereferentie en de afzonderlijk optionele MIT NVPI-begeleider. De selectie-UI van de Custom NV-voorinstelling en de transactie-integratie op de toelatingslijst behoren tot NVDriverForge; de voorinstelling is geen officiële NVIDIA-aanbeveling.

7-Zip 26.03, .NET/WPF 8.0.31 en Inno Setup blijven ongewijzigde externe componenten die onder hun eigen voorwaarden worden gebruikt. keylase NVENC-gegevens zijn niet ingebed; er wordt één exacte commit gekozen en gecontroleerd wanneer de gebruiker een compatibele download aanvraagt. Er is geen herdistributielicentie ingesteld voor die upstreamgegevens.

<a id="nvmfg-unlock40"></a>
## NVMFG Unlock40

NVMFG Unlock40 is onafhankelijk ontwikkeld door 禅堂 Zendo (RevoluSound Team). De beheerder gebruikte RTX40MFG-Unlock voor vergelijking en verfijning. De applicatie als geheel wordt niet gepresenteerd als fork. Dit onderscheid verwijdert de credits voor gedeelde/aangepaste componenten in de huidige native laag niet.

Vergelijkingsreferentie: dashdogy/RTX40MFG-Unlock, Michael Robles, MIT, commit `4e776d068f91b4a665425542bb005dd57cc3d891`. De privé-native-engine-boom bevat 48 vergeleken bestanden: 35 verschillen in alleen opmaak, 4 gewijzigde bestanden en 9 afwezig in het referentiepad. [Volledige vergelijking](../../../provenance/nvmfg-source-provenance.json).

Gewijzigde overgenomen bestanden: `entry_detour.h`, `patcher.cpp`, `temporal_interval_trace.cpp`, `temporal_interval_trace.h`. Extra paden zijn `game_selection.*`, `ngx_bootstrap.*`, `ngx_capability.h`, `presentation_tracker.h`, `vsync_observer.*` en een behouden upstream-licentie.

Productie C++-eenheden: patcher, midpoint_fix, dlssg_provider_policy, entry_detour, nvidia_mfg_policy, temporal_interval_trace, ngx_bootstrap, game_selection en vsync_observer; plus entry_detour-montage en MinHook-buffer/haak/trampoline/HDE64. De overgenomen ReShade-frontend, oudere shim-bronnen en ongebruikte CMake-doelen maken geen deel uit van deze productiecompilatie.

De bijpassende componenten omvatten patching/providerbeleid en tijdelijk werk; hun copyright- en toestemmingskennisgevingen blijven intact. De centrale coördinatie van NGX/bootstrap/controller, V-Sync-afhandeling per game, sessiediagnostiek en Windows-applicatie/SDK/back-upworkflow zijn projectwerk van 禅堂 Zendo (RevoluSound Team). De bovenstaande tellingen beschrijven bestanden, inclusief bestanden van derden en ongebruikte bestanden, en niet het auteurschapspercentage of de chronologie van het idee van een van beide projecten.

De helper past de NvapiDrsWrapper en NativeArrayHelper van NVPI aan in een afzonderlijke assembly, met door het project geschreven profiellogica. Het oude ontwikkel-neppad is uitgesloten. Gedeelde familiepaletten zijn afkomstig van NVPI.

MinHook referentie: `8fda4f5481fed5797dc2651cd91e238e9b3928c6`; de overgeërfde gecompileerde subset heeft geen functionele lokale veranderingen in de vergelijking. Streamline-integratieheaders: 2.12; open header-licentie geverifieerd op v2.12.0. NGX-headerbron: NVIDIA/DLSS commit `a291cc7d2cc642a51566f3dfd5376f635cd1b284`.

Kandidaat-engine SHA-256: `C793770D329B99CD9C5C640317CE435BFE353CA2868E36CF5DCD4D5295EFAE13`.

Vereiste provider SHA-256 in engine.json: `C64928FDB7C48A57722EA8EEF2662171EDC323473ADEA66C29A206A23F1A2BED`. Een gerapporteerde 310.9-providerfamilie is niet uitwisselbaar met deze exacte hash. Er is geen provider-DLL of -model inbegrepen.

**Uitstaand licentiepunt:** de volledige NVIDIA RTX SDK-licentie, versie 14 maart 2024, bevat een sectie 4(d)-beperking die relevant is voor het omzeilen van technische beperkingen. Uit de audit blijkt geen toestemming voor dit gebruik. Het behouden van de MIT-motorlicentie, het gratis zijn of het observeren van andere mods lost deze afzonderlijke voorwaarde niet op. De voorbereiding van kandidaten is geen wettelijke goedkeuring. De originele korte headeraankondiging wordt aangevuld met de volledige licentie; de Windows-1252-tekst wordt ook geleverd als leesbare UTF-8, waarbij de originele bytes behouden blijven.

De oorspronkelijke vergelijking is opnieuw berekend voor 0.2.3: dezelfde 48 bestanden en classificaties. Sinds de vorige audit zijn `game_selection.cpp`, `game_selection.h` en `patcher.cpp` gewijzigd voor observaties van activiteiten/mogelijkheden. Nieuwe bibliotheek-, diagnose-, voorkeurs-, update- en selectieworkflows behoren tot de onderhoudsapplicatie. Componentlicenties en de vereiste provider-hash blijven ongewijzigd.

<a id="nvrasterpulse"></a>
## NVRasterPulse

Onafhankelijke RTSS-profielmanager ontwikkeld in de van NVPI afgeleide repository. De overgenomen MIT UI-bronnen/paletten en projectoorsprong blijven gecrediteerd. De productie-app maakt expliciet gebruik van de meegeleverde MIT-licentie.

Projectwerk: nauwkeurig parseren/schrijven van RTSS-profielen en fractionele codering, back-ups, verwijdering van overschrijvingen, herlaadbrug, detectie van vereisten, compacte gebruikersinterface, levenscyclus van lade, opstartcontroles en lokalisatie. RTSS voert daadwerkelijke beperking uit.

Er is geen RTSS-bron, hook-DLL, SDK of installatieprogramma gebundeld. De bridge roept de export aan in een bestaande, door de gebruiker geselecteerde RTSS-installatie. Dit pakket bevat geen NVIDIA driverpakket, native experimentele limiter, Framepacer, MinHook, ReShade of DLSS runtime.

<a id="assets-generated-data-and-tools"></a>
## Activa, gegenereerde data en tools

[Activakredieten](../assets/README.md) identificeert de bestaande interfacevoorbeelden en de NVPI setup-selector. De fictieve waarden daarin zijn gelabeld. Er worden geen game-/Nexus-items, persoonlijk profiel, privé ICC, bedrijfslogo of lettertypebestand van NVIDIA gekopieerd.

Gegenereerde namen voor spelcompatibiliteit die zijn overgenomen in NVMFG zijn een detectiehulpmiddel en geen testbewijs. Gegenereerde installateurcatalogi worden vermeld in [vertaler merkt op](../../../../licenses/INSTALLER-TRANSLATORS.md). Gegenereerde buildrecords met absolute paden blijven privé.

Privé-buildtools omvatten .NET SDK/MSBuild, Visual Studio C++/MASM, Windows SDK, PowerShell, Inno Setup en Python auditscripts. Hun compilers, headers, testrunners en debug-middelen worden niet gedistribueerd. CRT voor statische releases valt onder de toepasselijke toolchain-voorwaarden van Microsoft.

<a id="scope-of-verification"></a>
## Reikwijdte van de verificatie

De lokale audit inventariseerde alle bestanden in de drie ontwikkelingswortels, terwijl Git-objectdatabases en gekoppelde mapdoelen werden uitgesloten. Actieve bron/documenten zijn gescand; historische bouwwerken werden geïnventariseerd en uitgesloten. Geselecteerde ZIP's en huidige payloads werden gescand en gehasht; de .NET-bundels zijn gedecomprimeerd voor aanvullende inspectie. Bij die eerste audit werd geen product, installatieprogramma, game, RTSS-proces of stuurprogramma uitgevoerd.

De latere NVPI setup-revisie 2 repareert de stand-alone taalselectie met behulp van de gedeelde Inno-besturingselementen en bootstrap. Licht/donker privéarmaturen geverifieerd muis- en toetsenbordnavigatie en alle 34 expliciete taalcodes. De daadwerkelijke installatiekiezer werd geopend op een nooit weergegeven privébureaublad en geannuleerd vóór de installatie. De zeven applicatiebestanden en draagbare ZIP zijn ongewijzigd. NVDriverForge 0.1.3 bevat de gecorrigeerde begeleider en stuurt nog steeds `/LANG` door.

NVDriverForge 0.1.3 werd voltooid op 10-09-2026. Het privéverificatierapport registreert 366 applicatietests, 118 begeleidende controles, 32 instellingscontroles, 156 native vergelijkingen en 34 gevallen van taaldoorsturen. De beveiligde componentselectie-fix werd afgespeeld tegen een origineel driverpakket zonder de payload te wijzigen of de driver te installeren. Dit zijn gedateerde resultaten van het productteam, geen tests die opnieuw zijn uitgevoerd door deze documentatie-update of een bewijs van een succesvolle installatie van een echt stuurprogramma.

Deze hubupdate verandert geen functionele applicatiecode. Eerdere tests voor het bouwen van applicaties/units/UI blijven gedateerd historisch bewijsmateriaal. Dit is geen volledige reverse engineering van elk binair bestand van derden of een garantie tegen elk mogelijk geheim patroon.

Update van 18 september 2026: NVDriverForge 0.1.4 voegt gereedheidscontroles, native profielback-up, componentbegeleiding, voorkeuren en kits, gedetailleerde resultaten, lokale rapportage en applicatie-updates toe. NVRasterPulse 0.2 voegt configuratiediagnostiek, FPS-begeleiding, pauzeren/hervatten, ongedaan maken, `.nvrp`-profielen en favorieten/verbergen toe, zonder een nieuwe limiter-engine. Individuele handleidingen beschrijven het gebruik en de limieten. Statische hubcontroles staan ​​los van de applicatietests die zijn vastgelegd in de privérapporten van 18 september; Voor deze hub zijn geen stuurprogramma-installatie, echte profielimport of latentiemeting uitgevoerd.
