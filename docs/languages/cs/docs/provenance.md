<!-- nv-language-navigation:start -->
🌐 [English](../../../provenance.md) | [Français](../../../provenance.fr.md) · [NV Laboratory](../README.md)

<details>
<summary>🌐 Language · 34</summary>

[العربية](../../ar/docs/provenance.md) · [বাংলা](../../bn/docs/provenance.md) · [简体中文](../../zh/docs/provenance.md) · **Čeština** · [Dansk](../../da/docs/provenance.md) · [Nederlands](../../nl/docs/provenance.md) · [English](../../../provenance.md) · [Filipino](../../fil/docs/provenance.md) · [Suomi](../../fi/docs/provenance.md) · [Français](../../../provenance.fr.md) · [Deutsch](../../de/docs/provenance.md) · [Ελληνικά](../../el/docs/provenance.md) · [हिन्दी](../../hi/docs/provenance.md) · [Magyar](../../hu/docs/provenance.md) · [Bahasa Indonesia](../../id/docs/provenance.md) · [Italiano](../../it/docs/provenance.md) · [日本語](../../ja/docs/provenance.md) · [한국어](../../ko/docs/provenance.md) · [मराठी](../../mr/docs/provenance.md) · [فارسی](../../fa/docs/provenance.md) · [Polski](../../pl/docs/provenance.md) · [Português](../../pt/docs/provenance.md) · [ਪੰਜਾਬੀ](../../pa/docs/provenance.md) · [Română](../../ro/docs/provenance.md) · [Русский](../../ru/docs/provenance.md) · [Español](../../es/docs/provenance.md) · [Kiswahili](../../sw/docs/provenance.md) · [Svenska](../../sv/docs/provenance.md) · [தமிழ்](../../ta/docs/provenance.md) · [ไทย](../../th/docs/provenance.md) · [Türkçe](../../tr/docs/provenance.md) · [Українська](../../uk/docs/provenance.md) · [اردو](../../ur/docs/provenance.md) · [Tiếng Việt](../../vi/docs/provenance.md)

[Translation policy](../../README.md)

</details>
<!-- nv-language-navigation:end -->

<!-- nv-translation-notice:start -->
> Strojově podporovaný překlad z angličtiny. Technické názvy, příkazy, URL a původní právní texty jsou zachovány. Recenze rodilým mluvčím je vítána; Pokud je znění nejasné, nahlédněte do anglického odkazu.
<!-- nv-translation-notice:end -->

<a id="provenance-changes-and-licensing"></a>
# Provenience, změny a licence

Tento audit popisuje kandidáty připravené dne **2026-09-09**. Zdroje aplikací zůstávají soukromé; veřejné inventáře obsahují názvy souborů a hash, nikoli zdrojový kód. Viz [oznámení o úplných součástech](../THIRD_PARTY_NOTICES.md).

<a id="nvidia-profile-inspector--nv-tools-fork"></a>
## NVIDIA Profile Inspector – NV Tools Fork

Reference: Orbmu2k/nvidiaProfileInspector commit `592d962cca8827efe8859461a84267755595064a`; kandidátská spustitelná verze 3.0.2.3. Referenční potvrzení a verze sestavení fork jsou různé identifikátory; z verze fork není odvozena žádná upstream verze.

157 zdrojových/zdrojových souborů čistého společníka bylo porovnáno s tímto odevzdáním: 2 bajtově shodné, 134 se liší pouze zakončením řádků nebo UTF-8 kusovníkem, 11 upravených, 10 nepřítomných na porovnávané upstreamové cestě. „Přidáno“ se vztahuje k této cestě a samo o sobě není důkazem původního autorství.

[Kompletní porovnání souborů/hash](../../../provenance/nvpi-source-provenance.json).

| Oblast | Zděděná práce | Příspěvek Fork |
| --- | --- | --- |
| Editor profilu | Model profilu, import/export, asociace aplikací a referenční data | Integrace s obrazovkou a externím spouštěčem nástrojů |
| NVAPI | Interop DRS Orbmu2k | Interoperace související s barvami a zobrazením, omezení produkčního nativního načítání a odstranění falešného obsahu |
| Zobrazovací služby | Windows/NVIDIA API jako externí rozhraní | DisplayInfoService, DisplayConfigurationService, DisplaySettingsBackend |
| UI | Upstream zdroje, palety a ikony WPF | Dialogy na obrazovce, 15sekundové potvrzení, stav/zpětné čtení a rozložení panelu nástrojů |
| Spouštěč | Stávající prostředí aplikace | Chráněné samostatně nainstalované vyhledávání a spouštění RasterPulse |
| Balení | MIT proti proudu | Čistý samostatný společník, samostatný instalátor/odinstalátor, uchovaná upozornění |

Mapa veřejného zdroje obsahuje cesty k řešení/zdrojům pro sledovatelnost; tyto soubory nejsou distribuovány jako zdroj. Vývojové testy, falešná rozhraní a stará kombinovaná binární NVPI/RasterPulse jsou vyloučeny.

