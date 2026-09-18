<!-- nv-language-navigation:start -->
🌐 [English](../../../provenance.md) | [Français](../../../provenance.fr.md) · [NV Laboratory](../README.md)

<details>
<summary>🌐 Language · 34</summary>

[العربية](../../ar/docs/provenance.md) · [বাংলা](../../bn/docs/provenance.md) · [简体中文](../../zh/docs/provenance.md) · [Čeština](../../cs/docs/provenance.md) · [Dansk](../../da/docs/provenance.md) · [Nederlands](../../nl/docs/provenance.md) · [English](../../../provenance.md) · [Filipino](../../fil/docs/provenance.md) · [Suomi](../../fi/docs/provenance.md) · [Français](../../../provenance.fr.md) · **Deutsch** · [Ελληνικά](../../el/docs/provenance.md) · [हिन्दी](../../hi/docs/provenance.md) · [Magyar](../../hu/docs/provenance.md) · [Bahasa Indonesia](../../id/docs/provenance.md) · [Italiano](../../it/docs/provenance.md) · [日本語](../../ja/docs/provenance.md) · [한국어](../../ko/docs/provenance.md) · [मराठी](../../mr/docs/provenance.md) · [فارسی](../../fa/docs/provenance.md) · [Polski](../../pl/docs/provenance.md) · [Português](../../pt/docs/provenance.md) · [ਪੰਜਾਬੀ](../../pa/docs/provenance.md) · [Română](../../ro/docs/provenance.md) · [Русский](../../ru/docs/provenance.md) · [Español](../../es/docs/provenance.md) · [Kiswahili](../../sw/docs/provenance.md) · [Svenska](../../sv/docs/provenance.md) · [தமிழ்](../../ta/docs/provenance.md) · [ไทย](../../th/docs/provenance.md) · [Türkçe](../../tr/docs/provenance.md) · [Українська](../../uk/docs/provenance.md) · [اردو](../../ur/docs/provenance.md) · [Tiếng Việt](../../vi/docs/provenance.md)

[Translation policy](../../README.md)

</details>
<!-- nv-language-navigation:end -->

<!-- nv-translation-notice:start -->
> Maschinell unterstützte Übersetzung aus dem Englischen. Technische Namen, Befehle, URLs und ursprüngliche Rechtstexte bleiben erhalten. Eine Rezension durch einen Muttersprachler ist willkommen; Konsultieren Sie die englische Referenz, wenn der Wortlaut unklar ist.
<!-- nv-translation-notice:end -->

<a id="provenance-changes-and-licensing"></a>
# Provenienz, Änderungen und Lizenzierung

Dieses Audit beschreibt die am **18.09.2026** vorbereiteten Kandidaten. Anwendungsquellen bleiben privat; Die öffentlichen Inventare enthalten Dateinamen und Hashes, keinen Quellcode. Siehe [Vollständige Komponentenhinweise](../THIRD_PARTY_NOTICES.md).

<a id="nvidia-profile-inspector--nv-tools-fork"></a>
## NVIDIA Profile Inspector – NV Tools Fork

Referenz: Orbmu2k/nvidiaProfileInspector commit `592d962cca8827efe8859461a84267755595064a`; Ausführbare Kandidatenversion 3.0.2.3. Das Referenz-Commit und die Assembly-Version von fork sind unterschiedliche Bezeichner. Aus der fork-Version wird keine Upstream-Release-Version abgeleitet.

Die 157 Quell-/Ressourcendateien des sauberen Begleiters wurden mit diesem Commit verglichen: 2 Byte identisch, 134 unterschieden sich nur in Zeilenenden oder UTF-8-BOM, 11 geändert, 10 fehlten im verglichenen Upstream-Pfad. „Hinzugefügt“ bezieht sich auf diesen Pfad und ist an sich kein Beweis für die ursprüngliche Urheberschaft.

[Vollständiger Datei-/Hash-Vergleich](../../../provenance/nvpi-source-provenance.json).

