<!-- nv-language-navigation:start -->
🌐 [English](../../../../NVRasterPulse/README.md) | [Français](../../../../NVRasterPulse/README.fr.md) · [NV Laboratory](../README.md)

<details>
<summary>🌐 Language · 34</summary>

[العربية](../../ar/NVRasterPulse/README.md) · [বাংলা](../../bn/NVRasterPulse/README.md) · [简体中文](../../zh/NVRasterPulse/README.md) · [Čeština](../../cs/NVRasterPulse/README.md) · [Dansk](../../da/NVRasterPulse/README.md) · **Nederlands** · [English](../../../../NVRasterPulse/README.md) · [Filipino](../../fil/NVRasterPulse/README.md) · [Suomi](../../fi/NVRasterPulse/README.md) · [Français](../../../../NVRasterPulse/README.fr.md) · [Deutsch](../../de/NVRasterPulse/README.md) · [Ελληνικά](../../el/NVRasterPulse/README.md) · [हिन्दी](../../hi/NVRasterPulse/README.md) · [Magyar](../../hu/NVRasterPulse/README.md) · [Bahasa Indonesia](../../id/NVRasterPulse/README.md) · [Italiano](../../it/NVRasterPulse/README.md) · [日本語](../../ja/NVRasterPulse/README.md) · [한국어](../../ko/NVRasterPulse/README.md) · [मराठी](../../mr/NVRasterPulse/README.md) · [فارسی](../../fa/NVRasterPulse/README.md) · [Polski](../../pl/NVRasterPulse/README.md) · [Português](../../pt/NVRasterPulse/README.md) · [ਪੰਜਾਬੀ](../../pa/NVRasterPulse/README.md) · [Română](../../ro/NVRasterPulse/README.md) · [Русский](../../ru/NVRasterPulse/README.md) · [Español](../../es/NVRasterPulse/README.md) · [Kiswahili](../../sw/NVRasterPulse/README.md) · [Svenska](../../sv/NVRasterPulse/README.md) · [தமிழ்](../../ta/NVRasterPulse/README.md) · [ไทย](../../th/NVRasterPulse/README.md) · [Türkçe](../../tr/NVRasterPulse/README.md) · [Українська](../../uk/NVRasterPulse/README.md) · [اردو](../../ur/NVRasterPulse/README.md) · [Tiếng Việt](../../vi/NVRasterPulse/README.md)

[Translation policy](../../README.md)

</details>
<!-- nv-language-navigation:end -->

<!-- nv-translation-notice:start -->
> Machineondersteunde vertaling uit het Engels. Technische namen, commando's, URL's en originele juridische teksten blijven behouden. Recensie door native speakers is welkom; raadpleeg de Engelse referentie als de formulering onduidelijk is.
<!-- nv-translation-notice:end -->

<a id="nvrasterpulse"></a>
# NVRasterPulse

**FPS-limieten per applicatie via RivaTuner Statistics Server.**

