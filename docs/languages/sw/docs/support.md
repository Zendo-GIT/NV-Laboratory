<!-- nv-language-navigation:start -->
🌐 [English](../../../support.md) | [Français](../../../support.fr.md) · [NV Laboratory](../README.md)

<details>
<summary>🌐 Language · 34</summary>

[العربية](../../ar/docs/support.md) · [বাংলা](../../bn/docs/support.md) · [简体中文](../../zh/docs/support.md) · [Čeština](../../cs/docs/support.md) · [Dansk](../../da/docs/support.md) · [Nederlands](../../nl/docs/support.md) · [English](../../../support.md) · [Filipino](../../fil/docs/support.md) · [Suomi](../../fi/docs/support.md) · [Français](../../../support.fr.md) · [Deutsch](../../de/docs/support.md) · [Ελληνικά](../../el/docs/support.md) · [हिन्दी](../../hi/docs/support.md) · [Magyar](../../hu/docs/support.md) · [Bahasa Indonesia](../../id/docs/support.md) · [Italiano](../../it/docs/support.md) · [日本語](../../ja/docs/support.md) · [한국어](../../ko/docs/support.md) · [मराठी](../../mr/docs/support.md) · [فارسی](../../fa/docs/support.md) · [Polski](../../pl/docs/support.md) · [Português](../../pt/docs/support.md) · [ਪੰਜਾਬੀ](../../pa/docs/support.md) · [Română](../../ro/docs/support.md) · [Русский](../../ru/docs/support.md) · [Español](../../es/docs/support.md) · **Kiswahili** · [Svenska](../../sv/docs/support.md) · [தமிழ்](../../ta/docs/support.md) · [ไทย](../../th/docs/support.md) · [Türkçe](../../tr/docs/support.md) · [Українська](../../uk/docs/support.md) · [اردو](../../ur/docs/support.md) · [Tiếng Việt](../../vi/docs/support.md)

[Translation policy](../../README.md)

</details>
<!-- nv-language-navigation:end -->

<!-- nv-translation-notice:start -->
> Tafsiri inayosaidiwa na mashine kutoka kwa Kiingereza. Majina ya kiufundi, amri, URL na maandishi asili ya kisheria yanahifadhiwa. Uhakiki wa mzungumzaji asilia unakaribishwa; angalia rejeleo la Kiingereza ikiwa maneno hayako wazi.
<!-- nv-translation-notice:end -->

<a id="compatibility-and-troubleshooting"></a>
# Utangamano na utatuzi wa matatizo

Hawa ndio watahiniwa waliotayarishwa, si matrix ya uidhinishaji kwa michanganyiko yote ya Windows, GPU, dereva na mchezo.

| Zana | Windows / wakati wa kukimbia | Vifaa / utegemezi wa nje | Operesheni zinazohitaji utunzaji |
| --- | --- | --- | --- |
| NVPI fork 3.0.2.3 | Windows 10/11 x64, .NET Framework 4.8 | Dereva/onyesho linalolingana la NVIDIA | Wasifu huandika na kuonyesha muhtasari |
| NVDriverForge 0.1.4 | Windows 10 kujenga 19041+ / 11 x64; .NET/WPF pamoja | Kifurushi cha viendeshaji kinacholingana cha NVIDIA | Usakinishaji ulioinuliwa, mipangilio ya hali ya juu, NVENC ya hiari |
| NVMFG Unlock40 0.2.3 | Windows 10/11 x64; .NET/WPF imejumuishwa, wasaidizi wa Mfumo 4.8 | RTX 40, mchezo unaostahiki wa DLSS FG na mtoaji aliyebandikwa | Uwekaji viraka wa ndani ya mchezo, jarida la wasifu wa kimataifa, masasisho ya mchezo wa SDK |
| NVRasterPulse 0.2 | Windows 10/11 x64, .NET Framework 4.8 | RTSS imewekwa; kukimbia kwa kofia | RTSS mabadiliko ya wasifu yanayoweza kutekelezwa |

Hakuna kifurushi cha ARM64 kilichotayarishwa. Upatikanaji wa Display/API na matoleo ya zamani ya Windows yanaweza kupunguza vipengele vya mtu binafsi. Hakuna toleo la chini kabisa la NVIDIA au RTSS lililovumbuliwa. Heshi halisi ya mtoa huduma wa NVMFG iko katika [asili](provenance.md).

<a id="before-reporting-a-bug"></a>
## Kabla ya kuripoti mdudu

Tambua toleo kamili linaloweza kutekelezeka/ulilofungua. Nakala iliyosakinishwa hapo awali si lazima iwe toleo la ZIP iliyopakuliwa upya. Rekodi hatua za uzazi, matokeo yanayotarajiwa na matokeo halisi. Kwa masuala ya kutoa/kuzuia, ni pamoja na toleo la mchezo, kuonyesha upya, FG/V-Sync/VRR hali na kikomo kingine chochote au wekeleaji.

