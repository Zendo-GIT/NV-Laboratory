<!-- nv-language-navigation:start -->
🌐 [English](../../../releasing.md) | [Français](../../../releasing.fr.md) · [NV Laboratory](../README.md)

<details>
<summary>🌐 Language · 34</summary>

[العربية](../../ar/docs/releasing.md) · [বাংলা](../../bn/docs/releasing.md) · [简体中文](../../zh/docs/releasing.md) · [Čeština](../../cs/docs/releasing.md) · [Dansk](../../da/docs/releasing.md) · [Nederlands](../../nl/docs/releasing.md) · [English](../../../releasing.md) · [Filipino](../../fil/docs/releasing.md) · **Suomi** · [Français](../../../releasing.fr.md) · [Deutsch](../../de/docs/releasing.md) · [Ελληνικά](../../el/docs/releasing.md) · [हिन्दी](../../hi/docs/releasing.md) · [Magyar](../../hu/docs/releasing.md) · [Bahasa Indonesia](../../id/docs/releasing.md) · [Italiano](../../it/docs/releasing.md) · [日本語](../../ja/docs/releasing.md) · [한국어](../../ko/docs/releasing.md) · [मराठी](../../mr/docs/releasing.md) · [فارسی](../../fa/docs/releasing.md) · [Polski](../../pl/docs/releasing.md) · [Português](../../pt/docs/releasing.md) · [ਪੰਜਾਬੀ](../../pa/docs/releasing.md) · [Română](../../ro/docs/releasing.md) · [Русский](../../ru/docs/releasing.md) · [Español](../../es/docs/releasing.md) · [Kiswahili](../../sw/docs/releasing.md) · [Svenska](../../sv/docs/releasing.md) · [தமிழ்](../../ta/docs/releasing.md) · [ไทย](../../th/docs/releasing.md) · [Türkçe](../../tr/docs/releasing.md) · [Українська](../../uk/docs/releasing.md) · [اردو](../../ur/docs/releasing.md) · [Tiếng Việt](../../vi/docs/releasing.md)

[Translation policy](../../README.md)

</details>
<!-- nv-language-navigation:end -->

<!-- nv-translation-notice:start -->
> Koneavusteinen käännös englannista. Tekniset nimet, komennot, URL-osoitteet ja alkuperäiset lakitekstit säilytetään. Äidinpuhujien arvostelu on tervetullut; katso englanninkielinen viittaus, jos sanamuoto on epäselvä.
<!-- nv-translation-notice:end -->

<a id="publishing-and-releases"></a>
# Julkaiseminen ja julkaisut

Julkinen arkisto on **Zendo-GIT/NV-Laboratory**. Ylläpitäjä tarkistaa, sitoo ja välittää dokumentaatiomuutokset **GitHub Desktop** avulla. Paikallinen toimitus ei lataa tiedostoja. Binaaripaketit ovat erillisiä GitHub Release -resursseja; ne eivät koskaan kuulu Git-muutosluetteloon.

<a id="documentation-updates"></a>
## Dokumentaatiopäivitykset

1. Avaa **NV-Laboratory**-kansio GitHub Desktop:ssä.
2. Tarkista dokumentaatio, ilmoitukset, kuvat, JSON-metatiedot ja dokumentaation validointiohjelma.
3. Suorita `python tools/validate_repository.py` kyseisestä kansiosta.
4. Vahvista tarkistetut muutokset ja käytä sitten **Push origin**. Tarkista toimintojen tulos.
5. Säilytä julkinen tekijän tunnistus **禅堂 Zendo (RevoluSound Team)** ja tilin GitHub `noreply` osoite.

