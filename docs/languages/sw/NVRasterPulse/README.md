<!-- nv-language-navigation:start -->
🌐 [English](../../../../NVRasterPulse/README.md) | [Français](../../../../NVRasterPulse/README.fr.md) · [NV Laboratory](../README.md)

<details>
<summary>🌐 Language · 34</summary>

[العربية](../../ar/NVRasterPulse/README.md) · [বাংলা](../../bn/NVRasterPulse/README.md) · [简体中文](../../zh/NVRasterPulse/README.md) · [Čeština](../../cs/NVRasterPulse/README.md) · [Dansk](../../da/NVRasterPulse/README.md) · [Nederlands](../../nl/NVRasterPulse/README.md) · [English](../../../../NVRasterPulse/README.md) · [Filipino](../../fil/NVRasterPulse/README.md) · [Suomi](../../fi/NVRasterPulse/README.md) · [Français](../../../../NVRasterPulse/README.fr.md) · [Deutsch](../../de/NVRasterPulse/README.md) · [Ελληνικά](../../el/NVRasterPulse/README.md) · [हिन्दी](../../hi/NVRasterPulse/README.md) · [Magyar](../../hu/NVRasterPulse/README.md) · [Bahasa Indonesia](../../id/NVRasterPulse/README.md) · [Italiano](../../it/NVRasterPulse/README.md) · [日本語](../../ja/NVRasterPulse/README.md) · [한국어](../../ko/NVRasterPulse/README.md) · [मराठी](../../mr/NVRasterPulse/README.md) · [فارسی](../../fa/NVRasterPulse/README.md) · [Polski](../../pl/NVRasterPulse/README.md) · [Português](../../pt/NVRasterPulse/README.md) · [ਪੰਜਾਬੀ](../../pa/NVRasterPulse/README.md) · [Română](../../ro/NVRasterPulse/README.md) · [Русский](../../ru/NVRasterPulse/README.md) · [Español](../../es/NVRasterPulse/README.md) · **Kiswahili** · [Svenska](../../sv/NVRasterPulse/README.md) · [தமிழ்](../../ta/NVRasterPulse/README.md) · [ไทย](../../th/NVRasterPulse/README.md) · [Türkçe](../../tr/NVRasterPulse/README.md) · [Українська](../../uk/NVRasterPulse/README.md) · [اردو](../../ur/NVRasterPulse/README.md) · [Tiếng Việt](../../vi/NVRasterPulse/README.md)

[Translation policy](../../README.md)

</details>
<!-- nv-language-navigation:end -->

<!-- nv-translation-notice:start -->
> Tafsiri inayosaidiwa na mashine kutoka kwa Kiingereza. Majina ya kiufundi, amri, URL na maandishi asili ya kisheria yanahifadhiwa. Uhakiki wa mzungumzaji asilia unakaribishwa; angalia rejeleo la Kiingereza ikiwa maneno hayako wazi.
<!-- nv-translation-notice:end -->

<a id="nvrasterpulse"></a>
# NVRasterPulse

**Vikomo vya FPS kwa kila ombi kupitia RivaTuner Statistics Server.**

