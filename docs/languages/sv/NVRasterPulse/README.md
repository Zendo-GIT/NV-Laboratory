<!-- nv-language-navigation:start -->
🌐 [English](../../../../NVRasterPulse/README.md) | [Français](../../../../NVRasterPulse/README.fr.md) · [NV Laboratory](../README.md)

<details>
<summary>🌐 Language · 34</summary>

[العربية](../../ar/NVRasterPulse/README.md) · [বাংলা](../../bn/NVRasterPulse/README.md) · [简体中文](../../zh/NVRasterPulse/README.md) · [Čeština](../../cs/NVRasterPulse/README.md) · [Dansk](../../da/NVRasterPulse/README.md) · [Nederlands](../../nl/NVRasterPulse/README.md) · [English](../../../../NVRasterPulse/README.md) · [Filipino](../../fil/NVRasterPulse/README.md) · [Suomi](../../fi/NVRasterPulse/README.md) · [Français](../../../../NVRasterPulse/README.fr.md) · [Deutsch](../../de/NVRasterPulse/README.md) · [Ελληνικά](../../el/NVRasterPulse/README.md) · [हिन्दी](../../hi/NVRasterPulse/README.md) · [Magyar](../../hu/NVRasterPulse/README.md) · [Bahasa Indonesia](../../id/NVRasterPulse/README.md) · [Italiano](../../it/NVRasterPulse/README.md) · [日本語](../../ja/NVRasterPulse/README.md) · [한국어](../../ko/NVRasterPulse/README.md) · [मराठी](../../mr/NVRasterPulse/README.md) · [فارسی](../../fa/NVRasterPulse/README.md) · [Polski](../../pl/NVRasterPulse/README.md) · [Português](../../pt/NVRasterPulse/README.md) · [ਪੰਜਾਬੀ](../../pa/NVRasterPulse/README.md) · [Română](../../ro/NVRasterPulse/README.md) · [Русский](../../ru/NVRasterPulse/README.md) · [Español](../../es/NVRasterPulse/README.md) · [Kiswahili](../../sw/NVRasterPulse/README.md) · **Svenska** · [தமிழ்](../../ta/NVRasterPulse/README.md) · [ไทย](../../th/NVRasterPulse/README.md) · [Türkçe](../../tr/NVRasterPulse/README.md) · [Українська](../../uk/NVRasterPulse/README.md) · [اردو](../../ur/NVRasterPulse/README.md) · [Tiếng Việt](../../vi/NVRasterPulse/README.md)

[Translation policy](../../README.md)

</details>
<!-- nv-language-navigation:end -->

<!-- nv-translation-notice:start -->
> Maskinassisterad översättning från engelska. Tekniska namn, kommandon, URL:er och ursprungliga lagtexter bevaras. Recension av modersmål är välkommen; konsultera den engelska referensen om formuleringen är otydlig.
<!-- nv-translation-notice:end -->

<a id="nvrasterpulse"></a>
# NVRasterPulse

**Per-applikation FPS gränser genom RivaTuner Statistics Server.**

