<!-- nv-language-navigation:start -->
🌐 [English](../../../installation.md) | [Français](../../../installation.fr.md) · [NV Laboratory](../README.md)

<details>
<summary>🌐 Language · 34</summary>

[العربية](../../ar/docs/installation.md) · [বাংলা](../../bn/docs/installation.md) · [简体中文](../../zh/docs/installation.md) · **Čeština** · [Dansk](../../da/docs/installation.md) · [Nederlands](../../nl/docs/installation.md) · [English](../../../installation.md) · [Filipino](../../fil/docs/installation.md) · [Suomi](../../fi/docs/installation.md) · [Français](../../../installation.fr.md) · [Deutsch](../../de/docs/installation.md) · [Ελληνικά](../../el/docs/installation.md) · [हिन्दी](../../hi/docs/installation.md) · [Magyar](../../hu/docs/installation.md) · [Bahasa Indonesia](../../id/docs/installation.md) · [Italiano](../../it/docs/installation.md) · [日本語](../../ja/docs/installation.md) · [한국어](../../ko/docs/installation.md) · [मराठी](../../mr/docs/installation.md) · [فارسی](../../fa/docs/installation.md) · [Polski](../../pl/docs/installation.md) · [Português](../../pt/docs/installation.md) · [ਪੰਜਾਬੀ](../../pa/docs/installation.md) · [Română](../../ro/docs/installation.md) · [Русский](../../ru/docs/installation.md) · [Español](../../es/docs/installation.md) · [Kiswahili](../../sw/docs/installation.md) · [Svenska](../../sv/docs/installation.md) · [தமிழ்](../../ta/docs/installation.md) · [ไทย](../../th/docs/installation.md) · [Türkçe](../../tr/docs/installation.md) · [Українська](../../uk/docs/installation.md) · [اردو](../../ur/docs/installation.md) · [Tiếng Việt](../../vi/docs/installation.md)

[Translation policy](../../README.md)

</details>
<!-- nv-language-navigation:end -->

<!-- nv-translation-notice:start -->
> Strojově podporovaný překlad z angličtiny. Technické názvy, příkazy, URL a původní právní texty jsou zachovány. Recenze rodilým mluvčím je vítána; Pokud je znění nejasné, nahlédněte do anglického odkazu.
<!-- nv-translation-notice:end -->

<a id="installation-guide"></a>
# Průvodce instalací

Začněte s [Stahování](downloads.md), který zaznamenává stav publikace a přesné názvy aktiv. Jedná se o samostatné nástroje: nainstalujte pouze ty, které potřebujete.

> **Pro NVRasterPulse nainstalujte [RTSS od Guru3D](https://www.guru3d.com/download/rtss-rivatuner-statistics-server-download/) před otevřením správce profilů.**
> Chcete-li použít limity, musí se spustit RTSS; není součástí NV Tools.

| Nástroj | Instalovaná edice | Přenosná edice | Hlavní předpoklad |
| --- | --- | --- | --- |
| NVIDIA Profile Inspector – NV Tools Fork | NVPI-CustomNV-3.0.2.3-Setup-r2.exe | Extrahujte kompletní NVPI ZIP | Ovladač NVIDIA a rozhraní .NET Framework 4.8 |
| NVDriverForge | NVDriverForge-Setup.exe | NVDriverForge.exe, včetně runtime | Kompatibilní originální balíček ovladače NVIDIA pro instalační operace |
| NVMFG Unlock40 | NVMFGUnlock40-0.2.3-Setup-x64.exe | Rozbalte kompletní NVMFG ZIP, ponechte podsložky | RTX 40, stávající DLSS FG, přesný poskytovatel a pomocníci .NET Framework 4.8 |
| NVRasterPulse | NVRasterPulse-0.2-win-x64-Setup.exe | Extrahujte kompletní RP ZIP | RTSS a .NET Framework 4.8 |

<a id="download-verify-install"></a>
## Stáhnout, ověřit, nainstalovat

1. Ve zvolené publikované verzi si stáhněte její pojmenované aplikační aktivum, poznámky ZIP a SHA256SUMS.txt.
2. Použijte [Příklad SHA-256](downloads.md#sha-256) se skutečným staženým názvem souboru.
3. Při instalaci postupujte podle běžného instalačního programu. U přenosného ZIP rozbalte vše do nové místní zapisovatelné složky; nespouštějte zevnitř ZIP.
4. Otevřete vlastní EXE aplikace. Uschovejte si doprovodné licenční/konfigurační/datové soubory.
5. Před povolením nastavení nebo operací systému si přečtěte pokyny k použití tohoto nástroje.

Aktuální binární soubory jsou bez znaménka. Odpovídající hash potvrzuje očekávané bajty; nejedná se o certifikát zabezpečení nebo kompatibility. Nevypínejte bezpečnostní ochranu Windows jen proto, abyste potlačili varování.

Instalace NVDF nebo jeho volitelného doprovodu NVPI je oddělená od instalace ovladače GPU. Společník NVPI si zachovává svůj stávající název interní instalace. Jeho vyvýšené tlačítko RasterPulse vyžaduje chráněnou instalaci v celém systému; další kopie RP lze otevřít pomocí jejich vlastních zkratek.

NVMFG je experimentální a má [zdokumentovaná licenční rezerva NVIDIA SDK](provenance.md). Není zahrnut žádný ovladač NVIDIA, poskytovatel/model NGX nebo běhové prostředí hry Streamline. Vybrané stahování SDK a aktualizace her jsou explicitně oddělené operace.

<a id="language-and-updates"></a>
## Jazyk a aktualizace

Pro dokumentaci použijte 34jazyčný volič README. NVDF, NVMFG a RP mají vlastní 34jazyčné nastavení uživatelského rozhraní; NVPI si zachovává stávající jazykovou podporu. Některé technické řetězce instalačního programu se vrátí do angličtiny.

Při aktualizaci zachovejte identitu instalace nástroje. Nejprve jej zavřete a zachovejte zálohy. U NVMFG zavřete postižené hry a vyřešte čekající obnovu profilu. Pro přenosné aktualizace použijte raději novou složku než kombinování vydání.

<a id="removing-a-tool"></a>
## Odebrání nástroje

Odinstalování aplikace automaticky nezruší její nastavení.

- **NVPI:** v případě potřeby před odstraněním obnovte zamýšlené profily/nastavení zobrazení.
- **NVDF:** Pokud chcete obnovit pokročilé změny/NVENC, použijte nejprve obnovení. Uninstall ponechává grafický ovladač, nastavení a zálohy.
- **NVMFG:** zavřete hry, deaktivujte/ukončete ovladač, vyřešte obnovu NVIDIA a obnovte požadované zálohy hry SDK před odstraněním.
- **RP:** nejprve odstraňte zamýšlené přepisy omezovače. Uninstall nevymaže uložené uzávěry RTSS ani neodstraní RTSS.

Přesná umístění dat a omezení najdete u každého [průvodce projektem](../README.md#projects) nebo v případě, že krok obnovy selže, [podporu](support.md).
