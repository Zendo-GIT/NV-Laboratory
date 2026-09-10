<!-- nv-language-navigation:start -->
🌐 [English](../../../support.md) | [Français](../../../support.fr.md) · [NV Laboratory](../README.md)

<details>
<summary>🌐 Language · 34</summary>

[العربية](../../ar/docs/support.md) · [বাংলা](../../bn/docs/support.md) · [简体中文](../../zh/docs/support.md) · [Čeština](../../cs/docs/support.md) · [Dansk](../../da/docs/support.md) · [Nederlands](../../nl/docs/support.md) · [English](../../../support.md) · [Filipino](../../fil/docs/support.md) · [Suomi](../../fi/docs/support.md) · [Français](../../../support.fr.md) · **Deutsch** · [Ελληνικά](../../el/docs/support.md) · [हिन्दी](../../hi/docs/support.md) · [Magyar](../../hu/docs/support.md) · [Bahasa Indonesia](../../id/docs/support.md) · [Italiano](../../it/docs/support.md) · [日本語](../../ja/docs/support.md) · [한국어](../../ko/docs/support.md) · [मराठी](../../mr/docs/support.md) · [فارسی](../../fa/docs/support.md) · [Polski](../../pl/docs/support.md) · [Português](../../pt/docs/support.md) · [ਪੰਜਾਬੀ](../../pa/docs/support.md) · [Română](../../ro/docs/support.md) · [Русский](../../ru/docs/support.md) · [Español](../../es/docs/support.md) · [Kiswahili](../../sw/docs/support.md) · [Svenska](../../sv/docs/support.md) · [தமிழ்](../../ta/docs/support.md) · [ไทย](../../th/docs/support.md) · [Türkçe](../../tr/docs/support.md) · [Українська](../../uk/docs/support.md) · [اردو](../../ur/docs/support.md) · [Tiếng Việt](../../vi/docs/support.md)

[Translation policy](../../README.md)

</details>
<!-- nv-language-navigation:end -->

<!-- nv-translation-notice:start -->
> Maschinell unterstützte Übersetzung aus dem Englischen. Technische Namen, Befehle, URLs und ursprüngliche Rechtstexte bleiben erhalten. Eine Rezension durch einen Muttersprachler ist willkommen; Konsultieren Sie die englische Referenz, wenn der Wortlaut unklar ist.
<!-- nv-translation-notice:end -->

<a id="compatibility-and-troubleshooting"></a>
# Kompatibilität und Fehlerbehebung

Dies sind die vorbereiteten Kandidaten, keine Zertifizierungsmatrix für alle Windows-, GPU-, Treiber- und Spielkombinationen.

| Werkzeug | Windows / Laufzeit | Hardware-/externe Abhängigkeit | Pflegebedürftige Operationen |
| --- | --- | --- | --- |
| NVPI fork 3.0.2.3 | Windows 10/11 x64, .NET Framework 4.8 | Kompatibler NVIDIA-Treiber/Display | Profil schreibt und zeigt Vorschauen an |
| NVDriverForge 0.1.2 | Windows 10 Build 19041+ / 11 x64; .NET/WPF enthalten | Kompatibles NVIDIA-Treiberpaket | Erweiterte Installation, erweiterte Einstellungen, optionales NVENC |
| NVMFG Unlock40 0.1.1 | Windows 10/11 x64; .NET/WPF enthalten, Framework 4.8-Helfer | RTX 40, berechtigtes DLSS FG-Spiel und angehefteter Anbieter | Native In-Game-Patches, globales Profiljournal, SDK-Spielaktualisierungen |
| NVRasterPulse 0.1 | Windows 10/11 x64, .NET Framework 4.8 | RTSS installiert; Rennen um Länderspiele | RTSS Profiländerungen pro ausführbarer Datei |

Es ist kein ARM64-Paket vorbereitet. Die Verfügbarkeit von Display/API und alte Windows-Versionen können einzelne Funktionen einschränken. Es wurde keine universelle Mindestversion NVIDIA oder RTSS erfunden. Der genaue NVMFG-Anbieter-Hash befindet sich in [Herkunft](provenance.md).

<a id="before-reporting-a-bug"></a>
## Bevor Sie einen Fehler melden

Identifizieren Sie die genaue ausführbare Datei/Version, die Sie geöffnet haben. Eine zuvor installierte Kopie ist nicht unbedingt die Version einer neu heruntergeladenen ZIP-Datei. Notieren Sie die Reproduktionsschritte, das erwartete Ergebnis und das tatsächliche Ergebnis. Geben Sie bei Rendering-/Limitierungsproblemen die Spielversion, die Anzeigeaktualisierung, den FG/V-Sync/VRR-Status und alle anderen Limiter oder Overlays an.

