<!-- nv-language-navigation:start -->
🌐 [English](../../../provenance.md) | [Français](../../../provenance.fr.md) · [NV Laboratory](../README.md)

<details>
<summary>🌐 Language · 34</summary>

[العربية](../../ar/docs/provenance.md) · [বাংলা](../../bn/docs/provenance.md) · [简体中文](../../zh/docs/provenance.md) · [Čeština](../../cs/docs/provenance.md) · [Dansk](../../da/docs/provenance.md) · [Nederlands](../../nl/docs/provenance.md) · [English](../../../provenance.md) · [Filipino](../../fil/docs/provenance.md) · **Suomi** · [Français](../../../provenance.fr.md) · [Deutsch](../../de/docs/provenance.md) · [Ελληνικά](../../el/docs/provenance.md) · [हिन्दी](../../hi/docs/provenance.md) · [Magyar](../../hu/docs/provenance.md) · [Bahasa Indonesia](../../id/docs/provenance.md) · [Italiano](../../it/docs/provenance.md) · [日本語](../../ja/docs/provenance.md) · [한국어](../../ko/docs/provenance.md) · [मराठी](../../mr/docs/provenance.md) · [فارسی](../../fa/docs/provenance.md) · [Polski](../../pl/docs/provenance.md) · [Português](../../pt/docs/provenance.md) · [ਪੰਜਾਬੀ](../../pa/docs/provenance.md) · [Română](../../ro/docs/provenance.md) · [Русский](../../ru/docs/provenance.md) · [Español](../../es/docs/provenance.md) · [Kiswahili](../../sw/docs/provenance.md) · [Svenska](../../sv/docs/provenance.md) · [தமிழ்](../../ta/docs/provenance.md) · [ไทย](../../th/docs/provenance.md) · [Türkçe](../../tr/docs/provenance.md) · [Українська](../../uk/docs/provenance.md) · [اردو](../../ur/docs/provenance.md) · [Tiếng Việt](../../vi/docs/provenance.md)

[Translation policy](../../README.md)

</details>
<!-- nv-language-navigation:end -->

<!-- nv-translation-notice:start -->
> Koneavusteinen käännös englannista. Tekniset nimet, komennot, URL-osoitteet ja alkuperäiset lakitekstit säilytetään. Äidinpuhujien arvostelu on tervetullut; katso englanninkielinen viittaus, jos sanamuoto on epäselvä.
<!-- nv-translation-notice:end -->

<a id="provenance-changes-and-licensing"></a>
# Lähde, muutokset ja lisenssit

Tämä tarkastus kuvaa **2026-09-09** valmisteltuja ehdokkaita. Sovelluslähteet pysyvät yksityisinä; julkiset luettelot sisältävät tiedostonimiä ja tiivisteitä, eivät lähdekoodia. Katso [täydelliset komponenttiilmoitukset](../THIRD_PARTY_NOTICES.md).

<a id="nvidia-profile-inspector--nv-tools-fork"></a>
## NVIDIA Profile Inspector – NV Tools Fork

Viite: Orbmu2k/nvidiaProfileInspector commit `592d962cca8827efe8859461a84267755595064a`; ehdokas suoritettava versio 3.0.2.3. Referenssisitoumus ja fork:n kokoonpanoversio ovat eri tunnisteita; fork-versiosta ei päätetä ylävirran julkaisuversiota.

Puhtaan kumppanin 157 lähde-/resurssitiedostoa verrattiin tähän sitoumukseen: 2 tavua identtisiä, 134 eroaa vain rivinpäätteistä tai UTF-8 BOM:sta, 11 modifioitua, 10 puuttuu verratussa ylävirran polussa. "Lisätty" liittyy tähän polkuun, eikä se sinänsä ole todiste alkuperäisestä kirjoittajuudesta.

[Täydellinen tiedosto/hash vertailu](../../../provenance/nvpi-source-provenance.json).

