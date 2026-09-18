<!-- nv-language-navigation:start -->
🌐 [English](../../../../NVDriverForge/README.md) | [Français](../../../../NVDriverForge/README.fr.md) · [NV Laboratory](../README.md)

<details>
<summary>🌐 Language · 34</summary>

[العربية](../../ar/NVDriverForge/README.md) · [বাংলা](../../bn/NVDriverForge/README.md) · [简体中文](../../zh/NVDriverForge/README.md) · [Čeština](../../cs/NVDriverForge/README.md) · [Dansk](../../da/NVDriverForge/README.md) · [Nederlands](../../nl/NVDriverForge/README.md) · [English](../../../../NVDriverForge/README.md) · [Filipino](../../fil/NVDriverForge/README.md) · **Suomi** · [Français](../../../../NVDriverForge/README.fr.md) · [Deutsch](../../de/NVDriverForge/README.md) · [Ελληνικά](../../el/NVDriverForge/README.md) · [हिन्दी](../../hi/NVDriverForge/README.md) · [Magyar](../../hu/NVDriverForge/README.md) · [Bahasa Indonesia](../../id/NVDriverForge/README.md) · [Italiano](../../it/NVDriverForge/README.md) · [日本語](../../ja/NVDriverForge/README.md) · [한국어](../../ko/NVDriverForge/README.md) · [मराठी](../../mr/NVDriverForge/README.md) · [فارسی](../../fa/NVDriverForge/README.md) · [Polski](../../pl/NVDriverForge/README.md) · [Português](../../pt/NVDriverForge/README.md) · [ਪੰਜਾਬੀ](../../pa/NVDriverForge/README.md) · [Română](../../ro/NVDriverForge/README.md) · [Русский](../../ru/NVDriverForge/README.md) · [Español](../../es/NVDriverForge/README.md) · [Kiswahili](../../sw/NVDriverForge/README.md) · [Svenska](../../sv/NVDriverForge/README.md) · [தமிழ்](../../ta/NVDriverForge/README.md) · [ไทย](../../th/NVDriverForge/README.md) · [Türkçe](../../tr/NVDriverForge/README.md) · [Українська](../../uk/NVDriverForge/README.md) · [اردو](../../ur/NVDriverForge/README.md) · [Tiếng Việt](../../vi/NVDriverForge/README.md)

[Translation policy](../../README.md)

</details>
<!-- nv-language-navigation:end -->

<!-- nv-translation-notice:start -->
> Koneavusteinen käännös englannista. Tekniset nimet, komennot, URL-osoitteet ja alkuperäiset lakitekstit säilytetään. Äidinpuhujien arvostelu on tervetullut; katso englanninkielinen viittaus, jos sanamuoto on epäselvä.
<!-- nv-translation-notice:end -->

<a id="nvdriverforge"></a>
# NVDriverForge

**Valmista NVIDIA-ajurin asennus selkeällä komponenttivalinnalla ja valinnaisilla asetuksilla.**

