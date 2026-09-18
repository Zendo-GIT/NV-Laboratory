<!-- nv-language-navigation:start -->
🌐 [English](../../../../NVDriverForge/README.md) | [Français](../../../../NVDriverForge/README.fr.md) · [NV Laboratory](../README.md)

<details>
<summary>🌐 Language · 34</summary>

[العربية](../../ar/NVDriverForge/README.md) · [বাংলা](../../bn/NVDriverForge/README.md) · [简体中文](../../zh/NVDriverForge/README.md) · [Čeština](../../cs/NVDriverForge/README.md) · [Dansk](../../da/NVDriverForge/README.md) · [Nederlands](../../nl/NVDriverForge/README.md) · [English](../../../../NVDriverForge/README.md) · [Filipino](../../fil/NVDriverForge/README.md) · [Suomi](../../fi/NVDriverForge/README.md) · [Français](../../../../NVDriverForge/README.fr.md) · [Deutsch](../../de/NVDriverForge/README.md) · [Ελληνικά](../../el/NVDriverForge/README.md) · [हिन्दी](../../hi/NVDriverForge/README.md) · [Magyar](../../hu/NVDriverForge/README.md) · [Bahasa Indonesia](../../id/NVDriverForge/README.md) · [Italiano](../../it/NVDriverForge/README.md) · [日本語](../../ja/NVDriverForge/README.md) · [한국어](../../ko/NVDriverForge/README.md) · [मराठी](../../mr/NVDriverForge/README.md) · [فارسی](../../fa/NVDriverForge/README.md) · [Polski](../../pl/NVDriverForge/README.md) · [Português](../../pt/NVDriverForge/README.md) · [ਪੰਜਾਬੀ](../../pa/NVDriverForge/README.md) · [Română](../../ro/NVDriverForge/README.md) · [Русский](../../ru/NVDriverForge/README.md) · [Español](../../es/NVDriverForge/README.md) · **Kiswahili** · [Svenska](../../sv/NVDriverForge/README.md) · [தமிழ்](../../ta/NVDriverForge/README.md) · [ไทย](../../th/NVDriverForge/README.md) · [Türkçe](../../tr/NVDriverForge/README.md) · [Українська](../../uk/NVDriverForge/README.md) · [اردو](../../ur/NVDriverForge/README.md) · [Tiếng Việt](../../vi/NVDriverForge/README.md)

[Translation policy](../../README.md)

</details>
<!-- nv-language-navigation:end -->

<!-- nv-translation-notice:start -->
> Tafsiri inayosaidiwa na mashine kutoka kwa Kiingereza. Majina ya kiufundi, amri, URL na maandishi asili ya kisheria yanahifadhiwa. Uhakiki wa mzungumzaji asilia unakaribishwa; angalia rejeleo la Kiingereza ikiwa maneno hayako wazi.
<!-- nv-translation-notice:end -->

<a id="nvdriverforge"></a>
# NVDriverForge

**Andaa usakinishaji wa kiendeshaji wa NVIDIA na chaguo wazi za sehemu na mipangilio ya hiari.**

