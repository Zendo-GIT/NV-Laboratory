<!-- nv-language-navigation:start -->
🌐 [English](../../../../NVIDIA-Profile-Inspector/README.md) | [Français](../../../../NVIDIA-Profile-Inspector/README.fr.md) · [NV Laboratory](../README.md)

<details>
<summary>🌐 Language · 34</summary>

[العربية](../../ar/NVIDIA-Profile-Inspector/README.md) · [বাংলা](../../bn/NVIDIA-Profile-Inspector/README.md) · [简体中文](../../zh/NVIDIA-Profile-Inspector/README.md) · [Čeština](../../cs/NVIDIA-Profile-Inspector/README.md) · [Dansk](../../da/NVIDIA-Profile-Inspector/README.md) · [Nederlands](../../nl/NVIDIA-Profile-Inspector/README.md) · [English](../../../../NVIDIA-Profile-Inspector/README.md) · **Filipino** · [Suomi](../../fi/NVIDIA-Profile-Inspector/README.md) · [Français](../../../../NVIDIA-Profile-Inspector/README.fr.md) · [Deutsch](../../de/NVIDIA-Profile-Inspector/README.md) · [Ελληνικά](../../el/NVIDIA-Profile-Inspector/README.md) · [हिन्दी](../../hi/NVIDIA-Profile-Inspector/README.md) · [Magyar](../../hu/NVIDIA-Profile-Inspector/README.md) · [Bahasa Indonesia](../../id/NVIDIA-Profile-Inspector/README.md) · [Italiano](../../it/NVIDIA-Profile-Inspector/README.md) · [日本語](../../ja/NVIDIA-Profile-Inspector/README.md) · [한국어](../../ko/NVIDIA-Profile-Inspector/README.md) · [मराठी](../../mr/NVIDIA-Profile-Inspector/README.md) · [فارسی](../../fa/NVIDIA-Profile-Inspector/README.md) · [Polski](../../pl/NVIDIA-Profile-Inspector/README.md) · [Português](../../pt/NVIDIA-Profile-Inspector/README.md) · [ਪੰਜਾਬੀ](../../pa/NVIDIA-Profile-Inspector/README.md) · [Română](../../ro/NVIDIA-Profile-Inspector/README.md) · [Русский](../../ru/NVIDIA-Profile-Inspector/README.md) · [Español](../../es/NVIDIA-Profile-Inspector/README.md) · [Kiswahili](../../sw/NVIDIA-Profile-Inspector/README.md) · [Svenska](../../sv/NVIDIA-Profile-Inspector/README.md) · [தமிழ்](../../ta/NVIDIA-Profile-Inspector/README.md) · [ไทย](../../th/NVIDIA-Profile-Inspector/README.md) · [Türkçe](../../tr/NVIDIA-Profile-Inspector/README.md) · [Українська](../../uk/NVIDIA-Profile-Inspector/README.md) · [اردو](../../ur/NVIDIA-Profile-Inspector/README.md) · [Tiếng Việt](../../vi/NVIDIA-Profile-Inspector/README.md)

[Translation policy](../../README.md)

</details>
<!-- nv-language-navigation:end -->

<!-- nv-translation-notice:start -->
> Pagsasalin na tinulungan ng makina mula sa Ingles. Ang mga teknikal na pangalan, utos, URL at orihinal na legal na teksto ay pinapanatili. Malugod na tinatanggap ang pagsusuri ng katutubong nagsasalita; kumonsulta sa sangguniang Ingles kung ang mga salita ay hindi malinaw.
<!-- nv-translation-notice:end -->

<a id="nvidia-profile-inspector--nv-tools-fork"></a>
# NVIDIA Profile Inspector – NV Tools Fork

