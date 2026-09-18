<!-- nv-language-navigation:start -->
🌐 [English](../../../releasing.md) | [Français](../../../releasing.fr.md) · [NV Laboratory](../README.md)

<details>
<summary>🌐 Language · 34</summary>

[العربية](../../ar/docs/releasing.md) · [বাংলা](../../bn/docs/releasing.md) · [简体中文](../../zh/docs/releasing.md) · [Čeština](../../cs/docs/releasing.md) · [Dansk](../../da/docs/releasing.md) · [Nederlands](../../nl/docs/releasing.md) · [English](../../../releasing.md) · [Filipino](../../fil/docs/releasing.md) · [Suomi](../../fi/docs/releasing.md) · [Français](../../../releasing.fr.md) · **Deutsch** · [Ελληνικά](../../el/docs/releasing.md) · [हिन्दी](../../hi/docs/releasing.md) · [Magyar](../../hu/docs/releasing.md) · [Bahasa Indonesia](../../id/docs/releasing.md) · [Italiano](../../it/docs/releasing.md) · [日本語](../../ja/docs/releasing.md) · [한국어](../../ko/docs/releasing.md) · [मराठी](../../mr/docs/releasing.md) · [فارسی](../../fa/docs/releasing.md) · [Polski](../../pl/docs/releasing.md) · [Português](../../pt/docs/releasing.md) · [ਪੰਜਾਬੀ](../../pa/docs/releasing.md) · [Română](../../ro/docs/releasing.md) · [Русский](../../ru/docs/releasing.md) · [Español](../../es/docs/releasing.md) · [Kiswahili](../../sw/docs/releasing.md) · [Svenska](../../sv/docs/releasing.md) · [தமிழ்](../../ta/docs/releasing.md) · [ไทย](../../th/docs/releasing.md) · [Türkçe](../../tr/docs/releasing.md) · [Українська](../../uk/docs/releasing.md) · [اردو](../../ur/docs/releasing.md) · [Tiếng Việt](../../vi/docs/releasing.md)

[Translation policy](../../README.md)

</details>
<!-- nv-language-navigation:end -->

<!-- nv-translation-notice:start -->
> Maschinell unterstützte Übersetzung aus dem Englischen. Technische Namen, Befehle, URLs und ursprüngliche Rechtstexte bleiben erhalten. Eine Rezension durch einen Muttersprachler ist willkommen; Konsultieren Sie die englische Referenz, wenn der Wortlaut unklar ist.
<!-- nv-translation-notice:end -->

<a id="publishing-and-releases"></a>
# Veröffentlichungen und Veröffentlichungen

Das öffentliche Repository ist **Zendo-GIT/NV-Laboratory**. Dokumentationsänderungen werden vom Betreuer mit **GitHub Desktop** überprüft, festgeschrieben und gepusht. Bei einem lokalen Commit werden keine Dateien hochgeladen. Binärpakete sind separate GitHub-Release-Assets; Sie gehören nie in die Git-Änderungsliste.

<a id="documentation-updates"></a>
## Aktualisierungen der Dokumentation

1. Öffnen Sie den Ordner **NV-Laboratory** in GitHub Desktop.
2. Überprüfen Sie Dokumentation, Hinweise, Bilder, JSON-Metadaten und den Dokumentationsvalidator.
3. Führen Sie `python tools/validate_repository.py` aus diesem Ordner aus.
4. Übernehmen Sie die überprüften Änderungen und verwenden Sie dann **Push origin**. Überprüfen Sie das Ergebnis der Aktionen.
5. Behalten Sie die öffentliche Autoridentität **禅堂 Zendo (RevoluSound Team)** und die Adresse GitHub `noreply` des Kontos bei.

