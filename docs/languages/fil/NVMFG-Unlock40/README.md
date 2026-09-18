<!-- nv-language-navigation:start -->
🌐 [English](../../../../NVMFG-Unlock40/README.md) | [Français](../../../../NVMFG-Unlock40/README.fr.md) · [NV Laboratory](../README.md)

<details>
<summary>🌐 Language · 34</summary>

[العربية](../../ar/NVMFG-Unlock40/README.md) · [বাংলা](../../bn/NVMFG-Unlock40/README.md) · [简体中文](../../zh/NVMFG-Unlock40/README.md) · [Čeština](../../cs/NVMFG-Unlock40/README.md) · [Dansk](../../da/NVMFG-Unlock40/README.md) · [Nederlands](../../nl/NVMFG-Unlock40/README.md) · [English](../../../../NVMFG-Unlock40/README.md) · **Filipino** · [Suomi](../../fi/NVMFG-Unlock40/README.md) · [Français](../../../../NVMFG-Unlock40/README.fr.md) · [Deutsch](../../de/NVMFG-Unlock40/README.md) · [Ελληνικά](../../el/NVMFG-Unlock40/README.md) · [हिन्दी](../../hi/NVMFG-Unlock40/README.md) · [Magyar](../../hu/NVMFG-Unlock40/README.md) · [Bahasa Indonesia](../../id/NVMFG-Unlock40/README.md) · [Italiano](../../it/NVMFG-Unlock40/README.md) · [日本語](../../ja/NVMFG-Unlock40/README.md) · [한국어](../../ko/NVMFG-Unlock40/README.md) · [मराठी](../../mr/NVMFG-Unlock40/README.md) · [فارسی](../../fa/NVMFG-Unlock40/README.md) · [Polski](../../pl/NVMFG-Unlock40/README.md) · [Português](../../pt/NVMFG-Unlock40/README.md) · [ਪੰਜਾਬੀ](../../pa/NVMFG-Unlock40/README.md) · [Română](../../ro/NVMFG-Unlock40/README.md) · [Русский](../../ru/NVMFG-Unlock40/README.md) · [Español](../../es/NVMFG-Unlock40/README.md) · [Kiswahili](../../sw/NVMFG-Unlock40/README.md) · [Svenska](../../sv/NVMFG-Unlock40/README.md) · [தமிழ்](../../ta/NVMFG-Unlock40/README.md) · [ไทย](../../th/NVMFG-Unlock40/README.md) · [Türkçe](../../tr/NVMFG-Unlock40/README.md) · [Українська](../../uk/NVMFG-Unlock40/README.md) · [اردو](../../ur/NVMFG-Unlock40/README.md) · [Tiếng Việt](../../vi/NVMFG-Unlock40/README.md)

[Translation policy](../../README.md)

</details>
<!-- nv-language-navigation:end -->

<!-- nv-translation-notice:start -->
> Pagsasalin na tinulungan ng makina mula sa Ingles. Ang mga teknikal na pangalan, utos, URL at orihinal na legal na teksto ay pinapanatili. Malugod na tinatanggap ang pagsusuri ng katutubong nagsasalita; kumonsulta sa sangguniang Ingles kung ang mga salita ay hindi malinaw.
<!-- nv-translation-notice:end -->

<a id="nvmfg-unlock40"></a>
# NVMFG Unlock40

** Pang-eksperimentong NVIDIA Multi Frame Generation para sa GeForce RTX 40, na may sentral na controller at mga pagpipilian sa bawat laro.**

