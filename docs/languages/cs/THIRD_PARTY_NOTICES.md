<!-- nv-language-navigation:start -->
🌐 [English](../../../THIRD_PARTY_NOTICES.md) | [Français](../fr/THIRD_PARTY_NOTICES.md) · [NV Laboratory](README.md)

<details>
<summary>🌐 Language · 34</summary>

[العربية](../ar/THIRD_PARTY_NOTICES.md) · [বাংলা](../bn/THIRD_PARTY_NOTICES.md) · [简体中文](../zh/THIRD_PARTY_NOTICES.md) · **Čeština** · [Dansk](../da/THIRD_PARTY_NOTICES.md) · [Nederlands](../nl/THIRD_PARTY_NOTICES.md) · [English](../../../THIRD_PARTY_NOTICES.md) · [Filipino](../fil/THIRD_PARTY_NOTICES.md) · [Suomi](../fi/THIRD_PARTY_NOTICES.md) · [Français](../fr/THIRD_PARTY_NOTICES.md) · [Deutsch](../de/THIRD_PARTY_NOTICES.md) · [Ελληνικά](../el/THIRD_PARTY_NOTICES.md) · [हिन्दी](../hi/THIRD_PARTY_NOTICES.md) · [Magyar](../hu/THIRD_PARTY_NOTICES.md) · [Bahasa Indonesia](../id/THIRD_PARTY_NOTICES.md) · [Italiano](../it/THIRD_PARTY_NOTICES.md) · [日本語](../ja/THIRD_PARTY_NOTICES.md) · [한국어](../ko/THIRD_PARTY_NOTICES.md) · [मराठी](../mr/THIRD_PARTY_NOTICES.md) · [فارسی](../fa/THIRD_PARTY_NOTICES.md) · [Polski](../pl/THIRD_PARTY_NOTICES.md) · [Português](../pt/THIRD_PARTY_NOTICES.md) · [ਪੰਜਾਬੀ](../pa/THIRD_PARTY_NOTICES.md) · [Română](../ro/THIRD_PARTY_NOTICES.md) · [Русский](../ru/THIRD_PARTY_NOTICES.md) · [Español](../es/THIRD_PARTY_NOTICES.md) · [Kiswahili](../sw/THIRD_PARTY_NOTICES.md) · [Svenska](../sv/THIRD_PARTY_NOTICES.md) · [தமிழ்](../ta/THIRD_PARTY_NOTICES.md) · [ไทย](../th/THIRD_PARTY_NOTICES.md) · [Türkçe](../tr/THIRD_PARTY_NOTICES.md) · [Українська](../uk/THIRD_PARTY_NOTICES.md) · [اردو](../ur/THIRD_PARTY_NOTICES.md) · [Tiếng Việt](../vi/THIRD_PARTY_NOTICES.md)

[Translation policy](../README.md)

</details>
<!-- nv-language-navigation:end -->

<!-- nv-translation-notice:start -->
> Strojově podporovaný překlad z angličtiny. Technické názvy, příkazy, URL a původní právní texty jsou zachovány. Recenze rodilým mluvčím je vítána; Pokud je znění nejasné, nahlédněte do anglického odkazu.
<!-- nv-translation-notice:end -->

<a id="third-party-notices-and-credits"></a>
# Oznámení a kredity třetích stran

Prvotní audit: 2026-09-09; NVDriverForge 0.1.3 a aktualizace provenience: 2026-09-10. **Licence komponenty se vztahuje na tuto komponentu, nikoli na celou sadu.** Zdroj aplikace zůstává soukromý. Upozornění na autorská práva a povolení jsou uchovávána doslovně; tato tabulka je index, nikoli jejich náhrada. „Externí“ znamená, že není distribuován v aktivech aplikace.

