<!-- nv-language-navigation:start -->
🌐 [English](../../../provenance.md) | [Français](../../../provenance.fr.md) · [NV Laboratory](../README.md)

<details>
<summary>🌐 Language · 34</summary>

[العربية](../../ar/docs/provenance.md) · [বাংলা](../../bn/docs/provenance.md) · [简体中文](../../zh/docs/provenance.md) · [Čeština](../../cs/docs/provenance.md) · [Dansk](../../da/docs/provenance.md) · [Nederlands](../../nl/docs/provenance.md) · [English](../../../provenance.md) · **Filipino** · [Suomi](../../fi/docs/provenance.md) · [Français](../../../provenance.fr.md) · [Deutsch](../../de/docs/provenance.md) · [Ελληνικά](../../el/docs/provenance.md) · [हिन्दी](../../hi/docs/provenance.md) · [Magyar](../../hu/docs/provenance.md) · [Bahasa Indonesia](../../id/docs/provenance.md) · [Italiano](../../it/docs/provenance.md) · [日本語](../../ja/docs/provenance.md) · [한국어](../../ko/docs/provenance.md) · [मराठी](../../mr/docs/provenance.md) · [فارسی](../../fa/docs/provenance.md) · [Polski](../../pl/docs/provenance.md) · [Português](../../pt/docs/provenance.md) · [ਪੰਜਾਬੀ](../../pa/docs/provenance.md) · [Română](../../ro/docs/provenance.md) · [Русский](../../ru/docs/provenance.md) · [Español](../../es/docs/provenance.md) · [Kiswahili](../../sw/docs/provenance.md) · [Svenska](../../sv/docs/provenance.md) · [தமிழ்](../../ta/docs/provenance.md) · [ไทย](../../th/docs/provenance.md) · [Türkçe](../../tr/docs/provenance.md) · [Українська](../../uk/docs/provenance.md) · [اردو](../../ur/docs/provenance.md) · [Tiếng Việt](../../vi/docs/provenance.md)

[Translation policy](../../README.md)

</details>
<!-- nv-language-navigation:end -->

<!-- nv-translation-notice:start -->
> Pagsasalin na tinulungan ng makina mula sa Ingles. Ang mga teknikal na pangalan, utos, URL at orihinal na legal na teksto ay pinapanatili. Malugod na tinatanggap ang pagsusuri ng katutubong nagsasalita; kumonsulta sa sangguniang Ingles kung ang mga salita ay hindi malinaw.
<!-- nv-translation-notice:end -->

<a id="provenance-changes-and-licensing"></a>
# Provenance, pagbabago at paglilisensya

Inilalarawan ng audit na ito ang mga kandidatong inihanda noong **2026-09-09**. Ang mga mapagkukunan ng aplikasyon ay nananatiling pribado; ang mga pampublikong imbentaryo ay naglalaman ng mga filename at hash, hindi source code. Tingnan ang [buong bahagi ng mga abiso](../THIRD_PARTY_NOTICES.md).

<a id="nvidia-profile-inspector--nv-tools-fork"></a>
## NVIDIA Profile Inspector – NV Tools Fork

Sanggunian: Orbmu2k/nvidiaProfileInspector gumawa ng `592d962cca8827efe8859461a84267755595064a`; kandidato executable na bersyon 3.0.2.3. Ang reference commit at ang bersyon ng assembly ng fork ay magkaibang mga identifier; walang upstream na bersyon ng release ang nahihinuha mula sa fork na bersyon.

Ang 157 source/resource file ng malinis na kasama ay inihambing sa commit na iyon: 2 byte-identical, 134 differing only in line endings o UTF-8 BOM, 11 modified, 10 absent at the compared upstream path. Ang "Idinagdag" ay nauugnay sa landas na iyon at hindi ito mismong patunay ng orihinal na may-akda.

[Kumpletuhin ang paghahambing ng file/hash](../../../provenance/nvpi-source-provenance.json).

