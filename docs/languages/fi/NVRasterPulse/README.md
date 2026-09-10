<!-- nv-language-navigation:start -->
🌐 [English](../../../../NVRasterPulse/README.md) | [Français](../../../../NVRasterPulse/README.fr.md) · [NV Laboratory](../README.md)

<details>
<summary>🌐 Language · 34</summary>

[العربية](../../ar/NVRasterPulse/README.md) · [বাংলা](../../bn/NVRasterPulse/README.md) · [简体中文](../../zh/NVRasterPulse/README.md) · [Čeština](../../cs/NVRasterPulse/README.md) · [Dansk](../../da/NVRasterPulse/README.md) · [Nederlands](../../nl/NVRasterPulse/README.md) · [English](../../../../NVRasterPulse/README.md) · [Filipino](../../fil/NVRasterPulse/README.md) · **Suomi** · [Français](../../../../NVRasterPulse/README.fr.md) · [Deutsch](../../de/NVRasterPulse/README.md) · [Ελληνικά](../../el/NVRasterPulse/README.md) · [हिन्दी](../../hi/NVRasterPulse/README.md) · [Magyar](../../hu/NVRasterPulse/README.md) · [Bahasa Indonesia](../../id/NVRasterPulse/README.md) · [Italiano](../../it/NVRasterPulse/README.md) · [日本語](../../ja/NVRasterPulse/README.md) · [한국어](../../ko/NVRasterPulse/README.md) · [मराठी](../../mr/NVRasterPulse/README.md) · [فارسی](../../fa/NVRasterPulse/README.md) · [Polski](../../pl/NVRasterPulse/README.md) · [Português](../../pt/NVRasterPulse/README.md) · [ਪੰਜਾਬੀ](../../pa/NVRasterPulse/README.md) · [Română](../../ro/NVRasterPulse/README.md) · [Русский](../../ru/NVRasterPulse/README.md) · [Español](../../es/NVRasterPulse/README.md) · [Kiswahili](../../sw/NVRasterPulse/README.md) · [Svenska](../../sv/NVRasterPulse/README.md) · [தமிழ்](../../ta/NVRasterPulse/README.md) · [ไทย](../../th/NVRasterPulse/README.md) · [Türkçe](../../tr/NVRasterPulse/README.md) · [Українська](../../uk/NVRasterPulse/README.md) · [اردو](../../ur/NVRasterPulse/README.md) · [Tiếng Việt](../../vi/NVRasterPulse/README.md)

[Translation policy](../../README.md)

</details>
<!-- nv-language-navigation:end -->

<!-- nv-translation-notice:start -->
> Koneavusteinen käännös englannista. Tekniset nimet, komennot, URL-osoitteet ja alkuperäiset lakitekstit säilytetään. Äidinpuhujien arvostelu on tervetullut; katso englanninkielinen viittaus, jos sanamuoto on epäselvä.
<!-- nv-translation-notice:end -->

<a id="nvrasterpulse"></a>
# NVRasterPulse

**Sovelluskohtaiset FPS-rajoitukset RivaTuner Statistics Server:n asti.**

