<!-- nv-language-navigation:start -->
🌐 [English](../../../installation.md) | [Français](../../../installation.fr.md) · [NV Laboratory](../README.md)

<details>
<summary>🌐 Language · 34</summary>

[العربية](../../ar/docs/installation.md) · [বাংলা](../../bn/docs/installation.md) · [简体中文](../../zh/docs/installation.md) · [Čeština](../../cs/docs/installation.md) · [Dansk](../../da/docs/installation.md) · [Nederlands](../../nl/docs/installation.md) · [English](../../../installation.md) · [Filipino](../../fil/docs/installation.md) · [Suomi](../../fi/docs/installation.md) · [Français](../../../installation.fr.md) · **Deutsch** · [Ελληνικά](../../el/docs/installation.md) · [हिन्दी](../../hi/docs/installation.md) · [Magyar](../../hu/docs/installation.md) · [Bahasa Indonesia](../../id/docs/installation.md) · [Italiano](../../it/docs/installation.md) · [日本語](../../ja/docs/installation.md) · [한국어](../../ko/docs/installation.md) · [मराठी](../../mr/docs/installation.md) · [فارسی](../../fa/docs/installation.md) · [Polski](../../pl/docs/installation.md) · [Português](../../pt/docs/installation.md) · [ਪੰਜਾਬੀ](../../pa/docs/installation.md) · [Română](../../ro/docs/installation.md) · [Русский](../../ru/docs/installation.md) · [Español](../../es/docs/installation.md) · [Kiswahili](../../sw/docs/installation.md) · [Svenska](../../sv/docs/installation.md) · [தமிழ்](../../ta/docs/installation.md) · [ไทย](../../th/docs/installation.md) · [Türkçe](../../tr/docs/installation.md) · [Українська](../../uk/docs/installation.md) · [اردو](../../ur/docs/installation.md) · [Tiếng Việt](../../vi/docs/installation.md)

[Translation policy](../../README.md)

</details>
<!-- nv-language-navigation:end -->

<!-- nv-translation-notice:start -->
> Maschinell unterstützte Übersetzung aus dem Englischen. Technische Namen, Befehle, URLs und ursprüngliche Rechtstexte bleiben erhalten. Eine Rezension durch einen Muttersprachler ist willkommen; Konsultieren Sie die englische Referenz, wenn der Wortlaut unklar ist.
<!-- nv-translation-notice:end -->

<a id="installation-guide"></a>
# Installationsanleitung

Beginnen Sie mit [Downloads](downloads.md), das den Veröffentlichungsstatus und die genauen Asset-Namen aufzeichnet. Dies sind separate Tools: Installieren Sie nur die, die Sie benötigen.

