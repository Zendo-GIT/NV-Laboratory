<!-- nv-language-navigation:start -->
🌐 [English](../../../README.md) | [Français](../../../README.fr.md) · [NV Laboratory](README.md)

<details>
<summary>🌐 Language · 34</summary>

[العربية](../ar/README.md) · [বাংলা](../bn/README.md) · [简体中文](../zh/README.md) · [Čeština](../cs/README.md) · **Dansk** · [Nederlands](../nl/README.md) · [English](../../../README.md) · [Filipino](../fil/README.md) · [Suomi](../fi/README.md) · [Français](../../../README.fr.md) · [Deutsch](../de/README.md) · [Ελληνικά](../el/README.md) · [हिन्दी](../hi/README.md) · [Magyar](../hu/README.md) · [Bahasa Indonesia](../id/README.md) · [Italiano](../it/README.md) · [日本語](../ja/README.md) · [한국어](../ko/README.md) · [मराठी](../mr/README.md) · [فارسی](../fa/README.md) · [Polski](../pl/README.md) · [Português](../pt/README.md) · [ਪੰਜਾਬੀ](../pa/README.md) · [Română](../ro/README.md) · [Русский](../ru/README.md) · [Español](../es/README.md) · [Kiswahili](../sw/README.md) · [Svenska](../sv/README.md) · [தமிழ்](../ta/README.md) · [ไทย](../th/README.md) · [Türkçe](../tr/README.md) · [Українська](../uk/README.md) · [اردو](../ur/README.md) · [Tiếng Việt](../vi/README.md)

[Translation policy](../README.md)

</details>
<!-- nv-language-navigation:end -->

<!-- nv-translation-notice:start -->
> Maskinassisteret oversættelse fra engelsk. Tekniske navne, kommandoer, URL'er og originale lovtekster er bevaret. Native-speaker anmeldelse er velkommen; se den engelske reference, hvis ordlyden er uklar.
<!-- nv-translation-notice:end -->

<a id="nv-laboratory"></a>
# NV Laboratory

**NV Tools af 禅堂 Zendo (RevoluSound Team).** Fire uafhængige Windows-værktøjer til NVIDIA-driverprofiler, driverinstallation, eksperimentelle Multi Frame Generation- og RTSS-rammegrænser.

[Få værktøjerne](docs/downloads.md) · [Installation](docs/installation.md) · [Kompatibilitet og hjælp](docs/support.md) · [Kreditter og licenser](THIRD_PARTY_NOTICES.md)

