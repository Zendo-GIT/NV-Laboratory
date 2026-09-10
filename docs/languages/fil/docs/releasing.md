<!-- nv-language-navigation:start -->
🌐 [English](../../../releasing.md) | [Français](../../../releasing.fr.md) · [NV Laboratory](../README.md)

<details>
<summary>🌐 Language · 34</summary>

[العربية](../../ar/docs/releasing.md) · [বাংলা](../../bn/docs/releasing.md) · [简体中文](../../zh/docs/releasing.md) · [Čeština](../../cs/docs/releasing.md) · [Dansk](../../da/docs/releasing.md) · [Nederlands](../../nl/docs/releasing.md) · [English](../../../releasing.md) · **Filipino** · [Suomi](../../fi/docs/releasing.md) · [Français](../../../releasing.fr.md) · [Deutsch](../../de/docs/releasing.md) · [Ελληνικά](../../el/docs/releasing.md) · [हिन्दी](../../hi/docs/releasing.md) · [Magyar](../../hu/docs/releasing.md) · [Bahasa Indonesia](../../id/docs/releasing.md) · [Italiano](../../it/docs/releasing.md) · [日本語](../../ja/docs/releasing.md) · [한국어](../../ko/docs/releasing.md) · [मराठी](../../mr/docs/releasing.md) · [فارسی](../../fa/docs/releasing.md) · [Polski](../../pl/docs/releasing.md) · [Português](../../pt/docs/releasing.md) · [ਪੰਜਾਬੀ](../../pa/docs/releasing.md) · [Română](../../ro/docs/releasing.md) · [Русский](../../ru/docs/releasing.md) · [Español](../../es/docs/releasing.md) · [Kiswahili](../../sw/docs/releasing.md) · [Svenska](../../sv/docs/releasing.md) · [தமிழ்](../../ta/docs/releasing.md) · [ไทย](../../th/docs/releasing.md) · [Türkçe](../../tr/docs/releasing.md) · [Українська](../../uk/docs/releasing.md) · [اردو](../../ur/docs/releasing.md) · [Tiếng Việt](../../vi/docs/releasing.md)

[Translation policy](../../README.md)

</details>
<!-- nv-language-navigation:end -->

<!-- nv-translation-notice:start -->
> Pagsasalin na tinulungan ng makina mula sa Ingles. Ang mga teknikal na pangalan, utos, URL at orihinal na legal na teksto ay pinapanatili. Malugod na tinatanggap ang pagsusuri ng katutubong nagsasalita; kumonsulta sa sangguniang Ingles kung ang mga salita ay hindi malinaw.
<!-- nv-translation-notice:end -->

<a id="publishing-and-releases"></a>
# Publishing at release

Ang pampublikong imbakan ay **Zendo-GIT/NV-Laboratory**. Ang mga pagbabago sa dokumentasyon ay sinusuri, ginawa at itinutulak ng maintainer gamit ang **GitHub Desktop**. Ang lokal na commit ay hindi nag-a-upload ng mga file. Ang mga binary package ay hiwalay na GitHub Release asset; hindi sila nabibilang sa listahan ng mga pagbabago sa Git.

<a id="documentation-updates"></a>
## Mga update sa dokumentasyon

1. Buksan ang folder na **NV-Laboratory** sa GitHub Desktop.
2. Suriin ang dokumentasyon, mga abiso, mga larawan, JSON metadata at ang documentation validator.
3. Patakbuhin ang `python tools/validate_repository.py` mula sa folder na iyon.
4. Ibigay ang nasuri na mga pagbabago, pagkatapos ay gamitin ang **Push origin**. Suriin ang resulta ng Mga Pagkilos.
5. Panatilihin ang pagkakakilanlan ng pampublikong may-akda **禅堂 Zendo (RevoluSound Team)** at ang address ng GitHub `noreply` ng account.

