<!-- nv-language-navigation:start -->
🌐 [English](../../../../NVRasterPulse/README.md) | [Français](../../../../NVRasterPulse/README.fr.md) · [NV Laboratory](../README.md)

<details>
<summary>🌐 Language · 34</summary>

[العربية](../../ar/NVRasterPulse/README.md) · [বাংলা](../../bn/NVRasterPulse/README.md) · [简体中文](../../zh/NVRasterPulse/README.md) · [Čeština](../../cs/NVRasterPulse/README.md) · **Dansk** · [Nederlands](../../nl/NVRasterPulse/README.md) · [English](../../../../NVRasterPulse/README.md) · [Filipino](../../fil/NVRasterPulse/README.md) · [Suomi](../../fi/NVRasterPulse/README.md) · [Français](../../../../NVRasterPulse/README.fr.md) · [Deutsch](../../de/NVRasterPulse/README.md) · [Ελληνικά](../../el/NVRasterPulse/README.md) · [हिन्दी](../../hi/NVRasterPulse/README.md) · [Magyar](../../hu/NVRasterPulse/README.md) · [Bahasa Indonesia](../../id/NVRasterPulse/README.md) · [Italiano](../../it/NVRasterPulse/README.md) · [日本語](../../ja/NVRasterPulse/README.md) · [한국어](../../ko/NVRasterPulse/README.md) · [मराठी](../../mr/NVRasterPulse/README.md) · [فارسی](../../fa/NVRasterPulse/README.md) · [Polski](../../pl/NVRasterPulse/README.md) · [Português](../../pt/NVRasterPulse/README.md) · [ਪੰਜਾਬੀ](../../pa/NVRasterPulse/README.md) · [Română](../../ro/NVRasterPulse/README.md) · [Русский](../../ru/NVRasterPulse/README.md) · [Español](../../es/NVRasterPulse/README.md) · [Kiswahili](../../sw/NVRasterPulse/README.md) · [Svenska](../../sv/NVRasterPulse/README.md) · [தமிழ்](../../ta/NVRasterPulse/README.md) · [ไทย](../../th/NVRasterPulse/README.md) · [Türkçe](../../tr/NVRasterPulse/README.md) · [Українська](../../uk/NVRasterPulse/README.md) · [اردو](../../ur/NVRasterPulse/README.md) · [Tiếng Việt](../../vi/NVRasterPulse/README.md)

[Translation policy](../../README.md)

</details>
<!-- nv-language-navigation:end -->

<!-- nv-translation-notice:start -->
> Maskinassisteret oversættelse fra engelsk. Tekniske navne, kommandoer, URL'er og originale lovtekster er bevaret. Native-speaker anmeldelse er velkommen; se den engelske reference, hvis ordlyden er uklar.
<!-- nv-translation-notice:end -->

<a id="nvrasterpulse"></a>
# NVRasterPulse

**Per-applikation FPS grænser til RivaTuner Statistics Server.**