Verwenden Sie [Fehlerform](https://github.com/Zendo-GIT/NV-Laboratory/issues/new?template=bug-report.yml). Hängen Sie niemals einen gesamten privaten Entwicklungsordner, ein Treiberarchiv, ein Modell, eine Spiele-DLL, einen Registry-Dump oder eine nicht überprüfte Protokollsammlung an.

| Problem | Erste Kontrollen |
| --- | --- |
| Falsche Anwendungsversion | Bestätigen Sie die EXE-Identität und den Release-Hash. Schließen Sie die ältere Kopie, bevor Sie sie ersetzen. |
| Laufzeit-/Startfehler | Installieren Sie das erforderliche Framework 4.8 oder behalten Sie alle bereitgestellten portablen Unterordner bei. |
| UAC abgebrochen | Versuchen Sie nur den beabsichtigten Vorgang. Abbruch ist keine erfolgreiche Installation. |
| Hash/Signatur-Konflikt | Hören Sie auf, diesen Kandidaten zu verwenden, und erhalten Sie die erwarteten offiziellen Bytes. |
| NVPI Farbe/Modus abgelehnt | Kehren Sie zurück und verwenden Sie eine Kombination, die vom tatsächlichen Display/Treiber unterstützt wird. |
| NVDF-Sicherungs- oder Wiederherstellungsfehler | Geschützten Job und RECOVERY.txt beibehalten; Löschen Sie das Tagebuch nicht und erzwingen Sie keine widersprüchlichen Schreibvorgänge. |
| Ausstehende NVMFG-Einstellungen | Beheben Sie die Wiederherstellung bei geschlossenen Spielen und bewahren Sie die Änderungen anderer Tools auf. |
| Die RP-Kappe hat keine Auswirkung | Führen Sie RTSS aus, identifizieren Sie die echte Spiel-EXE-Datei, überprüfen Sie den Hook-Status und die konkurrierenden Limits. |
| Die RP-Kappe bleibt nach dem Entfernen bestehen | Überprüfen Sie RTSS Global; Durch das Entfernen werden nur lokale Begrenzer außer Kraft gesetzt. |

<a id="logs-and-privacy"></a>
## Protokolle und Datenschutz

| Werkzeug | Lokale Daten zur Überprüfung, nicht zum vollständigen Hochladen |
| --- | --- |
| NVDF | `%LOCALAPPDATA%\NVDriverForge`; geschützte Jobs `%PROGRAMDATA%\NVDriverForge\Jobs` |
| NVMFG | `%LOCALAPPDATA%\RtxMfg`; Sicherungen `%LOCALAPPDATA%\NvidiaStreamlineMaintenance\Backups`; `Sessions` neben der EXE-Datei |
| RP | `%LOCALAPPDATA%\NVRasterPulse`; `Backups\RTSS` darunter |
| NVPI | Ihre gewählten Exporte und der angezeigte Fehler; Kein erfundener universeller Protokollpfad |

Entfernen Sie Kontonamen, Home-Verzeichnisse, Spielbibliothekspfade, Gerätekennungen, Token und nicht verwandte Fenster aus den Texten/Bildern, die Sie teilen. Bewahren Sie die Originale zur Wiederherstellung privat auf. Öffentliche Themen sind für jeden sichtbar.

Folgen Sie bei einer Sicherheitslücke, einem gefährlichen privilegierten Verhalten oder einem unbeabsichtigten destruktiven Vorgang [SECURITY.md](../SECURITY.md), anstatt Details öffentlich zu veröffentlichen.

<a id="what-has-been-verified"></a>
## Was wurde überprüft

Zur Hub-Vorbereitung wurden statische Payload-/ZIP-/Hash-/Metadaten-Scans und Dokumentationsprüfungen durchgeführt. Bestehende private Anwendungs-Build-/Unit-/UI-Tests sind historische, datierte Beweise. Im Rahmen dieser Vorbereitung wurde keine Treiberinstallation, Anzeigeänderung, Live-RTSS-Operation oder Spiele-Benchmark durchgeführt.

„Erkannt“, „geschrieben“, „nachgeladen“, „Fähigkeit verfügbar“ und „im Spiel gemessen“ sind unterschiedliche Ergebnisse. Melden Sie, welches Sie beobachtet haben.
