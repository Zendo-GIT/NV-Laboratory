<!-- nv-language-navigation:start -->
🌐 [English](../../../../NVDriverForge/README.md) | [Français](../../../../NVDriverForge/README.fr.md) · [NV Laboratory](../README.md)

<details>
<summary>🌐 Language · 34</summary>

[العربية](../../ar/NVDriverForge/README.md) · [বাংলা](../../bn/NVDriverForge/README.md) · [简体中文](../../zh/NVDriverForge/README.md) · **Čeština** · [Dansk](../../da/NVDriverForge/README.md) · [Nederlands](../../nl/NVDriverForge/README.md) · [English](../../../../NVDriverForge/README.md) · [Filipino](../../fil/NVDriverForge/README.md) · [Suomi](../../fi/NVDriverForge/README.md) · [Français](../../../../NVDriverForge/README.fr.md) · [Deutsch](../../de/NVDriverForge/README.md) · [Ελληνικά](../../el/NVDriverForge/README.md) · [हिन्दी](../../hi/NVDriverForge/README.md) · [Magyar](../../hu/NVDriverForge/README.md) · [Bahasa Indonesia](../../id/NVDriverForge/README.md) · [Italiano](../../it/NVDriverForge/README.md) · [日本語](../../ja/NVDriverForge/README.md) · [한국어](../../ko/NVDriverForge/README.md) · [मराठी](../../mr/NVDriverForge/README.md) · [فارسی](../../fa/NVDriverForge/README.md) · [Polski](../../pl/NVDriverForge/README.md) · [Português](../../pt/NVDriverForge/README.md) · [ਪੰਜਾਬੀ](../../pa/NVDriverForge/README.md) · [Română](../../ro/NVDriverForge/README.md) · [Русский](../../ru/NVDriverForge/README.md) · [Español](../../es/NVDriverForge/README.md) · [Kiswahili](../../sw/NVDriverForge/README.md) · [Svenska](../../sv/NVDriverForge/README.md) · [தமிழ்](../../ta/NVDriverForge/README.md) · [ไทย](../../th/NVDriverForge/README.md) · [Türkçe](../../tr/NVDriverForge/README.md) · [Українська](../../uk/NVDriverForge/README.md) · [اردو](../../ur/NVDriverForge/README.md) · [Tiếng Việt](../../vi/NVDriverForge/README.md)

[Translation policy](../../README.md)

</details>
<!-- nv-language-navigation:end -->

<!-- nv-translation-notice:start -->
> Strojově podporovaný překlad z angličtiny. Technické názvy, příkazy, URL a původní právní texty jsou zachovány. Recenze rodilým mluvčím je vítána; Pokud je znění nejasné, nahlédněte do anglického odkazu.
<!-- nv-translation-notice:end -->

<a id="nvdriverforge"></a>
# NVDriverForge

**Připravte si instalaci ovladače NVIDIA s jasným výběrem komponent a volitelným nastavením.**

