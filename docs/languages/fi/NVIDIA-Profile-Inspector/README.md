<!-- nv-language-navigation:start -->
🌐 [English](../../../../NVIDIA-Profile-Inspector/README.md) | [Français](../../../../NVIDIA-Profile-Inspector/README.fr.md) · [NV Laboratory](../README.md)

<details>
<summary>🌐 Language · 34</summary>

[العربية](../../ar/NVIDIA-Profile-Inspector/README.md) · [বাংলা](../../bn/NVIDIA-Profile-Inspector/README.md) · [简体中文](../../zh/NVIDIA-Profile-Inspector/README.md) · [Čeština](../../cs/NVIDIA-Profile-Inspector/README.md) · [Dansk](../../da/NVIDIA-Profile-Inspector/README.md) · [Nederlands](../../nl/NVIDIA-Profile-Inspector/README.md) · [English](../../../../NVIDIA-Profile-Inspector/README.md) · [Filipino](../../fil/NVIDIA-Profile-Inspector/README.md) · **Suomi** · [Français](../../../../NVIDIA-Profile-Inspector/README.fr.md) · [Deutsch](../../de/NVIDIA-Profile-Inspector/README.md) · [Ελληνικά](../../el/NVIDIA-Profile-Inspector/README.md) · [हिन्दी](../../hi/NVIDIA-Profile-Inspector/README.md) · [Magyar](../../hu/NVIDIA-Profile-Inspector/README.md) · [Bahasa Indonesia](../../id/NVIDIA-Profile-Inspector/README.md) · [Italiano](../../it/NVIDIA-Profile-Inspector/README.md) · [日本語](../../ja/NVIDIA-Profile-Inspector/README.md) · [한국어](../../ko/NVIDIA-Profile-Inspector/README.md) · [मराठी](../../mr/NVIDIA-Profile-Inspector/README.md) · [فارسی](../../fa/NVIDIA-Profile-Inspector/README.md) · [Polski](../../pl/NVIDIA-Profile-Inspector/README.md) · [Português](../../pt/NVIDIA-Profile-Inspector/README.md) · [ਪੰਜਾਬੀ](../../pa/NVIDIA-Profile-Inspector/README.md) · [Română](../../ro/NVIDIA-Profile-Inspector/README.md) · [Русский](../../ru/NVIDIA-Profile-Inspector/README.md) · [Español](../../es/NVIDIA-Profile-Inspector/README.md) · [Kiswahili](../../sw/NVIDIA-Profile-Inspector/README.md) · [Svenska](../../sv/NVIDIA-Profile-Inspector/README.md) · [தமிழ்](../../ta/NVIDIA-Profile-Inspector/README.md) · [ไทย](../../th/NVIDIA-Profile-Inspector/README.md) · [Türkçe](../../tr/NVIDIA-Profile-Inspector/README.md) · [Українська](../../uk/NVIDIA-Profile-Inspector/README.md) · [اردو](../../ur/NVIDIA-Profile-Inspector/README.md) · [Tiếng Việt](../../vi/NVIDIA-Profile-Inspector/README.md)

[Translation policy](../../README.md)

</details>
<!-- nv-language-navigation:end -->

<!-- nv-translation-notice:start -->
> Koneavusteinen käännös englannista. Tekniset nimet, komennot, URL-osoitteet ja alkuperäiset lakitekstit säilytetään. Äidinpuhujien arvostelu on tervetullut; katso englanninkielinen viittaus, jos sanamuoto on epäselvä.
<!-- nv-translation-notice:end -->

<a id="nvidia-profile-inspector--nv-tools-fork"></a>
# NVIDIA Profile Inspector – NV Tools Fork