[Lataa 0.1.4 ja tila](../docs/downloads.md#nvdriverforge) · [Asennus](#installation) · [Krediitit](#credits-and-upstream) · [Lisenssi](../../../../NVDriverForge/LICENSE)

<a id="overview-and-purpose"></a>
## Yleiskatsaus ja tarkoitus

NVDriverForge opastaa sinut alkuperäisen NVIDIA-ohjainpaketin läpi: valitse ohjain, tarkista sen komponentit, tarkista valinnaiset parannukset ja vahvista asennus. Se on olemassa, jotta nämä valinnat olisivat ymmärrettäviä ja asennuksen, etuoikeutettujen toimintojen ja palautustietojen pitäminen yhdessä.

Se on itsenäisesti kehitetty sovellus, joka on osittain inspiroitunut NVCleanstall:n työnkulusta. Se ei sisällä NVCleanstall:tä tai vaadi täydellistä ominaisuuspariteettia.

<a id="features"></a>
## Ominaisuudet

- NVIDIA Game Ready / Studio haku ja lataukset; valinnainen hotfix-korjauksen etsintä manuaalisella varatoiminnolla.
- Alkuperäisen paketin, tiivisteiden, NVIDIA-allekirjoitusten, luetteloiden ja yhteensopivien INF-merkintöjen analyysi.
- Komponenttien valinta riippuvuuksilla ja tuntemattomien komponenttien säilyttäminen.
- Versio 0.1.4 pitää valitut valinnaiset NVIDIA-komponentit ohitettavina ja sulkee pois vain vahvistetut tarkistamattomat komponentit. Jo olemassa olevia tai käyttämättömiä valinnaisia ​​ajonaikoja ei enää pakoteta kriittisiksi komponenteiksi.
- Selkeät asennusvirheiden yhteenvedot ja pääsy yksityiskohtaisiin lokeihin kaikilla 34 kielellä.
- Valmiustarkistukset, selkeä vahvistus, vienti ajurivarastoon ja alkuperäisen NVIDIA-profiilin varmuuskopiointi ennen asennusta.
- Valinnaiset lisäasetukset, joissa on lentoa edeltävät tarkistukset, päiväkirjat ja konfliktitietoinen palautus.
- Valinnainen **Custom NV** esiasetus nimetyillä valinnoilla ja selityksillä, mukaan lukien erillinen SILK vahvuuden valinta ja yhteensopivuustarkistukset.
- Valinnainen tarkan version NVENC korjaustiedoston lataukset; lähde- ja kohdetavut tarkistetaan.
- Profile Inspector fork:n erillinen valinnainen asennus Työkalut-näytöstä.
- Komponenttiopas, uudelleen käytettävät asetukset, ohjainsarjat, paikalliset tukiraportit ja valinnaiset sovelluspäivitykset.
- 34 käyttöliittymäkieltä ja neljä teemaa.

Käytettävissä olevat lisäasetukset koskevat MPO:tä, DLSS-ilmaisinta, Ansel-, NVIDIA-äänen lepotilaa, MSI, keskeytyskäytäntö/prioriteetti, HDCP, näyttösäilön käynnistys ja kelvollinen vanha telemetriapalvelu. Jokaisella on omat edellytyksensä ja vaikutuksensa; nämä eivät ole yleisiä suorituskyvyn parannuksia.

<a id="compatibility"></a>
## Yhteensopivuus

| Vaatimus | Yksityiskohdat |
| --- | --- |
| Järjestelmä | Windows 10 build 19041 tai uudempi / Windows 11, x64 |
| GPU/ohjain | Yhteensopiva NVIDIA-paketti ja havaittu laitteisto; automaattinen luettelohaku kattaa ensisijaisesti tunnetut GeForce-mallit |
| Suoritusaika | .NET 8 / WPF 8.0.31 mukana valmiissa erillisessä paketissa |
| Etuoikeudet | Normaali käyttöliittymä/käyttäjäkohtainen asetus; ohjaimen asennus ja järjestelmän muutokset vaativat järjestelmänvalvojan käyttöoikeuksia |
| Verkko | Vaaditaan online-NVIDIA-hakuihin/latauksiin ja eksplisiittisiin ylävirran NVENC-pyyntöihin; paikallinen alkuperäinen ohjain voidaan valita |
| Mukana työkalut | Muokkaamaton 7-Zip 26.03, ajonaikaiset ilmoitukset, valinnainen MIT Profile Inspector kumppani |
| Valinnainen kumppani | .NET Framework 4.8 erilliselle Profile Inspector fork |

Mikään mielivaltainen vähimmäisohjainversio ei kata kaikkia ominaisuuksia. Multi-GPU-haun on vastattava jokaista havaittua GPU:tä. Ei-tuetut/ammattimaiset mallit voivat edellyttää manuaalista ohjaimen valintaa. NVIDIA:n asennusohjelma on edelleen viimeinen laitteisto-/käyttöjärjestelmävaltuutettu.

<a id="installation"></a>
## Asennus

1. Vieraile osoitteessa [lataukset](../docs/downloads.md#nvdriverforge) ja vahvista, että julkaisu on julkaistu.
2. Valitse `NVDriverForge-Setup.exe` asennusta varten tai `NVDriverForge.exe` kannettavaa käyttöä varten.
3. Vertaa SHA-256:ää julkaisun `SHA256SUMS.txt`:ään.
4. Suorita asennusohjelma käyttäjäkohtaista asennusta ja tavallista poistoohjelmaa varten tai aseta kannettava EXE kirjoitettavaan kansioon ja avaa se.

Kannettava sisältää sen käyttöajan ja valinnaisen asennusohjelman. NVDriverForge:n asentaminen ei asenna GPU-ohjainta. Sen EXE-tiedostot ovat tällä hetkellä allekirjoittamattomia.

<a id="usage"></a>
## Käyttö

1. **Ohjain:** lataa osoitteesta NVIDIA tai valitse alkuperäinen NVIDIA-asennusohjelma EXE. Anna analyysin valmistua.
2. **Komponentit:** tarkista kuvaukset ja vaaditut riippuvuudet. Tuntemattomat komponentit säilyvät.
3. **Parannukset:** jätä ei-toivotut vaihtoehdot ennalleen. Lue tehosteet ja kompromissit ennen kuin valitset mitään.
4. **Tarkista:** tarkista tarkka ohjain, komponentit ja valinnaiset toiminnot ja vahvista asennus.
5. Hyväksy UAC vain valitsemasi toiminnon osalta. Säilytä suojatun työn palautusohjeet.
6. Jos uusi ohjain tarvitsee uudelleenkäynnistyksen, noudata raportoitua tilaa. Lykätyt toiminnot vaativat nimenomaisen jatkamisen uudelleenkäynnistyksen jälkeen.

Custom NV alkaa muuttumattomana. Valitse yksittäiset nimetyt arvot tai tarkista toimitettu esiasetus ja sen poissulkemiset. Sen kahta sisäistä informaatiokenttää ei ole kirjoitettu itsenäisesti. Asetuksia käytetään vain vahvistetussa uuden ohjaimen työnkulussa, ei koskaan avaamalla esikatselua. Erillistä NVPI-editoria ei tarvitse asentaa.

Valinnainen NVENC-työ lataa yhteensopivat tiedot kiinnitetystä keylase-toteutuksesta. Se muuttaa kahta ajurin DLL:tä ja mitätöi niiden allekirjoitukset; Windows, enkooderit, DRM tai huijauksen esto voivat evätä sen. NVDriverForge:ään ei ole upotettu tällaisia ​​tietoja tai NVIDIA DLL:tä. [Alkuperä- ja lisenssirajoitukset](../docs/provenance.md).

Asetukset hallitsevat kielen, teeman ja valinnaisten asennettujen käyttäjien päivitystarkistuksia. Kannettava ei luo asennettua taustatarkistustehtävää. Työkalut ja palautus ovat erillisiä neljästä asennusvaiheesta.

<a id="backup-and-diagnostic-tools"></a>
## Varmuuskopiointi- ja diagnostiikkatyökalut

**Ennen asennusta:** Valmiustarkistukset kattavat paketin allekirjoituksen, GPU:t, arvioidun työtilan/varmuuskopiotilan, odottavan uudelleenkäynnistyksen ja kilpailevat asentajat. Korotettu työntekijä toistaa ne. Kilpailevia prosesseja ei koskaan pysäytetä automaattisesti. Alkuperäisen NVIDIA-profiilitietokannan varmuuskopioinnin on onnistuttava ennen NVIDIA-asennuksen alkamista. driver-store -vienti on erillinen varmuuskopio.

**Uudelleen käytettävät vaihtoehdot:** komponenttiopas kysyy neljä kysymystä peleistä, äänestä, NVIDIA App:stä ja tallentamisesta. Tarkista sen ehdotukset; vaaditut, tuntemattomat ja riippuvuuskomponentit pysyvät suojattuina. Vie asetukset, esikatsele ja tarkista ne valitussa paketissa tuonnin yhteydessä. Suostumuksia, uudelleenkäynnistystoimintoja, ohjelmapolkuja ja korjaustiedostoja ei tuoda.

**Ohjainsarja:** vie `.nvdfkit.zip` säilyttääksesi alkuperäisen allekirjoitetun NVIDIA-asennusohjelman, valinnat, tiivisteet ja ohjeet yhdessä. Kuljeta `NVDriverForge.exe` erikseen. Tuo sarja Toolsissa, tarkista esikatselu ja käytä sitten normaalia asennustyönkulkua. Tämä ei ole ohut ohjain tai muokattu erillinen asennusohjelma. Valinnainen NVENC tarvitsee edelleen latauksen ja suostumuksen juuri kyseiselle ohjaimelle. NVIDIA:n uudelleenjakoehdot ovat edelleen voimassa.

**Tulokset ja tuki:** lue lyhyt tulos ja laajenna vaihe-/vaihtoehtokohtaisia tietoja. Onnistunut takaisinluku määrittää tallennetun arvon, ei mitattua parannusta. Paikallinen JSON-tukiraportti käyttää sallittujen luettelon kenttiä, mukaan lukien viimeinen tallennettu työ sovelluksen uudelleenkäynnistyksen jälkeen. Esikatsele sitä ennen tallentamista tai jakamista. Se ei sisällä raakalokeja, profiilin sisältöä tai laitteistotunnisteita, eikä sitä koskaan ladata automaattisesti.

**Palautus:** noudata suojatun työn opasta palauttaaksesi varmuuskopioitu ohjain. Selkeä profiilin palauttaminen vaatii alkuperäisen ohjainversion ja samat GPU:t; se korvaa koko tietokannan, säilyttää nykyisen kopion ja tarkistaa tiivisteet ja ristiriitaiset tilat. Älä pyyhi sen päiväkirjaa tai pakota yhteensopimattomuutta. Aidon ohjaimen asennus, täydellinen palautus ja alkuperäisen profiilin tuonti tämän uuden työnkulun avulla jäävät vahvistamatta todellisessa järjestelmässä.

**Sovelluspäivitykset:** lue julkaisutiedot ja valitse sitten erikseen SHA-256-vahvistettu lataus. Tarkastus on oletuksena manuaalinen, ja valinnainen tarkistus käynnistyksen yhteydessä. Mikään asennusohjelma ei käynnisty automaattisesti. Tämä ominaisuus on erillinen ohjainpäivitystarkistuksista ja asennetun version valinnaisesta ohjaimen tarkistustehtävästä.

<a id="screenshots"></a>
## Kuvakaappauksia

![NVDriverForge ohjainsivun esikatselu](../../../../assets/screenshots/nvdriverforge-0.1.2-preview.png)

Olemassa oleva 0.1.2 ranskalainen käyttöliittymän renderöinti esimerkkitiedoilla; säilytetään käyttöliittymän esikatseluna. Näytetty 699.99-ohjain on testilaite, ei ladattava oikea versio. [Kuvan alkuperä](../assets/README.md).

<a id="update-and-uninstall"></a>
## Päivitä ja poista asennus

Sulje NVDriverForge, hanki seuraava virallinen paketti ja tarkista sen hash. Käytä samaa asennusohjelman identiteettiä asennetulle päivitykselle; korvaa suljettu kannettava EXE uudella. Säilytä asetukset ja suojatut työt.

Uninstall kohteesta Windows **Installed apps**. Se poistaa sovelluksen ja sen päivitystehtävän, ei NVIDIA-ohjainta. Asetukset, lokit ja varmuuskopiot säilyvät. Halutessasi palauta edistyneet/NVENC-muutokset dokumentoidun palautusvirran avulla **ennen** sovelluksen poistamista. Palauta kieltää ristiriitaiset muutokset toisesta työkalusta.

Paikalliset tiedot ovat alla `%LOCALAPPDATA%\NVDriverForge`; suojatut työpaikat ja kuljettajien vienti ovat `%PROGRAMDATA%\NVDriverForge\Jobs`:n alaisia. Kannettava käyttö luo myös paikallista dataa. Ohjainmyymälän vienti ja alkuperäisen profiilin varmuuskopiointi ovat erillisiä. Sekään ei ole järjestelmäkuva.

<a id="known-limitations"></a>
## Tunnetut rajoitukset

- Ei laitteistolisäyksiä/INF-muokkausta, uudelleen luotuja NVIDIA-allekirjoituksia, huijausten eston kanssa yhteensopivaa eroamista tai automaattista allekirjoittamattoman varoituksen hyväksymistä.
- Ei täydellistä telemetrian/mainosten poistoa, ohuiden pakettien vientiä tai automaattista täydellistä palautusta edelliseen ohjaimeen.
- Ohjaimen asennusta, käynnistyksen palautusta ja valinnaisia profiilikirjoituksia ei ole tarkastettu kattavasti oikeilla koneilla keskittimen tarkastuksessa.
- Rekisterin takaisinluku ei ole todiste todellisista HDCP-, suorituskyky- tai latenssivaikutuksista.
- Allekirjoitustarkistukset käyttävät paikallisesti saatavilla olevaa Windows-luottamusta; online-peruuttamista ei tehdä.
- Käytettävissä on 34 kieltä, mutta äidinkielenään / esteettömyystestaus on edelleen kesken.

<a id="troubleshooting"></a>
## Vianetsintä

| Oire | Toiminta |
| --- | --- |
| Verkkoluettelo ei ole saatavilla | Valitse alkuperäinen paketti [NVIDIA ohjainlataukset](https://www.nvidia.com/en-us/drivers/):stä. Älä korvaa viereistä GPU-mallia. |
| Hotfix-haku ei ole käytettävissä | Käytä [NVIDIA:n Game Ready-ohjainfoorumi](https://www.nvidia.com/en-us/geforce/forums/game-ready-drivers/13/) ja tarkista todellinen paketti. |
| NVIDIA:n asennus epäonnistuu | Lue virheyhteenveto ja avaa yksityiskohtaiset lokit. Valinnaiset komponentit, jotka ovat jo voimassa tai eivät ole käytettävissä, jäävät ohitettaviksi 0.1.4:ssä. Epäonnistuneet asennukset eivät käynnistä valinnaisia ​​säätöjä tai onnistumista/uudelleenkäynnistystä. |
| Allekirjoitus/tiiviste/varmuuskopiointivirhe | Lopeta asennus ja säilytä virhe; hanki alkuperäinen paketti uudelleen, jos se on vioittunut. |
| Vaihtoehto ei ole käytettävissä | Lue sen laitteiston, osan tai kohdeohjaimen syy; pidä se muuttumattomana. |
| Uudelleenkäynnistys tai työ kesken | Käytä työn palautusohjeita ja nimenomaista ansioluetteloa; älä pyyhi sen päiväkirjaa. |
| Palauta konflikti | Toinen tila eroaa tallennetusta tapahtumasta. Säilytä se ja pyydä apua palautuksen pakottamisen sijaan. |

Sisällytä raportteihin valittu työkaluversio, Windows, GPU, ohjain ja toistettavat vaiheet; poistaa polkuja ja henkilötietoja lokeista. [Tuki](../docs/support.md).

<a id="faq"></a>
## FAQ

**Asentaako asennusohjelma grafiikkaohjaimen?** Ei. Tämä vaatii sovelluksen erillisen analyysin, tarkistuksen, vahvistuksen ja laajennetun asennusprosessin.

**Tarvitsenko NVCleanstall:n tai NVPI:n?** Ei. NVCleanstall on vain inspiraatiota. Profile Inspector-kumppani on itsenäinen valinnainen editori.

**Tekeekö se jokaisesta NVIDIA-ohjaimesta pienemmän tai nopeamman?** Ei. Valitut komponentit ja edellytykset määräävät, mikä voi muuttua; mitattua voittoa ei luvata.

**Missä lähteet ovat?** Sovelluskohtaiset lähde- ja yksityiset testit ylläpidetään erikseen. Tämä keskus tarjoaa dokumentaatiota, binaaritiedostoja ja kolmannen osapuolen lähdelinkkejä, joita tarvitaan tekijänmääritykseen/lisensointiin.

<a id="credits-and-upstream"></a>
## Krediitit ja ylävirtaan

Alkuperäinen sovellus, työnkulku, tapahtumat, lokalisointi, bootstrap ja mukautukset: 禅堂 Zendo (RevoluSound Team).

- [NVCleanstall / TechPowerUp](https://www.techpowerup.com/download/techpowerup-nvcleanstall/): työnkulun inspiraatiota; lähdettä tai binaarista ei tuotu.
- [NVIDIA Profile Inspector / Orbmu2k](https://github.com/Orbmu2k/nvidiaProfileInspector): MIT-teemat, laajennettu NVAPI-liittymäviittaus ja erikseen pakattu fork.
- [7-Zip / Igor Pavlov](https://www.7-zip.org/): muokkaamattomat poistotyökalut.
- [Microsoft .NET](https://github.com/dotnet/runtime) ja [WPF](https://github.com/dotnet/wpf): niputettu suoritusaika.
- [Inno Setup](https://jrsoftware.org/isinfo.php): alkuperäinen asennusohjelma ja hyvitetyt käännökset.
- [keylase/nvidia-patch](https://github.com/keylase/nvidia-patch): ulkoinen valinnainen NVENC-tietolähde; jakelulupaa ei ole vahvistettu.
- [NVIDIA](https://www.nvidia.com/en-us/drivers/): ulkoisten ajurien lataukset ja asennetut NVAPI/NVML-kirjastot.

[Koko komponenttitaulukko](../THIRD_PARTY_NOTICES.md) · [Muutokset ja alkuperä](../docs/provenance.md)

<a id="license"></a>
## Lisenssi

[Nykyinen binäärijakeluoikeus](../../../../NVDriverForge/LICENSE) sallii muokkaamattomien virallisten suoritettavien tiedostojen käytön ja jakamisen ilmoitusten kanssa. Sovelluskohtaiset lähdeoikeudet pidätetään. Se ei rajoita erillisten kolmannen osapuolen lisenssien myöntämiä oikeuksia. [Täydelliset ilmoitukset](LICENSES/README.md).

Riippumaton malleista NVIDIA Corporation, TechPowerUp ja keylase; joita he eivät ole sponsoroineet tai virallisesti hyväksyneet. Tuotenimet pysyvät omistajiensa tavaramerkeinä.
