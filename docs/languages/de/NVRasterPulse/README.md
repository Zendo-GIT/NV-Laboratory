<!-- nv-language-navigation:start -->
🌐 [English](../../../../NVRasterPulse/README.md) | [Français](../../../../NVRasterPulse/README.fr.md) · [NV Laboratory](../README.md)

<details>
<summary>🌐 Language · 34</summary>

[العربية](../../ar/NVRasterPulse/README.md) · [বাংলা](../../bn/NVRasterPulse/README.md) · [简体中文](../../zh/NVRasterPulse/README.md) · [Čeština](../../cs/NVRasterPulse/README.md) · [Dansk](../../da/NVRasterPulse/README.md) · [Nederlands](../../nl/NVRasterPulse/README.md) · [English](../../../../NVRasterPulse/README.md) · [Filipino](../../fil/NVRasterPulse/README.md) · [Suomi](../../fi/NVRasterPulse/README.md) · [Français](../../../../NVRasterPulse/README.fr.md) · **Deutsch** · [Ελληνικά](../../el/NVRasterPulse/README.md) · [हिन्दी](../../hi/NVRasterPulse/README.md) · [Magyar](../../hu/NVRasterPulse/README.md) · [Bahasa Indonesia](../../id/NVRasterPulse/README.md) · [Italiano](../../it/NVRasterPulse/README.md) · [日本語](../../ja/NVRasterPulse/README.md) · [한국어](../../ko/NVRasterPulse/README.md) · [मराठी](../../mr/NVRasterPulse/README.md) · [فارسی](../../fa/NVRasterPulse/README.md) · [Polski](../../pl/NVRasterPulse/README.md) · [Português](../../pt/NVRasterPulse/README.md) · [ਪੰਜਾਬੀ](../../pa/NVRasterPulse/README.md) · [Română](../../ro/NVRasterPulse/README.md) · [Русский](../../ru/NVRasterPulse/README.md) · [Español](../../es/NVRasterPulse/README.md) · [Kiswahili](../../sw/NVRasterPulse/README.md) · [Svenska](../../sv/NVRasterPulse/README.md) · [தமிழ்](../../ta/NVRasterPulse/README.md) · [ไทย](../../th/NVRasterPulse/README.md) · [Türkçe](../../tr/NVRasterPulse/README.md) · [Українська](../../uk/NVRasterPulse/README.md) · [اردو](../../ur/NVRasterPulse/README.md) · [Tiếng Việt](../../vi/NVRasterPulse/README.md)

[Translation policy](../../README.md)

</details>
<!-- nv-language-navigation:end -->

<!-- nv-translation-notice:start -->
> Maschinell unterstützte Übersetzung aus dem Englischen. Technische Namen, Befehle, URLs und ursprüngliche Rechtstexte bleiben erhalten. Eine Rezension durch einen Muttersprachler ist willkommen; Konsultieren Sie die englische Referenz, wenn der Wortlaut unklar ist.
<!-- nv-translation-notice:end -->

<a id="nvrasterpulse"></a>
# NVRasterPulse

**FPS-Grenzwerte pro Anwendung bis RivaTuner Statistics Server.**

