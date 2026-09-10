<!-- nv-language-navigation:start -->
🌐 [English](../../../development.md) | [Français](../../../development.fr.md) · [NV Laboratory](../README.md)

<details>
<summary>🌐 Language · 34</summary>

[العربية](../../ar/docs/development.md) · [বাংলা](../../bn/docs/development.md) · [简体中文](../../zh/docs/development.md) · [Čeština](../../cs/docs/development.md) · [Dansk](../../da/docs/development.md) · [Nederlands](../../nl/docs/development.md) · [English](../../../development.md) · [Filipino](../../fil/docs/development.md) · [Suomi](../../fi/docs/development.md) · [Français](../../../development.fr.md) · [Deutsch](../../de/docs/development.md) · [Ελληνικά](../../el/docs/development.md) · [हिन्दी](../../hi/docs/development.md) · [Magyar](../../hu/docs/development.md) · [Bahasa Indonesia](../../id/docs/development.md) · [Italiano](../../it/docs/development.md) · [日本語](../../ja/docs/development.md) · [한국어](../../ko/docs/development.md) · [मराठी](../../mr/docs/development.md) · [فارسی](../../fa/docs/development.md) · [Polski](../../pl/docs/development.md) · [Português](../../pt/docs/development.md) · [ਪੰਜਾਬੀ](../../pa/docs/development.md) · [Română](../../ro/docs/development.md) · [Русский](../../ru/docs/development.md) · [Español](../../es/docs/development.md) · **Kiswahili** · [Svenska](../../sv/docs/development.md) · [தமிழ்](../../ta/docs/development.md) · [ไทย](../../th/docs/development.md) · [Türkçe](../../tr/docs/development.md) · [Українська](../../uk/docs/development.md) · [اردو](../../ur/docs/development.md) · [Tiếng Việt](../../vi/docs/development.md)

[Translation policy](../../README.md)

</details>
<!-- nv-language-navigation:end -->

<!-- nv-translation-notice:start -->
> Tafsiri inayosaidiwa na mashine kutoka kwa Kiingereza. Majina ya kiufundi, amri, URL na maandishi asili ya kisheria yanahifadhiwa. Uhakiki wa mzungumzaji asilia unakaribishwa; angalia rejeleo la Kiingereza ikiwa maneno hayako wazi.
<!-- nv-translation-notice:end -->

<a id="repository-architecture-and-maintenance"></a>
# Usanifu wa hifadhi na matengenezo

NV Laboratory ni **hati ya umma na kitovu cha usambazaji wa binary**. Haina chanzo cha programu. Miradi hii minne huhifadhi miti tofauti ya ujenzi, matoleo, vitambulisho na rasilimali za kutolewa. Historia yao ya maendeleo ya kibinafsi haijaingizwa kwenye hazina hii ya Git.

<a id="layout"></a>
## Mpangilio

| Mahali | Kusudi |
| --- | --- |
| README.md / README.fr.md | Viingilio vya Kiingereza/Kifaransa |
| Folda nne za mradi | Kamilisha miongozo na arifa asili zinazotumika |
| hati | Upakuaji, utangamano, asili, ukuzaji na utaratibu wa kutolewa |
| hati/releases.json | Metadata ya mgombea/toleo lililokaguliwa, ukubwa na heshi |
| hati/uthibitisho | Ulinganisho wa faili/heshi; hakuna msimbo wa maombi |
| leseni | Imeshiriki maandishi kamili ya wahusika wengine na salio la mtafsiri aliyesakinisha |
| mali | Muhtasari wa UI uliopo uliokaguliwa na asili yake |
| .github | Fomu za kutoa na uthibitishaji wa nyaraka za kusoma tu |
| zana/validate_repository.py | Mipaka ya uchapishaji wa maktaba ya kawaida na ukaguzi wa viungo |

Kiingereza kinasalia kuwa GitHub README chaguomsingi. Viungo vilivyopo vya karibu vya `.fr.md` vinasalia kuwa halali. Tafsiri za ziada zinaakisi hati chini ya `docs/languages/<code>`; kiteuzi cha lugha huweka ukurasa sawa wakati wa kubadilisha lugha. Katalogi ya `docs/languages/catalog.json` hurekodi lugha zote 34 na alama za vidole chanzo. GitHub haichagui kiotomatiki README kwa lugha ya kivinjari. Angalia [faharasa ya lugha na sera ya tafsiri](../../README.md).

<a id="application-technologies"></a>
## Teknolojia za maombi

| Mpango | Teknolojia ya kibinafsi | Usambazaji |
| --- | --- | --- |
| NVPI fork | C#, WPF, .NET Framework 4.8, NVAPI/Windows interop | Kamilisha folda inayoweza kubebeka na utenganishe Inno Setup |
| NVDriverForge | C #, WPF, .NET 8; asili ya C++ bootstrap; Mchakato wa 7-Zip | EXE na Mipangilio inayobebeka yenyewe |
| NVMFG Unlock40 | C#/WPF .NET 8, Framework 4.8 wasaidizi, C++20/MASM/MinHook injini | Mti unaobebeka na Usanidi |
| NVRasterPulse | C#/WPF Mfumo 4.8; RTSS wasifu / ujumuishaji upya; bootstrap asili | Mti unaobebeka na Usanidi |

Malipo haya ya umma hayawezi kuunda upya programu. Kumbukumbu za kiotomatiki za "Source code" ni vijipicha vya kitovu. Viungo vya chanzo cha juu haviwakilishi chanzo halisi cha faragha kilichorekebishwa. CI ya umma inathibitisha hazina hii pekee.

<a id="local-checks"></a>
## Hundi za ndani

Kutoka kwa mzizi wa kumbukumbu:

```text
python tools/validate_repository.py
```

Python 3.10 au mpya zaidi inatosha. Cheki husoma faili, viungo vya Markdown vya ndani, arifa zinazohitajika/viungo vya RTSS, metadata ya kutolewa na mipaka ya uchapishaji. Haitekelezi programu, kusakinisha vitegemezi au kuwasiliana na mtandao.

Mtiririko wa kazi wa GitHub huendesha hundi hii kwa ruhusa ya kusoma pekee kwenye kusukuma, ombi la kuvuta au utumaji mwenyewe. Malipo yamebandikwa kwenye ahadi iliyokaguliwa na haiendelei vitambulisho. Hakuna kazi ya kutolewa au kusambaza iliyosanidiwa.

<a id="maintain-the-boundary"></a>
## Dumisha mpaka

Sasisha marejeleo ya Kiingereza, miongozo ya Kifaransa na tafsiri zilizoathiriwa pamoja. Weka mabadiliko makubwa tofauti na ulinganisho wa umbizo pekee. Rekodi heshi halisi za mgombea, marejeleo ya ahadi ya juu na leseni; usiwahi kudokeza leseni kutoka kwa umaarufu wa mradi.

Tumia toleo jipya la vipengee vya Utoaji na ukague upya jozi zilizobadilishwa, kumbukumbu na arifa zilizopachikwa. Hifadhi nakala za faragha nje ya hazina hii. Usitumie mtiririko wa kazi wa umma kuleta chanzo cha kibinafsi cha programu au folda za ujenzi wa ndani.

Majaribio yanayolingana na mabadiliko ya utendakazi ya programu yanayoendeshwa katika mradi wa kibinafsi. Usirudishe visakinishi vya viendeshaji au uandike wasifu halisi kwa sasisho la hati. [Utaratibu wa kutolewa kwa mikono](releasing.md).
