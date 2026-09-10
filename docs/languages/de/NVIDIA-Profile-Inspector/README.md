<!-- nv-language-navigation:start -->
🌐 [English](../../../../NVIDIA-Profile-Inspector/README.md) | [Français](../../../../NVIDIA-Profile-Inspector/README.fr.md) · [NV Laboratory](../README.md)

<details>
<summary>🌐 Language · 34</summary>

[العربية](../../ar/NVIDIA-Profile-Inspector/README.md) · [বাংলা](../../bn/NVIDIA-Profile-Inspector/README.md) · [简体中文](../../zh/NVIDIA-Profile-Inspector/README.md) · [Čeština](../../cs/NVIDIA-Profile-Inspector/README.md) · [Dansk](../../da/NVIDIA-Profile-Inspector/README.md) · [Nederlands](../../nl/NVIDIA-Profile-Inspector/README.md) · [English](../../../../NVIDIA-Profile-Inspector/README.md) · [Filipino](../../fil/NVIDIA-Profile-Inspector/README.md) · [Suomi](../../fi/NVIDIA-Profile-Inspector/README.md) · [Français](../../../../NVIDIA-Profile-Inspector/README.fr.md) · **Deutsch** · [Ελληνικά](../../el/NVIDIA-Profile-Inspector/README.md) · [हिन्दी](../../hi/NVIDIA-Profile-Inspector/README.md) · [Magyar](../../hu/NVIDIA-Profile-Inspector/README.md) · [Bahasa Indonesia](../../id/NVIDIA-Profile-Inspector/README.md) · [Italiano](../../it/NVIDIA-Profile-Inspector/README.md) · [日本語](../../ja/NVIDIA-Profile-Inspector/README.md) · [한국어](../../ko/NVIDIA-Profile-Inspector/README.md) · [मराठी](../../mr/NVIDIA-Profile-Inspector/README.md) · [فارسی](../../fa/NVIDIA-Profile-Inspector/README.md) · [Polski](../../pl/NVIDIA-Profile-Inspector/README.md) · [Português](../../pt/NVIDIA-Profile-Inspector/README.md) · [ਪੰਜਾਬੀ](../../pa/NVIDIA-Profile-Inspector/README.md) · [Română](../../ro/NVIDIA-Profile-Inspector/README.md) · [Русский](../../ru/NVIDIA-Profile-Inspector/README.md) · [Español](../../es/NVIDIA-Profile-Inspector/README.md) · [Kiswahili](../../sw/NVIDIA-Profile-Inspector/README.md) · [Svenska](../../sv/NVIDIA-Profile-Inspector/README.md) · [தமிழ்](../../ta/NVIDIA-Profile-Inspector/README.md) · [ไทย](../../th/NVIDIA-Profile-Inspector/README.md) · [Türkçe](../../tr/NVIDIA-Profile-Inspector/README.md) · [Українська](../../uk/NVIDIA-Profile-Inspector/README.md) · [اردو](../../ur/NVIDIA-Profile-Inspector/README.md) · [Tiếng Việt](../../vi/NVIDIA-Profile-Inspector/README.md)

[Translation policy](../../README.md)

</details>
<!-- nv-language-navigation:end -->

<!-- nv-translation-notice:start -->
> Maschinell unterstützte Übersetzung aus dem Englischen. Technische Namen, Befehle, URLs und ursprüngliche Rechtstexte bleiben erhalten. Eine Rezension durch einen Muttersprachler ist willkommen; Konsultieren Sie die englische Referenz, wenn der Wortlaut unklar ist.
<!-- nv-translation-notice:end -->

<a id="nvidia-profile-inspector--nv-tools-fork"></a>
# NVIDIA Profile Inspector – NV Tools Fork

