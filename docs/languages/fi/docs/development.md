<!-- nv-language-navigation:start -->
🌐 [English](../../../development.md) | [Français](../../../development.fr.md) · [NV Laboratory](../README.md)

<details>
<summary>🌐 Language · 34</summary>

[العربية](../../ar/docs/development.md) · [বাংলা](../../bn/docs/development.md) · [简体中文](../../zh/docs/development.md) · [Čeština](../../cs/docs/development.md) · [Dansk](../../da/docs/development.md) · [Nederlands](../../nl/docs/development.md) · [English](../../../development.md) · [Filipino](../../fil/docs/development.md) · **Suomi** · [Français](../../../development.fr.md) · [Deutsch](../../de/docs/development.md) · [Ελληνικά](../../el/docs/development.md) · [हिन्दी](../../hi/docs/development.md) · [Magyar](../../hu/docs/development.md) · [Bahasa Indonesia](../../id/docs/development.md) · [Italiano](../../it/docs/development.md) · [日本語](../../ja/docs/development.md) · [한국어](../../ko/docs/development.md) · [मराठी](../../mr/docs/development.md) · [فارسی](../../fa/docs/development.md) · [Polski](../../pl/docs/development.md) · [Português](../../pt/docs/development.md) · [ਪੰਜਾਬੀ](../../pa/docs/development.md) · [Română](../../ro/docs/development.md) · [Русский](../../ru/docs/development.md) · [Español](../../es/docs/development.md) · [Kiswahili](../../sw/docs/development.md) · [Svenska](../../sv/docs/development.md) · [தமிழ்](../../ta/docs/development.md) · [ไทย](../../th/docs/development.md) · [Türkçe](../../tr/docs/development.md) · [Українська](../../uk/docs/development.md) · [اردو](../../ur/docs/development.md) · [Tiếng Việt](../../vi/docs/development.md)

[Translation policy](../../README.md)

</details>
<!-- nv-language-navigation:end -->

<!-- nv-translation-notice:start -->
> Koneavusteinen käännös englannista. Tekniset nimet, komennot, URL-osoitteet ja alkuperäiset lakitekstit säilytetään. Äidinpuhujien arvostelu on tervetullut; katso englanninkielinen viittaus, jos sanamuoto on epäselvä.
<!-- nv-translation-notice:end -->

<a id="repository-architecture-and-maintenance"></a>
# Arkistoarkkitehtuuri ja ylläpito

NV Laboratory on julkinen **dokumentaatio- ja binäärijakelukeskus**. Se ei sisällä sovelluslähdettä. Neljä projektia säilyttävät erilliset rakennuspuut, versiot, identiteetit ja julkaisuresurssit. Heidän yksityistä kehityshistoriaansa ei tuoda tähän Git-tietovarastoon.

<a id="layout"></a>
## Asettelu

| Sijainti | Tarkoitus |
| --- | --- |
| README.md / README.fr.md | Englannin/ranskalaisen sisääntulopisteet |
| Neljä projektikansiota | Täydelliset oppaat ja sovellettavat alkuperäiset ilmoitukset |
| asiakirjoja | Lataukset, yhteensopivuus, alkuperä, kehitys ja julkaisumenettely |
| docs/releases.json | Tarkastetut ehdokkaiden/julkaisujen metatiedot, koot ja tiivisteet |
| asiakirjat / alkuperä | Tiedosto-/tiivistevertailut; ei sovelluskoodia |
| lisenssit | Jaettu täydelliset kolmannen osapuolen tekstit ja asentajan kääntäjän krediitit |
| omaisuutta | Olemassa olevat tarkistetut käyttöliittymän esikatselut ja niiden alkuperä |
| .github | Myönnä lomakkeita ja vain luku -dokumenttien validointi |
| työkalut/validate_repository.py | Vakiokirjaston julkaisurajojen ja linkkien tarkistukset |

Englanti on edelleen oletuskieli GitHub README. Olemassa olevat viereiset `.fr.md`-linkit pysyvät voimassa. Lisäkäännökset heijastavat dokumentaatiota kohdassa `docs/languages/<code>`; kielenvalitsin pitää saman sivun kieliä vaihdettaessa. Luettelo `docs/languages/catalog.json` tallentaa kaikki 34 kieltä ja lähdesormenjäljet. GitHub ei valitse automaattisesti README-komentoa selaimen kielen mukaan. Katso [kielihakemisto ja käännöspolitiikka](../../README.md).

<a id="application-technologies"></a>
## Sovellustekniikat

| Ohjelma | Yksityinen tekniikka | Jakelu |
| --- | --- | --- |
| NVPI fork | C#, WPF, .NET Framework 4.8, NVAPI/Windows yhteensopivuus | Täydellinen kannettava kansio ja erillinen Inno Setup |
| NVDriverForge | C#, WPF, .NET 8; alkuperäinen C++ bootstrap; 7-Zip-prosessi | Itsenäinen kannettava EXE ja asennusohjelma |
| NVMFG Unlock40 | C#/WPF .NET 8, Framework 4.8 apuohjelmat, C++20/MASM/MinHook moottori | Kannettava puu ja asetukset |
| NVRasterPulse | C#/WPF Framework 4.8; RTSS profiilin/uudelleenlatauksen integrointi; natiivi bootstrap | Kannettava puu ja asetukset |

Tämä julkinen kassa ei voi rakentaa sovelluksia uudelleen. Automaattiset "Source code" -arkistot ovat keskittimen tilannekuvia. Ylävirran lähdelinkit eivät edusta täsmälleen yksityistä muokattua lähdettä. Julkinen CI vahvistaa vain tämän arkiston.

<a id="local-checks"></a>
## Paikalliset tarkastukset

Arkiston juuresta:

```text
python tools/validate_repository.py
```

Python 3.10 tai uudempi riittää. Tarkistus lukee tiedostot, paikalliset Markdown-linkit, pakolliset ilmoitukset/RTSS-linkit, julkaisun metatiedot ja julkaisurajat. Se ei suorita ohjelmistoa, asenna riippuvuuksia tai ota yhteyttä verkkoon.

GitHub-työnkulku suorittaa saman tarkistuksen vain luku -sisällön luvalla push-, pull-pyynnön tai manuaalisen lähetyksen yhteydessä. Checkout on kiinnitetty tarkastettuun sitoumukseen, eikä se säilytä valtuustietoja. Julkaisu- tai käyttöönottotyötä ei ole määritetty.

<a id="maintain-the-boundary"></a>
## Säilytä raja

Päivitä englanninkielinen viittaus, ranskankieliset oppaat ja asiaankuuluvat käännökset yhdessä. Pidä olennaiset muutokset erillään vain muotoilua koskevista vertailuista. Tallenna todelliset ehdokastiivisteet, alkupään sitovat viittaukset ja lisenssit; Älä koskaan päättele lisenssiä projektin suosiosta.

Käytä tuoretta versioitua Release-sisältöä ja tarkista muuttuneet binaarit, arkistot ja upotetut ilmoitukset uudelleen. Säilytä yksityiset varmuuskopiot tämän arkiston ulkopuolella. Älä käytä julkista työnkulkua yksityisten sovelluslähteiden tai paikallisten koontikansioiden tuomiseen.

Toiminnalliseen sovelluksen muutokseen soveltuvat testit suoritetaan yksityisessä projektissa. Älä suorita ohjainasennusohjelmia uudelleen tai kirjoita oikeita profiileja dokumentaatiopäivitystä varten. [Manuaalinen vapautusmenettely](releasing.md).