> **NVRasterPulse kræver RTSS.** Installer [RivaTuner Statistics Server fra Guru3D](https://www.guru3d.com/download/rtss-rivatuner-statistics-server-download/) først. RTSS skal køre, for at dets FPS-grænser virker. Den downloades separat.

<a id="projects"></a>
## Projekter

| Projekt | Formål | version | Dokumentation | Download |
| --- | --- | --- | --- | --- |
| **NVIDIA Profile Inspector – NV Tools Fork** | NVIDIA driverprofileditor med tilføjet display, farve, HDR og ICC/WCS kontroller. Tidligere NVPI Custom. | 3.0.2.3 | [Vejledning](NVIDIA-Profile-Inspector/README.md) | [Pakker](docs/downloads.md#nvidia-profile-inspector) |
| **NVDriverForge** | Vælg driverkomponenter, gennemgå valgfri tweaks og installer en original NVIDIA driverpakke. | 0.1.3 | [Vejledning](NVDriverForge/README.md) | [Pakker](docs/downloads.md#nvdriverforge) |
| **NVMFG Unlock40** | Eksperimentelt RTX 40 MFG værktøj med valg pr. spil og Streamline SDK vedligeholdelse. | 0.1.1 | [Vejledning](NVMFG-Unlock40/README.md) | [Pakker og status](docs/downloads.md#nvmfg-unlock40) |
| **NVRasterPulse** | Administrer RTSS FPS-grænser pr. eksekverbar fil med brøkværdier, sikkerhedskopier og bakkeadgang. | 0.1 | [Vejledning](NVRasterPulse/README.md) | [Pakker](docs/downloads.md#nvrasterpulse) |

**Downloads:** [download side](docs/downloads.md) viser hver versions status, filer og SHA-256-værdier. Eksperimentelle funktioner og kompatibilitetsgrænser er beskrevet i projektvejledningerne.

<a id="start-here"></a>
## Start her

1. Vælg ét værktøj ovenfor. Hver arbejder selvstændigt; det er unødvendigt at installere hele suiten.
2. Læs kravene, og vælg **Opsætning** for en installeret app eller **bærbar** for en separat mappe.
3. Når dets udgivelse er offentliggjort, skal du downloade det navngivne applikationsaktiv, læse de medfølgende meddelelser og sammenligne dets SHA-256.
4. Behold sikkerhedskopier, før du ændrer en driver, skærmindstilling, NVIDIA-profil eller spilkørsel.

Dokumentation er tilgængelig på de samme 34 sprog som NV-applikationerne via vælgeren øverst i hver vejledning. GitHub vælger ikke automatisk et README efter browsersprog. Dokumentationssproget og applikationens egen sprogindstilling er adskilte.

<a id="provenance-and-ownership"></a>
## Herkomst og ejerskab

Denne hub distribuerer dokumentation og kompilerede applikationer. Applikationens kildekode vedligeholdes privat. Upstream-projekter bevarer deres forfatterskab og licenser; privat kildedistribution erstatter ikke disse vilkår.

- Profile Inspector fork beholder Orbmu2k's MIT-licens og er eksplicit identificeret som en fork.
- NVDriverForge har sine egne binære distributionsbetingelser og inkluderer separat licenserede runtime/værktøjskomponenter.
- NVMFG Unlock40 er en uafhængigt udviklet applikation. RTX40MFG-Unlock blev konsulteret med henblik på sammenligning og forfining; delte indbyggede komponenter beholder deres MIT-kreditter. MinHook og NVIDIA SDK vilkår forbliver adskilte.
- NVRasterPulse beholder den medfølgende MIT-licens og krediterer den Profile Inspector-afledte brugergrænseflade. RTSS er et påkrævet eksternt program.

Se [komplet komponenttabel](THIRD_PARTY_NOTICES.md), [fil herkomst og ændringer](docs/provenance.md) og [licensens omfang](../../../LICENSE).

<a id="other-projects--revolusound-team"></a>
## Andre projekter – RevoluSound Team

Disse er separate lydmodprojekter, der er linket her for at hjælpe dig med at opdage teamets arbejde.

| Spil | Projekt | Om |
| --- | --- | --- |
| Forza Horizon 6 | [Forza Horizon 6 Revolusound Team Pack](https://www.nexusmods.com/forzahorizon6/mods/56) | Køretøjslydændringer, der dækker motorer, udstødninger, indsugninger og turboeffekter. |
| Forza Horizon 5 | [Forza Horizon 5 Revolusound Team Pack 1.4.4 FINAL](https://www.nexusmods.com/forzahorizon5/mods/86) | Holdets senere FH5-køretøjslydpakke. |
| Forza Horizon 5 | [Forza Horizon 5.5 Zendo Revolusound Pack](https://www.nexusmods.com/forzahorizon5/mods/20) | Tidligere FH5-pakke; dens Nexus-side leder besøgende til den senere teampakke ovenfor. |

Titler følger de linkede Nexus Mods-sider. Deres downloads, krav, kreditter og tilladelser forbliver på Nexus Mods.

<a id="help-and-participation"></a>
## Hjælp og deltagelse

[Rapporter en fejl eller foreslå en funktion](https://github.com/Zendo-GIT/NV-Laboratory/issues) · [Bidrager](CONTRIBUTING.md) · [Sikkerhedsrapporter](SECURITY.md) · [Ændringslog](CHANGELOG.md)

For et sikkerhedsproblem skal du læse SECURITY.md, før du sender logfiler eller tekniske detaljer. Privat rapportering skal aktiveres af vedligeholderen efter offentliggørelse af lageret.

> **Uafhængige fællesskabsprojekter.** NV Laboratory, NV Tools og disse hjælpeprogrammer er ikke tilknyttet, sponsoreret af eller officielt godkendt af NVIDIA Corporation. NVIDIA, GeForce, RTX, DLSS og andre produktnavne er varemærker tilhørende deres respektive ejere. Navne beskriver kompatibilitet og herkomst, ikke officiel godkendelse.
