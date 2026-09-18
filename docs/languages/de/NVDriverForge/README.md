<!-- nv-language-navigation:start -->
🌐 [English](../../../../NVDriverForge/README.md) | [Français](../../../../NVDriverForge/README.fr.md) · [NV Laboratory](../README.md)

<details>
<summary>🌐 Language · 34</summary>

[العربية](../../ar/NVDriverForge/README.md) · [বাংলা](../../bn/NVDriverForge/README.md) · [简体中文](../../zh/NVDriverForge/README.md) · [Čeština](../../cs/NVDriverForge/README.md) · [Dansk](../../da/NVDriverForge/README.md) · [Nederlands](../../nl/NVDriverForge/README.md) · [English](../../../../NVDriverForge/README.md) · [Filipino](../../fil/NVDriverForge/README.md) · [Suomi](../../fi/NVDriverForge/README.md) · [Français](../../../../NVDriverForge/README.fr.md) · **Deutsch** · [Ελληνικά](../../el/NVDriverForge/README.md) · [हिन्दी](../../hi/NVDriverForge/README.md) · [Magyar](../../hu/NVDriverForge/README.md) · [Bahasa Indonesia](../../id/NVDriverForge/README.md) · [Italiano](../../it/NVDriverForge/README.md) · [日本語](../../ja/NVDriverForge/README.md) · [한국어](../../ko/NVDriverForge/README.md) · [मराठी](../../mr/NVDriverForge/README.md) · [فارسی](../../fa/NVDriverForge/README.md) · [Polski](../../pl/NVDriverForge/README.md) · [Português](../../pt/NVDriverForge/README.md) · [ਪੰਜਾਬੀ](../../pa/NVDriverForge/README.md) · [Română](../../ro/NVDriverForge/README.md) · [Русский](../../ru/NVDriverForge/README.md) · [Español](../../es/NVDriverForge/README.md) · [Kiswahili](../../sw/NVDriverForge/README.md) · [Svenska](../../sv/NVDriverForge/README.md) · [தமிழ்](../../ta/NVDriverForge/README.md) · [ไทย](../../th/NVDriverForge/README.md) · [Türkçe](../../tr/NVDriverForge/README.md) · [Українська](../../uk/NVDriverForge/README.md) · [اردو](../../ur/NVDriverForge/README.md) · [Tiếng Việt](../../vi/NVDriverForge/README.md)

[Translation policy](../../README.md)

</details>
<!-- nv-language-navigation:end -->

<!-- nv-translation-notice:start -->
> Maschinell unterstützte Übersetzung aus dem Englischen. Technische Namen, Befehle, URLs und ursprüngliche Rechtstexte bleiben erhalten. Eine Rezension durch einen Muttersprachler ist willkommen; Konsultieren Sie die englische Referenz, wenn der Wortlaut unklar ist.
<!-- nv-translation-notice:end -->

<a id="nvdriverforge"></a>
# NVDriverForge

**Bereiten Sie eine NVIDIA-Treiberinstallation mit klaren Komponentenauswahlen und optionalen Einstellungen vor.**

