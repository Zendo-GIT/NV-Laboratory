<!-- nv-language-navigation:start -->
🌐 [English](../../../README.md) | [Français](../../../README.fr.md) · [NV Laboratory](README.md)

<details>
<summary>🌐 Language · 34</summary>

[العربية](../ar/README.md) · [বাংলা](../bn/README.md) · [简体中文](../zh/README.md) · [Čeština](../cs/README.md) · [Dansk](../da/README.md) · [Nederlands](../nl/README.md) · [English](../../../README.md) · [Filipino](../fil/README.md) · [Suomi](../fi/README.md) · [Français](../../../README.fr.md) · **Deutsch** · [Ελληνικά](../el/README.md) · [हिन्दी](../hi/README.md) · [Magyar](../hu/README.md) · [Bahasa Indonesia](../id/README.md) · [Italiano](../it/README.md) · [日本語](../ja/README.md) · [한국어](../ko/README.md) · [मराठी](../mr/README.md) · [فارسی](../fa/README.md) · [Polski](../pl/README.md) · [Português](../pt/README.md) · [ਪੰਜਾਬੀ](../pa/README.md) · [Română](../ro/README.md) · [Русский](../ru/README.md) · [Español](../es/README.md) · [Kiswahili](../sw/README.md) · [Svenska](../sv/README.md) · [தமிழ்](../ta/README.md) · [ไทย](../th/README.md) · [Türkçe](../tr/README.md) · [Українська](../uk/README.md) · [اردو](../ur/README.md) · [Tiếng Việt](../vi/README.md)

[Translation policy](../README.md)

</details>
<!-- nv-language-navigation:end -->

<!-- nv-translation-notice:start -->
> Maschinell unterstützte Übersetzung aus dem Englischen. Technische Namen, Befehle, URLs und ursprüngliche Rechtstexte bleiben erhalten. Eine Rezension durch einen Muttersprachler ist willkommen; Konsultieren Sie die englische Referenz, wenn der Wortlaut unklar ist.
<!-- nv-translation-notice:end -->

<a id="nv-laboratory"></a>
# NV Laboratory

**NV Tools von 禅堂 Zendo (RevoluSound Team).** Vier unabhängige Windows-Dienstprogramme für NVIDIA-Treiberprofile, Treiberinstallation, experimentelle Multi Frame Generation- und RTSS-Frame-Grenzwerte.

[Holen Sie sich die Werkzeuge](docs/downloads.md) · [Installation](docs/installation.md) · [Kompatibilität und Hilfe](docs/support.md) · [Credits und Lizenzen](THIRD_PARTY_NOTICES.md)

