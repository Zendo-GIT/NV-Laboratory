<!-- nv-language-navigation:start -->
🌐 [English](../../../../NVMFG-Unlock40/README.md) | [Français](../../../../NVMFG-Unlock40/README.fr.md) · [NV Laboratory](../README.md)

<details>
<summary>🌐 Language · 34</summary>

[العربية](../../ar/NVMFG-Unlock40/README.md) · [বাংলা](../../bn/NVMFG-Unlock40/README.md) · [简体中文](../../zh/NVMFG-Unlock40/README.md) · **Čeština** · [Dansk](../../da/NVMFG-Unlock40/README.md) · [Nederlands](../../nl/NVMFG-Unlock40/README.md) · [English](../../../../NVMFG-Unlock40/README.md) · [Filipino](../../fil/NVMFG-Unlock40/README.md) · [Suomi](../../fi/NVMFG-Unlock40/README.md) · [Français](../../../../NVMFG-Unlock40/README.fr.md) · [Deutsch](../../de/NVMFG-Unlock40/README.md) · [Ελληνικά](../../el/NVMFG-Unlock40/README.md) · [हिन्दी](../../hi/NVMFG-Unlock40/README.md) · [Magyar](../../hu/NVMFG-Unlock40/README.md) · [Bahasa Indonesia](../../id/NVMFG-Unlock40/README.md) · [Italiano](../../it/NVMFG-Unlock40/README.md) · [日本語](../../ja/NVMFG-Unlock40/README.md) · [한국어](../../ko/NVMFG-Unlock40/README.md) · [मराठी](../../mr/NVMFG-Unlock40/README.md) · [فارسی](../../fa/NVMFG-Unlock40/README.md) · [Polski](../../pl/NVMFG-Unlock40/README.md) · [Português](../../pt/NVMFG-Unlock40/README.md) · [ਪੰਜਾਬੀ](../../pa/NVMFG-Unlock40/README.md) · [Română](../../ro/NVMFG-Unlock40/README.md) · [Русский](../../ru/NVMFG-Unlock40/README.md) · [Español](../../es/NVMFG-Unlock40/README.md) · [Kiswahili](../../sw/NVMFG-Unlock40/README.md) · [Svenska](../../sv/NVMFG-Unlock40/README.md) · [தமிழ்](../../ta/NVMFG-Unlock40/README.md) · [ไทย](../../th/NVMFG-Unlock40/README.md) · [Türkçe](../../tr/NVMFG-Unlock40/README.md) · [Українська](../../uk/NVMFG-Unlock40/README.md) · [اردو](../../ur/NVMFG-Unlock40/README.md) · [Tiếng Việt](../../vi/NVMFG-Unlock40/README.md)

[Translation policy](../../README.md)

</details>
<!-- nv-language-navigation:end -->

<!-- nv-translation-notice:start -->
> Strojově podporovaný překlad z angličtiny. Technické názvy, příkazy, URL a původní právní texty jsou zachovány. Recenze rodilým mluvčím je vítána; Pokud je znění nejasné, nahlédněte do anglického odkazu.
<!-- nv-translation-notice:end -->

<a id="nvmfg-unlock40"></a>
# NVMFG Unlock40

**Experimentální NVIDIA Multi Frame Generation pro GeForce RTX 40, s centrálním ovladačem a možnostmi pro jednotlivé hry.**

