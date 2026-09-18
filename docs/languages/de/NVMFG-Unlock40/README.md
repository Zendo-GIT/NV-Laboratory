<!-- nv-language-navigation:start -->
🌐 [English](../../../../NVMFG-Unlock40/README.md) | [Français](../../../../NVMFG-Unlock40/README.fr.md) · [NV Laboratory](../README.md)

<details>
<summary>🌐 Language · 34</summary>

[العربية](../../ar/NVMFG-Unlock40/README.md) · [বাংলা](../../bn/NVMFG-Unlock40/README.md) · [简体中文](../../zh/NVMFG-Unlock40/README.md) · [Čeština](../../cs/NVMFG-Unlock40/README.md) · [Dansk](../../da/NVMFG-Unlock40/README.md) · [Nederlands](../../nl/NVMFG-Unlock40/README.md) · [English](../../../../NVMFG-Unlock40/README.md) · [Filipino](../../fil/NVMFG-Unlock40/README.md) · [Suomi](../../fi/NVMFG-Unlock40/README.md) · [Français](../../../../NVMFG-Unlock40/README.fr.md) · **Deutsch** · [Ελληνικά](../../el/NVMFG-Unlock40/README.md) · [हिन्दी](../../hi/NVMFG-Unlock40/README.md) · [Magyar](../../hu/NVMFG-Unlock40/README.md) · [Bahasa Indonesia](../../id/NVMFG-Unlock40/README.md) · [Italiano](../../it/NVMFG-Unlock40/README.md) · [日本語](../../ja/NVMFG-Unlock40/README.md) · [한국어](../../ko/NVMFG-Unlock40/README.md) · [मराठी](../../mr/NVMFG-Unlock40/README.md) · [فارسی](../../fa/NVMFG-Unlock40/README.md) · [Polski](../../pl/NVMFG-Unlock40/README.md) · [Português](../../pt/NVMFG-Unlock40/README.md) · [ਪੰਜਾਬੀ](../../pa/NVMFG-Unlock40/README.md) · [Română](../../ro/NVMFG-Unlock40/README.md) · [Русский](../../ru/NVMFG-Unlock40/README.md) · [Español](../../es/NVMFG-Unlock40/README.md) · [Kiswahili](../../sw/NVMFG-Unlock40/README.md) · [Svenska](../../sv/NVMFG-Unlock40/README.md) · [தமிழ்](../../ta/NVMFG-Unlock40/README.md) · [ไทย](../../th/NVMFG-Unlock40/README.md) · [Türkçe](../../tr/NVMFG-Unlock40/README.md) · [Українська](../../uk/NVMFG-Unlock40/README.md) · [اردو](../../ur/NVMFG-Unlock40/README.md) · [Tiếng Việt](../../vi/NVMFG-Unlock40/README.md)

[Translation policy](../../README.md)

</details>
<!-- nv-language-navigation:end -->

<!-- nv-translation-notice:start -->
> Maschinell unterstützte Übersetzung aus dem Englischen. Technische Namen, Befehle, URLs und ursprüngliche Rechtstexte bleiben erhalten. Eine Rezension durch einen Muttersprachler ist willkommen; Konsultieren Sie die englische Referenz, wenn der Wortlaut unklar ist.
<!-- nv-translation-notice:end -->

<a id="nvmfg-unlock40"></a>
# NVMFG Unlock40

**Experimentelles NVIDIA Multi Frame Generation für GeForce RTX 40, mit zentralem Controller und Auswahlmöglichkeiten pro Spiel.**

