<!-- nv-language-navigation:start -->
🌐 [English](../../../../NVIDIA-Profile-Inspector/README.md) | [Français](../../../../NVIDIA-Profile-Inspector/README.fr.md) · [NV Laboratory](../README.md)

<details>
<summary>🌐 Language · 34</summary>

[العربية](../../ar/NVIDIA-Profile-Inspector/README.md) · [বাংলা](../../bn/NVIDIA-Profile-Inspector/README.md) · [简体中文](../../zh/NVIDIA-Profile-Inspector/README.md) · [Čeština](../../cs/NVIDIA-Profile-Inspector/README.md) · [Dansk](../../da/NVIDIA-Profile-Inspector/README.md) · **Nederlands** · [English](../../../../NVIDIA-Profile-Inspector/README.md) · [Filipino](../../fil/NVIDIA-Profile-Inspector/README.md) · [Suomi](../../fi/NVIDIA-Profile-Inspector/README.md) · [Français](../../../../NVIDIA-Profile-Inspector/README.fr.md) · [Deutsch](../../de/NVIDIA-Profile-Inspector/README.md) · [Ελληνικά](../../el/NVIDIA-Profile-Inspector/README.md) · [हिन्दी](../../hi/NVIDIA-Profile-Inspector/README.md) · [Magyar](../../hu/NVIDIA-Profile-Inspector/README.md) · [Bahasa Indonesia](../../id/NVIDIA-Profile-Inspector/README.md) · [Italiano](../../it/NVIDIA-Profile-Inspector/README.md) · [日本語](../../ja/NVIDIA-Profile-Inspector/README.md) · [한국어](../../ko/NVIDIA-Profile-Inspector/README.md) · [मराठी](../../mr/NVIDIA-Profile-Inspector/README.md) · [فارسی](../../fa/NVIDIA-Profile-Inspector/README.md) · [Polski](../../pl/NVIDIA-Profile-Inspector/README.md) · [Português](../../pt/NVIDIA-Profile-Inspector/README.md) · [ਪੰਜਾਬੀ](../../pa/NVIDIA-Profile-Inspector/README.md) · [Română](../../ro/NVIDIA-Profile-Inspector/README.md) · [Русский](../../ru/NVIDIA-Profile-Inspector/README.md) · [Español](../../es/NVIDIA-Profile-Inspector/README.md) · [Kiswahili](../../sw/NVIDIA-Profile-Inspector/README.md) · [Svenska](../../sv/NVIDIA-Profile-Inspector/README.md) · [தமிழ்](../../ta/NVIDIA-Profile-Inspector/README.md) · [ไทย](../../th/NVIDIA-Profile-Inspector/README.md) · [Türkçe](../../tr/NVIDIA-Profile-Inspector/README.md) · [Українська](../../uk/NVIDIA-Profile-Inspector/README.md) · [اردو](../../ur/NVIDIA-Profile-Inspector/README.md) · [Tiếng Việt](../../vi/NVIDIA-Profile-Inspector/README.md)

[Translation policy](../../README.md)

</details>
<!-- nv-language-navigation:end -->

<!-- nv-translation-notice:start -->
> Machineondersteunde vertaling uit het Engels. Technische namen, commando's, URL's en originele juridische teksten blijven behouden. Recensie door native speakers is welkom; raadpleeg de Engelse referentie als de formulering onduidelijk is.
<!-- nv-translation-notice:end -->

<a id="nvidia-profile-inspector--nv-tools-fork"></a>
# NVIDIA Profile Inspector – NV Tools Fork

