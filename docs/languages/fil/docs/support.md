<!-- nv-language-navigation:start -->
🌐 [English](../../../support.md) | [Français](../../../support.fr.md) · [NV Laboratory](../README.md)

<details>
<summary>🌐 Language · 34</summary>

[العربية](../../ar/docs/support.md) · [বাংলা](../../bn/docs/support.md) · [简体中文](../../zh/docs/support.md) · [Čeština](../../cs/docs/support.md) · [Dansk](../../da/docs/support.md) · [Nederlands](../../nl/docs/support.md) · [English](../../../support.md) · **Filipino** · [Suomi](../../fi/docs/support.md) · [Français](../../../support.fr.md) · [Deutsch](../../de/docs/support.md) · [Ελληνικά](../../el/docs/support.md) · [हिन्दी](../../hi/docs/support.md) · [Magyar](../../hu/docs/support.md) · [Bahasa Indonesia](../../id/docs/support.md) · [Italiano](../../it/docs/support.md) · [日本語](../../ja/docs/support.md) · [한국어](../../ko/docs/support.md) · [मराठी](../../mr/docs/support.md) · [فارسی](../../fa/docs/support.md) · [Polski](../../pl/docs/support.md) · [Português](../../pt/docs/support.md) · [ਪੰਜਾਬੀ](../../pa/docs/support.md) · [Română](../../ro/docs/support.md) · [Русский](../../ru/docs/support.md) · [Español](../../es/docs/support.md) · [Kiswahili](../../sw/docs/support.md) · [Svenska](../../sv/docs/support.md) · [தமிழ்](../../ta/docs/support.md) · [ไทย](../../th/docs/support.md) · [Türkçe](../../tr/docs/support.md) · [Українська](../../uk/docs/support.md) · [اردو](../../ur/docs/support.md) · [Tiếng Việt](../../vi/docs/support.md)

[Translation policy](../../README.md)

</details>
<!-- nv-language-navigation:end -->

<!-- nv-translation-notice:start -->
> Pagsasalin na tinulungan ng makina mula sa Ingles. Ang mga teknikal na pangalan, utos, URL at orihinal na legal na teksto ay pinapanatili. Malugod na tinatanggap ang pagsusuri ng katutubong nagsasalita; kumonsulta sa sangguniang Ingles kung ang mga salita ay hindi malinaw.
<!-- nv-translation-notice:end -->

<a id="compatibility-and-troubleshooting"></a>
# Pagkakatugma at pag-troubleshoot

Ito ang mga inihandang kandidato, hindi isang certification matrix para sa lahat ng Windows, GPU, driver at mga kumbinasyon ng laro.

| Tool | Windows / runtime | Hardware / panlabas na dependency | Mga operasyon na nangangailangan ng pangangalaga |
| --- | --- | --- | --- |
| NVPI fork 3.0.2.3 | Windows 10/11 x64, .NET Framework 4.8 | Mga katugmang NVIDIA driver/display | Nagsusulat ang profile at nagpapakita ng mga preview |
| NVDriverForge 0.1.2 | Windows 10 build 19041+ / 11 x64; Kasama ang .NET/WPF | Mga katugmang NVIDIA driver package | Nakataas na pag-install, mga advanced na setting, opsyonal na NVENC |
| NVMFG Unlock40 0.1.1 | Windows 10/11 x64; Kasama ang .NET/WPF, mga katulong ng Framework 4.8 | RTX 40, kwalipikadong DLSS FG na laro at naka-pin na provider | Native in-game patching, global profile journal, SDK na mga update sa laro |
| NVRasterPulse 0.1 | Windows 10/11 x64, .NET Framework 4.8 | Naka-install ang RTSS; tumatakbo para sa caps | RTSS per-executable na mga pagbabago sa profile |

Walang ARM64 package na inihanda. Ang availability ng Display/API at mga lumang bersyon ng Windows ay maaaring maglimita sa mga indibidwal na feature. Walang unibersal na minimum na NVIDIA o RTSS na bersyon ang naimbento. Ang eksaktong NVMFG provider hash ay nasa [pinanggalingan](provenance.md).

<a id="before-reporting-a-bug"></a>
## Bago mag-ulat ng isang bug

