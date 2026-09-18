<!-- nv-language-navigation:start -->
🌐 [English](../../../installation.md) | [Français](../../../installation.fr.md) · [NV Laboratory](../README.md)

<details>
<summary>🌐 Language · 34</summary>

[العربية](../../ar/docs/installation.md) · [বাংলা](../../bn/docs/installation.md) · [简体中文](../../zh/docs/installation.md) · [Čeština](../../cs/docs/installation.md) · [Dansk](../../da/docs/installation.md) · [Nederlands](../../nl/docs/installation.md) · [English](../../../installation.md) · [Filipino](../../fil/docs/installation.md) · [Suomi](../../fi/docs/installation.md) · [Français](../../../installation.fr.md) · [Deutsch](../../de/docs/installation.md) · [Ελληνικά](../../el/docs/installation.md) · [हिन्दी](../../hi/docs/installation.md) · [Magyar](../../hu/docs/installation.md) · [Bahasa Indonesia](../../id/docs/installation.md) · [Italiano](../../it/docs/installation.md) · [日本語](../../ja/docs/installation.md) · [한국어](../../ko/docs/installation.md) · [मराठी](../../mr/docs/installation.md) · [فارسی](../../fa/docs/installation.md) · [Polski](../../pl/docs/installation.md) · [Português](../../pt/docs/installation.md) · [ਪੰਜਾਬੀ](../../pa/docs/installation.md) · [Română](../../ro/docs/installation.md) · [Русский](../../ru/docs/installation.md) · [Español](../../es/docs/installation.md) · **Kiswahili** · [Svenska](../../sv/docs/installation.md) · [தமிழ்](../../ta/docs/installation.md) · [ไทย](../../th/docs/installation.md) · [Türkçe](../../tr/docs/installation.md) · [Українська](../../uk/docs/installation.md) · [اردو](../../ur/docs/installation.md) · [Tiếng Việt](../../vi/docs/installation.md)

[Translation policy](../../README.md)

</details>
<!-- nv-language-navigation:end -->

<!-- nv-translation-notice:start -->
> Tafsiri inayosaidiwa na mashine kutoka kwa Kiingereza. Majina ya kiufundi, amri, URL na maandishi asili ya kisheria yanahifadhiwa. Uhakiki wa mzungumzaji asilia unakaribishwa; angalia rejeleo la Kiingereza ikiwa maneno hayako wazi.
<!-- nv-translation-notice:end -->

<a id="installation-guide"></a>
# Mwongozo wa ufungaji

Anza na [Vipakuliwa](downloads.md), ambayo hurekodi hali ya uchapishaji na majina halisi ya mali. Hizi ni zana tofauti: sasisha zile tu unazohitaji.