> **Installer RTSS først.** NVRasterPulse kræver [RivaTuner Statistics Server (RTSS), downloadet fra Guru3D](https://www.guru3d.com/download/rtss-rivatuner-statistics-server-download/). RTSS skal køre for at håndhæve grænser. Ingen RTSS-installationsprogram, hook-DLL eller SDK er bundtet.

[Download 0.1 & status](../docs/downloads.md#nvrasterpulse) · [Installation](#installation) · [Hvordan grænser fungerer](#usage) · [Licens](../../../../NVRasterPulse/LICENSE)

<a id="overview-and-purpose"></a>
## Overblik og formål

NVRasterPulse er en kompakt Windows-grænseflade til styring af RTSS-rammegrænser efter eksekverbart navn. RTSS udfører begrænsningen. NVRasterPulse administrerer de tilsvarende profilværdier, sikkerhedskopier og genindlæsningsanmodninger med bakkeadgang og vedvarende valg.

Det eksisterer for at gøre det nemmere at redigere nøjagtige grænser pr. spil uden at erstatte en hel RTSS-profil eller forstyrre dens overlejringsindstillinger. Den nuværende **0.1**-kandidat er buildet den 9. september 2026 med et påkrævet RTSS-installationstjek.

<a id="features"></a>
## Funktioner

- Vælg et kørende program, eller tilføj dets eksekverbare manuelt.
- Gem FPS-grænser fra 1 til 1000 med op til tre decimaler.
- Nøjagtig rationel indkodning af indtastede værdier: 59.94 bliver 2997/50.
- Front Edge Sync-konfiguration (`SyncLimiter=1`) med aktiv ventetid (`PassiveWait=0`).
- Per-eksekverbare profilopdateringer, automatisk sikkerhedskopiering og atomskrivning.
- Fjernelse af limiter-tilsidesættelser, mens andet profilindhold bibeholdes.
- RTSS installationsdetektering, manuel stivalg og eksplicit start/genindlæsning.
- Betjening af en enkelt bakke, valgfri installeret opstart, 34 sprog og fire temaer.
- Adskil normal afslutning og **Afslut + RTSS** handlinger.

<a id="compatibility"></a>
## Kompatibilitet

| Krav | Detaljer |
| --- | --- |
| System | Windows 10/11 x64 |
| Runtime | [.NET Framework 4.8](https://dotnet.microsoft.com/en-us/download/dotnet-framework/net48), installeres separat hvis nødvendigt |
| Nødvendig software | RTSS med `RTSS.exe`, en matchende `Profiles`-mappe og kompatibel profil/genindlæsningsunderstøttelse |
| GPU | RTSS kompatibilitet bestemmer begrænseren; denne profilmanager kræver ikke en bestemt RTX-generation |
| Tilladelser | Nuværende applikation anmoder om administratoradgang; den valgte RTSS-profilmappe skal være tilgængelig |
| Spil | Afhænger af RTSS hooking support og hvert spils begrænsninger; ingen anti-snyd garanti |

Ingen specifik RTSS minimumsversion er blevet certificeret for hver funktion af denne hub-revision. Brug den officielle aktuelle distribution og rapporter den nøjagtige version, hvis en profilnøgle/genindlæsning ikke virker. Installeret-men-stoppet RTSS består installationskontrollen; den skal så startes for egentlig begrænsning.

<a id="installation"></a>
## Installation

1. **[Download og installer RTSS fra Guru3D](https://www.guru3d.com/download/rtss-rivatuner-statistics-server-download/).**
2. Åbn [NVRasterPulse downloads](../docs/downloads.md#nvrasterpulse) og tjek frigivelsestilgængelighed.
3. Download `NVRasterPulse-0.1-win-x64-Setup.exe` eller `NVRasterPulse-0.1-win-x64-portable.zip` plus meddelelserne/kontrolsummerne.
4. Sammenlign SHA-256. Kør Setup eller udpak hele den bærbare ZIP til en skrivbar lokal mappe.
5. Åbn `NVRasterPulse.exe`. Hvis RTSS mangler, skal du bruge **Download RTSS**, installere det og derefter **Tjek igen** eller vælge `RTSS.exe` manuelt.
6. Start RTSS med dens normale genvej eller NVRasterPulse's RTSS-knap, hvis den er stoppet.

Deaktivering af den valgfri påmindelse springer ikke forudsætningskontrollen over. En lydløs Windows-bakkeopstart venter, indtil hovedvinduet åbnes, før denne kontrol vises. Opsætningen installerer kun NVRasterPulse. Dens EXE'er er usignerede.

<a id="usage"></a>
## Brug

1. Vælg det tilsigtede kørende program, eller gennemse dets spil EXE.
2. Indtast en grænse mellem 1 og 1000 FPS, inklusive en brøkværdi, hvis det er nødvendigt.
3. Gem og kontroller det rapporterede resultat. NVRasterPulse opdaterer den eksekverbares RTSS-profil og anmoder om en genindlæsning.
4. Bekræft, at RTSS kører, og bekræft adfærden i det tilsigtede spil.

Profiler indtastes efter **eksekverbart navn**, såsom `Game.exe.cfg`. To forskellige mapper, der indeholder `Game.exe`, deler den samme RTSS-profil; lagring af den fulde sti fjerner ikke denne kollision.

Lagring bruger Front Edge Sync og aktiv ventetid. Aktiv ventetid kan øge brugen af ​​CPU. De alternative `LimitTime`-felter er neutraliseret. Eksisterende kommentarer, overlejringsindstillinger og `EnableHooking=0` bevares. RTSS Global-profilen ændres ikke.

Brug papirkurven til at fjerne NVRasterPulse's limiter-tilsidesættelser. Det sletter ikke hele RTSS-profilen. En grænse, der er arvet fra RTSS Global eller et andet værktøj, kan stadig gælde efterfølgende.

**Lukning og afslutning:** Hovedvinduet kan skjule sig til bakken. Normal **Afslut** efterlader RTSS kørende og gemte grænser intakte. **Afslut + RTSS** anmoder om en normal lukning af den matchende RTSS-proces i den aktuelle session, venter op til otte sekunder og tvinger den ikke ihjel. Gemte grænser forbliver i begge tilfælde.

Sprog og tema vælges i appen. Opstart ved Windows-logon er valgfri og beregnet til en installeret kopi. Informationsknappen forklarer almindelige handlinger.

<a id="screenshots"></a>
## Skærmbilleder

![NVRasterPulse forhåndsvisning af hovedvinduet](../../../../assets/screenshots/nvrasterpulse-0.1-preview.png)

Eksisterende fransk 0.1 UI gengivelse med eksempler på eksekverbare navne og en 176 FPS værdi. RTSS vises stoppet; dette er en grænsefladeillustration, ikke en kørebegrænser eller latensmåling. [Billedets oprindelse](../assets/README.md).

<a id="update-and-uninstall"></a>
## Opdater og afinstaller

Afslut NVRasterPulse, download og bekræft den nye version, kør derefter dens opsætning eller udpak den bærbare computer til en ny mappe. Bevar indstillinger og RTSS-sikkerhedskopier. RTSS-opdateringer er separate og kommer fra Guru3D.

For at fjerne en installeret kopi skal du bruge Windows **Installed apps**. For bærbar, luk og fjern dens udpakkede mappe, når dine sikkerhedskopier er sikre. Gemte RTSS-grænser fjernes ikke ved at afinstallere NVRasterPulse: fjern først de tilsigtede limiter-tilsidesættelser. RTSS har sit eget afinstallationsprogram.

Lokal stat: `%LOCALAPPDATA%\NVRasterPulse`. Automatiske RTSS-sikkerhedskopier: `%LOCALAPPDATA%\NVRasterPulse\Backups\RTSS`. En ældre `%LOCALAPPDATA%\RTSSProfileBridge`-placering kan læses til migrering. Disse filer kan indeholde personlige eksekverbare stier og bør ikke offentliggøres.

<a id="known-limitations"></a>
## Kendte begrænsninger

- RTSS udfører hætten. En gemt værdi eller en vellykket genindlæsningsanmodning er ikke et målt frame-time-resultat.
- Eksekverbare filer med samme navn deler en profil.
- En anden global/per-spil-begrænser kan påvirke resultatet; Deaktivering af den lokale tilsidesættelse fjerner ikke en nedarvet hætte.
- En bevidst deaktiveret RTSS krog forbliver deaktiveret.
- Aktiv venting har en CPU/strøm-afvejning.
- Intet universelt spil, anti-cheat eller end-to-end latency validering.
- Den tidligere eksperimentelle uafhængige limiter-motor er ikke kompileret eller afsendt.
- Automatiske sikkerhedskopier indebærer ikke en fuld backup-gendannelsesgrænseflade med et enkelt klik.

<a id="troubleshooting"></a>
## Fejlfinding

| Symptom | Handling |
| --- | --- |
| RTSS-forudsætningen forbliver åben | Vælg den faktiske `RTSS.exe` og matchende profiler-mappe, og tjek derefter igen. |
| Grænsen er gemt, men ingen effekt | Start RTSS; verificere den korrekte spil EXE/profil, hook-tilladelser og andre begrænsere. |
| Gem mislykkes | Tjek mappetilladelser og bevar den viste fejl/sikkerhedskopi. |
| Grænsen forbliver efter fjernelse | Undersøg RTSS Global og andre værktøjer; trash handlingen fjerner kun lokale begrænser tilsidesættelser. |
| To spil får den samme grænse | Kontroller, om deres eksekverbare filnavne er identiske. |
| Afslut + RTSS efterlader RTSS åben | Luk RTSS normalt selv; denne kommando undgår bevidst tvungen opsigelse. |

Hvis du manuelt gendanner en RTSS-sikkerhedskopi, skal du først lukke RTSS og bevare den aktuelle profil, før du erstatter den med den tilsigtede sikkerhedskopi. Dette kan overskrive ikke-relaterede profilredigeringer; inspicere filen og datoen. [Delt support](../docs/support.md).

<a id="faq"></a>
## FAQ

**Har jeg også brug for MSI Afterburner?** NVRasterPulse kræver RTSS; det afhænger ikke af Afterburner-applikationen. Følg RTSS-distributørens installationsmuligheder.

**Kan jeg bruge dette uden at RTSS kører?** Du kan administrere profiler, når en installation er fundet, men RTSS skal køre for at begrænse.

**Fjerner hætterne ved afslutning eller afinstallation?** Nej. Fjern eksplicit de ønskede limiter-tilsidesættelser, før du fjerner NVRasterPulse.

**Er det en fork af RTSS?** Nej. Det er en uafhængig profiladministrator; ingen RTSS-kilde eller eksekverbar er inkorporeret.

<a id="upstream-modifications-and-credits"></a>
## Upstream, ændringer og krediteringer

Udviklingsarkivet stammer fra [Orbmu2k's NVIDIA Profile Inspector](https://github.com/Orbmu2k/nvidiaProfileInspector). Dens MIT-paletter/UI-ressourcer krediteres. Profilstyringstjenesterne, fraktionskodning, sikkerhedskopier, RTSS genindlæsningsbro, bakkeadfærd, forudsætningsvejledning, sprog og applikationsspecifikt ikon blev udviklet/tilpasset af 禅堂 Zendo (RevoluSound Team).

RTSS er udviklet af **Unwinder** og distribueret separat gennem Guru3D. NVRasterPulse kalder `UpdateProfiles` fra den valgte installerede hook DLL; ingen RTSS SDK eller krog binær er omfordelt. Installationsprogrammet bruger umodificeret Inno Setup 7.1.0 med tilpassede scripts/oversættelser og en projektopstart.

[Fuld herkomst](../docs/provenance.md) · [Tredjeparts bord](../THIRD_PARTY_NOTICES.md)

<a id="license"></a>
## Licens

Pakken distribuerer eksplicit NVRasterPulse under den medfølgende [MIT licens](../../../../NVRasterPulse/LICENSE), med bevaring af Copyright (c) 2016 Orbmu2k. Applikationskilden vedligeholdes privat; MIT kræver ikke offentliggørelse af ændret kilde. RTSS og Windows/.NET forbliver under deres egne vilkår. [Fuldstændige meddelelser](LICENSES/README.md).

Uafhængig af NVIDIA Corporation, MSI og RTSS; ikke sponsoreret eller officielt godkendt af dem. Produktnavne forbliver deres ejeres varemærker.
