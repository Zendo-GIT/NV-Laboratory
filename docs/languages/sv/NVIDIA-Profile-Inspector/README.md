<!-- nv-language-navigation:start -->
🌐 [English](../../../../NVIDIA-Profile-Inspector/README.md) | [Français](../../../../NVIDIA-Profile-Inspector/README.fr.md) · [NV Laboratory](../README.md)

<details>
<summary>🌐 Language · 34</summary>

[العربية](../../ar/NVIDIA-Profile-Inspector/README.md) · [বাংলা](../../bn/NVIDIA-Profile-Inspector/README.md) · [简体中文](../../zh/NVIDIA-Profile-Inspector/README.md) · [Čeština](../../cs/NVIDIA-Profile-Inspector/README.md) · [Dansk](../../da/NVIDIA-Profile-Inspector/README.md) · [Nederlands](../../nl/NVIDIA-Profile-Inspector/README.md) · [English](../../../../NVIDIA-Profile-Inspector/README.md) · [Filipino](../../fil/NVIDIA-Profile-Inspector/README.md) · [Suomi](../../fi/NVIDIA-Profile-Inspector/README.md) · [Français](../../../../NVIDIA-Profile-Inspector/README.fr.md) · [Deutsch](../../de/NVIDIA-Profile-Inspector/README.md) · [Ελληνικά](../../el/NVIDIA-Profile-Inspector/README.md) · [हिन्दी](../../hi/NVIDIA-Profile-Inspector/README.md) · [Magyar](../../hu/NVIDIA-Profile-Inspector/README.md) · [Bahasa Indonesia](../../id/NVIDIA-Profile-Inspector/README.md) · [Italiano](../../it/NVIDIA-Profile-Inspector/README.md) · [日本語](../../ja/NVIDIA-Profile-Inspector/README.md) · [한국어](../../ko/NVIDIA-Profile-Inspector/README.md) · [मराठी](../../mr/NVIDIA-Profile-Inspector/README.md) · [فارسی](../../fa/NVIDIA-Profile-Inspector/README.md) · [Polski](../../pl/NVIDIA-Profile-Inspector/README.md) · [Português](../../pt/NVIDIA-Profile-Inspector/README.md) · [ਪੰਜਾਬੀ](../../pa/NVIDIA-Profile-Inspector/README.md) · [Română](../../ro/NVIDIA-Profile-Inspector/README.md) · [Русский](../../ru/NVIDIA-Profile-Inspector/README.md) · [Español](../../es/NVIDIA-Profile-Inspector/README.md) · [Kiswahili](../../sw/NVIDIA-Profile-Inspector/README.md) · **Svenska** · [தமிழ்](../../ta/NVIDIA-Profile-Inspector/README.md) · [ไทย](../../th/NVIDIA-Profile-Inspector/README.md) · [Türkçe](../../tr/NVIDIA-Profile-Inspector/README.md) · [Українська](../../uk/NVIDIA-Profile-Inspector/README.md) · [اردو](../../ur/NVIDIA-Profile-Inspector/README.md) · [Tiếng Việt](../../vi/NVIDIA-Profile-Inspector/README.md)

[Translation policy](../../README.md)

</details>
<!-- nv-language-navigation:end -->

<!-- nv-translation-notice:start -->
> Maskinassisterad översättning från engelska. Tekniska namn, kommandon, URL:er och ursprungliga lagtexter bevaras. Recension av modersmål är välkommen; konsultera den engelska referensen om formuleringen är otydlig.
<!-- nv-translation-notice:end -->

<a id="nvidia-profile-inspector--nv-tools-fork"></a>
# NVIDIA Profile Inspector – NV Tools Fork