Huwag kailanman piliin ang parent development workspace, pribadong audit directory o binary attachment directory. [Magbigay ng privacy sa email](https://docs.github.com/en/account-and-profile/how-tos/email-preferences/setting-your-commit-email-address).

<a id="independent-application-releases"></a>
## Mga independiyenteng paglabas ng aplikasyon

| Tool | Tag | Patakaran sa bersyon |
| --- | --- | --- |
| NVIDIA Profile Inspector – NV Tools Fork | nvpi-v3.0.2.3 | Umiiral na apat na bahagi na bersyon ng application; setup revision 2 ay may sariling filename |
| NVDriverForge | nvdriverforge-v0.1.3 | Umiiral na 0.x scheme; pinapanatili ng mga bersyong update ang mga naunang pakete |
| NVMFG Unlock40 | nvmfg-unlock40-v0.1.1 | Natukoy ang kandidato ng UI2 sa pamamagitan ng eksaktong mga hash nang hindi nag-imbento ng bagong bersyon ng application |
| NVRasterPulse | nvrasterpulse-v0.1 | Umiiral na dalawang bahagi na bersyon |

Ang tagapangasiwa ay maaaring direktang mag-publish o pahintulutan ang isang assistant na i-publish ang mga na-audit na asset. Ang publikasyon ay tahasan; walang workflow na lumilikha ng Release sa bawat commit.

1. Suriin ang kasalukuyang ulat bago ang paglalathala, mga pinagmumulan ng mga binary, lisensya at mga halaga ng SHA-256.
2. Gumawa ng draft para sa tag ng tool, na nagta-target sa nasuri na hub commit. Isama ang inihandang mga tala sa paglabas na partikular sa bersyon.
3. I-attach lang ang Setup/portable na asset ng bersyong iyon, `Licenses-and-Credits.zip` at `SHA256SUMS.txt`.
4. Suriin ang compatibility, pag-install, dependencies, pagbabago at alam na limitasyon. Panatilihing prominente ang RTSS para sa NVRasterPulse.
5. I-publish, i-verify ang mga URL, laki at hash ng pampublikong asset, at itala ang aktwal na petsa ng publikasyon sa `docs/releases.json`.
6. I-update ang mga pahina ng pag-download at pagsasalin, pagkatapos ay i-commit/i-push ang kanilang mga pagbabago sa GitHub Desktop.

Iniiwasan ng mga link na tag bawat proyekto ang pagpapadala ng mga user sa isa pang tool sa pamamagitan ng nakabahaging link na `releases/latest`. Ang mga awtomatikong **Source code** na archive ng GitHub ay naglalaman ng hub ng dokumentasyong ito. Mananatiling pribado ang mga source ng application. Nananatiling buo ang mga paunawa ng orihinal na bahagi, at hindi niresolba ng isang release ang nakadokumentong NVIDIA SDK na reserba ng NVMFG.

<a id="integrity-and-storage"></a>
## Integridad at imbakan

Huwag kailanman tahimik na palitan ang na-publish na mga binary byte. Gumamit ng bagong tahasang bersyon o rebisyon ng installer na may mga bagong hash. Ang mga legal na sidecar ay pandagdag sa mga naka-embed na abiso. Ang NVDriverForge 0.1.3 portable ay 141,760,351 bytes, higit sa ordinaryong 100 MiB Git-file na limitasyon ng GitHub. Iwasan ng mga release na attachment ang paglalagay ng mga binary o Git LFS sa hub na ito. [GitHub malaking-file na gabay](https://docs.github.com/en/repositories/working-with-files/managing-large-files/about-large-files-on-github).

Ang pag-uulat ng pribadong kahinaan ay dapat na pinagana sa mga setting ng seguridad ng imbakan. I-verify ang availability nito bago magdirekta ng mga sensitibong ulat doon; Nagbibigay ang [SECURITY.md](../SECURITY.md) ng fallback na hindi naglalantad ng mga detalye ng kahinaan.

[I-download ang catalog](downloads.md) · [Dokumentasyon ng paglabas ng GitHub](https://docs.github.com/en/repositories/releasing-projects-on-github/managing-releases-in-a-repository)
