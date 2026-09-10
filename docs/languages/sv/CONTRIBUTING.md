<!-- nv-language-navigation:start -->
🌐 [English](../../../CONTRIBUTING.md) | [Français](../fr/CONTRIBUTING.md) · [NV Laboratory](README.md)

<details>
<summary>🌐 Language · 34</summary>

[العربية](../ar/CONTRIBUTING.md) · [বাংলা](../bn/CONTRIBUTING.md) · [简体中文](../zh/CONTRIBUTING.md) · [Čeština](../cs/CONTRIBUTING.md) · [Dansk](../da/CONTRIBUTING.md) · [Nederlands](../nl/CONTRIBUTING.md) · [English](../../../CONTRIBUTING.md) · [Filipino](../fil/CONTRIBUTING.md) · [Suomi](../fi/CONTRIBUTING.md) · [Français](../fr/CONTRIBUTING.md) · [Deutsch](../de/CONTRIBUTING.md) · [Ελληνικά](../el/CONTRIBUTING.md) · [हिन्दी](../hi/CONTRIBUTING.md) · [Magyar](../hu/CONTRIBUTING.md) · [Bahasa Indonesia](../id/CONTRIBUTING.md) · [Italiano](../it/CONTRIBUTING.md) · [日本語](../ja/CONTRIBUTING.md) · [한국어](../ko/CONTRIBUTING.md) · [मराठी](../mr/CONTRIBUTING.md) · [فارسی](../fa/CONTRIBUTING.md) · [Polski](../pl/CONTRIBUTING.md) · [Português](../pt/CONTRIBUTING.md) · [ਪੰਜਾਬੀ](../pa/CONTRIBUTING.md) · [Română](../ro/CONTRIBUTING.md) · [Русский](../ru/CONTRIBUTING.md) · [Español](../es/CONTRIBUTING.md) · [Kiswahili](../sw/CONTRIBUTING.md) · **Svenska** · [தமிழ்](../ta/CONTRIBUTING.md) · [ไทย](../th/CONTRIBUTING.md) · [Türkçe](../tr/CONTRIBUTING.md) · [Українська](../uk/CONTRIBUTING.md) · [اردو](../ur/CONTRIBUTING.md) · [Tiếng Việt](../vi/CONTRIBUTING.md)

[Translation policy](../README.md)

</details>
<!-- nv-language-navigation:end -->

<!-- nv-translation-notice:start -->
> Maskinassisterad översättning från engelska. Tekniska namn, kommandon, URL:er och ursprungliga lagtexter bevaras. Recension av modersmål är välkommen; konsultera den engelska referensen om formuleringen är otydlig.
<!-- nv-translation-notice:end -->

<a id="contributing"></a>
# Bidrar

NV Laboratory underhålls av 禅堂 Zendo (RevoluSound Team). Underhållaren bestämmer vad som accepteras och släpps. Att öppna ett nummer eller en Pull-förfrågan betyder inte att ett bidrag är accepterat eller auktoriserat för distribution.

Använd bugg- eller funktionsformuläret och identifiera programmet/versionen. Sök efter befintliga problem först. Diskutera väsentliga förändringar innan du förbereder ett stort bidrag. För säkerhetsfrågor, följ [SECURITY.md](SECURITY.md).

Detta offentliga nav innehåller dokumentation, meddelanden, metadata för release och validering av arkiv. Applikationskälla och tester underhålls privat. Skicka inte in dekompilerad kod, privat källa, referenser, användarprofiler eller körbara nyttolaster.

Dokumentations-PR bör hålla de 34 språkens motsvarigheter och navigering i linje, bevara kommando-/fil-/produktnamn och beskriva det faktiska beteendet. Nya skärmdumpar måste vara dina egna, versionsidentifierade och fria från personliga detaljer; syntetiska data måste märkas. Ange härkomst och tillstånd för varje ny tredjepartstillgång.

Använd UTF-8, LF, läsbar Markdown och små fokuserade ändringar. Validatorn Python använder endast standardbiblioteket. Matcha dess befintliga stil, undvik onödiga beroenden och kör:

```text
python tools/validate_repository.py
```

För ändringar i release-metadata, inkludera den exakta versionen/taggen, filstorlekarna och SHA-256 från de granskade binärfilerna, och håll nedladdningssidorna anpassade. Applikationsförändringar kräver privat konstruktion/tester som är lämpliga för det påverkade beteendet; en dokumentationskontroll är inte ett applikationstest. Uppfinn aldrig historiska testresultat eller vinster.

Genom att bidra med original navmaterial godkänner du dess omfångade MIT-licens i [LICENS](../../../LICENSE). Behåll meddelanden från tredje part och identifiera dina ändringar; ersätt inte en uppströmslicens. Godkännande och publicering förblir underhållsbeslut.