<a id="nvdriverforge"></a>
## NVDriverForge

Nezávislá aplikace C#/.NET 8/WPF; pracovní postup orientovaný na uživatele je částečně inspirován NVCleanstall. V produkčním užitečném zatížení nebyl identifikován žádný zdroj/binární soubor NVCleanstall. Není reprezentován jako fork této proprietární aplikace.

Původní projektová práce zahrnuje analýzu/výběr komponent, chráněné instalační úlohy, zálohování a obnovu transakcí, stahování katalogu NVIDIA, kontroly aktualizací, lokalizovaná vysvětlení, volitelné pokročilé/NVENC pracovní postupy a zaváděcí pás instalátoru.

Zděděné/přizpůsobené komponenty: čtyři palety motivů NVPI, rozšířená reference rozhraní NVAPI DRS a samostatně volitelný doplněk MIT NVPI. Uživatelské rozhraní výběru předvolby Custom NV a integrace transakcí na seznamu povolených patří k NVDriverForge; předvolba není oficiální doporučení NVIDIA.

7-Zip 26.03, .NET/WPF 8.0.31 a Inno Setup zůstávají nezměněné externí komponenty používané podle vlastních podmínek. keylase Data NVENC nejsou vložena; jedno přesné potvrzení je vybráno a zkontrolováno, když uživatel požaduje kompatibilní stažení. Pro tato upstream data nebyla zřízena žádná redistribuční licence.

<a id="nvmfg-unlock40"></a>
## NVMFG Unlock40

NVMFG Unlock40 byl vyvinut nezávisle 禅堂 Zendo (RevoluSound Team). Správce použil pro srovnání a upřesnění RTX40MFG-Unlock. Aplikace jako celek není prezentována jako její fork. Toto rozlišení neodstraňuje zásluhy za sdílené/přizpůsobené komponenty v aktuální nativní vrstvě.

Srovnávací reference: dashdogy/RTX40MFG-Unlock, Michael Robles, MIT, potvrzení `4e776d068f91b4a665425542bb005dd57cc3d891`. Soukromý strom nativního motoru obsahuje 48 porovnávaných souborů: 35 rozdílů pouze ve formátování, 4 upravené soubory a 9 chybějících v referenční cestě. [Kompletní srovnání](../../../provenance/nvmfg-source-provenance.json).

Upravené zděděné soubory: `entry_detour.h`, `patcher.cpp`, `temporal_interval_trace.cpp`, `temporal_interval_trace.h`. Mezi další cesty patří `game_selection.*`, `ngx_bootstrap.*`, `ngx_capability.h`, `presentation_tracker.h`, `vsync_observer.*` a ponechaná upstream licence.

Produkční jednotky C++: patcher, midpoint_fix, dlssg_provider_policy, entry_detour, nvidia_mfg_policy, temporal_interval_trace, ngx_bootstrap, game_selection a vsync_observer; plus sestava entry_detour a vyrovnávací paměť/háček/trampolína/HDE64 MinHook. Zděděné frontend ReShade, starší zdroje shim a nepoužité cíle CMake nejsou součástí této produkční kompilace.

Odpovídající komponenty pokrývají politiku záplatování/poskytovatele a dočasnou práci; jejich upozornění na autorská práva a povolení zůstávají nedotčena. Centrální koordinace NGX/bootstrap/řadiče, zpracování V-Sync pro jednotlivé hry, diagnostika relace a pracovní postup aplikace/SDK/zálohování Windows jsou projektové práce 禅堂 Zendo (RevoluSound Team). Výše uvedené počty popisují soubory, včetně souborů třetích stran a nepoužitých souborů, nikoli procento autorství nebo chronologii nápadu žádného projektu.

Pomocník přizpůsobí NvapiDrsWrapper a NativeArrayHelper NVPI do samostatné sestavy s logikou profilu vytvořenou v projektu. Stará falešná vývojová cesta je vyloučena. Palety sdílené rodiny pocházejí z NVPI.

MinHook reference: `8fda4f5481fed5797dc2651cd91e238e9b3928c6`; zděděná kompilovaná podmnožina nemá ve srovnání žádné funkční lokální změny. Streamline integrační hlavičky: 2.12; licence otevřené hlavičky ověřená na v2.12.0. Zdroj hlavičky NGX: NVIDIA/DLSS potvrdit `a291cc7d2cc642a51566f3dfd5376f635cd1b284`.

Kandidátský motor SHA-256: `0E7FC0277C88B22095B622F6A3CB292EC0C14F7A0253D392502257B75E548890`.

Požadovaný poskytovatel SHA-256 v engine.json: `C64928FDB7C48A57722EA8EEF2662171EDC323473ADEA66C29A206A23F1A2BED`. Hlášená rodina poskytovatelů 310.9 není zaměnitelná s tímto přesným hashem. Není zahrnuta žádná knihovna DLL ani model poskytovatele.