[Stáhněte si 0.2.3 a stav](../docs/downloads.md#nvmfg-unlock40) · [Instalace](#installation) · [Proti proudu](#upstream-and-modifications) · [licence](LICENSES/README.md)

<a id="overview-and-purpose"></a>
## Přehled a účel

NVMFG Unlock40 je nezávisle vyvinutá aplikace od 禅堂 Zendo (RevoluSound Team). Kombinuje ovladač Windows, nativní vrstvu, pomocníka profilu a správu her/Streamline SDK. Zaměřuje se na hry, které již integrují NVIDIA DLSS Frame Generation a kompatibilní runtime NVIDIA.

[RTX40MFG-Unlock](https://github.com/dashdogy/RTX40MFG-Unlock) byl konzultován k porovnání a upřesnění práce. Aktuální nativní vrstva obsahuje sdílené a přizpůsobené komponenty, které jsou jednotlivě uvedeny níže. Tento odkaz nedělá z celé aplikace NVMFG fork tohoto projektu.

Existuje proto, aby centrálně koordinoval experimentální chování MFG, pamatoval si volby specifické pro hru a udržoval aktualizace a zálohy za běhu viditelné. Nepřidává DLSS Frame Generation do každé hry ani nepřevádí libovolnou implementaci FSR.

Aktuální balíček je **0.2.3**. Přidává trvalou herní knihovnu, informace o aktivitě a schopnostech, místní diagnostiku a opravené chování při výběru/postupu. [Stahování](../docs/downloads.md#nvmfg-unlock40) identifikuje přesné soubory a hash.

<a id="features"></a>
## Vlastnosti

- Centrální ovládání zapnutí/vypnutí a spuštění volitelného zásobníku Windows.
- Výběr podle hry mezi Dynamic MFG, nastavení hry a podporované pevné násobiče.
- Samostatné zapamatované volby pro pozorované stavy zapnutí/vypnutí V-Sync.
- Dynamic používá režim NVIDIA; je pozastaveno, když je V-Sync vypnuto, se samostatnou volbou ve hře/pevnou volbou.
- Vedení herního menu a trvalé vyloučení; hry bez DLSS FG zůstanou pod kontrolou.
- Objevování her, výběr nadřazených složek, vyhledávání, seskupování a odstraňování bez mazání herních souborů.
- Streamline Stažení/import SDK, ověřená místní mezipaměť, explicitní výběr, zálohování a obnova pro jednotlivé hry.
- Ověření nativního poskytovatele, diagnostika na relaci, deník globálního profilu a obnova s ohledem na konflikty.
- 34 jazyků rozhraní a čtyři témata.

Vypnutím FG ve hře to zůstane vypnuté. Pevné možnosti od 2x do 6x závisí na hře/menu/runtime; nejsou příslibem, že každá kombinace funguje. Ovladač sleduje V-Sync a nenastaví pro uživatele V-Sync nebo VRR.

<a id="compatibility"></a>
## Kompatibilita

| Požadavek | Podrobnosti |
| --- | --- |
| Systém | Windows 10/11 x64 |
| GPU | GeForce RTX 40 cíl; žádný univerzální nárok na kompatibilitu GPU |
| Hra | Stávající integrace NVIDIA DLSS Frame Generation a podporované běhové prostředí; žádná certifikace anti-cheat kompatibility |
| Poskytovatel | Kandidát je připojen k poskytovateli SHA-256 dokumentovanému v [provenience](../docs/provenance.md); neznámé hashe jsou odmítnuty |
| Doba běhu | Přibalený .NET 8/WPF 8.0.30 pro aplikaci/agenta; .NET Framework 4.8 pro pomocníky s profily |
| Oprávnění | Administrátorský přístup pro operace řadiče/profilu |
| Síť | Vyžadováno pro vybraná oficiální stahování SDK; importovaný kompatibilní SDKs lze lokálně uložit do mezipaměti |
| Externí dvojhvězdy | Ovladač NVIDIA, poskytovatel/modely NGX a runtime hry Streamline nejsou součástí balení |

Samotný štítek verze nestačí: záleží na ovladači, hash poskytovatele, integraci hry a skutečně načtených modulech. Chráněné nebo nekompatibilní procesy mohou odmítnout připojení. Aplikace není navržena tak, aby se vyhnula ochraně proti podvádění.

<a id="installation"></a>
## Instalace

1. Přečtěte si [status kandidáta a licenční poznámka](../docs/downloads.md#nvmfg-unlock40).
2. Stáhněte si `NVMFGUnlock40-0.2.3-Setup-x64.exe` nebo `NVMFGUnlock40-0.2.3-Portable-x64.zip`, jakmile bude k dispozici jeho vydání.
3. Zkontrolujte SHA-256 a uschovejte si doprovodná upozornění. Nainstalujte rozhraní .NET Framework 4.8, pokud jej Windows již neposkytuje.
4. Spusťte instalaci nebo extrahujte **celý** přenosný ZIP do zapisovatelné místní složky.
5. Spusťte `NVMFGUnlock40.exe`; ponechte `agent`, `driver`, `engine` a `Licenses` v dodaném rozložení.

Složka s názvem `driver` obsahuje pomocníky uživatelského prostoru, nikoli ovladač jádra. Nekopírujte pouze hlavní EXE ani nenahrazujte hash poskytovatele, abyste vynutili kompatibilitu. Aktuální EXE jsou nepodepsané.

<a id="usage"></a>
## Využití

1. Začněte s deaktivovaným ovladačem. Přidejte hru nebo nadřazenou složku a vyberte skutečné instalace.
2. Zkontrolujte nastavení MFG každé hry. Odpovězte, co nabízí její nabídka; odpověď je uložena pro každou hru.
3. Vyberte Dynamic nebo nastavení ve hře globálně a poté podle potřeby upravte možnosti pro jednotlivé hry.
4. Povolte ovladač pouze v případě, že jej hodláte používat. Může dočasně změnit šest globálních nastavení profilu NVIDIA pomocí deníku obnovy.
5. Spusťte vhodnou hru a povolte její vlastní DLSS Frame Generation. Postupujte podle jakéhokoli požadavku na volbu V-Sync-off.
6. Použijte výjimky pro hry, které nechcete spravovat. Odstranění hry zaznamená vyloučení a zachová její soubory/zálohy.
7. Po dokončení použijte postup úplného ukončení/deaktivace a obnovení aplikace.

Zavřením hlavního okna může ovladač zůstat v zásobníku. DLL již načtená do hry tam zůstává, dokud hra neskončí; deaktivace ovladače není zárukou vyložení. Před údržbou nebo aktualizacemi zavřete dotčené hry.

**Streamline SDKs:** Na stránce NVIDIA SDK si stáhněte oficiální verzi nebo importujte kompatibilní místní SDK. Import ukládá ověřenou kopii; **Use this version** jej vybere a **Uninstall** odstraní kopii uloženou v mezipaměti. Chybějící Streamline DLL lze doplnit z oficiálního NVIDIA SDK s uvedeným zdrojem. Toto nestahuje/nenahrazuje model NGX. Zavřete hru, vyberte zamýšlenou aktualizaci hry a ponechte si její původní zálohu. Chcete-li vrátit soubory hry, použijte obnovení zálohy, nikoli tlačítko Uninstall mezipaměti.

<a id="library-diagnostics-and-updates"></a>
## Knihovna, diagnostika a aktualizace

**Trvalá knihovna:** před zahájením jednoho skenování vyberte několik herních složek, včetně různých jednotek. Je vidět pokrok a je možné zrušení. Po prvním skenování obnoví místní mezipaměť knihovnu při spuštění bez procházení každé složky hry. Obnovte pro nalezení změn nebo přidejte další složku. Operace údržby stále obnovují platnost dotčených souborů; monitorování zálohování zůstává aktivní. Mezipaměť je uložena na adrese `%LOCALAPPDATA%\RtxMfg\library-cache.json`.

**Výběr:** Ctrl+A vybere vše a Ctrl+D vymaže aktivní kartu Hry nebo Zálohy. Automaticky není vybrána žádná hra. Aktualizace a aktualizace aktivit již nevytvářejí výběry duchů nebo nekonzistentní počty.

**Aktivita a kompatibilita:** Informace MFG pro jednotlivé hry pocházejí z pozorování NGX bez nového překrytí. Nejedná se o fyzický počet zobrazených snímků. Podpora Dynamic-s-V-Sync pochází z možností běhu; neznámá schopnost není odvozena z čísla verze. Aplikace nemění ani V-Sync ani VRR. Při vypnutém V-Sync zůstane Dynamic pozastavený; pevné nebo herně řízené volby jsou samostatné.

**Příští spuštění:** dočasné vyloučení přeskočí opravy při příštím spuštění hry a po jejím ukončení obnoví normální správu. Nemůže odstranit DLL již načtenou ve hře: zavřete a restartujte tuto hru. Wallpaper Engine je rozpoznán jako desktopová aplikace; tato oprava zachovává ochranu pro skutečné ignorované hry.

**Předvolby a podpora:** import/export předvoleb vyžaduje ruční opětovné přiřazení herních složek. Místní diagnostika v části O aplikaci filtruje soukromé informace a hlásí dostupné chybové kódy NVAPI nebo kategorie konfliktů. Před sdílením jej zkontrolujte; nic se nenahrává automaticky.

**Aktualizace aplikací:** volitelná kontrola zobrazuje poznámky k vydání a nabízí oficiální nastavení. Explicitní stahování se kontroluje podle velikosti GitHub a metadat SHA-256; instalaci spustíte sami. Verze 0.2.3 také vymaže dokončené zprávy o průběhu a zachová smysluplné chyby a výsledky. Tyto doplňky zahrnují změny od veřejné verze 0.1.1.

<a id="screenshots"></a>
## Snímky obrazovky

![Náhled seznamu NVMFG SDK](../../../../assets/screenshots/nvmfg-0.1.1-sdk-preview.png)

Stávající vykreslení anglického rozhraní 0.1.1 s ukázkovým inventářem SDK. Nejedná se o aktuální seznam verzí ani důkaz o běžící hře. [Image provenience](../assets/README.md).

<a id="update-and-uninstall"></a>
## Aktualizujte a odinstalujte

Zavřete postižené hry. Před aktualizací deaktivujte/ukončete NVMFG a vyřešte všechna čekající obnova nastavení NVIDIA. Nainstalujte další instalační program se stávající identitou nebo extrahujte nový přenosný počítač do nové složky; zachovat stav/zálohy.

Před odinstalací obnovte požadované zálohy hry SDK a nastavení NVIDIA prostřednictvím aplikace, poté zavřete hry a ukončete ovladač. Pro instalaci použijte Windows **Installed apps** nebo po zachování potřebných souborů odeberte uzavřenou přenosnou složku. Neodstraňujte ručně aktivní deník obnovy, abyste odblokovali nastavení.

Místní zálohy za běhu hry používají `%LOCALAPPDATA%\NvidiaStreamlineMaintenance\Backups`. Nastavení MFG/data SDK používají `%LOCALAPPDATA%\RtxMfg`; výstup relace je pod `Sessions` vedle aplikace. Tyto soubory mohou obsahovat cesty hry. Nezveřejňujte je bez úprav.

<a id="known-limitations"></a>
## Známá omezení

- Hlášená blokace aktivace/obnovy/odinstalace 0.1.1 zůstává nereprodukována a její příčina není známa. Toto vydání si nečiní nárok na opravu. Po selhání uchovejte žurnál obnovy a zkontrolujte místní diagnostiku; nevynucujte smazání dat pro obnovu.
- Experimentální nativní záplaty mohou způsobit pády nebo vizuální artefakty; v historii vývoje je zaznamenán nevyřešený pád Bodycam.
- Kontrolované testy rendereru nejsou certifikací pro každou hru, ovladač nebo anti-cheat.
- Generované snímky nevytvářejí nové vstupní vzorky; tento hub neslibuje žádnou měřenou latenci ani zvýšení výkonu.
- Několik nástrojů/překryvů pro generování rámců může být v konfliktu. Aplikace hlásí pozorované moduly, aniž by prokázala každý scénář koexistence.
- Manifest kompatibility je detekční pomůcka, nikoli seznam plně testovaných her.
- Úplné podmínky NVIDIA SDK a nevyřešená technická omezení zůstávají zdokumentovány v [provenience](../docs/provenance.md).

<a id="troubleshooting"></a>
## Odstraňování problémů

| Symptom | Akce |
| --- | --- |
| Poskytovatel není podporován | Ponechte původní ověřené soubory. Hlásit verze ovladače/poskytovatele a chybu; nevynechejte kontrolu hash. |
| Ve hře není DLSS FG | Vyberte tuto odpověď a nechte hru pod kontrolou; tento nástroj nemůže vytvořit tuto integraci. |
| Selhání hry/artefakty | Ukončete hru, deaktivujte NVMFG, použijte původní zálohu běhového prostředí hry, pokud byla změněna, a nahlaste reprodukovatelné podrobnosti. |
| Seznam nebo stažení SDK není k dispozici | Aktualizujte a zkontrolujte oficiální zdroj; verze uložená v mezipaměti/importovaná musí stále projít ověřením. |
| Čekající obnovení NVIDIA blokuje ukončení/aktualizaci | Použijte obnovu a zachovejte deník; konflikty se nesmí slepě přepisovat. |
| Odebraná hra se znovu neobjeví | Jeho vyloučení je trvalé. Přidejte ji explicitně, když ji chcete znovu spravovat. |

[Sdílené pokyny pro podporu](../docs/support.md) vysvětluje, co zahrnout do sestavy.

<a id="faq"></a>
## FAQ

**Zahrnuje NVIDIA DLL nebo modely?** Není zahrnut žádný ovladač, poskytovatel/model NGX nebo runtime Streamline. Explicitní stahování SDK pochází z NVIDIA.

**Funguje Dynamic s vypnutým V-Sync?** V tomto stavu je pozastaveno. Vyberte nastavení ve hře nebo vhodný pevný násobitel pro samostatný stav dané hry.

**Jedná se o balíček ReShade/OptiScaler/FSR?** Ne. Tyto balíčky nejsou kompilovány ani dodávány jako součást tohoto produkčního balíčku.

**Jsou upravené zdroje veřejné?** Ne. Jsou poskytovány zkompilované balíčky a požadované kredity/licence. Tím nejsou odstraněna práva nebo omezení třetích stran.

<a id="upstream-and-modifications"></a>
## Upstream a modifikace

Srovnávací reference a sdílené nativní komponenty: **RTX40MFG-Unlock od Michael Robles / dashdogy**, potvrzení reference `4e776d068f91b4a665425542bb005dd57cc3d891`, MIT. [Úložiště](https://github.com/dashdogy/RTX40MFG-Unlock) · [Původní stahování](https://github.com/dashdogy/RTX40MFG-Unlock/releases).

Porovnání zdrojů identifikuje sdílené opravy, zpracování poskytovatelů/zásad, časové opravy a komponenty objížďky založené na MinHook. Jejich upozornění MIT a BSD jsou zachována. Kompletní srovnání zahrnuje i soubory mimo produkční cíl.

Desktopovou aplikaci, řadič a pracovní postup správy SDK vyvinul 禅堂 Zendo (RevoluSound Team). Projektová práce zahrnuje centrální načítání, integraci bootstrapu NGX, ověřený výběr poskytovatele, koordinaci hry/V-Sync a diagnostiku relace. Průvodce proveniencí odděluje práci od sdílených komponent; samotné srovnání souborů neurčuje, kdy kterýkoli autor měl nápad.

Pomocník profilu přizpůsobí obal MIT NVAPI z Profile Inspector od Orbmu2k. [Detailní původ a rozsah komponent](../docs/provenance.md).

<a id="credits-and-license"></a>
## Kredity a licence

Michael Robles; Orbmu2k; přispěvatelé Tsuda Kageyu a HDE; NVIDIA Corporation; Microsoft a přispěvatelé; Autoři a překladatelé Inno Setup. Vývoj aplikací, integrace a balení: 禅堂 Zendo (RevoluSound Team).

[existující oprávnění ke sdílení kompilovaného balíčku](../../../../NVMFG-Unlock40/LICENSE) a všechny [licence komponent](LICENSES/README.md) jsou zachovány. Oprávnění MIT pro upstream kód se liší od podmínek NVIDIA SDK. Žádná paušální licence je nenahrazuje.

Nezávislé na NVIDIA Corporation, nesponzorované ani oficiálně neschválené. Všechny uvedené ochranné známky zůstávají majetkem jejich vlastníků.