| Bereich | Geerbte Arbeit | Fork-Beitrag |
| --- | --- | --- |
| Profileditor | Profilmodell, Import/Export, Anwendungszuordnungen und Referenzdaten | Integration mit Screen und dem externen Tool-Launcher |
| NVAPI | DRS-Interop von Orbmu2k | Farb-/anzeigebezogene Interoperabilität, Einschränkungen beim nativen Laden in der Produktion und Mock-Entfernung |
| Anzeigedienste | Windows/NVIDIA-APIs als externe Schnittstellen | DisplayInfoService, DisplayConfigurationService, DisplaySettingsBackend |
| Benutzeroberfläche | Vorgelagerte WPF-Ressourcen, Paletten und Symbole | Bildschirmdialoge, 15-Sekunden-Bestätigung, Status/Rücklesen und Symbolleistenlayout |
| Launcher | Vorhandene App-Shell | Geschützte, separat installierte RasterPulse-Suche und -Start |
| Verpackung | MIT Upstream | Sauberer eigenständiger Begleiter, separater Installer/Deinstaller, gespeicherte Hinweise |

Die öffentliche Quellkarte enthält Lösungs-/Ressourcenpfade zur Rückverfolgbarkeit; Diese Dateien werden nicht als Quelle verteilt. Entwicklungstests, Scheinschnittstellen und die alte kombinierte NVPI/RasterPulse-Binärdatei sind ausgeschlossen.

<a id="nvdriverforge"></a>
## NVDriverForge

Unabhängige C#/.NET 8/WPF-Anwendung; Der benutzerorientierte Workflow ist teilweise von NVCleanstall inspiriert. In der Produktionsnutzlast wurde keine NVCleanstall-Quelle/Binärdatei identifiziert. Es wird nicht als fork dieser proprietären Anwendung dargestellt.

Die ursprüngliche Projektarbeit umfasst Komponentenanalyse/-auswahl, geschützte Installationsjobs, Backups und Transaktionswiederherstellung, Downloads des NVIDIA-Katalogs, Aktualisierungsprüfungen, lokalisierte Erklärungen, optionale erweiterte/NVENC-Workflows und Installer-Bootstrap.

Geerbte/angepasste Komponenten: vier NVPI-Themenpaletten, erweiterte NVAPI-DRS-Schnittstellenreferenz und der separat optionale MIT NVPI-Begleiter. Die Auswahl-Benutzeroberfläche der Voreinstellung Custom NV und die Integration zugelassener Transaktionen gehören zu NVDriverForge; Bei der Voreinstellung handelt es sich nicht um eine offizielle NVIDIA-Empfehlung.

7-Zip 26.03, .NET/WPF 8.0.31 und Inno Setup bleiben unveränderte externe Komponenten, die unter ihren eigenen Bedingungen verwendet werden. keylase NVENC-Daten sind nicht eingebettet; Es wird ein exakter Commit ausgewählt und überprüft, wenn der Benutzer einen kompatiblen Download anfordert. Für diese Upstream-Daten wurde keine Weiterverbreitungslizenz eingerichtet.

<a id="nvmfg-unlock40"></a>
## NVMFG Unlock40

NVMFG Unlock40 wurde unabhängig von 禅堂 Zendo (RevoluSound Team) entwickelt. Der Betreuer verwendete RTX40MFG-Unlock zum Vergleich und zur Verfeinerung. Die Anwendung als Ganzes wird nicht als fork dargestellt. Durch diese Unterscheidung werden Credits für gemeinsam genutzte/angepasste Komponenten in der aktuellen nativen Ebene nicht entfernt.

Vergleichsreferenz: dashdogy/RTX40MFG-Unlock, Michael Robles, MIT, Commit `4e776d068f91b4a665425542bb005dd57cc3d891`. Der private Native-Engine-Baum enthält 48 verglichene Dateien: 35 reine Formatierungsunterschiede, 4 geänderte Dateien und 9 fehlen im Referenzpfad. [Vollständiger Vergleich](../../../provenance/nvmfg-source-provenance.json).

Geänderte geerbte Dateien: `entry_detour.h`, `patcher.cpp`, `temporal_interval_trace.cpp`, `temporal_interval_trace.h`. Zu den zusätzlichen Pfaden gehören `game_selection.*`, `ngx_bootstrap.*`, `ngx_capability.h`, `presentation_tracker.h`, `vsync_observer.*` und eine beibehaltene Upstream-Lizenz.

Produktions-C++-Einheiten: Patcher, midpoint_fix, dlssg_provider_policy, entry_detour, nvidia_mfg_policy, temporal_interval_trace, ngx_bootstrap, game_selection und vsync_observer; plus entry_detour-Baugruppe und MinHook-Puffer/Haken/Trampolin/HDE64. Das geerbte ReShade-Frontend, die alten Shim-Ressourcen und ungenutzten CMake-Ziele sind nicht Teil dieser Produktionskompilierung.