[Laden Sie 0.2.3 und Status herunter](../docs/downloads.md#nvmfg-unlock40) · [Installation](#installation) · [Stromaufwärts](#upstream-and-modifications) · [Lizenzen](LICENSES/README.md)

<a id="overview-and-purpose"></a>
## Überblick und Zweck

NVMFG Unlock40 ist eine unabhängig entwickelte Anwendung von 禅堂 Zendo (RevoluSound Team). Es kombiniert einen Windows-Controller, einen nativen Layer, einen Profilhelfer und eine Spiel-/Streamline-SDK-Verwaltung. Es zielt auf Spiele ab, die bereits NVIDIA DLSS Frame Generation und kompatible NVIDIA-Laufzeiten integrieren.

[RTX40MFG-Unlock](https://github.com/dashdogy/RTX40MFG-Unlock) wurde konsultiert, um die Arbeit zu vergleichen und zu verfeinern. Die aktuelle native Ebene enthält gemeinsam genutzte und angepasste Komponenten, die unten einzeln aufgeführt sind. Dieser Verweis macht nicht die gesamte NVMFG-Anwendung zu einem fork dieses Projekts.

Es dient dazu, das experimentelle MFG-Verhalten zentral zu koordinieren, spielspezifische Entscheidungen zu speichern und Laufzeitaktualisierungen und Backups sichtbar zu halten. Es fügt nicht jedem Spiel DLSS Frame Generation hinzu und konvertiert auch keine beliebige FSR-Implementierung.

Das aktuelle Paket ist **0.2.3**. Es fügt eine dauerhafte Spielbibliothek, Aktivitäts- und Fähigkeitsinformationen, lokale Diagnose und korrigiertes Auswahl-/Fortschrittsverhalten hinzu. [Downloads](../docs/downloads.md#nvmfg-unlock40) identifiziert die genauen Dateien und Hashes.

<a id="features"></a>
## Funktionen

- Zentrale Aktivierungs-/Deaktivierungssteuerung und optionaler Windows-Tray-Start.
- Auswahl pro Spiel zwischen Dynamic MFG, der Spieleinstellung und unterstützten festen Multiplikatoren.
- Separate gespeicherte Auswahlmöglichkeiten für beobachtete V-Sync-Ein/Aus-Zustände.
- Dynamic verwendet den Modus von NVIDIA; Es wird ausgesetzt, wenn V-Sync ausgeschaltet ist, mit einer separaten spielinternen/festen Auswahl.
- Spielmenüführung und dauerhafte Ausschlüsse; Spiele ohne DLSS FG behalten die Kontrolle.
- Spiele entdecken, übergeordnete Ordner auswählen, suchen, gruppieren und entfernen, ohne Spieldateien zu löschen.
- Streamline SDK Download/Import, verifizierter lokaler Cache, explizite Auswahl, Sicherung und Wiederherstellung pro Spiel.
- Native Anbieterüberprüfung, sitzungsspezifische Diagnose, globales Profiljournal und konfliktbewusste Wiederherstellung.
- 34 Schnittstellensprachen und vier Themen.

Wenn man FG im Spiel ausschaltet, bleibt es ausgeschaltet. Feste Auswahlmöglichkeiten von 2x bis 6x hängen vom Spiel/Menü/Laufzeit ab; Sie sind kein Versprechen, dass jede Kombination funktioniert. Der Controller beobachtet V-Sync und stellt V-Sync oder VRR nicht für den Benutzer ein.

<a id="compatibility"></a>
## Kompatibilität

| Anforderung | Einzelheiten |
| --- | --- |
| System | Windows 10/11 x64 |
| GPU | GeForce RTX 40 Ziel; Kein universeller GPU-Kompatibilitätsanspruch |
| Spiel | Vorhandene NVIDIA DLSS Frame Generation-Integration und unterstützte Laufzeit; Keine Anti-Cheat-Kompatibilitätszertifizierung |
| Anbieter | Der Kandidat ist an den Anbieter SHA-256 angeheftet, der in [Herkunft](../docs/provenance.md) dokumentiert ist. Unbekannte Hashes werden abgelehnt |
| Laufzeit | Im Lieferumfang enthaltenes .NET 8/WPF 8.0.30 für App/Agent; .NET Framework 4.8 für Profilhelfer |
| Berechtigungen | Administratorzugriff für die Controller-/Profiloperationen |
| Netzwerk | Erforderlich für ausgewählte offizielle SDK-Downloads; Importierte kompatible SDKs können lokal zwischengespeichert werden |
| Externe Binärdateien | NVIDIA-Treiber, NGX-Anbieter/-Modelle und Streamline-Spiellaufzeiten sind nicht im Paket enthalten |

Eine Versionsbezeichnung allein reicht nicht aus: Treiber, Anbieter-Hash, Spielintegration und tatsächlich geladene Module sind wichtig. Geschützte oder inkompatible Prozesse können den Anhang ablehnen. Die Anwendung ist nicht darauf ausgelegt, Anti-Cheat-Schutzmaßnahmen zu umgehen.

<a id="installation"></a>
## Installation

1. Lesen Sie den [Kandidatenstatus und Lizenzhinweis](../docs/downloads.md#nvmfg-unlock40).
2. Laden Sie `NVMFGUnlock40-0.2.3-Setup-x64.exe` oder `NVMFGUnlock40-0.2.3-Portable-x64.zip` herunter, sobald die Version verfügbar ist.
3. Überprüfen Sie SHA-256 und bewahren Sie die begleitenden Hinweise auf. Installieren Sie .NET Framework 4.8, falls Windows es nicht bereits bereitstellt.
4. Führen Sie Setup aus oder extrahieren Sie die **gesamte** portable ZIP-Datei in einen beschreibbaren lokalen Ordner.
5. Starten Sie `NVMFGUnlock40.exe`; Behalten Sie `agent`, `driver`, `engine` und `Licenses` im mitgelieferten Layout bei.

Der Ordner mit dem Namen `driver` enthält User-Space-Helfer, keinen Kernel-Treiber. Kopieren Sie nicht nur die Haupt-EXE-Datei und ersetzen Sie nicht den Anbieter-Hash, um die Kompatibilität zu erzwingen. Die aktuellen EXE-Dateien sind nicht signiert.

<a id="usage"></a>
## Nutzung

1. Beginnen Sie mit deaktiviertem Controller. Fügen Sie ein Spiel oder einen übergeordneten Ordner hinzu und wählen Sie die tatsächlichen Installationen aus.
2. Überprüfen Sie die MFG-Einstellungen jedes Spiels. Beantworten Sie, was die Speisekarte bietet; Die Antwort wird pro Spiel gespeichert.
3. Wählen Sie Dynamic oder die In-Game-Einstellung global und passen Sie dann die möglichen Optionen pro Spiel nach Bedarf an.
4. Aktivieren Sie den Controller nur, wenn Sie ihn verwenden möchten. Es kann vorübergehend sechs globale NVIDIA-Profileinstellungen mit einem Wiederherstellungsjournal ändern.
5. Starten Sie ein berechtigtes Spiel und aktivieren Sie sein eigenes DLSS Frame Generation. Folgen Sie jeder Anfrage für die V-Sync-off-Auswahl.
6. Verwenden Sie Ausschlüsse für Spiele, die nicht verwaltet werden sollen. Durch das Entfernen eines Spiels wird ein Ausschluss aufgezeichnet und seine Dateien/Backups bleiben erhalten.
7. Wenn Sie fertig sind, verwenden Sie den vollständigen Ablauf zum Beenden/Deaktivieren und Wiederherstellen der Anwendung.

Das Schließen des Hauptfensters kann dazu führen, dass der Controller in der Taskleiste verbleibt. Eine bereits in ein Spiel geladene DLL bleibt dort, bis das Spiel beendet wird; Das Deaktivieren des Controllers ist keine Entladegarantie. Schließen Sie betroffene Spiele vor Wartungsarbeiten oder Updates.

**Streamline SDKs:** Laden Sie auf der Seite NVIDIA SDK eine offizielle Version herunter oder importieren Sie eine kompatible lokale Version von SDK. Beim Import wird eine verifizierte Kopie gespeichert. **Use this version** wählt es aus und **Uninstall** entfernt diese zwischengespeicherte Kopie. Fehlende Streamline-DLLs können durch eine offizielle NVIDIA SDK ergänzt werden, wobei die Quelle angezeigt wird. Dadurch wird kein NGX-Modell heruntergeladen/ersetzt. Schließen Sie das Spiel, wählen Sie das gewünschte Spielupdate aus und behalten Sie die ursprüngliche Sicherung bei. Um Spieldateien wiederherzustellen, verwenden Sie die Backup-Wiederherstellung und nicht die Schaltfläche Uninstall des Caches.

<a id="library-diagnostics-and-updates"></a>
## Bibliothek, Diagnose und Updates

**Persistente Bibliothek:** Wählen Sie mehrere Spielordner, einschließlich verschiedener Laufwerke, aus, bevor Sie einen Scan starten. Der Fortschritt ist sichtbar und eine Stornierung ist möglich. Nach dem ersten Scan stellt ein lokaler Cache die Bibliothek beim Start wieder her, ohne jeden Spielordner zu durchsuchen. Aktualisieren Sie, um Änderungen zu finden oder einen weiteren Ordner hinzuzufügen. Durch Wartungsarbeiten werden die betroffenen Dateien immer noch erneut validiert. Die Backup-Überwachung bleibt aktiv. Der Cache wird unter `%LOCALAPPDATA%\RtxMfg\library-cache.json` gespeichert.

**Auswahl:** Ctrl+A wählt alle aus und Ctrl+D löscht die aktive Registerkarte „Spiele“ oder „Backups“. Es wird kein Spiel automatisch ausgewählt. Aktivitätsaktualisierungen und -aktualisierungen führen nicht mehr zu Geisterauswahlen oder inkonsistenten Zählungen.

**Aktivität und Kompatibilität:** Die MFG-Informationen pro Spiel stammen aus NGX-Beobachtungen ohne neues Overlay. Es handelt sich nicht um eine physische Zählung der angezeigten Frames. Die Unterstützung von Dynamic mit V-Sync erfolgt über Laufzeitfunktionen. Eine unbekannte Funktion wird nicht aus einer Versionsnummer abgeleitet. Die Anwendung ändert weder V-Sync noch VRR. Wenn V-Sync ausgeschaltet ist, bleibt Dynamic angehalten; Feste oder spielgesteuerte Auswahlmöglichkeiten sind unterschiedlich.

**Nächster Start:** Der vorübergehende Ausschluss überspringt das Patchen beim nächsten Spielstart und stellt nach dem Beenden die normale Verwaltung wieder her. Eine bereits in einem Spiel geladene DLL kann nicht entfernt werden: Schließen Sie das Spiel und starten Sie es neu. Wallpaper Engine wird als Desktop-Anwendung erkannt; Durch diese Korrektur bleibt der Schutz für tatsächlich ignorierte Spiele erhalten.

**Einstellungen und Unterstützung:** Der Import/Export von Einstellungen erfordert eine manuelle Neuzuordnung der Spielordner. Die lokale Diagnose in „Info“ filtert private Informationen und meldet verfügbare NVAPI-Fehlercodes oder Konfliktkategorien. Überprüfen Sie es, bevor Sie es teilen. Es wird nichts automatisch hochgeladen.

**Anwendungsaktualisierungen:** Eine optionale Prüfung zeigt Versionshinweise an und bietet das offizielle Setup. Der explizite Download wird anhand der GitHub-Größe und der SHA-256-Metadaten überprüft. Sie leiten die Installation selbst ein. Version 0.2.3 löscht auch abgeschlossene Fortschrittsmeldungen und behält gleichzeitig aussagekräftige Fehler und Ergebnisse bei. Diese Ergänzungen umfassen die Änderungen seit der öffentlichen Version 0.1.1.

<a id="screenshots"></a>
## Screenshots

![NVMFG SDK-Listenvorschau](../../../../assets/screenshots/nvmfg-0.1.1-sdk-preview.png)

Vorhandene englische 0.1.1-Schnittstellendarstellung mit einem Beispiel-SDK-Inventar. Es handelt sich nicht um eine aktuelle Versionsliste oder um einen Hinweis auf ein laufendes Spiel. [Bildherkunft](../assets/README.md).

<a id="update-and-uninstall"></a>
## Aktualisieren und deinstallieren

Schließen Sie betroffene Spiele. Deaktivieren/beenden Sie NVMFG und beheben Sie alle ausstehenden Wiederherstellungen der NVIDIA-Einstellungen vor der Aktualisierung. Installieren Sie das nächste Setup mit der vorhandenen Identität oder extrahieren Sie das neue tragbare Gerät in einen neuen Ordner. Zustand/Backups beibehalten.

Stellen Sie vor der Deinstallation die gewünschten SDK-Backups und NVIDIA-Einstellungen über die Anwendung wieder her, schließen Sie dann die Spiele und beenden Sie den Controller. Verwenden Sie Windows **Installed apps** für das Setup oder entfernen Sie den geschlossenen tragbaren Ordner, nachdem Sie die benötigten Dateien beibehalten haben. Löschen Sie ein aktives Wiederherstellungsjournal nicht manuell, um die Blockierung des Setups aufzuheben.

Lokale Spiellaufzeitsicherungen verwenden `%LOCALAPPDATA%\NvidiaStreamlineMaintenance\Backups`. MFG-Einstellungen/SDK-Daten verwenden `%LOCALAPPDATA%\RtxMfg`; Die Sitzungsausgabe befindet sich unter `Sessions` neben der Anwendung. Diese Dateien können Spielpfade enthalten. Veröffentlichen Sie sie nicht unzensiert.

<a id="known-limitations"></a>
## Bekannte Einschränkungen

- Eine gemeldete 0.1.1-Aktivierungs-/Wiederherstellungs-/Deinstallationsblockade bleibt unreproduziert und ihre Ursache ist unbekannt. Diese Version erhebt nicht den Anspruch, das Problem zu beheben. Bewahren Sie nach einem Fehler das Wiederherstellungsjournal auf und überprüfen Sie die lokale Diagnose. Erzwingen Sie nicht das Löschen von Wiederherstellungsdaten.
- Experimentelle native Patches können zu Abstürzen oder visuellen Artefakten führen; Im Entwicklungsverlauf wird ein ungelöster Bodycam-Absturz aufgezeichnet.
- Kontrollierte Renderer-Tests sind keine Zertifizierung für jedes Spiel, jeden Treiber oder Anti-Cheat.
- Generierte Frames erstellen keine neuen Eingabebeispiele. Dieser Hub verspricht keine gemessene Latenz oder Leistungssteigerung.
- Es kann zu Konflikten zwischen mehreren Tools/Overlays zur Frame-Generierung kommen. Die Anwendung berichtet über beobachtete Module, ohne jedes Koexistenzszenario nachzuweisen.
- Das Kompatibilitätsmanifest ist eine Erkennungshilfe und keine Liste vollständig getesteter Spiele.
- Die vollständigen NVIDIA SDK-Bedingungen und die ungelöste technische Einschränkung bleiben weiterhin in [Herkunft](../docs/provenance.md) dokumentiert.

<a id="troubleshooting"></a>
## Fehlerbehebung

| Symptom | Aktion |
| --- | --- |
| Anbieter nicht unterstützt | Bewahren Sie die überprüften Originaldateien auf. Treiber-/Anbieterversionen und den Fehler melden; Umgehen Sie nicht die Hash-Prüfung. |
| Kein DLSS FG im Spiel | Wählen Sie diese Antwort aus und überlassen Sie dem Spiel die Kontrolle; Dieses Tool kann diese Integration nicht herstellen. |
| Spielabstürze/Artefakte | Beenden Sie das Spiel, deaktivieren Sie NVMFG, verwenden Sie die ursprüngliche Laufzeitsicherung des Spiels, falls diese geändert wurde, und melden Sie reproduzierbare Details. |
| SDK-Liste oder Download nicht verfügbar | Aktualisieren und überprüfen Sie die offizielle Quelle; Eine zwischengespeicherte/importierte Version muss dennoch die Validierung bestehen. |
| Die ausstehende NVIDIA-Wiederherstellung blockiert den Exit/die Aktualisierung | Nutzen Sie die Wiederherstellung und bewahren Sie das Tagebuch auf; Konflikte dürfen nicht blind überschrieben werden. |
| Ein entferntes Spiel wird nicht wiederentdeckt | Sein Ausschluss ist hartnäckig. Fügen Sie es explizit hinzu, wenn Sie es erneut verwalten möchten. |

[Gemeinsame Support-Anleitung](../docs/support.md) erklärt, was in einen Bericht aufgenommen werden soll.

<a id="faq"></a>
## FAQ

**Enthält es NVIDIA-DLLs oder -Modelle?** Es ist kein Treiber, NGX-Anbieter/Modell oder Streamline-Laufzeit enthalten. Explizite SDK-Downloads stammen von NVIDIA.

**Funktioniert Dynamic, wenn V-Sync ausgeschaltet ist?** Es ist in diesem Zustand angehalten. Wählen Sie die Einstellung im Spiel oder einen geeigneten festen Multiplikator für den separaten Status dieses Spiels.

**Ist es ein ReShade/OptiScaler/FSR-Paket?** Nein. Diese werden nicht als Teil dieses Produktionspakets kompiliert oder versendet.

**Sind die geänderten Quellen öffentlich?** Nein. Kompilierte Pakete und erforderliche Credits/Lizenzen werden bereitgestellt. Rechte oder Einschränkungen Dritter werden dadurch nicht aufgehoben.

<a id="upstream-and-modifications"></a>
## Upstream und Modifikationen

Vergleichsreferenz und gemeinsam genutzte native Komponenten: **RTX40MFG-Unlock von Michael Robles / dashdogy**, Referenz-Commit `4e776d068f91b4a665425542bb005dd57cc3d891`, MIT. [Repository](https://github.com/dashdogy/RTX40MFG-Unlock) · [Original-Downloads](https://github.com/dashdogy/RTX40MFG-Unlock/releases).

Der Quellenvergleich identifiziert gemeinsames Patching, Anbieter-/Richtlinienhandhabung, zeitliche Korrekturen und MinHook-basierte Umleitungskomponenten. Ihre MIT- und BSD-Hinweise bleiben erhalten. Der vollständige Vergleich umfasst auch Dateien außerhalb des Produktionsziels.

Die Desktop-Anwendung, der Controller und der SDK-Verwaltungsworkflow werden von 禅堂 Zendo (RevoluSound Team) entwickelt. Die Projektarbeit umfasst zentrales Laden, NGX-Bootstrap-Integration, verifizierte Anbieterauswahl, Spiel-/V-Sync-Koordination und Sitzungsdiagnose. Der Provenienzleitfaden trennt diese Arbeit von den gemeinsam genutzten Komponenten; Ein Dateivergleich allein lässt nicht erkennen, wann einer der beiden Autoren auf die Idee gekommen ist.

Der Profilhelfer passt den MIT NVAPI-Wrapper aus dem Profile Inspector von Orbmu2k an. [Detaillierte Herkunft und Komponentenumfang](../docs/provenance.md).

<a id="credits-and-license"></a>
## Credits und Lizenz

Michael Robles; Orbmu2k; Tsuda Kageyu- und HDE-Mitwirkende; NVIDIA Corporation; Microsoft und Mitwirkende; Inno Setup Autoren und Übersetzer. Anwendungsentwicklung, Integrationen und Paketierung: 禅堂 Zendo (RevoluSound Team).

Der [vorhandene Berechtigung zum Teilen kompilierter Pakete](../../../../NVMFG-Unlock40/LICENSE) und alle [Komponentenlizenzen](LICENSES/README.md) bleiben erhalten. MIT-Berechtigungen für Upstream-Code unterscheiden sich von NVIDIA SDK-Bedingungen. Keine Pauschallizenz ersetzt sie.

Unabhängig von NVIDIA Corporation, nicht gesponsert und nicht offiziell unterstützt. Alle erwähnten Marken bleiben Eigentum ihrer Inhaber.
