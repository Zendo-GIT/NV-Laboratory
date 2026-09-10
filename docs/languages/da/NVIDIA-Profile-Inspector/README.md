<!-- nv-language-navigation:start -->
🌐 [English](../../../../NVIDIA-Profile-Inspector/README.md) | [Français](../../../../NVIDIA-Profile-Inspector/README.fr.md) · [NV Laboratory](../README.md)

<details>
<summary>🌐 Language · 34</summary>

[العربية](../../ar/NVIDIA-Profile-Inspector/README.md) · [বাংলা](../../bn/NVIDIA-Profile-Inspector/README.md) · [简体中文](../../zh/NVIDIA-Profile-Inspector/README.md) · [Čeština](../../cs/NVIDIA-Profile-Inspector/README.md) · **Dansk** · [Nederlands](../../nl/NVIDIA-Profile-Inspector/README.md) · [English](../../../../NVIDIA-Profile-Inspector/README.md) · [Filipino](../../fil/NVIDIA-Profile-Inspector/README.md) · [Suomi](../../fi/NVIDIA-Profile-Inspector/README.md) · [Français](../../../../NVIDIA-Profile-Inspector/README.fr.md) · [Deutsch](../../de/NVIDIA-Profile-Inspector/README.md) · [Ελληνικά](../../el/NVIDIA-Profile-Inspector/README.md) · [हिन्दी](../../hi/NVIDIA-Profile-Inspector/README.md) · [Magyar](../../hu/NVIDIA-Profile-Inspector/README.md) · [Bahasa Indonesia](../../id/NVIDIA-Profile-Inspector/README.md) · [Italiano](../../it/NVIDIA-Profile-Inspector/README.md) · [日本語](../../ja/NVIDIA-Profile-Inspector/README.md) · [한국어](../../ko/NVIDIA-Profile-Inspector/README.md) · [मराठी](../../mr/NVIDIA-Profile-Inspector/README.md) · [فارسی](../../fa/NVIDIA-Profile-Inspector/README.md) · [Polski](../../pl/NVIDIA-Profile-Inspector/README.md) · [Português](../../pt/NVIDIA-Profile-Inspector/README.md) · [ਪੰਜਾਬੀ](../../pa/NVIDIA-Profile-Inspector/README.md) · [Română](../../ro/NVIDIA-Profile-Inspector/README.md) · [Русский](../../ru/NVIDIA-Profile-Inspector/README.md) · [Español](../../es/NVIDIA-Profile-Inspector/README.md) · [Kiswahili](../../sw/NVIDIA-Profile-Inspector/README.md) · [Svenska](../../sv/NVIDIA-Profile-Inspector/README.md) · [தமிழ்](../../ta/NVIDIA-Profile-Inspector/README.md) · [ไทย](../../th/NVIDIA-Profile-Inspector/README.md) · [Türkçe](../../tr/NVIDIA-Profile-Inspector/README.md) · [Українська](../../uk/NVIDIA-Profile-Inspector/README.md) · [اردو](../../ur/NVIDIA-Profile-Inspector/README.md) · [Tiếng Việt](../../vi/NVIDIA-Profile-Inspector/README.md)

[Translation policy](../../README.md)

</details>
<!-- nv-language-navigation:end -->

<!-- nv-translation-notice:start -->
> Maskinassisteret oversættelse fra engelsk. Tekniske navne, kommandoer, URL'er og originale lovtekster er bevaret. Native-speaker anmeldelse er velkommen; se den engelske reference, hvis ordlyden er uklar.
<!-- nv-translation-notice:end -->

<a id="nvidia-profile-inspector--nv-tools-fork"></a>
# NVIDIA Profile Inspector – NV Tools Fork

