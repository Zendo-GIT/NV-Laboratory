<!-- nv-language-navigation:start -->
🌐 [English](../../../../NVRasterPulse/README.md) | [Français](../../../../NVRasterPulse/README.fr.md) · [NV Laboratory](../README.md)

<details>
<summary>🌐 Language · 34</summary>

[العربية](../../ar/NVRasterPulse/README.md) · [বাংলা](../../bn/NVRasterPulse/README.md) · [简体中文](../../zh/NVRasterPulse/README.md) · **Čeština** · [Dansk](../../da/NVRasterPulse/README.md) · [Nederlands](../../nl/NVRasterPulse/README.md) · [English](../../../../NVRasterPulse/README.md) · [Filipino](../../fil/NVRasterPulse/README.md) · [Suomi](../../fi/NVRasterPulse/README.md) · [Français](../../../../NVRasterPulse/README.fr.md) · [Deutsch](../../de/NVRasterPulse/README.md) · [Ελληνικά](../../el/NVRasterPulse/README.md) · [हिन्दी](../../hi/NVRasterPulse/README.md) · [Magyar](../../hu/NVRasterPulse/README.md) · [Bahasa Indonesia](../../id/NVRasterPulse/README.md) · [Italiano](../../it/NVRasterPulse/README.md) · [日本語](../../ja/NVRasterPulse/README.md) · [한국어](../../ko/NVRasterPulse/README.md) · [मराठी](../../mr/NVRasterPulse/README.md) · [فارسی](../../fa/NVRasterPulse/README.md) · [Polski](../../pl/NVRasterPulse/README.md) · [Português](../../pt/NVRasterPulse/README.md) · [ਪੰਜਾਬੀ](../../pa/NVRasterPulse/README.md) · [Română](../../ro/NVRasterPulse/README.md) · [Русский](../../ru/NVRasterPulse/README.md) · [Español](../../es/NVRasterPulse/README.md) · [Kiswahili](../../sw/NVRasterPulse/README.md) · [Svenska](../../sv/NVRasterPulse/README.md) · [தமிழ்](../../ta/NVRasterPulse/README.md) · [ไทย](../../th/NVRasterPulse/README.md) · [Türkçe](../../tr/NVRasterPulse/README.md) · [Українська](../../uk/NVRasterPulse/README.md) · [اردو](../../ur/NVRasterPulse/README.md) · [Tiếng Việt](../../vi/NVRasterPulse/README.md)

[Translation policy](../../README.md)

</details>
<!-- nv-language-navigation:end -->

<!-- nv-translation-notice:start -->
> Strojově podporovaný překlad z angličtiny. Technické názvy, příkazy, URL a původní právní texty jsou zachovány. Recenze rodilým mluvčím je vítána; Pokud je znění nejasné, nahlédněte do anglického odkazu.
<!-- nv-translation-notice:end -->

<a id="nvrasterpulse"></a>
# NVRasterPulse

**Omezení FPS pro jednotlivé aplikace až po RivaTuner Statistics Server.**

