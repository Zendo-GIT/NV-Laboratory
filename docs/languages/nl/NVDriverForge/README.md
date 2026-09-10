<!-- nv-language-navigation:start -->
🌐 [English](../../../../NVDriverForge/README.md) | [Français](../../../../NVDriverForge/README.fr.md) · [NV Laboratory](../README.md)

<details>
<summary>🌐 Language · 34</summary>

[العربية](../../ar/NVDriverForge/README.md) · [বাংলা](../../bn/NVDriverForge/README.md) · [简体中文](../../zh/NVDriverForge/README.md) · [Čeština](../../cs/NVDriverForge/README.md) · [Dansk](../../da/NVDriverForge/README.md) · **Nederlands** · [English](../../../../NVDriverForge/README.md) · [Filipino](../../fil/NVDriverForge/README.md) · [Suomi](../../fi/NVDriverForge/README.md) · [Français](../../../../NVDriverForge/README.fr.md) · [Deutsch](../../de/NVDriverForge/README.md) · [Ελληνικά](../../el/NVDriverForge/README.md) · [हिन्दी](../../hi/NVDriverForge/README.md) · [Magyar](../../hu/NVDriverForge/README.md) · [Bahasa Indonesia](../../id/NVDriverForge/README.md) · [Italiano](../../it/NVDriverForge/README.md) · [日本語](../../ja/NVDriverForge/README.md) · [한국어](../../ko/NVDriverForge/README.md) · [मराठी](../../mr/NVDriverForge/README.md) · [فارسی](../../fa/NVDriverForge/README.md) · [Polski](../../pl/NVDriverForge/README.md) · [Português](../../pt/NVDriverForge/README.md) · [ਪੰਜਾਬੀ](../../pa/NVDriverForge/README.md) · [Română](../../ro/NVDriverForge/README.md) · [Русский](../../ru/NVDriverForge/README.md) · [Español](../../es/NVDriverForge/README.md) · [Kiswahili](../../sw/NVDriverForge/README.md) · [Svenska](../../sv/NVDriverForge/README.md) · [தமிழ்](../../ta/NVDriverForge/README.md) · [ไทย](../../th/NVDriverForge/README.md) · [Türkçe](../../tr/NVDriverForge/README.md) · [Українська](../../uk/NVDriverForge/README.md) · [اردو](../../ur/NVDriverForge/README.md) · [Tiếng Việt](../../vi/NVDriverForge/README.md)

[Translation policy](../../README.md)

</details>
<!-- nv-language-navigation:end -->

<!-- nv-translation-notice:start -->
> Machineondersteunde vertaling uit het Engels. Technische namen, commando's, URL's en originele juridische teksten blijven behouden. Recensie door native speakers is welkom; raadpleeg de Engelse referentie als de formulering onduidelijk is.
<!-- nv-translation-notice:end -->

<a id="nvdriverforge"></a>
# NVDriverForge

**Bereid een NVIDIA-stuurprogramma-installatie voor met duidelijke componentkeuzes en optionele instellingen.**

