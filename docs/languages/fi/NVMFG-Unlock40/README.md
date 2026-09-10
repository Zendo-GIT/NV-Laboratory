<!-- nv-language-navigation:start -->
🌐 [English](../../../../NVMFG-Unlock40/README.md) | [Français](../../../../NVMFG-Unlock40/README.fr.md) · [NV Laboratory](../README.md)

<details>
<summary>🌐 Language · 34</summary>

[العربية](../../ar/NVMFG-Unlock40/README.md) · [বাংলা](../../bn/NVMFG-Unlock40/README.md) · [简体中文](../../zh/NVMFG-Unlock40/README.md) · [Čeština](../../cs/NVMFG-Unlock40/README.md) · [Dansk](../../da/NVMFG-Unlock40/README.md) · [Nederlands](../../nl/NVMFG-Unlock40/README.md) · [English](../../../../NVMFG-Unlock40/README.md) · [Filipino](../../fil/NVMFG-Unlock40/README.md) · **Suomi** · [Français](../../../../NVMFG-Unlock40/README.fr.md) · [Deutsch](../../de/NVMFG-Unlock40/README.md) · [Ελληνικά](../../el/NVMFG-Unlock40/README.md) · [हिन्दी](../../hi/NVMFG-Unlock40/README.md) · [Magyar](../../hu/NVMFG-Unlock40/README.md) · [Bahasa Indonesia](../../id/NVMFG-Unlock40/README.md) · [Italiano](../../it/NVMFG-Unlock40/README.md) · [日本語](../../ja/NVMFG-Unlock40/README.md) · [한국어](../../ko/NVMFG-Unlock40/README.md) · [मराठी](../../mr/NVMFG-Unlock40/README.md) · [فارسی](../../fa/NVMFG-Unlock40/README.md) · [Polski](../../pl/NVMFG-Unlock40/README.md) · [Português](../../pt/NVMFG-Unlock40/README.md) · [ਪੰਜਾਬੀ](../../pa/NVMFG-Unlock40/README.md) · [Română](../../ro/NVMFG-Unlock40/README.md) · [Русский](../../ru/NVMFG-Unlock40/README.md) · [Español](../../es/NVMFG-Unlock40/README.md) · [Kiswahili](../../sw/NVMFG-Unlock40/README.md) · [Svenska](../../sv/NVMFG-Unlock40/README.md) · [தமிழ்](../../ta/NVMFG-Unlock40/README.md) · [ไทย](../../th/NVMFG-Unlock40/README.md) · [Türkçe](../../tr/NVMFG-Unlock40/README.md) · [Українська](../../uk/NVMFG-Unlock40/README.md) · [اردو](../../ur/NVMFG-Unlock40/README.md) · [Tiếng Việt](../../vi/NVMFG-Unlock40/README.md)

[Translation policy](../../README.md)

</details>
<!-- nv-language-navigation:end -->

<!-- nv-translation-notice:start -->
> Koneavusteinen käännös englannista. Tekniset nimet, komennot, URL-osoitteet ja alkuperäiset lakitekstit säilytetään. Äidinpuhujien arvostelu on tervetullut; katso englanninkielinen viittaus, jos sanamuoto on epäselvä.
<!-- nv-translation-notice:end -->

<a id="nvmfg-unlock40"></a>
# NVMFG Unlock40

**Kokeellinen NVIDIA Multi Frame Generation GeForce RTX 40:lle, keskusohjaimella ja pelikohtaisilla valinnoilla.**

