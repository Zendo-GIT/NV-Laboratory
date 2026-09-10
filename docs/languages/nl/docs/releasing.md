<!-- nv-language-navigation:start -->
🌐 [English](../../../releasing.md) | [Français](../../../releasing.fr.md) · [NV Laboratory](../README.md)

<details>
<summary>🌐 Language · 34</summary>

[العربية](../../ar/docs/releasing.md) · [বাংলা](../../bn/docs/releasing.md) · [简体中文](../../zh/docs/releasing.md) · [Čeština](../../cs/docs/releasing.md) · [Dansk](../../da/docs/releasing.md) · **Nederlands** · [English](../../../releasing.md) · [Filipino](../../fil/docs/releasing.md) · [Suomi](../../fi/docs/releasing.md) · [Français](../../../releasing.fr.md) · [Deutsch](../../de/docs/releasing.md) · [Ελληνικά](../../el/docs/releasing.md) · [हिन्दी](../../hi/docs/releasing.md) · [Magyar](../../hu/docs/releasing.md) · [Bahasa Indonesia](../../id/docs/releasing.md) · [Italiano](../../it/docs/releasing.md) · [日本語](../../ja/docs/releasing.md) · [한국어](../../ko/docs/releasing.md) · [मराठी](../../mr/docs/releasing.md) · [فارسی](../../fa/docs/releasing.md) · [Polski](../../pl/docs/releasing.md) · [Português](../../pt/docs/releasing.md) · [ਪੰਜਾਬੀ](../../pa/docs/releasing.md) · [Română](../../ro/docs/releasing.md) · [Русский](../../ru/docs/releasing.md) · [Español](../../es/docs/releasing.md) · [Kiswahili](../../sw/docs/releasing.md) · [Svenska](../../sv/docs/releasing.md) · [தமிழ்](../../ta/docs/releasing.md) · [ไทย](../../th/docs/releasing.md) · [Türkçe](../../tr/docs/releasing.md) · [Українська](../../uk/docs/releasing.md) · [اردو](../../ur/docs/releasing.md) · [Tiếng Việt](../../vi/docs/releasing.md)

[Translation policy](../../README.md)

</details>
<!-- nv-language-navigation:end -->

<!-- nv-translation-notice:start -->
> Machineondersteunde vertaling uit het Engels. Technische namen, commando's, URL's en originele juridische teksten blijven behouden. Recensie door native speakers is welkom; raadpleeg de Engelse referentie als de formulering onduidelijk is.
<!-- nv-translation-notice:end -->

<a id="publishing-and-releases"></a>
# Publicaties en releases

De openbare repository is **Zendo-GIT/NV-Laboratorium**. Documentatiewijzigingen worden beoordeeld, vastgelegd en gepusht door de beheerder met **GitHub Desktop**. Een lokale commit uploadt geen bestanden. Binaire pakketten zijn afzonderlijke GitHub Release-middelen; ze horen nooit thuis in de lijst met Git-wijzigingen.

<a id="documentation-updates"></a>
## Documentatie-updates

1. Open de map **NV-Laboratory** in GitHub Desktop.
2. Beoordeel documentatie, mededelingen, afbeeldingen, JSON-metagegevens en de documentatievalidator.
3. Voer `python tools/validate_repository.py` uit vanuit die map.
4. Voer de beoordeelde wijzigingen door en gebruik vervolgens **Push origin**. Controleer het resultaat Acties.
5. Bewaar de openbare identiteit van de auteur **禅堂 Zendo (RevoluSound Team)** en het GitHub `noreply`-adres van het account.

Selecteer nooit de bovenliggende ontwikkelingswerkruimte, de privé-auditmap of de map voor binaire bijlagen. [Zorg voor e-mailprivacy](https://docs.github.com/en/account-and-profile/how-tos/email-preferences/setting-your-commit-email-address).

<a id="independent-application-releases"></a>
## Onafhankelijke applicatie-releases

| Gereedschap | Label | Versiebeleid |
| --- | --- | --- |
| NVIDIA Profile Inspector – NV Tools Fork | nvpi-v3.0.2.3 | Bestaande vierdelige applicatieversie; setup-revisie 2 heeft een eigen bestandsnaam |
| NVDriverForge | nvdriverforge-v0.1.3 | Bestaand 0.x-schema; Versie-updates behouden eerdere pakketten |
| NVMFG Unlock40 | nvmfg-unlock40-v0.1.1 | UI2-kandidaat geïdentificeerd door exacte hashes zonder een nieuwe applicatieversie uit te vinden |
| NVRasterPulse | nvrasterpulse-v0.1 | Bestaande tweedelige versie |

De beheerder kan de gecontroleerde activa rechtstreeks publiceren of een assistent machtigen om de gecontroleerde activa te publiceren. Publicatie is expliciet; geen enkele workflow creëert een Release voor elke commit.

1. Bekijk het huidige prepublicatierapport, de bronnen van de binaire bestanden, licenties en SHA-256-waarden.
2. Maak een concept voor de tag van de tool, gericht op de beoordeelde hub-vastlegging. Voeg de voorbereide versiespecifieke release-opmerkingen toe.
3. Voeg alleen de installatie-/draagbare middelen van die versie toe, `Licenses-and-Credits.zip` en `SHA256SUMS.txt`.
4. Controleer compatibiliteit, installatie, afhankelijkheden, wijzigingen en bekende limieten. Houd RTSS prominent aanwezig voor NVRasterPulse.
5. Publiceer, verifieer de URL's, groottes en hashes van openbare assets en noteer de daadwerkelijke publicatiedatum in `docs/releases.json`.
6. Werk de downloadpagina's en vertalingen bij en voer vervolgens de wijzigingen door in GitHub Desktop.

De tag-links per project voorkomen dat gebruikers naar een andere tool worden gestuurd via een gedeelde `releases/latest`-link. De automatische **Source code**-archieven van GitHub bevatten deze documentatiehub. Applicatiebronnen blijven privé. De oorspronkelijke componentkennisgevingen blijven intact en een release lost de gedocumenteerde NVIDIA SDK-reserve van NVMFG niet op.

<a id="integrity-and-storage"></a>
## Integriteit en opslag

Vervang nooit in stilte gepubliceerde binaire bytes. Gebruik een nieuwe expliciete versie of revisie van het installatieprogramma met nieuwe hashes. Juridische zijspannen vormen een aanvulling op ingebedde mededelingen. NVDriverForge 0.1.3 portable is 141.760.351 bytes, boven de gewone limiet van 100 MiB Git-bestanden van GitHub. Bij het vrijgeven van bijlagen moet u voorkomen dat binaire bestanden of Git LFS in deze hub worden geplaatst. [GitHub begeleiding voor grote bestanden](https://docs.github.com/en/repositories/working-with-files/managing-large-files/about-large-files-on-github).

Rapportage van privékwetsbaarheden moet zijn ingeschakeld in de beveiligingsinstellingen van de repository. Controleer de beschikbaarheid ervan voordat u gevoelige rapporten daar naartoe stuurt; [SECURITY.md](../SECURITY.md) biedt een fallback die geen details over de kwetsbaarheid blootlegt.

[Catalogus downloaden](downloads.md) · [GitHub-releasedocumentatie](https://docs.github.com/en/repositories/releasing-projects-on-github/managing-releases-in-a-repository)