| Alue | Peritty työ | Fork panos |
| --- | --- | --- |
| Profiilieditori | Profiilimalli, tuonti/vienti, sovellusliitokset ja viitetiedot | Integrointi näytön ja ulkoisen työkalun käynnistysohjelman kanssa |
| NVAPI | Orbmu2k:n DRS-yhteensopivuus | Väriin/näyttöön liittyvä yhteensopivuus, tuotannon alkuperäisen latausrajoitukset ja tekosyyn poistaminen |
| Näytä palvelut | Windows/NVIDIA API:t ulkoisina liitäntöinä | DisplayInfoService, DisplayConfigurationService, DisplaySettingsBackend |
| UI | Ylävirran WPF resurssit, paletit ja kuvakkeet | Näyttöikkunat, 15 sekunnin vahvistus, tila/takaisinluku ja työkalupalkin asettelu |
| Käynnistysohjelma | Olemassa oleva sovelluskuori | Suojattu erikseen asennettu RasterPulse-haku ja käynnistys |
| Pakkaus | MIT ylävirtaan | Puhdista itsenäinen kumppani, erillinen asennus-/poistoohjelma, säilytetyt ilmoitukset |

Julkinen lähdekartta sisältää ratkaisu-/resurssipolut jäljitettävyyttä varten; näitä tiedostoja ei jaeta lähteenä. Kehitystestit, valeliitännät ja vanha yhdistetty NVPI/RasterPulse-binaari eivät sisälly.

<a id="nvdriverforge"></a>
## NVDriverForge

Itsenäinen C#/.NET 8/WPF-sovellus; käyttäjälle suunnattu työnkulku on osittain inspiroitunut NVCleanstall:stä. Tuotannon hyötykuormasta ei tunnistettu NVCleanstall-lähdettä/binaaria. Sitä ei esitetä tämän patentoidun sovelluksen fork-tiedostona.

Alkuperäinen projektityö sisältää komponenttien analysoinnin/valinnan, suojatut asennustyöt, varmuuskopiot ja tapahtumien palautuksen, NVIDIA-luetteloiden lataukset, päivitysten tarkistukset, lokalisoidut selitykset, valinnaiset edistyneet/NVENC-työnkulut ja asennusohjelman käynnistyksen.

Perityt/sovitetut komponentit: neljä NVPI-teemapalettia, laajennettu NVAPI DRS-rajapintaviittaus ja erikseen valinnainen MIT NVPI -kumppani. Custom NV-esiasetuksen valintakäyttöliittymä ja sallittujen tapahtumien integrointi kuuluvat NVDriverForge:ään; esiasetus ei ole virallinen NVIDIA-suositus.

7-Zip 26.03, .NET/WPF 8.0.31 ja Inno Setup pysyvät muuttamattomina ulkoisina komponentteina, joita käytetään omien ehtojensa mukaisesti. keylase NVENC-tietoja ei ole upotettu; yksi tarkka sitoumus valitaan ja tarkistetaan, kun käyttäjä pyytää yhteensopivaa latausta. Tälle alkupään datalle ei myönnetty uudelleenjakelulisenssiä.

<a id="nvmfg-unlock40"></a>
## NVMFG Unlock40

NVMFG Unlock40 on kehittänyt itsenäisesti 禅堂 Zendo (RevoluSound Team). Ylläpitäjä käytti RTX40MFG-Unlock vertailua ja tarkennusta varten. Sovellusta kokonaisuutena ei esitetä nimellä fork. Tämä erottelu ei poista krediittejä jaetuista/muokatuista komponenteista nykyisessä alkuperäisessä kerroksessa.

Vertailuviite: dashdogy/RTX40MFG-Unlock, Michael Robles, MIT, sitoa `4e776d068f91b4a665425542bb005dd57cc3d891`. Yksityinen alkuperäisen moottorin puu sisältää 48 verrattua tiedostoa: 35 vain muotoilun eroa, 4 muokattua tiedostoa ja 9 puuttuu viitepolusta. [Täydellinen vertailu](../../../provenance/nvmfg-source-provenance.json).

Muokatut perityt tiedostot: `entry_detour.h`, `patcher.cpp`, `temporal_interval_trace.cpp`, `temporal_interval_trace.h`. Muita polkuja ovat `game_selection.*`, `ngx_bootstrap.*`, `ngx_capability.h`, `presentation_tracker.h`, `vsync_observer.*` ja säilytetty ylävirran lisenssi.

