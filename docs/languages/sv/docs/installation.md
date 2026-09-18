<!-- nv-language-navigation:start -->
🌐 [English](../../../installation.md) | [Français](../../../installation.fr.md) · [NV Laboratory](../README.md)

<details>
<summary>🌐 Language · 34</summary>

[العربية](../../ar/docs/installation.md) · [বাংলা](../../bn/docs/installation.md) · [简体中文](../../zh/docs/installation.md) · [Čeština](../../cs/docs/installation.md) · [Dansk](../../da/docs/installation.md) · [Nederlands](../../nl/docs/installation.md) · [English](../../../installation.md) · [Filipino](../../fil/docs/installation.md) · [Suomi](../../fi/docs/installation.md) · [Français](../../../installation.fr.md) · [Deutsch](../../de/docs/installation.md) · [Ελληνικά](../../el/docs/installation.md) · [हिन्दी](../../hi/docs/installation.md) · [Magyar](../../hu/docs/installation.md) · [Bahasa Indonesia](../../id/docs/installation.md) · [Italiano](../../it/docs/installation.md) · [日本語](../../ja/docs/installation.md) · [한국어](../../ko/docs/installation.md) · [मराठी](../../mr/docs/installation.md) · [فارسی](../../fa/docs/installation.md) · [Polski](../../pl/docs/installation.md) · [Português](../../pt/docs/installation.md) · [ਪੰਜਾਬੀ](../../pa/docs/installation.md) · [Română](../../ro/docs/installation.md) · [Русский](../../ru/docs/installation.md) · [Español](../../es/docs/installation.md) · [Kiswahili](../../sw/docs/installation.md) · **Svenska** · [தமிழ்](../../ta/docs/installation.md) · [ไทย](../../th/docs/installation.md) · [Türkçe](../../tr/docs/installation.md) · [Українська](../../uk/docs/installation.md) · [اردو](../../ur/docs/installation.md) · [Tiếng Việt](../../vi/docs/installation.md)

[Translation policy](../../README.md)

</details>
<!-- nv-language-navigation:end -->

<!-- nv-translation-notice:start -->
> Maskinassisterad översättning från engelska. Tekniska namn, kommandon, URL:er och ursprungliga lagtexter bevaras. Recension av modersmål är välkommen; konsultera den engelska referensen om formuleringen är otydlig.
<!-- nv-translation-notice:end -->

<a id="installation-guide"></a>
# Installationsguide

Börja med [Nedladdningar](downloads.md), som registrerar publiceringsstatus och exakta tillgångsnamn. Dessa är separata verktyg: installera bara de du behöver.

> **För NVRasterPulse, installera [RTSS från Guru3D](https://www.guru3d.com/download/rtss-rivatuner-statistics-server-download/) innan du öppnar profilhanteraren.**
> RTSS måste köras för att tillämpa gränser; den ingår inte i NV Tools.

| Verktyg | Installerad utgåva | Bärbar utgåva | Huvudförutsättning |
| --- | --- | --- | --- |
| NVIDIA Profile Inspector – NV Tools Fork | NVPI-CustomNV-3.0.2.3-Setup-r2.exe | Extrahera komplett NVPI ZIP | NVIDIA drivrutin och .NET Framework 4.8 |
| NVDriverForge | NVDriverForge-Setup.exe | NVDriverForge.exe, körtid ingår | Kompatibelt original NVIDIA drivrutinspaket för installationsoperationer |
| NVMFG Unlock40 | NVMFGUnlock40-0.2.3-Setup-x64.exe | Extrahera komplett NVMFG ZIP, behåll undermappar | RTX 40, befintlig DLSS FG, exakt leverantör och .NET Framework 4.8-hjälpare |
| NVRasterPulse | NVRasterPulse-0.2-win-x64-Setup.exe | Extrahera komplett RP ZIP | RTSS och .NET Framework 4.8 |

<a id="download-verify-install"></a>
## Ladda ner, verifiera, installera

1. På den valda publicerade versionen, ladda ner dess namngivna applikationstillgång, meddelanden ZIP och SHA256SUMS.txt.
2. Använd [SHA-256 exempel](downloads.md#sha-256), med det faktiska nedladdade filnamnet.
3. För installation, följ det vanliga installationsprogrammet. För portabel ZIP, extrahera allt till en ny lokal skrivbar mapp; kör inte inifrån ZIP.
4. Öppna programmets egna EXE. Behåll medföljande licens-/konfigurations-/datafiler.
5. Läs verktygets användningsinstruktioner innan du aktiverar inställningar eller systemoperationer.

Aktuella binärer är osignerade. En matchande hash bekräftar de förväntade byten; det är inte ett säkerhets- eller kompatibilitetscertifikat. Inaktivera inte Windows säkerhetsskydd bara för att undertrycka en varning.

Installation av NVDF eller dess valfria NVPI-kompanjon är separat från installation av en GPU-drivrutin. NVPI-kompanjonen behåller sitt befintliga interna installationsnamn. Dess förhöjda RasterPulse-knapp kräver en skyddad systemomfattande installation; andra RP-kopior kan öppnas med sina egna genvägar.

NVMFG är experimentell och har [dokumenterad NVIDIA SDK licensreserv](provenance.md). Ingen NVIDIA-drivrutin, NGX-leverantör/modell eller spel Streamline körtid ingår. Utvalda SDK-nedladdningar och speluppdateringar är explicit separata operationer.

<a id="language-and-updates"></a>
## Språk och uppdateringar

Använd README:s 34-språksväljare för dokumentation. NVDF, NVMFG och RP har sina egna 34-språkiga UI-inställning; NVPI behåller sitt befintliga språkstöd. Vissa tekniska installationssträngar faller tillbaka till engelska.

Behåll ett verktygs installationsidentitet när du uppdaterar. Stäng den först och bevara säkerhetskopior. För NVMFG, stäng berörda spel och lös pågående profilåterställning. För bärbara uppdateringar, använd en ny mapp istället för att kombinera utgåvor.

<a id="removing-a-tool"></a>
## Ta bort ett verktyg

Att avinstallera ett program ångrar inte automatiskt dess inställningar.

- **NVPI:** återställ avsedda profiler/visningsinställningar före borttagning om det behövs.
- **NVDF:** använd återställning först om du vill återställa avancerade/NVENC-ändringar. Uninstall lämnar grafikdrivrutinen, inställningar och säkerhetskopior.
- **NVMFG:** stäng spel, inaktivera/avsluta kontrollern, lös NVIDIA-återställning och återställ önskade spel SDK-säkerhetskopior innan de tas bort.
- **RP:** ta bort de avsedda begränsaröverstyrningarna först. Uninstall raderar inte sparade RTSS-kapslar eller tar inte bort RTSS.

Se varje [projektguide](../README.md#projects) för exakta dataplatser och begränsningar, eller [stöd](support.md) om ett återställningssteg misslyckas.
