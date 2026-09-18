<!-- nv-language-navigation:start -->
🌐 [English](../../../support.md) | [Français](../../../support.fr.md) · [NV Laboratory](../README.md)

<details>
<summary>🌐 Language · 34</summary>

[العربية](../../ar/docs/support.md) · [বাংলা](../../bn/docs/support.md) · [简体中文](../../zh/docs/support.md) · [Čeština](../../cs/docs/support.md) · [Dansk](../../da/docs/support.md) · [Nederlands](../../nl/docs/support.md) · [English](../../../support.md) · [Filipino](../../fil/docs/support.md) · **Suomi** · [Français](../../../support.fr.md) · [Deutsch](../../de/docs/support.md) · [Ελληνικά](../../el/docs/support.md) · [हिन्दी](../../hi/docs/support.md) · [Magyar](../../hu/docs/support.md) · [Bahasa Indonesia](../../id/docs/support.md) · [Italiano](../../it/docs/support.md) · [日本語](../../ja/docs/support.md) · [한국어](../../ko/docs/support.md) · [मराठी](../../mr/docs/support.md) · [فارسی](../../fa/docs/support.md) · [Polski](../../pl/docs/support.md) · [Português](../../pt/docs/support.md) · [ਪੰਜਾਬੀ](../../pa/docs/support.md) · [Română](../../ro/docs/support.md) · [Русский](../../ru/docs/support.md) · [Español](../../es/docs/support.md) · [Kiswahili](../../sw/docs/support.md) · [Svenska](../../sv/docs/support.md) · [தமிழ்](../../ta/docs/support.md) · [ไทย](../../th/docs/support.md) · [Türkçe](../../tr/docs/support.md) · [Українська](../../uk/docs/support.md) · [اردو](../../ur/docs/support.md) · [Tiếng Việt](../../vi/docs/support.md)

[Translation policy](../../README.md)

</details>
<!-- nv-language-navigation:end -->

<!-- nv-translation-notice:start -->
> Koneavusteinen käännös englannista. Tekniset nimet, komennot, URL-osoitteet ja alkuperäiset lakitekstit säilytetään. Äidinpuhujien arvostelu on tervetullut; katso englanninkielinen viittaus, jos sanamuoto on epäselvä.
<!-- nv-translation-notice:end -->

<a id="compatibility-and-troubleshooting"></a>
# Yhteensopivuus ja vianetsintä

Nämä ovat valmisteltuja ehdokkaita, eivät sertifiointimatriisia kaikille Windows, GPU, ohjain- ja peliyhdistelmille.

| Työkalu | Windows / suoritusaika | Laitteisto/ulkoinen riippuvuus | Hoitoa vaativat toimenpiteet |
| --- | --- | --- | --- |
| NVPI fork 3.0.2.3 | Windows 10/11 x64, .NET Framework 4.8 | Yhteensopiva NVIDIA-ohjain/näyttö | Profiili kirjoittaa ja näyttää esikatselut |
| NVDriverForge 0.1.4 | Windows 10 build 19041+ / 11 x 64; Mukana .NET/WPF | Yhteensopiva NVIDIA-ohjainpaketti | Edistynyt asennus, lisäasetukset, valinnainen NVENC |
| NVMFG Unlock40 0.2.3 | Windows 10/11 x64; Mukana .NET/WPF, Framework 4.8 -apuohjelmat | RTX 40, kelvollinen DLSS FG -peli ja kiinnitetty tarjoaja | Alkuperäinen pelin sisäinen korjaustiedosto, globaali profiilipäiväkirja, SDK-pelipäivitykset |
| NVRasterPulse 0.2 | Windows 10/11 x64, .NET Framework 4.8 | RTSS asennettu; juoksevat lippikset | RTSS suoritettavan profiilin muutokset |

ARM64-pakettia ei ole valmisteltu. Näytön/sovellusliittymän saatavuus ja vanhat Windows-versiot voivat rajoittaa yksittäisiä ominaisuuksia. Yleistä NVIDIA- tai RTSS-minimiversiota ei ole keksitty. Tarkka NVMFG-palveluntarjoajan hash on [alkuperä](provenance.md):ssä.

<a id="before-reporting-a-bug"></a>
## Ennen kuin ilmoitat virheestä

Tunnista tarkka suoritettava tiedosto/versio, jonka avasit. Aiempi asennettu kopio ei välttämättä ole juuri ladatun ZIP-tiedoston versio. Tallenna jäljentämisvaiheet, odotettu tulos ja todellinen tulos. Renderöinti-/rajoitusongelmia varten sisällytä pelin versio, näytön päivitys, FG/V-Sync/VRR tila ja mikä tahansa muu rajoitin tai peitto.

