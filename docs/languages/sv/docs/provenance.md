<!-- nv-language-navigation:start -->
🌐 [English](../../../provenance.md) | [Français](../../../provenance.fr.md) · [NV Laboratory](../README.md)

<details>
<summary>🌐 Language · 34</summary>

[العربية](../../ar/docs/provenance.md) · [বাংলা](../../bn/docs/provenance.md) · [简体中文](../../zh/docs/provenance.md) · [Čeština](../../cs/docs/provenance.md) · [Dansk](../../da/docs/provenance.md) · [Nederlands](../../nl/docs/provenance.md) · [English](../../../provenance.md) · [Filipino](../../fil/docs/provenance.md) · [Suomi](../../fi/docs/provenance.md) · [Français](../../../provenance.fr.md) · [Deutsch](../../de/docs/provenance.md) · [Ελληνικά](../../el/docs/provenance.md) · [हिन्दी](../../hi/docs/provenance.md) · [Magyar](../../hu/docs/provenance.md) · [Bahasa Indonesia](../../id/docs/provenance.md) · [Italiano](../../it/docs/provenance.md) · [日本語](../../ja/docs/provenance.md) · [한국어](../../ko/docs/provenance.md) · [मराठी](../../mr/docs/provenance.md) · [فارسی](../../fa/docs/provenance.md) · [Polski](../../pl/docs/provenance.md) · [Português](../../pt/docs/provenance.md) · [ਪੰਜਾਬੀ](../../pa/docs/provenance.md) · [Română](../../ro/docs/provenance.md) · [Русский](../../ru/docs/provenance.md) · [Español](../../es/docs/provenance.md) · [Kiswahili](../../sw/docs/provenance.md) · **Svenska** · [தமிழ்](../../ta/docs/provenance.md) · [ไทย](../../th/docs/provenance.md) · [Türkçe](../../tr/docs/provenance.md) · [Українська](../../uk/docs/provenance.md) · [اردو](../../ur/docs/provenance.md) · [Tiếng Việt](../../vi/docs/provenance.md)

[Translation policy](../../README.md)

</details>
<!-- nv-language-navigation:end -->

<!-- nv-translation-notice:start -->
> Maskinassisterad översättning från engelska. Tekniska namn, kommandon, URL:er och ursprungliga lagtexter bevaras. Recension av modersmål är välkommen; konsultera den engelska referensen om formuleringen är otydlig.
<!-- nv-translation-notice:end -->

<a id="provenance-changes-and-licensing"></a>
# Härkomst, ändringar och licensiering

Denna granskning beskriver de kandidater som förbereddes **2026-09-18**. Applikationskällor förblir privata; de offentliga inventeringarna innehåller filnamn och hash, inte källkod. Se [fullständiga komponentmeddelanden](../THIRD_PARTY_NOTICES.md).

<a id="nvidia-profile-inspector--nv-tools-fork"></a>
## NVIDIA Profile Inspector – NV Tools Fork

Referens: Orbmu2k/nvidiaProfileInspector commit `592d962cca8827efe8859461a84267755595064a`; kandidat körbar version 3.0.2.3. Referensen commit och fork:s monteringsversion är olika identifierare; ingen uppströmsversion härleds från fork-versionen.

Den rena följeslagarens 157 käll-/resursfiler jämfördes med den commit: 2 byte-identiska, 134 skiljer sig endast i radslut eller UTF-8 BOM, 11 modifierade, 10 frånvarande vid den jämförda uppströmsvägen. "Added" är relativt till den sökvägen och är inte i sig bevis på originalförfattarskap.

[Komplett fil/hash-jämförelse](../../../provenance/nvpi-source-provenance.json).

| Område | Ärvt arbete | Fork bidrag |
| --- | --- | --- |
| Profilredaktör | Profilmodell, import/export, applikationsassociationer och referensdata | Integration med Screen och den externa verktygsstartaren |
| NVAPI | Orbmu2k:s DRS-interop | Färg/skärmrelaterad interop, produktionsbegränsningar för inbyggd laddning och skenborttagning |
| Displaytjänster | Windows/NVIDIA API:er som externa gränssnitt | DisplayInfoService, DisplayConfigurationService, DisplaySettingsBackend |
| UI | Uppströms WPF resurser, paletter och ikoner | Skärmdialoger, 15 sekunders bekräftelse, status/återläsning och verktygsfältslayout |
| Launcher | Befintligt appskal | Skyddad separat installerad RasterPulse-sökning och start |
| Förpackning | MIT uppströms | Rengör fristående följeslagare, separat installatör/avinstallationsprogram, kvarhållna meddelanden |

Den offentliga källkartan inkluderar lösnings-/resursvägar för spårbarhet; dessa filer distribueras inte som källa. Utvecklingstester, mock-gränssnitt och den gamla kombinerade NVPI/RasterPulse-binären är undantagna.

<a id="nvdriverforge"></a>
## NVDriverForge

Oberoende C#/.NET 8/WPF-applikation; det användarinriktade arbetsflödet är delvis inspirerat av NVCleanstall. Ingen NVCleanstall-källa/binär identifierades i produktionsnyttolasten. Den representeras inte som en fork av den proprietära applikationen.