**Isang independiyenteng fork ng [NVIDIA Profile Inspector ni Orbmu2k](https://github.com/Orbmu2k/nvidiaProfileInspector), na may mga karagdagang kontrol sa display.** Dating pangalan ng proyekto: **NVPI Custom**.

[I-download at i-release ang status](../docs/downloads.md#nvidia-profile-inspector) · [Pag-install](#installation) · [Upstream at pagbabago](#upstream-and-changes) · [Lisensya](../../../../NVIDIA-Profile-Inspector/LICENSE)

<a id="overview"></a>
## Pangkalahatang-ideya

Ini-edit ng application ang mga profile ng driver ng NVIDIA, kabilang ang mga setting ng bawat application. Nagdaragdag din ang fork na ito ng **Screen** editor para sa aktibong Windows display: resolution, refresh rate, mga setting ng kulay ng output, HDR at naka-install na ICC/WCS profile associations.

Umiiral ito upang dalhin ang mga nauugnay na kontrol sa pagpapakita sa editor ng profile at upang gawing mas malinaw ang mga resulta ng preview, kumpirmasyon at pagpapanumbalik. Hindi ito nagtatag ng mga bagong kakayahan sa hardware.

Ang unang kandidato ay **3.0.2.3**, gamit ang nalinis na standalone companion build mula Setyembre 9, 2026. Ang kasalukuyang executable nito ay nananatiling `nvidiaProfileInspector.exe`; ang installer at ilang panloob na label ay nagsasabi pa rin ng `NVPI Custom NV`. Ang pampublikong pamagat sa itaas ay kinikilala ang fork nang hindi binabago ang pagkakakilanlan ng pag-install o nagpapanggap na ito ay opisyal na paglabas ng Orbmu2k.

<a id="features"></a>
## Mga tampok

- Umiiral na upstream profile browsing, application associations, setting edits at profile import/export.
- **Screen** dialog para sa display, mode, Hz, RGB/YCbCr, color depth, range at colorimetry.
- Kinokontrol at na-install ng Windows HDR ang pagpili ng asosasyon ng ICC/WCS.
- Isang 15-segundong display preview na may **Keep** / **Revert** at timeout restoration.
- Read-back ng mga pagbabago sa mode/HDR at naiulat na mga pagkabigo sa pagpapanumbalik.
- Hiwalay na pag-uulat ng HDR, SDR na may ACM/WCG at lalim ng kulay ng signal.
- Isang NVRasterPulse launcher para sa isang kwalipikadong hiwalay na naka-install na kopya.

<a id="compatibility"></a>
## Pagkakatugma

| Kinakailangan | Mga Detalye |
| --- | --- |
| Sistema | Windows 10/11 x64 na may katugmang NVIDIA driver |
| Runtime | [.NET Framework 4.8](https://dotnet.microsoft.com/en-us/download/dotnet-framework/net48), ibinibigay ng Windows o naka-install nang hiwalay |
| Mga Pahintulot | Humihiling ang editor ng access ng administrator kapag binuksan |
| Nagpapakita | Ang mga aktwal na mode at kumbinasyon ng kulay ay nakadepende sa GPU, driver, display, cable at Windows na mga API |
| Opsyonal na mga tool | NVRasterPulse para sa RTSS na pamamahala sa limitasyon; hindi ito kailangan o RTSS para sa editor ng Screen |
| Mga wika | Setup: 34-language selector. Pinapanatili ng editor ang kasalukuyang suporta sa wika. |

Walang na-verify na unibersal na minimum na driver o support matrix para sa bawat GPU. Ang mga available na pagpipilian sa bpc ng dialog ay mga kahilingan, hindi mga sertipikadong kumbinasyon. Ang mga modernong kontrol ng HDR at ang mas lumang Windows fallback ay may iba't ibang kakayahan.

<a id="installation"></a>
## Pag-install

1. Buksan ang [pahina ng pag-download](../docs/downloads.md#nvidia-profile-inspector) at tingnan ang katayuan ng publikasyon.
2. I-download ang Setup o portable asset at ihambing ang SHA-256 nito sa Release manifest.
3. Para sa Setup, patakbuhin ang `NVPI-CustomNV-3.0.2.3-Setup-r2.exe`, pumili ng wika at sundin ang installer. Lumilikha ito ng sarili nitong shortcut at uninstaller.
4. Para sa portable, i-extract ang kumpletong ZIP sa isang bagong masusulat na folder. Panatilihin ang `Reference.xml`, ang EXE configuration at lahat ng mga notice sa tabi ng executable.
5. Ilunsad ang `nvidiaProfileInspector.exe`.

Ang pag-install ng editor lamang ay hindi naglalapat ng profile o nag-i-install ng GPU driver. Magkahiwalay na nag-i-install ang kasama, hindi pinapalitan ang mga asosasyon ng `.nip` at hindi pinapagana ang startup sa pag-sign-in. Ang mga kasalukuyang binary ay hindi nalagdaan.

<a id="usage"></a>
## Paggamit

**Ang rebisyon ng installer 2** ay nagdaragdag ng parehong katutubong tagapili ng 34 na wika gaya ng iba pang mga tool, na may mouse/keyboard navigation, maliwanag/madilim na hitsura at pagkansela. Nalalapat ang pagpipilian sa pag-setup; hindi nito isinasalin ang NVPI editor. Ang isang tahasang `/LANG=fr` argument o silent mode ay lumalampas sa pagpili para sa mga tumatawag na nagbibigay na ng wika.

**Mga profile ng driver:** pumili ng profile, mag-export ng backup, pagkatapos ay i-edit lamang ang mga nilalayong setting at ilapat ang mga ito. Tinutukoy ng mga asosasyon ng application kung aling laro ang tumatanggap ng profile. Ang nakaimbak na halaga ay hindi patunay na ginagamit ito ng bawat driver o laro.

**Mga kontrol sa display:** buksan ang **Screen**, piliin ang display at mga hiniling na value, pagkatapos ay simulan ang preview. Suriin ang larawan bago piliin ang **Keep** sa loob ng 15 segundo. Gamitin ang **Revert**, isara ang kumpirmasyon o hayaan itong mag-expire para humiling ng pagpapanumbalik. Basahin ang anumang mensahe ng pagkabigo: ang isang matagumpay na tawag sa API lamang ay hindi patunay ng pagpapanumbalik.

Binabago ng isang ICC na seleksyon ang isang naka-install na asosasyon ng profile; hindi ito bumubuo, nag-calibrate o muling namamahagi ng ICC file. Inilalarawan ng HDR, ACM/WCG, RGB/YCbCr at bpc ang iba't ibang aspeto ng pipeline. Walang ibinigay na bagong independent ACM switch.

**NVRasterPulse:** tumatanggap ang button ng toolbar ng hiwalay na nakarehistrong pag-install sa buong system sa ibaba ng Program Files na may protektadong pagmamay-ari at mga pahintulot. Ang isang portable na kopya o isang user-writable/linked path ay maaaring tanggihan ng nakataas na launcher na ito. Sa kasong iyon, buksan ang NVRasterPulse gamit ang sarili nitong shortcut. [I-install ang RTSS nang hiwalay](https://www.guru3d.com/download/rtss-rivatuner-statistics-server-download/) para gamitin ang NVRasterPulse.

<a id="screenshots"></a>
## Mga screenshot

![NVPI setup revision 2 tagapili ng wika](../../../../assets/screenshots/nvpi-setup-r2-language.png)

Aktwal na tagapili ng setup sa French, nakuha sa panahon ng isang nakahiwalay na pagsubok at pagkatapos ay kinansela. Ipinapakita nito ang installer; pinapanatili ng editor ang interface at dialog ng Screen nito.

<a id="update-and-uninstall"></a>
## I-update at i-uninstall

Isara ang editor bago mag-update. Panatilihin ang mga na-export na profile at i-download ang bagong fork Release; i-install sa ibabaw ng parehong pagkakakilanlan ng kasama o i-extract ang mga portable na file sa isang bagong folder. Huwag paghaluin ang lumang `Reference.xml` sa bagong executable. Ang naka-bundle na upstream update-check suppression ay kabilang sa fork na ito.

Para sa naka-install na kopya, gamitin ang Windows **Installed apps** at ang uninstaller nito. Para sa portable, isara ito at alisin ang na-extract na folder nito kapag ligtas ang iyong mga pag-export. Ang pag-alis sa editor ay **hindi** nag-aalis ng mga pag-edit sa profile ng driver, mga kagustuhan sa pagpapakita, NVRasterPulse o RTSS. Ibalik ang nais na mga setting bago alisin.

<a id="known-limitations"></a>
## Mga kilalang limitasyon

- Ang 15-segundong kumpirmasyon ay hindi isang asong tagapagbantay para sa bawat pagbangga ng driver, pagkawala ng kuryente o sapilitang pagsara.
- Ang ilang kumbinasyon ng kulay/depth/refresh ay nagbabalik ng `NVAPI_NOT_SUPPORTED`.
- Hindi sinusukat ng software read-back ang lalim ng bit ng panel, katumpakan ng kulay o latency.
- Naaapektuhan ng mga setting ng screen ang kasalukuyang display ng Windows; ang dialog na ito ay hindi gumagawa ng per-game display preset.
- Walang performance, anti-cheat o universal HDR compatibility guarantee.

<a id="troubleshooting"></a>
## Pag-troubleshoot

| Sintomas | Aksyon |
| --- | --- |
| Error sa runtime sa paglulunsad | Suriin ang Windows update at .NET Framework 4.8; gamitin ang kumpletong pakete. |
| Tinanggihan ang hiniling na display mode | I-revert at subukan ang isang mode na inaalok ng Windows/NVIDIA para sa display na iyon. Basahin ang eksaktong error at iwasan ang paulit-ulit na bulag na pagbabago. |
| HDR o kulay ay bumalik sa lumang estado | Suriin kung nabigo ang isa pang operasyon at nag-trigger ng pagpapanumbalik; makilala ang HDR mula sa ACM. |
| Ang pindutan ng NVRasterPulse ay tumatanggi sa isang landas | Ilunsad ang sarili nitong shortcut; ang button na ito ay nangangailangan ng protektadong pag-install sa buong system. |
| Nananatili ang pagbabago pagkatapos i-uninstall | Ibalik ang na-export na NVIDIA profile o ang nilalayong Windows na mga setting ng display; ang pag-uninstall ay hindi isang rollback ng mga setting. |

Tingnan ang [nakabahaging gabay sa suporta](../docs/support.md) bago magpadala ng mga log.

<a id="faq"></a>
## FAQ

**Opisyal ba itong NVIDIA software o opisyal na build ng Orbmu2k?** Hindi. Ito ay isang independiyenteng fork; ang upstream na may-akda at lisensya ng MIT ay nananatiling kredito.

**Kinakailangan ba ng NVDriverForge ang editor na ito?** Hindi. Ang opsyonal na Custom NV na preset ng Custom NV ay gumagamit ng sarili nitong pagsasama. Ang pag-install ng editor ay isang hiwalay na pagpipilian.

**Ang RTSS ba ay mandatory para sa fork na ito?** Hindi. Ang RTSS ay mandatory para sa NVRasterPulse na limiter ng FPS, hindi para sa pag-edit ng profile o Screen.

**Nasaan ang pinagmulan?** Ang binagong pinagmulan ng application ay pinananatili nang pribado. Ang MIT notice at upstream repository ay ibinigay; Ang MIT ay hindi nangangailangan ng pag-publish ng binagong pinagmulan.

<a id="upstream-and-changes"></a>
## Upstream at pagbabago

Upstream: [Orbmu2k/nvidiaProfileInspector](https://github.com/Orbmu2k/nvidiaProfileInspector), reference commit `592d962cca8827efe8859461a84267755595064a`. [Mga orihinal na pag-download](https://github.com/Orbmu2k/nvidiaProfileInspector/releases).

Namana: editor ng profile, NVAPI interop, data ng sanggunian, mga mapagkukunan ng UI at mga tema. Idinagdag o inangkop ng 禅堂 Zendo (RevoluSound Team) ang mga serbisyo sa pagpapakita, mga transaksyong HDR/ICC, 15 segundong pagkumpirma/pagbasa-balik, layout ng toolbar at gawi sa paglulunsad ng RasterPulse. Ang nalinis na kasama ay hindi kasama ang mga development mocks/test entry point, gumagamit ng protektadong external launcher at nagbibigay ng hiwalay na installer. Ang lumang pinagsamang NVPI/RasterPulse development package ay hindi ang kandidato sa hub na ito.

[Detalyadong pinagmulan ng file](../docs/provenance.md) · [Orihinal na abiso ng fork](../../../../NVIDIA-Profile-Inspector/LICENSES/ORIGINAL-FORK-NOTICE.txt)

<a id="credits-and-license"></a>
## Mga kredito at lisensya

Copyright (c) 2016 Orbmu2k. Ang ibinigay na [Lisensya ng MIT](../../../../NVIDIA-Profile-Inspector/LICENSE) ay pinanatili. Mga adaptasyon at packaging: 禅堂 Zendo (RevoluSound Team). Ang installer ay gumagamit ng Inno Setup; Nananatiling panlabas ang Windows at .NET Framework. [Buong naaangkop na mga paunawa](LICENSES/README.md).

Independiyente sa, hindi ini-sponsor ng, at hindi opisyal na iniendorso ng NVIDIA Corporation. Ang mga trademark ay nananatili sa kani-kanilang mga may-ari.