[Pakua 0.1.4 & hali](../docs/downloads.md#nvdriverforge) · [Ufungaji](#installation) · [Mikopo](#credits-and-upstream) · [Leseni](../../../../NVDriverForge/LICENSE)

<a id="overview-and-purpose"></a>
## Muhtasari na madhumuni

NVDriverForge hukuongoza kupitia kifurushi asili cha kiendeshi cha NVIDIA: chagua kiendeshi, kagua vipengee vyake, kagua marekebisho ya hiari, kisha uthibitishe usakinishaji. Inapatikana ili kufanya chaguo hizo kueleweka na kuweka usakinishaji, utendakazi maalum na maelezo ya urejeshaji pamoja.

Ni programu iliyotengenezwa kwa kujitegemea iliyochochewa kwa sehemu na mtiririko wa kazi wa NVCleanstall. Haijumuishi NVCleanstall au kudai usawa kamili wa kipengele.

<a id="features"></a>
## Vipengele

- NVIDIA Game Ready / Studio utafutaji na upakuaji; ugunduzi wa hiari wa hotfix kwa njia mbadala.
- Uchambuzi wa kifurushi asili, heshi, saini za NVIDIA, maonyesho na maingizo yanayolingana ya INF.
- Uchaguzi wa vipengele na utegemezi na uhifadhi wa vipengele visivyojulikana.
- Toleo la 0.1.4 huweka vipengele vilivyochaguliwa vya NVIDIA kurukwa na haijumuishi vipengee vilivyothibitishwa ambavyo havijachaguliwa kutoka kwa ugunduzi. Saa za hiari za sasa au zisizotumika hazilazimishwi tena kama vipengee muhimu.
- Futa muhtasari wa kushindwa kwa usakinishaji na ufikiaji wa kumbukumbu za kina katika lugha zote 34.
- Huangalia utayari, uthibitisho wazi, usafirishaji wa duka la kiendeshi na nakala asili ya wasifu wa NVIDIA kabla ya kusakinisha.
- Mipangilio ya kina ya hiari, iliyo na ukaguzi wa kabla ya safari ya ndege, majarida na urejeshaji unaotambua migogoro.
- Hiari **Custom NV** iliyowekwa awali ikiwa na chaguo na maelezo yaliyotajwa, ikijumuisha uteuzi tofauti wa nguvu wa SILK na ukaguzi wa uoanifu.
- Vipakuliwa vya kiraka vya NVENC vya toleo halisi la hiari; ahadi ya chanzo na baiti lengwa huangaliwa.
- Usakinishaji tofauti, wa hiari wa Profile Inspector fork kutoka kwa skrini ya Zana.
- Mwongozo wa vipengele, mapendeleo yanayoweza kutumika tena, vifaa vya kiendeshi, ripoti za usaidizi wa ndani na masasisho ya hiari ya programu.
- Lugha 34 za kiolesura na mada nne.

Chaguzi za kina zinazopatikana zinahusu MPO, kiashirio cha DLSS, Ansel, usingizi wa sauti wa NVIDIA, MSI, sera ya kukatiza/kipaumbele, HDCP, uanzishaji wa kontena na huduma ya urithi inayostahiki. Kila moja ina sharti na athari zake; haya si maboresho ya utendaji kwa wote.

<a id="compatibility"></a>
## Utangamano

| Sharti | Maelezo |
| --- | --- |
| Mfumo | Windows 10 jenga 19041 au mpya zaidi / Windows 11, x64 |
| GPU/dereva | Kifurushi kinacholingana cha NVIDIA na vifaa vilivyogunduliwa; ukaguzi wa katalogi kiotomatiki kimsingi unashughulikia miundo inayojulikana ya GeForce |
| Muda wa kukimbia | .NET 8 / WPF 8.0.31 imejumuishwa kwenye kifurushi kinachojitosheleza kilichotayarishwa |
| Mapendeleo | Usanidi wa kawaida wa UI/kwa kila mtumiaji; usakinishaji wa dereva na mabadiliko ya mfumo huomba ufikiaji wa msimamizi |
| Mtandao | Inahitajika kwa utafutaji/upakuaji wa NVIDIA mtandaoni na maombi ya wazi ya NVENC; dereva wa asili wa ndani anaweza kuchaguliwa |
| Vifaa vilivyojumuishwa | 7-Zip 26.03 ambayo haijabadilishwa, arifa za wakati wa utekelezaji, MIT Profile Inspector mshirika wa hiari. |
| Mwenzi wa hiari | NET Framework 4.8 kwa Profile Inspector fork tofauti |

Hakuna toleo la kiendeshi cha chini kiholela linalojumuisha vipengele vyote. Utafutaji wa Multi-GPU lazima ulingane na kila GPU iliyotambuliwa. Miundo isiyotumika/kitaalamu inaweza kuhitaji uteuzi wa kiendeshi mwenyewe. Kisakinishi cha NVIDIA kinasalia kuwa mamlaka ya mwisho ya maunzi/OS.

<a id="installation"></a>
## Ufungaji

1. Tembelea [vipakuliwa](../docs/downloads.md#nvdriverforge) na uthibitishe kuwa Toleo limechapishwa.
2. Chagua `NVDriverForge-Setup.exe` kwa usakinishaji, au `NVDriverForge.exe` kwa matumizi ya kubebeka.
3. Linganisha SHA-256 na `SHA256SUMS.txt` ya Toleo.
4. Endesha Usanidi kwa usakinishaji wa kila mtumiaji na kiondoa kiwango cha kawaida, au weka EXE inayobebeka kwenye folda inayoweza kuandikwa na uifungue.

Inabebeka ni pamoja na wakati wake wa kutumika na kisakinishi chake cha hiari. Kufunga NVDriverForge hakusakinishi kiendeshaji cha GPU. EXE zake hazijasainiwa kwa sasa.

<a id="usage"></a>
## Matumizi

1. **Dereva:** pakua kutoka NVIDIA au chagua kisakinishi asili cha NVIDIA EXE. Acha uchambuzi umalize.
2. **Vipengele:** kagua maelezo na vitegemezi vinavyohitajika. Vipengele visivyojulikana huhifadhiwa.
3. **Marekebisho:** acha chaguo zisizohitajika bila kubadilishwa. Soma athari na ubadilishanaji kabla ya kuchagua chochote.
4. **Kagua:** angalia kiendeshi, vijenzi na shughuli za hiari, kisha uthibitishe usakinishaji.
5. Kubali UAC kwa operesheni uliyochagua pekee. Weka maagizo ya kurejesha kazi iliyolindwa.
6. Ikiwa kiendeshi kipya kinahitaji kuwashwa upya, fuata hali iliyoripotiwa. Shughuli zilizoahirishwa zinahitaji urejesho wazi baada ya kuwasha tena.

Custom NV inaanza bila kubadilika. Chagua thamani zilizotajwa au kagua uwekaji awali uliotolewa na vizuizi vyake. Sehemu zake mbili za habari za ndani hazijaandikwa kwa kujitegemea. Mipangilio inatumika tu katika mtiririko wa kiendeshi kipya uliothibitishwa, kamwe kwa kufungua onyesho la kukagua. Kusakinisha kihariri tofauti cha NVPI haihitajiki.

Hiari ya NVENC hupakua data inayooana kutoka kwa ahadi iliyobandikwa ya keylase. Inabadilisha DLL mbili za dereva na kubatilisha saini zao; inaweza kukataliwa na Windows, encoders, DRM au anti-cheat. Hakuna data kama hiyo au NVIDIA DLL iliyopachikwa katika NVDriverForge. [Viwango na mipaka ya leseni](../docs/provenance.md).

Lugha ya udhibiti wa mapendeleo, mandhari na ukaguzi wa hiari wa masasisho ya mtumiaji aliyesakinishwa. Kibebeka hakiundi kazi iliyosakinishwa ya kuangalia usuli. Zana na urejeshaji ni tofauti na hatua nne za ufungaji.

<a id="backup-and-diagnostic-tools"></a>
## Vifaa vya chelezo na uchunguzi

**Kabla ya usakinishaji:** ukaguzi wa utayari hufunika saini ya kifurushi, GPU, makadirio ya nafasi ya kazi/nafasi ya kuhifadhi nakala, inayosubiri kuanzishwa upya na visakinishaji shindani. Mfanyakazi aliyeinuliwa huwarudia. Michakato ya ushindani haizuiliwi kiotomatiki. Nakala asilia ya hifadhidata ya wasifu wa NVIDIA lazima ifaulu kabla ya Usanidi wa NVIDIA kuanza; uhamishaji wa duka la dereva ni chelezo tofauti.

**Chaguo zinazoweza kutumika tena:** mwongozo wa sehemu unauliza maswali manne kuhusu michezo, sauti, NVIDIA App na kurekodi. Pitia mapendekezo yake; zinazohitajika, zisizojulikana na vipengele tegemezi vinasalia kulindwa. Hamisha mapendeleo, kisha uhakiki na uyahakikishe upya dhidi ya kifurushi kilichochaguliwa wakati wa kuleta. Idhini, kuanzisha upya shughuli, njia za programu na upakiaji wa viraka haziagizwi.

**Kifaa cha udereva:** hamisha `.nvdfkit.zip` ili kuweka kisakinishi cha awali cha NVIDIA kilichotiwa saini, chaguo, heshi na maagizo pamoja. Beba `NVDriverForge.exe` kando. Ingiza kit katika Zana, kagua onyesho la kukagua, kisha utumie mtiririko wa kawaida wa usakinishaji. Hiki si kiendeshi chembamba au kisakinishi cha pekee kilichorekebishwa. NVENC ya hiari bado inahitaji upakuaji na idhini kwa kiendeshaji hicho. Masharti ya ugawaji upya ya NVIDIA bado yanatumika.

**Matokeo na usaidizi:** soma tokeo fupi na upanue maelezo ya kila hatua/kila chaguo. Usomaji uliofanikiwa huthibitisha thamani iliyohifadhiwa, sio uboreshaji uliopimwa. Ripoti ya usaidizi ya JSON ya ndani hutumia sehemu zilizoorodheshwa, ikijumuisha kazi ya mwisho iliyohifadhiwa baada ya kuanzisha upya programu. Ichunguze kabla ya kuhifadhi au kushiriki. Haijumuishi kumbukumbu mbichi, yaliyomo kwenye wasifu au vitambulishi vya maunzi na haipakii kiotomatiki.

**Urejeshaji:** fuata mwongozo wa kazi iliyolindwa ili kurejesha kiendeshi kilichochelezwa. Urejeshaji wa wasifu ulio wazi unahitaji toleo asili la kiendeshi na GPU sawa; inachukua nafasi ya hifadhidata nzima, huhifadhi nakala ya sasa, na hukagua heshi na hali inayokinzana. Usifute jarida lake au kulazimisha kutolingana. Usakinishaji halisi wa kiendeshi, urejeshaji kamili na uletaji wa wasifu asilia na mtiririko huu mpya wa kazi unasalia kuwa bila kuthibitishwa kwenye mfumo halisi.

**Sasisho za programu:** soma madokezo ya toleo, kisha uchague kwa uwazi kipakuliwa kilichothibitishwa na SHA-256. Kuangalia ni kwa chaguo-msingi, na hundi ya hiari wakati wa kuanza. Hakuna kisakinishi kinachoanzishwa kiotomatiki. Kipengele hiki ni tofauti na ukaguzi wa sasisho za viendeshaji na kazi ya hiari ya kuangalia kiendeshi cha toleo lililosakinishwa.

<a id="screenshots"></a>
## Picha za skrini

![Onyesho la kukagua ukurasa wa viendeshaji wa NVDriverForge](../../../../assets/screenshots/nvdriverforge-0.1.2-preview.png)

0.1.2 iliyopo ya kiolesura cha Kifaransa inatoa na data ya mfano; imehifadhiwa kama onyesho la kukagua kiolesura. Kiendeshaji cha 699.99 kilichoonyeshwa ni toleo la majaribio, si toleo halisi la kupakua. [Asili ya picha](../assets/README.md).

<a id="update-and-uninstall"></a>
## Sasisha na uondoe

Funga NVDriverForge, pata kifurushi rasmi kinachofuata na uthibitishe heshi yake. Tumia kitambulisho sawa cha Kuweka kwa sasisho lililosakinishwa; badilisha EXE inayoweza kusongeshwa na mpya. Weka mipangilio na kazi zilizolindwa.

Uninstall kutoka Windows **Installed apps**. Inaondoa programu na kazi yake ya kusasisha, sio kiendeshi cha NVIDIA. Mipangilio, kumbukumbu na nakala zimesalia. Ukipenda, rejesha mabadiliko ya hali ya juu/NVENC kupitia mtiririko wa urejeshaji uliorekodiwa **kabla** kuondoa programu. Rejesha inakataa mabadiliko yanayokinzana kutoka kwa zana nyingine.

Data ya ndani iko chini ya `%LOCALAPPDATA%\NVDriverForge`; kazi zinazolindwa na usafirishaji wa madereva ziko chini ya `%PROGRAMDATA%\NVDriverForge\Jobs`. Matumizi ya kubebeka pia huunda data ya ndani. Uhamishaji wa duka la kiendeshi na nakala asili ya wasifu ni tofauti. Wala si picha ya mfumo.

<a id="known-limitations"></a>
## Vikwazo vinavyojulikana

- Hakuna nyongeza za maunzi/uhariri wa INF, saini za NVIDIA zilizoundwa upya, kujiuzulu kwa kupingana na udanganyifu au kukubali onyo kiotomatiki bila kusainiwa.
- Hakuna uondoaji kamili wa telemetry/matangazo, uhamishaji wa kifurushi chembamba au urejeshaji kamili kiotomatiki kwa kiendeshi cha awali.
- Ufungaji wa kiendeshi, urejeshaji wa buti na uandishi wa hiari wa wasifu haujathibitishwa kikamilifu kwenye mashine halisi na ukaguzi wa kitovu.
- Usomaji wa Usajili sio uthibitisho wa HDCP halisi, utendaji au athari za kusubiri.
- Ukaguzi wa saini hutumia uaminifu wa Windows unaopatikana ndani; ubatilishaji mtandaoni haufanyiki.
- Lugha 34 zipo, lakini majaribio kamili ya mzungumzaji asilia/ufikivu bado hayajakamilika.

<a id="troubleshooting"></a>
## Kutatua matatizo

| Dalili | Kitendo |
| --- | --- |
| Katalogi ya mtandaoni haipatikani | Chagua kifurushi asili kutoka kwa [Pakua driver za kifaa NVIDIA](https://www.nvidia.com/en-us/drivers/). Usibadilishe mfano wa GPU wa jirani. |
| Utafutaji wa Hotfix haupatikani | Tumia [jukwaa la viendeshaji la NVIDIA's Game Ready](https://www.nvidia.com/en-us/geforce/forums/game-ready-drivers/13/) na uthibitishe kifurushi halisi. |
| Usakinishaji wa NVIDIA haukufaulu | Soma muhtasari wa kushindwa na ufungue kumbukumbu za kina. Vipengee vya hiari ambavyo tayari ni vya sasa au visivyotumika vinasalia kurukwa katika 0.1.4. Usakinishaji ambao haujafaulu hausababishi mabadiliko ya hiari au mtiririko wa mafanikio/kuzima upya. |
| Kushindwa kwa sahihi/heshi/chelezo | Acha usakinishaji huo na uhifadhi kosa; pata kifurushi asili tena ikiwa kimeharibika. |
| Chaguo halipatikani | Soma maunzi yake, sehemu au sababu ya kiendeshi-lengwa; weka bila kubadilika. |
| Anzisha tena au kazi bado inasubiri | Tumia maagizo ya kurejesha kazi na uendelee wazi; usifute jarida lake. |
| Rejesha mzozo | Hali nyingine inatofautiana na shughuli iliyorekodiwa. Ihifadhi na uombe usaidizi badala ya kulazimisha kurejeshwa. |

Kwa ripoti, ni pamoja na toleo la zana iliyochaguliwa, Windows, GPU, dereva na hatua zinazoweza kuzaliana; rekebisha njia na maelezo ya kibinafsi kutoka kwa kumbukumbu. [Msaada](../docs/support.md).

<a id="faq"></a>
## Maswali Yanayoulizwa Mara kwa Mara

**Je, Usanidi husakinisha kiendeshi cha michoro?** Hapana. Hilo linahitaji uchanganuzi tofauti wa programu, ukaguzi, uthibitishaji na mchakato wa usakinishaji wa hali ya juu.

**Je, ninahitaji NVCleanstall au NVPI?** Hapana. NVCleanstall ni msukumo pekee. Mshirika wa Profile Inspector ni mhariri wa hiari huru.

**Je, inafanya kila kiendeshi cha NVIDIA kuwa ndogo au kasi zaidi?** Hapana. Vipengee vilivyochaguliwa na sharti huamua nini kinaweza kubadilika; hakuna faida iliyopimwa iliyoahidiwa.

**Vyanzo viko wapi?** Chanzo mahususi cha programu na majaribio ya kibinafsi hudumishwa kando. Kitovu hiki hutoa hati, jozi na viungo vya chanzo vya wahusika wengine vinavyohitajika kwa maelezo/leseni.

<a id="credits-and-upstream"></a>
## Mikopo na mkondo wa juu

Programu asilia, mtiririko wa kazi, miamala, ujanibishaji, bootstrap na urekebishaji: 禅堂 Zendo (RevoluSound Team).

- [NVCleanstall / TechPowerUp](https://www.techpowerup.com/download/techpowerup-nvcleanstall/): msukumo wa mtiririko wa kazi; hakuna chanzo au binary iliyoingizwa.
- [NVIDIA Profile Inspector / Orbmu2k](https://github.com/Orbmu2k/nvidiaProfileInspector): Mandhari ya MIT, marejeleo ya kiolesura cha NVAPI na vifurushi tofauti vya fork.
- [7-Zip / Igor Pavlov](https://www.7-zip.org/): zana za uchimbaji ambazo hazijarekebishwa.
- [Microsoft .NET](https://github.com/dotnet/runtime) na [WPF](https://github.com/dotnet/wpf): wakati wa utekelezaji uliounganishwa.
- [Inno Setup](https://jrsoftware.org/isinfo.php): injini ya kisakinishi asili na tafsiri zilizowekwa alama.
- [keylase/nvidia-patch](https://github.com/keylase/nvidia-patch): chanzo cha data cha hiari cha NVENC; leseni ya ugawaji upya haijaanzishwa.
- [NVIDIA](https://www.nvidia.com/en-us/drivers/): upakuaji wa viendeshaji vya nje na kusakinisha maktaba za NVAPI/NVML.

[Jedwali la sehemu kamili](../THIRD_PARTY_NOTICES.md) · [Mabadiliko na asili](../docs/provenance.md)

<a id="license"></a>
## Leseni

[Ruhusa iliyopo ya usambazaji wa mfumo wa jozi](../../../../NVDriverForge/LICENSE) inaruhusu kutumia na kushiriki utekelezeji rasmi ambao haujarekebishwa na arifa zao. Haki za chanzo mahususi za programu zimehifadhiwa. Haizuii haki zinazotolewa na leseni tofauti za wahusika wengine. [Arifa kamili](LICENSES/README.md).

Kujitegemea kwa NVIDIA Corporation, TechPowerUp na keylase; haijafadhiliwa au kuidhinishwa rasmi nao. Majina ya bidhaa yanasalia kuwa alama za biashara za wamiliki wao.
