<!-- nv-language-navigation:start -->
🌐 [English](../../../../NVDriverForge/README.md) | [Français](../../../../NVDriverForge/README.fr.md) · [NV Laboratory](../README.md)

<details>
<summary>🌐 Language · 34</summary>

[العربية](../../ar/NVDriverForge/README.md) · [বাংলা](../../bn/NVDriverForge/README.md) · [简体中文](../../zh/NVDriverForge/README.md) · [Čeština](../../cs/NVDriverForge/README.md) · [Dansk](../../da/NVDriverForge/README.md) · [Nederlands](../../nl/NVDriverForge/README.md) · [English](../../../../NVDriverForge/README.md) · [Filipino](../../fil/NVDriverForge/README.md) · [Suomi](../../fi/NVDriverForge/README.md) · [Français](../../../../NVDriverForge/README.fr.md) · [Deutsch](../../de/NVDriverForge/README.md) · [Ελληνικά](../../el/NVDriverForge/README.md) · [हिन्दी](../../hi/NVDriverForge/README.md) · [Magyar](../../hu/NVDriverForge/README.md) · [Bahasa Indonesia](../../id/NVDriverForge/README.md) · [Italiano](../../it/NVDriverForge/README.md) · [日本語](../../ja/NVDriverForge/README.md) · [한국어](../../ko/NVDriverForge/README.md) · [मराठी](../../mr/NVDriverForge/README.md) · [فارسی](../../fa/NVDriverForge/README.md) · [Polski](../../pl/NVDriverForge/README.md) · [Português](../../pt/NVDriverForge/README.md) · [ਪੰਜਾਬੀ](../../pa/NVDriverForge/README.md) · [Română](../../ro/NVDriverForge/README.md) · [Русский](../../ru/NVDriverForge/README.md) · [Español](../../es/NVDriverForge/README.md) · [Kiswahili](../../sw/NVDriverForge/README.md) · **Svenska** · [தமிழ்](../../ta/NVDriverForge/README.md) · [ไทย](../../th/NVDriverForge/README.md) · [Türkçe](../../tr/NVDriverForge/README.md) · [Українська](../../uk/NVDriverForge/README.md) · [اردو](../../ur/NVDriverForge/README.md) · [Tiếng Việt](../../vi/NVDriverForge/README.md)

[Translation policy](../../README.md)

</details>
<!-- nv-language-navigation:end -->

<!-- nv-translation-notice:start -->
> Maskinassisterad översättning från engelska. Tekniska namn, kommandon, URL:er och ursprungliga lagtexter bevaras. Recension av modersmål är välkommen; konsultera den engelska referensen om formuleringen är otydlig.
<!-- nv-translation-notice:end -->

<a id="nvdriverforge"></a>
# NVDriverForge

**Förbered en NVIDIA-drivrutinsinstallation med tydliga komponentval och valfria inställningar.**