Älä koskaan valitse ylätason kehitystyötilaa, yksityistä tarkastushakemistoa tai binaarista liitehakemistoa. [Sitoudu sähköpostin tietosuojaan](https://docs.github.com/en/account-and-profile/how-tos/email-preferences/setting-your-commit-email-address).

<a id="independent-application-releases"></a>
## Riippumattomat sovellusjulkaisut

| Työkalu | Tag | Versiopolitiikka |
| --- | --- | --- |
| NVIDIA Profile Inspector – NV Tools Fork | nvpi-v3.0.2.3 | Nykyinen neliosainen sovellusversio; asennusversiolla 2 on oma tiedostonimi |
| NVDriverForge | nvdriverforge-v0.1.4 | Olemassa oleva 0.x-järjestelmä; versioidut päivitykset säilyttävät aiemmat paketit |
| NVMFG Unlock40 | nvmfg-unlock40-v0.2.3 | Sovellusversio 0.2.3; kumulatiiviset muutokset julkisen 0.1.1 jälkeen |
| NVRasterPulse | nvrasterpulse-v0.2 | Nykyinen kaksiosainen versio |

Ylläpitäjä voi julkaista tarkastetun omaisuuden suoraan tai valtuuttaa avustajan julkaisemaan tarkastetut varat. Julkaisu on selkeä; mikään työnkulku ei luo julkaisua jokaiselle toimitukselle.

1. Tarkista nykyinen esijulkaisuraportti, binäärien lähteet, lisenssit ja SHA-256-arvot.
2. Luo luonnos työkalun tunnisteelle, joka kohdistaa tarkistettuun keskittimeen. Liitä mukaan valmistetut versiokohtaiset julkaisutiedot.
3. Liitä vain kyseisen version Setup/Portable Content, `Licenses-and-Credits.zip` ja `SHA256SUMS.txt`.
4. Tarkista yhteensopivuus, asennus, riippuvuudet, muutokset ja tunnetut rajat. Pidä RTSS näkyvänä NVRasterPulse:lle.
5. Julkaise, vahvista julkisten resurssien URL-osoitteet, koot ja tiivisteet ja kirjaa todellinen julkaisupäivä `docs/releases.json`-tiedostoon.
6. Päivitä lataussivut ja käännökset ja vahvista/työnä niiden muutokset GitHub Desktop:ssä.

Projektikohtaiset tunnistelinkit estävät käyttäjien lähettämisen toiseen työkaluun jaetun `releases/latest`-linkin kautta. GitHub:n automaattiset **Source code**-arkistot sisältävät tämän dokumentaatiokeskuksen. Sovelluslähteet pysyvät yksityisinä. Alkuperäisten komponenttien ilmoitukset pysyvät ennallaan, eikä julkaisu ratkaise NVMFG:n dokumentoitua NVIDIA SDK -varausta.


Syyskuun 18. päivän päivitys valmistelee kolme uutta tunnistetta; nykyinen Profile Inspector-julkaisu pysyy ennallaan. Omaisuuden nimien, tunnisteiden ja `SHA256SUMS.txt`:n on pysyttävä täsmällisinä sovellusten päivitystarkistuksia varten. Julkaise normaalit julkaisut ilman esijulkaisua, jotta ne altistuvat vakaan julkaisun tarkistuksille. NVMFG on edelleen kokeellinen.

<a id="integrity-and-storage"></a>
## Eheys ja säilytys

Älä koskaan vaihda julkaistuja binääritavuja hiljaa. Käytä uutta eksplisiittistä versiota tai asennusohjelman versiota uusilla tiivisteillä. Lailliset sivuvaunut täydentävät upotettuja ilmoituksia. NVDriverForge Kannettava 0.1.4 on 142 017 891 tavua, mikä ylittää GitHub:n tavallisen 100 MiB Git-tiedoston rajan. Vapauta liitteet välttämään binäärien tai Git LFS:n sijoittamista tähän keskittimeen. [GitHub suurten tiedostojen opastus](https://docs.github.com/en/repositories/working-with-files/managing-large-files/about-large-files-on-github).

Yksityinen haavoittuvuusraportointi tulee ottaa käyttöön tietovaraston suojausasetuksissa. Varmista sen saatavuus ennen kuin ohjaat arkaluonteisia raportteja sinne. [SECURITY.md](../SECURITY.md) tarjoaa varavaihtoehdon, joka ei paljasta haavoittuvuuden tietoja.

[Lataa luettelo](downloads.md) · [GitHub julkaisudokumentaatio](https://docs.github.com/en/repositories/releasing-projects-on-github/managing-releases-in-a-repository)
