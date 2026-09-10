<!-- nv-language-navigation:start -->
🌐 [English](../../../development.md) | [Français](../../../development.fr.md) · [NV Laboratory](../README.md)

<details>
<summary>🌐 Language · 34</summary>

[العربية](../../ar/docs/development.md) · [বাংলা](../../bn/docs/development.md) · [简体中文](../../zh/docs/development.md) · [Čeština](../../cs/docs/development.md) · [Dansk](../../da/docs/development.md) · [Nederlands](../../nl/docs/development.md) · [English](../../../development.md) · [Filipino](../../fil/docs/development.md) · [Suomi](../../fi/docs/development.md) · [Français](../../../development.fr.md) · **Deutsch** · [Ελληνικά](../../el/docs/development.md) · [हिन्दी](../../hi/docs/development.md) · [Magyar](../../hu/docs/development.md) · [Bahasa Indonesia](../../id/docs/development.md) · [Italiano](../../it/docs/development.md) · [日本語](../../ja/docs/development.md) · [한국어](../../ko/docs/development.md) · [मराठी](../../mr/docs/development.md) · [فارسی](../../fa/docs/development.md) · [Polski](../../pl/docs/development.md) · [Português](../../pt/docs/development.md) · [ਪੰਜਾਬੀ](../../pa/docs/development.md) · [Română](../../ro/docs/development.md) · [Русский](../../ru/docs/development.md) · [Español](../../es/docs/development.md) · [Kiswahili](../../sw/docs/development.md) · [Svenska](../../sv/docs/development.md) · [தமிழ்](../../ta/docs/development.md) · [ไทย](../../th/docs/development.md) · [Türkçe](../../tr/docs/development.md) · [Українська](../../uk/docs/development.md) · [اردو](../../ur/docs/development.md) · [Tiếng Việt](../../vi/docs/development.md)

[Translation policy](../../README.md)

</details>
<!-- nv-language-navigation:end -->

<!-- nv-translation-notice:start -->
> Maschinell unterstützte Übersetzung aus dem Englischen. Technische Namen, Befehle, URLs und ursprüngliche Rechtstexte bleiben erhalten. Eine Rezension durch einen Muttersprachler ist willkommen; Konsultieren Sie die englische Referenz, wenn der Wortlaut unklar ist.
<!-- nv-translation-notice:end -->

<a id="repository-architecture-and-maintenance"></a>
# Repository-Architektur und -Wartung

NV Laboratory ist ein öffentlicher **Dokumentations- und Binärverteilungs-Hub**. Es enthält keine Anwendungsquelle. Die vier Projekte behalten separate Build-Bäume, Versionen, Identitäten und Release-Assets bei. Ihr privater Entwicklungsverlauf wird nicht in dieses Git-Repository importiert.

<a id="layout"></a>
## Layout

| Standort | Zweck |
| --- | --- |
| README.md / README.fr.md | Englische/Französische Einstiegspunkte |
| Vier Projektordner | Vollständige Anleitungen und entsprechende Originalmitteilungen |
| Dokumente | Downloads, Kompatibilität, Herkunft, Entwicklungs- und Veröffentlichungsverfahren |
| docs/releases.json | Geprüfte Kandidaten-/Release-Metadaten, Größen und Hashes |
| Dokumente/Herkunft | Datei-/Hash-Vergleiche; kein Anwendungscode |
| Lizenzen | Vollständige Texte von Drittanbietern und Credits des Installateur-Übersetzers wurden geteilt |
| Vermögenswerte | Vorhandene überprüfte UI-Vorschauen und ihre Herkunft |
| .github | Ausgabeformulare und schreibgeschützte Dokumentationsvalidierung |
| tools/validate_repository.py | Überprüfung der Publikationsgrenzen und Links in der Standardbibliothek |

Englisch bleibt die Standardeinstellung. GitHub README. Bestehende benachbarte `.fr.md`-Links bleiben gültig. Zusätzliche Übersetzungen spiegeln die Dokumentation unter `docs/languages/<code>` wider; Die Sprachauswahl behält beim Wechseln der Sprache die gleiche Seite bei. Der Katalog `docs/languages/catalog.json` erfasst alle 34 Sprachen und Quell-Fingerprints. GitHub wählt nicht automatisch eine README-Datei nach Browsersprache aus. Siehe [Sprachindex und Übersetzungspolitik](../../README.md).

<a id="application-technologies"></a>
## Anwendungstechnologien

| Programm | Private Technologie | Verteilung |
| --- | --- | --- |
| NVPI fork | C#, WPF, .NET Framework 4.8, NVAPI/Windows Interop | Vollständiger tragbarer Ordner und separater Inno Setup |
| NVDriverForge | C#, WPF, .NET 8; nativer C++-Bootstrap; 7-Zip-Prozess | Eigenständige tragbare EXE-Datei und Setup |
| NVMFG Unlock40 | C#/WPF .NET 8, Framework 4.8-Helfer, C++20/MASM/MinHook-Engine | Tragbarer Baum und Einrichtung |
| NVRasterPulse | C#/WPF Framework 4.8; RTSS-Profil-/Neuladeintegration; nativer Bootstrap | Tragbarer Baum und Einrichtung |

Dieser öffentliche Checkout kann die Anwendungen nicht neu erstellen. Automatische „Source code“-Archive sind Hub-Snapshots. Upstream-Quellenlinks stellen nicht die exakte private geänderte Quelle dar. Das öffentliche CI validiert nur dieses Repository.

<a id="local-checks"></a>
## Lokale Kontrollen

Aus dem Repository-Stammverzeichnis:

```text
python tools/validate_repository.py
```

Python 3.10 oder neuer ist ausreichend. Die Prüfung liest Dateien, lokale Markdown-Links, erforderliche Hinweise/RTSS-Links, Release-Metadaten und Veröffentlichungsgrenzen. Es führt keine Software aus, installiert keine Abhängigkeiten und kontaktiert kein Netzwerk.

Der GitHub-Workflow führt dieselbe Prüfung mit der Berechtigung zum schreibgeschützten Inhalt bei Push, Pull-Anfrage oder manuellem Versand aus. Der Checkout ist an einen überwachten Commit angeheftet und speichert keine Anmeldeinformationen. Es ist kein Release- oder Bereitstellungsjob konfiguriert.

<a id="maintain-the-boundary"></a>
## Behalten Sie die Grenze bei

Aktualisieren Sie die englische Referenz, die französischen Leitfäden und die betroffenen Übersetzungen gemeinsam. Halten Sie inhaltliche Änderungen von reinen Formatierungsvergleichen getrennt. Erfassen Sie tatsächliche Kandidaten-Hashes, Upstream-Commit-Referenzen und Lizenzen. Schließen Sie niemals aus der Beliebtheit eines Projekts eine Lizenz ab.

Verwenden Sie neu versionierte Release-Assets und überprüfen Sie geänderte Binärdateien, Archive und eingebettete Hinweise erneut. Bewahren Sie private Backups außerhalb dieses Repositorys auf. Verwenden Sie keinen öffentlichen Workflow, um private Anwendungsquellen oder lokale Build-Ordner zu importieren.

Für eine funktionale Anwendungsänderung geeignete Tests werden im privaten Projekt ausgeführt. Führen Sie keine Treiberinstallationsprogramme erneut aus und schreiben Sie keine echten Profile für ein Dokumentationsupdate. [Manuelles Freigabeverfahren](releasing.md).