| Lugar | Manang trabaho | Fork na kontribusyon |
| --- | --- | --- |
| Editor ng profile | Modelo ng profile, pag-import/pag-export, mga asosasyon ng application at data ng sanggunian | Pagsasama sa Screen at sa panlabas na tool launcher |
| NVAPI | Ang DRS interop ng Orbmu2k | Interop na nauugnay sa kulay/display, mga paghihigpit sa native-loading ng produksyon at pag-alis ng kunwaring |
| Mga serbisyo sa pagpapakita | Mga Windows/NVIDIA API bilang mga panlabas na interface | DisplayInfoService, DisplayConfigurationService, DisplaySettingsBackend |
| UI | Upstream na WPF na mga mapagkukunan, palette at icon | Mga dialog ng screen, 15 segundong kumpirmasyon, status/read-back at layout ng toolbar |
| Launcher | Kasalukuyang shell ng app | Pinoprotektahan ang hiwalay na naka-install na paghahanap at paglulunsad ng RasterPulse |
| Packaging | MIT upstream | Malinis na standalone na kasama, hiwalay na installer/uninstaller, napanatili ang mga abiso |

Kasama sa pampublikong mapagkukunang mapa ang mga landas ng solusyon/pagkukunan para sa kakayahang masubaybayan; ang mga file na iyon ay hindi ipinamahagi bilang pinagmulan. Ang mga pagsubok sa pag-develop, mga kunwaring interface at ang lumang pinagsamang NVPI/RasterPulse binary ay hindi kasama.

<a id="nvdriverforge"></a>
## NVDriverForge

Independent C#/.NET 8/WPF application; ang daloy ng trabaho na nakaharap sa gumagamit ay bahagyang inspirasyon ng NVCleanstall. Walang natukoy na NVCleanstall source/binary sa production payload. Hindi ito kinakatawan bilang isang fork ng pagmamay-ari na application na iyon.

Kasama sa orihinal na gawain ng proyekto ang pagsusuri/pagpili ng bahagi, mga protektadong trabaho sa pag-install, pag-backup at pagbawi ng transaksyon, pag-download ng katalogo ng NVIDIA, pagsusuri sa pag-update, mga naka-localize na paliwanag, opsyonal na advanced/NVENC na mga daloy ng trabaho at bootstrap ng installer.

Mga minana/na-adapt na bahagi: apat na NVPI theme palette, pinalawig na NVAPI DRS interface reference, at ang hiwalay na opsyonal na MIT NVPI na kasama. Ang piniling UI ng Custom NV preset at pinapayagang pagsasama ng transaksyon ay nabibilang sa NVDriverForge; ang preset ay hindi isang opisyal na rekomendasyon ng NVIDIA.

Ang 7-Zip 26.03, .NET/WPF 8.0.31 at Inno Setup ay nananatiling hindi nabagong mga panlabas na bahagi na ginagamit sa ilalim ng sarili nilang mga termino. Ang data ng keylase NVENC ay hindi naka-embed; isang eksaktong commit ang pipiliin at sinusuri kapag humiling ang user ng katugmang pag-download. Walang naitatag na lisensya sa muling pamamahagi para sa upstream na data na iyon.

<a id="nvmfg-unlock40"></a>
## NVMFG Unlock40

Ang NVMFG Unlock40 ay independiyenteng binuo ng 禅堂 Zendo (RevoluSound Team). Ginamit ng maintainer ang RTX40MFG-Unlock para sa paghahambing at pagpipino. Ang application sa kabuuan ay hindi ipinakita bilang fork nito. Ang pagkakaibang ito ay hindi nag-aalis ng mga kredito para sa mga nakabahagi/na-adapt na bahagi sa kasalukuyang native na layer.

Sanggunian sa paghahambing: dashdogy/RTX40MFG-Unlock, Michael Robles, MIT, i-commit ang `4e776d068f91b4a665425542bb005dd57cc3d891`. Ang pribadong native-engine tree ay naglalaman ng 48 kumpara sa mga file: 35 formatting-only na mga pagkakaiba, 4 na binagong file at 9 na wala sa reference path. [Kumpletong paghahambing](../../../provenance/nvmfg-source-provenance.json).