Ursprungligt projektarbete inkluderar komponentanalys/-val, skyddade installationsjobb, säkerhetskopiering och transaktionsåterställning, NVIDIA-katalognedladdningar, uppdateringskontroller, lokaliserade förklaringar, valfria avancerade/NVENC-arbetsflöden och installationsbootstrap.

Ärvda/anpassade komponenter: fyra NVPI-temapaletter, utökad NVAPI DRS-gränssnittsreferens och den separat valfria MIT NVPI-kompanjonen. Custom NV-förinställningens urvalsgränssnitt och godkända transaktionsintegration tillhör NVDriverForge; förinställningen är inte en officiell NVIDIA-rekommendation.

7-Zip 26.03, .NET/WPF 8.0.31 och Inno Setup förblir omodifierade externa komponenter som används under sina egna villkor. keylase NVENC-data är inte inbäddade; en exakt commit väljs och kontrolleras när användaren begär en kompatibel nedladdning. Ingen omfördelningslicens upprättades för dessa uppströmsdata.

<a id="nvmfg-unlock40"></a>
## NVMFG Unlock40

NVMFG Unlock40 utvecklades oberoende av 禅堂 Zendo (RevoluSound Team). Underhållaren använde RTX40MFG-Unlock för jämförelse och förfining. Applikationen som helhet presenteras inte som dess fork. Denna distinktion tar inte bort krediter för delade/anpassade komponenter i det aktuella inbyggda lagret.

Jämförelsereferens: dashdogy/RTX40MFG-Unlock, Michael Robles, MIT, commit `4e776d068f91b4a665425542bb005dd57cc3d891`. Det privata inbyggda motorträdet innehåller 48 jämförda filer: 35 skillnader endast för formatering, 4 modifierade filer och 9 saknas vid referenssökvägen. [Komplett jämförelse](../../../provenance/nvmfg-source-provenance.json).

Ändrade ärvda filer: `entry_detour.h`, `patcher.cpp`, `temporal_interval_trace.cpp`, `temporal_interval_trace.h`. Ytterligare sökvägar inkluderar `game_selection.*`, `ngx_bootstrap.*`, `ngx_capability.h`, `presentation_tracker.h`, `vsync_observer.*` och en bibehållen uppströmslicens.

Produktions C++-enheter: patcher, midpoint_fix, dlssg_provider_policy, entry_detour, nvidia_mfg_policy, temporal_interval_trace, ngx_bootstrap, game_selection och vsync_observer; plus entry_detour montering och MinHook buffert/krok/studsmatta/HDE64. Det ärvda ReShade-gränssnittet, äldre shim-resurser och oanvända CMake-mål är inte en del av denna produktionskompilering.

De matchande komponenterna täcker patch-/leverantörspolicy och tidsmässigt arbete; deras meddelanden om upphovsrätt och tillstånd förblir intakta. Den centrala NGX/bootstrap/ controller-koordineringen, V-Sync-hantering per spel, sessionsdiagnostik och Windows-applikationen/SDK/backup-arbetsflödet är projektarbete av 禅堂 Zendo (RevoluSound Team). Antalet ovan beskriver filer, inklusive tredjepartsfiler och oanvända filer, inte en författarandel eller kronologin för något av projektens idéer.

Hjälparen anpassar NVPI:s NvapiDrsWrapper och NativeArrayHelper till en separat sammansättning, med projektförfattad profillogik. Den gamla utvecklingsstråket är undantaget. Delade familjepaletter kommer från NVPI.

MinHook referens: `8fda4f5481fed5797dc2651cd91e238e9b3928c6`; den ärvda kompilerade delmängden har inga funktionella lokala förändringar i jämförelsen. Streamline-integrationshuvuden: 2.12; open header-licens verifierad på v2.12.0. NGX rubrikkälla: NVIDIA/DLSS commit `a291cc7d2cc642a51566f3dfd5376f635cd1b284`.

Kandidatmotor SHA-256: `C793770D329B99CD9C5C640317CE435BFE353CA2868E36CF5DCD4D5295EFAE13`.

Obligatorisk leverantör SHA-256 i engine.json: `C64928FDB7C48A57722EA8EEF2662171EDC323473ADEA66C29A206A23F1A2BED`. En rapporterad 310.9-leverantörsfamilj är inte utbytbar med denna exakta hash. Ingen leverantörs-DLL eller modell ingår.

**Utestående licensieringspunkt:** hela NVIDIA RTX SDK-licensen, version 14 mars 2024, innehåller en begränsning i avsnitt 4(d) som är relevant för att kringgå tekniska begränsningar. Revisionen fastställer inte tillstånd för denna användning. Att behålla MIT-motorlicensen, vara gratis eller observera andra mods löser inte det separata villkoret. Kandidatförberedelser är inte ett juridiskt godkännande. Det ursprungliga korta rubrikmeddelandet kompletteras med den fullständiga licensen; dess Windows-1252-text tillhandahålls också som läsbar UTF-8, med bibehållna originalbytes.

