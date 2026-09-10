<!-- nv-language-navigation:start -->
🌐 [English](../../../development.md) | [Français](../../../development.fr.md) · [NV Laboratory](../README.md)

<details>
<summary>🌐 Language · 34</summary>

[العربية](../../ar/docs/development.md) · [বাংলা](../../bn/docs/development.md) · [简体中文](../../zh/docs/development.md) · [Čeština](../../cs/docs/development.md) · **Dansk** · [Nederlands](../../nl/docs/development.md) · [English](../../../development.md) · [Filipino](../../fil/docs/development.md) · [Suomi](../../fi/docs/development.md) · [Français](../../../development.fr.md) · [Deutsch](../../de/docs/development.md) · [Ελληνικά](../../el/docs/development.md) · [हिन्दी](../../hi/docs/development.md) · [Magyar](../../hu/docs/development.md) · [Bahasa Indonesia](../../id/docs/development.md) · [Italiano](../../it/docs/development.md) · [日本語](../../ja/docs/development.md) · [한국어](../../ko/docs/development.md) · [मराठी](../../mr/docs/development.md) · [فارسی](../../fa/docs/development.md) · [Polski](../../pl/docs/development.md) · [Português](../../pt/docs/development.md) · [ਪੰਜਾਬੀ](../../pa/docs/development.md) · [Română](../../ro/docs/development.md) · [Русский](../../ru/docs/development.md) · [Español](../../es/docs/development.md) · [Kiswahili](../../sw/docs/development.md) · [Svenska](../../sv/docs/development.md) · [தமிழ்](../../ta/docs/development.md) · [ไทย](../../th/docs/development.md) · [Türkçe](../../tr/docs/development.md) · [Українська](../../uk/docs/development.md) · [اردو](../../ur/docs/development.md) · [Tiếng Việt](../../vi/docs/development.md)

[Translation policy](../../README.md)

</details>
<!-- nv-language-navigation:end -->

<!-- nv-translation-notice:start -->
> Maskinassisteret oversættelse fra engelsk. Tekniske navne, kommandoer, URL'er og originale lovtekster er bevaret. Native-speaker anmeldelse er velkommen; se den engelske reference, hvis ordlyden er uklar.
<!-- nv-translation-notice:end -->

<a id="repository-architecture-and-maintenance"></a>
# Depotarkitektur og vedligeholdelse

NV Laboratory er en offentlig **dokumentations- og binær distributionshub**. Den indeholder ikke applikationskilde. De fire projekter bevarer separate byggetræer, versioner, identiteter og frigivelsesaktiver. Deres private udviklingshistorie importeres ikke til dette Git-lager.

<a id="layout"></a>
## Layout

| Beliggenhed | Formål |
| --- | --- |
| README.md / README.fr.md | Engelsk/fransk indgangssteder |
| Fire projektmapper | Fuldstændige vejledninger og gældende originale meddelelser |
| dokumenter | Downloads, kompatibilitet, oprindelse, udvikling og frigivelsesprocedure |
| docs/releases.json | Revideret kandidat/udgivelsesmetadata, størrelser og hashes |
| dokumenter/herkomst | Fil/hash sammenligninger; ingen applikationskode |
| licenser | Delte fulde tredjepartstekster og installatøroversætterkreditter |
| aktiver | Eksisterende gennemgåede UI-forhåndsvisninger og deres oprindelse |
| .github | Udstedelse af formularer og skrivebeskyttet dokumentationsvalidering |
| værktøjer/validate_repository.py | Standard-bibliotekets publikationsgrænse og linkkontrol |

Engelsk forbliver standard GitHub README. Eksisterende tilstødende `.fr.md`-links forbliver gyldige. Yderligere oversættelser afspejler dokumentationen under `docs/languages/<code>`; sprogvælgeren beholder den samme side, når der skiftes sprog. Kataloget `docs/languages/catalog.json` registrerer alle 34 sprog og kildefingeraftryk. GitHub vælger ikke automatisk et README efter browsersprog. Se [sprogindeks og oversættelsespolitik](../../README.md).

<a id="application-technologies"></a>
## Applikationsteknologier

| Program | Privat teknologi | Distribution |
| --- | --- | --- |
| NVPI fork | C#, WPF, .NET Framework 4.8, NVAPI/Windows interop | Komplet bærbar mappe og separat Inno Setup |
| NVDriverForge | C#, WPF, .NET 8; native C++ bootstrap; 7-Zip proces | Selvstændig bærbar EXE og opsætning |
| NVMFG Unlock40 | C#/WPF .NET 8, Framework 4.8 hjælpere, C++20/MASM/MinHook motor | Bærbart træ og opsætning |
| NVRasterPulse | C#/WPF Framework 4.8; RTSS-profil/genindlæsningsintegration; native bootstrap | Bærbart træ og opsætning |

Denne offentlige kasse kan ikke genopbygge applikationerne. Automatiske "Source code"-arkiver er hub-øjebliksbilleder. Opstrøms kildelinks repræsenterer ikke den nøjagtige private ændrede kilde. Det offentlige CI validerer kun dette lager.

<a id="local-checks"></a>
## Lokal kontrol

Fra depotroden:

```text
python tools/validate_repository.py
```

Python 3.10 eller nyere er tilstrækkeligt. Checken læser filer, lokale Markdown-links, påkrævede meddelelser/RTSS-links, release-metadata og udgivelsesgrænser. Det udfører ikke softwaren, installerer afhængigheder eller kontakter et netværk.

GitHub-arbejdsgangen kører den samme kontrol med skrivebeskyttet indholdstilladelse ved push, pull-anmodning eller manuel afsendelse. Checkout er fastgjort til en revideret forpligtelse og bevarer ikke legitimationsoplysninger. Der er ikke konfigureret noget frigivelses- eller implementeringsjob.

<a id="maintain-the-boundary"></a>
## Overhold grænsen

Opdater den engelske reference, franske guider og berørte oversættelser sammen. Hold indholdsmæssige ændringer adskilt fra sammenligninger, der kun er formatering. Registrer faktiske kandidat-hash, opstrøms commit-referencer og licenser; aldrig udlede en licens fra et projekts popularitet.

Brug nye versioner af udgivelsesaktiver, og revidér ændrede binære filer, arkiver og indlejrede meddelelser. Bevar private sikkerhedskopier uden for dette lager. Brug ikke en offentlig arbejdsgang til at importere privat programkilde eller lokale build-mapper.

Tests, der passer til en funktionel applikationsændring, køres i det private projekt. Kør ikke driverinstallationsprogrammer igen eller skriv rigtige profiler til en dokumentationsopdatering. [Manuel frigivelsesprocedure](releasing.md).