**Een onafhankelijke fork van [NVIDIA Profile Inspector door Orbmu2k](https://github.com/Orbmu2k/nvidiaProfileInspector), met extra weergaveknoppen.** Voormalige projectnaam: **NVPI Custom**.

[Download- en releasestatus](../docs/downloads.md#nvidia-profile-inspector) · [Installatie](#installation) · [Stroomopwaarts en veranderingen](#upstream-and-changes) · [Licentie](../../../../NVIDIA-Profile-Inspector/LICENSE)

<a id="overview"></a>
## Overzicht

De applicatie bewerkt NVIDIA-stuurprogrammaprofielen, inclusief instellingen per applicatie. Deze fork voegt ook een **Scherm**-editor toe voor het actieve Windows-scherm: resolutie, vernieuwingsfrequentie, uitvoerkleurinstellingen, HDR en geïnstalleerde ICC/WCS-profielassociaties.

Het is bedoeld om gerelateerde weergaveknoppen in de profieleditor te brengen en om voorbeeld-, bevestigings- en herstelresultaten duidelijker te maken. Het creëert geen nieuwe hardwaremogelijkheden.

De eerste kandidaat is **3.0.2.3**, die gebruikmaakt van de opgeschoonde zelfstandige begeleidende build van 9 september 2026. Het bestaande uitvoerbare bestand blijft `nvidiaProfileInspector.exe`; het installatieprogramma en sommige interne labels zeggen nog steeds `NVPI Custom NV`. De openbare titel hierboven identificeert de fork zonder de installatie-identiteit te wijzigen of te doen alsof het de officiële release van Orbmu2k is.

<a id="features"></a>
## Kenmerken

- Bestaande upstream profielbrowsen, applicatiekoppelingen, instellingsbewerkingen en profielimport/export.
- **Scherm** dialoogvenster voor weergave, modus, Hz, RGB/YCbCr, kleurdiepte, bereik en colorimetrie.
- Windows HDR controle en geïnstalleerde ICC/WCS associatieselectie.
- Een weergavevoorbeeld van 15 seconden met **Keep** / **Revert** en time-outherstel.
- Teruglezen van modus/HDR-wijzigingen en gerapporteerde herstelfouten.
- Afzonderlijke rapportage van HDR, SDR met ACM/WCG en signaalkleurdiepte.
- Een NVRasterPulse-opstartprogramma voor een in aanmerking komend afzonderlijk geïnstalleerd exemplaar.

<a id="compatibility"></a>
## Compatibiliteit

| Vereiste | Details |
| --- | --- |
| Systeem | Windows 10/11 x64 met een compatibel NVIDIA-stuurprogramma |
| Looptijd | [.NET Framework 4.8](https://dotnet.microsoft.com/en-us/download/dotnet-framework/net48), geleverd door Windows of afzonderlijk geïnstalleerd |
| Machtigingen | De editor vraagt bij het openen om beheerderstoegang |
| Beeldschermen | Werkelijke modi en kleurencombinaties zijn afhankelijk van GPU, driver, display, kabel en Windows API's |
| Optioneel gereedschap | NVRasterPulse voor RTSS-limietbeheer; noch RTSS, noch dit, is nodig voor de Schermeditor |
| Talen | Configuratie: 34-talenkiezer. De editor behoudt zijn bestaande taalondersteuning. |

Er is geen geverifieerd universeel driverminimum of ondersteuningsmatrix voor elke GPU. De beschikbare bpc-keuzes in het dialoogvenster zijn verzoeken, geen gecertificeerde combinaties. Moderne HDR-bedieningselementen en de oudere Windows-fallback hebben verschillende mogelijkheden.

<a id="installation"></a>
## Installatie

1. Open de [downloadpagina](../docs/downloads.md#nvidia-profile-inspector) en controleer de publicatiestatus.
2. Download de Setup of het draagbare asset en vergelijk de SHA-256 met het Release-manifest.
3. Voer voor Setup `NVPI-CustomNV-3.0.2.3-Setup-r2.exe` uit, selecteer een taal en volg het installatieprogramma. Het creëert zijn eigen snelkoppeling en verwijderprogramma.
4. Voor draagbaar: pak de volledige ZIP uit naar een nieuwe beschrijfbare map. Bewaar `Reference.xml`, de EXE-configuratie en alle mededelingen naast het uitvoerbare bestand.
5. Start `nvidiaProfileInspector.exe`.

Als u alleen de editor installeert, wordt er geen profiel toegepast en wordt er geen GPU-stuurprogramma geïnstalleerd. De begeleidende installatie wordt afzonderlijk geïnstalleerd, neemt geen `.nip`-associaties over en maakt opstarten bij inloggen niet mogelijk. Bestaande binaire bestanden zijn niet ondertekend.

<a id="usage"></a>
## Gebruik

**Installatieprogrammarevisie 2** voegt dezelfde native 34-talenkiezer toe als de andere tools, met muis-/toetsenbordnavigatie, licht/donker uiterlijk en annulering. De keuze geldt voor de opstelling; het vertaalt de NVPI-editor niet. Een expliciet `/LANG=fr`-argument of stille modus omzeilt de selectie voor bellers die al een taal aanbieden.

**Bestuurderprofielen:** selecteer een profiel, exporteer een back-up, bewerk vervolgens alleen de bedoelde instellingen en pas deze toe. Applicatiekoppelingen bepalen welke game een profiel krijgt. Een opgeslagen waarde is geen bewijs dat elke driver of game deze gebruikt.

**Weergavebediening:** open **Scherm**, kies de weergave en de gewenste waarden en start vervolgens het voorbeeld. Controleer de afbeelding voordat u **Keep** kiest binnen 15 seconden. Gebruik **Herstellen**, sluit de bevestiging of laat deze verlopen om herstel aan te vragen. Lees elk foutbericht: een succesvolle API-aanroep alleen is geen bewijs van herstel.

Een ICC-selectie wijzigt een geïnstalleerde profielkoppeling; het genereert, kalibreert of herdistribueert geen ICC-bestand. HDR, ACM/WCG, RGB/YCbCr en bpc beschrijven verschillende aspecten van de pijplijn. Er is geen nieuwe onafhankelijke ACM-schakelaar voorzien.

**NVRasterPulse:** de werkbalkknop accepteert een afzonderlijk geregistreerde systeembrede installatie onder Programmabestanden met beschermd eigendom en machtigingen. Een draagbare kopie of een door de gebruiker beschrijfbaar/gekoppeld pad kan door dit verhoogde opstartprogramma worden geweigerd. Open in dat geval NVRasterPulse via een eigen snelkoppeling. [Installeer RTSS afzonderlijk](https://www.guru3d.com/download/rtss-rivatuner-statistics-server-download/) om NVRasterPulse te gebruiken.

<a id="screenshots"></a>
## Schermafbeeldingen

![NVPI setup revisie 2 taalkiezer](../../../../assets/screenshots/nvpi-setup-r2-language.png)

Werkelijke setup-selector in het Frans, vastgelegd tijdens een geïsoleerde test en vervolgens geannuleerd. Dit toont het installatieprogramma; de editor behoudt zijn interface en schermdialoog.

<a id="update-and-uninstall"></a>
## Updaten en verwijderen

Sluit de editor voordat u gaat updaten. Bewaar geëxporteerde profielen en download de nieuwe fork-release; installeer over dezelfde begeleidende identiteit of extraheer draagbare bestanden naar een nieuwe map. Meng geen oude `Reference.xml` met een nieuw uitvoerbaar bestand. De gebundelde upstream update-check-onderdrukking hoort bij deze fork.

Voor een geïnstalleerd exemplaar gebruikt u Windows **Installed apps** en het bijbehorende verwijderprogramma. Voor draagbaar: sluit het en verwijder de uitgepakte map wanneer uw export veilig is. Als u de editor verwijdert, worden wijzigingen in het stuurprogrammaprofiel, weergavevoorkeuren, NVRasterPulse of RTSS **niet** ongedaan gemaakt. Herstel de gewenste instellingen voordat u deze verwijdert.

<a id="known-limitations"></a>
## Bekende beperkingen

- De bevestiging van 15 seconden is geen waakhond voor elke crash van de bestuurder, stroomuitval of gedwongen uitschakeling.
- Sommige kleur/diepte/vernieuwingscombinaties retourneren `NVAPI_NOT_SUPPORTED`.
- Software-uitlezing meet geen paneelbitdiepte, kleurnauwkeurigheid of latentie.
- Scherminstellingen zijn van invloed op het huidige Windows-display; dit dialoogvenster maakt geen voorinstellingen voor de weergave per game.
- Geen prestatie-, anti-cheat- of universele HDR-compatibiliteitsgarantie.

<a id="troubleshooting"></a>
## Problemen oplossen

| Symptoom | Actie |
| --- | --- |
| Runtimefout bij opstarten | Controleer Windows-updates en .NET Framework 4.8; gebruik het volledige pakket. |
| Gevraagde weergavemodus afgewezen | Herstel en test een modus die wordt aangeboden door Windows/NVIDIA voor dat beeldscherm. Lees de exacte fout en vermijd herhaalde blinde wijzigingen. |
| HDR of kleur keert terug naar de oude staat | Controleer of een andere bewerking is mislukt en herstel heeft geactiveerd; onderscheid HDR van ACM. |
| NVRasterPulse-knop weigert een pad | Lanceer zijn eigen snelkoppeling; deze knop vereist een beschermde systeembrede installatie. |
| Na het verwijderen blijft er een wijziging bestaan | Herstel het geëxporteerde NVIDIA-profiel of de beoogde Windows-weergave-instellingen; verwijderen is geen terugdraaien van instellingen. |

Zie [gedeelde ondersteuningsbegeleiding](../docs/support.md) voordat u logbestanden verzendt.

<a id="faq"></a>
## Veelgestelde vragen

**Is dit officiële NVIDIA-software of de officiële build van Orbmu2k?** Nee. Het is een onafhankelijke fork; de upstream-auteur en MIT-licentie blijven gecrediteerd.

**Heeft NVDriverForge deze editor nodig?** Nee. De optionele Custom NV-voorinstelling van NVDriverForge gebruikt zijn eigen integratie. Het installeren van de editor is een aparte keuze.

**Is RTSS verplicht voor deze fork?** Nee. RTSS is verplicht voor de FPS-limiter van NVRasterPulse, niet voor profiel- of schermbewerking.

**Waar is de bron?** De gewijzigde applicatiebron wordt privé onderhouden. De MIT-kennisgeving en upstream-repository zijn aanwezig; MIT vereist geen publicatie van gewijzigde broncode.

<a id="upstream-and-changes"></a>
## Stroomopwaarts en veranderingen

Upstream: [Orbmu2k/nvidiaProfileInspector](https://github.com/Orbmu2k/nvidiaProfileInspector), referentiecommit `592d962cca8827efe8859461a84267755595064a`. [Originele downloads](https://github.com/Orbmu2k/nvidiaProfileInspector/releases).

Overgenomen: profieleditor, NVAPI-interoperabiliteit, referentiegegevens, UI-bronnen en thema's. 禅堂 Zendo (RevoluSound Team) heeft weergaveservices toegevoegd of aangepast, HDR/ICC-transacties, 15 seconden bevestiging/teruglezen, werkbalkindeling en RasterPulse-startgedrag. De opgeschoonde metgezel sluit ontwikkelingsmocks/testinvoerpunten uit, gebruikt een beschermd extern opstartprogramma en biedt een afzonderlijk installatieprogramma. Het oude gecombineerde NVPI/RasterPulse-ontwikkelpakket is niet de kandidaat in deze hub.

[Gedetailleerde herkomst van het bestand](../docs/provenance.md) · [Originele fork-kennisgeving](../../../../NVIDIA-Profile-Inspector/LICENSES/ORIGINAL-FORK-NOTICE.txt)

<a id="credits-and-license"></a>
## Credits en licentie

Auteursrecht (c) 2016 Orbmu2k. De meegeleverde [MIT-licentie](../../../../NVIDIA-Profile-Inspector/LICENSE) blijft behouden. Aanpassingen en verpakking: 禅堂 Zendo (RevoluSound Team). Het installatieprogramma gebruikt Inno Setup; Windows en .NET Framework blijven extern. [Volledige toepasselijke mededelingen](LICENSES/README.md).

Onafhankelijk van, niet gesponsord door en niet officieel goedgekeurd door NVIDIA Corporation. Handelsmerken blijven eigendom van hun respectievelijke eigenaren.
