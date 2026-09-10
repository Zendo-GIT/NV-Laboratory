<!-- nv-language-navigation:start -->
🌐 [English](../../../releasing.md) | [Français](../../../releasing.fr.md) · [NV Laboratory](../README.md)

<details>
<summary>🌐 Language · 34</summary>

[العربية](../../ar/docs/releasing.md) · [বাংলা](../../bn/docs/releasing.md) · [简体中文](../../zh/docs/releasing.md) · **Čeština** · [Dansk](../../da/docs/releasing.md) · [Nederlands](../../nl/docs/releasing.md) · [English](../../../releasing.md) · [Filipino](../../fil/docs/releasing.md) · [Suomi](../../fi/docs/releasing.md) · [Français](../../../releasing.fr.md) · [Deutsch](../../de/docs/releasing.md) · [Ελληνικά](../../el/docs/releasing.md) · [हिन्दी](../../hi/docs/releasing.md) · [Magyar](../../hu/docs/releasing.md) · [Bahasa Indonesia](../../id/docs/releasing.md) · [Italiano](../../it/docs/releasing.md) · [日本語](../../ja/docs/releasing.md) · [한국어](../../ko/docs/releasing.md) · [मराठी](../../mr/docs/releasing.md) · [فارسی](../../fa/docs/releasing.md) · [Polski](../../pl/docs/releasing.md) · [Português](../../pt/docs/releasing.md) · [ਪੰਜਾਬੀ](../../pa/docs/releasing.md) · [Română](../../ro/docs/releasing.md) · [Русский](../../ru/docs/releasing.md) · [Español](../../es/docs/releasing.md) · [Kiswahili](../../sw/docs/releasing.md) · [Svenska](../../sv/docs/releasing.md) · [தமிழ்](../../ta/docs/releasing.md) · [ไทย](../../th/docs/releasing.md) · [Türkçe](../../tr/docs/releasing.md) · [Українська](../../uk/docs/releasing.md) · [اردو](../../ur/docs/releasing.md) · [Tiếng Việt](../../vi/docs/releasing.md)

[Translation policy](../../README.md)

</details>
<!-- nv-language-navigation:end -->

<!-- nv-translation-notice:start -->
> Strojově podporovaný překlad z angličtiny. Technické názvy, příkazy, URL a původní právní texty jsou zachovány. Recenze rodilým mluvčím je vítána; Pokud je znění nejasné, nahlédněte do anglického odkazu.
<!-- nv-translation-notice:end -->

<a id="publishing-and-releases"></a>
# Publikování a vydání

Veřejné úložiště je **Zendo-GIT/NV-Laboratory**. Změny dokumentace jsou kontrolovány, potvrzeny a tlačeny správcem pomocí **GitHub Desktop**. Místní potvrzení nenahrává soubory. Binární balíčky jsou samostatná aktiva GitHub Release; nikdy nepatří do seznamu změn Git.

<a id="documentation-updates"></a>
## Aktualizace dokumentace

1. Otevřete složku **NV-Laboratory** v GitHub Desktop.
2. Prohlédněte si dokumentaci, upozornění, obrázky, metadata JSON a validátor dokumentace.
3. Spusťte `python tools/validate_repository.py` z této složky.
4. Potvrďte zkontrolované změny a poté použijte **Push origin**. Zkontrolujte výsledek Akce.
5. Ponechte si veřejnou identitu autora **禅堂 Zendo (RevoluSound Team)** a adresu účtu GitHub `noreply`.

Nikdy nevybírejte nadřazený vývojový pracovní prostor, soukromý adresář auditu nebo adresář binárních příloh. [Zavázat se k ochraně soukromí e-mailů](https://docs.github.com/en/account-and-profile/how-tos/email-preferences/setting-your-commit-email-address).

<a id="independent-application-releases"></a>
## Nezávislá vydání aplikací

| Nástroj | Tag | Zásady verzí |
| --- | --- | --- |
| NVIDIA Profile Inspector – NV Tools Fork | nvpi-v3.0.2.3 | Stávající čtyřdílná verze aplikace; setup revize 2 má svůj vlastní název souboru |
| NVDriverForge | nvdriverforge-v0.1.3 | Stávající schéma 0.x; verzované aktualizace zachovávají dřívější balíčky |
| NVMFG Unlock40 | nvmfg-unlock40-v0.1.1 | Kandidát UI2 identifikovaný přesnými hashemi bez vymýšlení nové verze aplikace |
| NVRasterPulse | nvrasterpulse-v0.1 | Stávající dvoudílná verze |

Správce může publikovat přímo nebo pověřit asistenta zveřejněním auditovaných aktiv. Publikace je explicitní; žádný pracovní postup nevytváří vydání při každém potvrzení.

1. Prohlédněte si aktuální předpublikační zprávu, zdroje binárních souborů, licence a hodnoty SHA-256.
2. Vytvořte koncept pro značku nástroje se zaměřením na recenzované potvrzení centra. Zahrňte připravené poznámky k verzi specifické pro verzi.
3. Připojte pouze instalační/přenosná aktiva této verze, `Licenses-and-Credits.zip` a `SHA256SUMS.txt`.
4. Zkontrolujte kompatibilitu, instalaci, závislosti, změny a známé limity. Udržujte RTSS prominentní pro NVRasterPulse.
5. Publikovat, ověřovat adresy URL veřejných prostředků, velikosti a hodnoty hash a zaznamenávat skutečné datum zveřejnění v `docs/releases.json`.
6. Aktualizujte stránky ke stažení a překlady a poté potvrďte/pusťte jejich změny v GitHub Desktop.

Odkazy na tagy pro jednotlivé projekty zabraňují odesílání uživatelů na jiný nástroj prostřednictvím sdíleného odkazu `releases/latest`. Tento dokumentační centrum obsahují automatické archivy **Source code** GitHub. Zdroje aplikací zůstávají soukromé. Původní upozornění na součásti zůstávají nedotčeny a vydání neřeší zdokumentovanou rezervu NVIDIA SDK NVMFG.

<a id="integrity-and-storage"></a>
## Integrita a úložiště

Nikdy tiše nenahrazujte publikované binární bajty. Použijte novou explicitní verzi nebo revizi instalačního programu s novými hodnotami hash. Právní postranní vozíky doplňují vložená oznámení. NVDriverForge Přenosný 0.1.3 má 141 760 351 bajtů, nad běžným limitem 100 MiB Git souboru GitHub. Uvolněte přílohy zabraňují vkládání binárních souborů nebo Git LFS do tohoto centra. [GitHub navádění velkých souborů](https://docs.github.com/en/repositories/working-with-files/managing-large-files/about-large-files-on-github).

Soukromé hlášení o chybách zabezpečení by mělo být povoleno v nastavení zabezpečení úložiště. Před přesměrováním citlivých hlášení tam ověřte jeho dostupnost; [SECURITY.md](../SECURITY.md) poskytuje záložní řešení, které neodhaluje podrobnosti o zranitelnosti.

[Stáhněte si katalog](downloads.md) · [Dokumentace k vydání GitHub](https://docs.github.com/en/repositories/releasing-projects-on-github/managing-releases-in-a-repository)
