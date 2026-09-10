<!-- nv-language-navigation:start -->
🌐 [English](../../../../NVDriverForge/README.md) | [Français](../../../../NVDriverForge/README.fr.md) · [NV Laboratory](../README.md)

<details>
<summary>🌐 Language · 34</summary>

[العربية](../../ar/NVDriverForge/README.md) · [বাংলা](../../bn/NVDriverForge/README.md) · [简体中文](../../zh/NVDriverForge/README.md) · [Čeština](../../cs/NVDriverForge/README.md) · **Dansk** · [Nederlands](../../nl/NVDriverForge/README.md) · [English](../../../../NVDriverForge/README.md) · [Filipino](../../fil/NVDriverForge/README.md) · [Suomi](../../fi/NVDriverForge/README.md) · [Français](../../../../NVDriverForge/README.fr.md) · [Deutsch](../../de/NVDriverForge/README.md) · [Ελληνικά](../../el/NVDriverForge/README.md) · [हिन्दी](../../hi/NVDriverForge/README.md) · [Magyar](../../hu/NVDriverForge/README.md) · [Bahasa Indonesia](../../id/NVDriverForge/README.md) · [Italiano](../../it/NVDriverForge/README.md) · [日本語](../../ja/NVDriverForge/README.md) · [한국어](../../ko/NVDriverForge/README.md) · [मराठी](../../mr/NVDriverForge/README.md) · [فارسی](../../fa/NVDriverForge/README.md) · [Polski](../../pl/NVDriverForge/README.md) · [Português](../../pt/NVDriverForge/README.md) · [ਪੰਜਾਬੀ](../../pa/NVDriverForge/README.md) · [Română](../../ro/NVDriverForge/README.md) · [Русский](../../ru/NVDriverForge/README.md) · [Español](../../es/NVDriverForge/README.md) · [Kiswahili](../../sw/NVDriverForge/README.md) · [Svenska](../../sv/NVDriverForge/README.md) · [தமிழ்](../../ta/NVDriverForge/README.md) · [ไทย](../../th/NVDriverForge/README.md) · [Türkçe](../../tr/NVDriverForge/README.md) · [Українська](../../uk/NVDriverForge/README.md) · [اردو](../../ur/NVDriverForge/README.md) · [Tiếng Việt](../../vi/NVDriverForge/README.md)

[Translation policy](../../README.md)

</details>
<!-- nv-language-navigation:end -->

<!-- nv-translation-notice:start -->
> Maskinassisteret oversættelse fra engelsk. Tekniske navne, kommandoer, URL'er og originale lovtekster er bevaret. Native-speaker anmeldelse er velkommen; se den engelske reference, hvis ordlyden er uklar.
<!-- nv-translation-notice:end -->

<a id="nvdriverforge"></a>
# NVDriverForge

**Forbered en NVIDIA driverinstallation med klare komponentvalg og valgfrie indstillinger.**