Den ursprungliga jämförelsen beräknades om för 0.2.3: samma 48 filer och klassificeringar. Sedan föregående granskning har `game_selection.cpp`, `game_selection.h` och `patcher.cpp` ändrats för observationer av aktivitet/kapacitet. Nya arbetsflöden för bibliotek, diagnostik, preferenser, uppdateringar och urval tillhör underhållsapplikationen. Komponentlicenser och den nödvändiga leverantörshashen är oförändrade.

<a id="nvrasterpulse"></a>
## NVRasterPulse

Oberoende RTSS-profilhanterare utvecklad i det NVPI-härledda arkivet. De ärvda MIT UI-resurserna/-paletterna och projektets ursprung förblir krediterade. Produktionsappen använder uttryckligen den medföljande MIT-licensen.

Projektarbete: exakt RTSS-profilparsning/skrivning och fraktionerad kodning, säkerhetskopiering, borttagning av åsidosättande, omladdningsbrygga, förutsättningsdetektering, kompakt användargränssnitt, livscykel för fack, startkontroller och lokalisering. RTSS utför faktisk begränsning.

Ingen RTSS-källa, hook-DLL, SDK eller installationsprogram medföljer. Bryggan anropar exporten i en befintlig användarvald RTSS-installation. Inget NVIDIA-drivrutinpaket, inbyggd experimentell limiter, Framepacer, MinHook, ReShade eller DLSS runtime finns i detta paket.

<a id="assets-generated-data-and-tools"></a>
## Tillgångar, genererad data och verktyg

[Tillgångskrediter](../assets/README.md) identifiera befintliga gränssnittsförhandsvisningar och NVPI inställningsväljare. De fiktiva värdena i dem är märkta. Inget spel/Nexus-tillgång, personlig profil, privat ICC, företag NVIDIA logotyp eller teckensnittsfil kopieras.

Genererade spelkompatibilitetsnamn som ärvs i NVMFG är ett detekteringshjälpmedel, inte testbevis. Genererade installationskataloger krediteras i [översättarmeddelanden](../../../../licenses/INSTALLER-TRANSLATORS.md). Genererade byggposter med absoluta sökvägar förblir privata.

Privata byggverktyg inkluderar revisionsskripten .NET SDK/MSBuild, Visual Studio C++/MASM, Windows SDK, PowerShell, Inno Setup och Python. Deras kompilatorer, rubriker, testlöpare och felsökningstillgångar distribueras inte. Statisk release CRT förblir under Microsoft:s tillämpliga verktygskedjevillkor.

<a id="scope-of-verification"></a>
## Omfattning av verifiering

Den lokala granskningen inventerade alla filer i de tre utvecklingsrötterna samtidigt som de exkluderade Git-objektdatabaser och länkade katalogmål. Aktiv källa/dokument skannades; historiska byggnader inventerades och exkluderades. Utvalda ZIP och aktuella nyttolaster skannades och hashades; .NET-paketen dekomprimerades för ytterligare inspektion. Den första granskningen körde ingen produkt, installationsprogram, spel, RTSS-process eller drivrutin.

Den senare NVPI-installationsversionen 2 fixar fristående språkval med hjälp av de delade Inno-kontrollerna och bootstrap. Ljus/mörker privata armaturer verifierade mus- och tangentbordsnavigering och alla 34 explicita språkkoder. Själva inställningsväljaren öppnades på ett privat skrivbord som aldrig visades och avbröts före installationen. Dess sju applikationsfiler och portabla ZIP är oförändrade. NVDriverForge 0.1.3 inkluderar den korrigerade medföljaren och skickar fortfarande `/LANG`.

NVDriverForge 0.1.3 färdigställdes 2026-09-10. Dess privata verifieringsrapport registrerar 366 applikationstester, 118 kompletterande kontroller, 32 inställningskontroller, 156 inhemska jämförelser och 34 fall för vidarebefordran av språk. Den skyddade komponentvalsfixen spelades upp mot ett originaldrivrutinpaket utan att ändra dess nyttolast eller installera drivrutinen. Dessa är daterade produktteamresultat, inte tester som körs om av den här dokumentationsuppdateringen eller bevis på en lyckad riktig drivrutinsinstallation.

Denna navuppdatering ändrar ingen funktionell applikationskod. Tidigare applikationsbygg-/enhets-/UI-tester förblir daterade historiska bevis. Detta är inte fullständig reverse engineering av alla binära filer från tredje part eller en garanti mot alla möjliga hemliga mönster.

Uppdatering 18 september 2026: NVDriverForge 0.1.4 lägger till beredskapskontroller, inbyggd profilsäkerhetskopiering, komponentvägledning, inställningar och kit, detaljerade resultat, lokal rapportering och programuppdateringar. NVRasterPulse 0.2 lägger till konfigurationsdiagnostik, FPS-vägledning, pausa/återuppta, ångra, `.nvrp`-profiler och favoriter/gömma, utan en ny limitermotor. Individuella guider beskriver användning och begränsningar. Statiska navkontroller är separata från applikationstesterna som registrerades i de privata rapporterna den 18 september; ingen drivrutinsinstallation, riktig profilimport eller latensmätning utfördes för denna hubb.
