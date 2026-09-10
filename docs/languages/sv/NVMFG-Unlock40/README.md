<!-- nv-language-navigation:start -->
🌐 [English](../../../../NVMFG-Unlock40/README.md) | [Français](../../../../NVMFG-Unlock40/README.fr.md) · [NV Laboratory](../README.md)

<details>
<summary>🌐 Language · 34</summary>

[العربية](../../ar/NVMFG-Unlock40/README.md) · [বাংলা](../../bn/NVMFG-Unlock40/README.md) · [简体中文](../../zh/NVMFG-Unlock40/README.md) · [Čeština](../../cs/NVMFG-Unlock40/README.md) · [Dansk](../../da/NVMFG-Unlock40/README.md) · [Nederlands](../../nl/NVMFG-Unlock40/README.md) · [English](../../../../NVMFG-Unlock40/README.md) · [Filipino](../../fil/NVMFG-Unlock40/README.md) · [Suomi](../../fi/NVMFG-Unlock40/README.md) · [Français](../../../../NVMFG-Unlock40/README.fr.md) · [Deutsch](../../de/NVMFG-Unlock40/README.md) · [Ελληνικά](../../el/NVMFG-Unlock40/README.md) · [हिन्दी](../../hi/NVMFG-Unlock40/README.md) · [Magyar](../../hu/NVMFG-Unlock40/README.md) · [Bahasa Indonesia](../../id/NVMFG-Unlock40/README.md) · [Italiano](../../it/NVMFG-Unlock40/README.md) · [日本語](../../ja/NVMFG-Unlock40/README.md) · [한국어](../../ko/NVMFG-Unlock40/README.md) · [मराठी](../../mr/NVMFG-Unlock40/README.md) · [فارسی](../../fa/NVMFG-Unlock40/README.md) · [Polski](../../pl/NVMFG-Unlock40/README.md) · [Português](../../pt/NVMFG-Unlock40/README.md) · [ਪੰਜਾਬੀ](../../pa/NVMFG-Unlock40/README.md) · [Română](../../ro/NVMFG-Unlock40/README.md) · [Русский](../../ru/NVMFG-Unlock40/README.md) · [Español](../../es/NVMFG-Unlock40/README.md) · [Kiswahili](../../sw/NVMFG-Unlock40/README.md) · **Svenska** · [தமிழ்](../../ta/NVMFG-Unlock40/README.md) · [ไทย](../../th/NVMFG-Unlock40/README.md) · [Türkçe](../../tr/NVMFG-Unlock40/README.md) · [Українська](../../uk/NVMFG-Unlock40/README.md) · [اردو](../../ur/NVMFG-Unlock40/README.md) · [Tiếng Việt](../../vi/NVMFG-Unlock40/README.md)

[Translation policy](../../README.md)

</details>
<!-- nv-language-navigation:end -->

<!-- nv-translation-notice:start -->
> Maskinassisterad översättning från engelska. Tekniska namn, kommandon, URL:er och ursprungliga lagtexter bevaras. Recension av modersmål är välkommen; konsultera den engelska referensen om formuleringen är otydlig.
<!-- nv-translation-notice:end -->

<a id="nvmfg-unlock40"></a>
# NVMFG Unlock40

**Experimentell NVIDIA Multi Frame Generation för GeForce RTX 40, med en central styrenhet och val per spel.**