> **Asenna ensin RTSS.** NVRasterPulse vaatii [RivaTuner Statistics Server (RTSS), ladattu Guru3D:stä](https://www.guru3d.com/download/rtss-rivatuner-statistics-server-download/):n. RTSS:n on oltava käynnissä rajoitusten pakottamiseksi. Mukana ei ole RTSS-asennusohjelmaa, koukku-DLL- tai SDK-tiedostoa.

[Lataa 0.1 ja tila](../docs/downloads.md#nvrasterpulse) · [Asennus](#installation) · [Miten rajat toimivat](#usage) · [Lisenssi](../../../../NVRasterPulse/LICENSE)

<a id="overview-and-purpose"></a>
## Yleiskatsaus ja tarkoitus

NVRasterPulse on kompakti Windows-liitäntä RTSS-kehysrajojen hallintaan suoritettavan nimen perusteella. RTSS suorittaa rajoituksen. NVRasterPulse hallitsee vastaavia profiiliarvoja, varmuuskopioita ja uudelleenlatauspyyntöjä tarjottimen käytön ja pysyvien valintojen avulla.

Se on olemassa, jotta tarkkoja pelikohtaisia rajoja olisi helpompi muokata ilman, että koko RTSS-profiilia vaihdetaan tai sen peittoasetuksia häiritään. Nykyinen **0.1**-ehdokas on 9. syyskuuta 2026 tehty koontiversio, jossa on vaadittu RTSS-asennustarkistus.

<a id="features"></a>
## Ominaisuudet

- Valitse käynnissä oleva sovellus tai lisää sen suoritettava tiedosto manuaalisesti.
- Tallenna FPS-rajat 1–1000, enintään kolmella desimaalilla.
- Syötettyjen arvojen tarkka rationaalinen koodaus: 59.94 muuttuu 2997/50.
- Front Edge Sync -määritys (`SyncLimiter=1`) aktiivisella odotuksella (`PassiveWait=0`).
- Suoritettavan profiilin päivitykset, automaattiset varmuuskopiot ja atomikirjoitukset.
- Rajoittimen ohitusten poistaminen säilyttäen samalla profiilin muun sisällön.
- RTSS asennuksen tunnistus, manuaalinen polun valinta ja selkeä käynnistys/uudelleenlataus.
- Yksittäisen lokeron käyttö, valinnainen asennettu käynnistys, 34 kieltä ja neljä teemaa.
- Erottele normaali lopetus ja **Lopeta + RTSS** -toiminnot.

<a id="compatibility"></a>
## Yhteensopivuus

| Vaatimus | Yksityiskohdat |
| --- | --- |
| Järjestelmä | Windows 10/11 x64 |
| Suoritusaika | [.NET Framework 4.8](https://dotnet.microsoft.com/en-us/download/dotnet-framework/net48), asennetaan tarvittaessa erikseen |
| Vaadittu ohjelmisto | RTSS ja `RTSS.exe`, vastaava `Profiles`-hakemisto ja yhteensopiva profiili/uudelleenlataustuki |
| GPU | RTSS-yhteensopivuus määrittää rajoittimen; tämä profiilinhallinta ei vaadi tiettyä RTX-sukupolvea |
| Käyttöoikeudet | Nykyinen sovellus pyytää järjestelmänvalvojan käyttöoikeuksia; valitun RTSS-profiilikansion on oltava käytettävissä |
| Pelit | Riippuu RTSS kytkentätuesta ja kunkin pelin rajoituksista; ei huijauksen vastaista takuuta |

Mitään erityistä RTSS-minimiversiota ei ole sertifioitu jokaiselle toiminnolle tällä keskittimen tarkastuksella. Käytä virallista nykyistä jakelua ja ilmoita tarkka versio, jos profiiliavain/uudelleenlataus ei toimi. Asennettu mutta pysäytetty RTSS läpäisee asennustarkistuksen; se on sitten käynnistettävä varsinaista rajoittamista varten.

<a id="installation"></a>
## Asennus

1. **[Lataa ja asenna RTSS Guru3D:stä](https://www.guru3d.com/download/rtss-rivatuner-statistics-server-download/).**
2. Avaa [NVRasterPulse lataukset](../docs/downloads.md#nvrasterpulse) ja tarkista Julkaisun saatavuus.
3. Lataa `NVRasterPulse-0.1-win-x64-Setup.exe` tai `NVRasterPulse-0.1-win-x64-portable.zip` sekä ilmoitukset/tarkistussummat.
4. Vertaa SHA-256. Suorita asennusohjelma tai pura koko kannettava ZIP-tiedosto kirjoitettavaan paikalliseen kansioon.
5. Avaa `NVRasterPulse.exe`. Jos RTSS puuttuu, käytä **Lataa RTSS**, asenna se ja sitten **Tarkista uudelleen** tai valitse `RTSS.exe` manuaalisesti.
6. Käynnistä RTSS käyttämällä sen normaalia pikakuvaketta tai NVRasterPulse:n RTSS-painiketta, jos se on pysäytetty.

Valinnaisen muistutuksen poistaminen käytöstä ei ohita edellytysten tarkistusta. Hiljainen Windows lokeron käynnistys odottaa, kunnes pääikkuna avautuu ennen tämän tarkistuksen näyttämistä. Asennus asentaa vain NVRasterPulse:n. Sen EXE-tiedostot ovat allekirjoittamattomia.

<a id="usage"></a>
## Käyttö

1. Valitse aiottu käynnissä oleva sovellus tai selaa sen peliin EXE.
2. Anna raja väliltä 1–1000 FPS, mukaan lukien tarvittaessa murto-osa.
3. Tallenna ja tarkista raportoitu tulos. NVRasterPulse päivittää kyseisen suoritettavan tiedoston RTSS-profiilin ja pyytää uudelleenlatausta.
4. Varmista, että RTSS on käynnissä ja tarkista toiminta aiotussa pelissä.

Profiilit avataan **suoritettavalla nimellä**, kuten `Game.exe.cfg`. Kahdella eri kansiolla, jotka sisältävät `Game.exe`:n, on sama RTSS-profiili. koko polun tallentaminen ei poista tätä törmäystä.

Tallennus käyttää Front Edge Synciä ja aktiivista odotusta. Aktiivinen odotus voi lisätä CPU:n käyttöä. Vaihtoehtoiset `LimitTime`-kentät neutraloidaan. Olemassa olevat kommentit, peittoasetukset ja `EnableHooking=0` säilytetään. RTSS Global -profiilia ei ole muutettu.

Käytä roskakoritoimintoa poistaaksesi NVRasterPulse:n rajoittimen ohitukset. Se ei poista koko RTSS-profiilia. RTSS Globalilta tai muulta työkalulta peritty raja saattaa silti olla voimassa myöhemminkin.

**Sulkeminen ja lopettaminen:** pääikkuna voi piiloutua lokeroon. Normaali **Lopeta** jättää RTSS:n käynnissä ja tallennetut rajat ennalleen. **Lopeta + RTSS** pyytää normaalia vastaavan RTSS-prosessin sulkemista nykyisessä istunnossa, odottaa enintään kahdeksan sekuntia eikä pakota sitä. Tallennetut rajat säilyvät molemmissa tapauksissa.

Kieli ja teema valitaan sovelluksessa. Käynnistys Windows-kirjautumisen yhteydessä on valinnainen ja tarkoitettu asennetulle kopiolle. Tietopainike selittää yleiset toimet.

<a id="screenshots"></a>
## Kuvakaappauksia

![NVRasterPulse pääikkunan esikatselu](../../../../assets/screenshots/nvrasterpulse-0.1-preview.png)

Olemassa oleva ranskalainen 0.1-käyttöliittymän renderöinti, jossa on esimerkkisuoritettavat nimet ja 176 FPS-arvo. RTSS näytetään pysäytettynä; tämä on käyttöliittymäkuvaus, ei käyntirajoitin tai latenssimittaus. [Kuvan alkuperä](../assets/README.md).

<a id="update-and-uninstall"></a>
## Päivitä ja poista asennus

Lopeta NVRasterPulse, lataa ja vahvista uusi versio ja suorita sen asennusohjelma tai pura kannettava laite uuteen kansioon. Säilytä asetukset ja RTSS-varmuuskopiot. RTSS-päivitykset ovat erillisiä ja tulevat Guru3D:ltä.

Jos haluat poistaa asennetun kopion, käytä Windows **Installed apps**. Jos kyseessä on kannettava, lopeta ja poista purettu kansio, kun varmuuskopiosi ovat turvallisia. Tallennettuja RTSS rajoituksia ei poisteta poistamalla NVRasterPulse: poista ensin aiotut rajoittimen ohitukset. RTSS:llä on oma asennuksen poisto.

Paikallinen osavaltio: `%LOCALAPPDATA%\NVRasterPulse`. Automaattiset RTSS-varmuuskopiot: `%LOCALAPPDATA%\NVRasterPulse\Backups\RTSS`. Vanhempi `%LOCALAPPDATA%\RTSSProfileBridge`-sijainti voidaan lukea siirtoa varten. Nämä tiedostot voivat sisältää henkilökohtaisia ​​suoritettavia polkuja, eikä niitä tule julkaista julkisesti.

<a id="known-limitations"></a>
## Tunnetut rajoitukset

- RTSS suorittaa korkin. Tallennettu arvo tai onnistunut uudelleenlatauspyyntö ei ole mitattu kehysaikatulos.
- Samannimiset suoritettavat tiedostot jakavat profiilin.
- Toinen globaali/pelikohtainen rajoitin voi vaikuttaa tulokseen; paikallisen ohituksen poistaminen käytöstä ei poista perittyä ylärajaa.
- Tarkoituksella poistettu RTSS-koukku pysyy poissa käytöstä.
- Aktiivisella odotuksella on CPU/teho-vaihto.
- Ei universaalia peliä, huijauksen estoa tai päästä päähän -latenssin validointia.
- Aikaisempaa kokeellista riippumatonta rajoitinmoottoria ei ole koottu tai toimitettu.
- Automaattiset varmuuskopiot eivät tarkoita yhden napsautuksen täydellistä varmuuskopiointi-palautusliittymää.

<a id="troubleshooting"></a>
## Vianetsintä

| Oire | Toiminta |
| --- | --- |
| RTSS-edellytys on avoinna | Valitse todellinen `RTSS.exe` ja vastaava Profiilit-kansio ja tarkista sitten uudelleen. |
| Rajoitus tallennettu, mutta ei vaikutusta | Käynnistä RTSS; Tarkista oikea pelin EXE/profiili, koukkuluvat ja muut rajoittimet. |
| Tallennus epäonnistuu | Tarkista kansion käyttöoikeudet ja säilytä näytetty virhe/varmuuskopio. |
| Raja jää pois poistamisen jälkeen | Tarkista RTSS Global ja muut työkalut; roskakoritoiminto poistaa vain paikallisen rajoittimen ohitukset. |
| Kaksi peliä saavat saman rajan | Tarkista, ovatko niiden suoritettavat tiedostonimet identtiset. |
| Lopeta + RTSS jättää RTSS auki | Sulje RTSS normaalisti itse; tämä komento välttää tarkoituksella pakotetun lopettamisen. |

Jos palautat RTSS-varmuuskopion manuaalisesti, sulje RTSS ensin ja säilytä nykyinen profiili ennen kuin korvaat sen aiotulla varmuuskopiolla. Tämä voi korvata asiaankuulumattomat profiilimuokkaukset; tarkista tiedosto ja päivämäärä. [Jaettu tuki](../docs/support.md).

<a id="faq"></a>
## FAQ

**Tarvitsenko myös MSI Afterburnerin?** NVRasterPulse vaatii RTSS; se ei riipu Afterburner-sovelluksesta. Noudata RTSS-jakelijan asennusvaihtoehtoja.

**Voinko käyttää tätä ilman, että RTSS on käynnissä?** Voit hallita profiileja, kun asennus havaitaan, mutta RTSS:n on suoritettava rajoittamista varten.

**Poistaako asennuksen lopettaminen tai poistaminen suojukset?** Ei. Poista halutut rajoittimen ohitukset nimenomaisesti ennen NVRasterPulse:n poistamista.

**Onko se fork ja RTSS?** Ei. Se on itsenäinen profiilinhallinta; RTSS-lähdettä tai suoritettavaa tiedostoa ei ole sisällytetty.

<a id="upstream-modifications-and-credits"></a>
## Ylävirta, muutokset ja hyvitykset

Kehitystietovarasto on peräisin [Orbmu2k's NVIDIA Profile Inspector](https://github.com/Orbmu2k/nvidiaProfileInspector):stä. Sen MIT-paletit/käyttöliittymäresurssit hyvitetään. Profiilinhallintapalvelut, murtokoodaus, varmuuskopiot, RTSS-uudelleenlataussilta, lokeron toiminta, edellytysopas, kielet ja sovelluskohtainen kuvake kehitti/sovitti 禅堂 Zendo (RevoluSound Team).

RTSS:n on kehittänyt **Unwinder** ja se jaetaan erikseen Guru3D:n kautta. NVRasterPulse kutsuu `UpdateProfiles` valitusta asennetusta hook DLL:stä; ei RTSS SDK tai koukkubinaaria jaetaan uudelleen. Asennusohjelma käyttää muokkaamatonta Inno Setup 7.1.0 mukautettuja komentosarjoja/käännöksiä ja projektin käynnistysohjelmaa.

[Täysi alkuperä](../docs/provenance.md) · [Kolmannen osapuolen pöytä](../THIRD_PARTY_NOTICES.md)

<a id="license"></a>
## Lisenssi

Paketti jakaa nimenomaisesti NVRasterPulse:n toimitetun [MIT-lisenssi](../../../../NVRasterPulse/LICENSE):n alla, säilyttäen tekijänoikeudet (c) 2016 Orbmu2k. Sovelluslähdettä ylläpidetään yksityisesti; MIT ei vaadi muokatun lähteen julkaisemista. RTSS ja Windows/.NET pysyvät omilla ehdoillaan. [Täydelliset ilmoitukset](LICENSES/README.md).

Riippumaton malleista NVIDIA Corporation, MSI ja RTSS; joita he eivät ole sponsoroineet tai virallisesti hyväksyneet. Tuotenimet pysyvät omistajiensa tavaramerkeinä.