**En uafhængig fork af [NVIDIA Profile Inspector af Orbmu2k](https://github.com/Orbmu2k/nvidiaProfileInspector), med tilføjede displaykontroller.** Tidligere projektnavn: **NVPI Custom**.

[Download og frigivelsesstatus](../docs/downloads.md#nvidia-profile-inspector) · [Installation](#installation) · [Upstream og ændringer](#upstream-and-changes) · [Licens](../../../../NVIDIA-Profile-Inspector/LICENSE)

<a id="overview"></a>
## Oversigt

Applikationen redigerer NVIDIA-driverprofiler, inklusive indstillinger pr. applikation. Denne fork tilføjer også en **Skærm**-editor til den aktive Windows-skærm: opløsning, opdateringshastighed, outputfarveindstillinger, HDR og installerede ICC/WCS-profiltilknytninger.

Det eksisterer for at bringe relaterede visningskontroller ind i profileditoren og for at gøre forhåndsvisning, bekræftelse og gendannelsesresultater klarere. Det etablerer ikke nye hardwarefunktioner.

Den første kandidat er **3.0.2.3**, der bruger den rensede selvstændige companion build fra 9. september 2026. Dens eksisterende eksekverbare forbliver `nvidiaProfileInspector.exe`; installationsprogrammet og nogle interne etiketter siger stadig `NVPI Custom NV`. Den offentlige titel ovenfor identificerer fork uden at ændre installationens identitet eller foregive, at det er Orbmu2k's officielle udgivelse.

<a id="features"></a>
## Funktioner

- Eksisterende opstrøms profilbrowsing, applikationstilknytninger, indstillingsredigeringer og profilimport/eksport.
- **Skærm**-dialog for display, tilstand, Hz, RGB/YCbCr, farvedybde, område og kolorimetri.
- Windows HDR kontrol og installeret ICC/WCS tilknytningsvalg.
- En 15-sekunders forhåndsvisning med **Keep** / **Revert** og timeoutgendannelse.
- Tilbagelæsning af tilstand/HDR ændringer og rapporterede gendannelsesfejl.
- Separat rapportering af HDR, SDR med ACM/WCG og signalfarvedybde.
- En NVRasterPulse launcher til en kvalificeret separat installeret kopi.

<a id="compatibility"></a>
## Kompatibilitet

| Krav | Detaljer |
| --- | --- |
| System | Windows 10/11 x64 med en kompatibel NVIDIA-driver |
| Runtime | [.NET Framework 4.8](https://dotnet.microsoft.com/en-us/download/dotnet-framework/net48), leveret af Windows eller installeret separat |
| Tilladelser | Redaktøren anmoder om administratoradgang, når den åbnes |
| Viser | Faktiske tilstande og farvekombinationer afhænger af GPU, driver, skærm, kabel og Windows API'er |
| Valgfri værktøjer | NVRasterPulse til RTSS grænsestyring; hverken den eller RTSS er nødvendig for skærmeditoren |
| Sprog | Opsætning: 34-sprogsvælger. Redaktøren bevarer sin eksisterende sprogunderstøttelse. |

Der er intet verificeret universelt driverminimum eller supportmatrix for hver GPU. Dialogens tilgængelige bpc-valg er anmodninger, ikke certificerede kombinationer. Moderne HDR kontroller og den ældre Windows fallback har forskellige muligheder.

<a id="installation"></a>
## Installation

1. Åbn [download side](../docs/downloads.md#nvidia-profile-inspector) og kontroller publikationsstatus.
2. Download opsætningen eller det bærbare aktiv, og sammenlign dets SHA-256 med udgivelsesmanifestet.
3. Til opsætning skal du køre `NVPI-CustomNV-3.0.2.3-Setup-r2.exe`, vælge et sprog og følge installationsprogrammet. Det opretter sin egen genvej og afinstallationsprogram.
4. For bærbar, udpak hele ZIP til en ny skrivbar mappe. Behold `Reference.xml`, EXE-konfigurationen og alle meddelelser ved siden af ​​den eksekverbare.
5. Start `nvidiaProfileInspector.exe`.

Installation af editoren alene anvender ikke en profil eller installerer en GPU-driver. Ledsageren installeres separat, overtager ikke `.nip`-tilknytninger og aktiverer ikke opstart ved login. Eksisterende binære filer er uden fortegn.

<a id="usage"></a>
## Brug

**Installationsversion 2** tilføjer den samme indbyggede 34-sprogsvælger som de andre værktøjer med mus/tastaturnavigation, lys/mørke udseende og annullering. Valget gælder opsætning; den oversætter ikke NVPI-editoren. Et eksplicit `/LANG=fr`-argument eller tavs tilstand omgår valg for opkaldere, der allerede leverer et sprog.

**Driverprofiler:** vælg en profil, eksporter en sikkerhedskopi, rediger derefter kun de tilsigtede indstillinger og anvend dem. Ansøgningsforeninger bestemmer, hvilket spil der modtager en profil. En lagret værdi er ikke et bevis på, at enhver driver eller spil bruger den.

**Skærmkontroller:** åbn **Skærm**, vælg displayet og de ønskede værdier, og start derefter forhåndsvisningen. Tjek billedet, før du vælger **Behold** inden for 15 sekunder. Brug **Vend tilbage**, luk bekræftelsen eller lad den udløbe for at anmode om gendannelse. Læs enhver fejlmeddelelse: Et vellykket API-kald alene er ikke bevis på gendannelse.

Et ICC-valg ændrer en installeret profiltilknytning; den genererer, kalibrerer eller omdistribuerer ikke en ICC-fil. HDR, ACM/WCG, RGB/YCbCr og bpc beskriver forskellige aspekter af rørledningen. Der medfølger ingen ny uafhængig ACM-switch.

**NVRasterPulse:** værktøjslinjeknappen accepterer en separat registreret systemdækkende installation under Programfiler med beskyttet ejerskab og tilladelser. En bærbar kopi eller en bruger-skrivbar/linket sti kan blive afvist af denne forhøjede launcher. I så fald skal du åbne NVRasterPulse med sin egen genvej. [Installer RTSS separat](https://www.guru3d.com/download/rtss-rivatuner-statistics-server-download/) for at bruge NVRasterPulse.

<a id="screenshots"></a>
## Skærmbilleder

![NVPI opsætning revision 2 sprogvælger](../../../../assets/screenshots/nvpi-setup-r2-language.png)

Faktisk opsætningsvælger på fransk, fanget under en isoleret test og derefter annulleret. Dette viser installationsprogrammet; editoren bevarer sin grænseflade og skærmdialog.

<a id="update-and-uninstall"></a>
## Opdater og afinstaller

Luk editoren før opdatering. Behold eksporterede profiler og download den nye fork-udgivelse; installer over den samme ledsagende identitet eller udpak bærbare filer i en ny mappe. Bland ikke en gammel `Reference.xml` med en ny eksekverbar. Den medfølgende upstream-opdateringskontrolundertrykkelse tilhører denne fork.

For en installeret kopi skal du bruge Windows **Installed apps** og dets afinstallationsprogram. For bærbar, luk den og fjern dens udpakkede mappe, når din eksport er sikker. Fjernelse af editoren fortryder **ikke** driverprofilredigeringer, visningspræferencer, NVRasterPulse eller RTSS. Gendan ønskede indstillinger før fjernelse.

<a id="known-limitations"></a>
## Kendte begrænsninger

- 15 sekunders bekræftelse er ikke en vagthund for hvert førerulykke, strømtab eller tvungen nedlukning.
- Nogle farve/dybde/opdateringskombinationer returnerer `NVAPI_NOT_SUPPORTED`.
- Softwaretilbagelæsning måler ikke panelbitdybde, farvenøjagtighed eller latens.
- Skærmindstillinger påvirker det aktuelle Windows-display; denne dialog opretter ikke forudindstillinger for visning pr. spil.
- Ingen ydeevne, anti-snyd eller universel HDR-kompatibilitetsgaranti.

<a id="troubleshooting"></a>
## Fejlfinding

| Symptom | Handling |
| --- | --- |
| Kørselsfejl ved lancering | Tjek Windows-opdateringer og .NET Framework 4.8; bruge hele pakken. |
| Den anmodede visningstilstand blev afvist | Vend tilbage og test en tilstand, der tilbydes af Windows/NVIDIA for den skærm. Læs den nøjagtige fejl og undgå gentagne blinde ændringer. |
| HDR eller farve vender tilbage til den gamle tilstand | Kontroller, om en anden operation mislykkedes og udløste gendannelse; skelne HDR fra ACM. |
| Knappen NVRasterPulse afviser en sti | Start sin egen genvej; denne knap kræver en beskyttet systemdækkende installation. |
| En ændring forbliver efter afinstallation | Gendan den eksporterede NVIDIA-profil eller de tilsigtede Windows-skærmindstillinger; afinstallation er ikke en tilbagerulning af indstillinger. |

Se [fælles støttevejledning](../docs/support.md), før du sender logfiler.

<a id="faq"></a>
## FAQ

**Er denne officielle NVIDIA-software eller Orbmu2k's officielle build?** Nej. Det er en uafhængig fork; upstream-forfatteren og MIT-licensen forbliver krediteret.

**Kræver NVDriverForge denne editor?** Nej. NVDriverForge's valgfri Custom NV forudindstilling bruger sin egen integration. Installation af editoren er et separat valg.

**Er RTSS obligatorisk for denne fork?** Nej. RTSS er obligatorisk for NVRasterPulse's FPS limiter, ikke til profil- eller skærmredigering.

**Hvor er kilden?** Den ændrede programkilde vedligeholdes privat. MIT-meddelelsen og upstream-lageret er leveret; MIT kræver ikke udgivelse af ændret kilde.

<a id="upstream-and-changes"></a>
## Upstream og ændringer

Upstream: [Orbmu2k/nvidiaProfileInspector](https://github.com/Orbmu2k/nvidiaProfileInspector), reference commit `592d962cca8827efe8859461a84267755595064a`. [Originale downloads](https://github.com/Orbmu2k/nvidiaProfileInspector/releases).

Nedarvet: profileditor, NVAPI interop, referencedata, UI-ressourcer og temaer. 禅堂 Zendo (RevoluSound Team) tilføjede eller tilpassede visningstjenester, HDR/ICC-transaktioner, 15-sekunders bekræftelse/tilbagelæsning, værktøjslinjelayout og RasterPulse-lanceringsadfærd. Den rensede ledsager udelukker udviklingsmocks/testindgangspunkter, bruger en beskyttet ekstern launcher og giver et separat installationsprogram. Den gamle kombinerede NVPI/RasterPulse udviklingspakke er ikke kandidaten i denne hub.

[Detaljeret fil herkomst](../docs/provenance.md) · [Original fork-meddelelse](../../../../NVIDIA-Profile-Inspector/LICENSES/ORIGINAL-FORK-NOTICE.txt)

<a id="credits-and-license"></a>
## Credits og licens

Copyright (c) 2016 Orbmu2k. Den medfølgende [MIT licens](../../../../NVIDIA-Profile-Inspector/LICENSE) bibeholdes. Tilpasninger og pakning: 禅堂 Zendo (RevoluSound Team). Installationsprogrammet bruger Inno Setup; Windows og .NET Framework forbliver eksterne. [Fuldstændige gældende meddelelser](LICENSES/README.md).

Uafhængig af, ikke sponsoreret af og ikke officielt godkendt af NVIDIA Corporation. Varemærker forbliver hos deres respektive ejere.