> **Installeer eerst RTSS.** NVRasterPulse vereist [RivaTuner Statistics Server (RTSS), gedownload van Guru3D](https://www.guru3d.com/download/rtss-rivatuner-statistics-server-download/). RTSS moet actief zijn om limieten af ​​te dwingen. Er is geen RTSS-installatieprogramma, hook-DLL of SDK gebundeld.

[Download 0.2 en status](../docs/downloads.md#nvrasterpulse) · [Installatie](#installation) · [Hoe grenzen werken](#usage) · [Licentie](../../../../NVRasterPulse/LICENSE)

<a id="overview-and-purpose"></a>
## Overzicht en doel

NVRasterPulse is een compacte Windows-interface voor het beheren van RTSS-framelimieten op uitvoerbare naam. RTSS voert de beperking uit. NVRasterPulse beheert de bijbehorende profielwaarden, back-ups en herlaadverzoeken, met ladetoegang en permanente keuzes.

Het is bedoeld om de exacte limieten per spel gemakkelijker te kunnen bewerken zonder een heel RTSS-profiel te vervangen of de overlay-instellingen te verstoren. Versie **0.2** voegt configuratiediagnostiek, een FPS-helper, pauzeren, ongedaan maken en profiel delen toe.

<a id="features"></a>
## Kenmerken

- Selecteer een actieve applicatie of voeg het uitvoerbare bestand handmatig toe.
- Bewaar FPS-limieten van 1 tot 1000, met maximaal drie decimalen.
- Exacte rationele codering van ingevoerde waarden: 59.94 wordt 2997/50.
- Front Edge Sync-configuratie (`SyncLimiter=1`) met actieve wachttijd (`PassiveWait=0`).
- Per uitvoerbare profielupdates, automatische back-ups en atomaire schrijfbewerkingen.
- Verwijdering van limiter-overschrijvingen met behoud van andere profielinhoud.
- RTSS installatiedetectie, handmatige padselectie en expliciet starten/herladen.
- Single-instance tray-bediening, optioneel geïnstalleerd opstarten, 34 talen en vier thema's.
- Scheid de normale acties Quit en **Quit + RTSS**.

<a id="compatibility"></a>
## Compatibiliteit

| Vereiste | Details |
| --- | --- |
| Systeem | Windows 10/11 x64 |
| Looptijd | [.NET Framework 4.8](https://dotnet.microsoft.com/en-us/download/dotnet-framework/net48), indien nodig afzonderlijk geïnstalleerd |
| Vereiste software | RTSS met `RTSS.exe`, een bijpassende `Profiles`-directory en compatibele profiel-/herlaadondersteuning |
| GPU | RTSS-compatibiliteit bepaalt de limiter; deze profielmanager vereist geen specifieke RTX-generatie |
| Machtigingen | Huidige applicatie vraagt om beheerderstoegang; de geselecteerde RTSS-profielmap moet toegankelijk zijn |
| Spellen | Afhankelijk van RTSS hooking-ondersteuning en de beperkingen van elk spel; geen anti-cheat garantie |

Er is geen specifieke RTSS-minimumversie gecertificeerd voor elke functie door deze hub-audit. Gebruik de officiële huidige distributie en rapporteer de exacte versie als een profielsleutel/herladen niet werkt. Geïnstalleerd maar gestopt RTSS slaagt voor de installatiecontrole; voor daadwerkelijke begrenzing moet deze dan worden gestart.

<a id="installation"></a>
## Installatie

1. **[Download en installeer RTSS van Guru3D](https://www.guru3d.com/download/rtss-rivatuner-statistics-server-download/).**
2. Open [NVRasterPulse-downloads](../docs/downloads.md#nvrasterpulse) en controleer de beschikbaarheid van de release.
3. Download `NVRasterPulse-0.2-win-x64-Setup.exe` of `NVRasterPulse-0.2-win-x64-portable.zip`, plus de mededelingen/controlesommen.
4. Vergelijk SHA-256. Voer Setup uit of pak de volledige draagbare ZIP uit naar een beschrijfbare lokale map.
5. Open `NVRasterPulse.exe`. Als RTSS ontbreekt, gebruik dan **Download RTSS**, installeer het en vervolgens **Controleer nogmaals**, of selecteer `RTSS.exe` handmatig.
6. Start RTSS met de normale snelkoppeling of met de RTSS-knop van NVRasterPulse als deze gestopt is.

Als u de optionele herinnering uitschakelt, wordt de controle op de vereisten niet overgeslagen. Een stil opstarten van de Windows-lade wacht tot het hoofdvenster wordt geopend voordat deze controle wordt weergegeven. Tijdens de installatie wordt alleen NVRasterPulse geïnstalleerd. De EXE's zijn niet ondertekend.

<a id="usage"></a>
## Gebruik

1. Selecteer de beoogde actieve applicatie of blader naar de game-EXE.
2. Voer een limiet in tussen 1 en 1000 FPS, inclusief een gedeeltelijke waarde indien nodig.
3. Bewaar en controleer het gerapporteerde resultaat. NVRasterPulse werkt het RTSS-profiel van dat uitvoerbare bestand bij en vraagt ​​om herladen.
4. Bevestig dat RTSS actief is en verifieer het gedrag in het beoogde spel.

Profielen worden gecodeerd met **uitvoerbare naam**, zoals `Game.exe.cfg`. Twee verschillende mappen met `Game.exe` delen hetzelfde RTSS-profiel; het opslaan van het volledige pad verwijdert deze botsing niet.

Bij het opslaan wordt gebruik gemaakt van Front Edge Sync en actief wachten. Actief wachten kan het gebruik van CPU verhogen. De alternatieve `LimitTime`-velden worden geneutraliseerd. Bestaande opmerkingen, overlay-instellingen en `EnableHooking=0` blijven behouden. Het RTSS Global-profiel is niet gewijzigd.

Gebruik de prullenbakactie om de limiteroverschrijvingen van NVRasterPulse te verwijderen. Het verwijdert niet het hele RTSS-profiel. Een limiet die is overgenomen van RTSS Global of een andere tool kan daarna nog steeds van toepassing zijn.

**Sluiten en afsluiten:** het hoofdvenster kan zich in de lade verbergen. Normaal **Afsluiten** zorgt ervoor dat RTSS actief blijft en de opgeslagen limieten intact blijven. **Quit + RTSS** vraagt ​​om een ​​normale afsluiting van het overeenkomende RTSS-proces in de huidige sessie, wacht maximaal acht seconden en forceert het niet. In beide gevallen blijven de opgeslagen limieten behouden.

Taal en thema worden geselecteerd in de app. Opstarten bij Windows aanmelden is optioneel en bedoeld voor een geïnstalleerd exemplaar. De informatieknop legt veelvoorkomende handelingen uit.

<a id="diagnostics-and-profile-tools"></a>
## Diagnostische en profieltools

Open het actiemenu voor de extra tools. Ze behouden RTSS Global, overlay-instellingen en uitsluitingen.

**Diagnostiek:** inspecteer lokale/effectieve limieten, gestopt RTSS, een ontbrekend uitvoerbaar bestand, geen gedetecteerd venster, uitgeschakelde hooking, overerving, gepauzeerde limieten, concurrerende instellingen en dubbele namen van uitvoerbare bestanden. Deze alleen-lezen-controle beschrijft de configuratie; het bewijst niet dat een game verslaafd is aan RTSS of de FPS meet.

**FPS helper:** selecteer het display en declareer zelf VRR/G-Sync, V-Sync, Reflex en Frame Generation. De afgeronde vernieuwingsfrequentie is afkomstig van Windows. Als Reflex of Frame Generation actief of onbekend is, wordt er geen automatische limiet aangeboden. Voor VRR met V-Sync aan en Reflex/FG uit trekt de heuristiek ten minste 3 FPS af, oftewel ongeveer 2% van de vernieuwingsfrequentie. Dit is geen gemeten optimaal. Door de suggestie toe te passen wordt het concept ingevuld; **Opslaan** blijft een aparte actie.

**Pauzeer en hervat:** schort de limiet van het geselecteerde programma op en herstelt vervolgens de vorige limitervelden. Tegenstrijdige wijzigingen door een ander hulpmiddel voorkomen een dubbelzinnig cv. Als u een item verbergt, wordt de limiet ervan niet gepauzeerd.

**Ongedaan maken:** herstelt de laatste wijziging in de zes beheerde limitervelden voor dat programma. Er is één niveau; hierdoor wordt RTSS niet volledig hersteld. Tegenstrijdige externe wijzigingen worden geweigerd. Bestandsback-ups blijven gescheiden.

**Profielen delen:** geselecteerde profielen exporteren naar een `.nvrp`-bestand. Importeren toont een voorbeeld en laat bestaande limieten standaard uitgeschakeld. Het bestand bevat alleen uitvoerbare namen, limieten en statussen, zonder absolute paden of scripts. Controleer uw selectie en solliciteer. Door een I/O-fout kunnen sommige profielen al zijn toegepast; het resultaat identificeert ze en elk behoudt zijn ongedaan maken. Identieke uitvoerbare namen adresseren nog steeds hetzelfde RTSS-profiel.

**Favorieten en verborgen items:** nuttige programma's eerst vastzetten, ongewenste items verbergen en ze herstellen in het speciale dialoogvenster. Deze keuzes blijven bestaan. Een gesloten favoriet verschijnt niet als actieve applicatie.

<a id="screenshots"></a>
## Schermafbeeldingen

![NVRasterPulse voorbeeld van het hoofdvenster](../../../../assets/screenshots/nvrasterpulse-0.1-preview.png)

Bestaande Franse 0.1 UI-weergave met voorbeeldnamen van uitvoerbare bestanden en een 176 FPS-waarde. RTSS wordt gestopt weergegeven; dit is een interface-illustratie, geen lopende limiter- of latentiemeting. [Herkomst afbeelding](../assets/README.md).

<a id="update-and-uninstall"></a>
## Updaten en verwijderen

Sluit NVRasterPulse af, download en verifieer de nieuwe versie, voer vervolgens de installatie uit of pak de draagbare versie uit naar een nieuwe map. Behoud instellingen en RTSS-back-ups. RTSS-updates zijn afzonderlijk en komen van Guru3D.

Om een geïnstalleerd exemplaar te verwijderen, gebruikt u Windows **Installed apps**. Voor draagbaar: sluit af en verwijder de uitgepakte map wanneer uw back-ups veilig zijn. Opgeslagen RTSS-limieten worden niet verwijderd door NVRasterPulse te verwijderen: verwijder eerst de bedoelde limiter-overschrijvingen. RTSS heeft een eigen verwijderprogramma.

Lokale staat: `%LOCALAPPDATA%\NVRasterPulse`. Automatische RTSS-back-ups: `%LOCALAPPDATA%\NVRasterPulse\Backups\RTSS`. Mogelijk wordt een oudere `%LOCALAPPDATA%\RTSSProfileBridge`-locatie gelezen voor migratie. Deze bestanden kunnen persoonlijke uitvoerbare paden bevatten en mogen niet openbaar worden geplaatst.

<a id="known-limitations"></a>
## Bekende beperkingen

- RTSS voert de cap uit. Een opgeslagen waarde of een succesvol herlaadverzoek is geen gemeten frametijdresultaat.
- Uitvoerbare bestanden met dezelfde naam delen een profiel.
- Een andere globale/per-game limiter kan het resultaat beïnvloeden; Als u de lokale overschrijving uitschakelt, wordt een overgenomen limiet niet verwijderd.
- Een opzettelijk uitgeschakelde RTSS-hook blijft uitgeschakeld.
- Actief wachten heeft een CPU/vermogen-afweging.
- Geen universeel spel, anti-cheat of end-to-end latentievalidatie.
- De eerdere experimentele onafhankelijke limiter-engine is niet samengesteld of verzonden.
- Automatische back-ups impliceren niet dat er met één klik een volledige back-up-herstelinterface nodig is.

<a id="troubleshooting"></a>
## Problemen oplossen

| Symptoom | Actie |
| --- | --- |
| RTSS-vereiste blijft open | Selecteer de daadwerkelijke `RTSS.exe` en de overeenkomende map Profielen en controleer vervolgens opnieuw. |
| Limiet opgeslagen maar geen effect | Start RTSS; verifieer de juiste game-EXE/profiel, hook-machtigingen en andere limiters. |
| Opslaan mislukt | Controleer de maprechten en bewaar de weergegeven fout/back-up. |
| Limiet blijft na verwijdering bestaan | Inspecteer RTSS Global en andere tools; de prullenbakactie verwijdert alleen lokale limiteroverschrijvingen. |
| Twee games krijgen dezelfde limiet | Controleer of de uitvoerbare bestandsnamen identiek zijn. |
| Afsluiten + RTSS laat RTSS open | Sluit RTSS normaal zelf af; dit commando vermijdt opzettelijk gedwongen beëindiging. |

Als u handmatig een RTSS-back-up herstelt, sluit dan eerst RTSS en bewaar het huidige profiel voordat u het vervangt door de beoogde back-up. Dit kan niet-gerelateerde profielbewerkingen overschrijven; controleer het bestand en de datum. [Gedeelde steun](../docs/support.md).

<a id="faq"></a>
## Veelgestelde vragen

**Heb ik ook MSI Afterburner nodig?** NVRasterPulse vereist RTSS; het is niet afhankelijk van de Afterburner-applicatie. Volg de installatieopties van de RTSS-distributeur.

**Kan ik dit gebruiken zonder dat RTSS actief is?** U kunt profielen beheren zodra een installatie is gedetecteerd, maar RTSS moet worden uitgevoerd vanwege beperking.

**Wordt bij het afsluiten of verwijderen van de installatie de kap verwijderd?** Nee. Verwijder de gewenste limiter-overschrijvingen expliciet voordat u NVRasterPulse verwijdert.

**Is het een fork of RTSS?** Nee. Het is een onafhankelijke profielbeheerder; er is geen RTSS-bron of uitvoerbaar bestand opgenomen.

<a id="upstream-modifications-and-credits"></a>
## Upstream, wijzigingen en credits

De ontwikkelingsrepository is afkomstig van [Orbmu2k's NVIDIA Profile Inspector](https://github.com/Orbmu2k/nvidiaProfileInspector). De MIT-paletten/UI-bronnen worden gecrediteerd. De profielbeheerservices, breukcodering, back-ups, RTSS-herlaadbrug, ladegedrag, vereistengids, talen en applicatiespecifiek pictogram zijn ontwikkeld/aangepast door 禅堂 Zendo (RevoluSound Team).

RTSS is ontwikkeld door **Unwinder** en afzonderlijk gedistribueerd via Guru3D. NVRasterPulse roept `UpdateProfiles` aan vanaf de geselecteerde geïnstalleerde hook-DLL; geen RTSS SDK of hook-binair bestand wordt opnieuw gedistribueerd. Het installatieprogramma gebruikt ongewijzigde Inno Setup 7.1.0 met aangepaste scripts/vertalingen en een project-bootstrap.

[Volledige herkomst](../docs/provenance.md) · [Tafel van derden](../THIRD_PARTY_NOTICES.md)

<a id="license"></a>
## Licentie

Het pakket distribueert NVRasterPulse expliciet onder de meegeleverde [MIT-licentie](../../../../NVRasterPulse/LICENSE), met behoud van Copyright (c) 2016 Orbmu2k. De applicatiebron wordt privé onderhouden; MIT vereist geen publicatie van gewijzigde broncode. RTSS en Windows/.NET blijven onder hun eigen voorwaarden vallen. [Volledige mededelingen](LICENSES/README.md).

Onafhankelijk van NVIDIA Corporation, MSI en RTSS; niet door hen gesponsord of officieel goedgekeurd. Productnamen blijven de handelsmerken van hun eigenaren.
