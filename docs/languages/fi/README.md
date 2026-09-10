<!-- nv-language-navigation:start -->
🌐 [English](../../../README.md) | [Français](../../../README.fr.md) · [NV Laboratory](README.md)

<details>
<summary>🌐 Language · 34</summary>

[العربية](../ar/README.md) · [বাংলা](../bn/README.md) · [简体中文](../zh/README.md) · [Čeština](../cs/README.md) · [Dansk](../da/README.md) · [Nederlands](../nl/README.md) · [English](../../../README.md) · [Filipino](../fil/README.md) · **Suomi** · [Français](../../../README.fr.md) · [Deutsch](../de/README.md) · [Ελληνικά](../el/README.md) · [हिन्दी](../hi/README.md) · [Magyar](../hu/README.md) · [Bahasa Indonesia](../id/README.md) · [Italiano](../it/README.md) · [日本語](../ja/README.md) · [한국어](../ko/README.md) · [मराठी](../mr/README.md) · [فارسی](../fa/README.md) · [Polski](../pl/README.md) · [Português](../pt/README.md) · [ਪੰਜਾਬੀ](../pa/README.md) · [Română](../ro/README.md) · [Русский](../ru/README.md) · [Español](../es/README.md) · [Kiswahili](../sw/README.md) · [Svenska](../sv/README.md) · [தமிழ்](../ta/README.md) · [ไทย](../th/README.md) · [Türkçe](../tr/README.md) · [Українська](../uk/README.md) · [اردو](../ur/README.md) · [Tiếng Việt](../vi/README.md)

[Translation policy](../README.md)

</details>
<!-- nv-language-navigation:end -->

<!-- nv-translation-notice:start -->
> Koneavusteinen käännös englannista. Tekniset nimet, komennot, URL-osoitteet ja alkuperäiset lakitekstit säilytetään. Äidinpuhujien arvostelu on tervetullut; katso englanninkielinen viittaus, jos sanamuoto on epäselvä.
<!-- nv-translation-notice:end -->

<a id="nv-laboratory"></a>
# NV Laboratory

**NV Tools, 禅堂 Zendo (RevoluSound Team).** Neljä erillistä Windows-apuohjelmaa NVIDIA-ohjainprofiileille, ohjaimen asennus, kokeelliset Multi Frame Generation- ja RTSS-kehysrajoitukset.

[Hanki työkalut](docs/downloads.md) · [Asennus](docs/installation.md) · [Yhteensopivuus ja apu](docs/support.md) · [Krediitit ja lisenssit](THIRD_PARTY_NOTICES.md)

