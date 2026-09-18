<!-- nv-language-navigation:start -->
🌐 [English](../../../support.md) | [Français](../../../support.fr.md) · [NV Laboratory](../README.md)

<details>
<summary>🌐 Language · 34</summary>

[العربية](../../ar/docs/support.md) · [বাংলা](../../bn/docs/support.md) · [简体中文](../../zh/docs/support.md) · **Čeština** · [Dansk](../../da/docs/support.md) · [Nederlands](../../nl/docs/support.md) · [English](../../../support.md) · [Filipino](../../fil/docs/support.md) · [Suomi](../../fi/docs/support.md) · [Français](../../../support.fr.md) · [Deutsch](../../de/docs/support.md) · [Ελληνικά](../../el/docs/support.md) · [हिन्दी](../../hi/docs/support.md) · [Magyar](../../hu/docs/support.md) · [Bahasa Indonesia](../../id/docs/support.md) · [Italiano](../../it/docs/support.md) · [日本語](../../ja/docs/support.md) · [한국어](../../ko/docs/support.md) · [मराठी](../../mr/docs/support.md) · [فارسی](../../fa/docs/support.md) · [Polski](../../pl/docs/support.md) · [Português](../../pt/docs/support.md) · [ਪੰਜਾਬੀ](../../pa/docs/support.md) · [Română](../../ro/docs/support.md) · [Русский](../../ru/docs/support.md) · [Español](../../es/docs/support.md) · [Kiswahili](../../sw/docs/support.md) · [Svenska](../../sv/docs/support.md) · [தமிழ்](../../ta/docs/support.md) · [ไทย](../../th/docs/support.md) · [Türkçe](../../tr/docs/support.md) · [Українська](../../uk/docs/support.md) · [اردو](../../ur/docs/support.md) · [Tiếng Việt](../../vi/docs/support.md)

[Translation policy](../../README.md)

</details>
<!-- nv-language-navigation:end -->

<!-- nv-translation-notice:start -->
> Strojově podporovaný překlad z angličtiny. Technické názvy, příkazy, URL a původní právní texty jsou zachovány. Recenze rodilým mluvčím je vítána; Pokud je znění nejasné, nahlédněte do anglického odkazu.
<!-- nv-translation-notice:end -->

<a id="compatibility-and-troubleshooting"></a>
# Kompatibilita a odstraňování problémů

Toto jsou připravení kandidáti, nikoli certifikační matice pro všechny kombinace Windows, GPU, ovladače a hry.

| Nástroj | Windows / runtime | Hardware / externí závislost | Operace vyžadující péči |
| --- | --- | --- | --- |
| NVPI fork 3.0.2.3 | Windows 10/11 x64, .NET Framework 4.8 | Kompatibilní ovladač/displej NVIDIA | Profil zapisuje a zobrazuje náhledy |
| NVDriverForge 0.1.4 | Windows 10 sestavení 19041+ / 11 x64; .NET/WPF součástí dodávky | Kompatibilní balíček ovladače NVIDIA | Zvýšená instalace, pokročilá nastavení, volitelný NVENC |
| NVMFG Unlock40 0.2.3 | Windows 10/11 x64; Včetně .NET/WPF, pomocníci Framework 4.8 | RTX 40, způsobilá hra DLSS FG a připnutý poskytovatel | Nativní opravy ve hře, deník globálního profilu, aktualizace hry SDK |
| NVRasterPulse 0.2 | Windows 10/11 x64, .NET Framework 4.8 | nainstalováno RTSS; běží pro čepice | Změny profilu RTSS pro každý spustitelný soubor |

Není připraven žádný balíček ARM64. Dostupnost displeje/API a staré verze Windows mohou omezit jednotlivé funkce. Žádná univerzální minimální verze NVIDIA nebo RTSS není vynalezena. Přesný hash poskytovatele NVMFG je v [provenience](provenance.md).

<a id="before-reporting-a-bug"></a>
## Před nahlášením chyby

Identifikujte přesný spustitelný soubor/verzi, kterou jste otevřeli. Předchozí nainstalovaná kopie nemusí být nutně verzí nově staženého ZIP. Zaznamenejte kroky reprodukce, očekávaný výsledek a skutečný výsledek. V případě problémů s vykreslováním/omezením zahrňte verzi hry, obnovení zobrazení, stav FG/V-Sync/VRR a jakýkoli jiný omezovač nebo překryv.

