<!-- nv-language-navigation:start -->
🌐 [English](../../../releasing.md) | [Français](../../../releasing.fr.md) · [NV Laboratory](../README.md)

<details>
<summary>🌐 Language · 34</summary>

[العربية](../../ar/docs/releasing.md) · [বাংলা](../../bn/docs/releasing.md) · [简体中文](../../zh/docs/releasing.md) · [Čeština](../../cs/docs/releasing.md) · [Dansk](../../da/docs/releasing.md) · [Nederlands](../../nl/docs/releasing.md) · [English](../../../releasing.md) · [Filipino](../../fil/docs/releasing.md) · [Suomi](../../fi/docs/releasing.md) · [Français](../../../releasing.fr.md) · [Deutsch](../../de/docs/releasing.md) · [Ελληνικά](../../el/docs/releasing.md) · [हिन्दी](../../hi/docs/releasing.md) · [Magyar](../../hu/docs/releasing.md) · [Bahasa Indonesia](../../id/docs/releasing.md) · [Italiano](../../it/docs/releasing.md) · [日本語](../../ja/docs/releasing.md) · [한국어](../../ko/docs/releasing.md) · [मराठी](../../mr/docs/releasing.md) · [فارسی](../../fa/docs/releasing.md) · [Polski](../../pl/docs/releasing.md) · [Português](../../pt/docs/releasing.md) · [ਪੰਜਾਬੀ](../../pa/docs/releasing.md) · [Română](../../ro/docs/releasing.md) · [Русский](../../ru/docs/releasing.md) · [Español](../../es/docs/releasing.md) · **Kiswahili** · [Svenska](../../sv/docs/releasing.md) · [தமிழ்](../../ta/docs/releasing.md) · [ไทย](../../th/docs/releasing.md) · [Türkçe](../../tr/docs/releasing.md) · [Українська](../../uk/docs/releasing.md) · [اردو](../../ur/docs/releasing.md) · [Tiếng Việt](../../vi/docs/releasing.md)

[Translation policy](../../README.md)

</details>
<!-- nv-language-navigation:end -->

<!-- nv-translation-notice:start -->
> Tafsiri inayosaidiwa na mashine kutoka kwa Kiingereza. Majina ya kiufundi, amri, URL na maandishi asili ya kisheria yanahifadhiwa. Uhakiki wa mzungumzaji asilia unakaribishwa; angalia rejeleo la Kiingereza ikiwa maneno hayako wazi.
<!-- nv-translation-notice:end -->

<a id="publishing-and-releases"></a>
# Uchapishaji na matoleo

Hazina ya umma ni **Zendo-GIT/NV-Maabara**. Mabadiliko ya hati hukaguliwa, kutekelezwa na kusukumwa na mtunzaji kwa **GitHub Desktop**. Ahadi ya ndani haipakii faili. Vifurushi vya binary ni mali tofauti za GitHub Release; hawashiriki kamwe kwenye orodha ya mabadiliko ya Git.

<a id="documentation-updates"></a>
## Masasisho ya hati

1. Fungua **NV-Laboratory** folda katika GitHub Desktop.
2. Kagua hati, arifa, picha, metadata ya JSON na kithibitishaji hati.
3. Endesha `python tools/validate_repository.py` kutoka kwa folda hiyo.
4. Fanya mabadiliko yaliyokaguliwa, kisha utumie **Push origin**. Angalia matokeo ya Vitendo.
5. Weka utambulisho wa umma wa mwandishi **禅堂 Zendo (RevoluSound Team)** na anwani ya GitHub `noreply` ya akaunti.

Usichague kamwe nafasi ya kazi ya ukuzaji wa mzazi, saraka ya ukaguzi wa kibinafsi au saraka ya viambatisho vya mfumo wa jozi. [Weka faragha ya barua pepe](https://docs.github.com/en/account-and-profile/how-tos/email-preferences/setting-your-commit-email-address).

<a id="independent-application-releases"></a>
## Matoleo ya programu ya kujitegemea

| Zana | Lebo | Sera ya toleo |
| --- | --- | --- |
| NVIDIA Profile Inspector – NV Tools Fork | nvpi-v3.0.2.3 | Toleo lililopo la programu ya sehemu nne; marekebisho ya 2 yana jina lake la faili |
| NVDriverForge | nvdriverforge-v0.1.3 | Mpango uliopo wa 0.x; sasisho zilizotolewa huhifadhi vifurushi vya mapema |
| NVMFG Unlock40 | nvmfg-unlock40-v0.1.1 | Mgombea wa UI2 aliyetambuliwa kwa heshi kamili bila kuvumbua toleo jipya la programu |
| NVRasterPulse | nvrasterpulse-v0.1 | Toleo lililopo la sehemu mbili |

Mtunzaji anaweza kuchapisha moja kwa moja au kuidhinisha msaidizi kuchapisha mali zilizokaguliwa. Uchapishaji ni wazi; hakuna mtiririko wa kazi unaounda Toleo kwa kila ahadi.

1. Kagua ripoti ya sasa ya uchapishaji, vyanzo vya jozi, leseni na thamani za SHA-256.
2. Unda rasimu ya lebo ya zana, ukilenga ahadi ya kitovu iliyopitiwa. Jumuisha maelezo ya toleo mahususi yaliyotayarishwa.
3. Ambatanisha tu toleo hilo la Mipangilio/mali zinazobebeka, `Licenses-and-Credits.zip` na `SHA256SUMS.txt`.
4. Angalia utangamano, usakinishaji, utegemezi, mabadiliko na mipaka inayojulikana. Weka RTSS maarufu kwa NVRasterPulse.
5. Chapisha, thibitisha URL za mali ya umma, ukubwa na heshi, na urekodi tarehe halisi ya uchapishaji katika `docs/releases.json`.
6. Sasisha kurasa za upakuaji na tafsiri, kisha utekeleze/usukuma mabadiliko yao katika GitHub Desktop.

Viungo vya lebo ya kila mradi huepuka kutuma watumiaji kwa zana nyingine kupitia kiungo cha `releases/latest` kilichoshirikiwa. Kumbukumbu za kiotomatiki za GitHub **Source code** zina kitovu hiki cha hati. Vyanzo vya maombi hubaki vya faragha. Arifa za sehemu asilia zinasalia kuwa sawa, na toleo halitatui hifadhi ya NVIDIA SDK iliyorekodiwa ya NVMFG.

<a id="integrity-and-storage"></a>
## Uadilifu na uhifadhi

Usiwahi kuchukua nafasi ya baiti binary zilizochapishwa kimya kimya. Tumia toleo jipya la lugha chafu au masahihisho ya kisakinishi na heshi mpya. Kando za kisheria huongeza arifa zilizopachikwa. NVDriverForge 0.1.3 inayoweza kubebeka ni baiti 141,760,351, zaidi ya kikomo cha kawaida cha faili za GitHub cha 100 MiB Git. Toa viambatisho epuka kuweka jozi au Git LFS kwenye kitovu hiki. [GitHub mwongozo wa faili kubwa](https://docs.github.com/en/repositories/working-with-files/managing-large-files/about-large-files-on-github).

Kuripoti kuathirika kwa kibinafsi kunapaswa kuwashwa katika mipangilio ya hifadhi ya usalama. Thibitisha upatikanaji wake kabla ya kuelekeza ripoti nyeti huko; [SECURITY.md](../SECURITY.md) hutoa njia mbadala ambayo haifichui maelezo ya athari.

[Pakua katalogi](downloads.md) · [Nyaraka za kutolewa za GitHub](https://docs.github.com/en/repositories/releasing-projects-on-github/managing-releases-in-a-repository)