Tuotanto C++ -yksiköt: patcher, midpoint_fix, dlssg_provider_policy, entry_detour, nvidia_mfg_policy, temporal_interval_trace, ngx_bootstrap, game_selection ja vsync_observer; plus entry_detour-kokoonpano ja MinHook puskuri/koukku/trampoliini/HDE64. Peritty ReShade-käyttöliittymä, vanhat välilevyresurssit ja käyttämättömät CMake-kohteet eivät ole osa tätä tuotantokokoelmaa.

Vastaavat komponentit kattavat korjaus-/tarjoajakäytännön ja ajallisen työn; heidän tekijänoikeus- ja lupailmoituksensa säilyvät ennallaan. Keskitetty NGX/bootstrap/ohjainkoordinointi, pelikohtainen V-Sync-käsittely, istunnon diagnostiikka ja Windows-sovellus/SDK/varmuuskopiointityönkulku ovat 禅堂 Zendo (RevoluSound Team):n projektityötä. Yllä olevat määrät kuvaavat tiedostoja, mukaan lukien kolmannen osapuolen ja käyttämättömät tiedostot, eivät tekijän prosenttiosuutta tai kummankaan projektin idean kronologiaa.

Apulainen sovittaa NVPI:n NvapiDrsWrapper:n ja NativeArrayHelper:n erilliseksi kokoonpanoksi projektin luomalla profiililogiikalla. Vanha kehityspolku on poissuljettu. Jaetut perhepaletit ovat peräisin NVPI:stä.

MinHook viite: `8fda4f5481fed5797dc2651cd91e238e9b3928c6`; perityllä käännetyllä osajoukolla ei ole toiminnallisia paikallisia muutoksia vertailussa. Streamline-integrointiotsikot: 2.12; avoimen otsikon lisenssi vahvistettu osoitteessa v2.12.0. NGX-otsikon lähde: NVIDIA/DLSS sitoa `a291cc7d2cc642a51566f3dfd5376f635cd1b284`.

Ehdokasmoottori SHA-256: `0E7FC0277C88B22095B622F6A3CB292EC0C14F7A0253D392502257B75E548890`.

Vaadittu palveluntarjoaja SHA-256 kohteessa engine.json: `C64928FDB7C48A57722EA8EEF2662171EDC323473ADEA66C29A206A23F1A2BED`. Ilmoitettu 310.9-palveluntarjoajaperhe ei ole vaihdettavissa tällä täsmälleen tällä hashilla. Mukana ei ole tarjoajan DLL-tiedostoa tai mallia.

**Erinomainen lisenssikohta:** täydellinen NVIDIA RTX SDK -lisenssi, versio 14. maaliskuuta 2024, sisältää kohdan 4(d) rajoituksen, joka koskee teknisten rajoitusten ohittamista. Tarkastus ei anna lupaa tälle käytölle. MIT-moottorilisenssin säilyttäminen, maksuton oleminen tai muiden modifikaatioiden tarkkaileminen ei ratkaise tätä erillistä ehtoa. Ehdokkaan valmistelu ei ole oikeudellinen hyväksyntä. Alkuperäinen lyhyt otsikkoilmoitus on täydennetty täydellä lisenssillä; sen Windows-1252-teksti on myös luettavissa UTF-8-muodossa, ja alkuperäiset tavut säilyvät.

<a id="nvrasterpulse"></a>
## NVRasterPulse

Itsenäinen RTSS-profiilien hallintaohjelma, joka on kehitetty NVPI-pohjaisessa arkistossa. Perityt MIT-käyttöliittymän resurssit/paletit ja projektin alkuperä säilyvät hyvitettyinä. Tuotantosovellus käyttää nimenomaisesti toimitettua MIT-lisenssiä.

Projektityö: tarkka RTSS-profiilin jäsennys/kirjoitus ja murtokoodaus, varmuuskopiot, ohituksen poisto, uudelleenlataussilta, edellytysten tunnistus, kompakti käyttöliittymä, alustan elinkaari, käynnistyksen hallinta ja lokalisointi. RTSS suorittaa todellisen rajoituksen.

