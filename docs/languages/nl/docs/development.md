<!-- nv-language-navigation:start -->
🌐 [English](../../../development.md) | [Français](../../../development.fr.md) · [NV Laboratory](../README.md)

<details>
<summary>🌐 Language · 34</summary>

[العربية](../../ar/docs/development.md) · [বাংলা](../../bn/docs/development.md) · [简体中文](../../zh/docs/development.md) · [Čeština](../../cs/docs/development.md) · [Dansk](../../da/docs/development.md) · **Nederlands** · [English](../../../development.md) · [Filipino](../../fil/docs/development.md) · [Suomi](../../fi/docs/development.md) · [Français](../../../development.fr.md) · [Deutsch](../../de/docs/development.md) · [Ελληνικά](../../el/docs/development.md) · [हिन्दी](../../hi/docs/development.md) · [Magyar](../../hu/docs/development.md) · [Bahasa Indonesia](../../id/docs/development.md) · [Italiano](../../it/docs/development.md) · [日本語](../../ja/docs/development.md) · [한국어](../../ko/docs/development.md) · [मराठी](../../mr/docs/development.md) · [فارسی](../../fa/docs/development.md) · [Polski](../../pl/docs/development.md) · [Português](../../pt/docs/development.md) · [ਪੰਜਾਬੀ](../../pa/docs/development.md) · [Română](../../ro/docs/development.md) · [Русский](../../ru/docs/development.md) · [Español](../../es/docs/development.md) · [Kiswahili](../../sw/docs/development.md) · [Svenska](../../sv/docs/development.md) · [தமிழ்](../../ta/docs/development.md) · [ไทย](../../th/docs/development.md) · [Türkçe](../../tr/docs/development.md) · [Українська](../../uk/docs/development.md) · [اردو](../../ur/docs/development.md) · [Tiếng Việt](../../vi/docs/development.md)

[Translation policy](../../README.md)

</details>
<!-- nv-language-navigation:end -->

<!-- nv-translation-notice:start -->
> Machineondersteunde vertaling uit het Engels. Technische namen, commando's, URL's en originele juridische teksten blijven behouden. Recensie door native speakers is welkom; raadpleeg de Engelse referentie als de formulering onduidelijk is.
<!-- nv-translation-notice:end -->

<a id="repository-architecture-and-maintenance"></a>
# Architectuur en onderhoud van opslagplaatsen

NV Laboratory is een openbare **documentatie- en binaire distributiehub**. Het bevat geen applicatiebron. De vier projecten behouden afzonderlijke buildbomen, versies, identiteiten en release-items. Hun persoonlijke ontwikkelingsgeschiedenis wordt niet geïmporteerd in deze Git-repository.

<a id="layout"></a>
## Indeling

| Locatie | Doel |
| --- | --- |
| README.md / README.fr.md | Engels/Franse toegangspunten |
| Vier projectmappen | Volledige handleidingen en toepasselijke originele mededelingen |
| documenten | Downloads, compatibiliteit, herkomst, ontwikkeling en releaseprocedure |
| docs/releases.json | Geauditeerde metadata, groottes en hashes van kandidaten/releases |
| documenten/herkomst | Bestand/hash-vergelijkingen; geen applicatiecode |
| licenties | Volledige teksten van derden en credits voor installateurvertalers gedeeld |
| activa | Bestaande beoordeelde UI-voorbeelden en hun herkomst |
| .github | Uitgifteformulieren en alleen-lezen documentatievalidatie |
| gereedschap/validate_repository.py | Controles op publicatiegrenzen en koppelingen in de standaardbibliotheek |

Engels blijft de standaard GitHub README. Bestaande aangrenzende `.fr.md`-links blijven geldig. Aanvullende vertalingen weerspiegelen de documentatie onder `docs/languages/<code>`; de taalkiezer behoudt dezelfde pagina bij het wisselen van taal. De catalogus `docs/languages/catalog.json` registreert alle 34 talen en bronvingerafdrukken. GitHub selecteert niet automatisch een README per browsertaal. Zie de [taalindex en vertaalbeleid](../../README.md).

<a id="application-technologies"></a>
## Applicatietechnologieën

| Programma | Privé technologie | Distributie |
| --- | --- | --- |
| NVPI fork | C#, WPF, .NET Framework 4.8, NVAPI/Windows interoperabiliteit | Complete draagbare map en losse Inno Setup |
| NVDriverForge | C#, WPF, .NET 8; native C++-bootstrap; 7-Zip-proces | Op zichzelf staande draagbare EXE en installatie |
| NVMFG Unlock40 | C#/WPF .NET 8, Framework 4.8-helpers, C++20/MASM/MinHook-engine | Draagbare boom en opstelling |
| NVRasterPulse | C#/WPF-framework 4.8; RTSS profiel/herladen-integratie; inheemse bootstrap | Draagbare boom en opstelling |

Deze openbare kassa kan de applicaties niet opnieuw opbouwen. Automatische “Source code”-archieven zijn hub-snapshots. Upstream-bronlinks vertegenwoordigen niet de exacte privé-gemodificeerde bron. Het openbare CI valideert alleen deze repository.

<a id="local-checks"></a>
## Lokale controles

Vanuit de root van de repository:

```text
python tools/validate_repository.py
```

Python 3.10 of nieuwer is voldoende. De controle leest bestanden, lokale Markdown-links, vereiste mededelingen/RTSS-links, release-metagegevens en publicatiegrenzen. Het voert de software niet uit, installeert geen afhankelijkheden en maakt geen contact met een netwerk.

De GitHub-workflow voert dezelfde controle uit met toestemming voor alleen-lezen inhoud bij push-, pull-verzoeken of handmatige verzending. Checkout is vastgemaakt aan een gecontroleerde commit en bewaart de inloggegevens niet. Er is geen release- of implementatietaak geconfigureerd.

<a id="maintain-the-boundary"></a>
## Handhaaf de grens

Werk de Engelse referentie, Franse gidsen en betrokken vertalingen samen bij. Houd inhoudelijke wijzigingen gescheiden van vergelijkingen met alleen opmaak. Registreer daadwerkelijke kandidaat-hashes, upstream commit-referenties en licenties; leid nooit een licentie af op basis van de populariteit van een project.

Gebruik een nieuwe versie. Geef middelen vrij en controleer gewijzigde binaire bestanden, archieven en ingesloten mededelingen opnieuw. Bewaar privéback-ups buiten deze repository. Gebruik geen openbare workflow om privé-applicatiebronnen of lokale buildmappen te importeren.

Tests die geschikt zijn voor een functionele applicatiewijziging die in het privéproject wordt uitgevoerd. Voer geen stuurprogramma-installatieprogramma's opnieuw uit en schrijf geen echte profielen voor een documentatie-update. [Handmatige vrijgaveprocedure](releasing.md).
