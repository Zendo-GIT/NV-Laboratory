<!-- nv-language-navigation:start -->
🌐 [English](../../../../NVDriverForge/README.md) | [Français](../../../../NVDriverForge/README.fr.md) · [NV Laboratory](../README.md)

<details>
<summary>🌐 Language · 34</summary>

[العربية](../../ar/NVDriverForge/README.md) · [বাংলা](../../bn/NVDriverForge/README.md) · [简体中文](../../zh/NVDriverForge/README.md) · [Čeština](../../cs/NVDriverForge/README.md) · [Dansk](../../da/NVDriverForge/README.md) · [Nederlands](../../nl/NVDriverForge/README.md) · [English](../../../../NVDriverForge/README.md) · **Filipino** · [Suomi](../../fi/NVDriverForge/README.md) · [Français](../../../../NVDriverForge/README.fr.md) · [Deutsch](../../de/NVDriverForge/README.md) · [Ελληνικά](../../el/NVDriverForge/README.md) · [हिन्दी](../../hi/NVDriverForge/README.md) · [Magyar](../../hu/NVDriverForge/README.md) · [Bahasa Indonesia](../../id/NVDriverForge/README.md) · [Italiano](../../it/NVDriverForge/README.md) · [日本語](../../ja/NVDriverForge/README.md) · [한국어](../../ko/NVDriverForge/README.md) · [मराठी](../../mr/NVDriverForge/README.md) · [فارسی](../../fa/NVDriverForge/README.md) · [Polski](../../pl/NVDriverForge/README.md) · [Português](../../pt/NVDriverForge/README.md) · [ਪੰਜਾਬੀ](../../pa/NVDriverForge/README.md) · [Română](../../ro/NVDriverForge/README.md) · [Русский](../../ru/NVDriverForge/README.md) · [Español](../../es/NVDriverForge/README.md) · [Kiswahili](../../sw/NVDriverForge/README.md) · [Svenska](../../sv/NVDriverForge/README.md) · [தமிழ்](../../ta/NVDriverForge/README.md) · [ไทย](../../th/NVDriverForge/README.md) · [Türkçe](../../tr/NVDriverForge/README.md) · [Українська](../../uk/NVDriverForge/README.md) · [اردو](../../ur/NVDriverForge/README.md) · [Tiếng Việt](../../vi/NVDriverForge/README.md)

[Translation policy](../../README.md)

</details>
<!-- nv-language-navigation:end -->

<!-- nv-translation-notice:start -->
> Pagsasalin na tinulungan ng makina mula sa Ingles. Ang mga teknikal na pangalan, utos, URL at orihinal na legal na teksto ay pinapanatili. Malugod na tinatanggap ang pagsusuri ng katutubong nagsasalita; kumonsulta sa sangguniang Ingles kung ang mga salita ay hindi malinaw.
<!-- nv-translation-notice:end -->

<a id="nvdriverforge"></a>
# NVDriverForge

**Maghanda ng NVIDIA na pag-install ng driver na may malinaw na mga pagpipilian sa bahagi at mga opsyonal na setting.**