[Ladda ner 0.1.4 & status](../docs/downloads.md#nvdriverforge) · [Installation](#installation) · [Krediter](#credits-and-upstream) · [Licens](../../../../NVDriverForge/LICENSE)

<a id="overview-and-purpose"></a>
## Överblick och syfte

NVDriverForge guidar dig genom ett original NVIDIA-drivrutinpaket: välj drivrutinen, inspektera dess komponenter, granska valfria justeringar och bekräfta sedan installationen. Det finns för att göra dessa val begripliga och hålla ihop installationen, privilegierad verksamhet och återställningsinformation.

Det är en oberoende utvecklad applikation som delvis är inspirerad av NVCleanstall:s arbetsflöde. Det inkluderar inte NVCleanstall eller anspråk på fullständig funktionsparitet.

<a id="features"></a>
## Funktioner

- NVIDIA Game Ready / Studio uppslag och nedladdningar; valfri snabbkorrigeringsupptäckt med manuell reserv.
- Analys av originalpaketet, hash, NVIDIA-signaturer, manifest och kompatibla INF-poster.
- Komponentval med beroenden och bevarande av okända komponenter.
- Version 0.1.4 håller utvalda valfria NVIDIA-komponenter överhoppningsbara och utesluter endast verifierade omarkerade komponenter från upptäckt. Redan aktuella eller otillämpliga valfria körtider tvingas inte längre fram som kritiska komponenter.
- Rensa sammanfattningar av installationsfel och tillgång till detaljerade loggar på alla 34 språk.
- Beredskapskontroller, explicit bekräftelse, export av drivrutiner från butik och inbyggd NVIDIA-profilsäkerhetskopiering före installation.
- Valfria avancerade inställningar, med preflight-kontroller, journaler och konfliktmedveten återställning.
- Valfri **Custom NV** förinställning med namngivna val och förklaringar, inklusive ett separat SILK-styrkeval och kompatibilitetskontroller.
- Valfri exakt-version NVENC patch-nedladdningar; source commit och målbyte kontrolleras.
- En separat, valfri installation av Profile Inspector fork från verktygsskärmen.
- Komponentguide, återanvändbara inställningar, drivrutinssatser, lokala supportrapporter och valfria programuppdateringar.
- 34 gränssnittsspråk och fyra teman.

Tillgängliga avancerade alternativ gäller MPO, DLSS-indikatorn, Ansel, NVIDIA ljudsömn, MSI, avbrottspolicy/prioritet, HDCP, start av bildskärmsbehållare och en kvalificerad äldre telemetritjänst. Var och en har sina egna förutsättningar och effekter; dessa är inte universella prestandaförbättringar.

<a id="compatibility"></a>
## Kompatibilitet

| Krav | Detaljer |
| --- | --- |
| System | Windows 10 build 19041 eller nyare / Windows 11, x64 |
| GPU/drivrutin | Kompatibelt NVIDIA-paket och upptäckt hårdvara; automatisk katalogsökning täcker i första hand kända GeForce-modeller |
| Körtid | .NET 8 / WPF 8.0.31 ingår i det förberedda fristående paketet |
| Privilegier | Normal UI/per-användare inställning; drivrutinsinstallation och systemändringar begär administratörsåtkomst |
| Nätverk | Krävs för onlinesökning/nedladdningar av NVIDIA och explicita uppströmsförfrågningar av NVENC; en lokal originaldrivrutin kan väljas |
| Inkluderade verktyg | Omodifierad 7-Zip 26.03, körtidsmeddelanden, valfri MIT Profile Inspector-kompanjon |
| Valfri följeslagare | .NET Framework 4.8 för den separata Profile Inspector fork |

Ingen godtycklig minimiversion av drivrutinen täcker alla funktioner. Multi-GPU-sökning måste matcha alla detekterade GPU. Modeller som inte stöds/professionella kan kräva manuellt val av förare. NVIDIA:s installationsprogram förblir den sista maskinvaru-/OS-auktoriteten.

<a id="installation"></a>
## Installation

1. Besök [nedladdningar](../docs/downloads.md#nvdriverforge) och bekräfta att releasen har publicerats.
2. Välj `NVDriverForge-Setup.exe` för installation eller `NVDriverForge.exe` för bärbar användning.
3. Jämför SHA-256 med versionens `SHA256SUMS.txt`.
4. Kör installationsprogrammet för en installation per användare och ett standardavinstallationsprogram, eller placera den bärbara EXE-filen i en skrivbar mapp och öppna den.

Den bärbara enheten inkluderar dess körtid och dess valfria installationsprogram. Att installera NVDriverForge installerar inte en GPU-drivrutin. Dess EXE är för närvarande osignerade.

<a id="usage"></a>
## Användning

1. **Drivrutin:** ladda ner från NVIDIA eller välj en original NVIDIA-installations-EXE. Låt analysen avslutas.
2. **Komponenter:** granska beskrivningar och nödvändiga beroenden. Okända komponenter finns kvar.
3. **Tweaks:** lämna oönskade alternativ oförändrade. Läs effekter och avvägningar innan du väljer något.
4. **Granska:** kontrollera den exakta drivrutinen, komponenterna och valfria funktioner och bekräfta sedan installationen.
5. Acceptera endast UAC för den åtgärd du valt. Spara det skyddade jobbets återställningsinstruktioner.
6. Om den nya föraren behöver en omstart, följ det rapporterade tillståndet. Uppskjutna operationer kräver explicit återupptagande efter den omstarten.

Custom NV startar oförändrad. Välj individuella namngivna värden eller granska den medföljande förinställningen och dess undantag. Dess två interna informationsfält är inte skrivna oberoende av varandra. Inställningarna tillämpas endast i det verifierade arbetsflödet för nya drivrutiner, aldrig genom att öppna en förhandsgranskning. Du behöver inte installera den separata NVPI-redigeraren.

Valfritt NVENC-arbete laddar ner kompatibla data från en fästad keylase-commit. Det ändrar två drivrutins-DLL:er och ogiltigförklarar deras signaturer; det kan vägras av Windows, kodare, DRM eller anti-cheat. Inga sådana data eller NVIDIA DLL är inbäddad i NVDriverForge. [Ursprungs- och licensgränser](../docs/provenance.md).

Inställningar styr språk, tema och valfria uppdateringskontroller för installerade användare. Den bärbara enheten skapar inte den installerade bakgrundskontrolluppgiften. Verktyg och återställning är separata från de fyra installationsstegen.

<a id="backup-and-diagnostic-tools"></a>
## Verktyg för säkerhetskopiering och diagnostik

**Före installation:** beredskapskontroller täcker paketsignaturen, GPU:er, beräknad arbetsyta/backuputrymme, väntande omstart och konkurrerande installatörer. Den upphöjda arbetaren upprepar dem. Konkurrerande processer stoppas aldrig automatiskt. Säkerhetskopieringen av den inbyggda NVIDIA-profildatabasen måste lyckas innan installationen av NVIDIA startar; driver-store export är en separat säkerhetskopia.

**Återanvändbara val:** komponentguiden ställer fyra frågor om spel, ljud, NVIDIA App och inspelning. Granska dess förslag; obligatoriska, okända och beroendekomponenter förblir skyddade. Exportera inställningar, förhandsgranska och validera dem sedan mot det valda paketet vid import. Samtycken, omstartsoperationer, programsökvägar och patchnyttolaster importeras inte.

**Drivrutinskit:** exportera en `.nvdfkit.zip` för att hålla det originalsignerade NVIDIA-installationsprogrammet, val, hash och instruktioner tillsammans. Bär `NVDriverForge.exe` separat. Importera satsen i Verktyg, granska förhandsgranskningen och använd sedan det normala installationsarbetsflödet. Detta är inte en slimmad drivrutin eller modifierad fristående installationsprogram. Valfri NVENC behöver fortfarande en nedladdning och samtycke för just den drivrutinen. NVIDIA:s omdistributionsvillkor gäller fortfarande.

**Resultat och support:** läs det korta resultatet och utöka detaljerna per steg/per alternativ. Lyckad återläsning etablerar ett lagrat värde, inte en uppmätt förbättring. Den lokala JSON-supportrapporten använder tillåtna fält, inklusive det senast sparade jobbet efter omstart av appen. Förhandsgranska det innan du sparar eller delar. Den innehåller inga råloggar, profilinnehåll eller maskinvaruidentifierare och laddas aldrig upp automatiskt.

**Återställning:** följ det skyddade jobbets guide för att återställa den säkerhetskopierade drivrutinen. Explicit profilåterställning kräver den ursprungliga drivrutinsversionen och samma GPU:er; den ersätter hela databasen, bevarar en aktuell kopia och kontrollerar hash och konflikttillstånd. Radera inte dess journal eller framtvinga en oöverensstämmelse. Verklig drivrutinsinstallation, fullständig återställning och inbyggd profilimport med detta nya arbetsflöde förblir ovaliderade på ett riktigt system.

**Appuppdateringar:** läs versionskommentarerna och välj sedan uttryckligen en SHA-256-verifierad nedladdning. Kontrollen är manuell som standard, med en valfri kontroll vid start. Inget installationsprogram startas automatiskt. Den här funktionen är separat från kontroller av drivrutinsuppdateringar och den installerade utgåvans valfria drivrutinskontrolluppgift.

<a id="screenshots"></a>
## Skärmdumpar

![NVDriverForge förhandsgranskning av drivrutinssidan](../../../../assets/screenshots/nvdriverforge-0.1.2-preview.png)

Befintlig 0.1.2 fransk UI-rendering med exempeldata; behålls som en förhandsvisning av gränssnittet. Den visade 699.99-drivrutinen är en testfixtur, inte en riktig version att ladda ner. [Bildens ursprung](../assets/README.md).

<a id="update-and-uninstall"></a>
## Uppdatera och avinstallera

Stäng NVDriverForge, skaffa nästa officiella paket och verifiera dess hash. Använd samma installationsidentitet för en installerad uppdatering; ersätt en stängd bärbar EXE med den nya. Behåll inställningar och skyddade jobb.

Uninstall från Windows **Installed apps**. Den tar bort appen och dess uppdateringsuppgift, inte NVIDIA-drivrutinen. Inställningar, loggar och säkerhetskopior finns kvar. Om så önskas kan du återställa avancerade/NVENC-ändringar genom det dokumenterade återställningsflödet **innan** du tar bort appen. Återställ nekar motstridiga ändringar från ett annat verktyg.

Lokal data är under `%LOCALAPPDATA%\NVDriverForge`; skyddade jobb och förareexport är under `%PROGRAMDATA%\NVDriverForge\Jobs`. Bärbar användning skapar också lokal data. Export från drivrutinsbutik och den inbyggda profilbackupen är separata. Inte heller en systembild.

<a id="known-limitations"></a>
## Kända begränsningar

- Inga hårdvarutillägg/INF-redigering, regenererade NVIDIA-signaturer, anti-fuskkompatibel avsägning eller automatisk osignerad varningsacceptans.
- Ingen fullständig borttagning av telemetri/reklam, export av slimmade paket eller automatisk fullständig återställning till föregående drivrutin.
- Drivrutinsinstallation, startåterställning och valfria profilskrivningar har inte validerats helt på riktiga maskiner av hubbrevisionen.
- Återläsning av registret är inte bevis på faktiska HDCP, prestanda eller latenseffekter.
- Signaturkontroller använder lokalt tillgängligt Windows-förtroende; återkallelse online utförs inte.
- Det finns 34 språk, men fullständiga tester av modersmål/tillgänglighet är fortfarande ofullständiga.

<a id="troubleshooting"></a>
## Felsökning

| Symptom | Åtgärd |
| --- | --- |
| Onlinekatalog ej tillgänglig | Välj ett originalpaket från [NVIDIA drivrutinsnedladdningar](https://www.nvidia.com/en-us/drivers/). Byt inte ut en intilliggande GPU-modell. |
| Snabbkorrigeringssökning är inte tillgänglig | Använd [NVIDIA:s Game Ready drivrutinsforum](https://www.nvidia.com/en-us/geforce/forums/game-ready-drivers/13/) och verifiera det faktiska paketet. |
| Installationen av NVIDIA misslyckas | Läs felsammanfattningen och öppna de detaljerade loggarna. Tillvalskomponenter som redan är aktuella eller otillämpliga förblir överhoppningsbara i 0.1.4. Misslyckade installationer utlöser inte valfria justeringar eller ett framgångsrikt/omstartsflöde. |
| Signatur/hash/säkerhetskopieringsfel | Stoppa den installationen och behåll felet; skaffa originalförpackningen igen om den är skadad. |
| Alternativet är inte tillgängligt | Läs orsaken till dess hårdvara, komponent eller måldrivrutin; hålla det oförändrat. |
| Omstart eller jobb väntar fortfarande | Använd jobbets återställningsinstruktioner och uttryckliga CV; radera inte dess journal. |
| Återställ konflikt | Ett annat tillstånd skiljer sig från den registrerade transaktionen. Bevara den och begär hjälp istället för att tvinga fram en återställning. |

För rapporter, inkludera den valda verktygsversionen, Windows, GPU, drivrutin och reproducerbara steg; redigera sökvägar och personuppgifter från loggar. [Support](../docs/support.md).

<a id="faq"></a>
## FAQ

**Installerar installationsprogrammet en grafikdrivrutin?** Nej. Det kräver applikationens separata analys, granskning, bekräftelse och förhöjd installationsprocess.

**Behöver jag NVCleanstall eller NVPI?** Nej. NVCleanstall är endast inspiration. Profile Inspector-kompanjonen är en oberoende valfri redigerare.

**Gör det varje NVIDIA-drivrutin mindre eller snabbare?** Nej. Utvalda komponenter och förutsättningar avgör vad som kan förändras; ingen uppmätt vinst utlovas.

**Var finns källorna?** Applikationsspecifika källor och privata tester underhålls separat. Det här navet tillhandahåller dokumentation, binärfiler och tredjepartslänkar som krävs för attribution/licensiering.

<a id="credits-and-upstream"></a>
## Krediter och uppströms

Ursprunglig applikation, arbetsflöde, transaktioner, lokalisering, bootstrap och anpassningar: 禅堂 Zendo (RevoluSound Team).

- [NVCleanstall / TechPowerUp](https://www.techpowerup.com/download/techpowerup-nvcleanstall/): arbetsflödesinspiration; ingen källa eller binär importerad.
- [NVIDIA Profile Inspector / Orbmu2k](https://github.com/Orbmu2k/nvidiaProfileInspector): MIT-teman, utökad NVAPI-gränssnittsreferens och separat förpackad fork.
- [7-Zip / Igor Pavlov](https://www.7-zip.org/): omodifierade extraktionsverktyg.
- [Microsoft .NET](https://github.com/dotnet/runtime) och [WPF](https://github.com/dotnet/wpf): medföljande körtid.
- [Inno Setup](https://jrsoftware.org/isinfo.php): originalinstallationsmotor och krediterade översättningar.
- [keylase/nvidia-patch](https://github.com/keylase/nvidia-patch): extern valfri NVENC-datakälla; omfördelningslicens inte upprättad.
- [NVIDIA](https://www.nvidia.com/en-us/drivers/): externa drivrutiner hämtar och installerade NVAPI/NVML-bibliotek.

[Fullständig komponenttabell](../THIRD_PARTY_NOTICES.md) · [Förändringar och härkomst](../docs/provenance.md)

<a id="license"></a>
## Licens

[Befintlig binär distributionsbehörighet](../../../../NVDriverForge/LICENSE) tillåter användning och delning av oförändrade officiella körbara filer med deras meddelanden. Applikationsspecifika källrättigheter förbehålls. Det begränsar inte rättigheter som beviljas av separata tredjepartslicenser. [Fullständiga meddelanden](LICENSES/README.md).

Oberoende av NVIDIA Corporation, TechPowerUp och keylase; inte sponsras eller officiellt godkänts av dem. Produktnamn förblir sina ägares varumärken.