Použijte [bug formulář](https://github.com/Zendo-GIT/NV-Laboratory/issues/new?template=bug-report.yml). Nikdy nepřipojujte celou soukromou vývojovou složku, archiv ovladačů, model, DLL hry, výpis registru nebo nezkontrolovanou sbírku protokolů.

| Problém | První kontroly |
| --- | --- |
| Špatná verze aplikace | Potvrďte identitu EXE a hodnotu hash Release; zavřete starší kopii před výměnou. |
| Chyba běhu/spouštění | Nainstalujte požadovaný Framework 4.8 nebo si ponechte všechny dodané přenosné podsložky. |
| UAC zrušeno | Opakujte pouze zamýšlenou operaci; zrušení není úspěšná instalace. |
| Neshoda hash/podpis | Přestaňte tohoto kandidáta používat a získejte očekávané oficiální bajty. |
| Barva/režim NVPI odmítnut | Vraťte se a použijte kombinaci podporovanou aktuálním displejem/ovladačem. |
| Selhání zálohování nebo obnovy NVDF | Zachovat chráněnou úlohu a RECOVERY.txt; nemažte deník ani nevynucujte konfliktní zápisy. |
| NVMFG čekající na nastavení | Vyřešte obnovu se zavřenými hrami a zachovejte změny z jiných nástrojů. |
| Čepice RP nemá žádný vliv | Spusťte RTSS, identifikujte skutečný EXE hry, zkontrolujte stav zavěšení a konkurenční limity. |
| Víčko RP přetrvává i po odstranění | Zkontrolujte RTSS Global; odstranění změn pouze přepíše lokální omezovač. |

NVDriverForge nabízí náhledovou místní zprávu JSON; NVMFG nabízí diagnostiku v aplikaci About. Upřednostněte tyto filtrované zprávy před úplným archivem protokolů a před sdílením je zkontrolujte. Zablokování obnovy hlášené na NVMFG 0.1.1 stále nemá žádnou stanovenou příčinu; uchovejte jeho deník a zaznamenejte všechny dostupné chybové kódy. NVRasterPulse 0.2 nabízí diagnostiku konfigurace v nabídce akcí bez měření FPS.

<a id="logs-and-privacy"></a>
## Protokoly a soukromí

| Nástroj | Místní data ke kontrole, nikoli k nahrání velkoobchodně |
| --- | --- |
| NVDF | `%LOCALAPPDATA%\NVDriverForge`; chráněné úlohy `%PROGRAMDATA%\NVDriverForge\Jobs` |
| NVMFG | `%LOCALAPPDATA%\RtxMfg`; zálohy `%LOCALAPPDATA%\NvidiaStreamlineMaintenance\Backups`; `Sessions` vedle EXE |
| RP | `%LOCALAPPDATA%\NVRasterPulse`; `Backups\RTSS` pod ním |
| NVPI | Vámi zvolené exporty a zobrazená chyba; žádná vynalezená univerzální cesta protokolu |

Odstraňte názvy účtů, domovské adresáře, cesty ke knihovně her, identifikátory zařízení, tokeny a nesouvisející okna z textu/obrázků, které sdílíte. Originály si uschovejte pro účely obnovení. Veřejná témata jsou viditelná pro všechny.

V případě chyby zabezpečení, nebezpečného privilegovaného chování nebo nezamýšlené destruktivní operace sledujte [SECURITY.md](../SECURITY.md) namísto zveřejňování podrobností.

<a id="what-has-been-verified"></a>
## Co bylo ověřeno

Pro přípravu hubu byly provedeny statické skeny užitečné zátěže/ZIP/hash/metadata a kontroly dokumentace. Existující testy sestavení/jednotky/uživatelského rozhraní soukromých aplikací jsou historické, datované důkazy. V rámci této přípravy nebyla provedena žádná instalace ovladače, změna zobrazení, živá operace RTSS nebo benchmark hry.

„Zjištěno“, „zapsáno“, „znovu načteno“, „dostupná schopnost“ a „měřeno ve hře“ jsou různé výsledky. Nahlaste, kterou jste pozorovali.