[I-download ang 0.2.3 at katayuan](../docs/downloads.md#nvmfg-unlock40) · [Pag-install](#installation) · [Upstream](#upstream-and-modifications) · [Mga lisensya](LICENSES/README.md)

<a id="overview-and-purpose"></a>
## Pangkalahatang-ideya at layunin

Ang NVMFG Unlock40 ay isang independiyenteng binuo na application ng 禅堂 Zendo (RevoluSound Team). Pinagsasama nito ang isang Windows controller, isang native na layer, isang profile helper at laro/Streamline SDK management. Tina-target nito ang mga laro na nagsasama na ng NVIDIA DLSS Frame Generation at mga katugmang NVIDIA runtime.

Ang [RTX40MFG-Unlock](https://github.com/dashdogy/RTX40MFG-Unlock) ay kinonsulta upang ihambing at pinuhin ang gawain. Ang kasalukuyang native na layer ay naglalaman ng mga nakabahagi at inangkop na mga bahagi, na isa-isang na-kredito sa ibaba. Hindi ginagawa ng reference na ito ang buong NVMFG application na isang fork ng proyektong iyon.

Umiiral ito upang i-coordinate ang pang-eksperimentong pag-uugali ng MFG sa gitna, tandaan ang mga pagpipiliang partikular sa laro, at panatilihing nakikita ang mga update sa runtime at pag-backup. Hindi ito nagdaragdag ng DLSS Frame Generation sa bawat laro o nagko-convert ng di-makatwirang pagpapatupad ng FSR.

Ang kasalukuyang package ay **0.2.3**. Nagdaragdag ito ng patuloy na library ng laro, impormasyon sa aktibidad at kakayahan, mga lokal na diagnostic at naitama na pag-uugali sa pagpili/pag-unlad. Tinutukoy ng [Mga download](../docs/downloads.md#nvmfg-unlock40) ang eksaktong mga file at hash.

<a id="features"></a>
## Mga tampok

- Central enable/disable control at opsyonal na Windows tray startup.
- Ang pagpili sa bawat laro sa pagitan ng Dynamic MFG, ang setting ng laro at mga sinusuportahang fixed multiplier.
- Paghiwalayin ang mga natatandaang pagpipilian para sa naobserbahang V-Sync on/off na estado.
- Gumagamit ang Dynamic ng mode ng NVIDIA; sinuspinde ito kapag naka-off ang V-Sync, na may hiwalay na in-game/fixed na pagpipilian.
- Gabay sa game-menu at patuloy na pagbubukod; ang mga larong walang DLSS FG ay mananatiling may kontrol.
- Pagtuklas ng laro, pagpili ng parent-folder, paghahanap, pagpapangkat at pagtanggal nang hindi tinatanggal ang mga file ng laro.
- Streamline SDK download/import, na-verify na lokal na cache, tahasang pagpili, bawat-laro backup at pagpapanumbalik.
- Pag-verify ng native na provider, mga diagnostic sa bawat session, journal ng pandaigdigang profile at pagbawi na may kamalayan sa salungatan.
- 34 interface na wika at apat na tema.

Ang pag-off ng FG sa laro ay nagpapanatili nito. Nakadepende ang mga nakapirming pagpipilian mula 2x hanggang 6x sa laro/menu/runtime; hindi sila isang pangako na gumagana ang bawat kumbinasyon. Inoobserbahan ng controller ang V-Sync at hindi itinatakda ang V-Sync o VRR para sa user.

<a id="compatibility"></a>
## Pagkakatugma

| Kinakailangan | Mga Detalye |
| --- | --- |
| Sistema | Windows 10/11 x64 |
| GPU | GeForce RTX 40 na target; walang universal GPU compatibility claim |
| Laro | Umiiral na NVIDIA DLSS Frame Generation integration at suportadong runtime; walang anti-cheat compatibility certification |
| Provider | Ang kandidato ay naka-pin sa provider na SHA-256 na nakadokumento sa [pinanggalingan](../docs/provenance.md); hindi kilalang mga hash ay tinanggihan |
| Runtime | Naka-bundle na .NET 8/WPF 8.0.30 para sa app/agent; .NET Framework 4.8 para sa mga katulong sa profile |
| Mga Pahintulot | Access ng administrator para sa mga operasyon ng controller/profile |
| Network | Kinakailangan para sa mga napiling opisyal na pag-download ng SDK; Ang na-import na katugmang SDKs ay maaaring i-cache nang lokal |
| Panlabas na binary | Ang driver ng NVIDIA, provider/modelo ng NGX at mga runtime ng laro ng Streamline ay hindi naka-bundle |

Ang isang label na bersyon lamang ay hindi sapat: driver, hash ng provider, pagsasama ng laro at aktwal na na-load na mga module ay mahalaga. Maaaring tanggihan ng mga protektado o hindi tugmang proseso ang pag-attach. Ang application ay hindi idinisenyo upang iwasan ang mga proteksyon laban sa cheat.

<a id="installation"></a>
## Pag-install

1. Basahin ang [katayuan ng kandidato at tala sa paglilisensya](../docs/downloads.md#nvmfg-unlock40).
2. I-download ang `NVMFGUnlock40-0.2.3-Setup-x64.exe` o `NVMFGUnlock40-0.2.3-Portable-x64.zip` kapag available na ang Paglabas nito.
3. Suriin ang SHA-256 at panatilihin ang mga kasamang abiso. I-install ang .NET Framework 4.8 kung hindi pa ito ibinibigay ng Windows.
4. Patakbuhin ang Setup, o i-extract ang **buong** portable ZIP sa isang masusulat na lokal na folder.
5. Ilunsad ang `NVMFGUnlock40.exe`; panatilihin ang `agent`, `driver`, `engine` at `Licenses` sa ibinigay na layout.

Ang folder na pinangalanang `driver` ay naglalaman ng mga katulong ng user-space, hindi isang kernel driver. Huwag kopyahin lamang ang pangunahing EXE o palitan ang hash ng provider upang pilitin ang pagiging tugma. Ang mga kasalukuyang EXE ay hindi nalagdaan.

<a id="usage"></a>
## Paggamit

1. Magsimula sa hindi pinagana ang controller. Magdagdag ng laro o folder ng magulang at piliin ang mga aktwal na pag-install.
2. Suriin ang mga setting ng MFG ng bawat laro. Sagutin kung ano ang iniaalok ng menu nito; ang sagot ay naka-imbak sa bawat laro.
3. Piliin ang Dynamic o ang in-game na setting sa buong mundo, pagkatapos ay isaayos ang mga kwalipikadong pagpipilian sa bawat laro kung kinakailangan.
4. I-enable lang ang controller kapag balak mong gamitin ito. Maaari nitong pansamantalang baguhin ang anim na pandaigdigang setting ng profile ng NVIDIA, gamit ang isang recovery journal.
5. Maglunsad ng isang karapat-dapat na laro at paganahin ang sarili nitong DLSS Frame Generation. Sundin ang anumang kahilingan para sa V-Sync-off na pagpipilian.
6. Gumamit ng mga pagbubukod para sa mga larong hindi mo gustong pamahalaan. Ang pag-alis ng laro ay nagtatala ng pagbubukod at pinapanatili ang mga file/backup nito.
7. Gamitin ang buong pag-quit/disable at daloy ng pagbawi ng application kapag natapos na.

Ang pagsasara sa pangunahing window ay maaaring iwanan ang controller sa tray. Ang isang DLL na na-load na sa isang laro ay nananatili doon hanggang sa lumabas ang laro; Ang hindi pagpapagana ng controller ay hindi isang garantiya sa pag-unload. Isara ang mga apektadong laro bago ang maintenance o mga update.

**Streamline SDKs:** sa page na NVIDIA SDK, mag-download ng opisyal na bersyon o mag-import ng tugmang lokal na SDK. Mag-import ng mga tindahan ng isang na-verify na kopya; Pinipili ito ng **Use this version**, at inaalis ng **Uninstall** ang naka-cache na kopya na iyon. Ang mga nawawalang Streamline DLL ay maaaring dagdagan mula sa isang opisyal na NVIDIA SDK, na ipinapakita ang pinagmulan. Hindi nito dina-download/pinapalitan ang isang NGX na modelo. Isara ang laro, piliin ang nilalayong pag-update ng laro, at panatilihin ang orihinal nitong backup. Upang ibalik ang mga file ng laro, gamitin ang backup na pagpapanumbalik nito, hindi ang Uninstall na button ng cache.

<a id="library-diagnostics-and-updates"></a>
## Library, diagnostic at update

**Persistent library:** pumili ng ilang folder ng laro, kabilang ang iba't ibang drive, bago magsimula ng isang pag-scan. Nakikita ang pag-unlad at available ang pagkansela. Pagkatapos ng unang pag-scan, ire-restore ng lokal na cache ang library sa paglulunsad nang hindi nilalakad ang bawat folder ng laro. I-refresh upang mahanap ang mga pagbabago o magdagdag ng isa pang folder. Ang mga operasyon sa pagpapanatili ay muling nagpapatunay sa mga apektadong file; nananatiling aktibo ang backup monitoring. Ang cache ay naka-imbak sa `%LOCALAPPDATA%\RtxMfg\library-cache.json`.

**Selection:** Pinipili ng Ctrl+A ang lahat at ki-clear ng Ctrl+D ang aktibong tab na Mga Laro o Backup. Walang laro ang awtomatikong napili. Ang mga pag-update at pag-refresh ng aktibidad ay hindi na gumagawa ng mga seleksyon ng multo o hindi pare-parehong bilang.

**Aktibidad at pagiging tugma:** bawat larong MFG na impormasyon ay mula sa NGX na mga obserbasyon nang walang bagong overlay. Ito ay hindi isang pisikal na bilang ng mga ipinapakitang frame. Ang suportang Dynamic-with-V-Sync ay nagmumula sa mga kakayahan sa runtime; hindi natukoy ang hindi kilalang kakayahan mula sa isang numero ng bersyon. Ang application ay hindi nagbabago alinman sa V-Sync o VRR. Kapag naka-off ang V-Sync, nananatiling suspendido ang Dynamic; hiwalay ang mga napiling naayos o kontrolado ng laro.

**Susunod na paglulunsad:** ang pansamantalang pagbubukod ay lumalaktaw sa pag-patch sa susunod na paglulunsad ng laro at ibinabalik ang normal na pamamahala pagkatapos nitong lumabas. Hindi nito maalis ang isang DLL na na-load na sa isang laro: isara at i-restart ang larong iyon. Ang Wallpaper Engine ay kinikilala bilang isang desktop application; ang pagwawasto na ito ay nagpapanatili ng proteksyon para sa aktwal na mga larong hindi pinansin.

**Mga Kagustuhan at suporta:** Ang kagustuhan sa pag-import/pag-export ay nangangailangan ng manu-manong reassociation ng mga folder ng laro. Pini-filter ng lokal na diagnostic sa About ang pribadong impormasyon at mga ulat na available na NVAPI error code o mga kategorya ng conflict. Suriin ito bago ibahagi; walang awtomatikong na-upload.

**Mga update sa application:** ang isang opsyonal na pagsusuri ay nagpapakita ng mga tala sa paglabas at nag-aalok ng opisyal na Setup. Sinusuri ang tahasang pag-download laban sa laki ng GitHub at metadata ng SHA-256; ikaw mismo ang magsisimula ng pag-install. Ang Bersyon na 0.2.3 ay nag-clear din ng mga nakumpletong mensahe ng pag-unlad habang pinapanatili ang mga makabuluhang error at resulta. Kasama sa mga karagdagan na ito ang mga pagbabago mula noong pampublikong bersyon na 0.1.1.

<a id="screenshots"></a>
## Mga screenshot

![NVMFG SDK-list preview](../../../../assets/screenshots/nvmfg-0.1.1-sdk-preview.png)

Ang kasalukuyang English 0.1.1 na interface ay nagre-render na may halimbawang SDK na imbentaryo. Ito ay hindi isang kasalukuyang listahan ng bersyon o katibayan ng isang tumatakbong laro. [Pinagmulan ng imahe](../assets/README.md).

<a id="update-and-uninstall"></a>
## I-update at i-uninstall

Isara ang mga apektadong laro. I-disable/iwanan ang NVMFG at lutasin ang anumang nakabinbing pag-recover ng mga setting ng NVIDIA bago mag-update. I-install ang susunod na Setup gamit ang kasalukuyang pagkakakilanlan, o i-extract ang bagong portable sa isang bagong folder; panatilihin ang estado/mga backup.

Bago i-uninstall, i-restore ang ninanais na mga backup ng laro na SDK at mga setting ng NVIDIA sa pamamagitan ng application, pagkatapos ay isara ang mga laro at isara ang controller. Gamitin ang Windows **Installed apps** para sa Setup, o alisin ang saradong portable folder pagkatapos mapanatili ang mga kinakailangang file. Huwag manu-manong tanggalin ang isang aktibong journal sa pagbawi upang i-unblock ang Setup.

Gumagamit ng `%LOCALAPPDATA%\NvidiaStreamlineMaintenance\Backups` ang mga lokal na backup ng runtime ng laro. Ang mga setting ng MFG/SDK data ay gumagamit ng `%LOCALAPPDATA%\RtxMfg`; session output ay sa ilalim ng `Sessions` sa tabi ng application. Ang mga file na ito ay maaaring maglaman ng mga path ng laro. Huwag i-post ang mga ito nang hindi na-redact.

<a id="known-limitations"></a>
## Mga kilalang limitasyon

- Ang isang iniulat na 0.1.1 activation/restoration/uninstall blockage ay nananatiling unreproduced at hindi alam ang sanhi nito. Hindi inaangkin ng release na ito na ayusin ito. Pagkatapos ng kabiguan, panatilihin ang recovery journal at siyasatin ang lokal na diagnostic; huwag pilitin ang pagtanggal ng data sa pagbawi.
- Maaaring magdulot ng mga pag-crash o visual artifact ang mga pang-eksperimentong katutubong patch; isang hindi nalutas na pag-crash ng Bodycam ang naitala sa kasaysayan ng pag-unlad.
- Ang mga kinokontrol na renderer test ay hindi certification para sa bawat laro, driver o anti-cheat.
- Ang mga nabuong frame ay hindi gumagawa ng mga bagong input sample; walang nasusukat na latency o performance gain ang ipinangako ng hub na ito.
- Maaaring magkasalungat ang maraming tool/mga overlay sa pagbuo ng frame. Ang application ay nag-uulat ng mga naobserbahang module nang hindi pinatutunayan ang bawat senaryo ng magkakasamang buhay.
- Ang compatibility manifest ay isang detection aid, hindi isang listahan ng mga ganap na nasubok na laro.
- Ang buong tuntunin ng NVIDIA SDK at ang hindi nalutas na paghihigpit sa teknikal na limitasyon ay nananatiling dokumentado sa [pinanggalingan](../docs/provenance.md).

<a id="troubleshooting"></a>
## Pag-troubleshoot

| Sintomas | Aksyon |
| --- | --- |
| Hindi suportado ang provider | Panatilihin ang orihinal na na-verify na mga file. Iulat ang mga bersyon ng driver/provider at ang error; huwag i-bypass ang hash check. |
| Walang DLSS FG sa laro | Piliin ang sagot na iyon at iwanan ang laro sa kontrol; hindi kayang gawin ng tool na ito ang pagsasamang iyon. |
| Mga pag-crash/artifact ng laro | Ihinto ang laro, huwag paganahin ang NVMFG, gamitin ang orihinal na runtime backup ng laro kung ito ay binago, at mag-ulat ng mga reproducible na detalye. |
| Hindi available ang listahan o pag-download ng SDK | I-refresh at suriin ang opisyal na pinagmulan; ang isang naka-cache/na-import na bersyon ay dapat pa ring pumasa sa pagpapatunay. |
| Nakabinbing NVIDIA ang pag-block sa paglabas/pag-update | Gamitin ang pagbawi at panatilihin ang journal; ang mga salungatan ay hindi dapat ma-overwrite nang bulag. |
| Ang isang inalis na laro ay hindi muling natuklasan | Ang pagbubukod nito ay paulit-ulit. Idagdag ito nang tahasan kapag gusto mo itong pamahalaang muli. |

Ipinapaliwanag ng [Nakabahaging gabay sa suporta](../docs/support.md) kung ano ang isasama sa isang ulat.

<a id="faq"></a>
## FAQ

**Kasama ba dito ang mga NVIDIA DLL o modelo?** Walang kasamang driver, NGX provider/modelo o Streamline runtime. Ang mga tahasang SDK na pag-download ay nagmula sa NVIDIA.

**Gumagana ba ang Dynamic nang naka-off ang V-Sync?** Nasuspinde ito sa estadong iyon. Piliin ang in-game na setting o isang kwalipikadong fixed multiplier para sa hiwalay na estado ng larong iyon.

**Ito ba ay isang ReShade/OptiScaler/FSR package?** Hindi. Ang mga iyon ay hindi pinagsama-sama o ipinadala bilang bahagi ng production package na ito.

**Pampubliko ba ang mga binagong mapagkukunan?** Hindi. Ang mga pinagsama-samang pakete at kinakailangang mga kredito/lisensya ay ibinigay. Hindi nito inaalis ang mga karapatan o paghihigpit ng mga ikatlong partido.

<a id="upstream-and-modifications"></a>
## Upstream at mga pagbabago

Sanggunian sa paghahambing at mga nakabahaging katutubong bahagi: **RTX40MFG-Unlock ni Michael Robles / dashdogy**, ang reference ay nag-commit ng `4e776d068f91b4a665425542bb005dd57cc3d891`, MIT. [Imbakan](https://github.com/dashdogy/RTX40MFG-Unlock) · [Mga orihinal na pag-download](https://github.com/dashdogy/RTX40MFG-Unlock/releases).

Tinutukoy ng paghahambing ng pinagmulan ang ibinahaging patching, pangangasiwa ng provider/patakaran, mga temporal na pagwawasto at mga bahagi ng detour na nakabatay sa MinHook. Ang kanilang mga abiso sa MIT at BSD ay pinapanatili. Kasama rin sa kumpletong paghahambing ang mga file sa labas ng target ng produksyon.

Ang desktop application, controller at SDK-management workflow ay binuo ng 禅堂 Zendo (RevoluSound Team). Kasama sa gawaing proyekto ang central loading, NGX bootstrap integration, verified provider selection, game/V-Sync coordination at session diagnostics. Ang gabay sa pinagmulan ay naghihiwalay na gumagana mula sa mga nakabahaging bahagi; Ang paghahambing ng file lamang ay hindi nagtatatag kung kailan nagkaroon ng ideya ang alinmang may-akda.

Inaangkop ng profile helper ang MIT NVAPI wrapper mula sa Orbmu2k's Profile Inspector. [Detalyadong pinagmulan at saklaw ng bahagi](../docs/provenance.md).

<a id="credits-and-license"></a>
## Mga kredito at lisensya

Michael Robles; Orbmu2k; Mga kontribyutor ng Tsuda Kageyu at HDE; NVIDIA Corporation; Microsoft at mga kontribyutor; Inno Setup mga may-akda at tagasalin. Pagbuo ng application, pagsasama at packaging: 禅堂 Zendo (RevoluSound Team).

Ang [umiiral na pahintulot sa pagbabahagi ng pinagsama-samang pakete](../../../../NVMFG-Unlock40/LICENSE) at lahat ng [mga lisensya ng bahagi](LICENSES/README.md) ay napanatili. Ang mga pahintulot ng MIT para sa upstream code ay naiiba sa mga termino ng NVIDIA SDK. Walang kumot na lisensya ang pumapalit sa kanila.

Independiyente sa, hindi ini-sponsor ng, at hindi opisyal na iniendorso ng NVIDIA Corporation. Ang lahat ng na-refer na trademark ay nananatiling pag-aari ng kanilang mga may-ari.