Tukuyin ang eksaktong executable/bersyon na iyong binuksan. Ang isang nakaraang naka-install na kopya ay hindi nangangahulugang ang bersyon ng isang bagong na-download na ZIP. Itala ang mga hakbang sa pagpaparami, inaasahang resulta at aktwal na resulta. Para sa mga isyu sa pag-render/paglilimita, isama ang bersyon ng laro, pag-refresh ng display, estado ng FG/V-Sync/VRR at anumang iba pang limiter o overlay.

Gamitin ang [form ng bug](https://github.com/Zendo-GIT/NV-Laboratory/issues/new?template=bug-report.yml). Huwag kailanman mag-attach ng buong folder ng pribadong development, archive ng driver, modelo, DLL ng laro, registry dump o hindi pa nasuri na koleksyon ng log.

| Problema | Mga unang pagsusuri |
| --- | --- |
| Maling bersyon ng application | Kumpirmahin ang pagkakakilanlan ng EXE at Ilabas ang hash; isara ang mas lumang kopya bago palitan. |
| Error sa runtime/startup | I-install ang kinakailangang Framework 4.8 o panatilihin ang lahat ng ibinigay na portable subfolder. |
| Kinansela ang UAC | Subukang muli lamang ang nilalayong operasyon; hindi matagumpay na pag-install ang pagkansela. |
| Hash/signature mismatch | Itigil ang paggamit sa kandidatong iyon at kunin ang inaasahang opisyal na byte. |
| Tinanggihan ang kulay/mode ng NVPI | Ibalik at gumamit ng kumbinasyong sinusuportahan ng aktwal na display/driver. |
| NVDF backup o recovery failure | Panatilihin ang protektadong trabaho at RECOVERY.txt; huwag burahin ang journal o pilitin ang magkasalungat na pagsusulat. |
| Mga nakabinbing setting ng NVMFG | Lutasin ang pagbawi nang sarado ang mga laro, pinapanatili ang mga pagbabago mula sa iba pang mga tool. |
| Walang epekto ang cap ng RP | Patakbuhin ang RTSS, tukuyin ang totoong EXE ng laro, suriin ang katayuan ng hook at mga limitasyon sa pakikipagkumpitensya. |
| Ang takip ng RP ay nagpapatuloy pagkatapos alisin | Siyasatin ang RTSS Global; ang mga pagbabago sa pag-alis ay mga lokal na limitasyon ng override lamang. |

<a id="logs-and-privacy"></a>
## Mga log at privacy

| Tool | Lokal na data upang suriin, hindi mag-upload ng pakyawan |
| --- | --- |
| NVDF | `%LOCALAPPDATA%\NVDriverForge`; mga protektadong trabaho `%PROGRAMDATA%\NVDriverForge\Jobs` |
| NVMFG | `%LOCALAPPDATA%\RtxMfg`; mga backup na `%LOCALAPPDATA%\NvidiaStreamlineMaintenance\Backups`; `Sessions` sa tabi ng EXE |
| RP | `%LOCALAPPDATA%\NVRasterPulse`; `Backups\RTSS` sa ibaba nito |
| NVPI | Ang iyong mga napiling pag-export at ang ipinakitang error; walang naimbentong unibersal na landas ng log |

Alisin ang mga pangalan ng account, home directory, game-library path, device identifier, token at hindi nauugnay na mga window mula sa text/mga larawang ibinabahagi mo. Panatilihing pribado ang mga orihinal para sa pagbawi. Ang mga Pampublikong Isyu ay nakikita ng lahat.

Para sa isang kahinaan, mapanganib na may pribilehiyong pag-uugali o hindi sinasadyang mapanirang operasyon, sundin ang [SECURITY.md](../SECURITY.md) sa halip na mag-post ng mga detalye sa publiko.

<a id="what-has-been-verified"></a>
## Kung ano ang na-verify

Para sa paghahanda ng hub, ang mga static na payload/ZIP/hash/metadata scan at mga pagsusuri sa dokumentasyon ay pinatakbo. Ang mga kasalukuyang pagsubok sa build/unit/UI ng pribadong application ay makasaysayan at may petsang ebidensya. Walang pag-install ng driver, pagpapalit ng display, live na operasyon ng RTSS o benchmark ng laro na ginawa bilang bahagi ng paghahandang ito.

Ang "natukoy", "nakasulat", "na-reload", "magagamit ang kakayahan" at "nasusukat sa laro" ay magkaibang mga resulta. Iulat kung alin ang iyong naobserbahan.