**Nevyřízený bod licencování:** plná licence NVIDIA RTX SDK, verze 14. března 2024, obsahuje část 4(d) omezení týkající se obcházení technických omezení. Audit nezakládá oprávnění pro toto použití. Ponechání licence motoru MIT, bezplatné používání nebo sledování jiných modů tuto samostatnou podmínku nevyřeší. Příprava kandidáta není právní povolení. Původní krátké záhlaví je doplněno plnou licencí; jeho text Windows-1252 je také poskytován jako čitelný UTF-8 se zachováním původních bajtů.

<a id="nvrasterpulse"></a>
## NVRasterPulse

Nezávislý správce profilů RTSS vyvinutý v úložišti odvozeném od NVPI. Zděděné prostředky/palety uživatelského rozhraní MIT a původ projektu zůstávají připsány. Produkční aplikace výslovně používá poskytnutou licenci MIT.

Práce na projektu: přesná analýza/zápis profilu RTSS a zlomkové kódování, zálohování, odstranění přepsání, přemostění opětovného načtení, detekce předpokladů, kompaktní uživatelské rozhraní, životní cyklus zásobníku, ovládací prvky spouštění a lokalizace. RTSS provádí skutečné omezení.

Není přibalen žádný zdroj RTSS, hook DLL, SDK nebo instalační program. Most zavolá export v existující uživatelem vybrané instalaci RTSS. V tomto balíčku není žádný balíček ovladače NVIDIA, nativní experimentální omezovač, Framepacer, MinHook, ReShade nebo DLSS.

<a id="assets-generated-data-and-tools"></a>
## Aktiva, generovaná data a nástroje

[Aktivní kredity](../assets/README.md) identifikuje existující náhledy rozhraní a volič nastavení NVPI. Fiktivní hodnoty v nich jsou označeny. Není zkopírována žádná hra/Nexus aktivum, osobní profil, soukromé ICC, firemní logo NVIDIA nebo soubor písma.

Vygenerované názvy kompatibility her zděděné v NVMFG jsou pomůckou pro detekci, nikoli důkazem testu. Vygenerované instalační katalogy jsou připsány v [upozornění překladatele](../../../../licenses/INSTALLER-TRANSLATORS.md). Vygenerované záznamy sestavení s absolutními cestami zůstávají soukromé.

Nástroje pro soukromé sestavení zahrnují auditní skripty .NET SDK/MSBuild, Visual Studio C++/MASM, Windows SDK, PowerShell, Inno Setup a Python. Jejich kompilátory, hlavičky, testovací běhy a ladicí prostředky nejsou distribuovány. Statická verze CRT zůstává pod příslušnými podmínkami toolchainu Microsoft.

<a id="scope-of-verification"></a>
## Rozsah ověření

Lokální audit inventarizoval všechny soubory ve třech vývojových kořenech, přičemž vyloučil objektové databáze Git a propojené cíle adresářů. Aktivní zdroj/dokumenty byly zkontrolovány; historické stavby byly inventarizovány a vyloučeny. Vybrané ZIP a aktuální užitečné zatížení byly skenovány a hashovány; svazky .NET byly dekomprimovány pro další kontrolu. Tento počáteční audit nespustil žádný produkt, instalační program, hru, proces RTSS ani ovladač.

Pozdější revize 2 nastavení NVPI opravuje výběr samostatného jazyka pomocí sdílených ovládacích prvků Inno a bootstrapu. Světlá/tmavá soukromá zařízení ověřila navigaci myší a klávesnicí a všech 34 explicitních jazykových kódů. Vlastní selektor nastavení byl otevřen na nikdy nezobrazené soukromé ploše a před instalací byl zrušen. Jeho sedm aplikačních souborů a přenosný ZIP jsou nezměněny. NVDriverForge 0.1.3 obsahuje opraveného společníka a stále předává `/LANG`.

NVDriverForge 0.1.3 byl dokončen dne 2026-09-10. Jeho soukromá ověřovací zpráva zaznamenává 366 testů aplikací, 118 doprovodných kontrol, 32 kontrol nastavení, 156 nativních srovnání a 34 případů přeposílání jazyků. Oprava výběru chráněné komponenty byla přehrána s původním balíčkem ovladače, aniž by se změnila jeho užitečná zátěž nebo instaloval ovladač. Jedná se o datované výsledky produktového týmu, nikoli o testy znovu provedené touto aktualizací dokumentace nebo důkaz o úspěšné skutečné instalaci ovladače.

Tato aktualizace centra nemění žádný funkční kód aplikace. Dřívější testy sestavení/jednotky/UI aplikací zůstávají zastaralými historickými důkazy. Nejedná se o úplné zpětné inženýrství všech binárních souborů třetích stran ani o záruku proti všem možným tajným vzorům.
