<!-- nv-language-navigation:start -->
🌐 [English](../../../../NVRasterPulse/README.md) | [Français](../../../../NVRasterPulse/README.fr.md) · [NV Laboratory](../README.md)

<details>
<summary>🌐 Language · 34</summary>

[العربية](../../ar/NVRasterPulse/README.md) · [বাংলা](../../bn/NVRasterPulse/README.md) · [简体中文](../../zh/NVRasterPulse/README.md) · [Čeština](../../cs/NVRasterPulse/README.md) · [Dansk](../../da/NVRasterPulse/README.md) · [Nederlands](../../nl/NVRasterPulse/README.md) · [English](../../../../NVRasterPulse/README.md) · **Filipino** · [Suomi](../../fi/NVRasterPulse/README.md) · [Français](../../../../NVRasterPulse/README.fr.md) · [Deutsch](../../de/NVRasterPulse/README.md) · [Ελληνικά](../../el/NVRasterPulse/README.md) · [हिन्दी](../../hi/NVRasterPulse/README.md) · [Magyar](../../hu/NVRasterPulse/README.md) · [Bahasa Indonesia](../../id/NVRasterPulse/README.md) · [Italiano](../../it/NVRasterPulse/README.md) · [日本語](../../ja/NVRasterPulse/README.md) · [한국어](../../ko/NVRasterPulse/README.md) · [मराठी](../../mr/NVRasterPulse/README.md) · [فارسی](../../fa/NVRasterPulse/README.md) · [Polski](../../pl/NVRasterPulse/README.md) · [Português](../../pt/NVRasterPulse/README.md) · [ਪੰਜਾਬੀ](../../pa/NVRasterPulse/README.md) · [Română](../../ro/NVRasterPulse/README.md) · [Русский](../../ru/NVRasterPulse/README.md) · [Español](../../es/NVRasterPulse/README.md) · [Kiswahili](../../sw/NVRasterPulse/README.md) · [Svenska](../../sv/NVRasterPulse/README.md) · [தமிழ்](../../ta/NVRasterPulse/README.md) · [ไทย](../../th/NVRasterPulse/README.md) · [Türkçe](../../tr/NVRasterPulse/README.md) · [Українська](../../uk/NVRasterPulse/README.md) · [اردو](../../ur/NVRasterPulse/README.md) · [Tiếng Việt](../../vi/NVRasterPulse/README.md)

[Translation policy](../../README.md)

</details>
<!-- nv-language-navigation:end -->

<!-- nv-translation-notice:start -->
> Pagsasalin na tinulungan ng makina mula sa Ingles. Ang mga teknikal na pangalan, utos, URL at orihinal na legal na teksto ay pinapanatili. Malugod na tinatanggap ang pagsusuri ng katutubong nagsasalita; kumonsulta sa sangguniang Ingles kung ang mga salita ay hindi malinaw.
<!-- nv-translation-notice:end -->

<a id="nvrasterpulse"></a>
# NVRasterPulse

**Per-application FPS limitasyon sa pamamagitan ng RivaTuner Statistics Server.**