| Součást / původní projekt | Autor | Oficiální stránky, úložiště nebo stahování | Licence / upozornění | Použijte v NV Tools | Úpravy |
| --- | --- | --- | --- | --- | --- |
| NVIDIA Profile Inspector | Orbmu2k; Copyright 2016 | [Úložiště](https://github.com/Orbmu2k/nvidiaProfileInspector), [stahování](https://github.com/Orbmu2k/nvidiaProfileInspector/releases) | [MIT](../../../NVIDIA-Profile-Inspector/LICENSE) | Celý NVPI fork; NVDF témata/rozšířená reference rozhraní; obal/styly NVMFG; Zdroje uživatelského rozhraní RP | Fork zobrazovací služby, transakce a spouštěč; integrace tématu/ovládání a přizpůsobení obalu |
| RTX40MFG-Unlock | Michael Robles / dashdogy; Copyright 2026 | [Úložiště](https://github.com/dashdogy/RTX40MFG-Unlock), [stahování](https://github.com/dashdogy/RTX40MFG-Unlock/releases) | [MIT](../../../NVMFG-Unlock40/LICENSES/RTX40MFG-Unlock-MIT.txt) | Referenční porovnání/upřesnění a sdílené/přizpůsobené nativní komponenty NVMFG; nezávisle vyvinutá aplikace | Centrální načítání, koordinace NGX/řadiče, integrace a diagnostika pro jednotlivé hry/V-Sync |
| MinHook, připnutý 8fda4f5 | Tsuda Kageyu; Copyright 2009–2017 | [Úložiště](https://github.com/TsudaKageyu/minhook), [připnutý zdroj](https://github.com/TsudaKageyu/minhook/tree/8fda4f5481fed5797dc2651cd91e238e9b3928c6) | [BSD 2-klauzule](../../../NVMFG-Unlock40/LICENSES/MinHook.txt) | Staticky zkompilovaný do NVMFG motoru | Zahrnutá podmnožina nezměněná kromě formátování textu proti zděděné kopii |
| Hacker Disassembler Engine (HDE64) | Vyacheslav Patkov; Copyright 2008–2009 | [Zdrojová kolekce MinHook](https://github.com/TsudaKageyu/minhook/tree/8fda4f5481fed5797dc2651cd91e238e9b3928c6/src/hde) | [Úplná upozornění MinHook/HDE](../../../NVMFG-Unlock40/LICENSES/MinHook.txt) | Dekodér MinHook v NVMFG | Nebyly zjištěny žádné funkční změny; Upozornění HDE32 zachováno, ačkoli produkce používá HDE64 |
| Streamline Integrační hlavičky 2.12 | NVIDIA Corporation; Copyright 2023 | [Úložiště](https://github.com/NVIDIA-RTX/Streamline), [stahování](https://github.com/NVIDIA-RTX/Streamline/releases) | [MIT pro vhodná záhlaví](../../../NVMFG-Unlock40/LICENSES/Streamline-MIT.txt) | Kompiluje integraci NVMFG Streamline | Záhlaví neupravená; žádná runtime DLL v balíčku aplikace |
| Záhlaví NVIDIA NGX / DLSS SDK | NVIDIA Corporation | [Připnuté úložiště](https://github.com/NVIDIA/DLSS/tree/a291cc7d2cc642a51566f3dfd5376f635cd1b284), [SDK](https://developer.nvidia.com/rtx/dlss) | [Podmínky NVIDIA RTX SDK](../../../NVMFG-Unlock40/LICENSES/NVIDIA-RTX-SDK.txt), [upozornění v záhlaví](../../../NVMFG-Unlock40/LICENSES/NGX-Header-Notice.txt) | Kompiluje integraci NVMFG NGX | Záhlaví neupravená; není přibalen žádný model/poskytovatel NGX; nevyřešené omezení popsané níže |
| Runtime .NET 8.0.31 (NVDF) / 8.0.30 (NVMFG) | .NET Foundation, Microsoft a přispěvatelé | [Zdroj](https://github.com/dotnet/runtime), [stahování](https://dotnet.microsoft.com/en-us/download/dotnet/8.0) | [MIT](../../../licenses/third-party/Microsoft-NET-LICENSE.txt) a [vyplňte oznámení třetích stran](../../../licenses/third-party/Microsoft-NET-THIRD-PARTY-NOTICES.txt) | Samostatná aplikace/agent NVDF a NVMFG | Runtime beze změn |
| WPF / Windows Desktop Runtime 8.0.31 (NVDF) / 8.0.30 (NVMFG) | .NET Foundation, Microsoft a přispěvatelé | [Zdroj](https://github.com/dotnet/wpf), [stahování](https://dotnet.microsoft.com/en-us/download/dotnet/8.0) | [MIT](../../../licenses/third-party/Microsoft-WPF-LICENSE.txt), runtime upozornění výše | Uživatelská rozhraní NVDF a NVMFG | Rámec neupravený; uživatelské rozhraní aplikace vytvořené/přizpůsobené samostatně |
| .NET Framework 4.8 | Microsoft | [Oficiální runtime ke stažení](https://dotnet.microsoft.com/en-us/download/dotnet-framework/net48) | podmínky platformy/runtime Microsoft; externí | Pomocníci profilu NVPI, RP a NVMFG | Žádný; tímto centrem není distribuován žádný instalační program ani knihovna DLL |
| 7-Zip 26.03 x64 | Igor Pavlov; Copyright 1999–2026 | [Stránky/stahování](https://www.7-zip.org/download.html), [přesný zdrojový archiv](https://github.com/ip7z/7zip/releases/download/26.03/7z2603-src.tar.xz) | Části [Úplné upozornění](../../../licenses/third-party/7-Zip.txt), [LGPL 2.1-or-later](../../../licenses/third-party/LGPL-2.1.txt), BSD a omezení unRAR | NVDF vkládá neupravené 7z.exe/7z.dll a spouští CLI jako samostatný proces | Žádné úpravy |
| Inno Setup 7.1.0 | Jordan Russell, Martijn Laan a přispěvatelé | [Stránky/stahování](https://jrsoftware.org/isinfo.php), [zdroj](https://github.com/jrsoftware/issrc) | [Původní licence Inno Setup](../../../licenses/third-party/Inno-Setup.txt) | Instalační motory a generované odinstalační programy | Engine/kompilátor bez úprav; přizpůsobeny projektové skripty, branding a nativní fokus |
| Překladové katalogy Inno Setup | Jmenovaní původní překladatelé | [Oficiální kolekce](https://jrsoftware.org/files/istrans/) | Inno/katalogové poznámky a [kompletní hlavičky kreditů](../../../licenses/INSTALLER-TRANSLATORS.md) | Sdílené 34jazyčné katalogy pro všechny čtyři instalační programy, včetně revize 2 nastavení NVPI | Klíče, ID, fonty, záložní technická angličtina; v případě potřeby katalogy náhledů vytvořené podle projektu |
| Runtime Microsoft Visual C++ / podpora Windows SDK | Microsoft | [Nástroje Visual Studio](https://visualstudio.microsoft.com/downloads/), [redistribuční podmínky index](https://learn.microsoft.com/en-us/visualstudio/releases/2022/redistribution) | Microsoft toolchain/runtime podmínky; není MIT podle této tabulky | Statické vydání CRT v nativních binárních souborech motoru/bootstrapu; nainstalovaná rozhraní API Windows | Žádné změny zdroje runtime; není distribuován žádný kompilátor, SDK nebo ladění runtime |
| RivaTuner Statistics Server (RTSS) | Unwinder | [Oficiální guru3D ke stažení](https://www.guru3d.com/download/rtss-rivatuner-statistics-server-download/) | Podmínky dodavatele; žádné oprávnění k redistribuci není odvozeno z „freewaru“ | Požadovaný externí omezovač pro RP; nainstalovaný export UpdateProfiles | Žádný kód RTSS/binární modifikovaný nebo spojený; RP zapíše vybrané klíče profilu |
| Ovladač NVIDIA / NVAPI / NVML | NVIDIA Corporation | [Stahování ovladačů](https://www.nvidia.com/en-us/drivers/), [NVAPI](https://developer.nvidia.com/nvapi), [NVML](https://developer.nvidia.com/management-library-nvml) | NVIDIA ovladač/SDK podmínky; externí | Nainstalovaná nativní rozhraní a explicitní stažení původního ovladače | Žádná NVIDIA DLL v aktivech hubu; Volitelná operace NVDF NVENC upravuje uživatelem vybrané nainstalované knihovny DLL |
| NVIDIA Poskytovatel/modely NGX a runtime Streamline | NVIDIA Corporation | [DLSS SDK](https://developer.nvidia.com/rtx/dlss), [Vychází Streamline](https://github.com/NVIDIA-RTX/Streamline/releases) | Termíny NVIDIA specifické pro součást, odlišné od záhlaví MIT | Externí komponenty hry/ovladače používané NVMFG; SDK lze získat pouze na vyžádání | NVMFG aplikuje experimentální změny chování v paměti; Kopie hry SDK lze aktualizovat pomocí zálohy |
| keylase/nvidia-patch | keylase a přispěvatelé | [Úložiště](https://github.com/keylase/nvidia-patch), [Data Windows](https://github.com/keylase/nvidia-patch/tree/master/win) | Redistribuční licence nebyla tímto auditem stanovena | Externí volitelná data katalogu/oprav NVDF NVENC, načtená z jednoho připnutého potvrzení na výběr | Do aktiva hub/aplikace nejsou zkopírovány žádné upstream zdrojové, opravné nebo opravné údaje |
| NVCleanstall | TechPowerUp | [Oficiální stránka/ke stažení](https://www.techpowerup.com/download/techpowerup-nvcleanstall/) | Vlastní distribuce; nebylo vyvozeno žádné oprávnění k redistribuci zdroje/binární | Pracovní postup a inspirace možností pro NVDF | Žádný importovaný zdroj nebo binární soubor; není fork nebo běhová závislost |

<a id="obligations-and-boundaries"></a>
## Povinnosti a hranice

**Součásti MIT:** si u kopií uchovávají autorská práva, text povolení a prohlášení o vyloučení odpovědnosti. Jejich licence nevyžaduje zveřejnění upraveného zdroje. Původní autorství je zachováno, i když je zdroj aplikace udržován soukromě.

**MinHook/HDE:** zachová upozornění, podmínky a vyloučení odpovědnosti v binární dokumentaci. Poskytuje se úplné kombinované oznámení.

**7-Zip:** zachová upozornění LGPL/BSD/unRAR a poskytne přístup k přesnému nezměněnému zdroji. Zdrojový archiv je uveden výše, spolu s úplným LGPL. Omezení unRAR platí pro příslušný dekompresní kód; toto není paušální závislost MIT. Viz autorův [Časté dotazy k distribuci](https://www.7-zip.org/faq.html).

**Inno Setup:** zachovejte požadovaná upozornění na autorská práva/webové stránky a označte změny zdroje tam, kde je to možné. Kredit neupraveného motoru zůstává v instalačních programech. Upravené katalogy uchovávají původní zdrojová upozornění; jména jsou zde indexována.

**Materiál NVIDIA:** Licence MIT pro integrační hlavičky Streamline nepokrývá každý soubor SDK. Jeho upozornění výslovně odděluje materiál Nsight Perf SDK; tento materiál se v tomto výrobním cíli nepoužívá. Záhlaví NGX podléhají vlastnickým podmínkám RTX SDK společnosti NVIDIA. Jejich plný text byl přidán s [originál-bajtová kopie](../../../NVMFG-Unlock40/LICENSES/NVIDIA-RTX-SDK.original.txt). Omezení oddílu 4(d) týkající se technických omezení zůstává pro použití NVMFG nevyřešeno. Z existence jiného modu není odvozeno žádné souhlasné povolení.

**Externí neznámé/proprietární komponenty:** RTSS, NVCleanstall, NVIDIA ovladače, modely a keylase data patchů nejsou svázána v připravených aktivech centra. Odkazy identifikují jejich skutečné vlastníky. Stažení spuštěné uživatelem znovu nelicencuje komponentu.

Nástroje používají rozhraní API a fonty poskytované Windows. Do tohoto úložiště Git není zkopírován žádný soubor Windows SDK/kompilátor/font. Nástroje pro sestavení a soukromé testy jsou mimo distribuci. Oznámení o interních komponentách za běhu zůstávají v úplném souboru oznámení Microsoft, místo aby byly znovu přiděleny vydavateli.

<a id="publisher-contributions"></a>
## Příspěvky vydavatelů

禅堂 Zendo (RevoluSound Team) udržuje původní práci aplikace, úpravy a dokumentaci popsanou v [provenience průvodce](docs/provenance.md). [NVPI](NVIDIA-Profile-Inspector/README.md), [NVDF](NVDriverForge/README.md), [NVMFG](NVMFG-Unlock40/README.md) a [RP](NVRasterPulse/README.md) rozlišují zděděnou práci od změn.

Nezávislé projekty; není naznačeno žádné spojení s NVIDIA Corporation nebo uvedenými upstream autory, sponzorství nebo oficiální podpora od NVIDIA Corporation.