Binago ang mga minanang file: `entry_detour.h`, `patcher.cpp`, `temporal_interval_trace.cpp`, `temporal_interval_trace.h`. Kasama sa mga karagdagang path ang `game_selection.*`, `ngx_bootstrap.*`, `ngx_capability.h`, `presentation_tracker.h`, `vsync_observer.*` at isang pinananatiling upstream na lisensya.

Mga unit ng Production C++: patcher, midpoint_fix, dlssg_provider_policy, entry_detour, nvidia_mfg_policy, temporal_interval_trace, ngx_bootstrap, game_selection at vsync_observer; kasama ang entry_detour assembly at MinHook buffer/hook/trampoline/HDE64. Ang minanang ReShade frontend, legacy shim resources at hindi nagamit na CMake target ay hindi bahagi ng production compilation na ito.

Ang mga tumutugmang bahagi ay sumasaklaw sa patching/provider na patakaran at temporal na gawain; nananatiling buo ang kanilang mga abiso sa copyright at pahintulot. Ang gitnang NGX/bootstrap/ controller coordination, per-game V-Sync handling, session diagnostics at Windows application/SDK/backup workflow ay proyekto ng 禅堂 Zendo (RevoluSound Team). Ang mga bilang sa itaas ay naglalarawan ng mga file, kabilang ang mga third-party at hindi nagamit na mga file, hindi isang porsyento ng authorship o ang kronolohiya ng alinmang ideya ng proyekto.

Ang katulong ay umaangkop NVPI's NvapiDrsWrapper at NativeArrayHelper sa isang hiwalay na pagpupulong, na may lohika ng profile na may akda ng proyekto. Ang lumang development mock path ay hindi kasama. Nagmula ang mga nakabahaging palette ng pamilya NVPI.

MinHook sanggunian: `8fda4f5481fed5797dc2651cd91e238e9b3928c6`; ang minanang compiled subset ay walang functional na lokal na pagbabago sa paghahambing. Streamline integration header: 2.12; na-verify na lisensya ng open header sa v2.12.0. Pinagmulan ng header ng NGX: NVIDIA/DLSS gumawa ng `a291cc7d2cc642a51566f3dfd5376f635cd1b284`.

Ang makina ng kandidato SHA-256: `0E7FC0277C88B22095B622F6A3CB292EC0C14F7A0253D392502257B75E548890`.

Kinakailangang provider na SHA-256 sa engine.json: `C64928FDB7C48A57722EA8EEF2662171EDC323473ADEA66C29A206A23F1A2BED`. Ang isang naiulat na pamilya ng provider ng 310.9 ay hindi mapapalitan ng eksaktong hash na ito. Walang provider na DLL o modelo ang kasama.

**Natitirang punto ng paglilisensya:** ang buong lisensyang NVIDIA RTX SDK, bersyon Marso 14, 2024, ay naglalaman ng seksyon 4(d) na paghihigpit na nauugnay sa pag-bypass sa mga teknikal na limitasyon. Ang pag-audit ay hindi nagtatag ng pahintulot para sa paggamit na ito. Ang pagpapanatili ng MIT na lisensya ng makina, pagiging walang bayad, o pag-obserba sa iba pang mga mod ay hindi nireresolba ang hiwalay na kundisyon na iyon. Ang paghahanda ng kandidato ay hindi isang legal na clearance. Ang orihinal na maikling paunawa sa header ay dinagdagan ng buong lisensya; ang Windows-1252 na text nito ay ibinibigay din bilang nababasang UTF-8, na may mga orihinal na byte na napanatili.

<a id="nvrasterpulse"></a>
## NVRasterPulse

Independiyenteng RTSS profile manager na binuo sa NVPI-derived repository. Nananatiling kredito ang minanang MIT UI na mga mapagkukunan/palette at pinagmulan ng proyekto. Tahasang ginagamit ng production app ang nagbigay ng lisensyang MIT.

Paggawa ng proyekto: tumpak na pag-parse/pagsusulat ng profile ng RTSS at fractional na pag-encode, pag-backup, pag-alis ng override, pag-reload ng tulay, pagtuklas ng kinakailangan, compact na UI, lifecycle ng tray, mga kontrol sa pagsisimula at lokalisasyon. Ang RTSS ay gumaganap ng aktwal na paglilimita.