> **NVRasterPulse vaatii RTSS:n.** Asenna ensin [RivaTuner Statistics Server Guru3D:ltä](https://www.guru3d.com/download/rtss-rivatuner-statistics-server-download/). RTSS:n on oltava käynnissä, jotta sen FPS-rajoitukset toimivat. Se ladataan erikseen.

<a id="projects"></a>
## Projektit

| Projekti | Tarkoitus | Versio | Dokumentaatio | Lataa |
| --- | --- | --- | --- | --- |
| **NVIDIA Profile Inspector – NV Tools Fork** | NVIDIA kuljettajaprofiilien editori, johon on lisätty näyttö-, väri-, HDR- ja ICC/WCS-ohjaimet. Aiemmin NVPI Custom. | 3.0.2.3 | [Opas](NVIDIA-Profile-Inspector/README.md) | [Paketit](docs/downloads.md#nvidia-profile-inspector) |
| **NVDriverForge** | Valitse ohjainkomponentit, tarkista valinnaiset parannukset ja asenna alkuperäinen NVIDIA-ohjainpaketti. | 0.1.3 | [Opas](NVDriverForge/README.md) | [Paketit](docs/downloads.md#nvdriverforge) |
| **NVMFG Unlock40** | Kokeellinen RTX 40 MFG -työkalu pelikohtaisilla valinnoilla ja Streamline SDK -ylläpidolla. | 0.1.1 | [Opas](NVMFG-Unlock40/README.md) | [Paketit ja tila](docs/downloads.md#nvmfg-unlock40) |
| **NVRasterPulse** | Hallitse RTSS FPS rajoituksia suoritettavaa kohdetta kohti murto-arvoilla, varmuuskopioilla ja lokeron käyttöoikeuksilla. | 0.1 | [Opas](NVRasterPulse/README.md) | [Paketit](docs/downloads.md#nvrasterpulse) |

**Lataukset:** [lataussivu](docs/downloads.md) näyttää kunkin version tilan, tiedostot ja SHA-256-arvot. Kokeelliset ominaisuudet ja yhteensopivuusrajat on kuvattu projektioppaissa.

<a id="start-here"></a>
## Aloita tästä

1. Valitse yksi työkalu ylhäältä. Jokainen toimii itsenäisesti; koko sarjan asentaminen on tarpeetonta.
2. Lue sen vaatimukset ja valitse **Setup** asennetulle sovellukselle tai **portable** erilliselle kansiolle.
3. Kun sen julkaisu on julkaistu, lataa nimetty sovellusresurssi, lue mukana tulevat ilmoitukset ja vertaa sen SHA-256-tiedostoa.
4. Pidä varmuuskopiot ennen ohjaimen, näyttöasetuksen, NVIDIA-profiilin tai pelin suoritusajan muuttamista.

Dokumentaatio on saatavilla samoilla 34 kielellä kuin NV-sovellukset kunkin oppaan yläosassa olevan valitsimen kautta. GitHub ei valitse automaattisesti README-komentoa selaimen kielen mukaan. Dokumentaation kieli ja sovelluksen oma kieliasetus ovat erillisiä.

<a id="provenance-and-ownership"></a>
## Alkuperä ja omistus

Tämä keskus jakaa dokumentaatiota ja koottuja sovelluksia. Sovelluksen lähdekoodia ylläpidetään yksityisesti. Varhaisemmat hankkeet säilyttävät tekijän ja lisenssinsä; yksityisen lähteen jakelu ei korvaa näitä ehtoja.

- Profile Inspector fork säilyttää Orbmu2k:n MIT-lisenssin ja on nimenomaisesti tunnistettu fork:ksi.
- NVDriverForge:llä on omat binaariset jakeluehdot ja se sisältää erikseen lisensoidut ajonaikaiset/työkalukomponentit.
- NVMFG Unlock40 on itsenäisesti kehitetty sovellus. RTX40MFG-Unlock:tä kuultiin vertailua ja tarkennusta varten; jaetut natiivikomponentit säilyttävät MIT-hyvityksensä. MinHook ja NVIDIA SDK ehdot pysyvät erillisinä.
- NVRasterPulse säilyttää toimitetun MIT-lisenssin ja hyvittää Profile Inspector-pohjaisen käyttöliittymän. RTSS on pakollinen ulkoinen ohjelma.

Katso [täydellinen komponenttitaulukko](THIRD_PARTY_NOTICES.md), [tiedostojen alkuperä ja muutokset](docs/provenance.md) ja [lisenssin laajuus](../../../LICENSE).

<a id="other-projects--revolusound-team"></a>
## Muut projektit – RevoluSound Team

Nämä ovat erillisiä audiomodiprojekteja, jotka on linkitetty tähän auttamaan sinua tutustumaan tiimin työhön.

| Peli | Projekti | Tietoja |
| --- | --- | --- |
| Forza Horizon 6 | [Forza Horizon 6 Revolusound Team Pack](https://www.nexusmods.com/forzahorizon6/mods/56) | Ajoneuvon äänen muutokset kattavat moottorit, pakoputket, imut ja turboefektit. |
| Forza Horizon 5 | [Forza Horizon 5 Revolusound Team Pack 1.4.4 FINAL](https://www.nexusmods.com/forzahorizon5/mods/86) | Joukkueen myöhempi FH5-ajoneuvon äänipaketti. |
| Forza Horizon 5 | [Forza Horizon 5.5 Zendo Revolusound Pack](https://www.nexusmods.com/forzahorizon5/mods/20) | Aikaisempi FH5-paketti; sen Nexus-sivu ohjaa vierailijat yllä olevaan myöhempään tiimipakettiin. |

Otsikot seuraavat linkitettyjä Nexus Mods-sivuja. Heidän lataukset, vaatimuksensa, hyvitykset ja käyttöoikeudet säilyvät Nexus Mods:ssä.

<a id="help-and-participation"></a>
## Apua ja osallistumista

[Ilmoita virheestä tai ehdota ominaisuutta](https://github.com/Zendo-GIT/NV-Laboratory/issues) · [Osallistuminen](CONTRIBUTING.md) · [Turvallisuusraportit](SECURITY.md) · [Muutosloki](CHANGELOG.md)

Jos sinulla on tietoturvaongelma, lue SECURITY.md ennen lokien tai teknisten tietojen lähettämistä. Ylläpitäjän tulee ottaa yksityinen raportointi käyttöön arkiston julkaisemisen jälkeen.

> **Riippumattomia yhteisöprojekteja.** NV Laboratory, NV Tools ja nämä apuohjelmat eivät ole sidoksissa NVIDIA Corporation:n, sponsoroi tai ole virallisesti hyväksynyt. NVIDIA, GeForce, RTX, DLSS ja muut tuotenimet ovat omistajiensa tavaramerkkejä. Nimet kuvaavat yhteensopivuutta ja alkuperää, eivät virallista hyväksyntää.
