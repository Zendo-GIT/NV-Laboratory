<!-- nv-language-navigation:start -->
🌐 [English](../../../development.md) | [Français](../../../development.fr.md) · [NV Laboratory](../README.md)

<details>
<summary>🌐 Language · 34</summary>

[العربية](../../ar/docs/development.md) · [বাংলা](../../bn/docs/development.md) · [简体中文](../../zh/docs/development.md) · **Čeština** · [Dansk](../../da/docs/development.md) · [Nederlands](../../nl/docs/development.md) · [English](../../../development.md) · [Filipino](../../fil/docs/development.md) · [Suomi](../../fi/docs/development.md) · [Français](../../../development.fr.md) · [Deutsch](../../de/docs/development.md) · [Ελληνικά](../../el/docs/development.md) · [हिन्दी](../../hi/docs/development.md) · [Magyar](../../hu/docs/development.md) · [Bahasa Indonesia](../../id/docs/development.md) · [Italiano](../../it/docs/development.md) · [日本語](../../ja/docs/development.md) · [한국어](../../ko/docs/development.md) · [मराठी](../../mr/docs/development.md) · [فارسی](../../fa/docs/development.md) · [Polski](../../pl/docs/development.md) · [Português](../../pt/docs/development.md) · [ਪੰਜਾਬੀ](../../pa/docs/development.md) · [Română](../../ro/docs/development.md) · [Русский](../../ru/docs/development.md) · [Español](../../es/docs/development.md) · [Kiswahili](../../sw/docs/development.md) · [Svenska](../../sv/docs/development.md) · [தமிழ்](../../ta/docs/development.md) · [ไทย](../../th/docs/development.md) · [Türkçe](../../tr/docs/development.md) · [Українська](../../uk/docs/development.md) · [اردو](../../ur/docs/development.md) · [Tiếng Việt](../../vi/docs/development.md)

[Translation policy](../../README.md)

</details>
<!-- nv-language-navigation:end -->

<!-- nv-translation-notice:start -->
> Strojově podporovaný překlad z angličtiny. Technické názvy, příkazy, URL a původní právní texty jsou zachovány. Recenze rodilým mluvčím je vítána; Pokud je znění nejasné, nahlédněte do anglického odkazu.
<!-- nv-translation-notice:end -->

<a id="repository-architecture-and-maintenance"></a>
# Architektura a údržba úložiště

NV Laboratory je veřejný **dokumentační a binární distribuční centrum**. Neobsahuje zdroj aplikace. Tyto čtyři projekty si uchovávají samostatné stromy sestavení, verze, identity a aktiva vydání. Jejich soukromá historie vývoje se do tohoto úložiště Git neimportuje.

<a id="layout"></a>
## Rozložení

| Umístění | Účel |
| --- | --- |
| README.md / README.fr.md | Vstupní body v angličtině/francouzštině |
| Čtyři složky projektu | Kompletní příručky a příslušné originální upozornění |
| dokumenty | Stahování, kompatibilita, původ, vývoj a postup vydání |
| docs/releases.json | Auditovaná metadata, velikosti a hash kandidáta/vydání |
| dokumenty/provenience | Porovnání souborů/hash; žádný aplikační kód |
| licencí | Sdílené plné texty třetích stran a kredity instalačního překladatele |
| aktiva | Stávající recenzované náhledy uživatelského rozhraní a jejich původ |
| .github | Vystavujte formuláře a ověřování dokumentace pouze pro čtení |
| nářadí/validate_repository.py | Standardní-knihovní publikace-hranice a kontroly odkazů |

Angličtina zůstává výchozí GitHub README. Stávající sousední odkazy `.fr.md` zůstávají v platnosti. Další překlady zrcadlí dokumentaci pod `docs/languages/<code>`; volič jazyka zachovává stejnou stránku při přepínání jazyků. Katalog `docs/languages/catalog.json` zaznamenává všech 34 jazyků a zdrojové otisky prstů. GitHub automaticky nevybere soubor README podle jazyka prohlížeče. Viz [jazykový index a zásady překladu](../../README.md).

<a id="application-technologies"></a>
## Aplikační technologie

| Program | Soukromá technologie | Distribuce |
| --- | --- | --- |
| NVPI fork | C#, WPF, .NET Framework 4.8, interoperace NVAPI/Windows | Kompletní přenosná složka a samostatný Inno Setup |
| NVDriverForge | C#, WPF, .NET 8; nativní bootstrap C++; Proces 7-Zip | Samostatný přenosný EXE a nastavení |
| NVMFG Unlock40 | C#/WPF .NET 8, pomocníci Framework 4.8, engine C++20/MASM/MinHook | Přenosný strom a nastavení |
| NVRasterPulse | C#/WPF Framework 4.8; integrace profilu/reload RTSS; nativní bootstrap | Přenosný strom a nastavení |

Tato veřejná pokladna nemůže znovu sestavit aplikace. Automatické archivy „Source code“ jsou snímky rozbočovače. Upstream zdrojové odkazy nepředstavují přesný soukromý upravený zdroj. Veřejná CI ověřuje pouze toto úložiště.

<a id="local-checks"></a>
## Místní kontroly

Z kořenového adresáře úložiště:

```text
python tools/validate_repository.py
```

Python 3.10 nebo novější je dostačující. Kontrola čte soubory, místní odkazy Markdown, požadovaná upozornění/odkazy RTSS, metadata vydání a hranice publikace. Nespouští software, neinstaluje závislosti ani nekontaktuje síť.

Pracovní postup GitHub spouští stejnou kontrolu s povolením obsahu pouze pro čtení při požadavku push, pull nebo ručního odeslání. Checkout je připojen k auditovanému potvrzení a neuchovává přihlašovací údaje. Není nakonfigurována žádná úloha vydání nebo nasazení.

<a id="maintain-the-boundary"></a>
## Udržujte hranici

Aktualizujte společně anglickou referenci, francouzské průvodce a dotčené překlady. Podstatné změny uchovávejte odděleně od porovnávání pouze pro formátování. Zaznamenávejte skutečné hash kandidátů, upstreamové reference a licence; nikdy neodvozujte licenci z popularity projektu.

Používejte nové verze položek Release a znovu auditujte změněné binární soubory, archivy a vložená upozornění. Zachovejte soukromé zálohy mimo toto úložiště. Nepoužívejte veřejný pracovní postup k importu soukromých zdrojů aplikace nebo místních složek sestavení.

V soukromém projektu běží testy vhodné pro změnu funkční aplikace. Nespouštějte znovu instalační programy ovladačů ani nezapisujte skutečné profily pro aktualizaci dokumentace. [Postup ručního uvolnění](releasing.md).
