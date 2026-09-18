<!-- nv-language-navigation:start -->
🌐 [English](../../../installation.md) | [Français](../../../installation.fr.md) · [NV Laboratory](../README.md)

<details>
<summary>🌐 Language · 34</summary>

[العربية](../../ar/docs/installation.md) · [বাংলা](../../bn/docs/installation.md) · [简体中文](../../zh/docs/installation.md) · [Čeština](../../cs/docs/installation.md) · [Dansk](../../da/docs/installation.md) · [Nederlands](../../nl/docs/installation.md) · [English](../../../installation.md) · **Filipino** · [Suomi](../../fi/docs/installation.md) · [Français](../../../installation.fr.md) · [Deutsch](../../de/docs/installation.md) · [Ελληνικά](../../el/docs/installation.md) · [हिन्दी](../../hi/docs/installation.md) · [Magyar](../../hu/docs/installation.md) · [Bahasa Indonesia](../../id/docs/installation.md) · [Italiano](../../it/docs/installation.md) · [日本語](../../ja/docs/installation.md) · [한국어](../../ko/docs/installation.md) · [मराठी](../../mr/docs/installation.md) · [فارسی](../../fa/docs/installation.md) · [Polski](../../pl/docs/installation.md) · [Português](../../pt/docs/installation.md) · [ਪੰਜਾਬੀ](../../pa/docs/installation.md) · [Română](../../ro/docs/installation.md) · [Русский](../../ru/docs/installation.md) · [Español](../../es/docs/installation.md) · [Kiswahili](../../sw/docs/installation.md) · [Svenska](../../sv/docs/installation.md) · [தமிழ்](../../ta/docs/installation.md) · [ไทย](../../th/docs/installation.md) · [Türkçe](../../tr/docs/installation.md) · [Українська](../../uk/docs/installation.md) · [اردو](../../ur/docs/installation.md) · [Tiếng Việt](../../vi/docs/installation.md)

[Translation policy](../../README.md)

</details>
<!-- nv-language-navigation:end -->

<!-- nv-translation-notice:start -->
> Pagsasalin na tinulungan ng makina mula sa Ingles. Ang mga teknikal na pangalan, utos, URL at orihinal na legal na teksto ay pinapanatili. Malugod na tinatanggap ang pagsusuri ng katutubong nagsasalita; kumonsulta sa sangguniang Ingles kung ang mga salita ay hindi malinaw.
<!-- nv-translation-notice:end -->

<a id="installation-guide"></a>
# Gabay sa pag-install

Magsimula sa [Mga download](downloads.md), na nagtatala ng status ng publikasyon at mga eksaktong pangalan ng asset. Ang mga ito ay hiwalay na mga tool: i-install lamang ang mga kailangan mo.