Mukana ei ole RTSS-lähdettä, koukku-DLL-, SDK- tai asennusohjelmaa. Silta kutsuu vientiä olemassa olevassa käyttäjän valitsemassa RTSS-asennuksessa. Tässä paketissa ei ole NVIDIA-ohjainpakettia, alkuperäistä kokeellista rajoitinta, Framepacer-, MinHook-, ReShade- tai DLSS-ajoaikaa.

<a id="assets-generated-data-and-tools"></a>
## Omaisuus, tuotettu data ja työkalut

[Omaisuushyvityksiä](../assets/README.md) tunnistaa olemassa olevat käyttöliittymän esikatselut ja NVPI-asetusvalitsin. Niissä olevat kuvitteelliset arvot on merkitty. Peliä/Nexus-sisältöä, henkilökohtaista profiilia, yksityistä ICC:tä, yrityksen NVIDIA-logoa tai fonttitiedostoa ei kopioida.

NVMFG:ssä perityt luodut pelien yhteensopivuusnimet ovat tunnistusapua, eivät testitodisteita. Luodut asentajaluettelot hyvitetään [kääntäjän huomautuksia](../../../../licenses/INSTALLER-TRANSLATORS.md):ssä. Luodut koontitietueet absoluuttisilla poluilla pysyvät yksityisinä.

Yksityisiin koontityökaluihin kuuluvat .NET SDK/MSBuild, Visual Studio C++/MASM, Windows SDK, PowerShell, Inno Setup ja Python auditointi. Niiden kääntäjiä, otsikoita, testiajoja ja virheenkorjausresursseja ei jaeta. Staattinen vapautus CRT pysyy Microsoft:n sovellettavien työkaluketjun ehtojen alaisena.

<a id="scope-of-verification"></a>
## Vahvistuksen laajuus

Paikallinen tarkastus inventoi kaikki tiedostot kolmessa kehitysjuuressa, mutta jätti pois Git-objektitietokannat ja linkitetyt hakemistokohteet. Aktiivinen lähde/asiakirjat tarkistettiin; historialliset rakennukset inventoitiin ja jätettiin pois. Valitut ZIP-osoitteet ja nykyiset hyötykuormat skannattiin ja tiivistettiin; .NET-paketit purettiin lisätarkastusta varten. Alkutarkastus ei suorittanut tuotetta, asennusohjelmaa, peliä, RTSS-prosessia tai ohjainta.

Myöhempi NVPI-asennusversio 2 korjaa erillisen kielen valinnan jaettujen Inno-säätimien ja käynnistysohjelman avulla. Vaaleat/tummat yksityiset valaisimet vahvistivat hiiren ja näppäimistön navigoinnin ja kaikki 34 selkeää kielikoodia. Varsinainen asennuksen valitsin avattiin yksityiselle työpöydälle, jota ei koskaan näytetä, ja peruutettiin ennen asennusta. Sen seitsemän sovellustiedostoa ja kannettava ZIP ovat ennallaan. NVDriverForge 0.1.3 sisältää korjatun kumppanin ja lähettää edelleen `/LANG`:n.

NVDriverForge 0.1.3 valmistui 2026-09-10. Sen yksityinen vahvistusraportti tallentaa 366 sovellustestiä, 118 kumppanin tarkistusta, 32 määritystarkistusta, 156 alkuperäistä vertailua ja 34 kielen edelleenlähetystapausta. Suojattu komponenttivalinnan korjaus toistettiin alkuperäistä ohjainpakettia vastaan ​​muuttamatta sen hyötykuormaa tai asentamatta ohjainta. Nämä ovat vanhentuneita tuotetiimien tuloksia, eivät tämän dokumentaatiopäivityksen suorittamia testejä tai todisteita onnistuneesta todellisen ohjaimen asennuksesta.

Tämä keskitinpäivitys ei muuta toimivaa sovelluskoodia. Aiemmat sovelluskoonti-/yksikkö-/käyttöliittymätestit ovat vanhentuneita historiallisia todisteita. Tämä ei ole kaikkien kolmannen osapuolen binaarien täydellistä käänteistä suunnittelua tai takuuta kaikilta mahdollisilta salaisuuksilta.
