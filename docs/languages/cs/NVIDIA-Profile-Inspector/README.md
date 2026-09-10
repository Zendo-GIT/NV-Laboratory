<!-- nv-language-navigation:start -->
🌐 [English](../../../../NVIDIA-Profile-Inspector/README.md) | [Français](../../../../NVIDIA-Profile-Inspector/README.fr.md) · [NV Laboratory](../README.md)

<details>
<summary>🌐 Language · 34</summary>

[العربية](../../ar/NVIDIA-Profile-Inspector/README.md) · [বাংলা](../../bn/NVIDIA-Profile-Inspector/README.md) · [简体中文](../../zh/NVIDIA-Profile-Inspector/README.md) · **Čeština** · [Dansk](../../da/NVIDIA-Profile-Inspector/README.md) · [Nederlands](../../nl/NVIDIA-Profile-Inspector/README.md) · [English](../../../../NVIDIA-Profile-Inspector/README.md) · [Filipino](../../fil/NVIDIA-Profile-Inspector/README.md) · [Suomi](../../fi/NVIDIA-Profile-Inspector/README.md) · [Français](../../../../NVIDIA-Profile-Inspector/README.fr.md) · [Deutsch](../../de/NVIDIA-Profile-Inspector/README.md) · [Ελληνικά](../../el/NVIDIA-Profile-Inspector/README.md) · [हिन्दी](../../hi/NVIDIA-Profile-Inspector/README.md) · [Magyar](../../hu/NVIDIA-Profile-Inspector/README.md) · [Bahasa Indonesia](../../id/NVIDIA-Profile-Inspector/README.md) · [Italiano](../../it/NVIDIA-Profile-Inspector/README.md) · [日本語](../../ja/NVIDIA-Profile-Inspector/README.md) · [한국어](../../ko/NVIDIA-Profile-Inspector/README.md) · [मराठी](../../mr/NVIDIA-Profile-Inspector/README.md) · [فارسی](../../fa/NVIDIA-Profile-Inspector/README.md) · [Polski](../../pl/NVIDIA-Profile-Inspector/README.md) · [Português](../../pt/NVIDIA-Profile-Inspector/README.md) · [ਪੰਜਾਬੀ](../../pa/NVIDIA-Profile-Inspector/README.md) · [Română](../../ro/NVIDIA-Profile-Inspector/README.md) · [Русский](../../ru/NVIDIA-Profile-Inspector/README.md) · [Español](../../es/NVIDIA-Profile-Inspector/README.md) · [Kiswahili](../../sw/NVIDIA-Profile-Inspector/README.md) · [Svenska](../../sv/NVIDIA-Profile-Inspector/README.md) · [தமிழ்](../../ta/NVIDIA-Profile-Inspector/README.md) · [ไทย](../../th/NVIDIA-Profile-Inspector/README.md) · [Türkçe](../../tr/NVIDIA-Profile-Inspector/README.md) · [Українська](../../uk/NVIDIA-Profile-Inspector/README.md) · [اردو](../../ur/NVIDIA-Profile-Inspector/README.md) · [Tiếng Việt](../../vi/NVIDIA-Profile-Inspector/README.md)

[Translation policy](../../README.md)

</details>
<!-- nv-language-navigation:end -->

<!-- nv-translation-notice:start -->
> Strojově podporovaný překlad z angličtiny. Technické názvy, příkazy, URL a původní právní texty jsou zachovány. Recenze rodilým mluvčím je vítána; Pokud je znění nejasné, nahlédněte do anglického odkazu.
<!-- nv-translation-notice:end -->

<a id="nvidia-profile-inspector--nv-tools-fork"></a>
# NVIDIA Profile Inspector – NV Tools Fork