> **Für NVRasterPulse installieren Sie [RTSS von Guru3D](https://www.guru3d.com/download/rtss-rivatuner-statistics-server-download/), bevor Sie den Profilmanager öffnen.**
> RTSS muss ausgeführt werden, um Grenzwerte anzuwenden. Es ist nicht in NV Tools enthalten.

| Werkzeug | Installierte Edition | Tragbare Ausgabe | Hauptvoraussetzung |
| --- | --- | --- | --- |
| NVIDIA Profile Inspector – NV Tools Fork | NVPI-CustomNV-3.0.2.3-Setup-r2.exe | Extrahieren Sie die vollständige NVPI-ZIP-Datei | NVIDIA-Treiber und .NET Framework 4.8 |
| NVDriverForge | NVDriverForge-Setup.exe | NVDriverForge.exe, Laufzeit inklusive | Kompatibles Original-Treiberpaket NVIDIA für Installationsvorgänge |
| NVMFG Unlock40 | NVMFGUnlock40-0.2.3-Setup-x64.exe | Extrahieren Sie die vollständige NVMFG-ZIP-Datei und behalten Sie die Unterordner bei | RTX 40, vorhandener DLSS FG, genauer Anbieter und .NET Framework 4.8-Helfer |
| NVRasterPulse | NVRasterPulse-0.2-win-x64-Setup.exe | Extrahieren Sie die vollständige RP-ZIP-Datei | RTSS und .NET Framework 4.8 |

<a id="download-verify-install"></a>
## Herunterladen, überprüfen, installieren

1. Laden Sie für die ausgewählte veröffentlichte Version das benannte Anwendungs-Asset, die Hinweise ZIP und SHA256SUMS.txt herunter.
2. Verwenden Sie [SHA-256-Beispiel](downloads.md#sha-256) mit dem tatsächlich heruntergeladenen Dateinamen.
3. Befolgen Sie für die Einrichtung das normale Installationsprogramm. Extrahieren Sie für tragbares ZIP alles in einen neuen lokalen beschreibbaren Ordner. Führen Sie nicht innerhalb der ZIP-Datei aus.
4. Öffnen Sie die EXE-Datei der Anwendung. Bewahren Sie die zugehörigen Lizenz-/Konfigurations-/Datendateien auf.
5. Lesen Sie die Gebrauchsanweisung dieses Tools, bevor Sie Einstellungen oder Systemvorgänge aktivieren.

Aktuelle Binärdateien sind nicht signiert. Ein passender Hash bestätigt die erwarteten Bytes; Es handelt sich nicht um ein Sicherheits- oder Kompatibilitätszertifikat. Deaktivieren Sie den Windows-Sicherheitsschutz nicht, nur um eine Warnung zu unterdrücken.

Die Installation von NVDF oder seinem optionalen NVPI-Begleiter erfolgt unabhängig von der Installation eines GPU-Treibers. Der NVPI-Begleiter behält seinen bestehenden internen Installationsnamen. Die erhöhte RasterPulse-Taste erfordert eine geschützte systemweite Installation. Andere RP-Kopien können über ihre eigenen Verknüpfungen geöffnet werden.

NVMFG ist experimentell und verfügt über den [dokumentierte NVIDIA SDK Lizenzreserve](provenance.md). Es ist kein NVIDIA-Treiber, kein NGX-Anbieter/-Modell oder eine Streamline-Laufzeitumgebung für das Spiel enthalten. Ausgewählte SDK-Downloads und Spielaktualisierungen sind explizite separate Vorgänge.

<a id="language-and-updates"></a>
## Sprache und Updates

Verwenden Sie zur Dokumentation die 34-Sprachen-Auswahl der README-Datei. NVDF, NVMFG und RP verfügen über ihre eigene 34-sprachige UI-Einstellung; NVPI behält seine bestehende Sprachunterstützung. Einige technische Zeichenfolgen des Installationsprogramms werden auf Englisch zurückgesetzt.

Behalten Sie beim Aktualisieren die Installationsidentität eines Tools bei. Schließen Sie es zuerst und bewahren Sie Backups auf. Schließen Sie bei NVMFG die betroffenen Spiele und beheben Sie die ausstehende Profilwiederherstellung. Verwenden Sie für portable Updates einen neuen Ordner, anstatt Releases zu kombinieren.

<a id="removing-a-tool"></a>
## Entfernen eines Werkzeugs

Durch die Deinstallation einer Anwendung werden ihre Einstellungen nicht automatisch rückgängig gemacht.

- **NVPI:** Stellen Sie bei Bedarf die beabsichtigten Profile/Anzeigeeinstellungen vor dem Entfernen wieder her.
- **NVDF:** Verwenden Sie zuerst die Wiederherstellung, wenn Sie erweiterte/NVENC-Änderungen wiederherstellen möchten. Uninstall verlässt den Grafiktreiber, die Einstellungen und Backups.
- **NVMFG:** Spiele schließen, Controller deaktivieren/beenden, NVIDIA-Wiederherstellung durchführen und gewünschte SDK-Backups des Spiels vor dem Entfernen wiederherstellen.
- **RP:** Entfernen Sie zuerst die vorgesehenen Limiter-Überschreibungen. Uninstall löscht keine gespeicherten RTSS-Kappen und entfernt auch nicht RTSS.

Genaue Datenspeicherorte und Einschränkungen finden Sie in jedem [Projektleitfaden](../README.md#projects) oder in [Unterstützung](support.md), wenn ein Wiederherstellungsschritt fehlschlägt.