Die passenden Komponenten umfassen Patching/Provider-Richtlinie und zeitliche Arbeit; Ihre Urheberrechts- und Genehmigungshinweise bleiben intakt. Die zentrale NGX/Bootstrap/Controller-Koordination, die V-Sync-Verarbeitung pro Spiel, die Sitzungsdiagnose und der Windows-Anwendungs-/SDK/Backup-Workflow sind Projektarbeit von 禅堂 Zendo (RevoluSound Team). Die oben genannten Zahlen beziehen sich auf Dateien, einschließlich Dateien Dritter und ungenutzter Dateien, nicht auf den Prozentsatz der Urheberschaft oder die Chronologie der Projektidee.

Der Helfer passt NvapiDrsWrapper und NativeArrayHelper von NVPI in eine separate Assembly mit vom Projekt erstellter Profillogik an. Der alte Entwicklungs-Mock-Pfad ist ausgeschlossen. Gemeinsam genutzte Familienpaletten stammen aus NVPI.

MinHook-Referenz: `8fda4f5481fed5797dc2651cd91e238e9b3928c6`; Die geerbte kompilierte Teilmenge weist im Vergleich keine funktionalen lokalen Änderungen auf. Streamline-Integrationsheader: 2.12; Open-Header-Lizenz verifiziert bei v2.12.0. NGX-Header-Quelle: NVIDIA/DLSS `a291cc7d2cc642a51566f3dfd5376f635cd1b284` festschreiben.

Kandidaten-Engine SHA-256: `C793770D329B99CD9C5C640317CE435BFE353CA2868E36CF5DCD4D5295EFAE13`.

Erforderlicher Anbieter SHA-256 in engine.json: `C64928FDB7C48A57722EA8EEF2662171EDC323473ADEA66C29A206A23F1A2BED`. Eine gemeldete 310.9-Anbieterfamilie ist nicht mit genau diesem Hash austauschbar. Es ist keine Anbieter-DLL oder kein Modell enthalten.

**Herausragender Lizenzierungspunkt:** Die vollständige NVIDIA RTX SDK-Lizenz, Version 14. März 2024, enthält eine Einschränkung in Abschnitt 4(d), die für die Umgehung technischer Einschränkungen relevant ist. Die Prüfung stellt keine Genehmigung für diese Verwendung dar. Die Beibehaltung der MIT-Engine-Lizenz, die kostenlose Nutzung oder die Beachtung anderer Mods lösen diesen separaten Zustand nicht. Die Kandidatenvorbereitung ist keine rechtliche Freigabe. Die ursprüngliche Kurzmitteilung wird durch die vollständige Lizenz ergänzt; Sein Windows-1252-Text wird auch als lesbares UTF-8 bereitgestellt, wobei die Originalbytes beibehalten werden.

Der native Vergleich wurde für 0.2.3 neu berechnet: dieselben 48 Dateien und Klassifizierungen. Seit der letzten Prüfung haben sich `game_selection.cpp`, `game_selection.h` und `patcher.cpp` für Aktivitäts-/Fähigkeitsbeobachtungen geändert. Zur Betreueranwendung gehören neue Bibliotheks-, Diagnose-, Präferenz-, Aktualisierungs- und Auswahl-Workflows. Komponentenlizenzen und der erforderliche Provider-Hash bleiben unverändert.

<a id="nvrasterpulse"></a>
## NVRasterPulse

Unabhängiger RTSS-Profilmanager, entwickelt im von NVPI abgeleiteten Repository. Die geerbten MIT-UI-Ressourcen/Paletten und der Projektursprung bleiben gutgeschrieben. Die Produktions-App verwendet explizit die bereitgestellte MIT-Lizenz.

Projektarbeit: Präzises RTSS-Profil-Parsing/-Schreiben und fraktionierte Codierung, Backups, Override-Entfernung, Neuladebrücke, Voraussetzungserkennung, kompakte Benutzeroberfläche, Tray-Lebenszyklus, Startkontrollen und Lokalisierung. RTSS führt die eigentliche Begrenzung durch.

Es ist keine RTSS-Quelle, Hook-DLL, SDK oder Installationsprogramm enthalten. Die Bridge ruft den Export in einer vorhandenen, vom Benutzer ausgewählten RTSS-Installation auf. Dieses Paket enthält kein NVIDIA-Treiberpaket, keinen nativen experimentellen Limiter, keinen Framepacer, keine MinHook-, ReShade- oder DLSS-Laufzeitumgebung.

<a id="assets-generated-data-and-tools"></a>
## Assets, generierte Daten und Tools

