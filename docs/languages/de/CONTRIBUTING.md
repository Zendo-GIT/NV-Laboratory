<!-- nv-language-navigation:start -->
🌐 [English](../../../CONTRIBUTING.md) | [Français](../fr/CONTRIBUTING.md) · [NV Laboratory](README.md)

<details>
<summary>🌐 Language · 34</summary>

[العربية](../ar/CONTRIBUTING.md) · [বাংলা](../bn/CONTRIBUTING.md) · [简体中文](../zh/CONTRIBUTING.md) · [Čeština](../cs/CONTRIBUTING.md) · [Dansk](../da/CONTRIBUTING.md) · [Nederlands](../nl/CONTRIBUTING.md) · [English](../../../CONTRIBUTING.md) · [Filipino](../fil/CONTRIBUTING.md) · [Suomi](../fi/CONTRIBUTING.md) · [Français](../fr/CONTRIBUTING.md) · **Deutsch** · [Ελληνικά](../el/CONTRIBUTING.md) · [हिन्दी](../hi/CONTRIBUTING.md) · [Magyar](../hu/CONTRIBUTING.md) · [Bahasa Indonesia](../id/CONTRIBUTING.md) · [Italiano](../it/CONTRIBUTING.md) · [日本語](../ja/CONTRIBUTING.md) · [한국어](../ko/CONTRIBUTING.md) · [मराठी](../mr/CONTRIBUTING.md) · [فارسی](../fa/CONTRIBUTING.md) · [Polski](../pl/CONTRIBUTING.md) · [Português](../pt/CONTRIBUTING.md) · [ਪੰਜਾਬੀ](../pa/CONTRIBUTING.md) · [Română](../ro/CONTRIBUTING.md) · [Русский](../ru/CONTRIBUTING.md) · [Español](../es/CONTRIBUTING.md) · [Kiswahili](../sw/CONTRIBUTING.md) · [Svenska](../sv/CONTRIBUTING.md) · [தமிழ்](../ta/CONTRIBUTING.md) · [ไทย](../th/CONTRIBUTING.md) · [Türkçe](../tr/CONTRIBUTING.md) · [Українська](../uk/CONTRIBUTING.md) · [اردو](../ur/CONTRIBUTING.md) · [Tiếng Việt](../vi/CONTRIBUTING.md)

[Translation policy](../README.md)

</details>
<!-- nv-language-navigation:end -->

<!-- nv-translation-notice:start -->
> Maschinell unterstützte Übersetzung aus dem Englischen. Technische Namen, Befehle, URLs und ursprüngliche Rechtstexte bleiben erhalten. Eine Rezension durch einen Muttersprachler ist willkommen; Konsultieren Sie die englische Referenz, wenn der Wortlaut unklar ist.
<!-- nv-translation-notice:end -->

<a id="contributing"></a>
# Mitwirken

NV Laboratory wird von 禅堂 Zendo (RevoluSound Team) verwaltet. Der Betreuer entscheidet, was akzeptiert und freigegeben wird. Das Öffnen einer Ausgabe oder eines Pull-Requests bedeutet nicht, dass ein Beitrag angenommen oder zur Verteilung autorisiert wird.

Verwenden Sie das Bug- oder Feature-Formular und identifizieren Sie das Programm/die Version. Suchen Sie zuerst nach vorhandenen Problemen. Besprechen Sie wesentliche Änderungen, bevor Sie einen großen Beitrag vorbereiten. Befolgen Sie aus Sicherheitsgründen [SECURITY.md](SECURITY.md).

Dieser öffentliche Hub enthält Dokumentation, Hinweise, Release-Metadaten und Repository-Validierung. Anwendungsquelle und Tests werden privat verwaltet. Senden Sie keinen dekompilierten Code, keine privaten Quellen, Anmeldeinformationen, Benutzerprofile oder ausführbaren Nutzlasten.

Dokumentations-PRs sollten die 34 Sprachgegenstücke und die Navigation aufeinander abstimmen, Befehls-/Datei-/Produktnamen beibehalten und das tatsächliche Verhalten beschreiben. Neue Screenshots müssen von Ihnen stammen, versioniert sein und keine persönlichen Daten enthalten; Synthetische Daten müssen gekennzeichnet werden. Geben Sie Herkunft und Erlaubnis für jedes neue Asset Dritter an.

Verwenden Sie UTF-8, LF, lesbaren Markdown und kleine gezielte Änderungen. Der Python-Validator verwendet nur die Standardbibliothek. Passen Sie es an den vorhandenen Stil an, vermeiden Sie unnötige Abhängigkeiten und führen Sie Folgendes aus:

```text
python tools/validate_repository.py
```

Geben Sie bei Änderungen der Release-Metadaten die genaue Version/das genaue Tag, die Dateigrößen und SHA-256 aus den geprüften Binärdateien an und achten Sie darauf, dass die Download-Seiten ausgerichtet sind. Anwendungsänderungen erfordern private Builds/Tests, die dem betroffenen Verhalten entsprechen; Eine Dokumentationsprüfung ist kein Anwendungstest. Erfinden Sie niemals historische Testergebnisse oder Gewinne.

Durch die Bereitstellung von Original-Hub-Material stimmen Sie der eingeschränkten MIT-Lizenz in [LIZENZ](../../../LICENSE) zu. Bewahren Sie Mitteilungen Dritter auf und identifizieren Sie Ihre Änderungen. Ersetzen Sie keine Upstream-Lizenz. Annahme und Veröffentlichung bleiben Entscheidungen des Betreuers.
