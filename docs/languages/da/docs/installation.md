<!-- nv-language-navigation:start -->
🌐 [English](../../../installation.md) | [Français](../../../installation.fr.md) · [NV Laboratory](../README.md)

<details>
<summary>🌐 Language · 34</summary>

[العربية](../../ar/docs/installation.md) · [বাংলা](../../bn/docs/installation.md) · [简体中文](../../zh/docs/installation.md) · [Čeština](../../cs/docs/installation.md) · **Dansk** · [Nederlands](../../nl/docs/installation.md) · [English](../../../installation.md) · [Filipino](../../fil/docs/installation.md) · [Suomi](../../fi/docs/installation.md) · [Français](../../../installation.fr.md) · [Deutsch](../../de/docs/installation.md) · [Ελληνικά](../../el/docs/installation.md) · [हिन्दी](../../hi/docs/installation.md) · [Magyar](../../hu/docs/installation.md) · [Bahasa Indonesia](../../id/docs/installation.md) · [Italiano](../../it/docs/installation.md) · [日本語](../../ja/docs/installation.md) · [한국어](../../ko/docs/installation.md) · [मराठी](../../mr/docs/installation.md) · [فارسی](../../fa/docs/installation.md) · [Polski](../../pl/docs/installation.md) · [Português](../../pt/docs/installation.md) · [ਪੰਜਾਬੀ](../../pa/docs/installation.md) · [Română](../../ro/docs/installation.md) · [Русский](../../ru/docs/installation.md) · [Español](../../es/docs/installation.md) · [Kiswahili](../../sw/docs/installation.md) · [Svenska](../../sv/docs/installation.md) · [தமிழ்](../../ta/docs/installation.md) · [ไทย](../../th/docs/installation.md) · [Türkçe](../../tr/docs/installation.md) · [Українська](../../uk/docs/installation.md) · [اردو](../../ur/docs/installation.md) · [Tiếng Việt](../../vi/docs/installation.md)

[Translation policy](../../README.md)

</details>
<!-- nv-language-navigation:end -->

<!-- nv-translation-notice:start -->
> Maskinassisteret oversættelse fra engelsk. Tekniske navne, kommandoer, URL'er og originale lovtekster er bevaret. Native-speaker anmeldelse er velkommen; se den engelske reference, hvis ordlyden er uklar.
<!-- nv-translation-notice:end -->

<a id="installation-guide"></a>
# Installationsvejledning

Start med [Downloads](downloads.md), som registrerer udgivelsesstatus og nøjagtige aktivnavne. Disse er separate værktøjer: installer kun dem, du har brug for.

> **For NVRasterPulse skal du installere [RTSS fra Guru3D](https://www.guru3d.com/download/rtss-rivatuner-statistics-server-download/), før du åbner profiladministratoren.**
> RTSS skal køre for at anvende grænser; det er ikke inkluderet i NV Tools.

| Værktøj | Installeret udgave | Bærbar udgave | Hovedforudsætning |
| --- | --- | --- | --- |
| NVIDIA Profile Inspector – NV Tools Fork | NVPI-CustomNV-3.0.2.3-Setup-r2.exe | Udpak komplet NVPI ZIP | NVIDIA driver og .NET Framework 4.8 |
| NVDriverForge | NVDriverForge-Setup.exe | NVDriverForge.exe, køretid inkluderet | Kompatibel original NVIDIA driverpakke til installationshandlinger |
| NVMFG Unlock40 | NVMFGUnlock40-0.2.3-Setup-x64.exe | Udpak komplet NVMFG ZIP, behold undermapper | RTX 40, eksisterende DLSS FG, nøjagtig udbyder og .NET Framework 4.8 hjælpere |
| NVRasterPulse | NVRasterPulse-0.2-win-x64-Setup.exe | Udpak komplet RP ZIP | RTSS og .NET Framework 4.8 |

<a id="download-verify-install"></a>
## Download, bekræft, installer

1. På den valgte offentliggjorte udgivelse skal du downloade dets navngivne applikationsaktiv, meddelelser ZIP og SHA256SUMS.txt.
2. Brug [SHA-256 eksempel](downloads.md#sha-256) med det faktiske downloadede filnavn.
3. Følg det normale installationsprogram for opsætning. For bærbar ZIP, udpak alt til en ny lokal skrivbar mappe; løb ikke inde fra ZIP.
4. Åbn programmets egen EXE. Gem den medfølgende licens-/konfigurations-/datafiler.
5. Læs værktøjets brugsvejledning, før du aktiverer indstillinger eller systemhandlinger.

Nuværende binære filer er usignerede. En matchende hash bekræfter de forventede bytes; det er ikke et sikkerheds- eller kompatibilitetscertifikat. Deaktiver ikke Windows sikkerhedsbeskyttelse bare for at undertrykke en advarsel.

Installation af NVDF eller dens valgfri NVPI ledsager er adskilt fra installation af en GPU driver. NVPI-ledsageren beholder sit eksisterende interne installationsnavn. Dens forhøjede RasterPulse-knap kræver en beskyttet systemdækkende installation; andre RP-kopier kan åbnes via deres egne genveje.

NVMFG er eksperimentel og har [dokumenteret NVIDIA SDK licensreserve](provenance.md). Ingen NVIDIA driver, NGX udbyder/model eller spil Streamline runtime er inkluderet. Udvalgte SDK-downloads og spilopdateringer er eksplicitte separate operationer.

<a id="language-and-updates"></a>
## Sprog og opdateringer

Brug README's 34-sprogsvælger til dokumentation. NVDF, NVMFG og RP har deres egen 34-sprogs UI-indstilling; NVPI beholder sin eksisterende sprogunderstøttelse. Nogle tekniske installationsstrenge falder tilbage til engelsk.

Behold et værktøjs installationsidentitet, når du opdaterer. Luk det først og bevar sikkerhedskopier. For NVMFG skal du lukke berørte spil og løse afventende profilgendannelse. For bærbare opdateringer skal du bruge en ny mappe i stedet for at kombinere udgivelser.

<a id="removing-a-tool"></a>
## Fjernelse af et værktøj

Afinstallation af et program fortryder ikke automatisk dets indstillinger.

- **NVPI:** gendan tiltænkte profiler/skærmindstillinger før fjernelse, hvis det er nødvendigt.
- **NVDF:** brug først gendannelse, hvis du vil gendanne avancerede/NVENC ændringer. Uninstall forlader grafikdriveren, indstillinger og sikkerhedskopier.
- **NVMFG:** luk spil, deaktiver/luk controlleren, løs NVIDIA-gendannelse og gendan ønskede spil SDK-sikkerhedskopier før fjernelse.
- **RP:** fjern først de tilsigtede begrænsertilsidesættelser. Uninstall sletter ikke gemte RTSS-hætter eller fjerner RTSS.

Se hver [projektvejledning](../README.md#projects) for nøjagtige dataplaceringer og begrænsninger, eller [støtte](support.md), hvis et gendannelsestrin mislykkes.