[Download 0.1.3 & status](../docs/downloads.md#nvdriverforge) · [Installation](#installation) · [Credits](#credits-and-upstream) · [Licens](../../../../NVDriverForge/LICENSE)

<a id="overview-and-purpose"></a>
## Overblik og formål

NVDriverForge guider dig gennem en original NVIDIA driverpakke: vælg driveren, inspicér dens komponenter, gennemgå valgfri justeringer, og bekræft derefter installationen. Den eksisterer for at gøre disse valg forståelige og holde installationen, privilegerede operationer og genoprettelsesoplysninger sammen.

Det er en uafhængigt udviklet applikation, der er delvist inspireret af NVCleanstall's arbejdsgang. Det inkluderer ikke NVCleanstall eller hævder fuldstændig funktionsparitet.

<a id="features"></a>
## Funktioner

- NVIDIA Game Ready / Studio opslag og downloads; valgfri hotfix-opdagelse med manuel fallback.
- Analyse af den originale pakke, hashes, NVIDIA-signaturer, manifester og kompatible INF-poster.
- Komponentvalg med afhængigheder og bevarelse af ukendte komponenter.
- Version 0.1.3 bevarer udvalgte valgfrie NVIDIA-komponenter, der kan springes over, og udelukker kun verificerede umarkerede komponenter fra opdagelse. Allerede nuværende eller uanvendelige valgfrie kørselstider tvinges ikke længere som kritiske komponenter.
- Ryd installationsfejloversigter og adgang til detaljerede logfiler på alle 34 sprog.
- Eksplicit installationsbekræftelse, beskyttet iscenesættelse og eksport af eksisterende driver-store-pakker.
- Valgfri avancerede indstillinger med forhåndskontrol, journaler og konfliktbevidst genopretning.
- Valgfri **Custom NV** forudindstilling med navngivne valg og forklaringer, inklusive et separat SILK styrkevalg og kompatibilitetstjek.
- Valgfri nøjagtig version af NVENC-patch-downloads; kildebekræftelse og målbytes kontrolleres.
- En separat, valgfri installation af Profile Inspector fork fra skærmen Værktøjer.
- Valgfri installerede brugeropdateringstjek, 34 grænsefladesprog og fire temaer.

Tilgængelige avancerede muligheder vedrører MPO, DLSS-indikatoren, Ansel, NVIDIA-lydsøvn, MSI, afbrydelsespolitik/-prioritet, HDCP, opstart af display-container og en kvalificeret ældre telemetritjeneste. Hver har sine egne forudsætninger og virkninger; disse er ikke universelle præstationsforbedringer.

<a id="compatibility"></a>
## Kompatibilitet

| Krav | Detaljer |
| --- | --- |
| System | Windows 10 build 19041 eller nyere / Windows 11, x64 |
| GPU/driver | Kompatibel NVIDIA-pakke og fundet hardware; automatisk katalogopslag dækker primært kendte GeForce-modeller |
| Runtime | .NET 8 / WPF 8.0.31 inkluderet i den forberedte selvstændige pakke |
| Privilegier | Normal UI/per-bruger opsætning; driverinstallation og systemændringer anmoder om administratoradgang |
| Netværk | Påkrævet for online NVIDIA opslag/downloads og eksplicitte upstream NVENC anmodninger; en lokal original driver kan vælges |
| Medfølgende værktøj | Uændret 7-Zip 26.03, runtime notifikationer, valgfri MIT Profile Inspector ledsager |
| Valgfri ledsager | .NET Framework 4.8 til den separate Profile Inspector fork |

Ingen vilkårlig minimumsdriverversion dækker alle funktioner. Multi-GPU-opslag skal matche alle detekterede GPU. Ikke-understøttede/professionelle modeller kan kræve manuel drivervalg. NVIDIA's installationsprogram forbliver den endelige hardware/OS-autoritet.

<a id="installation"></a>
## Installation

1. Besøg [downloads](../docs/downloads.md#nvdriverforge) og bekræft, at udgivelsen er offentliggjort.
2. Vælg `NVDriverForge-Setup.exe` til installation eller `NVDriverForge.exe` til bærbar brug.
3. Sammenlign SHA-256 med udgivelsens `SHA256SUMS.txt`.
4. Kør Setup for en per-bruger installation og standard afinstallationsprogram, eller placer den bærbare EXE i en skrivbar mappe, og åbn den.

Den bærbare computer inkluderer dens runtime og dens valgfri installationsprogram. Installation af NVDriverForge installerer ikke en GPU-driver. Dens EXE'er er i øjeblikket usignerede.

<a id="usage"></a>
## Brug

1. **Driver:** download fra NVIDIA eller vælg en original NVIDIA-installations-EXE. Lad analysen afslutte.
2. **Komponenter:** gennemgå beskrivelser og påkrævede afhængigheder. Ukendte komponenter bibeholdes.
3. **Tweaks:** lad uønskede indstillinger være uændrede. Læs effekter og afvejninger, før du vælger noget.
4. **Gennemgang:** tjek den nøjagtige driver, komponenter og valgfri handlinger, og bekræft derefter installationen.
5. Accepter kun UAC for den handling, du har valgt. Gem det beskyttede jobs genoprettelsesinstruktioner.
6. Hvis den nye driver har brug for en genstart, skal du følge den rapporterede tilstand. Udskudte operationer kræver eksplicit genoptagelse efter denne genstart.

Custom NV starter uændret. Vælg individuelle navngivne værdier, eller gennemgå den medfølgende forudindstilling og dens ekskluderinger. Dens to informative interne felter er ikke uafhængigt skrevet. Indstillinger anvendes kun i den verificerede nye driver-workflow, aldrig ved at åbne en forhåndsvisning. Det er ikke nødvendigt at installere den separate NVPI-editor.

Valgfrit NVENC-arbejde downloader kompatible data fra en fastgjort keylase-commit. Det ændrer to driver-DLL'er og ugyldiggør deres signaturer; det kan afvises af Windows, indkodere, DRM eller anti-cheat. Ingen sådanne data eller NVIDIA DLL er indlejret i NVDriverForge. [Herkomst- og licensgrænser](../docs/provenance.md).

Præferencer kontrollerer sprog, tema og valgfri opdateringskontrol for installerede brugere. Den bærbare computer opretter ikke den installerede baggrundskontrolopgave. Værktøjer og gendannelse er adskilt fra de fire installationstrin.

<a id="screenshots"></a>
## Skærmbilleder

![NVDriverForge forhåndsvisning af driverside](../../../../assets/screenshots/nvdriverforge-0.1.2-preview.png)

Eksisterende 0.1.2 fransk UI-gengivelse med eksempeldata; bevares som en interface-forhåndsvisning. Den viste 699.99-driver er et testarmatur, ikke en rigtig version, der skal downloades. [Billedets oprindelse](../assets/README.md).

<a id="update-and-uninstall"></a>
## Opdater og afinstaller

Luk NVDriverForge, få den næste officielle pakke og bekræft dens hash. Brug den samme opsætningsidentitet til en installeret opdatering; erstatte en lukket bærbar EXE med den nye. Behold indstillinger og beskyttede job.

Uninstall fra Windows **Installed apps**. Det fjerner appen og dens opdateringsopgave, ikke NVIDIA-driveren. Indstillinger, logfiler og sikkerhedskopier forbliver. Gendan om ønsket avancerede/NVENC-ændringer gennem det dokumenterede gendannelsesflow **inden** du fjerner appen. Gendan afviser modstridende ændringer fra et andet værktøj.

Lokale data er under `%LOCALAPPDATA%\NVDriverForge`; beskyttede job og førereksport er under `%PROGRAMDATA%\NVDriverForge\Jobs`. Bærbar brug skaber også lokale data. En driver-store eksport er ikke et systembillede eller en fuld profil backup.

<a id="known-limitations"></a>
## Kendte begrænsninger

- Ingen hardwaretilføjelser/INF-redigering, regenererede NVIDIA-signaturer, anti-cheat-kompatibel fratræden eller automatisk accept af usigneret advarsel.
- Ingen fuldstændig fjernelse af telemetri/reklamer, eksport af slanke pakker eller automatisk fuld tilbagerulning til den tidligere driver.
- Driverinstallation, opstartsgendannelse og valgfri profilskrivning er ikke blevet grundigt valideret på rigtige maskiner af hub-revisionen.
- Tilbagelæsning af registreringsdatabasen er ikke bevis for faktiske HDCP, ydeevne eller latenseffekter.
- Signaturkontrol bruger lokalt tilgængelig Windows-tillid; online tilbagekaldelse udføres ikke.
- 34 sprog er til stede, men fuld modersmåls-/tilgængelighedstest er fortsat ufuldstændig.

<a id="troubleshooting"></a>
## Fejlfinding

| Symptom | Handling |
| --- | --- |
| Onlinekatalog ikke tilgængeligt | Vælg en original pakke fra [NVIDIA driver downloads](https://www.nvidia.com/en-us/drivers/). Udskift ikke en tilstødende GPU-model. |
| Hotfix-opslag er ikke tilgængeligt | Brug [NVIDIA's Game Ready driverforum](https://www.nvidia.com/en-us/geforce/forums/game-ready-drivers/13/) og bekræft den faktiske pakke. |
| Installationen af NVIDIA mislykkes | Læs fejloversigten, og åbn de detaljerede logfiler. Valgfrie komponenter, der allerede er aktuelle eller ikke anvendelige, kan springes over i 0.1.3. Mislykkede installationer udløser ikke valgfri tweaks eller et succes/genstartsflow. |
| Signatur/hash/sikkerhedskopieringsfejl | Stop installationen og behold fejlen; få den originale pakke igen, hvis den er beskadiget. |
| Mulighed ikke tilgængelig | Læs årsagen til hardware, komponent eller måldriver; holde det uændret. |
| Genstart eller job afventer stadig | Brug jobbets genoprettelsesinstruktioner og eksplicitte CV; slet ikke dens journal. |
| Gendan konflikt | En anden tilstand adskiller sig fra den registrerede transaktion. Bevar det og bed om hjælp i stedet for at tvinge en gendannelse. |

For rapporter skal du inkludere den valgte værktøjsversion, Windows, GPU, driver og reproducerbare trin; redigere stier og personlige oplysninger fra logfiler. [Support](../docs/support.md).

<a id="faq"></a>
## FAQ

**Installerer Setup en grafikdriver?** Nej. Det kræver applikationens separate analyse, gennemgang, bekræftelse og forhøjede installationsproces.

**Har jeg brug for NVCleanstall eller NVPI?** Nej. NVCleanstall er kun inspiration. Profile Inspector-ledsageren er en uafhængig valgfri editor.

**Gør det hver NVIDIA-driver mindre eller hurtigere?** Nej. Udvalgte komponenter og forudsætninger bestemmer, hvad der kan ændres; der loves ingen målt gevinst.

**Hvor er kilderne?** Applikationsspecifikke kilde- og private tests vedligeholdes separat. Denne hub leverer dokumentation, binære filer og tredjepartskildelinks, der kræves for tilskrivning/licensering.

<a id="credits-and-upstream"></a>
## Credits og upstream

Original applikation, arbejdsgang, transaktioner, lokalisering, bootstrap og tilpasninger: 禅堂 Zendo (RevoluSound Team).

- [NVCleanstall / TechPowerUp](https://www.techpowerup.com/download/techpowerup-nvcleanstall/): workflow inspiration; ingen kilde eller binær importeret.
- [NVIDIA Profile Inspector / Orbmu2k](https://github.com/Orbmu2k/nvidiaProfileInspector): MIT-temaer, udvidet NVAPI-grænsefladereference og separat pakket fork.
- [7-Zip / Igor Pavlov](https://www.7-zip.org/): umodificerede ekstraktionsværktøjer.
- [Microsoft .NET](https://github.com/dotnet/runtime) og [WPF](https://github.com/dotnet/wpf): bundtet kørselstid.
- [Inno Setup](https://jrsoftware.org/isinfo.php): original installationsprogram og krediterede oversættelser.
- [keylase/nvidia-patch](https://github.com/keylase/nvidia-patch): ekstern valgfri NVENC datakilde; omfordelingslicens ikke etableret.
- [NVIDIA](https://www.nvidia.com/en-us/drivers/): ekstern driver downloader og installerede NVAPI/NVML-biblioteker.

[Fuld komponent tabel](../THIRD_PARTY_NOTICES.md) · [Ændringer og herkomst](../docs/provenance.md)

<a id="license"></a>
## Licens

[Eksisterende binær distributionstilladelse](../../../../NVDriverForge/LICENSE) tillader brug og deling af umodificerede officielle eksekverbare filer med deres meddelelser. Applikationsspecifikke kilderettigheder forbeholdes. Det begrænser ikke rettigheder givet af de separate tredjepartslicenser. [Fuldstændige meddelelser](LICENSES/README.md).

Uafhængig af NVIDIA Corporation, TechPowerUp og keylase; ikke sponsoreret eller officielt godkendt af dem. Produktnavne forbliver deres ejeres varemærker.
