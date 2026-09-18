<!-- nv-language-navigation:start -->
🌐 [English](../../../installation.md) | [Français](../../../installation.fr.md) · [NV Laboratory](../README.md)

<details>
<summary>🌐 Language · 34</summary>

[العربية](../../ar/docs/installation.md) · [বাংলা](../../bn/docs/installation.md) · [简体中文](../../zh/docs/installation.md) · [Čeština](../../cs/docs/installation.md) · [Dansk](../../da/docs/installation.md) · **Nederlands** · [English](../../../installation.md) · [Filipino](../../fil/docs/installation.md) · [Suomi](../../fi/docs/installation.md) · [Français](../../../installation.fr.md) · [Deutsch](../../de/docs/installation.md) · [Ελληνικά](../../el/docs/installation.md) · [हिन्दी](../../hi/docs/installation.md) · [Magyar](../../hu/docs/installation.md) · [Bahasa Indonesia](../../id/docs/installation.md) · [Italiano](../../it/docs/installation.md) · [日本語](../../ja/docs/installation.md) · [한국어](../../ko/docs/installation.md) · [मराठी](../../mr/docs/installation.md) · [فارسی](../../fa/docs/installation.md) · [Polski](../../pl/docs/installation.md) · [Português](../../pt/docs/installation.md) · [ਪੰਜਾਬੀ](../../pa/docs/installation.md) · [Română](../../ro/docs/installation.md) · [Русский](../../ru/docs/installation.md) · [Español](../../es/docs/installation.md) · [Kiswahili](../../sw/docs/installation.md) · [Svenska](../../sv/docs/installation.md) · [தமிழ்](../../ta/docs/installation.md) · [ไทย](../../th/docs/installation.md) · [Türkçe](../../tr/docs/installation.md) · [Українська](../../uk/docs/installation.md) · [اردو](../../ur/docs/installation.md) · [Tiếng Việt](../../vi/docs/installation.md)

[Translation policy](../../README.md)

</details>
<!-- nv-language-navigation:end -->

<!-- nv-translation-notice:start -->
> Machineondersteunde vertaling uit het Engels. Technische namen, commando's, URL's en originele juridische teksten blijven behouden. Recensie door native speakers is welkom; raadpleeg de Engelse referentie als de formulering onduidelijk is.
<!-- nv-translation-notice:end -->

<a id="installation-guide"></a>
# Installatiehandleiding

Begin met [Downloads](downloads.md), waarin de publicatiestatus en exacte itemnamen worden vastgelegd. Dit zijn afzonderlijke tools: installeer alleen de tools die je nodig hebt.

> **Voor NVRasterPulse installeert u [RTSS van Guru3D](https://www.guru3d.com/download/rtss-rivatuner-statistics-server-download/) voordat u Profielbeheer opent.**
> RTSS moet worden uitgevoerd om limieten toe te passen; het is niet opgenomen in NV Tools.

| Gereedschap | Geïnstalleerde editie | Draagbare editie | Belangrijkste voorwaarde |
| --- | --- | --- | --- |
| NVIDIA Profile Inspector – NV Tools Fork | NVPI-CustomNV-3.0.2.3-Setup-r2.exe | Pak de volledige NVPI ZIP uit | NVIDIA-stuurprogramma en .NET Framework 4.8 |
| NVDriverForge | NVDriverForge-Setup.exe | NVDriverForge.exe, runtime inbegrepen | Compatibel origineel NVIDIA driverpakket voor installatiebewerkingen |
| NVMFG Unlock40 | NVMFGUnlock40-0.2.3-Setup-x64.exe | Pak de volledige NVMFG ZIP uit, behoud submappen | RTX 40, bestaande DLSS FG, exacte provider en .NET Framework 4.8 helpers |
| NVRasterPulse | NVRasterPulse-0.2-win-x64-Setup.exe | Pak de volledige RP ZIP uit | RTSS en .NET Framework 4.8 |

<a id="download-verify-install"></a>
## Downloaden, verifiëren, installeren

1. Download op de gekozen gepubliceerde release het genoemde applicatie-item, merkt ZIP en SHA256SUMS.txt op.
2. Gebruik de [SHA-256 voorbeeld](downloads.md#sha-256), met de daadwerkelijk gedownloade bestandsnaam.
3. Volg voor de installatie het normale installatieprogramma. Voor draagbare ZIP: pak alles uit naar een nieuwe lokale beschrijfbare map; ren niet vanuit de ZIP.
4. Open de eigen EXE van de applicatie. Bewaar de bijbehorende licentie-/configuratie-/gegevensbestanden.
5. Lees de gebruiksinstructies van dat hulpprogramma voordat u instellingen of systeembewerkingen inschakelt.

De huidige binaire bestanden zijn niet ondertekend. Een overeenkomende hash bevestigt de verwachte bytes; het is geen beveiligings- of compatibiliteitscertificaat. Schakel de Windows-beveiligingsvoorzieningen niet uit alleen maar om een ​​waarschuwing te onderdrukken.

Het installeren van NVDF of de optionele NVPI-begeleider staat los van het installeren van een GPU-stuurprogramma. De NVPI-metgezel behoudt de bestaande interne installatienaam. De verhoogde RasterPulse-knop vereist een beschermde systeembrede installatie; andere RP-kopieën kunnen worden geopend via hun eigen snelkoppelingen.

NVMFG is experimenteel en heeft de [gedocumenteerde NVIDIA SDK licentiereserve](provenance.md). Er is geen NVIDIA-stuurprogramma, NGX-provider/-model of game Streamline-runtime inbegrepen. Geselecteerde SDK-downloads en game-updates zijn expliciet afzonderlijke bewerkingen.

<a id="language-and-updates"></a>
## Taal en updates

Gebruik de README's 34-talenkiezer voor documentatie. NVDF, NVMFG en RP hebben hun eigen 34-talige UI-instelling; NVPI behoudt zijn bestaande taalondersteuning. Sommige technische strings van het installatieprogramma vallen terug naar het Engels.

Behoud de installatie-identiteit van een tool tijdens het updaten. Sluit het eerst en bewaar back-ups. Voor NVMFG: sluit de betrokken games en los het lopende profielherstel op. Gebruik voor draagbare updates een nieuwe map in plaats van releases te combineren.

<a id="removing-a-tool"></a>
## Een hulpmiddel verwijderen

Het verwijderen van een applicatie betekent niet automatisch dat de instellingen ervan ongedaan worden gemaakt.

- **NVPI:** herstel indien nodig de beoogde profielen/weergave-instellingen voordat u deze verwijdert.
- **NVDF:** gebruik eerst herstel als u geavanceerde/NVENC-wijzigingen wilt herstellen. Uninstall verlaat het grafische stuurprogramma, de instellingen en back-ups.
- **NVMFG:** games afsluiten, de controller uitschakelen/afsluiten, NVIDIA-herstel oplossen en gewenste game-SDK-back-ups herstellen voordat deze worden verwijderd.
- **RP:** verwijder eerst de beoogde begrenzeroverschrijvingen. Uninstall wist de opgeslagen RTSS-capsules niet en verwijdert RTSS niet.

Bekijk elke [projectgids](../README.md#projects) voor de exacte gegevenslocaties en beperkingen, of [ondersteuning](support.md) als een herstelstap mislukt.