Tumia [fomu ya mdudu](https://github.com/Zendo-GIT/NV-Laboratory/issues/new?template=bug-report.yml). Usiwahi kuambatisha folda nzima ya ukuzaji wa kibinafsi, kumbukumbu ya kiendeshi, modeli, DLL ya mchezo, dampo la usajili au mkusanyiko wa kumbukumbu ambao haujakaguliwa.

| Tatizo | Kwanza hundi |
| --- | --- |
| Toleo lisilo sahihi la programu | Thibitisha utambulisho wa EXE na Toa heshi; funga nakala ya zamani kabla ya kubadilisha. |
| Hitilafu ya wakati wa kukimbia/kuanzisha | Sakinisha Mfumo unaohitajika wa 4.8 au uhifadhi folda zote zinazobebeka zinazotolewa. |
| UAC imeghairiwa | Jaribu tena operesheni iliyokusudiwa; kughairi hakufanikiwa usakinishaji. |
| Hashi/saini kutolingana | Acha kutumia mgombeaji huyo na upate baiti rasmi zinazotarajiwa. |
| NVPI rangi/hali imekataliwa | Rejesha na utumie mchanganyiko unaoungwa mkono na onyesho/dereva halisi. |
| Imeshindwa kuhifadhi nakala ya NVDF | Hifadhi kazi iliyolindwa na RECOVERY.txt; usifute jarida au kulazimisha maandishi yanayokinzana. |
| NVMFG inasubiri mipangilio | Tatua urejeshaji michezo ikiwa imefungwa, kuhifadhi mabadiliko kutoka kwa zana zingine. |
| Kofia ya RP haina athari | Endesha RTSS, tambua EXE ya mchezo halisi, kagua hali ya ndoano na mipaka inayoshindana. |
| Kofia ya RP inaendelea baada ya kuondolewa | Kagua RTSS Global; uondoaji mabadiliko ya kikomo cha ndani hubatilisha pekee. |

NVDriverForge inatoa ripoti ya ndani ya JSON inayoweza kutazamwa; NVMFG inatoa uchunguzi katika About. Pendelea ripoti hizi zilizochujwa kwenye kumbukumbu kamili ya kumbukumbu na uikague kabla ya kushiriki. Kizuizi cha urejeshaji kilichoripotiwa kwenye NVMFG 0.1.1 bado hakina sababu iliyothibitishwa; kuhifadhi jarida lake na kurekodi msimbo wowote wa makosa unaopatikana. NVRasterPulse 0.2 inatoa uchunguzi wa usanidi katika menyu ya vitendo vyake, bila kupima FPS.

<a id="logs-and-privacy"></a>
## Kumbukumbu na faragha

| Zana | Data ya ndani ya kukagua, si kupakia jumla |
| --- | --- |
| NVDF | `%LOCALAPPDATA%\NVDriverForge`; kazi zinazolindwa `%PROGRAMDATA%\NVDriverForge\Jobs` |
| NVMFG | `%LOCALAPPDATA%\RtxMfg`; chelezo `%LOCALAPPDATA%\NvidiaStreamlineMaintenance\Backups`; `Sessions` kando ya EXE |
| RP | `%LOCALAPPDATA%\NVRasterPulse`; `Backups\RTSS` chini yake |
| NVPI | Uhamisho uliochagua na hitilafu iliyoonyeshwa; hakuna njia ya logi iliyobuniwa ya ulimwengu wote |

Ondoa majina ya akaunti, saraka za nyumbani, njia za maktaba ya mchezo, vitambulishi vya vifaa, tokeni na madirisha yasiyohusiana kwenye maandishi/picha unazoshiriki. Weka asili kwa faragha ili urejeshe. Masuala ya Umma yanaonekana kwa kila mtu.

Kwa uwezekano wa kuathiriwa, tabia hatari iliyobahatika au operesheni haribifu, fuata [SECURITY.md](../SECURITY.md) badala ya kuchapisha maelezo hadharani.

<a id="what-has-been-verified"></a>
## Nini kimethibitishwa

Kwa utayarishaji wa kitovu, ukaguzi wa malipo tuli/ZIP/hash/metadata na ukaguzi wa hati uliendeshwa. Majaribio yaliyopo ya uundaji wa programu ya kibinafsi/kitengo/UI ni ushahidi wa kihistoria, wa tarehe. Hakuna usakinishaji wa kiendeshi, mabadiliko ya kuonyesha, operesheni ya moja kwa moja ya RTSS au alama ya mchezo iliyotekelezwa kama sehemu ya maandalizi haya.

"Imegunduliwa", "imeandikwa", "imepakiwa upya", "uwezo unapatikana" na "kupimwa katika mchezo" ni matokeo tofauti. Ripoti ni ipi uliyoona.