> **I-install muna ang RTSS.** Ang NVRasterPulse ay nangangailangan ng [RivaTuner Statistics Server (RTSS), na-download mula sa Guru3D](https://www.guru3d.com/download/rtss-rivatuner-statistics-server-download/). Dapat na tumatakbo ang RTSS upang ipatupad ang mga limitasyon. Walang RTSS installer, hook DLL o SDK na naka-bundle.

[I-download ang 0.1 at katayuan](../docs/downloads.md#nvrasterpulse) · [Pag-install](#installation) · [Paano gumagana ang mga limitasyon](#usage) · [Lisensya](../../../../NVRasterPulse/LICENSE)

<a id="overview-and-purpose"></a>
## Pangkalahatang-ideya at layunin

Ang NVRasterPulse ay isang compact na interface ng Windows para sa pamamahala ng mga limitasyon ng frame ng RTSS ayon sa executable na pangalan. Ginagawa ng RTSS ang paglilimita. Pinamamahalaan ng NVRasterPulse ang mga kaukulang value ng profile, pag-backup at mga kahilingan sa pag-reload, na may access sa tray at patuloy na mga pagpipilian.

Umiiral ito upang gawing mas madaling i-edit ang mga eksaktong limitasyon sa bawat laro nang hindi pinapalitan ang isang buong profile ng RTSS o nakakagambala sa mga setting ng overlay nito. Ang kasalukuyang kandidato na **0.1** ay ang September 9, 2026 build na may kinakailangang RTSS installation check.

<a id="features"></a>
## Mga tampok

- Pumili ng tumatakbong application o idagdag ang executable nito nang manu-mano.
- I-save ang mga limitasyon ng FPS mula 1 hanggang 1000, na may hanggang tatlong decimal na lugar.
- Eksaktong nakapangangatwiran na pag-encode ng mga inilagay na value: Ang 59.94 ay nagiging 2997/50.
- Configuration ng Front Edge Sync (`SyncLimiter=1`) na may aktibong paghihintay (`PassiveWait=0`).
- Per-executable na mga update sa profile, awtomatikong pag-backup at atomic na pagsusulat.
- Ang pag-alis ng limiter ay na-override habang pinapanatili ang iba pang nilalaman ng profile.
- RTSS installation detection, manual na pagpili ng path at tahasang paglulunsad/reload.
- Single-instance tray operation, opsyonal na naka-install na startup, 34 na wika at apat na tema.
- Paghiwalayin ang mga normal na quit at **Quit + RTSS** na mga aksyon.

<a id="compatibility"></a>
## Pagkakatugma

| Kinakailangan | Mga Detalye |
| --- | --- |
| Sistema | Windows 10/11 x64 |
| Runtime | [.NET Framework 4.8](https://dotnet.microsoft.com/en-us/download/dotnet-framework/net48), naka-install nang hiwalay kung kinakailangan |
| Kinakailangang software | RTSS na may `RTSS.exe`, isang tumutugmang direktoryo ng `Profiles` at katugmang profile/reload na suporta |
| GPU | Tinutukoy ng compatibility ng RTSS ang limiter; ang tagapamahala ng profile na ito ay hindi nangangailangan ng partikular na henerasyon ng RTX |
| Mga Pahintulot | Ang kasalukuyang application ay humihiling ng pag-access ng administrator; ang napiling folder ng profile na RTSS ay dapat ma-access |
| Mga laro | Depende sa RTSS hooking support at mga paghihigpit sa bawat laro; walang garantiyang anti-cheat |

Walang partikular na RTSS na minimum na bersyon ang na-certify para sa bawat function ng hub audit na ito. Gamitin ang opisyal na kasalukuyang distribusyon at iulat ang eksaktong bersyon kung hindi gumagana ang profile key/reload. Ang naka-install-ngunit-tinigil na RTSS ay pumasa sa tseke ng pag-install; dapat na itong simulan para sa aktwal na paglilimita.

<a id="installation"></a>
## Pag-install

1. **[I-download at i-install ang RTSS mula sa Guru3D](https://www.guru3d.com/download/rtss-rivatuner-statistics-server-download/).**
2. Buksan ang [Mga pag-download ng NVRasterPulse](../docs/downloads.md#nvrasterpulse) at tingnan ang availability ng Paglabas.
3. I-download ang `NVRasterPulse-0.1-win-x64-Setup.exe` o `NVRasterPulse-0.1-win-x64-portable.zip`, kasama ang mga notice/checksum.
4. Ihambing ang SHA-256. Patakbuhin ang Setup o i-extract ang buong portable ZIP sa isang nasusulat na lokal na folder.
5. Buksan ang `NVRasterPulse.exe`. Kung nawawala ang RTSS, gamitin ang **Download RTSS**, i-install ito, pagkatapos ay **Suriin muli**, o manu-manong piliin ang `RTSS.exe`.
6. Simulan ang RTSS gamit ang normal na shortcut nito o ang NVRasterPulse na button ng RTSS kung ito ay itinigil.

Ang pag-off sa opsyonal na paalala ay hindi laktawan ang kinakailangang pagsusuri. Ang isang tahimik na Windows tray startup ay naghihintay hanggang sa magbukas ang pangunahing window bago ipakita ang tseke na ito. Ang setup ay nag-i-install lamang ng NVRasterPulse. Ang mga EXE nito ay hindi pinirmahan.

<a id="usage"></a>
## Paggamit

1. Piliin ang nilalayong tumatakbong application o mag-browse sa EXE ng laro nito.
2. Maglagay ng limitasyon sa pagitan ng 1 at 1000 FPS, kasama ang fractional value kung kinakailangan.
3. I-save at suriin ang naiulat na resulta. Ina-update ng NVRasterPulse ang profile ng RTSS na iyon ng executable at humihiling ng reload.
4. Kumpirmahin na tumatakbo ang RTSS at i-verify ang gawi sa nilalayon na laro.

Ang mga profile ay inilalagay sa pamamagitan ng **executable name**, gaya ng `Game.exe.cfg`. Dalawang magkaibang folder na naglalaman ng `Game.exe` ay nagbabahagi ng parehong profile na RTSS; hindi inaalis ng pag-iimbak ng buong landas ang banggaan na ito.

Ang pag-save ay gumagamit ng Front Edge Sync at aktibong paghihintay. Ang aktibong paghihintay ay maaaring tumaas ang paggamit ng CPU. Ang mga kahaliling `LimitTime` na field ay neutralisado. Ang mga kasalukuyang komento, mga setting ng overlay at `EnableHooking=0` ay pinapanatili. Ang RTSS Global na profile ay hindi nabago.

Gamitin ang trash action para alisin ang mga override ng limiter ng NVRasterPulse. Hindi nito tinatanggal ang buong profile ng RTSS. Ang limitasyon na minana mula sa RTSS Global o ibang tool ay maaari pa ring malapat pagkatapos.

**Pagsasara at pagtigil:** ang pangunahing window ay maaaring magtago sa tray. Ang normal na **Quit** ay iniiwan ang RTSS na tumatakbo at ang mga naka-save na limitasyon ay buo. **Quit + RTSS** humihiling ng normal na pagsasara ng tumutugmang proseso ng RTSS sa kasalukuyang session, naghihintay ng hanggang walong segundo at hindi ito pinipilit na patayin. Nananatili ang mga nakaimbak na limitasyon sa parehong mga kaso.

Pinipili ang wika at tema sa app. Ang pagsisimula sa Windows sign-in ay opsyonal at nilayon para sa isang naka-install na kopya. Ipinapaliwanag ng button ng impormasyon ang mga karaniwang pagkilos.

<a id="screenshots"></a>
## Mga screenshot

![NVRasterPulse main-window preview](../../../../assets/screenshots/nvrasterpulse-0.1-preview.png)

Umiiral na French 0.1 UI render na may mga halimbawang executable na pangalan at isang 176 FPS value. Ang RTSS ay ipinapakita na huminto; isa itong paglalarawan ng interface, hindi isang running limiter o latency measurement. [Pinagmulan ng imahe](../assets/README.md).

<a id="update-and-uninstall"></a>
## I-update at i-uninstall

Ihinto ang NVRasterPulse, i-download at i-verify ang bagong bersyon, pagkatapos ay patakbuhin ang Setup nito o i-extract ang portable sa isang bagong folder. Panatilihin ang mga setting at RTSS backup. Ang mga update ng RTSS ay hiwalay at nagmula sa Guru3D.

Upang mag-alis ng naka-install na kopya, gamitin ang Windows **Installed apps**. Para sa portable, huminto pagkatapos ay alisin ang na-extract na folder nito kapag ligtas ang iyong mga backup. Ang mga naka-save na limitasyon ng RTSS ay hindi inaalis sa pamamagitan ng pag-uninstall sa NVRasterPulse: alisin muna ang mga nilalayong pag-override ng limiter. Ang RTSS ay may sariling uninstaller.

Lokal na estado: `%LOCALAPPDATA%\NVRasterPulse`. Mga awtomatikong pag-backup ng RTSS: `%LOCALAPPDATA%\NVRasterPulse\Backups\RTSS`. Maaaring basahin ang isang mas lumang lokasyon ng `%LOCALAPPDATA%\RTSSProfileBridge` para sa paglipat. Ang mga file na ito ay maaaring maglaman ng mga personal na executable path at hindi dapat i-post sa publiko.

<a id="known-limitations"></a>
## Mga kilalang limitasyon

- Ginagawa ng RTSS ang cap. Ang isang naka-save na halaga o matagumpay na kahilingan sa pag-reload ay hindi isang nasusukat na resulta ng frame-time.
- Ang mga executable na may parehong pangalan ay nagbabahagi ng profile.
- Ang isa pang global/per-game limiter ay maaaring makaapekto sa resulta; hindi nag-aalis ng minanang cap ang hindi pagpapagana sa lokal na override.
- Ang isang sadyang hindi pinagana na RTSS hook ay nananatiling hindi pinagana.
- Ang aktibong paghihintay ay may CPU/power trade-off.
- Walang unibersal na laro, anti-cheat o end-to-end latency validation.
- Ang naunang experimental independent limiter engine ay hindi pinagsama-sama o naipadala.
- Ang mga awtomatikong backup ay hindi nagpapahiwatig ng isang pag-click na buong backup-restore na interface.

<a id="troubleshooting"></a>
## Pag-troubleshoot

| Sintomas | Aksyon |
| --- | --- |
| Ang RTSS ay nananatiling bukas | Piliin ang aktwal na `RTSS.exe` at tumutugma sa folder ng Mga Profile, pagkatapos ay Suriin muli. |
| Na-save ang limitasyon ngunit walang epekto | Simulan ang RTSS; i-verify ang tamang EXE/profile ng laro, mga pahintulot sa hook at iba pang mga limiter. |
| Nabigo ang pag-save | Suriin ang mga pahintulot sa folder at panatilihin ang ipinapakitang error/backup. |
| Nananatili ang limitasyon pagkatapos alisin | Siyasatin ang RTSS Global at iba pang mga tool; inaalis lang ng pagkilos ng basura ang mga lokal na override ng limiter. |
| Dalawang laro ang tumatanggap ng parehong limitasyon | Suriin kung ang kanilang mga executable filename ay magkapareho. |
| Ang Quit + RTSS ay umalis sa RTSS na bukas | Isara ang RTSS nang normal sa iyong sarili; ang utos na ito ay sadyang umiiwas sa sapilitang pagwawakas. |

Kung manu-manong nire-restore ang isang backup na RTSS, isara muna ang RTSS at panatilihin ang kasalukuyang profile bago ito palitan ng nilalayong backup. Maaari nitong i-overwrite ang hindi nauugnay na mga pag-edit sa profile; suriin ang file at petsa. [Nakabahaging suporta](../docs/support.md).

<a id="faq"></a>
## FAQ

**Kailangan ko rin ba ng MSI Afterburner?** Ang NVRasterPulse ay nangangailangan ng RTSS; hindi ito nakadepende sa Afterburner application. Sundin ang mga opsyon sa pag-install ng distributor ng RTSS.

**Maaari ko bang gamitin ito nang hindi tumatakbo ang RTSS?** Maaari mong pamahalaan ang mga profile kapag may nakitang pag-install, ngunit dapat tumakbo ang RTSS para sa paglilimita.

**Ang pagtigil o pag-uninstall ba ay nag-aalis ng mga takip?** Hindi. Alisin ang gustong limiter ay tahasang nag-o-override bago alisin ang NVRasterPulse.

**Ito ba ay isang fork ng RTSS?** Hindi. Ito ay isang independiyenteng tagapamahala ng profile; walang RTSS source o executable na kasama.

<a id="upstream-modifications-and-credits"></a>
## Upstream, mga pagbabago at mga kredito

Ang development repository ay nagmula sa [Orbmu2k's NVIDIA Profile Inspector](https://github.com/Orbmu2k/nvidiaProfileInspector). Ang MIT palettes/UI resources nito ay kredito. Ang mga serbisyo sa pamamahala ng profile, fraction encoding, backup, RTSS reload bridge, tray behavior, prerequisite na gabay, mga wika at application-specific na icon ay binuo/na-adapt ng 禅堂 Zendo (RevoluSound Team).

Ang RTSS ay binuo ni **Unwinder** at ibinahagi nang hiwalay sa pamamagitan ng Guru3D. Ang NVRasterPulse ay tumatawag sa `UpdateProfiles` mula sa napiling naka-install na hook DLL; walang RTSS SDK o hook binary na muling ipinamahagi. Gumagamit ang installer ng hindi nabagong Inno Setup 7.1.0 na may mga inangkop na script/translation at isang project bootstrap.

[Buong pinagmulan](../docs/provenance.md) · [Third-party na talahanayan](../THIRD_PARTY_NOTICES.md)

<a id="license"></a>
## Lisensya

Ang package ay tahasang namamahagi ng NVRasterPulse sa ilalim ng ibinigay na [Lisensya ng MIT](../../../../NVRasterPulse/LICENSE), na pinapanatili ang Copyright (c) 2016 Orbmu2k. Ang pinagmulan ng aplikasyon ay pinananatili nang pribado; Ang MIT ay hindi nangangailangan ng paglalathala ng binagong pinagmulan. Ang RTSS at Windows/.NET ay nananatili sa ilalim ng kanilang sariling mga tuntunin. [Buong abiso](LICENSES/README.md).

Independent ng NVIDIA Corporation, MSI at RTSS; hindi itinataguyod o opisyal na inendorso nila. Ang mga pangalan ng produkto ay nananatiling trademark ng kanilang mga may-ari.