**Riippumaton fork [NVIDIA Profile Inspector tekijä Orbmu2k](https://github.com/Orbmu2k/nvidiaProfileInspector):stä, lisätyillä näytön ohjaimilla.** Projektin entinen nimi: **NVPI Custom**.

[Latauksen ja julkaisun tila](../docs/downloads.md#nvidia-profile-inspector) · [Asennus](#installation) · [Ylävirta ja muutokset](#upstream-and-changes) · [Lisenssi](../../../../NVIDIA-Profile-Inspector/LICENSE)

<a id="overview"></a>
## Yleiskatsaus

Sovellus muokkaa NVIDIA-ohjainprofiileja, mukaan lukien sovelluskohtaiset asetukset. Tämä fork lisää myös **Näyttö**-editorin aktiiviselle Windows-näytölle: resoluutio, virkistystaajuus, tulosteen väriasetukset, HDR ja asennetut ICC/WCS-profiiliyhteydet.

Se on tarkoitettu tuomaan liittyvät näytön säätimet profiilieditoriin ja selkeyttämään esikatselu-, vahvistus- ja palautustuloksia. Se ei luo uusia laitteistoominaisuuksia.

Ensimmäinen ehdokas on **3.0.2.3**, joka käyttää puhdistettua itsenäistä kumppaniversiota 9. syyskuuta 2026 alkaen. Sen nykyinen suoritettava tiedosto on edelleen `nvidiaProfileInspector.exe`; asennusohjelmassa ja joissakin sisäisissä tarroissa lukee edelleen `NVPI Custom NV`. Yllä oleva julkinen otsikko identifioi fork:n muuttamatta asennusidentiteettiä tai teeskentelemättä sen olevan Orbmu2k:n virallinen julkaisu.

<a id="features"></a>
## Ominaisuudet

- Nykyinen profiilien selaus, sovellusten yhdistäminen, asetusten muokkaukset ja profiilin tuonti/vienti.
- **Näyttö**-valintaikkuna näytölle, tilalle, Hz:lle, RGB/YCbCr:lle, värisyvyydelle, -alueelle ja kolorimetrialle.
- Windows HDR ohjaa ja asentaa ICC/WCS-yhdistyksen valintaa.
- 15 sekunnin näytön esikatselu, jossa on **Keep** / **Revert** ja aikakatkaisun palautus.
- Mode/HDR muutosten ja raportoitujen palautusvirheiden lukeminen.
- Erillinen raportointi HDR:stä, SDR:stä ACM/WCG:llä ja signaalin värisyvyydestä.
- NVRasterPulse-käynnistysohjelma kelvolliseen erikseen asennettavaan kopioon.

<a id="compatibility"></a>
## Yhteensopivuus

| Vaatimus | Yksityiskohdat |
| --- | --- |
| Järjestelmä | Windows 10/11 x64 yhteensopivalla NVIDIA-ohjaimella |
| Suoritusaika | [.NET Framework 4.8](https://dotnet.microsoft.com/en-us/download/dotnet-framework/net48), toimittaa Windows tai asennettu erikseen |
| Käyttöoikeudet | Editori pyytää järjestelmänvalvojan oikeuksia avattaessa |
| Näytöt | Todelliset tilat ja väriyhdistelmät riippuvat GPU:stä, ohjaimesta, näytöstä, kaapelista ja Windows API:sta |
| Valinnaiset työkalut | NVRasterPulse RTSS-rajojen hallintaan; Näyttöeditoriin ei tarvita sitä eikä RTSS:ää |
| Kielet | Asennus: 34 kielen valitsin. Editori säilyttää nykyisen kielituen. |

Jokaiselle GPU:lle ei ole vahvistettua yleistä ajurin minimi- tai tukimatriisia. Valintaikkunan käytettävissä olevat bpc-vaihtoehdot ovat pyyntöjä, eivät varmennettuja yhdistelmiä. Nykyaikaisilla HDR-ohjaimilla ja vanhemmilla Windows-varasilla on erilaiset ominaisuudet.

<a id="installation"></a>
## Asennus

1. Avaa [lataussivu](../docs/downloads.md#nvidia-profile-inspector) ja tarkista julkaisun tila.
2. Lataa asennusohjelma tai kannettava omaisuus ja vertaa sen SHA-256-tiedostoa julkaisuluetteloon.
3. Suorita asennusta varten `NVPI-CustomNV-3.0.2.3-Setup-r2.exe`, valitse kieli ja seuraa asennusohjelman ohjeita. Se luo oman pikakuvakkeen ja asennuksen poistoohjelman.
4. Kannettavia varten pura koko ZIP uuteen kirjoitettavaan kansioon. Säilytä `Reference.xml`, EXE-kokoonpano ja kaikki ilmoitukset suoritettavan tiedoston vieressä.
5. Käynnistä `nvidiaProfileInspector.exe`.

Pelkkä editorin asentaminen ei käytä profiilia tai asenna GPU-ohjainta. Kumppani asentuu erikseen, ei ota `.nip`-yhteyksiä eikä salli käynnistystä sisäänkirjautumisen yhteydessä. Olemassa olevat binaarit ovat allekirjoittamattomia.

<a id="usage"></a>
## Käyttö

**Asennusohjelman versio 2** lisää saman alkuperäisen 34-kielen valitsimen kuin muut työkalut, jossa on hiiren/näppäimistön navigointi, vaalea/tumma ulkoasu ja peruutus. Valinta koskee asennusta; se ei käännä NVPI-editoria. Eksplisiittinen `/LANG=fr`-argumentti tai hiljainen tila ohittaa valinnan soittajille, jotka jo tarjoavat kielen.

**Ajuriprofiilit:** valitse profiili, vie varmuuskopio, muokkaa sitten vain haluttuja asetuksia ja ota ne käyttöön. Sovellusyhdistykset määrittävät, mikä peli saa profiilin. Tallennettu arvo ei ole todiste siitä, että jokainen ohjain tai peli käyttää sitä.

**Näytön säätimet:** avaa **Näyttö**, valitse näyttö ja pyydetyt arvot ja aloita sitten esikatselu. Tarkista kuva ennen kuin valitset **Säilytä** 15 sekunnin sisällä. Käytä **Palauta**, sulje vahvistus tai anna sen vanhentua pyytääksesi palautusta. Lue kaikki virheviestit: onnistunut API-kutsu ei yksinään ole todiste palautuksesta.

ICC-valinta muuttaa asennetun profiiliyhteyden; se ei luo, kalibroi tai jaa uudelleen ICC-tiedostoa. HDR, ACM/WCG, RGB/YCbCr ja bpc kuvaavat putkilinjan eri näkökohtia. Uutta itsenäistä ACM-kytkintä ei toimiteta.

**NVRasterPulse:** työkalupalkin painike hyväksyy erikseen rekisteröidyn järjestelmän laajuisen asennuksen Ohjelmatiedostojen alla suojatulla omistajuudella ja käyttöoikeuksilla. Tämä korotettu kantoraketti voi hylätä kannettavan kopion tai käyttäjän kirjoitettavan/linkitettävän polun. Avaa siinä tapauksessa NVRasterPulse käyttämällä omaa pikakuvaketta. [Asenna RTSS erikseen](https://www.guru3d.com/download/rtss-rivatuner-statistics-server-download/) käyttääksesi NVRasterPulse:ää.

<a id="screenshots"></a>
## Kuvakaappauksia

![NVPI asennusversion 2 kielivalitsin](../../../../assets/screenshots/nvpi-setup-r2-language.png)

Todellinen asetusvalitsin ranskaksi, otettu erillisen testin aikana ja sitten peruutettu. Tämä näyttää asennusohjelman; editori säilyttää käyttöliittymänsä ja näyttöikkunansa.

<a id="update-and-uninstall"></a>
## Päivitä ja poista asennus

Sulje editori ennen päivittämistä. Säilytä viedyt profiilit ja lataa uusi fork-julkaisu; asentaa saman kumppanitunnuksen päälle tai purkaa kannettavat tiedostot uuteen kansioon. Älä sekoita vanhaa `Reference.xml`:ää uuteen suoritettavaan tiedostoon. Mukana oleva ylävirran päivityksen tarkistuksen esto kuuluu tälle fork:lle.

Käytä asennettua kopiota varten Windows **Installed apps** ja sen asennuksen poistoohjelmaa. Jos kyseessä on kannettava, sulje se ja poista purettu kansio, kun vientisi on turvallista. Editorin poistaminen **ei** kumoa ohjainprofiilin muokkauksia, näyttöasetuksia, NVRasterPulse tai RTSS. Palauta haluamasi asetukset ennen poistamista.

<a id="known-limitations"></a>
## Tunnetut rajoitukset

- 15 sekunnin vahvistus ei ole vartija jokaiselle kuljettajan törmäykselle, sähkökatkolle tai pakkopysäytykselle.
- Jotkut väri/syvyys/päivitysyhdistelmät palauttavat `NVAPI_NOT_SUPPORTED`.
- Ohjelmiston takaisinluku ei mittaa paneelin bittisyvyyttä, värien tarkkuutta tai latenssia.
- Näytön asetukset vaikuttavat nykyiseen Windows-näyttöön; tämä valintaikkuna ei luo pelikohtaisia ​​näytön esiasetuksia.
- Ei suorituskykyä, huijauksen estoa tai yleistä HDR-yhteensopivuustakuuta.

<a id="troubleshooting"></a>
## Vianetsintä

| Oire | Toiminta |
| --- | --- |
| Ajonaikainen virhe käynnistyksen yhteydessä | Tarkista Windows-päivitykset ja .NET Framework 4.8; käytä koko pakettia. |
| Pyydetty näyttötila hylätty | Palauta ja testaa Windows/NVIDIA:n tälle näytölle tarjoamaa tilaa. Lue tarkka virhe ja vältä toistuvia sokea muutoksia. |
| HDR tai väri palaa vanhaan tilaan | Tarkista, onko jokin muu toiminto epäonnistunut ja laukaisiko palautuksen; erottaa HDR ACM:stä. |
| NVRasterPulse-painike hylkää polun | Käynnistä oma pikakuvake; Tämä painike vaatii suojatun järjestelmän laajuisen asennuksen. |
| Muutos säilyy asennuksen poistamisen jälkeen | Palauta viety NVIDIA-profiili tai aiotut Windows-näyttöasetukset; asennuksen poisto ei ole asetusten palautus. |

Katso [jaettu tukiopastus](../docs/support.md) ennen lokien lähettämistä.

<a id="faq"></a>
## FAQ

**Onko tämä virallinen NVIDIA-ohjelmisto vai Orbmu2k:n virallinen versio?** Ei. Se on itsenäinen fork; alkuvaiheen kirjoittaja ja MIT-lisenssi säilyvät hyvitettyinä.

**Tarvitseeko NVDriverForge tämän editorin?** Ei. NVDriverForge:n valinnainen Custom NV-esiasetus käyttää omaa integrointiaan. Editorin asentaminen on erillinen valinta.

**Onko RTSS pakollinen tälle fork:lle?** Ei. RTSS on pakollinen NVRasterPulse:n FPS-rajoittimelle, ei profiilin tai näytön muokkaamiseen.

**Missä lähde on?** Muokattua sovelluslähdettä ylläpidetään yksityisesti. MIT-ilmoitus ja alkupään tietovarasto tarjotaan; MIT ei vaadi muokatun lähteen julkaisemista.

<a id="upstream-and-changes"></a>
## Ylävirta ja muutokset

Ylävirtaan: [Orbmu2k/nvidiaProfileInspector](https://github.com/Orbmu2k/nvidiaProfileInspector), referenssisitoumus `592d962cca8827efe8859461a84267755595064a`. [Alkuperäiset lataukset](https://github.com/Orbmu2k/nvidiaProfileInspector/releases).

Peritty: profiilieditori, NVAPI-yhteensopivuus, viitetiedot, käyttöliittymäresurssit ja teemat. 禅堂 Zendo (RevoluSound Team) lisätyt tai mukautetut näyttöpalvelut, HDR/ICC-tapahtumat, 15 sekunnin vahvistus/takaisinluku, työkalupalkin asettelu ja RasterPulse-käynnistyskäyttäytyminen. Puhdistettu kumppani ei sisällä kehityspiloja/testauspisteitä, se käyttää suojattua ulkoista kantorakettia ja sisältää erillisen asennusohjelman. Vanha yhdistetty NVPI/RasterPulse-kehityspaketti ei ole ehdokas tässä keskittimessä.

[Yksityiskohtainen tiedoston alkuperä](../docs/provenance.md) · [Alkuperäinen fork ilmoitus](../../../../NVIDIA-Profile-Inspector/LICENSES/ORIGINAL-FORK-NOTICE.txt)

<a id="credits-and-license"></a>
## Krediitit ja lisenssi

Tekijänoikeus (c) 2016 Orbmu2k. Mukana toimitettu [MIT-lisenssi](../../../../NVIDIA-Profile-Inspector/LICENSE) säilytetään. Mukautukset ja pakkaus: 禅堂 Zendo (RevoluSound Team). Asennusohjelma käyttää Inno Setup; Windows ja .NET Framework pysyvät ulkoisina. [Täydelliset sovellettavat ilmoitukset](LICENSES/README.md).

Riippumaton, ei sponsoroima, eikä NVIDIA Corporation ole virallisesti hyväksynyt. Tavaramerkit jäävät omistajilleen.