> **Installera RTSS först.** NVRasterPulse kräver [RivaTuner Statistics Server (RTSS), nedladdad från Guru3D](https://www.guru3d.com/download/rtss-rivatuner-statistics-server-download/). RTSS måste köras för att upprätthålla gränser. Ingen RTSS-installationsprogram, krok-DLL eller SDK medföljer.

[Ladda ner 0.2 & status](../docs/downloads.md#nvrasterpulse) · [Installation](#installation) · [Hur gränser fungerar](#usage) · [Licens](../../../../NVRasterPulse/LICENSE)

<a id="overview-and-purpose"></a>
## Överblick och syfte

NVRasterPulse är ett kompakt Windows-gränssnitt för hantering av RTSS-ramgränser efter körbart namn. RTSS utför begränsningen. NVRasterPulse hanterar motsvarande profilvärden, säkerhetskopior och omladdningsförfrågningar, med fackåtkomst och beständiga val.

Det finns för att göra exakta gränser per spel lättare att redigera utan att ersätta en hel RTSS-profil eller störa dess överlagringsinställningar. Version **0.2** lägger till konfigurationsdiagnostik, en FPS-hjälpare, paus, ångra och profildelning.

<a id="features"></a>
## Funktioner

- Välj ett program som körs eller lägg till dess körbara filer manuellt.
- Spara FPS-gränser från 1 till 1000, med upp till tre decimaler.
- Exakt rationell kodning av inmatade värden: 59.94 blir 2997/50.
- Front Edge Sync-konfiguration (`SyncLimiter=1`) med aktiv väntan (`PassiveWait=0`).
- Per-körbara profiluppdateringar, automatiska säkerhetskopieringar och atomskrivningar.
- Borttagning av begränsar åsidosätter samtidigt som annat profilinnehåll behålls.
- RTSS installationsdetektering, manuellt sökvägsval och explicit start/återladdning.
- En-instans fackdrift, valfri installerad start, 34 språk och fyra teman.
- Separera normalt avsluta och **Avsluta + RTSS** åtgärder.

<a id="compatibility"></a>
## Kompatibilitet

| Krav | Detaljer |
| --- | --- |
| System | Windows 10/11 x64 |
| Körtid | [.NET Framework 4.8](https://dotnet.microsoft.com/en-us/download/dotnet-framework/net48), installeras separat vid behov |
| Nödvändig programvara | RTSS med `RTSS.exe`, en matchande `Profiles`-katalog och kompatibel profil/återladdningsstöd |
| GPU | RTSS-kompatibilitet bestämmer begränsaren; denna profilhanterare kräver inte en speciell RTX-generation |
| Behörigheter | Aktuell applikation begär administratörsåtkomst; den valda RTSS-profilmappen måste vara tillgänglig |
| Spel | Beror på RTSS hooking support och varje spels begränsningar; ingen anti-fusk garanti |

Ingen specifik RTSS minimiversion har certifierats för varje funktion av denna hubbrevision. Använd den officiella aktuella distributionen och rapportera den exakta versionen om en profilnyckel/reload inte fungerar. Installerad-men-stoppad RTSS klarar installationskontrollen; den måste sedan startas för faktisk begränsning.

<a id="installation"></a>
## Installation

1. **[Ladda ner och installera RTSS från Guru3D](https://www.guru3d.com/download/rtss-rivatuner-statistics-server-download/).**
2. Öppna [NVRasterPulse nedladdningar](../docs/downloads.md#nvrasterpulse) och kontrollera Release tillgänglighet.
3. Ladda ner `NVRasterPulse-0.2-win-x64-Setup.exe` eller `NVRasterPulse-0.2-win-x64-portable.zip`, plus meddelanden/kontrollsummor.
4. Jämför SHA-256. Kör installationsprogrammet eller extrahera hela den bärbara ZIP-filen till en skrivbar lokal mapp.
5. Öppna `NVRasterPulse.exe`. Om RTSS saknas, använd **Ladda ner RTSS**, installera den och **Kontrollera igen**, eller välj `RTSS.exe` manuellt.
6. Starta RTSS med dess vanliga genväg eller NVRasterPulse:s RTSS-knapp om den är stoppad.

Att stänga av den valfria påminnelsen hoppar inte över förutsättningskontrollen. En tyst start av Windows-facket väntar tills huvudfönstret öppnas innan denna kontroll visas. Installationen installerar endast NVRasterPulse. Dess EXE är osignerade.

<a id="usage"></a>
## Användning

1. Välj det avsedda programmet som körs eller bläddra till dess spel-EXE.
2. Ange en gräns mellan 1 och 1000 FPS, inklusive ett bråktal vid behov.
3. Spara och kontrollera det rapporterade resultatet. NVRasterPulse uppdaterar den körbara filens RTSS-profil och begär en omladdning.
4. Bekräfta att RTSS körs och verifiera beteendet i det avsedda spelet.

Profiler kodas av **körbart namn**, såsom `Game.exe.cfg`. Två olika mappar som innehåller `Game.exe` delar samma RTSS-profil; Att lagra hela banan tar inte bort denna kollision.

Spara använder Front Edge Sync och aktiv väntan. Aktiv väntan kan öka användningen av CPU. De alternativa `LimitTime`-fälten är neutraliserade. Befintliga kommentarer, överlagringsinställningar och `EnableHooking=0` bevaras. RTSS Global-profilen har inte ändrats.

Använd papperskorgen för att ta bort NVRasterPulse:s limiter-överstyrningar. Det tar inte bort hela RTSS-profilen. En gräns som ärvts från RTSS Global eller ett annat verktyg kan fortfarande gälla efteråt.

**Stänga och avsluta:** huvudfönstret kan gömma sig till facket. Normal **Avsluta** lämnar RTSS igång och sparade gränser intakta. **Avsluta + RTSS** begär en normal stängning av den matchande RTSS-processen i den aktuella sessionen, väntar upp till åtta sekunder och tvångsdödar den inte. Lagrade gränser kvarstår i båda fallen.

Språk och tema väljs i appen. Inloggning vid Windows är valfri och avsedd för en installerad kopia. Informationsknappen förklarar vanliga åtgärder.

<a id="diagnostics-and-profile-tools"></a>
## Diagnostik och profilverktyg

Öppna åtgärdsmenyn för ytterligare verktyg. De bevarar RTSS Global, överlagringsinställningar och undantag.

**Diagnostik:** inspektera lokala/effektiva gränser, stoppade RTSS, en saknad körbar fil, inget upptäckt fönster, inaktiverad hooking, arv, pausade gränser, konkurrerande inställningar och dubbletter av körbara namn. Denna skrivskyddade kontroll beskriver konfigurationen; det bevisar inte att ett spel är anslutet av RTSS eller mäter dess FPS.

**FPS-hjälpare:** välj displayen och deklarera VRR/G-Sync, V-Sync, Reflex och Frame Generation själv. Avrundad uppdateringsfrekvens kommer från Windows. Om Reflex eller Frame Generation är aktiv eller okänd, erbjuds inget automatiskt tak. För VRR med V-Sync på och Reflex/FG av, subtraherar heuristiken minst 3 FPS eller ungefär 2 % av uppdateringsfrekvensen. Detta är inte ett uppmätt optimum. Att tillämpa förslaget fyller utkastet; **Spara** förblir en separat åtgärd.

**Pausa och återuppta:** stoppa det valda programmets lock och återställ sedan dess tidigare begränsarfält. Motstridiga ändringar av ett annat verktyg förhindrar ett tvetydigt CV. Att dölja en post pausar inte dess tak.

**Ångra:** återställ den senaste ändringen av de sex hanterade begränsarfälten för det programmet. Det finns en nivå; detta återställer inte hela RTSS. Motstridiga yttre förändringar vägras. Säkerhetskopieringar av filer förblir separata.

**Dela profiler:** exportera valda profiler till en `.nvrp`-fil. Import visar en förhandsgranskning och lämnar befintliga tak omarkerade som standard. Filen innehåller endast körbara namn, gränser och tillstånd, utan absoluta sökvägar eller skript. Granska ditt val och ansök. Ett I/O-fel kan lämna vissa profiler redan tillämpade; resultatet identifierar dem och var och en behåller sin ångra. Identiska körbara namn adresserar fortfarande samma RTSS-profil.

**Favoriter och dolda poster:** fäst användbara program först, dölj oönskade poster och återställ dem i den dedikerade dialogrutan. Dessa val kvarstår. En stängd favorit visas inte som en applikation som körs.

<a id="screenshots"></a>
## Skärmdumpar

![NVRasterPulse förhandsvisning i huvudfönstret](../../../../assets/screenshots/nvrasterpulse-0.1-preview.png)

Befintlig fransk 0.1 UI-rendering med exempel på körbara namn och ett 176 FPS värde. RTSS visas stoppad; detta är en gränssnittsillustration, inte en löpande limiter eller latensmätning. [Bildens ursprung](../assets/README.md).

<a id="update-and-uninstall"></a>
## Uppdatera och avinstallera

Avsluta NVRasterPulse, ladda ner och verifiera den nya versionen, kör sedan dess installation eller extrahera den bärbara datorn till en ny mapp. Bevara inställningar och RTSS-säkerhetskopior. RTSS-uppdateringar är separata och kommer från Guru3D.

För att ta bort en installerad kopia, använd Windows **Installed apps**. För bärbar, avsluta och ta bort den extraherade mappen när dina säkerhetskopior är säkra. Sparade RTSS-gränser tas inte bort genom att avinstallera NVRasterPulse: ta bort de avsedda begränsaröverstyrningarna först. RTSS har ett eget avinstallationsprogram.

Lokal stat: `%LOCALAPPDATA%\NVRasterPulse`. Automatiska RTSS-säkerhetskopior: `%LOCALAPPDATA%\NVRasterPulse\Backups\RTSS`. En äldre `%LOCALAPPDATA%\RTSSProfileBridge`-plats kan läsas för migrering. Dessa filer kan innehålla personliga körbara sökvägar och bör inte publiceras offentligt.

<a id="known-limitations"></a>
## Kända begränsningar

- RTSS utför locket. Ett sparat värde eller en lyckad omladdningsbegäran är inte ett uppmätt resultat för bildruta.
- Körbara filer med samma namn delar en profil.
- En annan global/per-spel-begränsare kan påverka resultatet; inaktivering av den lokala åsidosättningen tar inte bort ett ärvt lock.
- En avsiktligt inaktiverad RTSS-krok förblir inaktiverad.
- Aktiv väntan har en CPU/strömavvägning.
- Inget universellt spel, anti-cheat eller end-to-end latensvalidering.
- Den tidigare experimentella oberoende limitermotorn kompileras eller skickas inte.
- Automatiska säkerhetskopieringar innebär inte ett fullständigt säkerhetskopierings-återställningsgränssnitt med ett klick.

<a id="troubleshooting"></a>
## Felsökning

| Symptom | Åtgärd |
| --- | --- |
| RTSS-förutsättningen förblir öppen | Välj den faktiska `RTSS.exe` och den matchande mappen Profiler och kontrollera sedan igen. |
| Gränsen sparad men ingen effekt | Starta RTSS; verifiera rätt spel EXE/profil, krokbehörigheter och andra begränsare. |
| Spara misslyckas | Kontrollera mappbehörigheter och bevara det visade felet/säkerhetskopian. |
| Gränsen kvarstår efter borttagning | Inspektera RTSS Global och andra verktyg; trash-åtgärden tar bara bort lokala limiter-åsidosättningar. |
| Två spel får samma gräns | Kontrollera om deras körbara filnamn är identiska. |
| Avsluta + RTSS lämnar RTSS öppen | Stäng RTSS normalt själv; detta kommando undviker medvetet påtvingad uppsägning. |

Om du manuellt återställer en RTSS-säkerhetskopia, stäng RTSS först och bevara den aktuella profilen innan du ersätter den med den avsedda säkerhetskopian. Detta kan skriva över orelaterade profilredigeringar; inspektera filen och datumet. [Delad support](../docs/support.md).

<a id="faq"></a>
## FAQ

**Behöver jag MSI Afterburner också?** NVRasterPulse kräver RTSS; det beror inte på Afterburner-applikationen. Följ RTSS-distributörens installationsalternativ.

**Kan jag använda detta utan att RTSS körs?** Du kan hantera profiler när en installation upptäcks, men RTSS måste köras för att begränsa.

**Ta bort locken när du avslutar eller avinstallerar?** Nej. Ta bort de önskade begränsarförbidragen uttryckligen innan du tar bort NVRasterPulse.

**Är det en fork av RTSS?** Nej. Det är en oberoende profilhanterare; ingen RTSS-källa eller körbar är inbyggd.

<a id="upstream-modifications-and-credits"></a>
## Uppströms, ändringar och krediter

Utvecklingsförrådet kommer från [Orbmu2k's NVIDIA Profile Inspector](https://github.com/Orbmu2k/nvidiaProfileInspector). Dess MIT-paletter/UI-resurser krediteras. Profilhanteringstjänsterna, bråkkodning, säkerhetskopior, RTSS omladdningsbrygga, brickbeteende, förutsättningsguide, språk och applikationsspecifik ikon utvecklades/anpassades av 禅堂 Zendo (RevoluSound Team).

RTSS är utvecklad av **Unwinder** och distribueras separat via Guru3D. NVRasterPulse anropar `UpdateProfiles` från den valda installerade hook-DLL-filen; ingen RTSS SDK eller krokbinär omdistribueras. Installationsprogrammet använder omodifierad Inno Setup 7.1.0 med anpassade skript/översättningar och en projektbootstrap.

[Fullständig härkomst](../docs/provenance.md) · [Tredjepartsbord](../THIRD_PARTY_NOTICES.md)

<a id="license"></a>
## Licens

Paketet distribuerar uttryckligen NVRasterPulse under den medföljande [MIT-licens](../../../../NVRasterPulse/LICENSE), med upphovsrätt (c) 2016 Orbmu2k. Applikationskällan underhålls privat; MIT kräver inte publicering av modifierad källa. RTSS och Windows/.NET förblir under sina egna villkor. [Fullständiga meddelanden](LICENSES/README.md).

Oberoende av NVIDIA Corporation, MSI och RTSS; inte sponsras eller officiellt godkänts av dem. Produktnamn förblir sina ägares varumärken.
