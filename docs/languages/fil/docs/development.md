<!-- nv-language-navigation:start -->
🌐 [English](../../../development.md) | [Français](../../../development.fr.md) · [NV Laboratory](../README.md)

<details>
<summary>🌐 Language · 34</summary>

[العربية](../../ar/docs/development.md) · [বাংলা](../../bn/docs/development.md) · [简体中文](../../zh/docs/development.md) · [Čeština](../../cs/docs/development.md) · [Dansk](../../da/docs/development.md) · [Nederlands](../../nl/docs/development.md) · [English](../../../development.md) · **Filipino** · [Suomi](../../fi/docs/development.md) · [Français](../../../development.fr.md) · [Deutsch](../../de/docs/development.md) · [Ελληνικά](../../el/docs/development.md) · [हिन्दी](../../hi/docs/development.md) · [Magyar](../../hu/docs/development.md) · [Bahasa Indonesia](../../id/docs/development.md) · [Italiano](../../it/docs/development.md) · [日本語](../../ja/docs/development.md) · [한국어](../../ko/docs/development.md) · [मराठी](../../mr/docs/development.md) · [فارسی](../../fa/docs/development.md) · [Polski](../../pl/docs/development.md) · [Português](../../pt/docs/development.md) · [ਪੰਜਾਬੀ](../../pa/docs/development.md) · [Română](../../ro/docs/development.md) · [Русский](../../ru/docs/development.md) · [Español](../../es/docs/development.md) · [Kiswahili](../../sw/docs/development.md) · [Svenska](../../sv/docs/development.md) · [தமிழ்](../../ta/docs/development.md) · [ไทย](../../th/docs/development.md) · [Türkçe](../../tr/docs/development.md) · [Українська](../../uk/docs/development.md) · [اردو](../../ur/docs/development.md) · [Tiếng Việt](../../vi/docs/development.md)

[Translation policy](../../README.md)

</details>
<!-- nv-language-navigation:end -->

<!-- nv-translation-notice:start -->
> Pagsasalin na tinulungan ng makina mula sa Ingles. Ang mga teknikal na pangalan, utos, URL at orihinal na legal na teksto ay pinapanatili. Malugod na tinatanggap ang pagsusuri ng katutubong nagsasalita; kumonsulta sa sangguniang Ingles kung ang mga salita ay hindi malinaw.
<!-- nv-translation-notice:end -->

<a id="repository-architecture-and-maintenance"></a>
# Arkitektura at pagpapanatili ng imbakan

Ang NV Laboratory ay isang pampublikong **dokumentasyon at binary-distribution hub**. Hindi ito naglalaman ng pinagmulan ng application. Ang apat na proyekto ay nagpapanatili ng magkahiwalay na mga build tree, mga bersyon, pagkakakilanlan at mga asset ng release. Ang kanilang kasaysayan ng pribadong pag-unlad ay hindi na-import sa Git repository na ito.

<a id="layout"></a>
## Layout

| Lokasyon | Layunin |
| --- | --- |
| README.md / README.fr.md | English/French entry point |
| Apat na folder ng proyekto | Mga kumpletong gabay at naaangkop na orihinal na mga abiso |
| mga doc | Mga download, compatibility, provenance, development at release procedure |
| docs/releases.json | Na-audit ang kandidato/paglabas ng metadata, laki at hash |
| docs/provenance | Mga paghahambing ng file/hash; walang application code |
| mga lisensya | Ibinahagi ang buong third-party na mga text at mga kredito ng tagasalin ng installer |
| mga ari-arian | Mga kasalukuyang nasuri na preview ng UI at ang pinagmulan ng mga ito |
| .github | Mga form ng isyu at pagpapatunay ng read-only na dokumentasyon |
| tool/validate_repository.py | Standard-library publication-boundary at mga pagsusuri sa link |

Ang English ay nananatiling default na GitHub README. Mananatiling wasto ang mga umiiral na katabing link na `.fr.md`. Ang mga karagdagang pagsasalin ay sumasalamin sa dokumentasyon sa ilalim ng `docs/languages/<code>`; pinapanatili ng tagapili ng wika ang parehong pahina kapag nagpapalit ng mga wika. Itinatala ng catalog na `docs/languages/catalog.json` ang lahat ng 34 na wika at pinagmulan ng mga fingerprint. Ang GitHub ay hindi awtomatikong pumipili ng README ayon sa wika ng browser. Tingnan ang [index ng wika at patakaran sa pagsasalin](../../README.md).

<a id="application-technologies"></a>
## Mga teknolohiya ng aplikasyon

| Programa | Pribadong teknolohiya | Pamamahagi |
| --- | --- | --- |
| NVPI fork | C#, WPF, .NET Framework 4.8, NVAPI/Windows interop | Kumpletuhin ang portable na folder at hiwalay na Inno Setup |
| NVDriverForge | C#, WPF, .NET 8; katutubong C++ bootstrap; Proseso ng 7-Zip | Self-contained portable EXE at Setup |
| NVMFG Unlock40 | C#/WPF .NET 8, Framework 4.8 helpers, C++20/MASM/MinHook engine | Portable na puno at Setup |
| NVRasterPulse | C#/WPF Framework 4.8; RTSS pagsasama ng profile/reload; katutubong bootstrap | Portable na puno at Setup |

Ang pampublikong pag-checkout na ito ay hindi maaaring muling buuin ang mga application. Ang mga awtomatikong archive ng "Source code" ay mga snapshot ng hub. Ang mga link sa upstream na pinagmulan ay hindi kumakatawan sa eksaktong pribadong binagong pinagmulan. Ang pampublikong CI ay nagpapatunay lamang sa repositoryong ito.

<a id="local-checks"></a>
## Mga lokal na tseke

Mula sa root ng repositoryo:

```text
python tools/validate_repository.py
```

Python 3.10 o mas bago ay sapat na. Ang tseke ay nagbabasa ng mga file, mga lokal na Markdown na link, mga kinakailangang paunawa/RTSS na mga link, naglalabas ng metadata at mga hangganan ng publikasyon. Hindi nito pinaandar ang software, nag-i-install ng mga dependency o nakikipag-ugnayan sa isang network.

Ang daloy ng trabaho ng GitHub ay nagpapatakbo ng parehong pagsusuri na may pahintulot ng read-only na nilalaman sa push, pull request o manu-manong pagpapadala. Ang pag-checkout ay naka-pin sa isang na-audit na commit at hindi nagpatuloy ng mga kredensyal. Walang release o deployment na trabaho ang naka-configure.

<a id="maintain-the-boundary"></a>
## Panatilihin ang hangganan

I-update ang sanggunian sa Ingles, mga gabay sa Pranses at mga apektadong pagsasalin nang magkasama. Panatilihing hiwalay ang mga makabuluhang pagbabago sa mga paghahambing sa pag-format lang. Mag-record ng aktwal na mga hash ng kandidato, upstream commit reference at lisensya; hindi kailanman maghihinuha ng lisensya mula sa kasikatan ng isang proyekto.

Gumamit ng bagong bersyon na mga asset ng Release at muling i-audit ang mga binary na binary, archive at naka-embed na notice. Panatilihin ang mga pribadong backup sa labas ng repositoryong ito. Huwag gumamit ng pampublikong workflow para mag-import ng pribadong application source o local build folder.

Ang mga pagsubok na naaangkop sa isang functional na pagbabago ng application ay tumatakbo sa pribadong proyekto. Huwag muling patakbuhin ang mga installer ng driver o magsulat ng mga totoong profile para sa pag-update ng dokumentasyon. [Manu-manong pamamaraan ng pagpapalabas](releasing.md).