> **Kwa NVRasterPulse, sakinisha [RTSS kutoka Guru3D](https://www.guru3d.com/download/rtss-rivatuner-statistics-server-download/) kabla ya kufungua kidhibiti wasifu.**
> RTSS lazima iendeshe ili kuweka vikomo; haijajumuishwa katika NV Tools.

| Zana | Toleo lililosakinishwa | Toleo la kubebeka | Sharti kuu |
| --- | --- | --- | --- |
| NVIDIA Profile Inspector – NV Tools Fork | NVPI-CustomNV-3.0.2.3-Setup-r2.exe | Dondoo kamili ya NVPI ZIP | Viendeshaji vya NVIDIA na .NET Framework 4.8 |
| NVDriverForge | NVDriverForge-Setup.exe | NVDriverForge.exe, wakati wa kukimbia umejumuishwa | Kifurushi cha asili kinacholingana cha NVIDIA kwa shughuli za usakinishaji |
| NVMFG Unlock40 | NVMFGUnlock40-0.2.3-Setup-x64.exe | Toa ZIP kamili ya NVMFG, uhifadhi folda ndogo | RTX 40, DLSS FG iliyopo, mtoa huduma kamili na wasaidizi wa NET Framework 4.8 |
| NVRasterPulse | NVRasterPulse-0.2-win-x64-Setup.exe | Dondoo kamili ya RP ZIP | RTSS na .NET Framework 4.8 |

<a id="download-verify-install"></a>
## Pakua, thibitisha, sakinisha

1. Kwenye Toleo lililochaguliwa lililochapishwa, pakua kipengee cha programu iliyopewa jina, matangazo ZIP na SHA256SUMS.txt.
2. Tumia [Mfano wa SHA-256](downloads.md#sha-256), na jina halisi la faili lililopakuliwa.
3. Kwa Usanidi, fuata kisakinishi cha kawaida. Kwa ZIP inayobebeka, toa kila kitu kwenye folda mpya inayoweza kuandikwa ya ndani; usikimbie kutoka ndani ya ZIP.
4. Fungua EXE ya programu mwenyewe. Weka faili za leseni/usanidi/data zinazoambatana.
5. Soma maagizo ya matumizi ya zana hiyo kabla ya kuwezesha mipangilio au uendeshaji wa mfumo.

Jozi za sasa hazijatiwa saini. Heshi inayolingana inathibitisha baiti zinazotarajiwa; sio cheti cha usalama au uoanifu. Usizime ulinzi wa usalama wa Windows ili tu kukandamiza onyo.

Kusakinisha NVDF au mshirika wake wa hiari wa NVPI ni tofauti na kusakinisha kiendeshi cha GPU. Mshirika wa NVPI huhifadhi jina lake la usakinishaji wa ndani lililopo. Kitufe chake cha juu cha RasterPulse kinahitaji usakinishaji wa mfumo mzima unaolindwa; nakala zingine za RP zinaweza kufunguliwa kupitia njia zao za mkato.

NVMFG ni ya majaribio na ina [hifadhi ya leseni ya NVIDIA SDK](provenance.md). Hakuna dereva wa NVIDIA, mtoa huduma/muundo wa NGX au muda wa utekelezaji wa mchezo wa Streamline umejumuishwa. Vipakuliwa vilivyochaguliwa vya SDK na masasisho ya mchezo ni shughuli tofauti.

<a id="language-and-updates"></a>
## Lugha na sasisho

Tumia kiteuzi cha README cha lugha 34 kwa uhifadhi wa hati. NVDF, NVMFG na RP wana mpangilio wao wa UI wa lugha 34; NVPI huweka usaidizi wake wa lugha uliopo. Baadhi ya masharti ya kiufundi ya kisakinishi hurudi kwa Kiingereza.

Weka utambulisho wa usakinishaji wa zana wakati wa kusasisha. Ifunge kwanza na uhifadhi chelezo. Kwa NVMFG, funga michezo iliyoathiriwa na usuluhishe urejeshaji wa wasifu unaosubiri. Kwa masasisho yanayobebeka, tumia folda mpya badala ya kuchanganya matoleo.

<a id="removing-a-tool"></a>
## Kuondoa chombo

Kuondoa programu sio kutengua mipangilio yake kiotomatiki.

- **NVPI:** rejesha mipangilio ya wasifu/onyesho iliyokusudiwa kabla ya kuondolewa ikihitajika.
- **NVDF:** tumia urejeshaji kwanza ikiwa unataka kurejesha mabadiliko ya hali ya juu/NVENC. Uninstall huacha kiendeshi cha picha, mipangilio na chelezo.
- **NVMFG:** funga michezo, zima/acha kidhibiti, suluhisha urejeshaji wa NVIDIA na urejeshe chelezo za mchezo unaotaka za SDK kabla ya kuondolewa.
- **RP:** ondoa kikomo kilichokusudiwa kwanza. Uninstall haifuti vifuniko vya RTSS vilivyohifadhiwa au kuondoa RTSS.

Tazama kila [mwongozo wa mradi](../README.md#projects) kwa maeneo kamili ya data na vikwazo, au [msaada](support.md) ikiwa hatua ya kurejesha itashindwa.
