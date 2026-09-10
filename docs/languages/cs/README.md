<!-- nv-language-navigation:start -->
🌐 [English](../../../README.md) | [Français](../../../README.fr.md) · [NV Laboratory](README.md)

<details>
<summary>🌐 Language · 34</summary>

[العربية](../ar/README.md) · [বাংলা](../bn/README.md) · [简体中文](../zh/README.md) · **Čeština** · [Dansk](../da/README.md) · [Nederlands](../nl/README.md) · [English](../../../README.md) · [Filipino](../fil/README.md) · [Suomi](../fi/README.md) · [Français](../../../README.fr.md) · [Deutsch](../de/README.md) · [Ελληνικά](../el/README.md) · [हिन्दी](../hi/README.md) · [Magyar](../hu/README.md) · [Bahasa Indonesia](../id/README.md) · [Italiano](../it/README.md) · [日本語](../ja/README.md) · [한국어](../ko/README.md) · [मराठी](../mr/README.md) · [فارسی](../fa/README.md) · [Polski](../pl/README.md) · [Português](../pt/README.md) · [ਪੰਜਾਬੀ](../pa/README.md) · [Română](../ro/README.md) · [Русский](../ru/README.md) · [Español](../es/README.md) · [Kiswahili](../sw/README.md) · [Svenska](../sv/README.md) · [தமிழ்](../ta/README.md) · [ไทย](../th/README.md) · [Türkçe](../tr/README.md) · [Українська](../uk/README.md) · [اردو](../ur/README.md) · [Tiếng Việt](../vi/README.md)

[Translation policy](../README.md)

</details>
<!-- nv-language-navigation:end -->

<!-- nv-translation-notice:start -->
> Strojově podporovaný překlad z angličtiny. Technické názvy, příkazy, URL a původní právní texty jsou zachovány. Recenze rodilým mluvčím je vítána; Pokud je znění nejasné, nahlédněte do anglického odkazu.
<!-- nv-translation-notice:end -->

<a id="nv-laboratory"></a>
# NV Laboratory

**NV Tools od 禅堂 Zendo (RevoluSound Team).** Čtyři nezávislé nástroje Windows pro profily ovladačů NVIDIA, instalace ovladače, experimentální limity rámců Multi Frame Generation a RTSS.

[Získejte nástroje](docs/downloads.md) · [Instalace](docs/installation.md) · [Kompatibilita a nápověda](docs/support.md) · [Kredity a licence](THIRD_PARTY_NOTICES.md)