> **NVRasterPulse erfordert RTSS.** Installieren Sie zuerst [RivaTuner Statistics Server von Guru3D](https://www.guru3d.com/download/rtss-rivatuner-statistics-server-download/). RTSS muss ausgeführt werden, damit die FPS-Grenzwerte funktionieren. Es wird separat heruntergeladen.

<a id="projects"></a>
## Projekte

| Projekt | Zweck | Version | Dokumentation | Herunterladen |
| --- | --- | --- | --- | --- |
| **NVIDIA Profile Inspector – NV Tools Fork** | NVIDIA-Treiberprofileditor mit zusätzlichen Anzeige-, Farb- und HDR- und ICC/WCS-Steuerelementen. Früher NVPI Custom. | 3.0.2.3 | [Leitfaden](NVIDIA-Profile-Inspector/README.md) | [Pakete](docs/downloads.md#nvidia-profile-inspector) |
| **NVDriverForge** | Wählen Sie Treiberkomponenten aus, überprüfen Sie optionale Optimierungen und installieren Sie ein Original-NVIDIA-Treiberpaket. | 0.1.3 | [Leitfaden](NVDriverForge/README.md) | [Pakete](docs/downloads.md#nvdriverforge) |
| **NVMFG Unlock40** | Experimentelles RTX 40 MFG-Tool mit Auswahlmöglichkeiten pro Spiel und Streamline SDK-Wartung. | 0.1.1 | [Leitfaden](NVMFG-Unlock40/README.md) | [Pakete & Status](docs/downloads.md#nvmfg-unlock40) |
| **NVRasterPulse** | Verwalten Sie RTSS FPS-Limits pro ausführbarer Datei, mit Bruchwerten, Backups und Tray-Zugriff. | 0.1 | [Leitfaden](NVRasterPulse/README.md) | [Pakete](docs/downloads.md#nvrasterpulse) |

**Downloads:** Der [Download-Seite](docs/downloads.md) listet den Status, die Dateien und die SHA-256-Werte jeder Version auf. Experimentelle Funktionen und Kompatibilitätsgrenzen werden in den Projekthandbüchern beschrieben.

<a id="start-here"></a>
## Beginnen Sie hier

1. Wählen Sie oben ein Werkzeug aus. Jeder arbeitet unabhängig; Die Installation der gesamten Suite ist nicht erforderlich.
2. Lesen Sie die Anforderungen und wählen Sie **Setup** für eine installierte App oder **Portable** für einen separaten Ordner.
3. Wenn die Veröffentlichung veröffentlicht wird, laden Sie das benannte Anwendungs-Asset herunter, lesen Sie die begleitenden Hinweise und vergleichen Sie dessen SHA-256.
4. Erstellen Sie Backups, bevor Sie einen Treiber, eine Anzeigeeinstellung, ein NVIDIA-Profil oder eine Spiellaufzeit ändern.

Die Dokumentation ist in denselben 34 Sprachen wie die NV-Anwendungen über die Auswahl oben in jedem Handbuch verfügbar. GitHub wählt nicht automatisch eine README-Datei nach Browsersprache aus. Die Dokumentationssprache und die anwendungseigene Spracheinstellung sind getrennt.

<a id="provenance-and-ownership"></a>
## Provenienz und Eigentum

Dieser Hub verteilt Dokumentation und kompilierte Anwendungen. Der Quellcode der Anwendung wird privat verwaltet. Upstream-Projekte behalten ihre Urheberschaft und Lizenzen; Die private Quellenverteilung ersetzt diese Bedingungen nicht.

- Der Profile Inspector fork behält die MIT-Lizenz von Orbmu2k und wird ausdrücklich als fork identifiziert.
- NVDriverForge verfügt über eigene Binärverteilungsbedingungen und enthält separat lizenzierte Laufzeit-/Toolkomponenten.
- NVMFG Unlock40 ist eine unabhängig entwickelte Anwendung. RTX40MFG-Unlock wurde zum Vergleich und zur Verfeinerung herangezogen; Gemeinsam genutzte native Komponenten behalten ihr MIT-Guthaben. Die Bedingungen MinHook und NVIDIA SDK bleiben getrennt.
- NVRasterPulse behält die bereitgestellte MIT-Lizenz und schreibt die von Profile Inspector abgeleitete Benutzeroberfläche gut. RTSS ist ein erforderliches externes Programm.

Siehe [vollständige Komponententabelle](THIRD_PARTY_NOTICES.md), [Dateiherkunft und Änderungen](docs/provenance.md) und [Lizenzumfang](../../../LICENSE).

<a id="other-projects--revolusound-team"></a>
## Andere Projekte – RevoluSound Team

Dabei handelt es sich um separate Audio-Mod-Projekte, die hier verlinkt sind, damit Sie die Arbeit des Teams entdecken können.

| Spiel | Projekt | Über |
| --- | --- | --- |
| Forza Horizon 6 | [Forza Horizon 6 Revolusound Team Pack](https://www.nexusmods.com/forzahorizon6/mods/56) | Fahrzeuggeräuschänderungen in Bezug auf Motoren, Auspuffanlagen, Ansaugöffnungen und Turboeffekte. |
| Forza Horizon 5 | [Forza Horizon 5 Revolusound Team Pack 1.4.4 FINAL](https://www.nexusmods.com/forzahorizon5/mods/86) | Das spätere FH5-Fahrzeug-Audiopaket des Teams. |
| Forza Horizon 5 | [Forza Horizon 5.5 Zendo Revolusound Pack](https://www.nexusmods.com/forzahorizon5/mods/20) | Früheres FH5-Paket; Die Nexus-Seite leitet Besucher zum späteren Teampaket oben weiter. |

Die Titel folgen den verlinkten Nexus Mods-Seiten. Ihre Downloads, Anforderungen, Credits und Berechtigungen verbleiben auf Nexus Mods.

<a id="help-and-participation"></a>
## Hilfe und Mitmachen

[Melden Sie einen Fehler oder schlagen Sie eine Funktion vor](https://github.com/Zendo-GIT/NV-Laboratory/issues) · [Mitwirken](CONTRIBUTING.md) · [Sicherheitsberichte](SECURITY.md) · [Änderungsprotokoll](CHANGELOG.md)

Lesen Sie bei einem Sicherheitsproblem SECURITY.md, bevor Sie Protokolle oder technische Details veröffentlichen. Die private Berichterstattung muss vom Betreuer nach der Veröffentlichung des Repositorys aktiviert werden.

> **Unabhängige Gemeinschaftsprojekte.** NV Laboratory, NV Tools und diese Dienstprogramme sind nicht mit NVIDIA Corporation verbunden, werden nicht von NVIDIA Corporation gesponsert oder offiziell unterstützt. NVIDIA, GeForce, RTX, DLSS und andere Produktnamen sind Marken ihrer jeweiligen Eigentümer. Namen beschreiben Kompatibilität und Herkunft, keine offizielle Empfehlung.
