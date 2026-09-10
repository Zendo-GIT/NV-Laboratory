<!-- nv-language-navigation:start -->
🌐 [English](../../../CONTRIBUTING.md) | [Français](../fr/CONTRIBUTING.md) · [NV Laboratory](README.md)

<details>
<summary>🌐 Language · 34</summary>

[العربية](../ar/CONTRIBUTING.md) · [বাংলা](../bn/CONTRIBUTING.md) · [简体中文](../zh/CONTRIBUTING.md) · [Čeština](../cs/CONTRIBUTING.md) · [Dansk](../da/CONTRIBUTING.md) · **Nederlands** · [English](../../../CONTRIBUTING.md) · [Filipino](../fil/CONTRIBUTING.md) · [Suomi](../fi/CONTRIBUTING.md) · [Français](../fr/CONTRIBUTING.md) · [Deutsch](../de/CONTRIBUTING.md) · [Ελληνικά](../el/CONTRIBUTING.md) · [हिन्दी](../hi/CONTRIBUTING.md) · [Magyar](../hu/CONTRIBUTING.md) · [Bahasa Indonesia](../id/CONTRIBUTING.md) · [Italiano](../it/CONTRIBUTING.md) · [日本語](../ja/CONTRIBUTING.md) · [한국어](../ko/CONTRIBUTING.md) · [मराठी](../mr/CONTRIBUTING.md) · [فارسی](../fa/CONTRIBUTING.md) · [Polski](../pl/CONTRIBUTING.md) · [Português](../pt/CONTRIBUTING.md) · [ਪੰਜਾਬੀ](../pa/CONTRIBUTING.md) · [Română](../ro/CONTRIBUTING.md) · [Русский](../ru/CONTRIBUTING.md) · [Español](../es/CONTRIBUTING.md) · [Kiswahili](../sw/CONTRIBUTING.md) · [Svenska](../sv/CONTRIBUTING.md) · [தமிழ்](../ta/CONTRIBUTING.md) · [ไทย](../th/CONTRIBUTING.md) · [Türkçe](../tr/CONTRIBUTING.md) · [Українська](../uk/CONTRIBUTING.md) · [اردو](../ur/CONTRIBUTING.md) · [Tiếng Việt](../vi/CONTRIBUTING.md)

[Translation policy](../README.md)

</details>
<!-- nv-language-navigation:end -->

<!-- nv-translation-notice:start -->
> Machineondersteunde vertaling uit het Engels. Technische namen, commando's, URL's en originele juridische teksten blijven behouden. Recensie door native speakers is welkom; raadpleeg de Engelse referentie als de formulering onduidelijk is.
<!-- nv-translation-notice:end -->

<a id="contributing"></a>
# Bijdragen

NV Laboratory wordt onderhouden door 禅堂 Zendo (RevoluSound Team). De beheerder bepaalt wat wordt geaccepteerd en vrijgegeven. Het openen van een Issue of Pull Request betekent niet dat een bijdrage wordt geaccepteerd of geautoriseerd voor distributie.

Gebruik het bug- of featureformulier en identificeer het programma/de versie. Zoek eerst naar bestaande problemen. Bespreek substantiële wijzigingen voordat u een grote bijdrage voorbereidt. Voor veiligheidskwesties volgt u [SECURITY.md](SECURITY.md).

Deze openbare hub bevat documentatie, mededelingen, release-metagegevens en repository-validatie. Applicatiebron en tests worden privé onderhouden. Dien geen gedecompileerde code, privébron, inloggegevens, gebruikersprofielen of uitvoerbare payloads in.

Documentatie-PR's moeten de 34 taaltegenhangers en navigatie op één lijn houden, opdracht-/bestands-/productnamen behouden en feitelijk gedrag beschrijven. Nieuwe screenshots moeten van jou zijn, versie-geïdentificeerd en vrij van persoonlijke gegevens; synthetische gegevens moeten worden gelabeld. Geef de herkomst en toestemming op voor elk nieuw item van derden.

Gebruik UTF-8, LF, leesbare Markdown en kleine gerichte wijzigingen. De Python-validator gebruikt alleen de standaardbibliotheek. Pas de bestaande stijl aan, vermijd onnodige afhankelijkheden en voer het volgende uit:

```text
python tools/validate_repository.py
```

Voor wijzigingen in de release-metagegevens moet u de exacte versie/tag, bestandsgroottes en SHA-256 uit de gecontroleerde binaire bestanden opnemen, en de downloadpagina's op één lijn houden. Voor applicatiewijzigingen zijn privé-builds/tests nodig die geschikt zijn voor het betreffende gedrag; een documentatiecontrole is geen applicatietest. Verzin nooit historische testresultaten of winsten.

Door origineel hubmateriaal bij te dragen, gaat u akkoord met de MIT-licentie in [LICENTIE](../../../LICENSE). Kennisgevingen van derden bijhouden en uw wijzigingen identificeren; vervangt geen upstream-licentie. Acceptatie en publicatie blijven beslissingen van de beheerder.