> **Sakinisha RTSS kwanza.** NVRasterPulse inahitaji [RivaTuner Statistics Server (RTSS), iliyopakuliwa kutoka Guru3D](https://www.guru3d.com/download/rtss-rivatuner-statistics-server-download/). RTSS lazima iwe inaendesha ili kutekeleza vikomo. Hakuna kisakinishi cha RTSS, ndoano ya DLL au SDK imeunganishwa.

[Pakua 0.1 & hali](../docs/downloads.md#nvrasterpulse) · [Ufungaji](#installation) · [Jinsi mipaka inavyofanya kazi](#usage) · [Leseni](../../../../NVRasterPulse/LICENSE)

<a id="overview-and-purpose"></a>
## Muhtasari na madhumuni

NVRasterPulse ni kiolesura cha Windows cha kudhibiti vikomo vya fremu vya RTSS kwa jina linaloweza kutekelezeka. RTSS hufanya kizuizi. NVRasterPulse hudhibiti thamani zinazolingana za wasifu, hifadhi rudufu na maombi ya kupakia upya, kwa ufikiaji wa trei na chaguo zinazoendelea.

Inapatikana ili kurahisisha kuhariri vikomo kamili vya kila mchezo bila kubadilisha wasifu mzima wa RTSS au kutatiza mipangilio yake ya kuwekelea. Mgombea wa sasa wa **0.1** ni muundo wa Septemba 9, 2026 na hundi inayohitajika ya usakinishaji ya RTSS.

<a id="features"></a>
## Vipengele

- Chagua programu inayoendeshwa au ongeza inayoweza kutekelezeka wewe mwenyewe.
- Okoa vikomo vya FPS kutoka 1 hadi 1000, na hadi nafasi tatu za desimali.
- Usimbaji halisi wa kimantiki wa thamani zilizoingizwa: 59.94 inakuwa 2997/50.
- Usanidi wa Usawazishaji wa Ukingo wa Mbele (`SyncLimiter=1`) na usubiri amilifu (`PassiveWait=0`).
- Masasisho ya wasifu yanayoweza kutekelezwa, nakala rudufu za kiotomatiki na maandishi ya atomiki.
- Kuondolewa kwa vikomo vya kubatilisha huku tukihifadhi maudhui mengine ya wasifu.
- Ugunduzi wa usakinishaji wa RTSS, uteuzi wa njia mwenyewe na uzinduzi / upakiaji upya.
- Uendeshaji wa trei ya mfano mmoja, uanzishaji wa hiari uliosakinishwa, lugha 34 na mada nne.
- Tenganisha kuacha kawaida na ** Acha + RTSS** vitendo.

<a id="compatibility"></a>
## Utangamano

| Sharti | Maelezo |
| --- | --- |
| Mfumo | Windows 10/11 x64 |
| Muda wa kukimbia | [NET Framework 4.8](https://dotnet.microsoft.com/en-us/download/dotnet-framework/net48), imewekwa kando ikiwa inahitajika |
| Programu inayohitajika | RTSS na `RTSS.exe`, saraka inayolingana ya `Profiles` na usaidizi unaolingana wa wasifu/pakia upya |
| GPU | Utangamano wa RTSS huamua kikomo; meneja wa wasifu huu hauhitaji kizazi fulani cha RTX |
| Ruhusa | Maombi ya sasa ya maombi ya kufikia msimamizi; folda ya wasifu iliyochaguliwa ya RTSS lazima ipatikane |
| Michezo | Inategemea usaidizi wa kuunganisha wa RTSS na vizuizi vya kila mchezo; hakuna dhamana ya kupambana na kudanganya |

Hakuna toleo mahususi la RTSS ambalo limeidhinishwa kwa kila utendakazi na ukaguzi huu wa kitovu. Tumia usambazaji rasmi wa sasa na uripoti toleo kamili ikiwa ufunguo wa wasifu/upakiaji upya haufanyi kazi. Imewekwa-lakini-kusimamishwa RTSS hupitisha hundi ya usakinishaji; ni lazima basi ianzishwe kwa ukomo halisi.

<a id="installation"></a>
## Ufungaji

1. **[Pakua na usakinishe RTSS kutoka Guru3D](https://www.guru3d.com/download/rtss-rivatuner-statistics-server-download/).**
2. Fungua [Vipakuliwa vya NVRasterPulse](../docs/downloads.md#nvrasterpulse) na uangalie upatikanaji wa Toleo.
3. Pakua `NVRasterPulse-0.1-win-x64-Setup.exe` au `NVRasterPulse-0.1-win-x64-portable.zip`, pamoja na arifa/hesabu za hundi.
4. Linganisha SHA-256. Tekeleza Mipangilio au toa ZIP nzima inayoweza kusongeshwa kwenye folda ya ndani inayoweza kuandikwa.
5. Fungua `NVRasterPulse.exe`. Ikiwa RTSS haipo, tumia **Pakua RTSS**, isakinishe, kisha **Angalia tena**, au uchague `RTSS.exe` wewe mwenyewe.
6. Anzisha RTSS ukitumia njia yake ya mkato ya kawaida au kitufe cha NVRasterPulse's RTSS ikiwa imesimamishwa.

Kuzima kikumbusho cha hiari hakuruki ukaguzi wa sharti. Uanzishaji wa trei ya Windows kimya husubiri hadi dirisha kuu lifunguke kabla ya kuonyesha hundi hii. Mipangilio inasakinisha NVRasterPulse pekee. EXE zake hazijasainiwa.

<a id="usage"></a>
## Matumizi

1. Chagua programu inayoendeshwa inayokusudiwa au uvinjari kwa EXE ya mchezo wake.
2. Weka kikomo kati ya 1 na 1000 FPS, ikijumuisha thamani ya sehemu ikihitajika.
3. Hifadhi na uangalie matokeo yaliyoripotiwa. NVRasterPulse inasasisha wasifu wa RTSS unaotekelezeka na kuomba upakiaji upya.
4. Thibitisha kuwa RTSS inaendeshwa na uthibitishe tabia katika mchezo unaokusudiwa.

Profaili zimewekwa na **jina linaloweza kutekelezeka**, kama vile `Game.exe.cfg`. Folda mbili tofauti zilizo na `Game.exe` zinashiriki wasifu sawa wa RTSS; kuhifadhi njia kamili hakuondoi mgongano huu.

Kuhifadhi hutumia Usawazishaji wa Mbele ya Mbele na kusubiri amilifu. Kusubiri kwa bidii kunaweza kuongeza matumizi ya CPU. Sehemu mbadala za `LimitTime` hazibadilishwi. Maoni yaliyopo, mipangilio ya kuwekelea na `EnableHooking=0` huhifadhiwa. Wasifu wa RTSS Global haujabadilishwa.

Tumia kitendo cha tupio kuondoa vikomo vya NVRasterPulse. Haifuti wasifu wote wa RTSS. Kikomo kilichorithiwa kutoka RTSS Global au zana nyingine bado kinaweza kutumika baadaye.

**Kufunga na kuacha:** dirisha kuu linaweza kujificha kwenye trei. **Ondoka** ya Kawaida huacha RTSS ikiendelea na vikomo vilivyohifadhiwa vikiwa sawa. **Ondoka + RTSS** inaomba kufungwa kwa kawaida kwa mchakato wa RTSS unaolingana katika kipindi cha sasa, inasubiri hadi sekunde nane na hailazimishi kuua. Mipaka iliyohifadhiwa inabaki katika hali zote mbili.

Lugha na mandhari huchaguliwa katika programu. Kuanzisha katika Windows kuingia ni hiari na kunalenga nakala iliyosakinishwa. Kitufe cha habari kinaelezea vitendo vya kawaida.

<a id="screenshots"></a>
## Picha za skrini

![Onyesho la kukagua dirisha kuu la NVRasterPulse](../../../../assets/screenshots/nvrasterpulse-0.1-preview.png)

Kiolesura kilichopo cha 0.1 cha Kifaransa kikitoa kwa mfano majina yanayoweza kutekelezeka na thamani ya 176 FPS. RTSS imeonyeshwa imesimamishwa; hiki ni kielelezo cha kiolesura, si kikomo kinachoendesha au kipimo cha kusubiri. [Asili ya picha](../assets/README.md).

<a id="update-and-uninstall"></a>
## Sasisha na uondoe

Acha NVRasterPulse, pakua na uthibitishe toleo jipya, kisha endesha Usanidi wake au toa kinachobebeka kwenye folda mpya. Hifadhi mipangilio na chelezo za RTSS. Masasisho ya RTSS ni tofauti na yanatoka Guru3D.

Ili kuondoa nakala iliyosakinishwa, tumia Windows **Installed apps**. Kwa kubebeka, acha kisha uondoe folda yake iliyotolewa wakati nakala zako ziko salama. Vikomo vya RTSS vilivyohifadhiwa haviondolewi kwa kusanidua NVRasterPulse: ondoa ubatilifu wa kikomo kilichokusudiwa kwanza. RTSS ina kiondoa chake.

Jimbo la ndani: `%LOCALAPPDATA%\NVRasterPulse`. Hifadhi nakala za RTSS otomatiki: `%LOCALAPPDATA%\NVRasterPulse\Backups\RTSS`. Eneo la zamani la `%LOCALAPPDATA%\RTSSProfileBridge` linaweza kusomwa kwa uhamiaji. Faili hizi zinaweza kuwa na njia za kibinafsi zinazoweza kutekelezwa na hazifai kuchapishwa hadharani.

<a id="known-limitations"></a>
## Vikwazo vinavyojulikana

- RTSS hufanya kofia. Thamani iliyohifadhiwa au ombi lililofanikiwa la kupakia upya si matokeo yaliyopimwa ya muda wa fremu.
- Vitekelezo vya jina moja hushiriki wasifu.
- Kikomo kingine cha kimataifa/kwa kila mchezo kinaweza kuathiri matokeo; kuzima ubatilishaji wa ndani hakuondoi kofia iliyorithiwa.
- Hook ya RTSS iliyozimwa kimakusudi bado imezimwa.
- Kusubiri kikamilifu kuna CPU/power off trade-off.
- Hakuna mchezo wa jumla, kupinga udanganyifu au uthibitishaji wa kusubiri wa mwisho hadi mwisho.
- Injini huru ya kikomo ya majaribio ya awali haijakusanywa au kusafirishwa.
- Hifadhi rudufu otomatiki haimaanishi kiolesura cha mbofyo mmoja kamili chelezo.

<a id="troubleshooting"></a>
## Kutatua matatizo

| Dalili | Kitendo |
| --- | --- |
| RTSS sharti bado wazi | Chagua `RTSS.exe` halisi na folda ya Profaili inayolingana, kisha Angalia tena. |
| Kikomo kimehifadhiwa lakini hakuna athari | Anzisha RTSS; thibitisha mchezo sahihi wa EXE/wasifu, ruhusa za ndoano na vikomo vingine. |
| Imeshindwa kuhifadhi | Angalia ruhusa za folda na uhifadhi hitilafu iliyoonyeshwa / chelezo. |
| Kikomo kinabaki baada ya kuondolewa | Kagua RTSS Global na zana zingine; kitendo cha tupio huondoa tu kubatilisha kikomo cha ndani. |
| Michezo miwili hupokea kikomo sawa | Angalia ikiwa majina yao ya faili yanayoweza kutekelezwa yanafanana. |
| Acha + RTSS inaacha RTSS wazi | Funga RTSS kawaida mwenyewe; amri hii inaepuka kwa makusudi kukomesha kwa lazima. |

Ikiwa unarejesha mwenyewe hifadhi rudufu ya RTSS, funga RTSS kwanza na uhifadhi wasifu wa sasa kabla ya kuubadilisha na chelezo inayokusudiwa. Hii inaweza kubatilisha uhariri wa wasifu ambao hauhusiani; kagua faili na tarehe. [Usaidizi wa pamoja](../docs/support.md).

<a id="faq"></a>
## Maswali Yanayoulizwa Mara kwa Mara

**Je, ninahitaji MSI Afterburner pia?** NVRasterPulse inahitaji RTSS; haitegemei programu ya Afterburner. Fuata chaguzi za usakinishaji za msambazaji wa RTSS.

**Je, ninaweza kutumia hii bila RTSS kufanya kazi?** Unaweza kudhibiti wasifu mara usakinishaji utakapogunduliwa, lakini RTSS lazima ifanyike ili kuwekewa vikwazo.

**Je, kuacha au kusanidua huondoa vifuniko?** Hapana. Ondoa vidhibiti unavyotaka kwa uwazi kabla ya kuondoa NVRasterPulse.

**Je, ni fork ya RTSS?** Hapana. Ni meneja wa wasifu huru; hakuna chanzo cha RTSS au kinachoweza kutekelezeka kimejumuishwa.

<a id="upstream-modifications-and-credits"></a>
## Juu, marekebisho na mikopo

Hifadhi ya ukuzaji inatoka kwa [Orbmu2k's NVIDIA Profile Inspector](https://github.com/Orbmu2k/nvidiaProfileInspector). Rasilimali zake za MIT/UI zimepewa sifa. Huduma za udhibiti wa wasifu, usimbaji wa sehemu, hifadhi rudufu, daraja la upakiaji upya la RTSS, tabia ya trei, mwongozo wa sharti, lugha na ikoni mahususi ya programu iliundwa/kuchukuliwa na 禅堂 Zendo (RevoluSound Team).

RTSS imetengenezwa na **Unwinder** na kusambazwa kando kupitia Guru3D. NVRasterPulse inaita `UpdateProfiles` kutoka kwa ndoano iliyochaguliwa iliyochaguliwa ya DLL; hakuna RTSS SDK au ndoano ya ndoano inasambazwa tena. Kisakinishi hutumia Inno Setup 7.1.0 ambayo haijabadilishwa iliyo na hati/tafsiri zilizorekebishwa na kiunzi cha mradi.

[Asili kamili](../docs/provenance.md) · [Jedwali la mtu wa tatu](../THIRD_PARTY_NOTICES.md)

<a id="license"></a>
## Leseni

Kifurushi hiki kinasambaza NVRasterPulse kwa uwazi chini ya [Leseni ya MIT](../../../../NVRasterPulse/LICENSE) iliyotolewa, ikihifadhi Hakimiliki (c) 2016 Orbmu2k. Chanzo cha maombi kinatunzwa kwa faragha; MIT haihitaji uchapishaji wa chanzo kilichobadilishwa. RTSS na Windows/.NET zinasalia chini ya masharti yao wenyewe. [Arifa kamili](LICENSES/README.md).

Kujitegemea kwa NVIDIA Corporation, MSI na RTSS; haijafadhiliwa au kuidhinishwa rasmi nao. Majina ya bidhaa yanasalia kuwa alama za biashara za wamiliki wao.