**Nezávislý fork od [NVIDIA Profile Inspector od Orbmu2k](https://github.com/Orbmu2k/nvidiaProfileInspector) s přidanými ovládacími prvky zobrazení.** Původní název projektu: **NVPI Custom**.

[Stav stahování a vydání](../docs/downloads.md#nvidia-profile-inspector) · [Instalace](#installation) · [Upstream a změny](#upstream-and-changes) · [Licence](../../../../NVIDIA-Profile-Inspector/LICENSE)

<a id="overview"></a>
## Přehled

Aplikace upravuje profily ovladače NVIDIA, včetně nastavení pro jednotlivé aplikace. Tento fork také přidává editor **Screen** pro aktivní displej Windows: rozlišení, obnovovací frekvenci, nastavení barev výstupu, HDR a nainstalované asociace profilů ICC/WCS.

Existuje proto, aby do editoru profilu přinesl související ovládací prvky zobrazení a aby byly výsledky náhledu, potvrzení a obnovení jasnější. Nevytváří nové možnosti hardwaru.

Prvním kandidátem je **3.0.2.3**, který používá vyčištěnou samostatnou doprovodnou sestavu z 9. září 2026. Jeho stávající spustitelný soubor zůstává `nvidiaProfileInspector.exe`; instalační program a některé interní štítky stále říkají `NVPI Custom NV`. Výše uvedený veřejný název identifikuje fork bez změny identity instalace nebo předstírání, že jde o oficiální vydání Orbmu2k.

<a id="features"></a>
## Vlastnosti

- Procházení existujících upstream profilů, přidružení aplikací, úpravy nastavení a import/export profilu.
- **Obrazovka** dialog pro zobrazení, režim, Hz, RGB/YCbCr, barevnou hloubku, rozsah a kolorimetrii.
- Windows Řízení HDR a nainstalovaný výběr přidružení ICC/WCS.
- 15sekundový náhled zobrazení s **Keep** / **Revert** a obnovením časového limitu.
- Zpětné čtení změn režimu/HDR a hlášených selhání obnovy.
- Samostatné hlášení HDR, SDR s ACM/WCG a barevnou hloubkou signálu.
- Spouštěč NVRasterPulse pro způsobilou samostatně instalovanou kopii.

<a id="compatibility"></a>
## Kompatibilita

| Požadavek | Podrobnosti |
| --- | --- |
| Systém | Windows 10/11 x64 s kompatibilním ovladačem NVIDIA |
| Doba běhu | [.NET Framework 4.8](https://dotnet.microsoft.com/en-us/download/dotnet-framework/net48), dodává Windows nebo je instalován samostatně |
| Oprávnění | Editor při otevření požaduje administrátorský přístup |
| Displeje | Skutečné režimy a barevné kombinace závisí na GPU, ovladači, displeji, kabelu a Windows API |
| Volitelné nástroje | NVRasterPulse pro správu limitů RTSS; ani on, ani RTSS není potřeba pro Screen editor |
| Jazyky | Nastavení: 34jazyčný volič. Editor si zachovává stávající jazykovou podporu. |

Pro každý GPU neexistuje žádné ověřené minimum univerzálního ovladače nebo matice podpory. Dostupné volby bpc v dialogu jsou požadavky, nikoli certifikované kombinace. Moderní ovládací prvky HDR a starší záložní Windows mají různé možnosti.

<a id="installation"></a>
## Instalace

1. Otevřete [stránka ke stažení](../docs/downloads.md#nvidia-profile-inspector) a zkontrolujte stav publikace.
2. Stáhněte si instalační nebo přenosný prostředek a porovnejte jeho SHA-256 s manifestem vydání.
3. Pro instalaci spusťte `NVPI-CustomNV-3.0.2.3-Setup-r2.exe`, vyberte jazyk a postupujte podle instalačního programu. Vytvoří si vlastní zástupce a odinstalační program.
4. Pro přenositelnost extrahujte celý ZIP do nové zapisovatelné složky. Udržujte `Reference.xml`, konfiguraci EXE a všechna upozornění vedle spustitelného souboru.
5. Spusťte `nvidiaProfileInspector.exe`.

Samotná instalace editoru nepoužije profil ani nenainstaluje ovladač GPU. Doprovodná aplikace se instaluje samostatně, nepřebírá přidružení `.nip` a nepovoluje spuštění při přihlášení. Stávající binární soubory jsou bez znaménka.

<a id="usage"></a>
## Využití

**Instalační revize 2** přidává stejný nativní 34jazyčný selektor jako ostatní nástroje s navigací pomocí myši/klávesnice, světlým/tmavým vzhledem a zrušením. Volba platí pro nastavení; nepřekládá editor NVPI. Explicitní argument `/LANG=fr` nebo tichý režim obchází výběr pro volající, kteří již poskytují jazyk.

**Profily ovladačů:** vyberte profil, exportujte zálohu, poté upravte pouze zamýšlená nastavení a použijte je. Přidružení aplikací určují, která hra obdrží profil. Uložená hodnota není důkazem, že ji používá každý ovladač nebo hra.

**Ovládací prvky zobrazení:** otevřete **Obrazovku**, vyberte zobrazení a požadované hodnoty a poté spusťte náhled. Před výběrem **Zachovat** do 15 sekund zkontrolujte obrázek. Chcete-li požádat o obnovení, použijte **Vrátit**, zavřete potvrzení nebo nechte vypršet. Přečtěte si jakoukoli zprávu o selhání: samotné úspěšné volání API není důkazem obnovení.

Výběr ICC změní asociaci nainstalovaného profilu; negeneruje, nekalibruje ani nedistribuuje soubor ICC. HDR, ACM/WCG, RGB/YCbCr a bpc popisují různé aspekty potrubí. Není k dispozici žádný nový nezávislý přepínač ACM.

**NVRasterPulse:** tlačítko na panelu nástrojů přijímá samostatně registrovanou celosystémovou instalaci pod Program Files s chráněným vlastnictvím a oprávněními. Přenosná kopie nebo uživatelsky zapisovatelná/propojená cesta může být tímto vyvýšeným spouštěčem odmítnuta. V takovém případě otevřete NVRasterPulse pomocí jeho vlastní zkratky. [Nainstalujte RTSS samostatně](https://www.guru3d.com/download/rtss-rivatuner-statistics-server-download/) pro použití NVRasterPulse.

<a id="screenshots"></a>
## Snímky obrazovky

![Volič jazyka nastavení NVPI revize 2](../../../../assets/screenshots/nvpi-setup-r2-language.png)

Aktuální volič nastavení ve francouzštině, zachycený během izolovaného testu a poté zrušen. Toto ukazuje instalační program; editor si zachová své rozhraní a dialog Screen.

<a id="update-and-uninstall"></a>
## Aktualizujte a odinstalujte

Před aktualizací zavřete editor. Udržujte exportované profily a stáhněte si novou verzi fork; nainstalovat přes stejnou doprovodnou identitu nebo extrahovat přenosné soubory do nové složky. Nemíchejte starý `Reference.xml` s novým spustitelným souborem. Součástí tohoto fork je přibalené potlačení upstream kontroly aktualizací.

Pro nainstalovanou kopii použijte Windows **Installed apps** a jeho odinstalační program. V případě přenositelnosti jej zavřete a odeberte jeho extrahovanou složku, až budou vaše exporty bezpečné. Odebráním editoru **nezrušíte** úpravy profilu ovladače, předvolby zobrazení, NVRasterPulse nebo RTSS. Před odstraněním obnovte požadovaná nastavení.

<a id="known-limitations"></a>
## Známá omezení

- 15sekundové potvrzení není hlídacím psem pro každou havárii řidiče, výpadek napájení nebo nucené vypnutí.
- Některé kombinace barev/hloubka/obnovení vrátí `NVAPI_NOT_SUPPORTED`.
- Zpětné čtení softwaru neměří bitovou hloubku panelu, přesnost barev ani latenci.
- Nastavení obrazovky ovlivňují aktuální zobrazení Windows; tento dialog nevytváří předvolby zobrazení pro jednotlivé hry.
- Žádná záruka výkonu, anti-cheat nebo univerzální kompatibility HDR.

<a id="troubleshooting"></a>
## Odstraňování problémů

| Symptom | Akce |
| --- | --- |
| Chyba runtime při spuštění | Zkontrolujte aktualizace Windows a .NET Framework 4.8; použijte celé balení. |
| Požadovaný režim zobrazení byl zamítnut | Vraťte a otestujte režim nabízený Windows/NVIDIA pro tento displej. Přečtěte si přesnou chybu a vyhněte se opakovaným slepým změnám. |
| HDR nebo barva se vrátí do starého stavu | Zkontrolujte, zda jiná operace selhala a nespustila obnovu; odlišit HDR od ACM. |
| Tlačítko NVRasterPulse odmítá cestu | Spusťte vlastní zkratku; toto tlačítko vyžaduje chráněnou instalaci v celém systému. |
| Po odinstalaci zůstane změna | Obnovte exportovaný profil NVIDIA nebo zamýšlená nastavení zobrazení Windows; odinstalace není vrácením nastavení. |

Před odesláním protokolů si přečtěte [sdílené podpůrné pokyny](../docs/support.md).

<a id="faq"></a>
## FAQ

**Je to oficiální software NVIDIA nebo oficiální sestavení Orbmu2k?** Ne. Je to nezávislý fork; autor upstream a licence MIT zůstávají připsány.

**Vyžaduje NVDriverForge tento editor?** Ne. Volitelná předvolba Custom NV NVDriverForge používá vlastní integraci. Instalace editoru je samostatná volba.

**Je RTSS povinný pro tento fork?** Ne. RTSS je povinný pro omezovač FPS NVRasterPulse, nikoli pro úpravy profilu nebo obrazovky.

**Kde je zdroj?** Upravený zdroj aplikace je udržován soukromě. K dispozici je upozornění MIT a upstream úložiště; MIT nevyžaduje publikování upraveného zdroje.

<a id="upstream-and-changes"></a>
## Upstream a změny

Upstream: [Orbmu2k/nvidiaProfileInspector](https://github.com/Orbmu2k/nvidiaProfileInspector), referenční potvrzení `592d962cca8827efe8859461a84267755595064a`. [Původní stahování](https://github.com/Orbmu2k/nvidiaProfileInspector/releases).

Zděděno: editor profilu, interoperabilita NVAPI, referenční data, zdroje uživatelského rozhraní a motivy. 禅堂 Zendo (RevoluSound Team) přidané nebo upravené zobrazovací služby, transakce HDR/ICC, 15sekundové potvrzení/zpětné čtení, rozložení panelu nástrojů a chování při spouštění RasterPulse. Vyčištěný společník vylučuje vývojové simulace/testovací vstupní body, používá chráněný externí spouštěč a poskytuje samostatný instalační program. Starý kombinovaný vývojový balíček NVPI/RasterPulse není v tomto centru kandidátem.

[Podrobná provenience souboru](../docs/provenance.md) · [Původní oznámení fork](../../../../NVIDIA-Profile-Inspector/LICENSES/ORIGINAL-FORK-NOTICE.txt)

<a id="credits-and-license"></a>
## Kredity a licence

Copyright (c) 2016 Orbmu2k. Dodaný [Licence MIT](../../../../NVIDIA-Profile-Inspector/LICENSE) zůstane zachován. Úpravy a balení: 禅堂 Zendo (RevoluSound Team). Instalační program používá Inno Setup; Windows a .NET Framework zůstávají externí. [Úplná platná upozornění](LICENSES/README.md).

Nezávislé na NVIDIA Corporation, nesponzorované ani oficiálně nepodporované. Ochranné známky zůstávají u příslušných vlastníků.