[Download 0.1.3 en status](../docs/downloads.md#nvdriverforge) · [Installatie](#installation) · [Kredieten](#credits-and-upstream) · [Licentie](../../../../NVDriverForge/LICENSE)

<a id="overview-and-purpose"></a>
## Overzicht en doel

NVDriverForge begeleidt u door een origineel NVIDIA-stuurprogrammapakket: kies het stuurprogramma, inspecteer de componenten, bekijk optionele aanpassingen en bevestig vervolgens de installatie. Het is bedoeld om deze keuzes begrijpelijk te maken en de installatie-, bevoorrechte bewerkingen en herstelinformatie bij elkaar te houden.

Het is een onafhankelijk ontwikkelde applicatie die gedeeltelijk is geïnspireerd op de workflow van NVCleanstall. Het omvat niet NVCleanstall en claimt geen volledige functiepariteit.

<a id="features"></a>
## Kenmerken

- NVIDIA Game Ready / Studio opzoeken en downloaden; optionele hotfix-detectie met handmatige terugval.
- Analyse van het originele pakket, hashes, NVIDIA-handtekeningen, manifesten en compatibele INF-vermeldingen.
- Componentselectie met afhankelijkheden en behoud van onbekende componenten.
- Versie 0.1.3 zorgt ervoor dat geselecteerde optionele NVIDIA-componenten kunnen worden overgeslagen en sluit alleen geverifieerde, niet-gecontroleerde componenten uit van detectie. Reeds bestaande of niet-toepasbare optionele runtimes worden niet langer geforceerd als kritische componenten.
- Duidelijke samenvattingen van installatiefouten en toegang tot gedetailleerde logboeken in alle 34 talen.
- Expliciete installatiebevestiging, beschermde staging en export van bestaande driver-store-pakketten.
- Optionele geavanceerde instellingen, met preflight-controles, journalen en conflictbewust herstel.
- Optionele **Custom NV**-voorinstelling met benoemde keuzes en uitleg, inclusief een afzonderlijke SILK-sterkteselectie en compatibiliteitscontroles.
- Optionele NVENC-patchdownloads van de exacte versie; broncommit en doelbytes worden gecontroleerd.
- Een aparte, optionele installatie van de Profile Inspector fork vanuit het scherm Tools.
- Optionele controles op updates voor geïnstalleerde gebruikers, 34 interfacetalen en vier thema's.

Beschikbare geavanceerde opties betreffen MPO, de DLSS-indicator, Ansel, NVIDIA audio-slaapstand, MSI, interruptbeleid/prioriteit, HDCP, opstarten van display-containers en een in aanmerking komende oudere telemetrieservice. Elk heeft zijn eigen voorwaarden en effecten; dit zijn geen universele prestatieverbeteringen.

<a id="compatibility"></a>
## Compatibiliteit

| Vereiste | Details |
| --- | --- |
| Systeem | Windows 10 build 19041 of nieuwer / Windows 11, x64 |
| GPU/stuurprogramma | Compatibel NVIDIA-pakket en gedetecteerde hardware; automatisch zoeken in de catalogus heeft voornamelijk betrekking op bekende GeForce-modellen |
| Looptijd | .NET 8 / WPF 8.0.31 inbegrepen in het voorbereide, op zichzelf staande pakket |
| Voorrechten | Normale UI/per-gebruiker-installatie; Installatie van stuurprogramma's en systeemwijzigingen vereisen beheerderstoegang |
| Netwerk | Vereist voor online NVIDIA-zoekopdrachten/downloads en expliciete upstream NVENC-verzoeken; er kan een lokaal origineel stuurprogramma worden geselecteerd |
| Inclusief gereedschap | Ongewijzigde 7-Zip 26.03, runtime-kennisgevingen, optionele MIT Profile Inspector-metgezel |
| Optionele metgezel | .NET Framework 4.8 voor de afzonderlijke Profile Inspector fork |

Er is geen willekeurige minimale driverversie die alle functies dekt. Multi-GPU-zoekopdracht moet overeenkomen met elke gedetecteerde GPU. Voor niet-ondersteunde/professionele modellen kan handmatige driverselectie nodig zijn. Het installatieprogramma van NVIDIA blijft de uiteindelijke hardware-/OS-autoriteit.

<a id="installation"></a>
## Installatie

1. Ga naar [downloads](../docs/downloads.md#nvdriverforge) en bevestig dat de release is gepubliceerd.
2. Kies `NVDriverForge-Setup.exe` voor installatie, of `NVDriverForge.exe` voor draagbaar gebruik.
3. Vergelijk SHA-256 met de `SHA256SUMS.txt` van de release.
4. Voer Setup uit voor een installatie per gebruiker en een standaard verwijderprogramma, of plaats de draagbare EXE in een beschrijfbare map en open deze.

De draagbare versie bevat de runtime en het optionele installatieprogramma. Als u NVDriverForge installeert, wordt er geen GPU-stuurprogramma geïnstalleerd. De EXE's zijn momenteel niet ondertekend.

<a id="usage"></a>
## Gebruik

1. **Stuurprogramma:** downloaden van NVIDIA of selecteer een originele NVIDIA-installatieprogramma-EXE. Laat de analyse eindigen.
2. **Componenten:** bekijk beschrijvingen en vereiste afhankelijkheden. Onbekende componenten blijven behouden.
3. **Tweaks:** laat ongewenste opties ongewijzigd. Lees de effecten en afwegingen voordat u iets selecteert.
4. **Beoordeling:** controleer de exacte driver, componenten en optionele handelingen en bevestig vervolgens de installatie.
5. Accepteer UAC alleen voor de door u gekozen bewerking. Bewaar de herstelinstructies van de beveiligde taak.
6. Als het nieuwe stuurprogramma opnieuw moet worden opgestart, volgt u de gerapporteerde status. Uitgestelde bewerkingen vereisen een expliciete hervatting na die herstart.

Custom NV start ongewijzigd. Kies individueel benoemde waarden of bekijk de meegeleverde voorinstelling en de uitsluitingen ervan. De twee informatieve interne velden zijn niet onafhankelijk geschreven. Instellingen worden alleen toegepast in de geverifieerde workflow voor nieuwe stuurprogramma's, nooit door een voorbeeld te openen. Het installeren van de aparte NVPI-editor is niet vereist.

Optioneel NVENC-werk downloadt compatibele gegevens van een vastgezette keylase-commit. Het wijzigt twee driver-DLL's en maakt hun handtekeningen ongeldig; het kan worden geweigerd door Windows, encoders, DRM of anti-cheat. Dergelijke gegevens of NVIDIA DLL zijn niet ingebed in NVDriverForge. [Herkomst- en licentielimieten](../docs/provenance.md).

Voorkeuren bepalen de taal, het thema en optionele controles op updates voor geïnstalleerde gebruikers. De draagbare versie maakt de geïnstalleerde achtergrondcontroletaak niet aan. Tools en herstel staan ​​los van de vier installatiestappen.

<a id="screenshots"></a>
## Schermafbeeldingen

![NVDriverForge voorbeeld van stuurprogrammapagina](../../../../assets/screenshots/nvdriverforge-0.1.2-preview.png)

Bestaande 0.1.2 Franse UI-weergave met voorbeeldgegevens; bewaard als interfacevoorbeeld. Het weergegeven 699.99-stuurprogramma is een testopstelling en geen echte versie om te downloaden. [Herkomst afbeelding](../assets/README.md).

<a id="update-and-uninstall"></a>
## Updaten en verwijderen

Sluit NVDriverForge, verkrijg het volgende officiële pakket en verifieer de hash. Gebruik dezelfde Setup-identiteit voor een geïnstalleerde update; vervang een gesloten draagbare EXE door de nieuwe. Behoud instellingen en beveiligde taken.

Uninstall van Windows **Installed apps**. Het verwijdert de app en de updatetaak, niet het NVIDIA-stuurprogramma. Instellingen, logs en back-ups blijven behouden. Indien gewenst kunt u de geavanceerde/NVENC-wijzigingen herstellen via de gedocumenteerde herstelstroom **voordat** u de app verwijdert. Herstel weigert conflicterende wijzigingen van een andere tool.

Lokale gegevens staan onder `%LOCALAPPDATA%\NVDriverForge`; beschermde banen en chauffeursexports vallen onder `%PROGRAMDATA%\NVDriverForge\Jobs`. Draagbaar gebruik creëert ook lokale gegevens. Een export van een driverstore is geen systeemimage of een volledige profielback-up.

<a id="known-limitations"></a>
## Bekende beperkingen

- Geen hardwaretoevoegingen/INF-bewerking, geregenereerde NVIDIA-handtekeningen, anti-cheat-compatibel ontslag of automatische aanvaarding van niet-ondertekende waarschuwingen.
- Geen volledige verwijdering van telemetrie/advertenties, export van kleine pakketten of automatisch volledig terugdraaien naar het vorige stuurprogramma.
- Installatie van stuurprogramma's, opstartherstel en optionele profielschrijfbewerkingen zijn door de hub-audit niet volledig gevalideerd op echte machines.
- Het teruglezen van het register is geen bewijs van daadwerkelijke HDCP-, prestatie- of latentie-effecten.
- Handtekeningcontroles maken gebruik van lokaal beschikbare Windows-vertrouwen; online herroeping wordt niet uitgevoerd.
- Er zijn 34 talen aanwezig, maar de volledige tests van de moedertaalspreker/toegankelijkheid blijven onvolledig.

<a id="troubleshooting"></a>
## Problemen oplossen

| Symptoom | Actie |
| --- | --- |
| Online catalogus niet beschikbaar | Selecteer een origineel pakket uit [NVIDIA-stuurprogramma downloaden](https://www.nvidia.com/en-us/drivers/). Vervang het model niet door een naburig GPU-model. |
| Hotfix-zoekopdracht niet beschikbaar | Gebruik [NVIDIA's Game Ready-stuurprogrammaforum](https://www.nvidia.com/en-us/geforce/forums/game-ready-drivers/13/) en verifieer het daadwerkelijke pakket. |
| NVIDIA-installatie mislukt | Lees het storingsoverzicht en open de gedetailleerde logboeken. Optionele componenten die al actueel of niet van toepassing zijn, kunnen worden overgeslagen in 0.1.3. Mislukte installaties veroorzaken geen optionele aanpassingen of een succes-/herstartstroom. |
| Handtekening/hash/back-up mislukt | Stop die installatie en behoud de fout; verkrijg het originele pakket opnieuw als het beschadigd is. |
| Optie niet beschikbaar | Lees de reden van de hardware, component of doeldriver; laat het onveranderd. |
| Opnieuw opstarten of taak is nog in behandeling | Gebruik de herstelinstructies en het expliciete cv van de taak; wis het dagboek niet. |
| Herstel conflicten | Een andere status wijkt af van de geregistreerde transactie. Bewaar het en vraag om hulp in plaats van een herstel af te dwingen. |

Vermeld voor rapporten de geselecteerde toolversie, Windows, GPU, driver en reproduceerbare stappen; paden en persoonlijke gegevens uit logboeken redigeren. [Ondersteuning](../docs/support.md).

<a id="faq"></a>
## Veelgestelde vragen

**Installeert Setup een grafisch stuurprogramma?** Nee. Hiervoor is het afzonderlijke analyse-, beoordelings-, bevestigings- en verhoogde installatieproces van de applicatie vereist.

**Heb ik NVCleanstall of NVPI nodig?** Nee. NVCleanstall is alleen inspiratie. De Profile Inspector-metgezel is een onafhankelijke optionele editor.

**Maakt dit elk NVIDIA-stuurprogramma kleiner of sneller?** Nee. Geselecteerde componenten en vereisten bepalen wat er kan veranderen; er wordt geen gemeten winst beloofd.

**Waar zijn de bronnen?** Applicatiespecifieke bron- en privétests worden afzonderlijk onderhouden. Deze hub biedt documentatie, binaire bestanden en bronlinks van derden die vereist zijn voor attributie/licenties.

<a id="credits-and-upstream"></a>
## Credits en stroomopwaarts

Originele applicatie, workflow, transacties, lokalisatie, bootstrap en aanpassingen: 禅堂 Zendo (RevoluSound Team).

- [NVCleanstall / TechPowerUp](https://www.techpowerup.com/download/techpowerup-nvcleanstall/): workflow-inspiratie; geen bron of binair geïmporteerd.
- [NVIDIA Profile Inspector / Orbmu2k](https://github.com/Orbmu2k/nvidiaProfileInspector): MIT-thema's, uitgebreide NVAPI-interfacereferentie en afzonderlijk verpakte fork.
- [7-Zip / Igor Pavlov](https://www.7-zip.org/): ongewijzigde extractietools.
- [Microsoft .NET](https://github.com/dotnet/runtime) en [WPF](https://github.com/dotnet/wpf): gebundelde runtime.
- [Inno Setup](https://jrsoftware.org/isinfo.php): originele installatie-engine en gecrediteerde vertalingen.
- [keylase/nvidia-patch](https://github.com/keylase/nvidia-patch): externe optionele NVENC-gegevensbron; herverdelingsvergunning niet vastgesteld.
- [NVIDIA](https://www.nvidia.com/en-us/drivers/): downloads van externe stuurprogramma's en geïnstalleerde NVAPI/NVML-bibliotheken.

[Volledige componententabel](../THIRD_PARTY_NOTICES.md) · [Wijzigingen en herkomst](../docs/provenance.md)

<a id="license"></a>
## Licentie

[Bestaande toestemming voor binaire distributie](../../../../NVDriverForge/LICENSE) staat het gebruik en delen toe van ongewijzigde officiële uitvoerbare bestanden met hun kennisgevingen. Applicatiespecifieke bronrechten zijn voorbehouden. Het beperkt de rechten die worden verleend door de afzonderlijke licenties van derden niet. [Volledige mededelingen](LICENSES/README.md).

Onafhankelijk van NVIDIA Corporation, TechPowerUp en keylase; niet door hen gesponsord of officieel goedgekeurd. Productnamen blijven de handelsmerken van hun eigenaren.
