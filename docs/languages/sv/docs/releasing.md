<!-- nv-language-navigation:start -->
🌐 [English](../../../releasing.md) | [Français](../../../releasing.fr.md) · [NV Laboratory](../README.md)

<details>
<summary>🌐 Language · 34</summary>

[العربية](../../ar/docs/releasing.md) · [বাংলা](../../bn/docs/releasing.md) · [简体中文](../../zh/docs/releasing.md) · [Čeština](../../cs/docs/releasing.md) · [Dansk](../../da/docs/releasing.md) · [Nederlands](../../nl/docs/releasing.md) · [English](../../../releasing.md) · [Filipino](../../fil/docs/releasing.md) · [Suomi](../../fi/docs/releasing.md) · [Français](../../../releasing.fr.md) · [Deutsch](../../de/docs/releasing.md) · [Ελληνικά](../../el/docs/releasing.md) · [हिन्दी](../../hi/docs/releasing.md) · [Magyar](../../hu/docs/releasing.md) · [Bahasa Indonesia](../../id/docs/releasing.md) · [Italiano](../../it/docs/releasing.md) · [日本語](../../ja/docs/releasing.md) · [한국어](../../ko/docs/releasing.md) · [मराठी](../../mr/docs/releasing.md) · [فارسی](../../fa/docs/releasing.md) · [Polski](../../pl/docs/releasing.md) · [Português](../../pt/docs/releasing.md) · [ਪੰਜਾਬੀ](../../pa/docs/releasing.md) · [Română](../../ro/docs/releasing.md) · [Русский](../../ru/docs/releasing.md) · [Español](../../es/docs/releasing.md) · [Kiswahili](../../sw/docs/releasing.md) · **Svenska** · [தமிழ்](../../ta/docs/releasing.md) · [ไทย](../../th/docs/releasing.md) · [Türkçe](../../tr/docs/releasing.md) · [Українська](../../uk/docs/releasing.md) · [اردو](../../ur/docs/releasing.md) · [Tiếng Việt](../../vi/docs/releasing.md)

[Translation policy](../../README.md)

</details>
<!-- nv-language-navigation:end -->

<!-- nv-translation-notice:start -->
> Maskinassisterad översättning från engelska. Tekniska namn, kommandon, URL:er och ursprungliga lagtexter bevaras. Recension av modersmål är välkommen; konsultera den engelska referensen om formuleringen är otydlig.
<!-- nv-translation-notice:end -->

<a id="publishing-and-releases"></a>
# Publicering och releaser

Det offentliga förvaret är **Zendo-GIT/NV-Laboratory**. Dokumentationsändringar granskas, genomförs och drivs av underhållaren med **GitHub Desktop**. En lokal commit laddar inte upp filer. Binära paket är separata GitHub Releasetillgångar; de hör aldrig hemma i Git-ändringslistan.

<a id="documentation-updates"></a>
## Uppdateringar av dokumentation

1. Öppna mappen **NV-Laboratory** i GitHub Desktop.
2. Granska dokumentation, meddelanden, bilder, JSON-metadata och dokumentationsvalideraren.
3. Kör `python tools/validate_repository.py` från den mappen.
4. Beslut de granskade ändringarna och använd sedan **Push origin**. Kontrollera åtgärdsresultatet.
5. Behåll den offentliga författaridentiteten **禅堂 Zendo (RevoluSound Team)** och kontots GitHub `noreply`-adress.

Välj aldrig den överordnade utvecklingsarbetsytan, den privata revisionskatalogen eller den binära bifogade katalogen. [Begär e-postsekretess](https://docs.github.com/en/account-and-profile/how-tos/email-preferences/setting-your-commit-email-address).

<a id="independent-application-releases"></a>
## Oberoende programversioner

| Verktyg | Tagga | Versionspolicy |
| --- | --- | --- |
| NVIDIA Profile Inspector – NV Tools Fork | nvpi-v3.0.2.3 | Befintlig fyrdelad applikationsversion; setup version 2 har sitt eget filnamn |
| NVDriverForge | nvdriverforge-v0.1.3 | Befintligt 0.x-schema; versionsuppdateringar bevarar tidigare paket |
| NVMFG Unlock40 | nvmfg-unlock40-v0.1.1 | UI2-kandidat identifieras med exakta hash-värden utan att ha uppfunnit en ny applikationsversion |
| NVRasterPulse | nvrasterpulse-v0.1 | Befintlig tvådelad version |

Underhållaren kan publicera direkt eller auktorisera en assistent att publicera de granskade tillgångarna. Publiceringen är explicit; inget arbetsflöde skapar en release för varje commit.

1. Granska den aktuella förpubliceringsrapporten, källor till binärfilerna, licenser och SHA-256-värden.
2. Skapa ett utkast för verktygets tagg, inriktat på den granskade hub-commit. Inkludera de förberedda versionsspecifika utgåvorna.
3. Bifoga endast den versionens Setup/portabla tillgångar, `Licenses-and-Credits.zip` och `SHA256SUMS.txt`.
4. Kontrollera kompatibilitet, installation, beroenden, ändringar och kända gränser. Håll RTSS framträdande för NVRasterPulse.
5. Publicera, verifiera de offentliga tillgångarnas webbadresser, storlekar och hash, och registrera det faktiska publiceringsdatumet i `docs/releases.json`.
6. Uppdatera nedladdningssidorna och översättningarna, commit/driv sedan deras ändringar i GitHub Desktop.

Tagglänkarna per projekt undviker att skicka användare till ett annat verktyg via en delad `releases/latest`-länk. GitHub:s automatiska **Source code**-arkiv innehåller denna dokumentationshub. Applikationskällor förblir privata. Ursprungliga komponentmeddelanden förblir intakta, och en utgåva löser inte NVMFG:s dokumenterade NVIDIA SDK-reserv.

<a id="integrity-and-storage"></a>
## Integritet och lagring

Ersätt aldrig publicerade binära bytes i tysthet. Använd en ny explicit version eller installationsversion med nya hash. Lagliga sidvagnar kompletterar inbäddade meddelanden. NVDriverForge 0.1.3 bärbar är 141 760 351 byte, över GitHub:s vanliga Git-filgräns på 100 MiB. Släpp bilagor undvik att sätta binärfiler eller Git LFS i denna hubb. [GitHub vägledning för stora filer](https://docs.github.com/en/repositories/working-with-files/managing-large-files/about-large-files-on-github).

Privat sårbarhetsrapportering bör aktiveras i förvarets säkerhetsinställningar. Verifiera dess tillgänglighet innan du skickar känsliga rapporter dit; [SECURITY.md](../SECURITY.md) ger en reserv som inte avslöjar sårbarhetsdetaljer.

[Ladda ner katalog](downloads.md) · [GitHub versionsdokumentation](https://docs.github.com/en/repositories/releasing-projects-on-github/managing-releases-in-a-repository)