[Lataa 0.1.1 ja tila](../docs/downloads.md#nvmfg-unlock40) · [Asennus](#installation) · [Vastavirtaan](#upstream-and-modifications) · [Lisenssit](LICENSES/README.md)

<a id="overview-and-purpose"></a>
## Yleiskatsaus ja tarkoitus

NVMFG Unlock40 on 禅堂 Zendo (RevoluSound Team):n itsenäisesti kehittämä sovellus. Se yhdistää Windows-ohjaimen, alkuperäisen kerroksen, profiiliapuohjelman ja pelin/Streamline SDK -hallinnan. Se kohdistuu peleihin, joissa on jo integroitu NVIDIA DLSS Frame Generation ja yhteensopivat NVIDIA-ajoajat.

[RTX40MFG-Unlock](https://github.com/dashdogy/RTX40MFG-Unlock):tä kuultiin työn vertailemiseksi ja tarkentamiseksi. Nykyinen natiivitaso sisältää jaettuja ja mukautettuja komponentteja, jotka on merkitty erikseen alla. Tämä viittaus ei tee koko NVMFG-sovelluksesta kyseisen projektin fork.

Se on olemassa kokeellisen MFG-käyttäytymisen koordinoimiseksi keskitetysti, pelikohtaisten valintojen muistamiseksi ja ajonaikaisten päivitysten ja varmuuskopioiden pitämiseksi näkyvissä. Se ei lisää DLSS Frame Generation:ää jokaiseen peliin tai muunna mielivaltaista FSR-toteutusta.

Valmisteltu ehdokas on **0.1.1**, mukaan lukien SDK-luettelon visuaalinen korjaus, joka on tallennettu sisäisesti nimellä UI2. Julkinen versio pysyy 0.1.1; sen tarkat tiivisteet erottavat tämän ehdokkaan vanhemmista paikallisista versioista.

<a id="features"></a>
## Ominaisuudet

- Keskitetty käyttöön-/poisohjaus ja valinnainen Windows alustan käynnistys.
- Pelikohtainen valinta Dynamic MFG, pelin asetusten ja tuettujen kiinteiden kertoimien välillä.
- Erilliset muistetut valinnat havaituille V-Sync päälle/pois -tiloille.
- Dynamic käyttää NVIDIA:n tilaa; se keskeytetään, kun V-Sync on pois päältä, erillisellä pelin sisäisellä/kiinteällä valinnalla.
- Pelivalikon ohjaus ja jatkuvat poissulkemiset; pelit ilman DLSS FG:tä pysyvät hallinnassa.
- Pelien etsintä, yläkansion valinta, haku, ryhmittely ja poistaminen poistamatta pelitiedostoja.
- Streamline SDK lataus/tuonti, vahvistettu paikallinen välimuisti, selkeä valinta, pelikohtainen varmuuskopiointi ja palautus.
- Alkuperäisen palveluntarjoajan vahvistus, istuntokohtainen diagnostiikka, globaali profiilipäiväkirja ja konfliktitietoinen palautus.
- 34 käyttöliittymäkieltä ja neljä teemaa.

FG:n sammuttaminen pelissä pitää sen pois päältä. Kiinteät valinnat 2x - 6x riippuvat pelistä/valikosta/ajoajasta; ne eivät ole lupaus siitä, että jokainen yhdistelmä toimii. Ohjain tarkkailee V-Sync:ää eikä aseta käyttäjälle arvoa V-Sync tai VRR.

<a id="compatibility"></a>
## Yhteensopivuus

| Vaatimus | Yksityiskohdat |
| --- | --- |
| Järjestelmä | Windows 10/11 x64 |
| GPU | GeForce RTX 40 tavoite; ei yleistä GPU-yhteensopivuusvaatimusta |
| Peli | Nykyinen NVIDIA DLSS Frame Generation -integraatio ja tuettu suoritusaika; ei huijauksenvastaista yhteensopivuussertifikaattia |
| Palveluntarjoaja | Ehdokas on kiinnitetty palveluntarjoajaan SHA-256, joka on dokumentoitu tiedostossa [alkuperä](../docs/provenance.md); tuntemattomat tiivisteet hylätään |
| Suoritusaika | Mukana .NET 8/WPF 8.0.30 sovellukselle/agentille; .NET Framework 4.8 profiiliavustajille |
| Käyttöoikeudet | Järjestelmänvalvojan käyttöoikeudet ohjain/profiilitoimintoihin |
| Verkko | Pakollinen valituille virallisille SDK-latauksille; tuotu yhteensopiva SDKs voidaan tallentaa välimuistiin paikallisesti |
| Ulkoiset binaarit | NVIDIA-ohjainta, NGX-toimittajaa/malleja ja Streamline-pelien ajoaikoja ei ole yhdistetty |

Pelkkä versiomerkintä ei riitä: ajuri, palveluntarjoajan hash, peliintegraatio ja todelliset ladatut moduulit ovat tärkeitä. Suojatut tai yhteensopimattomat prosessit voivat kieltäytyä liittämisestä. Sovellusta ei ole suunniteltu välttämään huijaussuojauksia.

<a id="installation"></a>
## Asennus

1. Lue [ehdokkaan asema ja lisenssihuomautus](../docs/downloads.md#nvmfg-unlock40).
2. Lataa `NVMFGUnlock40-0.1.1-Setup-x64.exe` tai `NVMFGUnlock40-0.1.1-Portable-x64.zip`, kun sen julkaisu on saatavilla.
3. Tarkista SHA-256 ja säilytä mukana tulevat ilmoitukset. Asenna .NET Framework 4.8, jos Windows ei vielä tarjoa sitä.
4. Suorita asennusohjelma tai pura **koko** kannettava ZIP-tiedosto kirjoitettavaan paikalliseen kansioon.
5. Käynnistä `NVMFGUnlock40.exe`; Säilytä `agent`, `driver`, `engine` ja `Licenses` toimitetussa asettelussa.

Kansio nimeltä `driver` sisältää käyttäjätilan avustajia, ei ydinohjainta. Älä kopioi vain pääasiallista EXE-tiedostoa tai vaihda palveluntarjoajan tiivistettä pakottaaksesi yhteensopivuuden. Nykyiset EXE-tiedostot ovat allekirjoittamattomia.

<a id="usage"></a>
## Käyttö

1. Aloita ohjaimen ollessa pois käytöstä. Lisää peli tai yläkansio ja valitse todelliset asennukset.
2. Tarkista kunkin pelin MFG-asetukset. Vastaa, mitä sen valikko tarjoaa; vastaus tallennetaan pelikohtaisesti.
3. Valitse Dynamic tai pelin sisäinen asetus maailmanlaajuisesti ja säädä sitten kelvollisia pelikohtaisia valintoja tarpeen mukaan.
4. Ota ohjain käyttöön vain, kun aiot käyttää sitä. Se voi väliaikaisesti muuttaa kuutta maailmanlaajuista NVIDIA-profiiliasetusta palautuspäiväkirjan avulla.
5. Käynnistä kelvollinen peli ja ota sen oma DLSS Frame Generation käyttöön. Noudata kaikkia V-Sync-off-valintapyyntöjä.
6. Käytä poissulkemisia peleissä, joita et halua hallinnoida. Pelin poistaminen tallentaa poissulkemisen ja säilyttää sen tiedostot/varmuuskopiot.
7. Käytä sovelluksen täyttä sulkemis-/poisto- ja palautuskulkua, kun olet valmis.

Pääikkunan sulkeminen voi jättää ohjaimen lokeroon. Peliin jo ladattu DLL pysyy siellä, kunnes peli poistuu; ohjaimen poistaminen käytöstä ei takaa purkamista. Sulje kyseiset pelit ennen huoltoa tai päivityksiä.

**Streamline SDKs:** NVIDIA SDK -sivulla lataa virallinen versio tai tuo yhteensopiva paikallinen SDK. Tuo tallentaa vahvistetun kopion; **Use this version** valitsee sen ja **Uninstall** poistaa välimuistissa olevan kopion. Puuttuvat Streamline DLL -tiedostot voidaan täydentää virallisesta NVIDIA SDK -tiedostosta, jossa lähde näkyy. Tämä ei lataa/korvaa NGX-mallia. Sulje peli, valitse suunniteltu pelipäivitys ja säilytä sen alkuperäinen varmuuskopio. Palauttaaksesi pelitiedostot, käytä sen varmuuskopion palautusta, älä välimuistin Uninstall-painiketta.

<a id="screenshots"></a>
## Kuvakaappauksia

![NVMFG SDK-luettelon esikatselu](../../../../assets/screenshots/nvmfg-0.1.1-sdk-preview.png)

Nykyinen englanninkielinen 0.1.1-liittymän renderöinti esimerkki SDK-inventaariolla. Se ei ole nykyinen versioluettelo tai todiste käynnissä olevasta pelistä. [Kuvan alkuperä](../assets/README.md).

<a id="update-and-uninstall"></a>
## Päivitä ja poista asennus

Sulje ongelmalliset pelit. Poista NVMFG käytöstä/sulje ja ratkaise kaikki odottavat NVIDIA-asetusten palautukset ennen päivittämistä. Asenna seuraava asennusohjelma olemassa olevalla henkilöllisyydellä tai pura uusi kannettava uuteen kansioon; säilyttää tila/varmuuskopiot.

Ennen kuin poistat asennuksen, palauta haluamasi pelin SDK varmuuskopiot ja NVIDIA asetukset sovelluksen kautta, sulje sitten pelit ja sulje ohjain. Käytä Windows **Installed apps** asennusta tai poista suljettu kannettava kansio tarvittavien tiedostojen säilyttämisen jälkeen. Älä poista aktiivista palautuspäiväkirjaa manuaalisesti asennuksen eston poistamiseksi.

Paikalliset pelin ajonaikaiset varmuuskopiot käyttävät `%LOCALAPPDATA%\NvidiaStreamlineMaintenance\Backups`:ää. MFG-asetukset/SDK-tietojen käyttö `%LOCALAPPDATA%\RtxMfg`; istunnon lähtö on sovelluksen vieressä olevan `Sessions`:n alla. Nämä tiedostot voivat sisältää pelipolkuja. Älä julkaise niitä muokkaamattomina.

<a id="known-limitations"></a>
## Tunnetut rajoitukset

- Kokeelliset alkuperäiset korjaustiedostot voivat aiheuttaa kaatumisia tai visuaalisia artefakteja; ratkaisematon Bodycam kaatuminen on kirjattu kehityshistoriaan.
- Hallitut renderöintitestit eivät ole sertifiointi jokaiselle pelille, ajurille tai huijauksen estolle.
- Luodut kehykset eivät luo uusia tulonäytteitä; tämä keskitin ei lupaa mitattua latenssia tai suorituskyvyn lisäystä.
- Useat kehyksen luontityökalut/peittokuvat voivat olla ristiriidassa keskenään. Sovellus raportoi havaitut moduulit todistamatta jokaista rinnakkaiseloa.
- Yhteensopivuusluettelo on tunnistusapu, ei luettelo täysin testatuista peleistä.
- Täydelliset NVIDIA SDK ehdot ja ratkaisemattomat tekniset rajoitukset dokumentoidaan [alkuperä](../docs/provenance.md):ssä.

<a id="troubleshooting"></a>
## Vianetsintä

| Oire | Toiminta |
| --- | --- |
| Palveluntarjoajaa ei tueta | Säilytä alkuperäiset vahvistetut tiedostot. Ilmoita ajurin/palveluntarjoajan versiot ja virhe; älä ohita hash-tarkistusta. |
| Ei DLSS FG:tä pelissä | Valitse vastaus ja jätä peli hallintaan; tämä työkalu ei voi valmistaa tätä integraatiota. |
| Pelin kaatumiset/artefaktit | Lopeta peli, poista NVMFG käytöstä, käytä pelin alkuperäistä ajonaikaista varmuuskopiota, jos sitä on muutettu, ja ilmoita toistettavat tiedot. |
| SDK-luettelo tai lataus ei ole saatavilla | Päivitä ja tarkista virallinen lähde; välimuistissa olevan/tuodun version on silti läpäistävä vahvistus. |
| Odottava NVIDIA-palautus estää poistumisen/päivityksen | Käytä palautusta ja säilytä päiväkirja; konflikteja ei saa ylikirjoittaa sokeasti. |
| Poistettua peliä ei löydetä uudelleen | Sen poissulkeminen on jatkuvaa. Lisää se erikseen, kun haluat, että sitä hallitaan uudelleen. |

[Jaettu tukiopas](../docs/support.md) selittää, mitä raporttiin tulee sisällyttää.

<a id="faq"></a>
## FAQ

**Sisältääkö se NVIDIA DLL:itä tai malleja?** Ei ohjainta, NGX-toimittajaa/mallia tai Streamline-ajoaikaa. Eksplisiittiset SDK-lataukset tulevat NVIDIA:stä.

**Toimiiko Dynamic, kun V-Sync on pois päältä?** Se on jäädytetty tässä tilassa. Valitse pelin sisäinen asetus tai kelvollinen kiinteä kerroin pelin erilliselle tilalle.

**Onko tämä ReShade/OptiScaler/FSR-paketti?** Ei. Niitä ei ole koottu tai toimitettu osana tätä tuotantopakettia.

**Ovatko muokatut lähteet julkisia?** Ei. Käännetyt paketit ja vaaditut krediitit/lisenssit toimitetaan. Tämä ei poista kolmansien osapuolten oikeuksia tai rajoituksia.

<a id="upstream-and-modifications"></a>
## Ylävirta ja muutokset

Vertailuviite ja jaetut natiivikomponentit: **RTX40MFG-Unlock, Michael Robles / dashdogy**, viitesitoumus `4e776d068f91b4a665425542bb005dd57cc3d891`, MIT. [Arkisto](https://github.com/dashdogy/RTX40MFG-Unlock) · [Alkuperäiset lataukset](https://github.com/dashdogy/RTX40MFG-Unlock/releases).

Lähdevertailu tunnistaa jaetut korjaukset, palveluntarjoajan/käytännön käsittelyn, ajalliset korjaukset ja MinHook-pohjaiset kiertotiekomponentit. Heidän MIT- ja BSD-ilmoituksensa säilytetään. Täydellinen vertailu sisältää myös tuotantokohteen ulkopuoliset tiedostot.

禅堂 Zendo (RevoluSound Team) on kehittänyt työpöytäsovelluksen, ohjaimen ja SDK-hallintatyönkulun. Projektityö sisältää keskitetyn latauksen, NGX bootstrap -integroinnin, varmennetun palveluntarjoajan valinnan, pelin/V-Sync koordinoinnin ja istuntojen diagnosoinnin. Lähde-opas erottaa nämä työt jaetuista komponenteista; tiedostovertailu ei yksin pysty selvittämään, milloin kummallakaan kirjoittajalla oli idea.

Profiiliapulainen mukauttaa MIT NVAPI -kääreen Orbmu2k:n Profile Inspector:stä. [Yksityiskohtainen alkuperä ja komponenttien laajuus](../docs/provenance.md).

<a id="credits-and-license"></a>
## Krediitit ja lisenssi

Michael Robles; Orbmu2k; Tsuda Kageyu- ja HDE-avustajat; NVIDIA Corporation; Microsoft ja avustajat; Inno Setup kirjoittajat ja kääntäjät. Sovelluskehitys, integraatiot ja pakkaus: 禅堂 Zendo (RevoluSound Team).

[olemassa oleva käännetyn paketin jakamisoikeus](../../../../NVMFG-Unlock40/LICENSE) ja kaikki [komponenttilisenssit](LICENSES/README.md) säilytetään. Ylävirran koodin MIT-oikeudet eroavat NVIDIA SDK -ehdoista. Mikään yleislisenssi ei korvaa niitä.

Riippumaton, ei sponsoroima, eikä NVIDIA Corporation ole virallisesti hyväksynyt. Kaikki viitatut tavaramerkit ovat omistajiensa omaisuutta.