> **Installieren Sie zuerst RTSS.** NVRasterPulse erfordert [RivaTuner Statistics Server (RTSS), heruntergeladen von Guru3D](https://www.guru3d.com/download/rtss-rivatuner-statistics-server-download/). RTSS muss ausgeführt werden, um Grenzwerte durchzusetzen. Es ist kein RTSS-Installationsprogramm, keine Hook-DLL oder SDK im Lieferumfang enthalten.

[Laden Sie 0.2 und Status herunter](../docs/downloads.md#nvrasterpulse) · [Installation](#installation) · [Wie Grenzen funktionieren](#usage) · [Lizenz](../../../../NVRasterPulse/LICENSE)

<a id="overview-and-purpose"></a>
## Überblick und Zweck

NVRasterPulse ist eine kompakte Windows-Schnittstelle zum Verwalten von RTSS-Frame-Limits nach ausführbarem Namen. RTSS führt die Begrenzung durch. NVRasterPulse verwaltet die entsprechenden Profilwerte, Backups und Neuladeanforderungen mit Tray-Zugriff und dauerhaften Auswahlmöglichkeiten.

Es dient dazu, die Bearbeitung genauer Limits pro Spiel zu erleichtern, ohne ein ganzes RTSS-Profil zu ersetzen oder seine Overlay-Einstellungen zu ändern. Version **0.2** fügt Konfigurationsdiagnose, einen FPS-Helfer, Pause, Rückgängigmachen und Profilfreigabe hinzu.

<a id="features"></a>
## Funktionen

- Wählen Sie eine laufende Anwendung aus oder fügen Sie deren ausführbare Datei manuell hinzu.
- Speichern Sie FPS-Grenzwerte von 1 bis 1000 mit bis zu drei Dezimalstellen.
- Exakte rationale Kodierung der eingegebenen Werte: 59.94 wird zu 2997/50.
- Front Edge Sync-Konfiguration (`SyncLimiter=1`) mit aktivem Warten (`PassiveWait=0`).
- Profilaktualisierungen pro ausführbarer Datei, automatische Sicherungen und atomare Schreibvorgänge.
- Entfernung von Begrenzerüberschreibungen unter Beibehaltung anderer Profilinhalte.
- RTSS-Installationserkennung, manuelle Pfadauswahl und explizites Starten/Neuladen.
- Single-Instance-Tray-Betrieb, optional installiertes Startup, 34 Sprachen und vier Themes.
- Separate normale Beenden- und **Beenden + RTSS**-Aktionen.

<a id="compatibility"></a>
## Kompatibilität

| Anforderung | Einzelheiten |
| --- | --- |
| System | Windows 10/11 x64 |
| Laufzeit | [.NET Framework 4.8](https://dotnet.microsoft.com/en-us/download/dotnet-framework/net48), bei Bedarf separat installiert |
| Erforderliche Software | RTSS mit `RTSS.exe`, einem passenden `Profiles`-Verzeichnis und kompatibler Profil-/Neuladeunterstützung |
| GPU | Die RTSS-Kompatibilität bestimmt den Begrenzer; Für diesen Profilmanager ist keine bestimmte RTX-Generation erforderlich |
| Berechtigungen | Die aktuelle Anwendung fordert Administratorzugriff an. Auf den ausgewählten RTSS-Profilordner muss zugegriffen werden können |
| Spiele | Hängt von der RTSS-Hooking-Unterstützung und den Einschränkungen jedes Spiels ab; Keine Anti-Cheat-Garantie |

Bei diesem Hub-Audit wurde für jede Funktion keine bestimmte RTSS-Mindestversion zertifiziert. Verwenden Sie die offizielle aktuelle Distribution und melden Sie die genaue Version, wenn ein Profilschlüssel/Neuladen nicht funktioniert. Der installierte, aber gestoppte RTSS besteht die Installationsprüfung. Es muss dann zur eigentlichen Begrenzung gestartet werden.

<a id="installation"></a>
## Installation

1. **[Laden Sie RTSS von Guru3D herunter und installieren Sie es](https://www.guru3d.com/download/rtss-rivatuner-statistics-server-download/).**
2. Öffnen Sie [NVRasterPulse-Downloads](../docs/downloads.md#nvrasterpulse) und prüfen Sie die Release-Verfügbarkeit.
3. Laden Sie `NVRasterPulse-0.2-win-x64-Setup.exe` oder `NVRasterPulse-0.2-win-x64-portable.zip` sowie die Hinweise/Prüfsummen herunter.
4. Vergleiche SHA-256. Führen Sie Setup aus oder extrahieren Sie die gesamte portable ZIP-Datei in einen beschreibbaren lokalen Ordner.
5. Öffnen Sie `NVRasterPulse.exe`. Wenn RTSS fehlt, verwenden Sie **RTSS herunterladen**, installieren Sie es und **erneut prüfen** oder wählen Sie `RTSS.exe` manuell aus.
6. Starten Sie RTSS über die normale Verknüpfung oder über die Schaltfläche RTSS von NVRasterPulse, wenn es gestoppt ist.

Durch das Deaktivieren der optionalen Erinnerung wird die Prüfung der Voraussetzungen nicht übersprungen. Ein stiller Windows-Tray-Start wartet, bis das Hauptfenster geöffnet wird, bevor diese Prüfung angezeigt wird. Das Setup installiert nur NVRasterPulse. Seine EXE-Dateien sind nicht signiert.

<a id="usage"></a>
## Nutzung

1. Wählen Sie die gewünschte laufende Anwendung aus oder navigieren Sie zu der EXE-Datei des Spiels.
2. Geben Sie einen Grenzwert zwischen 1 und 1000 FPS ein, bei Bedarf auch einen Bruchwert.
3. Speichern und überprüfen Sie das gemeldete Ergebnis. NVRasterPulse aktualisiert das RTSS-Profil dieser ausführbaren Datei und fordert ein Neuladen an.
4. Bestätigen Sie, dass RTSS ausgeführt wird, und überprüfen Sie das Verhalten im beabsichtigten Spiel.

Profile werden durch den **ausführbaren Namen** verschlüsselt, z. B. `Game.exe.cfg`. Zwei verschiedene Ordner, die `Game.exe` enthalten, verwenden dasselbe RTSS-Profil. Durch das Speichern des vollständigen Pfads wird diese Kollision nicht behoben.

Beim Speichern werden Front Edge Sync und aktives Warten verwendet. Aktives Warten kann die Nutzung von CPU erhöhen. Die alternativen `LimitTime`-Felder werden neutralisiert. Vorhandene Kommentare, Overlay-Einstellungen und `EnableHooking=0` bleiben erhalten. Das globale Profil RTSS wird nicht geändert.

Verwenden Sie die Papierkorbaktion, um die Limiter-Überschreibungen von NVRasterPulse zu entfernen. Es wird nicht das gesamte RTSS-Profil gelöscht. Ein von RTSS Global oder einem anderen Tool übernommenes Limit gilt möglicherweise auch danach noch.

**Schließen und Beenden:** Das Hauptfenster kann in der Taskleiste ausgeblendet werden. Beim normalen **Beenden** bleibt RTSS aktiv und die gespeicherten Grenzwerte bleiben erhalten. **Beenden + RTSS** fordert ein normales Schließen des entsprechenden RTSS-Prozesses in der aktuellen Sitzung an, wartet bis zu acht Sekunden und beendet ihn nicht zwangsweise. Gespeicherte Limits bleiben in beiden Fällen bestehen.

Sprache und Thema werden in der App ausgewählt. Der Start bei der Windows-Anmeldung ist optional und für eine installierte Kopie vorgesehen. Die Informationsschaltfläche erläutert häufige Aktionen.

<a id="diagnostics-and-profile-tools"></a>
## Diagnose- und Profiltools

Öffnen Sie das Aktionsmenü für die zusätzlichen Tools. Sie behalten RTSS Global, Overlay-Einstellungen und Ausschlüsse bei.

**Diagnose:** Überprüfen Sie lokale/effektive Grenzwerte, gestopptes RTSS, eine fehlende ausführbare Datei, kein erkanntes Fenster, deaktiviertes Hooking, Vererbung, angehaltene Grenzwerte, konkurrierende Einstellungen und doppelte ausführbare Namen. Diese schreibgeschützte Prüfung beschreibt die Konfiguration; Es beweist nicht, dass ein Spiel an RTSS gebunden ist, und misst auch nicht dessen FPS.

**FPS-Helfer:** Wählen Sie die Anzeige aus und deklarieren Sie selbst VRR/G-Sync, V-Sync, Reflex und Frame Generation. Die gerundete Aktualisierungsfrequenz stammt von Windows. Wenn Reflex oder Frame Generation aktiv oder unbekannt ist, wird keine automatische Obergrenze angeboten. Für VRR mit aktiviertem V-Sync und deaktiviertem Reflex/FG subtrahiert die Heuristik mindestens 3 FPS oder etwa 2 % der Bildwiederholfrequenz. Dies ist kein gemessenes Optimum. Durch die Anwendung des Vorschlags wird der Entwurf ausgefüllt; **Speichern** bleibt eine separate Aktion.

**Pause und Fortsetzen:** setzt die Obergrenze des ausgewählten Programms außer Kraft und stellt dann die vorherigen Begrenzerfelder wieder her. Widersprüchliche Änderungen durch ein anderes Tool verhindern eine Wiederaufnahme bei unklarem Zustand. Durch das Ausblenden eines Eintrags wird dessen Obergrenze nicht angehalten.

**Rückgängig machen:** stellt die letzte Änderung an den sechs verwalteten Limiterfeldern für dieses Programm wieder her. Es gibt eine Ebene; Dadurch wird nicht das gesamte RTSS wiederhergestellt. Widersprüchliche externe Änderungen werden abgelehnt. Dateisicherungen bleiben getrennt.

**Profile teilen:** Ausgewählte Profile in eine `.nvrp`-Datei exportieren. Der Import zeigt eine Vorschau an und lässt vorhandene Obergrenzen standardmäßig deaktiviert. Die Datei enthält nur ausführbare Namen, Limits und Zustände, ohne absolute Pfade oder Skripte. Prüfen Sie Ihre Auswahl und übernehmen Sie die ausgewählten Profile. Ein E/A-Fehler kann dazu führen, dass einige Profile bereits angewendet werden; Das Ergebnis identifiziert sie und jeder behält seine Rückgängigmachung. Identische ausführbare Namen adressieren immer noch dasselbe RTSS-Profil.

**Favoriten und ausgeblendete Einträge:** Nützliche Programme zuerst anheften, unerwünschte Einträge ausblenden und im entsprechenden Dialog wiederherstellen. Diese Entscheidungen bleiben bestehen. Ein geschlossener Favorit wird nicht als laufende Anwendung angezeigt.

<a id="screenshots"></a>
## Screenshots

![NVRasterPulse-Hauptfenstervorschau](../../../../assets/screenshots/nvrasterpulse-0.1-preview.png)

Vorhandenes französisches 0.1-UI-Rendering mit ausführbaren Beispielnamen und einem FPS-Wert von 176. RTSS wird als gestoppt angezeigt; Hierbei handelt es sich um eine Schnittstellendarstellung, nicht um einen laufenden Begrenzer oder eine Latenzmessung. [Bildherkunft](../assets/README.md).

<a id="update-and-uninstall"></a>
## Aktualisieren und deinstallieren

Beenden Sie NVRasterPulse, laden Sie die neue Version herunter und überprüfen Sie sie. Führen Sie dann das Setup aus oder extrahieren Sie das tragbare Gerät in einen neuen Ordner. Einstellungen und RTSS-Backups beibehalten. RTSS-Updates sind separat und stammen von Guru3D.

Um eine installierte Kopie zu entfernen, verwenden Sie Windows **Installed apps**. Bei tragbaren Geräten beenden Sie das Programm und entfernen den extrahierten Ordner, wenn Ihre Backups sicher sind. Gespeicherte RTSS-Grenzwerte werden durch die Deinstallation von NVRasterPulse nicht entfernt: Entfernen Sie zuerst die vorgesehenen Limiter-Überschreibungen. RTSS verfügt über ein eigenes Deinstallationsprogramm.

Lokaler Status: `%LOCALAPPDATA%\NVRasterPulse`. Automatische RTSS-Backups: `%LOCALAPPDATA%\NVRasterPulse\Backups\RTSS`. Möglicherweise wird ein älterer `%LOCALAPPDATA%\RTSSProfileBridge`-Standort zur Migration gelesen. Diese Dateien können persönliche ausführbare Pfade enthalten und sollten nicht öffentlich veröffentlicht werden.

<a id="known-limitations"></a>
## Bekannte Einschränkungen

- RTSS führt die Obergrenze durch. Ein gespeicherter Wert oder eine erfolgreiche Neuladeanforderung ist kein gemessenes Frame-Time-Ergebnis.
- Ausführbare Dateien mit demselben Namen teilen sich ein Profil.
- Ein weiterer globaler/spielbezogener Limiter kann das Ergebnis beeinflussen; Durch das Deaktivieren der lokalen Überschreibung wird eine geerbte Obergrenze nicht entfernt.
- Ein absichtlich deaktivierter RTSS-Hook bleibt deaktiviert.
- Aktives Warten hat einen Kompromiss zwischen CPU und Leistung.
- Kein universelles Spiel, keine Anti-Cheat- oder End-to-End-Latenzvalidierung.
- Die frühere experimentelle unabhängige Limiter-Engine wird weder kompiliert noch ausgeliefert.
- Automatische Backups erfordern keine Schnittstelle zur vollständigen Sicherung und Wiederherstellung mit nur einem Klick.

<a id="troubleshooting"></a>
## Fehlerbehebung

| Symptom | Aktion |
| --- | --- |
| RTSS-Voraussetzung bleibt offen | Wählen Sie den tatsächlichen `RTSS.exe` und den passenden Profilordner aus und prüfen Sie dann erneut. |
| Limit gespeichert, aber keine Auswirkung | Starten Sie RTSS; Überprüfen Sie die korrekte Spiel-EXE-Datei/das richtige Profil, die Hook-Berechtigungen und andere Einschränkungen. |
| Speichern schlägt fehl | Überprüfen Sie die Ordnerberechtigungen und bewahren Sie den angezeigten Fehler/die angezeigte Sicherung auf. |
| Das Limit bleibt nach dem Entfernen bestehen | Überprüfen Sie RTSS Global und andere Tools. Die Papierkorbaktion entfernt nur lokale Limiter-Überschreibungen. |
| Zwei Spiele erhalten das gleiche Limit | Überprüfen Sie, ob die Namen der ausführbaren Dateien identisch sind. |
| Beenden + RTSS lässt RTSS geöffnet | Schließen Sie RTSS normalerweise selbst; Dieser Befehl vermeidet bewusst eine erzwungene Beendigung. |

Wenn Sie ein RTSS-Backup manuell wiederherstellen, schließen Sie zuerst RTSS und bewahren Sie das aktuelle Profil auf, bevor Sie es durch das beabsichtigte Backup ersetzen. Dadurch können nicht verwandte Profilbearbeitungen überschrieben werden. Überprüfen Sie die Datei und das Datum. [Geteilte Unterstützung](../docs/support.md).

<a id="faq"></a>
## FAQ

**Benötige ich auch MSI Afterburner?** NVRasterPulse erfordert RTSS; es hängt nicht von der Afterburner-Anwendung ab. Befolgen Sie die Installationsoptionen des RTSS-Händlers.

**Kann ich dies verwenden, ohne dass RTSS ausgeführt wird?** Sie können Profile verwalten, sobald eine Installation erkannt wird, RTSS muss jedoch zur Einschränkung ausgeführt werden.

**Entfernt das Beenden oder Deinstallieren die Kappen?** Nein. Entfernen Sie die gewünschten Begrenzerüberschreibungen explizit, bevor Sie NVRasterPulse entfernen.

**Ist es ein fork von RTSS?** Nein. Es handelt sich um einen unabhängigen Profilmanager; Es ist keine RTSS-Quelle oder ausführbare Datei integriert.

<a id="upstream-modifications-and-credits"></a>
## Upstream, Modifikationen und Credits

Das Entwicklungs-Repository stammt von [Orbmu2k's NVIDIA Profile Inspector](https://github.com/Orbmu2k/nvidiaProfileInspector). Seine MIT-Paletten/UI-Ressourcen werden gutgeschrieben. Die Profilverwaltungsdienste, Fraktionskodierung, Backups, RTSS-Reload-Bridge, Tray-Verhalten, Voraussetzungshandbuch, Sprachen und anwendungsspezifisches Symbol wurden von 禅堂 Zendo (RevoluSound Team) entwickelt/angepasst.

RTSS wird von **Unwinder** entwickelt und separat über Guru3D vertrieben. NVRasterPulse ruft `UpdateProfiles` von der ausgewählten installierten Hook-DLL auf; Nein RTSS SDK oder Hook-Binärdatei wird neu verteilt. Das Installationsprogramm verwendet unverändertes Inno Setup 7.1.0 mit angepassten Skripten/Übersetzungen und einem Projekt-Bootstrap.

[Vollständige Provenienz](../docs/provenance.md) · [Tabelle eines Drittanbieters](../THIRD_PARTY_NOTICES.md)

<a id="license"></a>
## Lizenz

Das Paket vertreibt NVRasterPulse ausdrücklich unter dem bereitgestellten [MIT-Lizenz](../../../../NVRasterPulse/LICENSE) und behält das Copyright (c) 2016 Orbmu2k. Die Anwendungsquelle wird privat verwaltet; MIT erfordert keine Veröffentlichung der geänderten Quelle. RTSS und Windows/.NET unterliegen weiterhin ihren eigenen Bedingungen. [Vollständige Mitteilungen](LICENSES/README.md).

Unabhängig von NVIDIA Corporation, MSI und RTSS; nicht von ihnen gesponsert oder offiziell unterstützt. Produktnamen bleiben Marken ihrer Eigentümer.