[Laden Sie 0.1.4 und Status herunter](../docs/downloads.md#nvdriverforge) · [Installation](#installation) · [Credits](#credits-and-upstream) · [Lizenz](../../../../NVDriverForge/LICENSE)

<a id="overview-and-purpose"></a>
## Überblick und Zweck

NVDriverForge führt Sie durch ein Original-Treiberpaket NVIDIA: Wählen Sie den Treiber aus, überprüfen Sie seine Komponenten, überprüfen Sie optionale Optimierungen und bestätigen Sie dann die Installation. Es dient dazu, diese Entscheidungen verständlich zu machen und die Informationen zur Installation, zu privilegierten Vorgängen und zur Wiederherstellung zusammenzuhalten.

Es handelt sich um eine unabhängig entwickelte Anwendung, die teilweise vom Workflow von NVCleanstall inspiriert ist. NVCleanstall ist nicht enthalten und es wird keine vollständige Funktionsparität beansprucht.

<a id="features"></a>
## Funktionen

- NVIDIA Game Ready / Studio Suche und Downloads; optionale Hotfix-Erkennung mit manuellem Fallback.
- Analyse des Originalpakets, Hashes, NVIDIA-Signaturen, Manifesten und kompatiblen INF-Einträgen.
- Komponentenauswahl mit Abhängigkeiten und Erhaltung unbekannter Komponenten.
- Mit der Version 0.1.4 bleiben ausgewählte optionale NVIDIA-Komponenten überspringbar und schließen nur verifizierte, ungeprüfte Komponenten von der Erkennung aus. Bereits aktuelle oder nicht anwendbare optionale Laufzeiten werden nicht mehr als kritische Komponenten erzwungen.
- Klare Zusammenfassungen von Installationsfehlern und Zugriff auf detaillierte Protokolle in allen 34 Sprachen.
- Bereitschaftsprüfungen, explizite Bestätigung, Export des Treiberspeichers und native NVIDIA-Profilsicherung vor der Installation.
- Optionale erweiterte Einstellungen mit Preflight-Prüfungen, Journalen und konfliktbewusster Wiederherstellung.
- Optionale **Custom NV**-Voreinstellung mit benannten Auswahlmöglichkeiten und Erklärungen, einschließlich einer separaten SILK-Stärkeauswahl und Kompatibilitätsprüfungen.
- Optionale Downloads des genauen NVENC-Patches; Quell-Commit- und Zielbytes werden überprüft.
- Eine separate, optionale Installation des Profile Inspector fork über den Tools-Bildschirm.
- Komponentenhandbuch, wiederverwendbare Einstellungen, Treiberkits, lokale Supportberichte und optionale Anwendungsaktualisierungen.
- 34 Schnittstellensprachen und vier Themen.

Zu den verfügbaren erweiterten Optionen gehören MPO, der DLSS-Indikator, Ansel, NVIDIA Audio Sleep, MSI, Interrupt-Richtlinie/Priorität, HDCP, Display-Container-Start und ein berechtigter Legacy-Telemetriedienst. Jedes hat seine eigenen Voraussetzungen und Auswirkungen; Hierbei handelt es sich nicht um universelle Leistungsverbesserungen.

<a id="compatibility"></a>
## Kompatibilität

| Anforderung | Einzelheiten |
| --- | --- |
| System | Windows 10 Build 19041 oder neuer / Windows 11, x64 |
| GPU/Treiber | Kompatibles NVIDIA-Paket und erkannte Hardware; Die automatische Katalogsuche deckt hauptsächlich bekannte GeForce-Modelle ab |
| Laufzeit | .NET 8 / WPF 8.0.31 im vorbereiteten eigenständigen Paket enthalten |
| Privilegien | Normale Benutzeroberfläche/Einrichtung pro Benutzer; Für die Treiberinstallation und Systemänderungen ist Administratorzugriff erforderlich |
| Netzwerk | Erforderlich für Online-NVIDIA-Suchen/Downloads und explizite Upstream-NVENC-Anfragen; Es kann ein lokaler Originaltreiber ausgewählt werden |
| Enthaltene Werkzeuge | Unverändertes 7-Zip 26.03, Laufzeithinweise, optionaler MIT Profile Inspector-Begleiter |
| Optionaler Begleiter | .NET Framework 4.8 für das separate Profile Inspector fork |

Es gibt keine willkürliche Mindesttreiberversion, die alle Funktionen abdeckt. Die Multi-GPU-Suche muss mit jedem erkannten GPU übereinstimmen. Nicht unterstützte/professionelle Modelle erfordern möglicherweise eine manuelle Treiberauswahl. Das Installationsprogramm von NVIDIA bleibt die letzte Hardware-/Betriebssystemautorität.

<a id="installation"></a>
## Installation

1. Besuchen Sie [Downloads](../docs/downloads.md#nvdriverforge) und bestätigen Sie, dass die Version veröffentlicht wurde.
2. Wählen Sie `NVDriverForge-Setup.exe` für die Installation oder `NVDriverForge.exe` für den mobilen Einsatz.
3. Vergleichen Sie SHA-256 mit `SHA256SUMS.txt` der Version.
4. Führen Sie das Setup für eine benutzerspezifische Installation und ein Standard-Deinstallationsprogramm aus oder legen Sie die tragbare EXE-Datei in einem beschreibbaren Ordner ab und öffnen Sie sie.

Das tragbare Gerät enthält seine Laufzeit und sein optionales Installationsprogramm. Durch die Installation von NVDriverForge wird kein GPU-Treiber installiert. Seine EXE-Dateien sind derzeit nicht signiert.

<a id="usage"></a>
## Nutzung

1. **Treiber:** Laden Sie von NVIDIA herunter oder wählen Sie eine Original-Installations-EXE-Datei für NVIDIA aus. Lassen Sie die Analyse zu Ende gehen.
2. **Komponenten:** Beschreibungen und erforderliche Abhängigkeiten überprüfen. Unbekannte Komponenten bleiben erhalten.
3. **Optimierungen:** unerwünschte Optionen unverändert lassen. Lesen Sie die Auswirkungen und Kompromisse, bevor Sie etwas auswählen.
4. **Überprüfung:** Überprüfen Sie den genauen Treiber, die Komponenten und optionalen Vorgänge und bestätigen Sie dann die Installation.
5. Akzeptieren Sie UAC nur für den von Ihnen ausgewählten Vorgang. Bewahren Sie die Wiederherstellungsanweisungen des geschützten Jobs auf.
6. Wenn der neue Treiber einen Neustart benötigt, befolgen Sie den gemeldeten Status. Verzögerte Vorgänge erfordern nach diesem Neustart eine explizite Wiederaufnahme.

Custom NV startet unverändert. Wählen Sie einzelne benannte Werte aus oder überprüfen Sie die bereitgestellte Voreinstellung und ihre Ausschlüsse. Die beiden internen Informationsfelder werden nicht unabhängig voneinander geschrieben. Einstellungen werden nur im überprüften neuen Treiber-Workflow angewendet, niemals durch Öffnen einer Vorschau. Die Installation des separaten NVPI-Editors ist nicht erforderlich.

Die optionale NVENC-Arbeit lädt kompatible Daten von einem angehefteten keylase-Commit herunter. Es verändert zwei Treiber-DLLs und macht ihre Signaturen ungültig; es kann durch Windows, Encoder, DRM oder Anti-Cheat abgelehnt werden. In NVDriverForge sind keine derartigen Daten oder NVIDIA-DLLs eingebettet. [Herkunft und Lizenzbeschränkungen](../docs/provenance.md).

Die Einstellungen steuern die Sprache, das Design und optionale Prüfungen für installierte Benutzeraktualisierungen. Das tragbare Gerät erstellt die installierte Hintergrundüberprüfungsaufgabe nicht. Tools und Wiederherstellung sind von den vier Installationsschritten getrennt.

<a id="backup-and-diagnostic-tools"></a>
## Backup- und Diagnosetools

**Vor der Installation:** Bereitschaftsprüfungen umfassen die Paketsignatur, GPUs, geschätzten Arbeitsbereich/Backup-Speicherplatz, ausstehenden Neustart und konkurrierende Installationsprogramme. Der erhöhte Arbeiter wiederholt sie. Konkurrierende Prozesse werden nie automatisch gestoppt. Die native Sicherung der NVIDIA-Profildatenbank muss erfolgreich sein, bevor das NVIDIA-Setup gestartet wird. Der Export des Treiberspeichers ist ein separates Backup.

**Wiederverwendbare Auswahlmöglichkeiten:** Im Komponentenhandbuch werden vier Fragen zu Spielen, Audio, NVIDIA App und Aufnahme gestellt. Überprüfen Sie die Vorschläge. Erforderliche, unbekannte und Abhängigkeitskomponenten bleiben geschützt. Exportieren Sie die Einstellungen, zeigen Sie sie dann in der Vorschau an und validieren Sie sie beim Import erneut anhand des ausgewählten Pakets. Einwilligungen, Neustartvorgänge, Programmpfade und Patch-Payloads werden nicht importiert.

**Treiberkit:** Exportieren Sie ein `.nvdfkit.zip`, um das ursprünglich signierte NVIDIA-Installationsprogramm, Auswahlmöglichkeiten, Hashes und Anweisungen zusammenzuhalten. Tragen Sie `NVDriverForge.exe` separat. Importieren Sie das Kit in Tools, überprüfen Sie die Vorschau und verwenden Sie dann den normalen Installationsablauf. Dies ist kein schlanker Treiber oder modifiziertes eigenständiges Installationsprogramm. Für den optionalen NVENC ist noch ein Download und die Zustimmung für genau diesen Treiber erforderlich. Die Weiterverbreitungsbedingungen von NVIDIA gelten weiterhin.

**Ergebnisse und Unterstützung:** Lesen Sie das kurze Ergebnis und erweitern Sie die Details pro Stufe/pro Option. Bei einem erfolgreichen Rücklesen wird ein gespeicherter Wert ermittelt, keine gemessene Verbesserung. Der lokale JSON-Supportbericht verwendet Felder auf der Zulassungsliste, einschließlich des zuletzt gespeicherten Jobs nach dem Neustart der App. Sehen Sie sich eine Vorschau an, bevor Sie es speichern oder teilen. Es enthält keine Rohprotokolle, Profilinhalte oder Hardware-IDs und wird niemals automatisch hochgeladen.

**Wiederherstellung:** Befolgen Sie die Anleitung des geschützten Jobs, um den gesicherten Treiber wiederherzustellen. Für die explizite Profilwiederherstellung sind die ursprüngliche Treiberversion und dieselben GPUs erforderlich. Es ersetzt die gesamte Datenbank, behält eine aktuelle Kopie bei und prüft Hashes und Konfliktzustände. Löschen Sie nicht das Tagebuch und erzwingen Sie keine Nichtübereinstimmung. Die echte Treiberinstallation, die vollständige Wiederherstellung und der native Profilimport bleiben mit diesem neuen Workflow auf einem realen System unvalidiert.

**Anwendungsaktualisierungen:** Lesen Sie die Versionshinweise und wählen Sie dann explizit einen SHA-256-verifizierten Download aus. Die Prüfung erfolgt standardmäßig manuell, mit einer optionalen Prüfung beim Start. Es wird kein Installationsprogramm automatisch gestartet. Diese Funktion ist unabhängig von Treiberaktualisierungsprüfungen und der optionalen Treiberprüfungsaufgabe der installierten Edition.

<a id="screenshots"></a>
## Screenshots

![Vorschau der Treiberseite NVDriverForge](../../../../assets/screenshots/nvdriverforge-0.1.2-preview.png)

Vorhandenes 0.1.2 französisches UI-Rendering mit Beispieldaten; als Schnittstellenvorschau beibehalten. Der angezeigte 699.99-Treiber ist ein Testgerät und keine echte Version zum Herunterladen. [Bildherkunft](../assets/README.md).

<a id="update-and-uninstall"></a>
## Aktualisieren und deinstallieren

Schließen Sie NVDriverForge, holen Sie sich das nächste offizielle Paket und überprüfen Sie dessen Hash. Verwenden Sie für ein installiertes Update dieselbe Setup-Identität. Ersetzen Sie eine geschlossene tragbare EXE-Datei durch die neue. Behalten Sie Einstellungen und geschützte Jobs bei.

Uninstall von Windows **Installed apps**. Es entfernt die App und ihre Aktualisierungsaufgabe, nicht den NVIDIA-Treiber. Einstellungen, Protokolle und Backups bleiben erhalten. Stellen Sie bei Bedarf erweiterte/NVENC-Änderungen über den dokumentierten Wiederherstellungsablauf wieder her, **bevor** Sie die App entfernen. Die Wiederherstellung lehnt widersprüchliche Änderungen von einem anderen Tool ab.

Lokale Daten liegen unter `%LOCALAPPDATA%\NVDriverForge`; Geschützte Jobs und Treiberexporte liegen unter `%PROGRAMDATA%\NVDriverForge\Jobs`. Durch den mobilen Einsatz entstehen auch lokale Daten. Der Treiberspeicherexport und die native Profilsicherung sind getrennt. Es handelt sich auch nicht um ein Systemabbild.

<a id="known-limitations"></a>
## Bekannte Einschränkungen

- Keine Hardware-Ergänzungen/INF-Bearbeitung, neu generierte NVIDIA-Signaturen, Anti-Cheat-kompatibles Zurücktreten oder automatische Akzeptanz von unsignierten Warnungen.
- Keine vollständige Telemetrie-/Werbungsentfernung, Slim-Package-Export oder automatisches vollständiges Rollback auf den vorherigen Treiber.
- Treiberinstallation, Boot-Wiederherstellung und optionale Profilschreibvorgänge wurden durch das Hub-Audit auf realen Maschinen nicht umfassend validiert.
- Das Zurücklesen der Registrierung ist kein Beweis für tatsächliche HDCP-, Leistungs- oder Latenzeffekte.
- Signaturprüfungen verwenden die lokal verfügbare Windows-Vertrauensstellung; Ein Online-Widerruf wird nicht durchgeführt.
- Es sind 34 Sprachen vorhanden, die vollständige Prüfung auf Muttersprachler/Barrierefreiheit ist jedoch noch unvollständig.

<a id="troubleshooting"></a>
## Fehlerbehebung

| Symptom | Aktion |
| --- | --- |
| Online-Katalog nicht verfügbar | Wählen Sie ein Originalpaket aus [NVIDIA-Treiber-Downloads](https://www.nvidia.com/en-us/drivers/) aus. Ersetzen Sie es nicht durch ein benachbartes GPU-Modell. |
| Hotfix-Suche nicht verfügbar | Verwenden Sie [NVIDIAs Game Ready-Treiberforum](https://www.nvidia.com/en-us/geforce/forums/game-ready-drivers/13/) und überprüfen Sie das tatsächliche Paket. |
| Die Installation von NVIDIA schlägt fehl | Lesen Sie die Fehlerzusammenfassung und öffnen Sie die detaillierten Protokolle. Optionale Komponenten, die bereits aktuell oder nicht anwendbar sind, können in 0.1.4 weiterhin übersprungen werden. Fehlgeschlagene Installationen lösen keine optionalen Optimierungen oder einen Erfolgs-/Neustartablauf aus. |
| Signatur-/Hash-/Backup-Fehler | Stoppen Sie die Installation und behalten Sie den Fehler bei. Besorgen Sie sich das Originalpaket erneut, wenn es beschädigt ist. |
| Option nicht verfügbar | Lesen Sie den Grund für die Hardware, Komponente oder den Zieltreiber. Behalten Sie es unverändert bei. |
| Neustart oder Job steht noch aus | Verwenden Sie die Wiederherstellungsanweisungen und den expliziten Lebenslauf des Jobs. Lösche nicht sein Tagebuch. |
| Konflikt wiederherstellen | Ein anderer Status weicht von der erfassten Transaktion ab. Behalten Sie es und fordern Sie Hilfe an, anstatt eine Wiederherstellung zu erzwingen. |

Geben Sie für Berichte die ausgewählte Toolversion, Windows, GPU, den Treiber und reproduzierbare Schritte an. Entfernen Sie Pfade und persönliche Daten aus Protokollen. [Unterstützung](../docs/support.md).

<a id="faq"></a>
## FAQ

**Installiert Setup einen Grafiktreiber?** Nein. Dies erfordert eine separate Analyse, Überprüfung, Bestätigung und einen erweiterten Installationsprozess der Anwendung.

**Benötige ich NVCleanstall oder NVPI?** Nein. NVCleanstall dient nur zur Inspiration. Der Profile Inspector-Begleiter ist ein unabhängiger optionaler Editor.

**Wird dadurch jeder NVIDIA-Treiber kleiner oder schneller?** Nein. Ausgewählte Komponenten und Voraussetzungen bestimmen, was sich ändern kann; Es wird kein gemessener Gewinn versprochen.

**Wo sind die Quellen?** Anwendungsspezifische Quellen und private Tests werden separat verwaltet. Dieser Hub stellt Dokumentation, Binärdateien und Quelllinks von Drittanbietern bereit, die für die Namensnennung/Lizenzierung erforderlich sind.

<a id="credits-and-upstream"></a>
## Credits und Upstream

Ursprüngliche Anwendung, Workflow, Transaktionen, Lokalisierung, Bootstrap und Anpassungen: 禅堂 Zendo (RevoluSound Team).

- [NVCleanstall / TechPowerUp](https://www.techpowerup.com/download/techpowerup-nvcleanstall/): Workflow-Inspiration; Keine Quelle oder Binärdatei importiert.
- [NVIDIA Profile Inspector / Orbmu2k](https://github.com/Orbmu2k/nvidiaProfileInspector): MIT-Themen, erweiterte NVAPI-Schnittstellenreferenz und separat verpacktes fork.
- [7-Zip / Igor Pavlov](https://www.7-zip.org/): unveränderte Extraktionswerkzeuge.
- [Microsoft .NET](https://github.com/dotnet/runtime) und [WPF](https://github.com/dotnet/wpf): gebündelte Laufzeit.
- [Inno Setup](https://jrsoftware.org/isinfo.php): Original-Installations-Engine und gutgeschriebene Übersetzungen.
- [keylase/nvidia-patch](https://github.com/keylase/nvidia-patch): externe optionale NVENC-Datenquelle; Weiterverbreitungslizenz nicht eingerichtet.
- [NVIDIA](https://www.nvidia.com/en-us/drivers/): Externe Treiber-Downloads und installierte NVAPI/NVML-Bibliotheken.

[Vollständige Komponententabelle](../THIRD_PARTY_NOTICES.md) · [Veränderungen und Herkunft](../docs/provenance.md)

<a id="license"></a>
## Lizenz

[Vorhandene Binärverteilungsberechtigung](../../../../NVDriverForge/LICENSE) erlaubt die Verwendung und Weitergabe unveränderter offizieller ausführbarer Dateien mit ihren Hinweisen. Anwendungsspezifische Quellrechte bleiben vorbehalten. Die Rechte, die durch die separaten Lizenzen Dritter gewährt werden, werden dadurch nicht eingeschränkt. [Vollständige Mitteilungen](LICENSES/README.md).

Unabhängig von NVIDIA Corporation, TechPowerUp und keylase; nicht von ihnen gesponsert oder offiziell unterstützt. Produktnamen bleiben Marken ihrer Eigentümer.