Käytä [bugi muoto](https://github.com/Zendo-GIT/NV-Laboratory/issues/new?template=bug-report.yml). Älä koskaan liitä kokonaista yksityistä kehityskansiota, ohjainarkistoa, mallia, pelin DLL-tiedostoa, rekisterivedostetta tai tarkistamatonta lokikokoelmaa.

| Ongelma | Ensimmäiset tarkastukset |
| --- | --- |
| Väärä sovellusversio | Vahvista EXE-identiteetti ja vapauta hash; sulje vanhempi kopio ennen vaihtamista. |
| Suoritusaika/käynnistysvirhe | Asenna tarvittava Framework 4.8 tai säilytä kaikki mukana toimitetut kannettavat alikansiot. |
| UAC peruutettu | Yritä uudelleen vain aiottua toimintoa; peruutus ei ole onnistunut asennus. |
| Hash/allekirjoitus ei täsmää | Lopeta kyseisen ehdokkaan käyttö ja hanki odotetut viralliset tavut. |
| NVPI väri/tila hylätty | Palauta ja käytä todellisen näytön/ohjaimen tukemaa yhdistelmää. |
| NVDF varmuuskopiointi- tai palautusvirhe | Säilytä suojattu työ ja RECOVERY.txt; älä pyyhi päiväkirjaa tai pakota ristiriitaisia ​​kirjoituksia. |
| NVMFG odottavat asetukset | Ratkaise palautus sulkemalla pelejä, säilyttäen muiden työkalujen muutokset. |
| RP-korkilla ei ole vaikutusta | Suorita RTSS, tunnista todellinen pelin EXE, tarkista koukun tila ja kilpailevat rajat. |
| RP-suojus säilyy poiston jälkeen | Tarkista RTSS Global; poisto muuttaa vain paikallisen rajoittimen ohituksia. |

NVDriverForge tarjoaa esikatseltavissa olevan paikallisen JSON-raportin; NVMFG tarjoaa diagnostiikkaa Tietoja. Suosi nämä suodatetut raportit täydelliseen lokiarkistoon ja tarkista ne ennen jakamista. NVMFG:ssä 0.1.1 raportoidulle palautustukokselle ei vieläkään ole vahvistettua syytä; säilyttää päiväkirjansa ja kirjata kaikki saatavilla olevat virhekoodit. NVRasterPulse 0.2 tarjoaa määritysdiagnostiikkaa toimintovalikossaan ilman FPS:n mittausta.

<a id="logs-and-privacy"></a>
## Lokit ja yksityisyys

| Työkalu | Paikalliset tiedot tarkistettavaksi, ei tukkumyyntiin |
| --- | --- |
| NVDF | `%LOCALAPPDATA%\NVDriverForge`; suojatut työt `%PROGRAMDATA%\NVDriverForge\Jobs` |
| NVMFG | `%LOCALAPPDATA%\RtxMfg`; varmuuskopiot `%LOCALAPPDATA%\NvidiaStreamlineMaintenance\Backups`; `Sessions` EXE:n vieressä |
| RP | `%LOCALAPPDATA%\NVRasterPulse`; `Backups\RTSS` sen alla |
| NVPI | Valitsemasi viennit ja näytettävä virhe; ei keksittyä yleistä hirsipolkua |

Poista tilien nimet, kotihakemistot, pelikirjaston polut, laitetunnisteet, tunnukset ja asiaankuulumattomat ikkunat jakamastasi tekstistä/kuvista. Säilytä alkuperäiset yksityisesti palautusta varten. Julkiset aiheet ovat kaikkien nähtävillä.

Jos kyseessä on haavoittuvuus, vaarallinen käyttöoikeus tai tahaton tuhoava toiminta, seuraa [SECURITY.md](../SECURITY.md)-koodia sen sijaan, että julkaiset tietoja julkisesti.

<a id="what-has-been-verified"></a>
## Mikä on varmistettu

Keskittimen valmistelua varten suoritettiin staattiset hyötykuorman/ZIP/hash/metadatan skannaukset ja dokumentaatiotarkistukset. Nykyiset yksityiset sovelluskoonti-/yksikkö-/käyttöliittymätestit ovat historiallisia, vanhentuneita todisteita. Tämän valmistelun aikana ei suoritettu ohjaimen asennusta, näytön vaihtoa, live RTSS -toimintoa tai pelien vertailua.

"Havaittu", "kirjoitettu", "uudelleenladattu", "ominaisuus käytettävissä" ja "mitattu pelissä" ovat eri tuloksia. Ilmoita kumman olet havainnut.