[Ladda ner 0.1.1 & status](../docs/downloads.md#nvmfg-unlock40) · [Installation](#installation) · [Uppströms](#upstream-and-modifications) · [Licenser](LICENSES/README.md)

<a id="overview-and-purpose"></a>
## Överblick och syfte

NVMFG Unlock40 är en oberoende utvecklad applikation av 禅堂 Zendo (RevoluSound Team). Den kombinerar en Windows-kontroller, ett inbyggt lager, en profilhjälp och spel/Streamline SDK-hantering. Den riktar sig till spel som redan integrerar NVIDIA DLSS Frame Generation och kompatibla NVIDIA-körtider.

[RTX40MFG-Unlock](https://github.com/dashdogy/RTX40MFG-Unlock) konsulterades för att jämföra och förfina arbetet. Det aktuella inbyggda lagret innehåller delade och anpassade komponenter, som krediteras individuellt nedan. Denna referens gör inte hela NVMFG-applikationen till en fork för det projektet.

Det finns för att koordinera experimentellt MFG-beteende centralt, komma ihåg spelspecifika val och hålla runtime-uppdateringar och säkerhetskopior synliga. Den lägger inte till DLSS Frame Generation till varje spel eller konverterar en godtycklig FSR-implementering.

Den förberedda kandidaten är **0.1.1**, inklusive SDK-listans visuella korrigering internt registrerad som UI2. Den offentliga versionen förblir 0.1.1; dess exakta hash skiljer denna kandidat från äldre lokala byggen.

<a id="features"></a>
## Funktioner

- Central aktivera/avaktivera kontroll och valfri Windows-fackstart.
- Val per spel mellan Dynamic MFG, spelets inställning och stödda fasta multiplikatorer.
- Separat ihågkomna val för observerade V-Sync på/av-tillstånd.
- Dynamic använder NVIDIAs läge; den är avstängd när V-Sync är avstängd, med ett separat in-game/fast val.
- Spelmenyvägledning och ihållande uteslutningar; spel utan DLSS FG behåller kontrollen.
- Spelupptäckt, val av förälder-mapp, sökning, gruppering och borttagning utan att radera spelfiler.
- Streamline SDK nedladdning/import, verifierad lokal cache, explicit val, säkerhetskopiering och återställning per spel.
- Inbyggd leverantörsverifiering, diagnostik per session, global profiljournal och konfliktmedveten återställning.
- 34 gränssnittsspråk och fyra teman.

Att stänga av FG i spelet håller det avstängt. Fasta val från 2x till 6x beror på spelet/menyn/körningstid; de är inte ett löfte om att varje kombination fungerar. Styrenheten observerar V-Sync och ställer inte in V-Sync eller VRR för användaren.

<a id="compatibility"></a>
## Kompatibilitet

| Krav | Detaljer |
| --- | --- |
| System | Windows 10/11 x64 |
| GPU | GeForce RTX 40 mål; inga universella GPU-kompatibilitetsanspråk |
| Spel | Befintlig NVIDIA DLSS Frame Generation-integration och stödd körtid; ingen anti-fusk-kompatibilitetscertifiering |
| Leverantör | Kandidaten är fäst vid leverantören SHA-256 dokumenterad i [härkomst](../docs/provenance.md); okända hash nekas |
| Körtid | Medföljande .NET 8/WPF 8.0.30 för app/agent; .NET Framework 4.8 för profilhjälpare |
| Behörigheter | Administratörsåtkomst för kontroller/profiloperationer |
| Nätverk | Krävs för utvalda officiella SDK-nedladdningar; importerade kompatibla SDKs kan cachelagras lokalt |
| Externa binärer | NVIDIA-drivrutin, NGX-leverantör/modeller och Streamline-spelkörningstider är inte paketerade |

Enbart en versionsetikett är otillräcklig: drivrutin, leverantörshash, spelintegration och faktiskt laddade moduler spelar roll. Skyddade eller inkompatibla processer kan vägra bifogning. Applikationen är inte utformad för att undvika skydd mot fusk.

<a id="installation"></a>
## Installation

1. Läs [kandidatstatus och licensanteckning](../docs/downloads.md#nvmfg-unlock40).
2. Ladda ner `NVMFGUnlock40-0.1.1-Setup-x64.exe` eller `NVMFGUnlock40-0.1.1-Portable-x64.zip` när dess release är tillgänglig.
3. Kontrollera SHA-256 och spara de medföljande meddelandena. Installera .NET Framework 4.8 om Windows inte redan tillhandahåller det.
4. Kör installationsprogrammet eller extrahera **hela** portabla ZIP till en skrivbar lokal mapp.
5. Starta `NVMFGUnlock40.exe`; behåll `agent`, `driver`, `engine` och `Licenses` i den medföljande layouten.

Mappen med namnet `driver` innehåller hjälpare för användarutrymme, inte en kärndrivrutin. Kopiera inte bara huvud-EXE eller byt ut leverantörens hash för att tvinga fram kompatibilitet. De nuvarande EXE:erna är osignerade.

<a id="usage"></a>
## Användning

1. Börja med kontrollenheten inaktiverad. Lägg till ett spel eller en överordnad mapp och välj de faktiska installationerna.
2. Granska varje spels MFG-inställningar. Svara på vad dess meny erbjuder; svaret lagras per spel.
3. Välj Dynamic eller inställningen i spelet globalt och justera sedan valbara val per spel efter behov.
4. Aktivera endast styrenheten när du tänker använda den. Den kan tillfälligt ändra sex globala NVIDIA-profilinställningar, med en återställningsjournal.
5. Starta ett kvalificerat spel och aktivera dess eget DLSS Frame Generation. Följ varje begäran om valet V-Sync-off.
6. Använd undantag för spel som du inte vill hantera. Att ta bort ett spel registrerar en uteslutning och bevarar dess filer/säkerhetskopior.
7. Använd programmets fullständiga avsluta/inaktivera och återställningsflöde när du är klar.

Stängning av huvudfönstret kan lämna kontrollenheten i facket. En DLL som redan laddats in i ett spel finns kvar tills spelet avslutas; Att inaktivera styrenheten är inte en garanti för avlastning. Stäng berörda spel före underhåll eller uppdateringar.

**Streamline SDKs:** på sidan NVIDIA SDK, ladda ner en officiell version eller importera en kompatibel lokal SDK. Import lagrar en verifierad kopia; **Use this version** markerar den och **Uninstall** tar bort den cachade kopian. Saknade Streamline DLL:er kan kompletteras från en officiell NVIDIA SDK, med källan visad. Detta laddar inte ner/ersätter inte en NGX-modell. Stäng spelet, välj den avsedda speluppdateringen och behåll den ursprungliga säkerhetskopian. För att återställa spelfiler, använd dess backupåterställning, inte cachens Uninstall-knapp.

<a id="screenshots"></a>
## Skärmdumpar

![Förhandsgranskning av NVMFG SDK-listan](../../../../assets/screenshots/nvmfg-0.1.1-sdk-preview.png)

Befintligt engelska 0.1.1-gränssnitt återges med ett exempel på SDK-inventering. Det är inte en aktuell versionslista eller bevis på ett pågående spel. [Bildens ursprung](../assets/README.md).

<a id="update-and-uninstall"></a>
## Uppdatera och avinstallera

Stäng berörda spel. Inaktivera/avsluta NVMFG och åtgärda eventuella pågående återställning av NVIDIA-inställningar innan du uppdaterar. Installera nästa installation med den befintliga identiteten, eller extrahera den nya bärbara datorn till en ny mapp; behålla tillstånd/säkerhetskopior.

Innan du avinstallerar, återställ önskade säkerhetskopior av spel SDK och NVIDIA-inställningar via programmet, stäng sedan spel och avsluta handkontrollen. Använd Windows **Installed apps** för installationen, eller ta bort den stängda portabla mappen efter att ha bevarat nödvändiga filer. Ta inte bort en aktiv återställningsjournal manuellt för att avblockera installationen.

Lokala spel-runtime-säkerhetskopior använder `%LOCALAPPDATA%\NvidiaStreamlineMaintenance\Backups`. MFG-inställningar/SDK-data använder `%LOCALAPPDATA%\RtxMfg`; sessionsutgång är under `Sessions` bredvid applikationen. Dessa filer kan innehålla spelvägar. Lägg inte upp dem oredigerade.

<a id="known-limitations"></a>
## Kända begränsningar

- Experimentella inbyggda patchar kan orsaka krascher eller visuella artefakter; en olöst Bodycam-krasch registreras i utvecklingshistoriken.
- Kontrollerade återgivningstester är inte certifiering för varje spel, drivrutin eller anti-fusk.
- Genererade ramar skapar inte nya ingångsexempel; ingen uppmätt latens eller prestandavinst utlovas av denna hubb.
- Flera ramgenereringsverktyg/överlägg kan komma i konflikt. Applikationen rapporterar observerade moduler utan att bevisa varje samexistensscenario.
- Kompatibilitetsmanifestet är ett detekteringshjälpmedel, inte en lista över fullt testade spel.
- Fullständiga NVIDIA SDK-villkor och den olösta tekniska begränsningen förblir dokumenterade i [härkomst](../docs/provenance.md).

<a id="troubleshooting"></a>
## Felsökning

| Symptom | Åtgärd |
| --- | --- |
| Leverantören stöds inte | Behåll de ursprungliga verifierade filerna. Rapportera drivrutins-/leverantörsversioner och felet; gå inte förbi hashkontrollen. |
| Ingen DLSS FG i spelet | Välj det svaret och lämna spelet i kontroll; det här verktyget kan inte tillverka den integrationen. |
| Spelkrascher/artefakter | Avsluta spelet, inaktivera NVMFG, använd spelets ursprungliga runtime backup om den ändrades och rapportera reproducerbara detaljer. |
| SDK lista eller nedladdning är inte tillgänglig | Uppdatera och kontrollera den officiella källan; en cachad/importerad version måste fortfarande godkännas. |
| Väntande NVIDIA-återställning blockerar exit/uppdatering | Använd återvinning och bevara journalen; konflikter får inte skrivas över blint. |
| Ett borttaget spel återupptäcks inte | Dess uteslutning är ihållande. Lägg till det explicit när du vill att det ska hanteras igen. |

[Delad supportvägledning](../docs/support.md) förklarar vad som ska inkluderas i en rapport.

<a id="faq"></a>
## FAQ

**Inkluderar det NVIDIA DLL:er eller modeller?** Ingen drivrutin, NGX leverantör/modell eller Streamline runtime ingår. Explicita SDK-nedladdningar kommer från NVIDIA.

**Fungerar Dynamic med V-Sync avstängd?** Den är avstängd i det läget. Välj inställningen i spelet eller en kvalificerad fast multiplikator för det spelets separata tillstånd.

**Är detta ett ReShade/OptiScaler/FSR-paket?** Nej. De är inte kompilerade eller skickade som en del av detta produktionspaket.

**Är de modifierade källorna offentliga?** Nej. Kompilerade paket och obligatoriska krediter/licenser tillhandahålls. Detta tar inte bort tredje parts rättigheter eller begränsningar.

<a id="upstream-and-modifications"></a>
## Uppströms och modifieringar

Jämförelsereferens och delade inbyggda komponenter: **RTX40MFG-Unlock av Michael Robles / dashdogy**, referens commit `4e776d068f91b4a665425542bb005dd57cc3d891`, MIT. [Förvar](https://github.com/dashdogy/RTX40MFG-Unlock) · [Originalnedladdningar](https://github.com/dashdogy/RTX40MFG-Unlock/releases).

Källjämförelsen identifierar delad patchning, leverantör/policyhantering, tidskorrigeringar och MinHook-baserade omvägskomponenter. Deras meddelanden MIT och BSD behålls. Den fullständiga jämförelsen inkluderar även filer utanför produktionsmålet.

Desktopapplikationen, styrenheten och SDK-hanteringsarbetsflödet är utvecklade av 禅堂 Zendo (RevoluSound Team). Projektarbetet inkluderar central laddning, NGX bootstrap-integration, verifierat leverantörsval, spel/V-Sync-koordinering och sessionsdiagnostik. Proveniensguiden skiljer det arbetet från de delade komponenterna; en filjämförelse ensam visar inte när någon av författaren hade idén.

Profilhjälpen anpassar MIT NVAPI omslaget från Orbmu2k:s Profile Inspector. [Detaljerad härkomst och komponentomfattning](../docs/provenance.md).

<a id="credits-and-license"></a>
## Krediter och licens

Michael Robles; Orbmu2k; Tsuda Kageyu och HDE bidragsgivare; NVIDIA Corporation; Microsoft och bidragsgivare; Inno Setup författare och översättare. Applikationsutveckling, integrationer och paketering: 禅堂 Zendo (RevoluSound Team).

[befintlig delningsbehörighet för kompilerade paket](../../../../NVMFG-Unlock40/LICENSE) och alla [komponentlicenser](LICENSES/README.md) är bevarade. MIT-behörigheter för uppströmskod skiljer sig från NVIDIA SDK-termer. Ingen filtlicens ersätter dem.

Oberoende av, inte sponsrad av och inte officiellt godkänd av NVIDIA Corporation. Alla refererade varumärken förblir deras ägares egendom.