**En oberoende fork av [NVIDIA Profile Inspector av Orbmu2k](https://github.com/Orbmu2k/nvidiaProfileInspector), med extra displaykontroller.** Tidigare projektnamn: **NVPI Custom**.

[Nedladdnings- och släppstatus](../docs/downloads.md#nvidia-profile-inspector) · [Installation](#installation) · [Uppströms och förändringar](#upstream-and-changes) · [Licens](../../../../NVIDIA-Profile-Inspector/LICENSE)

<a id="overview"></a>
## Översikt

Applikationen redigerar NVIDIA drivrutinsprofiler, inklusive inställningar per applikation. Denna fork lägger också till en **Skärm**-redigerare för den aktiva Windows-skärmen: upplösning, uppdateringsfrekvens, utdatafärginställningar, HDR och installerade ICC/WCS-profilassociationer.

Det finns för att föra in relaterade visningskontroller i profilredigeraren och för att göra förhandsgransknings-, bekräftelse- och återställningsresultat tydligare. Det etablerar inte nya hårdvarufunktioner.

Den första kandidaten är **3.0.2.3**, med den rensade fristående kompanjonbyggen från den 9 september 2026. Dess befintliga körbara fil förblir `nvidiaProfileInspector.exe`; installationsprogrammet och vissa interna etiketter säger fortfarande `NVPI Custom NV`. Den offentliga titeln ovan identifierar fork utan att ändra installationsidentitet eller låtsas att det är Orbmu2k:s officiella utgåva.

<a id="features"></a>
## Funktioner

- Befintlig uppströms profilsurfning, applikationsassociationer, inställningsredigeringar och profilimport/export.
- **Skärm**-dialog för display, läge, Hz, RGB/YCbCr, färgdjup, intervall och kolorimetri.
- Windows HDR styr och installerat ICC/WCS associationsval.
- En 15-sekunders förhandsvisning med **Keep** / **Revert** och återställning av timeout.
- Återläsning av mod/HDR ändringar och rapporterade återställningsfel.
- Separat rapportering av HDR, SDR med ACM/WCG och signalfärgdjup.
- En NVRasterPulse startprogram för en kvalificerad separat installerad kopia.

<a id="compatibility"></a>
## Kompatibilitet

| Krav | Detaljer |
| --- | --- |
| System | Windows 10/11 x64 med en kompatibel NVIDIA-drivrutin |
| Körtid | [.NET Framework 4.8](https://dotnet.microsoft.com/en-us/download/dotnet-framework/net48), levererad av Windows eller installerad separat |
| Behörigheter | Redaktören begär administratörsåtkomst när den öppnas |
| Displayer | Faktiska lägen och färgkombinationer beror på GPU, drivrutin, display, kabel och Windows API:er |
| Valfria verktyg | NVRasterPulse för RTSS gränshantering; varken det eller RTSS behövs för skärmredigeraren |
| Språk | Inställning: 34-språksväljare. Redaktören behåller sitt befintliga språkstöd. |

Det finns ingen verifierad universell drivrutinsminimum eller supportmatris för varje GPU. Dialogrutans tillgängliga bpc-val är förfrågningar, inte certifierade kombinationer. Moderna HDR-kontroller och den äldre Windows reservfunktionen har olika möjligheter.

<a id="installation"></a>
## Installation

1. Öppna [nedladdningssida](../docs/downloads.md#nvidia-profile-inspector) och kontrollera publiceringsstatus.
2. Ladda ner installationsprogrammet eller den bärbara tillgången och jämför dess SHA-256 med releasemanifestet.
3. För installation, kör `NVPI-CustomNV-3.0.2.3-Setup-r2.exe`, välj ett språk och följ installationsprogrammet. Den skapar sin egen genväg och avinstallationsprogram.
4. För bärbar, extrahera hela ZIP till en ny skrivbar mapp. Behåll `Reference.xml`, EXE-konfigurationen och alla meddelanden bredvid den körbara filen.
5. Starta `nvidiaProfileInspector.exe`.

Enbart installation av editorn tillämpar inte en profil eller installerar en GPU-drivrutin. Kompanjonen installeras separat, tar inte över `.nip`-associationer och möjliggör inte start vid inloggning. Befintliga binärer är osignerade.

<a id="usage"></a>
## Användning

**Installationsversion 2** lägger till samma inbyggda 34-språksväljare som de andra verktygen, med mus/tangentbordsnavigering, ljus/mörkt utseende och annullering. Valet gäller installation; den översätter inte NVPI-redigeraren. Ett explicit `/LANG=fr`-argument eller tyst läge förbigår valet för uppringare som redan tillhandahåller ett språk.

**Förarprofiler:** välj en profil, exportera en säkerhetskopia och redigera sedan endast de avsedda inställningarna och använd dem. Applikationsföreningar avgör vilket spel som får en profil. Ett lagrat värde är inte ett bevis på att varje förare eller spel använder det.

**Visningskontroller:** öppna **Skärmen**, välj displayen och begärda värden och starta sedan förhandsgranskningen. Kontrollera bilden innan du väljer **Behåll** inom 15 sekunder. Använd **Återställ**, stäng bekräftelsen eller låt den löpa ut för att begära återställning. Läs alla felmeddelanden: enbart ett lyckat API-anrop är inte ett bevis på återställning.

Ett ICC-val ändrar en installerad profilassociation; den genererar, kalibrerar eller omdistribuerar inte en ICC-fil. HDR, ACM/WCG, RGB/YCbCr och bpc beskriver olika aspekter av pipelinen. Ingen ny oberoende ACM-switch tillhandahålls.

**NVRasterPulse:** verktygsfältsknappen accepterar en separat registrerad systemomfattande installation under Programfiler med skyddat ägande och behörighet. En bärbar kopia eller en användarskrivbar/länkad sökväg kan nekas av denna förhöjda startprogram. Öppna i så fall NVRasterPulse med sin egen genväg. [Installera RTSS separat](https://www.guru3d.com/download/rtss-rivatuner-statistics-server-download/) för att använda NVRasterPulse.

<a id="screenshots"></a>
## Skärmdumpar

![NVPI setup version 2 språkväljare](../../../../assets/screenshots/nvpi-setup-r2-language.png)

Faktisk inställningsväljare på franska, fångad under ett isolerat test och sedan avbruten. Detta visar installationsprogrammet; redigeraren behåller sitt gränssnitt och skärmdialog.

<a id="update-and-uninstall"></a>
## Uppdatera och avinstallera

Stäng redigeraren innan du uppdaterar. Behåll exporterade profiler och ladda ner den nya fork-versionen; installera över samma medföljande identitet eller extrahera bärbara filer till en ny mapp. Blanda inte en gammal `Reference.xml` med en ny körbar fil. Den medföljande undertryckningen av uppströmsuppdateringskontroll tillhör denna fork.

För en installerad kopia, använd Windows **Installed apps** och dess avinstallationsprogram. För bärbar, stäng den och ta bort den extraherade mappen när dina exporter är säkra. Om du tar bort editorn ångras **inte** redigeringar av drivrutinsprofiler, visningsinställningar, NVRasterPulse eller RTSS. Återställ önskade inställningar före borttagning.

<a id="known-limitations"></a>
## Kända begränsningar

- Den 15 sekunder långa bekräftelsen är inte en vakthund för varje förarkrasch, strömavbrott eller tvångsavstängning.
- Vissa kombinationer av färg/djup/uppdatering returnerar `NVAPI_NOT_SUPPORTED`.
- Återläsning av programvara mäter inte panelbitdjup, färgnoggrannhet eller latens.
- Skärminställningar påverkar den aktuella Windows-skärmen; Den här dialogrutan skapar inte förinställningar för visning per spel.
- Ingen prestanda, anti-fusk eller universell HDR-kompatibilitetsgaranti.

<a id="troubleshooting"></a>
## Felsökning

| Symptom | Åtgärd |
| --- | --- |
| Körtidsfel vid start | Kontrollera Windows-uppdateringar och .NET Framework 4.8; använda hela paketet. |
| Begärt visningsläge avvisades | Återställ och testa ett läge som erbjuds av Windows/NVIDIA för den skärmen. Läs det exakta felet och undvik upprepade blindbyten. |
| HDR eller färg återgår till det gamla tillståndet | Kontrollera om en annan operation misslyckades och utlöste återställning; skilja HDR från ACM. |
| NVRasterPulse-knappen vägrar en sökväg | Starta en egen genväg; den här knappen kräver en skyddad systemomfattande installation. |
| En ändring kvarstår efter avinstallationen | Återställ den exporterade NVIDIA-profilen eller de avsedda Windows-skärminställningarna; avinstallation är inte en återställning av inställningar. |

Se [delad stödvägledning](../docs/support.md) innan du skickar loggar.

<a id="faq"></a>
## FAQ

**Är denna officiella NVIDIA-programvara eller Orbmu2k:s officiella version?** Nej. Det är en oberoende fork; uppströmsförfattaren och MIT-licensen förblir krediterade.

**Kräver NVDriverForge denna editor?** Nej. NVDriverForge:s valfria förinställning Custom NV använder sin egen integration. Att installera editorn är ett separat val.

**Är RTSS obligatoriskt för denna fork?** Nej. RTSS är obligatoriskt för NVRasterPulse:s FPS limiter, inte för profil- eller skärmredigering.

**Var är källan?** Den modifierade programkällan underhålls privat. MIT-meddelandet och uppströmsförrådet tillhandahålls; MIT kräver inte publicering av modifierad källa.

<a id="upstream-and-changes"></a>
## Uppströms och förändringar

Uppströms: [Orbmu2k/nvidiaProfile Inspector](https://github.com/Orbmu2k/nvidiaProfileInspector), referens commit `592d962cca8827efe8859461a84267755595064a`. [Originalnedladdningar](https://github.com/Orbmu2k/nvidiaProfileInspector/releases).

Ärvt: profilredigerare, NVAPI interop, referensdata, UI-resurser och teman. 禅堂 Zendo (RevoluSound Team) tillagda eller anpassade visningstjänster, HDR/ICC-transaktioner, 15-sekunders bekräftelse/återläsning, verktygsfältslayout och RasterPulse-startbeteende. Den rengjorda följeslagaren utesluter utvecklingsmocks/testingångspunkter, använder en skyddad extern launcher och tillhandahåller ett separat installationsprogram. Det gamla kombinerade utvecklingspaketet NVPI/RasterPulse är inte kandidaten i detta nav.

[Detaljerad fil härkomst](../docs/provenance.md) · [Original fork meddelande](../../../../NVIDIA-Profile-Inspector/LICENSES/ORIGINAL-FORK-NOTICE.txt)

<a id="credits-and-license"></a>
## Krediter och licens

Copyright (c) 2016 Orbmu2k. Den medföljande [MIT-licens](../../../../NVIDIA-Profile-Inspector/LICENSE) bibehålls. Anpassningar och paketering: 禅堂 Zendo (RevoluSound Team). Installationsprogrammet använder Inno Setup; Windows och .NET Framework förblir externa. [Fullständiga tillämpliga meddelanden](LICENSES/README.md).

Oberoende av, inte sponsrad av och inte officiellt godkänd av NVIDIA Corporation. Varumärken förblir hos sina respektive ägare.
