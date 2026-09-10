<!-- nv-language-navigation:start -->
🌐 [English](../../../installation.md) | [Français](../../../installation.fr.md) · [NV Laboratory](../README.md)

<details>
<summary>🌐 Language · 34</summary>

[العربية](../../ar/docs/installation.md) · [বাংলা](../../bn/docs/installation.md) · [简体中文](../../zh/docs/installation.md) · [Čeština](../../cs/docs/installation.md) · [Dansk](../../da/docs/installation.md) · [Nederlands](../../nl/docs/installation.md) · [English](../../../installation.md) · [Filipino](../../fil/docs/installation.md) · **Suomi** · [Français](../../../installation.fr.md) · [Deutsch](../../de/docs/installation.md) · [Ελληνικά](../../el/docs/installation.md) · [हिन्दी](../../hi/docs/installation.md) · [Magyar](../../hu/docs/installation.md) · [Bahasa Indonesia](../../id/docs/installation.md) · [Italiano](../../it/docs/installation.md) · [日本語](../../ja/docs/installation.md) · [한국어](../../ko/docs/installation.md) · [मराठी](../../mr/docs/installation.md) · [فارسی](../../fa/docs/installation.md) · [Polski](../../pl/docs/installation.md) · [Português](../../pt/docs/installation.md) · [ਪੰਜਾਬੀ](../../pa/docs/installation.md) · [Română](../../ro/docs/installation.md) · [Русский](../../ru/docs/installation.md) · [Español](../../es/docs/installation.md) · [Kiswahili](../../sw/docs/installation.md) · [Svenska](../../sv/docs/installation.md) · [தமிழ்](../../ta/docs/installation.md) · [ไทย](../../th/docs/installation.md) · [Türkçe](../../tr/docs/installation.md) · [Українська](../../uk/docs/installation.md) · [اردو](../../ur/docs/installation.md) · [Tiếng Việt](../../vi/docs/installation.md)

[Translation policy](../../README.md)

</details>
<!-- nv-language-navigation:end -->

<!-- nv-translation-notice:start -->
> Koneavusteinen käännös englannista. Tekniset nimet, komennot, URL-osoitteet ja alkuperäiset lakitekstit säilytetään. Äidinpuhujien arvostelu on tervetullut; katso englanninkielinen viittaus, jos sanamuoto on epäselvä.
<!-- nv-translation-notice:end -->

<a id="installation-guide"></a>
# Asennusopas

Aloita [Lataukset](downloads.md):stä, joka tallentaa julkaisun tilan ja tarkat resurssien nimet. Nämä ovat erillisiä työkaluja: asenna vain tarvitsemasi työkalut.

> **Jos kyseessä on NVRasterPulse, asenna [RTSS Guru3D:ltä](https://www.guru3d.com/download/rtss-rivatuner-statistics-server-download/) ennen profiilinhallinnan avaamista.**
> RTSS on suoritettava rajoitusten soveltamiseksi; se ei sisälly NV Tools:ään.

| Työkalu | Asennettu versio | Kannettava painos | Pääedellytys |
| --- | --- | --- | --- |
| NVIDIA Profile Inspector – NV Tools Fork | NVPI-CustomNV-3.0.2.3-Setup-r2.exe | Pura täydellinen NVPI ZIP | NVIDIA-ohjain ja .NET Framework 4.8 |
| NVDriverForge | NVDriverForge-Setup.exe | NVDriverForge.exe, mukana suoritusaika | Yhteensopiva alkuperäinen NVIDIA-ohjainpaketti asennustoimintoihin |
| NVMFG Unlock40 | NVMFGUnlock40-0.1.1-Setup-x64.exe | Pura täydellinen NVMFG ZIP, säilytä alikansiot | RTX 40, olemassa oleva DLSS FG, tarkka toimittaja ja .NET Framework 4.8 -apuohjelmat |
| NVRasterPulse | NVRasterPulse-0.1-win-x64-Setup.exe | Pura täydellinen RP ZIP | RTSS ja .NET Framework 4.8 |

<a id="download-verify-install"></a>
## Lataa, tarkista, asenna

1. Lataa valitusta julkaistusta julkaisusta sen nimetty sovellussisältö, ilmoitukset ZIP ja SHA256SUMS.txt.
2. Käytä tiedostoa [Esimerkki SHA-256](downloads.md#sha-256) todellisella ladatulla tiedostonimellä.
3. Noudata asennuksessa normaalia asennusohjelmaa. Kannettavan ZIP:n tapauksessa pura kaikki uuteen paikalliseen kirjoitettavaan kansioon; älä juokse ZIP:n sisältä.
4. Avaa sovelluksen oma EXE. Säilytä mukana tulevat lisenssi-/määritys-/datatiedostot.
5. Lue työkalun käyttöohjeet ennen asetusten tai järjestelmätoimintojen käyttöönottoa.

Nykyiset binaarit ovat allekirjoittamattomia. Vastaava hash vahvistaa odotetut tavut; se ei ole tietoturva- tai yhteensopivuusvarmenne. Älä poista Windows-suojauksia käytöstä vain varoituksen poistamiseksi.

NVDF:n tai sen valinnaisen NVPI-kumppanin asentaminen on erillistä GPU-ohjaimen asentamisesta. NVPI-kumppani säilyttää nykyisen sisäisen asennuksen nimensä. Sen korotettu RasterPulse-painike vaatii suojatun järjestelmän laajuisen asennuksen; muut RP-kopiot voidaan avata omilla pikanäppäimillä.

NVMFG on kokeellinen ja siinä on [dokumentoitu NVIDIA SDK lisenssireservi](provenance.md). Mukana ei ole NVIDIA-ohjainta, NGX-toimittajaa/mallia tai pelin Streamline-ajoaikaa. Tietyt SDK-lataukset ja pelipäivitykset ovat erillisiä toimintoja.

<a id="language-and-updates"></a>
## Kieli ja päivitykset

Käytä README:n 34-kielenvalitsinta dokumentaatioon. NVDF:llä, NVMFG:llä ja RP:llä on oma 34-kielinen käyttöliittymäasetus; NVPI säilyttää nykyisen kielituen. Jotkut asentajien tekniset merkkijonot ovat englanninkielisiä.

Säilytä työkalun asennusidentiteetti päivityksen aikana. Sulje se ensin ja säilytä varmuuskopiot. Jos käytät NVMFG:tä, sulje ongelmalliset pelit ja ratkaise odottava profiilin palautus. Käytä kannettaville päivityksille uutta kansiota julkaisujen yhdistämisen sijaan.

<a id="removing-a-tool"></a>
## Työkalun poistaminen

Sovelluksen asennuksen poistaminen ei peruuta automaattisesti sen asetuksia.

- **NVPI:** palauta aiotut profiilit/näyttöasetukset ennen poistamista tarvittaessa.
- **NVDF:** käytä ensin palautusta, jos haluat palauttaa edistyneet/NVENC muutokset. Uninstall jättää näytönohjaimen, asetukset ja varmuuskopiot.
- **NVMFG:** sulje pelit, poista ohjain käytöstä/sulje ohjain, ratkaise NVIDIA-palautus ja palauta haluamasi pelin SDK-varmuuskopiot ennen poistamista.
- **RP:** poista ensin aiotut rajoittimen ohitukset. Uninstall ei poista tallennettuja RTSS-suojuksia tai poista RTSS.

Katso kustakin [projektiopas](../README.md#projects):stä tarkat tietojen sijainnit ja rajoitukset tai [tukea](support.md), jos palautusvaihe epäonnistuu.