[Stáhněte si 0.1.3 a stav](../docs/downloads.md#nvdriverforge) · [Instalace](#installation) · [Kredity](#credits-and-upstream) · [Licence](../../../../NVDriverForge/LICENSE)

<a id="overview-and-purpose"></a>
## Přehled a účel

NVDriverForge vás provede originálním balíčkem ovladače NVIDIA: vyberte ovladač, prohlédněte si jeho součásti, prohlédněte si volitelná vylepšení a potvrďte instalaci. Existuje proto, aby byly tyto volby srozumitelné a aby byly informace o instalaci, privilegovaných operacích a obnově pohromadě.

Je to nezávisle vyvinutá aplikace inspirovaná částečně pracovním postupem NVCleanstall. Nezahrnuje NVCleanstall ani nárok na úplnou paritu funkcí.

<a id="features"></a>
## Vlastnosti

- NVIDIA Game Ready / Studio vyhledávání a stahování; volitelné zjišťování opravy hotfix s ručním zálohováním.
- Analýza původního balíčku, hashů, podpisů NVIDIA, manifestů a kompatibilních položek INF.
- Výběr komponent se závislostmi a zachování neznámých komponent.
- Verze 0.1.3 ponechává vybrané volitelné komponenty NVIDIA přeskočitelné a ze zjišťování vylučuje pouze ověřené nekontrolované komponenty. Již aktuální nebo neaplikovatelné volitelné runtimes již nejsou nuceny jako kritické komponenty.
- Jasné shrnutí selhání instalace a přístup k podrobným protokolům ve všech 34 jazycích.
- Explicitní potvrzení instalace, chráněná příprava a export existujících balíčků úložiště ovladačů.
- Volitelná pokročilá nastavení s kontrolami před výstupem, deníky a obnovou s ohledem na konflikty.
- Volitelná předvolba **Custom NV** s pojmenovanými volbami a vysvětlením, včetně samostatného výběru síly SILK a kontrol kompatibility.
- Volitelné stahování oprav přesné verze NVENC; jsou kontrolovány zdrojové potvrzení a cílové bajty.
- Samostatná volitelná instalace Profile Inspector fork z obrazovky Nástroje.
- Volitelné instalované uživatelské aktualizace, 34 jazyků rozhraní a čtyři motivy.

Dostupné pokročilé možnosti se týkají MPO, indikátoru DLSS, Ansel, NVIDIA zvukového spánku, MSI, zásady/priority přerušení, HDCP, spouštění zobrazovacího kontejneru a způsobilé starší služby telemetrie. Každý má své vlastní předpoklady a účinky; nejedná se o univerzální vylepšení výkonu.

<a id="compatibility"></a>
## Kompatibilita

| Požadavek | Podrobnosti |
| --- | --- |
| Systém | Windows 10 sestavení 19041 nebo novější / Windows 11, x64 |
| GPU/ovladač | Kompatibilní balíček NVIDIA a detekovaný hardware; automatické vyhledávání v katalogu pokrývá především známé modely GeForce |
| Doba běhu | .NET 8 / WPF 8.0.31 součástí připraveného samostatného balíčku |
| privilegia | Normální nastavení uživatelského rozhraní/uživatele; instalace ovladače a změny systému vyžadují přístup správce |
| Síť | Vyžadováno pro online vyhledávání/stahování NVIDIA a explicitní upstream požadavky NVENC; lze vybrat místní originální ovladač |
| Zahrnuté nástroje | Neupravený 7-Zip 26.03, upozornění za běhu, volitelný doprovod MIT Profile Inspector |
| Volitelný společník | .NET Framework 4.8 pro samostatný Profile Inspector fork |

Žádná libovolná minimální verze ovladače nepokrývá všechny funkce. Vyhledávání více GPU se musí shodovat s každým zjištěným GPU. Nepodporované/profesionální modely mohou vyžadovat ruční výběr ovladače. Instalační program NVIDIA zůstává konečnou autoritou hardwaru/OS.

<a id="installation"></a>
## Instalace

1. Navštivte [stahování](../docs/downloads.md#nvdriverforge) a potvrďte vydání vydání.
2. Vyberte `NVDriverForge-Setup.exe` pro instalaci nebo `NVDriverForge.exe` pro přenosné použití.
3. Porovnejte SHA-256 s vydáním `SHA256SUMS.txt`.
4. Spusťte instalační program pro instalaci pro uživatele a standardní odinstalační program nebo umístěte přenosný EXE do zapisovatelné složky a otevřete jej.

Přenosný počítač obsahuje běhové prostředí a volitelný instalační program. Instalace NVDriverForge nenainstaluje ovladač GPU. Jeho EXE jsou aktuálně nepodepsané.

<a id="usage"></a>
## Využití

1. **Ovladač:** stáhněte si z NVIDIA nebo vyberte originální instalační EXE NVIDIA. Nechte analýzu dokončit.
2. **Komponenty:** zkontrolujte popisy a požadované závislosti. Neznámé součásti jsou zachovány.
3. **Tweaks:** nechtěné možnosti beze změny. Než něco vyberete, přečtěte si efekty a kompromisy.
4. **Kontrola:** zkontrolujte přesný ovladač, součásti a volitelné operace a potvrďte instalaci.
5. Přijměte UAC pouze pro operaci, kterou jste vybrali. Uschovejte pokyny k obnově chráněné úlohy.
6. Pokud nový ovladač potřebuje restart, postupujte podle hlášeného stavu. Odložené operace vyžadují po tomto restartu explicitní obnovení.

Custom NV se spustí beze změny. Vyberte jednotlivé pojmenované hodnoty nebo si prohlédněte dodanou předvolbu a její výjimky. Jeho dvě informační vnitřní pole nejsou zapsána nezávisle. Nastavení se použijí pouze v ověřeném pracovním postupu nového ovladače, nikdy ne otevřením náhledu. Instalace samostatného editoru NVPI není nutná.

Volitelná práce NVENC stahuje kompatibilní data z připojeného potvrzení keylase. Změní dvě knihovny DLL ovladače a zneplatní jejich podpisy; může být odmítnut Windows, kodéry, DRM nebo anti-cheat. Žádná taková data nebo knihovna DLL NVIDIA nejsou v NVDriverForge vloženy. [Provenience a licenční limity](../docs/provenance.md).

Předvolby řídí jazyk, motiv a volitelné kontroly aktualizací nainstalovaných uživatelem. Přenosný počítač nevytváří nainstalovanou úlohu kontroly pozadí. Nástroje a obnova jsou odděleny od čtyř kroků instalace.

<a id="screenshots"></a>
## Snímky obrazovky

![Náhled stránky ovladače NVDriverForge](../../../../assets/screenshots/nvdriverforge-0.1.2-preview.png)

Stávající vykreslení francouzského uživatelského rozhraní 0.1.2 s ukázkovými daty; zachován jako náhled rozhraní. Zobrazený ovladač 699.99 je testovací zařízení, nikoli skutečná verze ke stažení. [Image provenience](../assets/README.md).

<a id="update-and-uninstall"></a>
## Aktualizujte a odinstalujte

Zavřete NVDriverForge, získejte další oficiální balíček a ověřte jeho hash. Použijte stejnou identitu instalačního programu pro nainstalovanou aktualizaci; vyměňte uzavřený přenosný EXE za nový. Uchovávejte nastavení a chráněné úlohy.

Uninstall od Windows **Installed apps**. Odebere aplikaci a její aktualizační úlohu, nikoli ovladač NVIDIA. Nastavení, protokoly a zálohy zůstávají. V případě potřeby obnovte pokročilé/NVENC pomocí zdokumentovaného postupu obnovy **před** odebráním aplikace. Obnovení odmítne konfliktní změny z jiného nástroje.

Místní data jsou pod `%LOCALAPPDATA%\NVDriverForge`; chráněné úlohy a exporty ovladačů jsou pod `%PROGRAMDATA%\NVDriverForge\Jobs`. Přenosné použití také vytváří místní data. Export z úložiště ovladačů není obraz systému ani záloha úplného profilu.

<a id="known-limitations"></a>
## Známá omezení

- Žádné přidávání hardwaru/úpravy INF, regenerované signatury NVIDIA, odstoupení kompatibilní s anti-cheatem nebo automatické přijímání upozornění bez podpisu.
- Žádné úplné odstranění telemetrie/reklamy, export tenkých balíčků nebo automatický úplný návrat k předchozímu ovladači.
- Instalace ovladače, obnova spouštění a volitelné zápisy profilu nebyly na skutečných počítačích komplexně ověřeny auditem hubu.
- Zpětné čtení registru není důkazem skutečných účinků HDCP, výkonu nebo latence.
- Kontroly podpisu používají lokálně dostupný důvěryhodnost Windows; online odvolání se neprovádí.
- K dispozici je 34 jazyků, ale úplné testování rodilého mluvčího/přístupnosti zůstává neúplné.

<a id="troubleshooting"></a>
## Odstraňování problémů

| Symptom | Akce |
| --- | --- |
| Online katalog není k dispozici | Vyberte originální balíček z [Stažení ovladačů NVIDIA](https://www.nvidia.com/en-us/drivers/). Nenahrazujte sousední model GPU. |
| Vyhledávání opravy hotfix není k dispozici | Použijte [Fórum ovladačů NVIDIA Game Ready](https://www.nvidia.com/en-us/geforce/forums/game-ready-drivers/13/) a ověřte skutečný balíček. |
| Instalace NVIDIA se nezdařila | Přečtěte si souhrn poruch a otevřete podrobné protokoly. Volitelné komponenty, které jsou již aktuální nebo nepoužitelné, lze v 0.1.3 přeskočit. Neúspěšné instalace nespustí volitelná vylepšení ani tok úspěchu/restartování. |
| Selhání podpisu/hash/zálohování | Zastavte tuto instalaci a ponechte chybu; v případě poškození získejte znovu původní balíček. |
| Možnost nedostupná | Přečtěte si důvod hardwaru, součásti nebo cílového ovladače; ponechat beze změny. |
| Restart nebo úloha stále čeká | Použijte pokyny k obnově úlohy a explicitní obnovení; nemažte jeho deník. |
| Obnovit konflikt | Jiný stav se liší od zaznamenané transakce. Zachovejte jej a požádejte o pomoc namísto vynucení obnovení. |

Pro zprávy zahrňte vybranou verzi nástroje, Windows, GPU, ovladač a reprodukovatelné kroky; redigovat cesty a osobní údaje z protokolů. [Podpora](../docs/support.md).

<a id="faq"></a>
## FAQ

**Instaluje instalační program grafický ovladač?** Ne. To vyžaduje samostatnou analýzu, kontrolu, potvrzení a vyšší instalační proces aplikace.

**Potřebuji NVCleanstall nebo NVPI?** Ne. NVCleanstall je pouze inspirace. Doprovodník Profile Inspector je nezávislý volitelný editor.

**Zmenší nebo zrychlí každý ovladač NVIDIA?** Ne. Vybrané komponenty a předpoklady určují, co se může změnit; není slíben žádný naměřený zisk.

**Kde jsou zdroje?** Zdroje specifické pro aplikaci a soukromé testy jsou spravovány odděleně. Toto centrum poskytuje dokumentaci, binární soubory a odkazy na zdroje třetích stran potřebné pro přiřazení/licencování.

<a id="credits-and-upstream"></a>
## Kredity a upstream

Původní aplikace, workflow, transakce, lokalizace, bootstrap a úpravy: 禅堂 Zendo (RevoluSound Team).

- [NVCleanstall / TechPowerUp](https://www.techpowerup.com/download/techpowerup-nvcleanstall/): inspirace workflow; není importován žádný zdroj ani binární soubor.
- [NVIDIA Profile Inspector / Orbmu2k](https://github.com/Orbmu2k/nvidiaProfileInspector): Motivy MIT, rozšířená reference rozhraní NVAPI a samostatně zabalené fork.
- [7-Zip / Igor Pavlov](https://www.7-zip.org/): neupravené extrakční nástroje.
- [Microsoft .NET](https://github.com/dotnet/runtime) a [WPF](https://github.com/dotnet/wpf): sdružené běhové prostředí.
- [Inno Setup](https://jrsoftware.org/isinfo.php): původní instalační modul a připsané překlady.
- [keylase/nvidia-patch](https://github.com/keylase/nvidia-patch): externí volitelný zdroj dat NVENC; licence k redistribuci není zřízena.
- [NVIDIA](https://www.nvidia.com/en-us/drivers/): stažení externích ovladačů a nainstalované knihovny NVAPI/NVML.

[Kompletní tabulka komponent](../THIRD_PARTY_NOTICES.md) · [Proměny a provenience](../docs/provenance.md)

<a id="license"></a>
## Licence

[Existující oprávnění k binární distribuci](../../../../NVDriverForge/LICENSE) umožňuje použití a sdílení neupravených oficiálních spustitelných souborů s jejich upozorněními. Práva zdroje specifická pro aplikaci jsou vyhrazena. Neomezuje práva udělená samostatnými licencemi třetích stran. [Úplné oznámení](LICENSES/README.md).

Nezávislé na NVIDIA Corporation, TechPowerUp a keylase; jimi nesponzorované ani oficiálně nepodporované. Názvy produktů zůstávají ochrannými známkami jejich vlastníků.