[Vermögensgutschriften](../assets/README.md) identifiziert die vorhandenen Schnittstellenvorschauen und den NVPI-Setup-Selektor. Die darin enthaltenen fiktiven Werte sind beschriftet. Es werden keine Spiel-/Nexus-Assets, persönlichen Profile, privaten ICC-, Unternehmens-NVIDIA-Logos oder Schriftartdateien kopiert.

Generierte Spielkompatibilitätsnamen, die in NVMFG geerbt werden, dienen als Erkennungshilfe und nicht als Testbeweis. Generierte Installationskataloge werden in [Hinweise des Übersetzers](../../../../licenses/INSTALLER-TRANSLATORS.md) gutgeschrieben. Generierte Build-Datensätze mit absoluten Pfaden bleiben privat.

Zu den privaten Build-Tools gehören .NET SDK/MSBuild, Visual Studio C++/MASM, Windows SDK, PowerShell, Inno Setup und Python-Prüfskripte. Ihre Compiler, Header, Testläufer und Debug-Assets werden nicht verteilt. Für die statische Freigabe von CRT gelten weiterhin die geltenden Toolchain-Bedingungen von Microsoft.

<a id="scope-of-verification"></a>
## Umfang der Überprüfung

Die lokale Prüfung hat alle Dateien in den drei Entwicklungsstämmen inventarisiert und dabei Git-Objektdatenbanken und verknüpfte Verzeichnisziele ausgeschlossen. Aktive Quelle/Dokumente wurden gescannt; Historische Gebäude wurden inventarisiert und ausgeschlossen. Ausgewählte Postleitzahlen und aktuelle Nutzlasten wurden gescannt und gehasht; Die .NET-Bundles wurden zur weiteren Überprüfung dekomprimiert. Bei dieser ersten Prüfung wurden weder Produkte noch Installationsprogramme, Spiele, RTSS-Prozesse oder Treiber ausgeführt.

Die spätere NVPI-Setup-Revision 2 behebt die eigenständige Sprachauswahl mithilfe der gemeinsam genutzten Inno-Steuerelemente und des Bootstrap. Helle/dunkle private Geräte überprüften die Maus- und Tastaturnavigation und alle 34 expliziten Sprachcodes. Der eigentliche Setup-Selektor wurde auf einem nie angezeigten privaten Desktop geöffnet und vor der Installation abgebrochen. Die sieben Anwendungsdateien und die tragbare ZIP-Datei bleiben unverändert. NVDriverForge 0.1.3 schließt den korrigierten Begleiter ein und leitet `/LANG` weiterhin weiter.

NVDriverForge 0.1.3 wurde am 10.09.2026 fertiggestellt. Im privaten Verifizierungsbericht werden 366 Anwendungstests, 118 Companion-Checks, 32 Setup-Checks, 156 native Vergleiche und 34 Sprachweiterleitungsfälle erfasst. Der Fix für die geschützte Komponentenauswahl wurde mit einem ursprünglichen Treiberpaket wiederholt, ohne dessen Nutzlast zu ändern oder den Treiber zu installieren. Hierbei handelt es sich um datierte Ergebnisse des Produktteams, nicht um Tests, die durch dieses Dokumentationsupdate wiederholt werden, oder um den Nachweis einer erfolgreichen echten Treiberinstallation.

Dieses Hub-Update ändert keinen funktionalen Anwendungscode. Frühere Anwendungs-Build-/Unit-/UI-Tests bleiben veraltete historische Beweise. Dabei handelt es sich nicht um ein vollständiges Reverse Engineering aller Drittanbieter-Binärdateien oder um eine Garantie gegen jedes mögliche geheime Muster.

Aktualisierung vom 18. September 2026: NVDriverForge 0.1.4 fügt Bereitschaftsprüfungen, native Profilsicherung, Komponentenanleitung, Einstellungen und Kits, detaillierte Ergebnisse, lokale Berichterstattung und Anwendungsaktualisierungen hinzu. NVRasterPulse 0.2 fügt Konfigurationsdiagnose, FPS-Anleitung, Pause/Fortsetzung, Rückgängigmachen, `.nvrp`-Profile und Favoriten/Ausblenden hinzu, ohne eine neue Limiter-Engine. Einzelne Anleitungen beschreiben die Nutzung und Grenzen. Statische Hub-Prüfungen sind getrennt von den Anwendungstests, die in den privaten Berichten vom 18. September aufgezeichnet wurden; Für diesen Hub wurde keine Treiberinstallation, kein echter Profilimport oder keine Latenzmessung durchgeführt.