> **Para sa NVRasterPulse, i-install ang [RTSS mula sa Guru3D](https://www.guru3d.com/download/rtss-rivatuner-statistics-server-download/) bago buksan ang profile manager.**
> Dapat tumakbo ang RTSS upang maglapat ng mga limitasyon; hindi ito kasama sa NV Tools.

| Tool | Naka-install na edisyon | Portable na edisyon | Pangunahing kinakailangan |
| --- | --- | --- | --- |
| NVIDIA Profile Inspector – NV Tools Fork | NVPI-CustomNV-3.0.2.3-Setup-r2.exe | I-extract ang kumpletong NVPI ZIP | NVIDIA driver at .NET Framework 4.8 |
| NVDriverForge | NVDriverForge-Setup.exe | NVDriverForge.exe, kasama ang runtime | Mga katugmang orihinal na NVIDIA driver package para sa mga operasyon sa pag-install |
| NVMFG Unlock40 | NVMFGUnlock40-0.2.3-Setup-x64.exe | I-extract ang kumpletong NVMFG ZIP, panatilihin ang mga subfolder | RTX 40, kasalukuyang DLSS FG, eksaktong provider at .NET Framework na 4.8 na mga katulong |
| NVRasterPulse | NVRasterPulse-0.2-win-x64-Setup.exe | I-extract ang kumpletong RP ZIP | RTSS at .NET Framework 4.8 |

<a id="download-verify-install"></a>
## I-download, i-verify, i-install

1. Sa napiling na-publish na Release, i-download ang pinangalanang asset ng application nito, notices ZIP at SHA256SUMS.txt.
2. Gamitin ang [Halimbawa ng SHA-256](downloads.md#sha-256), kasama ang aktwal na na-download na filename.
3. Para sa Setup, sundin ang normal na installer. Para sa portable ZIP, i-extract ang lahat sa isang bagong lokal na masusulat na folder; huwag tumakbo mula sa loob ng ZIP.
4. Buksan ang sariling EXE ng application. Panatilihin ang kasamang lisensya/configuration/data file.
5. Basahin ang mga tagubilin sa paggamit ng tool na iyon bago i-enable ang mga setting o pagpapatakbo ng system.

Ang mga kasalukuyang binary ay hindi nalagdaan. Kinukumpirma ng katugmang hash ang inaasahang byte; hindi ito isang sertipiko ng seguridad o pagiging tugma. Huwag i-disable ang mga proteksyon sa seguridad ng Windows para lang sugpuin ang isang babala.

Ang pag-install ng NVDF o ang opsyonal na kasama nitong NVPI ay hiwalay sa pag-install ng driver ng GPU. Pinapanatili ng kasamang NVPI ang umiiral nitong pangalan sa panloob na pag-install. Ang nakataas na button na RasterPulse nito ay nangangailangan ng protektadong pag-install sa buong system; iba pang mga kopya ng RP ay maaaring mabuksan sa pamamagitan ng kanilang sariling mga shortcut.

Ang NVMFG ay eksperimental at mayroong [dokumentado NVIDIA SDK reserbang paglilisensya](provenance.md). Walang kasamang NVIDIA driver, NGX provider/modelo o larong Streamline runtime. Ang mga napiling SDK na pag-download at pag-update ng laro ay tahasang magkahiwalay na operasyon.

<a id="language-and-updates"></a>
## Wika at mga update

Gamitin ang 34-language selector ng README para sa dokumentasyon. Ang NVDF, NVMFG at RP ay may sariling 34-language na setting ng UI; Pinapanatili ng NVPI ang umiiral nitong suporta sa wika. Ang ilang mga teknikal na string ng installer ay bumabalik sa Ingles.

Panatilihin ang pagkakakilanlan ng pag-install ng tool kapag nag-a-update. Isara muna ito at panatilihin ang mga backup. Para sa NVMFG, isara ang mga apektadong laro at lutasin ang nakabinbing pagbawi ng profile. Para sa mga portable na update, gumamit ng bagong folder sa halip na pagsamahin ang mga release.

<a id="removing-a-tool"></a>
## Pag-alis ng isang tool

Ang pag-uninstall ng isang application ay hindi awtomatikong ina-undo ang mga setting nito.

- **NVPI:** ibalik ang mga nilalayong profile/setting ng display bago alisin kung kinakailangan.
- **NVDF:** gamitin muna ang pagbawi kung gusto mong i-restore ang mga advanced/NVENC na pagbabago. Ang Uninstall ay umalis sa graphics driver, mga setting at backup.
- **NVMFG:** isara ang mga laro, i-disable/iwanan ang controller, lutasin ang pagbawi ng NVIDIA at i-restore ang ninanais na pag-backup ng SDK ng laro bago alisin.
- **RP:** alisin muna ang nilalayong pag-override ng limiter. Hindi binubura ng Uninstall ang mga naka-save na cap ng RTSS o inaalis ang RTSS.

Tingnan ang bawat [gabay sa proyekto](../README.md#projects) para sa eksaktong mga lokasyon at limitasyon ng data, o [suporta](support.md) kung nabigo ang isang hakbang sa pagbawi.