**Ein unabhängiger fork von [NVIDIA Profile Inspector von Orbmu2k](https://github.com/Orbmu2k/nvidiaProfileInspector), mit zusätzlichen Anzeigesteuerungen.** Ehemaliger Projektname: **NVPI Custom**.

[Download- und Veröffentlichungsstatus](../docs/downloads.md#nvidia-profile-inspector) · [Installation](#installation) · [Upstream und Änderungen](#upstream-and-changes) · [Lizenz](../../../../NVIDIA-Profile-Inspector/LICENSE)

<a id="overview"></a>
## Übersicht

Die Anwendung bearbeitet NVIDIA-Treiberprofile, einschließlich anwendungsspezifischer Einstellungen. Dieser fork fügt außerdem einen **Bildschirm**-Editor für die aktive Windows-Anzeige hinzu: Auflösung, Bildwiederholfrequenz, Ausgabefarbeinstellungen, HDR und installierte ICC/WCS-Profilzuordnungen.

Es dient dazu, zugehörige Anzeigesteuerungen in den Profileditor zu integrieren und Vorschau-, Bestätigungs- und Wiederherstellungsergebnisse klarer zu gestalten. Es werden keine neuen Hardwarefunktionen geschaffen.

Der erste Kandidat ist **3.0.2.3** und verwendet den bereinigten Standalone-Companion-Build vom 9. September 2026. Die vorhandene ausführbare Datei bleibt `nvidiaProfileInspector.exe`; Das Installationsprogramm und einige interne Beschriftungen sagen immer noch `NVPI Custom NV`. Der obige öffentliche Titel identifiziert den fork, ohne die Installationsidentität zu ändern oder vorzugeben, dass es sich um die offizielle Version von Orbmu2k handelt.

<a id="features"></a>
## Funktionen

- Durchsuchen vorhandener Upstream-Profile, Anwendungszuordnungen, Einstellungsänderungen und Profilimport/-export.
- **Bildschirm**-Dialogfeld für Anzeige, Modus, Hz, RGB/YCbCr, Farbtiefe, Bereich und Farbmetrik.
- Windows HDR-Steuerung und installierte ICC/WCS-Zuordnungsauswahl.
- Eine 15-sekündige Anzeigevorschau mit **Behalten** / **Zurücksetzen** und Timeout-Wiederherstellung.
- Rücklesen von Modus-/HDR-Änderungen und gemeldeten Wiederherstellungsfehlern.
- Separate Meldung von HDR, SDR mit ACM/WCG und Signalfarbtiefe.
- Ein NVRasterPulse-Launcher für eine berechtigte, separat installierte Kopie.

<a id="compatibility"></a>
## Kompatibilität

| Anforderung | Einzelheiten |
| --- | --- |
| System | Windows 10/11 x64 mit einem kompatiblen NVIDIA-Treiber |
| Laufzeit | [.NET Framework 4.8](https://dotnet.microsoft.com/en-us/download/dotnet-framework/net48), geliefert von Windows oder separat installiert |
| Berechtigungen | Der Editor fordert beim Öffnen Administratorzugriff an |
| Zeigt an | Die tatsächlichen Modi und Farbkombinationen hängen von den GPU-, Treiber-, Display-, Kabel- und Windows-APIs ab |
| Optionale Werkzeuge | NVRasterPulse für RTSS-Limitverwaltung; Weder es noch RTSS werden für den Bildschirmeditor benötigt |
| Sprachen | Einrichtung: 34-Sprachen-Auswahl. Der Editor behält seine bestehende Sprachunterstützung. |

Für jedes GPU gibt es kein verifiziertes universelles Treiberminimum oder keine Unterstützungsmatrix. Die im Dialog verfügbaren BPC-Auswahlmöglichkeiten sind Anfragen, keine zertifizierten Kombinationen. Moderne HDR-Steuerungen und das ältere Windows-Fallback verfügen über unterschiedliche Funktionen.

<a id="installation"></a>
## Installation

1. Öffnen Sie [Download-Seite](../docs/downloads.md#nvidia-profile-inspector) und überprüfen Sie den Veröffentlichungsstatus.
2. Laden Sie das Setup oder das tragbare Asset herunter und vergleichen Sie dessen SHA-256 mit dem Release-Manifest.
3. Führen Sie für das Setup `NVPI-CustomNV-3.0.2.3-Setup-r2.exe` aus, wählen Sie eine Sprache aus und folgen Sie dem Installationsprogramm. Es erstellt eine eigene Verknüpfung und ein eigenes Deinstallationsprogramm.
4. Extrahieren Sie für tragbare Dateien die vollständige ZIP-Datei in einen neuen beschreibbaren Ordner. Bewahren Sie `Reference.xml`, die EXE-Konfiguration und alle Hinweise neben der ausführbaren Datei auf.
5. Starten Sie `nvidiaProfileInspector.exe`.

Durch die alleinige Installation des Editors wird weder ein Profil angewendet noch ein GPU-Treiber installiert. Der Begleiter wird separat installiert, übernimmt keine `.nip`-Zuordnungen und ermöglicht keinen Start bei der Anmeldung. Vorhandene Binärdateien sind nicht signiert.

<a id="usage"></a>
## Nutzung

**Installer-Revision 2** fügt die gleiche native 34-Sprachen-Auswahl wie die anderen Tools hinzu, mit Maus-/Tastaturnavigation, Hell-/Dunkel-Darstellung und Abbruch. Die Auswahl gilt für das Setup; Der NVPI-Editor wird nicht übersetzt. Ein explizites `/LANG=fr`-Argument oder ein stiller Modus umgeht die Auswahl für Aufrufer, die bereits eine Sprache bereitstellen.

**Treiberprofile:** Wählen Sie ein Profil aus, exportieren Sie ein Backup, bearbeiten Sie dann nur die beabsichtigten Einstellungen und wenden Sie sie an. Anwendungszuordnungen bestimmen, welches Spiel ein Profil erhält. Ein gespeicherter Wert ist kein Beweis dafür, dass jeder Treiber oder jedes Spiel ihn verwendet.

**Anzeigesteuerung:** Öffnen Sie **Bildschirm**, wählen Sie die Anzeige und die gewünschten Werte aus und starten Sie dann die Vorschau. Überprüfen Sie das Bild, bevor Sie innerhalb von 15 Sekunden **Behalten** wählen. Verwenden Sie **Zurücksetzen**, schließen Sie die Bestätigung oder lassen Sie sie ablaufen, um eine Wiederherstellung anzufordern. Lesen Sie alle Fehlermeldungen: Ein erfolgreicher API-Aufruf allein ist kein Beweis für die Wiederherstellung.

Eine ICC-Auswahl ändert eine installierte Profilzuordnung; Es wird keine ICC-Datei generiert, kalibriert oder weitergegeben. HDR, ACM/WCG, RGB/YCbCr und bpc beschreiben verschiedene Aspekte der Pipeline. Es ist kein neuer unabhängiger ACM-Schalter vorgesehen.

**NVRasterPulse:** Die Symbolleistenschaltfläche akzeptiert eine separat registrierte systemweite Installation unter „Programme“ mit geschützten Eigentumsrechten und Berechtigungen. Eine tragbare Kopie oder ein vom Benutzer beschreibbarer/verknüpfter Pfad kann von diesem erhöhten Launcher abgelehnt werden. Öffnen Sie in diesem Fall NVRasterPulse mit einer eigenen Verknüpfung. [Installieren Sie RTSS separat](https://www.guru3d.com/download/rtss-rivatuner-statistics-server-download/) zur Verwendung von NVRasterPulse.

<a id="screenshots"></a>
## Screenshots

![NVPI Setup Revision 2 Sprachauswahl](../../../../assets/screenshots/nvpi-setup-r2-language.png)

Tatsächlicher Setup-Selektor auf Französisch, während eines isolierten Tests erfasst und dann abgebrochen. Dies zeigt das Installationsprogramm; Der Editor behält seine Benutzeroberfläche und seinen Bildschirmdialog.

<a id="update-and-uninstall"></a>
## Aktualisieren und deinstallieren

Schließen Sie den Editor vor dem Aktualisieren. Behalten Sie exportierte Profile bei und laden Sie die neue Version fork herunter. über dieselbe Companion-Identität installieren oder tragbare Dateien in einen neuen Ordner extrahieren. Mischen Sie kein altes `Reference.xml` mit einer neuen ausführbaren Datei. Zu diesem fork gehört die gebündelte Upstream-Update-Check-Unterdrückung.

Für eine installierte Kopie verwenden Sie Windows **Installed apps** und das zugehörige Deinstallationsprogramm. Wenn Sie ein tragbares Gerät verwenden, schließen Sie es und entfernen Sie den extrahierten Ordner, wenn Ihre Exporte sicher sind. Durch das Entfernen des Editors werden Änderungen an Treiberprofilen, Anzeigeeinstellungen, NVRasterPulse oder RTSS **nicht** rückgängig gemacht. Stellen Sie vor dem Entfernen die gewünschten Einstellungen wieder her.

<a id="known-limitations"></a>
## Bekannte Einschränkungen

- Die 15-Sekunden-Bestätigung dient nicht als Überwachungsmaßnahme für jeden Fahrerabsturz, jeden Stromausfall oder jedes erzwungene Herunterfahren.
- Einige Farb-/Tiefe-/Aktualisierungskombinationen geben `NVAPI_NOT_SUPPORTED` zurück.
- Beim Software-Rücklesen werden weder die Bittiefe, die Farbgenauigkeit noch die Latenz des Panels gemessen.
- Die Bildschirmeinstellungen wirken sich auf die aktuelle Windows-Anzeige aus; In diesem Dialogfeld werden keine spielspezifischen Anzeigevoreinstellungen erstellt.
- Keine Leistungs-, Anti-Cheat- oder universelle HDR-Kompatibilitätsgarantie.

<a id="troubleshooting"></a>
## Fehlerbehebung

| Symptom | Aktion |
| --- | --- |
| Laufzeitfehler beim Start | Überprüfen Sie Windows-Updates und .NET Framework 4.8; Nutzen Sie das Komplettpaket. |
| Angeforderter Anzeigemodus abgelehnt | Setzen Sie einen von Windows/NVIDIA für diese Anzeige angebotenen Modus zurück und testen Sie ihn. Lesen Sie den genauen Fehler und vermeiden Sie wiederholte blinde Änderungen. |
| HDR oder Farbe kehrt zum alten Zustand zurück | Überprüfen Sie, ob ein anderer Vorgang fehlgeschlagen ist und eine Wiederherstellung ausgelöst hat. Unterscheiden Sie HDR von ACM. |
| Die Schaltfläche NVRasterPulse lehnt einen Pfad ab | Starten Sie eine eigene Verknüpfung. Für diese Schaltfläche ist eine geschützte systemweite Installation erforderlich. |
| Eine Änderung bleibt nach der Deinstallation bestehen | Stellen Sie das exportierte NVIDIA-Profil oder die beabsichtigten Windows-Anzeigeeinstellungen wieder her. Bei der Deinstallation handelt es sich nicht um ein Zurücksetzen der Einstellungen. |

Sehen Sie sich [Gemeinsame Support-Anleitung](../docs/support.md) an, bevor Sie Protokolle senden.

<a id="faq"></a>
## FAQ

**Ist dies die offizielle NVIDIA-Software oder der offizielle Build von Orbmu2k?** Nein. Es handelt sich um ein unabhängiges fork; Der Upstream-Autor und die MIT-Lizenz bleiben gutgeschrieben.

**Benötigt NVDriverForge diesen Editor?** Nein. Die optionale Custom NV-Voreinstellung von NVDriverForge verwendet eine eigene Integration. Die Installation des Editors ist eine separate Option.

**Ist RTSS für diesen fork obligatorisch?** Nein. RTSS ist für den FPS-Limiter von NVRasterPulse obligatorisch, nicht für die Profil- oder Bildschirmbearbeitung.

**Wo ist die Quelle?** Die geänderte Anwendungsquelle wird privat verwaltet. Der MIT-Hinweis und das Upstream-Repository werden bereitgestellt; MIT erfordert keine Veröffentlichung der geänderten Quelle.

<a id="upstream-and-changes"></a>
## Upstream und Änderungen

Upstream: [Orbmu2k/nvidiaProfileInspector](https://github.com/Orbmu2k/nvidiaProfileInspector), Referenz-Commit `592d962cca8827efe8859461a84267755595064a`. [Original-Downloads](https://github.com/Orbmu2k/nvidiaProfileInspector/releases).

Geerbt: Profileditor, NVAPI-Interop, Referenzdaten, UI-Ressourcen und Themen. 禅堂 Zendo (RevoluSound Team) hat Anzeigedienste, HDR/ICC-Transaktionen, 15-Sekunden-Bestätigung/Rücklesen, Symbolleistenlayout und RasterPulse-Startverhalten hinzugefügt oder angepasst. Der bereinigte Begleiter schließt Entwicklungsmocks/Testeinstiegspunkte aus, verwendet einen geschützten externen Launcher und stellt einen separaten Installer bereit. Das alte kombinierte NVPI/RasterPulse-Entwicklungspaket ist in diesem Hub nicht der Kandidat.

[Detaillierte Aktenherkunft](../docs/provenance.md) · [Originaler fork-Hinweis](../../../../NVIDIA-Profile-Inspector/LICENSES/ORIGINAL-FORK-NOTICE.txt)

<a id="credits-and-license"></a>
## Credits und Lizenz

Copyright (c) 2016 Orbmu2k. Das mitgelieferte [MIT-Lizenz](../../../../NVIDIA-Profile-Inspector/LICENSE) bleibt erhalten. Anpassungen und Verpackung: 禅堂 Zendo (RevoluSound Team). Das Installationsprogramm verwendet Inno Setup; Windows und .NET Framework bleiben extern. [Vollständige anwendbare Hinweise](LICENSES/README.md).

Unabhängig von NVIDIA Corporation, nicht gesponsert und nicht offiziell unterstützt. Marken verbleiben bei ihren jeweiligen Eigentümern.