> **NVRasterPulse vyžaduje RTSS.** Nejprve nainstalujte [RivaTuner Statistics Server od Guru3D](https://www.guru3d.com/download/rtss-rivatuner-statistics-server-download/). Aby limity FPS fungovaly, musí být spuštěn RTSS. Stahuje se samostatně.

<a id="projects"></a>
## Projekty

| Projekt | Účel | Verze | Dokumentace | Stáhnout |
| --- | --- | --- | --- | --- |
| **NVIDIA Profile Inspector – NV Tools Fork** | Editor profilu ovladače NVIDIA s přidaným zobrazením, barvami, ovládacími prvky HDR a ICC/WCS. Dříve NVPI Custom. | 3.0.2.3 | [Průvodce](NVIDIA-Profile-Inspector/README.md) | [Balíčky](docs/downloads.md#nvidia-profile-inspector) |
| **NVDriverForge** | Vyberte součásti ovladače, prohlédněte si volitelná vylepšení a nainstalujte originální balíček ovladače NVIDIA. | 0.1.3 | [Průvodce](NVDriverForge/README.md) | [Balíčky](docs/downloads.md#nvdriverforge) |
| **NVMFG Unlock40** | Experimentální nástroj RTX 40 MFG s možnostmi pro jednotlivé hry a údržbou Streamline SDK. | 0.1.1 | [Průvodce](NVMFG-Unlock40/README.md) | [Balíčky a stav](docs/downloads.md#nvmfg-unlock40) |
| **NVRasterPulse** | Spravujte limity RTSS FPS na spustitelný soubor s dílčími hodnotami, zálohami a přístupem k zásobníku. | 0.1 | [Průvodce](NVRasterPulse/README.md) | [Balíčky](docs/downloads.md#nvrasterpulse) |

**Stahování:** [stránka ke stažení](docs/downloads.md) uvádí stav jednotlivých verzí, soubory a hodnoty SHA-256. Experimentální funkce a limity kompatibility jsou popsány v průvodcích projektem.

<a id="start-here"></a>
## Začněte zde

1. Vyberte jeden nástroj výše. Každý pracuje samostatně; instalace celé sady je zbytečná.
2. Přečtěte si její požadavky a vyberte **Nastavení** pro nainstalovanou aplikaci nebo **přenosné** pro samostatnou složku.
3. Až bude zveřejněna její verze, stáhněte si pojmenovanou aplikaci, přečtěte si doprovodná upozornění a porovnejte její SHA-256.
4. Před změnou ovladače, nastavení displeje, profilu NVIDIA nebo běhu hry si uchovávejte zálohy.

Dokumentace je k dispozici ve stejných 34 jazycích jako aplikace NV prostřednictvím voliče v horní části každého průvodce. GitHub automaticky nevybere soubor README podle jazyka prohlížeče. Jazyk dokumentace a vlastní jazykové nastavení aplikace jsou samostatné.

<a id="provenance-and-ownership"></a>
## Provenience a vlastnictví

Toto centrum distribuuje dokumentaci a kompilované aplikace. Zdrojový kód aplikace je udržován soukromě. Upstream projekty si ponechávají své autorství a licence; distribuce soukromých zdrojů tyto podmínky nenahrazuje.

- Profile Inspector fork si zachovává licenci Orbmu2k MIT a je výslovně označena jako fork.
- NVDriverForge má své vlastní binární distribuční podmínky a zahrnuje samostatně licencované komponenty runtime/nástroje.
- NVMFG Unlock40 je nezávisle vyvinutá aplikace. Pro srovnání a upřesnění byl konzultován RTX40MFG-Unlock; sdílené nativní komponenty si zachovávají své kredity MIT. Podmínky MinHook a NVIDIA SDK zůstávají samostatné.
- NVRasterPulse si ponechává dodanou licenci MIT a připisuje uživatelské rozhraní odvozené od Profile Inspector. RTSS je požadovaný externí program.

Viz [kompletní tabulka součástí](THIRD_PARTY_NOTICES.md), [provenience souboru a změny](docs/provenance.md) a [rozsah licence](../../../LICENSE).

<a id="other-projects--revolusound-team"></a>
## Další projekty – RevoluSound Team

Jedná se o samostatné projekty audio modů, které jsou zde propojeny, aby vám pomohly objevit práci týmu.

| Hra | Projekt | O |
| --- | --- | --- |
| Forza Horizon 6 | [Forza Horizon 6 Revolusound Team Pack](https://www.nexusmods.com/forzahorizon6/mods/56) | Změny zvuku vozidla zahrnující motory, výfuky, sání a turbo efekty. |
| Forza Horizon 5 | [Forza Horizon 5 Revolusound Team Pack 1.4.4 FINAL](https://www.nexusmods.com/forzahorizon5/mods/86) | Pozdější týmový audio balíček pro vozidlo FH5. |
| Forza Horizon 5 | [Forza Horizon 5.5 Zendo Revolusound Pack](https://www.nexusmods.com/forzahorizon5/mods/20) | Dřívější balení FH5; jeho stránka Nexus nasměruje návštěvníky na novější týmový balíček výše. |

Názvy následují propojené stránky Nexus Mods. Jejich stahování, požadavky, kredity a oprávnění zůstávají na Nexus Mods.

<a id="help-and-participation"></a>
## Pomoc a účast

[Nahlaste chybu nebo navrhněte funkci](https://github.com/Zendo-GIT/NV-Laboratory/issues) · [Přispívání](CONTRIBUTING.md) · [Bezpečnostní zprávy](SECURITY.md) · [Seznam změn](CHANGELOG.md)

V případě problému se zabezpečením si před odesláním protokolů nebo technických podrobností přečtěte SECURITY.md. Po zveřejnění úložiště musí správce povolit soukromé hlášení.

> **Nezávislé komunitní projekty.** NV Laboratory, NV Tools a tyto nástroje nejsou spojeny s NVIDIA Corporation, nejsou jím sponzorovány ani oficiálně podporovány. NVIDIA, GeForce, RTX, DLSS a další názvy produktů jsou ochranné známky příslušných vlastníků. Názvy popisují kompatibilitu a původ, nikoli oficiální potvrzení.