Walang RTSS source, hook DLL, SDK o installer na naka-bundle. Ang tulay ay tumatawag sa pag-export sa isang umiiral na pinili ng user na pag-install na RTSS. Walang NVIDIA driver package, native experimental limiter, Framepacer, MinHook, ReShade o DLSS runtime ang nasa package na ito.

<a id="assets-generated-data-and-tools"></a>
## Mga asset, nabuong data at mga tool

Tinukoy ng [Mga kredito sa asset](../assets/README.md) ang mga kasalukuyang preview ng interface at ang tagapili ng setup ng NVPI. Ang mga kathang-isip na halaga sa mga ito ay may label. Walang nakopya na asset ng laro/Nexus, personal na profile, pribadong ICC, corporate NVIDIA logo o font file.

Ang mga nabuong pangalan ng compatibility ng laro na minana sa NVMFG ay isang tulong sa pagtuklas, hindi pansubok na ebidensya. Ang mga nabuong katalogo ng installer ay kredito sa [mga paunawa ng tagasalin](../../../../licenses/INSTALLER-TRANSLATORS.md). Nananatiling pribado ang mga nabuong talaan ng build na may ganap na mga landas.

Kasama sa mga private build tool ang .NET SDK/MSBuild, Visual Studio C++/MASM, Windows SDK, PowerShell, Inno Setup at Python audit script. Hindi ipinamahagi ang kanilang mga compiler, header, test runner at debug asset. Ang static na release CRT ay nananatili sa ilalim ng mga naaangkop na tuntunin ng toolchain ng Microsoft.

<a id="scope-of-verification"></a>
## Saklaw ng pagpapatunay

Ang lokal na pag-audit ay nag-imbentaryo ng lahat ng mga file sa tatlong pinagmulan ng pag-unlad habang hindi kasama ang mga database ng object ng Git at naka-link na mga target na direktoryo. Na-scan ang aktibong pinagmulan/doc; ang mga makasaysayang build ay inimbentaryo at hindi kasama. Na-scan at na-hash ang mga napiling ZIP at kasalukuyang mga payload; ang mga .NET na bundle ay na-decompress para sa karagdagang inspeksyon. Ang paunang pag-audit na iyon ay walang produkto, installer, laro, proseso ng RTSS o driver.

Ang susunod na NVPI setup revision 2 ay nag-aayos ng standalone na pagpili ng wika gamit ang mga shared Inno controls at bootstrap. Na-verify ng maliwanag/madilim na pribadong fixture ang mouse at keyboard navigation at lahat ng 34 na tahasang code ng wika. Ang aktwal na tagapili ng setup ay binuksan sa isang hindi kailanman ipinapakitang pribadong desktop at kinansela bago i-install. Ang pitong application file at portable ZIP nito ay hindi nagbabago. Kasama sa NVDriverForge 0.1.3 ang naitama na kasama at nagpapasa pa rin ng `/LANG`.

Nakumpleto ang NVDriverForge 0.1.3 noong 2026-09-10. Ang ulat ng pribadong pag-verify nito ay nagtatala ng 366 na pagsubok sa aplikasyon, 118 kasamang pagsusuri, 32 pagsusuri sa pag-setup, 156 katutubong paghahambing at 34 na kaso sa pagpapasa ng wika. Ang protektadong component-selection fix ay na-replay laban sa isang orihinal na driver package nang hindi binabago ang kargamento nito o ini-install ang driver. Ang mga ito ay may petsang mga resulta ng pangkat ng produkto, hindi mga pagsubok na muling pinalabas ng pag-update ng dokumentasyong ito o patunay ng isang matagumpay na pag-install ng tunay na driver.

Ang pag-update ng hub na ito ay walang pagbabago sa functional na code ng application. Ang mga naunang pagsubok sa build/unit/UI ng application ay nananatiling may petsang makasaysayang ebidensya. Hindi ito ganap na reverse engineering ng bawat third-party na binary o isang garantiya laban sa bawat posibleng lihim na pattern.