> **Nejprve nainstalujte RTSS.** NVRasterPulse vyžaduje [RivaTuner Statistics Server (RTSS), staženo z Guru3D](https://www.guru3d.com/download/rtss-rivatuner-statistics-server-download/). Aby bylo možné vynutit omezení, musí být spuštěn RTSS. Není přibalen žádný instalační program RTSS, hook DLL nebo SDK.

[Stáhněte si 0.2 a stav](../docs/downloads.md#nvrasterpulse) · [Instalace](#installation) · [Jak fungují limity](#usage) · [Licence](../../../../NVRasterPulse/LICENSE)

<a id="overview-and-purpose"></a>
## Přehled a účel

NVRasterPulse je kompaktní rozhraní Windows pro správu limitů rámců RTSS podle názvu spustitelného souboru. RTSS provádí omezení. NVRasterPulse spravuje odpovídající hodnoty profilu, zálohování a požadavky na opětovné načtení, s přístupem do zásobníku a trvalými volbami.

Existuje proto, aby bylo snazší upravovat přesné limity pro jednotlivé hry, aniž by bylo nutné nahrazovat celý profil RTSS nebo narušovat jeho nastavení překrytí. Verze **0.2** přidává diagnostiku konfigurace, pomocníka FPS, pozastavení, vrácení zpět a sdílení profilu.

<a id="features"></a>
## Vlastnosti

- Vyberte spuštěnou aplikaci nebo přidejte její spustitelný soubor ručně.
- Uložte limity FPS od 1 do 1000 s až třemi desetinnými místy.
- Přesné racionální kódování zadaných hodnot: 59.94 se stane 2997/50.
- Konfigurace Front Edge Sync (`SyncLimiter=1`) s aktivním čekáním (`PassiveWait=0`).
- Aktualizace profilu podle spustitelnosti, automatické zálohování a atomické zápisy.
- Odstranění přepisů omezovače při zachování ostatního obsahu profilu.
- Detekce instalace RTSS, ruční výběr cesty a explicitní spuštění/znovu načtení.
- Operace zásobníku s jednou instancí, volitelné instalované spuštění, 34 jazyků a čtyři motivy.
- Samostatné akce normálního ukončení a **Konec + RTSS**.

<a id="compatibility"></a>
## Kompatibilita

| Požadavek | Podrobnosti |
| --- | --- |
| Systém | Windows 10/11 x64 |
| Doba běhu | [.NET Framework 4.8](https://dotnet.microsoft.com/en-us/download/dotnet-framework/net48), v případě potřeby instalován samostatně |
| Požadovaný software | RTSS s `RTSS.exe`, odpovídající adresář `Profiles` a kompatibilní profil/podpora opětovného načtení |
| GPU | Kompatibilita RTSS určuje omezovač; tento správce profilů nevyžaduje konkrétní generaci RTX |
| Oprávnění | Aktuální aplikace vyžaduje přístup správce; vybraná složka profilu RTSS musí být přístupná |
| Hry | Závisí na podpoře hákování RTSS a omezeních jednotlivých her; žádná záruka proti podvádění |

Pro každou funkci nebyla tímto auditem hubu certifikována žádná konkrétní minimální verze RTSS. Použijte oficiální aktuální distribuci a nahlaste přesnou verzi, pokud klíč profilu / opětovné načtení nefunguje. Nainstalovaný, ale zastavený RTSS projde kontrolou instalace; pro skutečné omezení se pak musí spustit.

<a id="installation"></a>
## Instalace

1. **[Stáhněte a nainstalujte RTSS z Guru3D](https://www.guru3d.com/download/rtss-rivatuner-statistics-server-download/).**
2. Otevřete [NVRasterPulse ke stažení](../docs/downloads.md#nvrasterpulse) a zkontrolujte dostupnost vydání.
3. Stáhněte si `NVRasterPulse-0.2-win-x64-Setup.exe` nebo `NVRasterPulse-0.2-win-x64-portable.zip` plus upozornění/kontrolní součty.
4. Porovnejte SHA-256. Spusťte instalaci nebo extrahujte celý přenosný ZIP do zapisovatelné místní složky.
5. Otevřete `NVRasterPulse.exe`. Pokud RTSS chybí, použijte **Stáhnout RTSS**, nainstalujte jej a poté **Zkontrolujte znovu** nebo vyberte `RTSS.exe` ručně.
6. Spusťte RTSS pomocí jeho normální zkratky nebo pomocí tlačítka RTSS NVRasterPulse, pokud je zastaven.

Vypnutím volitelného připomenutí se nepřeskočí kontrola předpokladů. Tiché spuštění zásobníku Windows počká, dokud se neotevře hlavní okno, než se zobrazí tato kontrola. Instalační program nainstaluje pouze NVRasterPulse. Jeho EXE jsou nepodepsané.

<a id="usage"></a>
## Využití

1. Vyberte zamýšlenou spuštěnou aplikaci nebo přejděte na její hru EXE.
2. Zadejte limit mezi 1 a 1000 FPS, v případě potřeby včetně zlomkové hodnoty.
3. Uložte a zkontrolujte nahlášený výsledek. NVRasterPulse aktualizuje profil RTSS tohoto spustitelného souboru a požaduje opětovné načtení.
4. Potvrďte, že RTSS běží, a ověřte chování v zamýšlené hře.

Profily jsou klíčovány **názvem spustitelného souboru**, například `Game.exe.cfg`. Dvě různé složky obsahující `Game.exe` sdílejí stejný profil RTSS; uložení celé cesty tuto kolizi neodstraní.

Ukládání využívá Front Edge Sync a aktivní čekání. Aktivní čekání může zvýšit využití CPU. Alternativní pole `LimitTime` jsou neutralizována. Stávající komentáře, nastavení překrytí a `EnableHooking=0` jsou zachovány. Globální profil RTSS se nezmění.

Použijte akci koše k odstranění přepisů omezovače NVRasterPulse. Neodstraní celý profil RTSS. Limit zděděný z RTSS Global nebo jiného nástroje může platit i poté.

**Zavření a ukončení:** hlavní okno se může skrýt do zásobníku. Normální **Ukončit** ponechá RTSS spuštěný a uložené limity nedotčené. **Quit + RTSS** požaduje normální uzavření odpovídajícího procesu RTSS v aktuální relaci, počká až osm sekund a nevynucuje ho. Uložené limity zůstávají v obou případech zachovány.

Jazyk a motiv se volí v aplikaci. Spuštění při přihlášení Windows je volitelné a je určeno pro nainstalovanou kopii. Informační tlačítko vysvětluje běžné akce.

<a id="diagnostics-and-profile-tools"></a>
## Diagnostické a profilové nástroje

Otevřete nabídku akcí pro další nástroje. Zachovávají RTSS Global, nastavení překrytí a výjimky.

**Diagnostika:** kontrola místních/efektivních limitů, zastavený RTSS, chybějící spustitelný soubor, žádné zjištěné okno, zakázáno hákování, dědičnost, pozastavené limity, konkurenční nastavení a duplicitní názvy spustitelných souborů. Tato kontrola pouze pro čtení popisuje konfiguraci; nedokazuje to, že je hra napojena na RTSS nebo neměří její FPS.

**Pomocník FPS:** vyberte zobrazení a sami deklarujte VRR/G-Sync, V-Sync, Reflex a Frame Generation. Zaoblená obnovovací frekvence pochází z Windows. Pokud je Reflex nebo Frame Generation aktivní nebo neznámý, nenabízí se žádné automatické omezení. Pro VRR se zapnutým V-Sync a vypnutým Reflex/FG heuristika odečte alespoň 3 FPS nebo přibližně 2 % obnovovací frekvence. To není měřené optimum. Použitím návrhu se návrh vyplní; **Uložit** zůstává samostatnou akcí.

**Pozastavit a obnovit:** pozastavit omezení vybraného programu a poté obnovit jeho předchozí pole omezovače. Konfliktní změny jiným nástrojem zabraňují nejednoznačnému životopisu. Skrytím záznamu se nepozastaví jeho horní hranice.

**Undo:** obnoví poslední změnu v šesti polích spravovaného omezovače pro daný program. Existuje jedna úroveň; toto neobnoví celý RTSS. Konfliktní vnější změny jsou odmítnuty. Zálohy souborů zůstávají oddělené.

**Sdílet profily:** exportovat vybrané profily do souboru `.nvrp`. Import zobrazí náhled a ve výchozím nastavení ponechá existující velká písmena nezaškrtnutá. Soubor obsahuje pouze názvy spustitelných souborů, limity a stavy, bez absolutních cest nebo skriptů. Zkontrolujte svůj výběr a přihlaste se. Chyba I/O může zanechat některé profily již aplikované; výsledek je identifikuje a každý si ponechá svůj zpět. Identické názvy spustitelných souborů stále adresují stejný profil RTSS.

**Oblíbené a skryté položky:** nejprve připněte užitečné programy, skryjte nechtěné položky a obnovte je ve vyhrazeném dialogu. Tyto volby přetrvávají. Uzavřená oblíbená položka se nezobrazí jako spuštěná aplikace.

<a id="screenshots"></a>
## Snímky obrazovky

![Náhled hlavního okna NVRasterPulse](../../../../assets/screenshots/nvrasterpulse-0.1-preview.png)

Stávající francouzské vykreslení uživatelského rozhraní 0.1 s ukázkovými názvy spustitelných souborů a hodnotou 176 FPS. RTSS je zobrazen jako zastavený; toto je ilustrace rozhraní, nikoli omezovač běhu nebo měření latence. [Image provenience](../assets/README.md).

<a id="update-and-uninstall"></a>
## Aktualizujte a odinstalujte

Ukončete NVRasterPulse, stáhněte a ověřte novou verzi, poté spusťte její instalaci nebo extrahujte přenosný počítač do nové složky. Zachovat nastavení a zálohy RTSS. Aktualizace RTSS jsou samostatné a pocházejí od Guru3D.

Chcete-li odebrat nainstalovanou kopii, použijte Windows **Installed apps**. U přenosných ukončete a poté odstraňte extrahovanou složku, až budou vaše zálohy bezpečné. Uložené limity RTSS nejsou odstraněny odinstalováním NVRasterPulse: nejprve odstraňte zamýšlené přepsání omezovače. RTSS má svůj vlastní odinstalační program.

Místní stav: `%LOCALAPPDATA%\NVRasterPulse`. Automatické zálohy RTSS: `%LOCALAPPDATA%\NVRasterPulse\Backups\RTSS`. Pro migraci lze přečíst starší umístění `%LOCALAPPDATA%\RTSSProfileBridge`. Tyto soubory mohou obsahovat osobní cesty ke spustitelným souborům a neměly by být zveřejňovány.

<a id="known-limitations"></a>
## Známá omezení

- RTSS provádí omezení. Uložená hodnota nebo úspěšný požadavek na opětovné načtení není výsledkem naměřeného rámce.
- Spustitelné soubory se stejným názvem sdílejí profil.
- Výsledek může ovlivnit jiný globální/herní omezovač; zakázání místního přepsání neodstraní zděděné omezení.
- Záměrně deaktivovaný háček RTSS zůstává deaktivován.
- Aktivní čekání má kompromis CPU/výkon.
- Žádná univerzální hra, anti-cheat nebo end-to-end ověřování latence.
- Dřívější experimentální motor s nezávislým omezovačem není sestavován ani dodáván.
- Automatické zálohování neznamená rozhraní pro úplnou obnovu zálohy na jedno kliknutí.

<a id="troubleshooting"></a>
## Odstraňování problémů

| Symptom | Akce |
| --- | --- |
| Předpoklad RTSS zůstává otevřený | Vyberte aktuální `RTSS.exe` a odpovídající složku Profiles a poté znovu zkontrolujte. |
| Limit uložen, ale žádný efekt | Spusťte RTSS; ověřte správný EXE/profil hry, oprávnění háku a další omezovače. |
| Uložení se nezdařilo | Zkontrolujte oprávnění složky a zachovejte zobrazenou chybu/zálohu. |
| Limit zůstává po odstranění | Zkontrolujte RTSS Global a další nástroje; akce koše odstraní pouze lokální přepisy omezovače. |
| Dvě hry mají stejný limit | Zkontrolujte, zda jsou názvy jejich spustitelných souborů identické. |
| Ukončit + RTSS ponechá RTSS otevřený | Zavřete RTSS normálně sami; tento příkaz se záměrně vyhýbá nucenému ukončení. |

Pokud ručně obnovujete zálohu RTSS, nejprve zavřete RTSS a zachovejte aktuální profil, než jej nahradíte zamýšlenou zálohou. To může přepsat nesouvisející úpravy profilu; zkontrolovat soubor a datum. [Sdílená podpora](../docs/support.md).

<a id="faq"></a>
## FAQ

**Potřebuji také MSI Afterburner?** NVRasterPulse vyžaduje RTSS; nezávisí na aplikaci Afterburner. Postupujte podle instalačních možností distributora RTSS.

**Mohu to použít bez spuštěného RTSS?** Jakmile je detekována instalace, můžete spravovat profily, ale kvůli omezení musí běžet RTSS.

**Odstraní ukončení nebo odinstalování krytky?** Ne. Před odstraněním NVRasterPulse explicitně odstraňte požadované přepsání omezovače.

**Je to fork nebo RTSS?** Ne. Je to nezávislý správce profilů; není začleněn žádný zdroj nebo spustitelný soubor RTSS.

<a id="upstream-modifications-and-credits"></a>
## Upstream, úpravy a kredity

Vývojové úložiště pochází z [Orbmu2k's NVIDIA Profile Inspector](https://github.com/Orbmu2k/nvidiaProfileInspector). Jeho MIT palety / prostředky uživatelského rozhraní jsou připsány. Služby správy profilů, kódování zlomků, zálohy, můstek opětovného načtení RTSS, chování zásobníku, průvodce předpoklady, jazyky a ikona specifická pro aplikaci byly vyvinuty/přizpůsobeny 禅堂 Zendo (RevoluSound Team).

RTSS je vyvinut společností **Unwinder** a distribuován samostatně prostřednictvím Guru3D. NVRasterPulse volá `UpdateProfiles` z vybrané nainstalované knihovny DLL; není redistribuován žádný RTSS SDK nebo hook binární. Instalační program používá neupravený Inno Setup 7.1.0 s upravenými skripty/překlady a bootstrap projektu.

[Plná provenience](../docs/provenance.md) · [Tabulka třetí strany](../THIRD_PARTY_NOTICES.md)

<a id="license"></a>
## Licence

Balíček výslovně distribuuje NVRasterPulse pod dodaným [Licence MIT](../../../../NVRasterPulse/LICENSE), přičemž si zachovává Copyright (c) 2016 Orbmu2k. Zdroj aplikace je udržován soukromě; MIT nevyžaduje zveřejnění upraveného zdroje. RTSS a Windows/.NET zůstávají pod svými vlastními podmínkami. [Úplné oznámení](LICENSES/README.md).

Nezávislé na NVIDIA Corporation, MSI a RTSS; jimi nesponzorované ani oficiálně nepodporované. Názvy produktů zůstávají ochrannými známkami jejich vlastníků.