Wählen Sie niemals den übergeordneten Entwicklungsarbeitsbereich, das private Prüfverzeichnis oder das Verzeichnis für binäre Anhänge aus. [Setzen Sie E-Mail-Datenschutz ein](https://docs.github.com/en/account-and-profile/how-tos/email-preferences/setting-your-commit-email-address).

<a id="independent-application-releases"></a>
## Unabhängige Anwendungsversionen

| Werkzeug | Etikett | Versionsrichtlinie |
| --- | --- | --- |
| NVIDIA Profile Inspector – NV Tools Fork | nvpi-v3.0.2.3 | Vorhandene vierteilige Antragsversion; Setup-Revision 2 hat einen eigenen Dateinamen |
| NVDriverForge | nvdriverforge-v0.1.4 | Vorhandenes 0.x-Schema; Bei versionierten Updates bleiben frühere Pakete erhalten |
| NVMFG Unlock40 | nvmfg-unlock40-v0.2.3 | Anwendungsversion 0.2.3; kumulative Änderungen seit öffentlichem 0.1.1 |
| NVRasterPulse | nvrasterpulse-v0.2 | Vorhandene zweiteilige Version |

Der Betreuer kann die geprüften Assets direkt veröffentlichen oder einen Assistenten mit der Veröffentlichung beauftragen. Die Veröffentlichung erfolgt explizit; Kein Workflow erstellt bei jedem Commit ein Release.

1. Sehen Sie sich den aktuellen Vorveröffentlichungsbericht, die Quellen der Binärdateien, Lizenzen und SHA-256-Werte an.
2. Erstellen Sie einen Entwurf für das Tag des Tools, der auf den überprüften Hub-Commit abzielt. Fügen Sie die vorbereiteten versionspezifischen Versionshinweise bei.
3. Hängen Sie nur die Setup-/tragbaren Assets dieser Version an, `Licenses-and-Credits.zip` und `SHA256SUMS.txt`.
4. Überprüfen Sie Kompatibilität, Installation, Abhängigkeiten, Änderungen und bekannte Grenzen. Halten Sie RTSS für NVRasterPulse im Vordergrund.
5. Veröffentlichen Sie, überprüfen Sie die URLs, Größen und Hashes der öffentlichen Assets und zeichnen Sie das tatsächliche Veröffentlichungsdatum in `docs/releases.json` auf.
6. Aktualisieren Sie die Download-Seiten und Übersetzungen und übernehmen/pushen Sie dann ihre Änderungen in GitHub Desktop.

Durch die projektspezifischen Tag-Links wird vermieden, dass Benutzer über einen gemeinsam genutzten `releases/latest`-Link zu einem anderen Tool weitergeleitet werden. Die automatischen **Source code**-Archive von GitHub enthalten diesen Dokumentations-Hub. Anwendungsquellen bleiben privat. Die ursprünglichen Komponentenhinweise bleiben erhalten und eine Veröffentlichung löst nicht die dokumentierte NVIDIA SDK-Reserve von NVMFG auf.


Das Update vom 18. September bereitet drei neue Tags vor; Die bestehende Profile Inspector-Version bleibt unverändert. Asset-Namen, Tags und `SHA256SUMS.txt` müssen für die Anwendungsaktualisierungsprüfungen exakt bleiben. Veröffentlichen Sie normale Releases ohne das Prerelease-Flag, um sie den Stable-Release-Prüfungen auszusetzen. NVMFG bleibt experimentell.

<a id="integrity-and-storage"></a>
## Integrität und Speicherung

Ersetzen Sie veröffentlichte Binärbytes niemals stillschweigend. Verwenden Sie eine neue explizite Version oder Installer-Revision mit neuen Hashes. Legal Sidecars ergänzen eingebettete Hinweise. NVDriverForge 0.1.4 portable ist 142.017.891 Bytes groß und liegt damit über dem normalen 100-MiB-Git-Dateilimit von GitHub. Release-Anhänge vermeiden das Einfügen von Binärdateien oder Git LFS in diesen Hub. [GitHub Anleitung für große Dateien](https://docs.github.com/en/repositories/working-with-files/managing-large-files/about-large-files-on-github).

Die private Schwachstellenberichterstattung sollte in den Repository-Sicherheitseinstellungen aktiviert sein. Überprüfen Sie die Verfügbarkeit, bevor Sie sensible Berichte dorthin weiterleiten. [SECURITY.md](../SECURITY.md) bietet einen Fallback, der keine Schwachstellendetails offenlegt.

[Katalog herunterladen](downloads.md) · [GitHub-Release-Dokumentation](https://docs.github.com/en/repositories/releasing-projects-on-github/managing-releases-in-a-repository)