[I-download ang 0.1.3 at katayuan](../docs/downloads.md#nvdriverforge) · [Pag-install](#installation) · [Mga kredito](#credits-and-upstream) · [Lisensya](../../../../NVDriverForge/LICENSE)

<a id="overview-and-purpose"></a>
## Pangkalahatang-ideya at layunin

Ginagabayan ka ng NVDriverForge sa isang orihinal na package ng driver ng NVIDIA: piliin ang driver, suriin ang mga bahagi nito, suriin ang mga opsyonal na pag-aayos, pagkatapos ay kumpirmahin ang pag-install. Umiiral ito upang gawing nauunawaan ang mga pagpipiliang iyon at panatilihing magkasama ang pag-install, mga privileged na operasyon at impormasyon sa pagbawi.

Ito ay isang independiyenteng binuo na application na inspirasyon sa bahagi ng daloy ng trabaho ng NVCleanstall. Hindi kasama dito ang NVCleanstall o pag-claim ng kumpletong parity ng feature.

<a id="features"></a>
## Mga tampok

- NVIDIA Game Ready / Studio paghahanap at pag-download; opsyonal na pagtuklas ng hotfix na may manu-manong fallback.
- Pagsusuri ng orihinal na pakete, mga hash, mga lagda ng NVIDIA, mga manifest, at mga katugmang INF na mga entry.
- Pagpili ng bahagi na may mga dependency at pangangalaga ng hindi kilalang mga bahagi.
- Pinapanatili ng Bersyon ng 0.1.3 ang mga napiling opsyonal na bahagi ng NVIDIA na nalalaktawan at hindi kasama ang mga na-verify na hindi naka-check na bahagi mula sa pagtuklas. Ang kasalukuyan na o hindi nalalapat na mga opsyonal na runtime ay hindi na pinipilit bilang mga kritikal na bahagi.
- I-clear ang mga buod ng pagkabigo sa pag-install at pag-access sa mga detalyadong log sa lahat ng 34 na wika.
- Tahasang kumpirmasyon sa pag-install, protektadong pagtatanghal ng dula at pag-export ng mga umiiral nang driver-store packages.
- Opsyonal na mga advanced na setting, na may mga pagsusuri sa preflight, mga journal at pagbawi na may kamalayan sa salungatan.
- Opsyonal **Custom NV** preset na may pinangalanang mga pagpipilian at paliwanag, kabilang ang isang hiwalay na SILK pagpili ng lakas at mga pagsusuri sa compatibility.
- Opsyonal eksaktong-bersyon NVENC pag-download ng patch; sinusuri ang source commit at target byte.
- Isang hiwalay, opsyonal na pag-install ng Profile Inspector fork mula sa screen ng Tools.
- Opsyonal na mga pagsusuri sa pag-update ng naka-install na user, 34 na wika ng interface at apat na tema.

Ang mga available na advanced na opsyon ay may kinalaman sa MPO, ang DLSS indicator, Ansel, NVIDIA audio sleep, MSI, interrupt policy/priority, HDCP, display-container startup at isang kwalipikadong legacy telemetry service. Ang bawat isa ay may sariling mga kinakailangan at epekto; hindi ito mga pangkalahatang pagpapahusay sa pagganap.

<a id="compatibility"></a>
## Pagkakatugma

| Kinakailangan | Mga Detalye |
| --- | --- |
| Sistema | Windows 10 build 19041 o mas bago / Windows 11, x64 |
| GPU/driver | Mga katugmang NVIDIA package at nakitang hardware; Pangunahing sinasaklaw ng awtomatikong paghahanap ng catalog ang mga kilalang modelong GeForce |
| Runtime | .NET 8 / WPF 8.0.31 kasama sa inihandang self-contained na package |
| Mga Pribilehiyo | Normal na UI/per-user setup; ang pag-install ng driver at mga pagbabago sa system ay humiling ng pag-access ng administrator |
| Network | Kinakailangan para sa online na paghahanap/pag-download ng NVIDIA at tahasang mga kahilingan sa upstream na NVENC; maaaring pumili ng lokal na orihinal na driver |
| Kasama ang mga tool | Hindi nabagong 7-Zip 26.03, mga runtime notice, opsyonal na MIT Profile Inspector na kasama |
| Opsyonal na kasama | .NET Framework 4.8 para sa hiwalay na Profile Inspector fork |

Walang arbitrary na minimum na bersyon ng driver ang sumasaklaw sa lahat ng feature. Dapat tumugma ang Multi-GPU lookup sa bawat nakitang GPU. Maaaring mangailangan ng manu-manong pagpili ng driver ang mga hindi sinusuportahan/propesyonal na modelo. Ang installer ng NVIDIA ay nananatiling panghuling awtoridad sa hardware/OS.

<a id="installation"></a>
## Pag-install

1. Bisitahin ang [mga download](../docs/downloads.md#nvdriverforge) at kumpirmahin na ang Paglabas ay nai-publish.
2. Piliin ang `NVDriverForge-Setup.exe` para sa pag-install, o `NVDriverForge.exe` para sa portable na paggamit.
3. Ihambing ang SHA-256 sa `SHA256SUMS.txt` ng Release.
4. Patakbuhin ang Setup para sa pag-install ng bawat user at karaniwang uninstaller, o ilagay ang portable EXE sa isang masusulat na folder at buksan ito.

Kasama sa portable ang runtime nito at ang opsyonal na installer nito. Ang pag-install ng NVDriverForge ay hindi nag-i-install ng GPU driver. Ang mga EXE nito ay kasalukuyang hindi nakapirma.

<a id="usage"></a>
## Paggamit

1. **Driver:** mag-download mula sa NVIDIA o pumili ng orihinal na NVIDIA installer EXE. Hayaang matapos ang pagsusuri.
2. **Mga Bahagi:** suriin ang mga paglalarawan at kinakailangang dependency. Ang mga hindi kilalang bahagi ay pinananatili.
3. **Tweaks:** iwanang hindi nababago ang mga hindi gustong opsyon. Basahin ang mga epekto at trade-off bago pumili ng anuman.
4. **Repasuhin:** suriin ang eksaktong driver, mga bahagi at opsyonal na operasyon, pagkatapos ay kumpirmahin ang pag-install.
5. Tanggapin ang UAC para lang sa operasyong pinili mo. Panatilihin ang mga tagubilin sa pagbawi ng protektadong trabaho.
6. Kung kailangan ng bagong driver ng pag-restart, sundin ang iniulat na estado. Ang mga ipinagpaliban na operasyon ay nangangailangan ng tahasang resume pagkatapos ng pag-restart na iyon.

Ang Custom NV ay nagsisimula nang hindi nagbabago. Pumili ng mga indibidwal na pinangalanang value o suriin ang ibinigay na preset at ang mga pagbubukod nito. Ang dalawang panloob na field na nagbibigay-kaalaman nito ay hindi independyenteng nakasulat. Inilapat lang ang mga setting sa na-verify na workflow ng bagong driver, hindi kailanman sa pamamagitan ng pagbubukas ng preview. Ang pag-install ng hiwalay na NVPI editor ay hindi kinakailangan.

Ang opsyonal na NVENC na trabaho ay nagda-download ng katugmang data mula sa naka-pin na keylase commit. Binabago nito ang dalawang DLL ng driver at pinapawalang-bisa ang kanilang mga lagda; maaari itong tanggihan ng Windows, mga encoder, DRM o anti-cheat. Walang ganoong data o NVIDIA DLL ang naka-embed sa NVDriverForge. [Mga limitasyon sa pinagmulan at paglilisensya](../docs/provenance.md).

Kinokontrol ng mga kagustuhan ang wika, tema at opsyonal na mga pagsusuri sa pag-update ng naka-install na user. Ang portable ay hindi gumagawa ng naka-install na background-check na gawain. Ang mga tool at pagbawi ay hiwalay sa apat na hakbang sa pag-install.

<a id="screenshots"></a>
## Mga screenshot

![NVDriverForge preview ng pahina ng driver](../../../../assets/screenshots/nvdriverforge-0.1.2-preview.png)

Umiiral na 0.1.2 French UI render na may halimbawang data; pinanatili bilang isang preview ng interface. Ang ipinapakitang driver ng 699.99 ay isang test fixture, hindi isang tunay na bersyon na ida-download. [Pinagmulan ng imahe](../assets/README.md).

<a id="update-and-uninstall"></a>
## I-update at i-uninstall

Isara ang NVDriverForge, kunin ang susunod na opisyal na pakete at i-verify ang hash nito. Gamitin ang parehong pagkakakilanlan sa Setup para sa isang naka-install na update; palitan ang isang saradong portable EXE ng bago. Panatilihin ang mga setting at protektadong trabaho.

Uninstall mula sa Windows **Installed apps**. Inaalis nito ang app at ang gawain sa pag-update nito, hindi ang driver ng NVIDIA. Nananatili ang mga setting, log at backup. Kung ninanais, i-restore ang mga advanced/NVENC na pagbabago sa pamamagitan ng nakadokumentong daloy ng pagbawi **bago** alisin ang app. Tinatanggihan ng Restore ang mga magkasalungat na pagbabago mula sa isa pang tool.

Ang lokal na data ay nasa ilalim ng `%LOCALAPPDATA%\NVDriverForge`; Ang mga protektadong trabaho at pag-export ng driver ay nasa ilalim ng `%PROGRAMDATA%\NVDriverForge\Jobs`. Ang portable na paggamit ay lumilikha din ng lokal na data. Ang pag-export ng driver-store ay hindi isang imahe ng system o isang buong backup ng profile.

<a id="known-limitations"></a>
## Mga kilalang limitasyon

- Walang mga pagdaragdag ng hardware/INF na pag-edit, muling nabuong mga lagda ng NVIDIA, pagbibitiw na katugma sa anti-cheat o awtomatikong pagtanggap ng walang pirmang babala.
- Walang kumpletong pag-alis ng telemetry/advertising, pag-export ng slim-package o awtomatikong buong rollback sa dating driver.
- Ang pag-install ng driver, pagbawi ng boot at pagsusulat ng opsyonal na profile ay hindi komprehensibong napatunayan sa mga tunay na makina ng hub audit.
- Ang registry read-back ay hindi patunay ng aktwal na HDCP, performance o latency effect.
- Ang mga tseke ng lagda ay gumagamit ng lokal na available na tiwala sa Windows; hindi ginaganap ang online revocation.
- 34 na wika ang naroroon, ngunit ang buong pagsusuri sa native-speaker/accessibility ay nananatiling hindi kumpleto.

<a id="troubleshooting"></a>
## Pag-troubleshoot

| Sintomas | Aksyon |
| --- | --- |
| Hindi available ang online na catalog | Pumili ng orihinal na package mula sa [Mga pag-download ng driver ng NVIDIA](https://www.nvidia.com/en-us/drivers/). Huwag palitan ang isang kalapit na modelong GPU. |
| Hindi available ang paghahanap ng hotfix | Gamitin ang [Forum ng driver ng NVIDIA ng Game Ready](https://www.nvidia.com/en-us/geforce/forums/game-ready-drivers/13/) at i-verify ang aktwal na package. |
| Nabigo ang pag-install ng NVIDIA | Basahin ang buod ng kabiguan at buksan ang mga detalyadong log. Ang mga opsyonal na bahagi na kasalukuyan na o hindi nalalapat ay nananatiling nalalaktawan sa 0.1.3. Ang mga nabigong pag-install ay hindi nagti-trigger ng mga opsyonal na pag-tweak o isang tagumpay/i-restart ang daloy. |
| Signature/hash/backup failure | Itigil ang pag-install na iyon at panatilihin ang error; makuha muli ang orihinal na pakete kung sira. |
| Hindi available ang opsyon | Basahin ang dahilan ng hardware, component o target-driver nito; panatilihin itong walang pagbabago. |
| I-restart o nakabinbin pa ang trabaho | Gamitin ang mga tagubilin sa pagbawi ng trabaho at tahasang resume; huwag burahin ang journal nito. |
| Ibalik ang salungatan | Ang isa pang estado ay naiiba sa naitala na transaksyon. Panatilihin ito at humiling ng tulong sa halip na pilitin ang pagpapanumbalik. |

Para sa mga ulat, isama ang napiling bersyon ng tool, Windows, GPU, driver at mga reproducible na hakbang; i-redact ang mga landas at personal na detalye mula sa mga log. [Suporta](../docs/support.md).

<a id="faq"></a>
## FAQ

**Nag-i-install ba ang Setup ng isang graphics driver?** Hindi. Nangangailangan iyon ng hiwalay na pagsusuri, pagsusuri, pagkumpirma at mataas na proseso ng pag-install ng application.

**Kailangan ko ba ng NVCleanstall o NVPI?** Hindi. Ang NVCleanstall ay inspirasyon lang. Ang kasamang Profile Inspector ay isang independiyenteng opsyonal na editor.

**Nagagawa ba nitong mas maliit o mas mabilis ang bawat driver ng NVIDIA?** Hindi. Tinutukoy ng mga napiling bahagi at kinakailangan kung ano ang maaaring magbago; walang nasusukat na pakinabang ang ipinangako.

**Nasaan ang mga pinagmumulan?** Ang pinagmumulan na tukoy sa application at mga pribadong pagsubok ay pinapanatili nang hiwalay. Nagbibigay ang hub na ito ng dokumentasyon, binary, at mga third-party na source link na kinakailangan para sa attribution/licensing.

<a id="credits-and-upstream"></a>
## Mga kredito at upstream

Orihinal na aplikasyon, daloy ng trabaho, mga transaksyon, lokalisasyon, bootstrap at mga adaptasyon: 禅堂 Zendo (RevoluSound Team).

- [NVCleanstall / TechPowerUp](https://www.techpowerup.com/download/techpowerup-nvcleanstall/): inspirasyon sa daloy ng trabaho; walang source o binary na na-import.
- [NVIDIA Profile Inspector / Orbmu2k](https://github.com/Orbmu2k/nvidiaProfileInspector): MIT na mga tema, pinalawig na NVAPI interface reference at hiwalay na naka-package na fork.
- [7-Zip / Igor Pavlov](https://www.7-zip.org/): hindi binagong mga tool sa pagkuha.
- [Microsoft .NET](https://github.com/dotnet/runtime) at [WPF](https://github.com/dotnet/wpf): naka-bundle na runtime.
- [Inno Setup](https://jrsoftware.org/isinfo.php): orihinal na installer engine at mga kreditong pagsasalin.
- [keylase/nvidia-patch](https://github.com/keylase/nvidia-patch): panlabas na opsyonal na NVENC data source; hindi itinatag ang lisensya sa muling pamamahagi.
- [NVIDIA](https://www.nvidia.com/en-us/drivers/): nagda-download ng external na driver at nag-install ng mga library ng NVAPI/NVML.

[Buong talahanayan ng bahagi](../THIRD_PARTY_NOTICES.md) · [Mga pagbabago at pinagmulan](../docs/provenance.md)

<a id="license"></a>
## Lisensya

Pinahihintulutan ng [Umiiral na binary distribution permission](../../../../NVDriverForge/LICENSE) ang paggamit at pagbabahagi ng hindi nabagong opisyal na mga executable sa kanilang mga abiso. Ang mga karapatan sa pinagmulang partikular sa application ay nakalaan. Hindi nito pinaghihigpitan ang mga karapatang ibinibigay ng hiwalay na mga lisensya ng third-party. [Buong abiso](LICENSES/README.md).

Independent ng NVIDIA Corporation, TechPowerUp at keylase; hindi itinataguyod o opisyal na inendorso nila. Ang mga pangalan ng produkto ay nananatiling trademark ng kanilang mga may-ari.
