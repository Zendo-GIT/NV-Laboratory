<!-- nv-language-navigation:start -->
🌐 [English](../../../provenance.md) | [Français](../../../provenance.fr.md) · [NV Laboratory](../README.md)

<details>
<summary>🌐 Language · 34</summary>

[العربية](../../ar/docs/provenance.md) · [বাংলা](../../bn/docs/provenance.md) · [简体中文](../../zh/docs/provenance.md) · [Čeština](../../cs/docs/provenance.md) · [Dansk](../../da/docs/provenance.md) · [Nederlands](../../nl/docs/provenance.md) · [English](../../../provenance.md) · [Filipino](../../fil/docs/provenance.md) · [Suomi](../../fi/docs/provenance.md) · [Français](../../../provenance.fr.md) · [Deutsch](../../de/docs/provenance.md) · [Ελληνικά](../../el/docs/provenance.md) · [हिन्दी](../../hi/docs/provenance.md) · **Magyar** · [Bahasa Indonesia](../../id/docs/provenance.md) · [Italiano](../../it/docs/provenance.md) · [日本語](../../ja/docs/provenance.md) · [한국어](../../ko/docs/provenance.md) · [मराठी](../../mr/docs/provenance.md) · [فارسی](../../fa/docs/provenance.md) · [Polski](../../pl/docs/provenance.md) · [Português](../../pt/docs/provenance.md) · [ਪੰਜਾਬੀ](../../pa/docs/provenance.md) · [Română](../../ro/docs/provenance.md) · [Русский](../../ru/docs/provenance.md) · [Español](../../es/docs/provenance.md) · [Kiswahili](../../sw/docs/provenance.md) · [Svenska](../../sv/docs/provenance.md) · [தமிழ்](../../ta/docs/provenance.md) · [ไทย](../../th/docs/provenance.md) · [Türkçe](../../tr/docs/provenance.md) · [Українська](../../uk/docs/provenance.md) · [اردو](../../ur/docs/provenance.md) · [Tiếng Việt](../../vi/docs/provenance.md)

[Translation policy](../../README.md)

</details>
<!-- nv-language-navigation:end -->

<!-- nv-translation-notice:start -->
> Gépi fordítás angolból. A műszaki nevek, parancsok, URL-ek és az eredeti jogi szövegek megmaradnak. Szívesen fogadjuk az anyanyelvű véleményt; olvassa el az angol hivatkozást, ha a megfogalmazás nem egyértelmű.
<!-- nv-translation-notice:end -->

<a id="provenance-changes-and-licensing"></a>
# Származási hely, változások és engedélyezés

Ez az ellenőrzés a **2026-09-18** napon elkészített jelölteket ismerteti. Az alkalmazásforrások privátak maradnak; a nyilvános leltárak fájlneveket és kivonatokat tartalmaznak, nem forráskódot. Lásd: [a teljes összetevőre vonatkozó megjegyzések](../THIRD_PARTY_NOTICES.md).

<a id="nvidia-profile-inspector--nv-tools-fork"></a>
## NVIDIA Profile Inspector – NV Tools Fork

Hivatkozás: Orbmu2k/nvidiaProfileInspector commit `592d962cca8827efe8859461a84267755595064a`; jelölt végrehajtható verzió 3.0.2.3. A referencia véglegesítés és az fork összeállítási verziója különböző azonosítók; az fork verzióból nem következik az upstream kiadású verzió.

A tiszta társ 157 forrás/erőforrás fájlját összehasonlították ezzel a véglegesítéssel: 2 bájt azonos, 134 csak sorvégződésben vagy UTF-8 BOM-ban különbözik, 11 módosított, 10 hiányzik az összehasonlított upstream útvonalon. A „hozzáadva” az adott útvonalhoz viszonyított, és önmagában nem az eredeti szerzőség bizonyítéka.

[Teljes fájl/hash összehasonlítás](../../../provenance/nvpi-source-provenance.json).

| Terület | Örökös munka | Fork hozzájárulás |
| --- | --- | --- |
| Profilszerkesztő | Profilmodell, import/export, alkalmazástársítások és referenciaadatok | Integráció a képernyővel és a külső eszközindítóval |
| NVAPI | Orbmu2k DRS interop | Színekkel/megjelenítéssel kapcsolatos interop, gyártási natív betöltési korlátozások és ál-eltávolítás |
| Megjelenítési szolgáltatások | Windows/NVIDIA API-k külső interfészként | DisplayInfoService, DisplayConfigurationService, DisplaySettingsBackend |
| UI | Upstream WPF erőforrások, paletták és ikonok | Képernyő párbeszédpanelek, 15 másodperces megerősítés, állapot/visszaolvasás és eszköztár elrendezés |
| Indító | Meglévő alkalmazáshéj | Védett, külön telepített RasterPulse keresés és indítás |
| Csomagolás | MIT felfelé | Tiszta különálló társ, külön telepítő/eltávolító, megőrzött megjegyzések |

A nyilvános forrástérkép megoldási/erőforrás-útvonalakat tartalmaz a nyomon követhetőség érdekében; ezeket a fájlokat nem terjesztik forrásként. A fejlesztési tesztek, az álinterfészek és a régi kombinált NVPI/RasterPulse bináris program nem szerepel.

<a id="nvdriverforge"></a>
## NVDriverForge

Független C#/.NET 8/WPF alkalmazás; a felhasználóbarát munkafolyamatot részben az NVCleanstall ihlette. Nem azonosított NVCleanstall forrás/bináris fájl a termelési hasznos adatban. Nem az adott védett alkalmazás fork-jeként szerepel.

Az eredeti projektmunka magában foglalja az összetevőelemzést/kiválasztást, a védett telepítési feladatokat, a biztonsági mentéseket és a tranzakciók helyreállítását, az NVIDIA katalógus letöltését, a frissítések ellenőrzését, a lokalizált magyarázatokat, az opcionális speciális/NVENC munkafolyamatokat és a telepítő rendszerindítását.

Öröklött/adaptált összetevők: négy NVPI témapaletta, kiterjesztett NVAPI DRS interfész hivatkozás és a külön választható MIT NVPI kiegészítő. Az Custom NV előre beállított kiválasztási felhasználói felülete és az engedélyezett tranzakció-integráció az NVDriverForge-hez tartozik; az előre beállított beállítás nem hivatalos NVIDIA ajánlás.

7-Zip 26.03, .NET/WPF Az 8.0.31 és Inno Setup változatlan külső összetevők maradnak, amelyeket saját feltételeik szerint használnak. keylase Az NVENC adatok nincsenek beágyazva; Egy pontos véglegesítés kerül kiválasztásra és ellenőrzésre, amikor a felhasználó kompatibilis letöltést kér. Nem jött létre újraelosztási engedély ezekhez az upstream adatokhoz.

<a id="nvmfg-unlock40"></a>
## NVMFG Unlock40

Az NVMFG Unlock40-et az 禅堂 Zendo (RevoluSound Team) függetlenül fejlesztette ki. A karbantartó az RTX40MFG-Unlock kódot használta összehasonlításra és finomításra. Az alkalmazás egésze nem fork néven jelenik meg. Ez a megkülönböztetés nem távolítja el a megosztott/adaptált összetevők jóváírásait az aktuális natív rétegben.

Összehasonlítási hivatkozás: dashdogy/RTX40MFG-Unlock, Michael Robles, MIT, véglegesítés `4e776d068f91b4a665425542bb005dd57cc3d891`. A privát natív motorfa 48 összehasonlított fájlt tartalmaz: 35 csak formázási eltérés, 4 módosított fájl és 9 hiányzik a hivatkozási útvonalon. [Teljes összehasonlítás](../../../provenance/nvmfg-source-provenance.json).

Módosított örökölt fájlok: `entry_detour.h`, `patcher.cpp`, `temporal_interval_trace.cpp`, `temporal_interval_trace.h`. További elérési utak közé tartozik az `game_selection.*`, `ngx_bootstrap.*`, `ngx_capability.h`, `presentation_tracker.h`, `vsync_observer.*` és a fenntartott upstream licenc.

Gyártási C++ egységek: patcher, midpoint_fix, dlssg_provider_policy, entry_detour, nvidia_mfg_policy, temporal_interval_trace, ngx_bootstrap, game_selection és vsync_observer; plusz entry_detour összeállítás és MinHook puffer/hook/trambulin/HDE64. Az örökölt ReShade előtér, az örökölt alátét-erőforrások és a fel nem használt CMake célok nem részei ennek az éles összeállításnak.

A megfelelő összetevők a javítási/szolgáltatói szabályzatot és az időbeli munkát fedik le; szerzői jogi és engedélyezési megjegyzéseik sértetlenek maradnak. A központi NGX/bootstrap/vezérlő koordináció, a játékonkénti V-Sync kezelés, a munkamenet-diagnosztika és az Windows alkalmazás/SDK/backup munkafolyamat az 禅堂 Zendo (RevoluSound Team) projektmunkája. A fenti számok a fájlokat írják le, beleértve a harmadik féltől származó és a fel nem használt fájlokat, nem pedig a szerzői százalékot vagy a projektötlet kronológiáját.

A segítő az NVPI NvapiDrsWrapper és NativeArrayHelper moduljait egy külön összeállításba adaptálja, projekt által létrehozott profillogikával. A régi fejlesztési álút kizárva. A megosztott családi paletták az NVPI-től származnak.

MinHook hivatkozás: `8fda4f5481fed5797dc2651cd91e238e9b3928c6`; az örökölt lefordított részhalmaznak nincs funkcionális lokális változása az összehasonlításban. Streamline integrációs fejlécek: 2.12; nyitott fejléc licence ellenőrizve a v2.12.0 címen. NGX fejléc forrása: NVIDIA/DLSS véglegesítés `a291cc7d2cc642a51566f3dfd5376f635cd1b284`.

SHA-256 jelölt motor: `C793770D329B99CD9C5C640317CE435BFE353CA2868E36CF5DCD4D5295EFAE13`.

Szükséges szolgáltató SHA-256 az engine.json-ben: `C64928FDB7C48A57722EA8EEF2662171EDC323473ADEA66C29A206A23F1A2BED`. A bejelentett 310.9 szolgáltatócsalád nem cserélhető fel ezzel a pontos hash-sel. Nem tartalmaz szolgáltatói DLL-t vagy modellt.

**Kiemelkedő engedélyezési pont:** a teljes NVIDIA RTX SDK licenc, 2024. március 14-i verzió, a műszaki korlátozások megkerülésére vonatkozó 4(d) szakasz korlátozást tartalmaz. Az audit nem ad engedélyt erre a felhasználásra. Az MIT motorlicenc megőrzése, az ingyenesség vagy más módosítások megfigyelése nem oldja meg ezt a külön feltételt. A jelöltek felkészítése nem jogorvoslat. Az eredeti rövid fejléc közlemény kiegészül a teljes licenccel; Windows-1252 szövege is olvasható UTF-8 formátumban van megadva, az eredeti bájtokkal.

A natív összehasonlítást újraszámították az 0.2.3 esetében: ugyanaz a 48 fájl és besorolás. Az előző audit óta az `game_selection.cpp`, `game_selection.h` és `patcher.cpp` módosult a tevékenység/képesség megfigyelésekhez. Az új könyvtári, diagnosztikai, preferenciális, frissítési és kiválasztási munkafolyamatok a karbantartó alkalmazáshoz tartoznak. A komponenslicencek és a szükséges szolgáltatói hash változatlanok.

<a id="nvrasterpulse"></a>
## NVRasterPulse

Független RTSS profilkezelő, amelyet az NVPI-ből származó tárolóban fejlesztettek ki. Az örökölt MIT UI erőforrások/paletták és a projekt eredete jóváírás marad. Az éles alkalmazás kifejezetten a mellékelt MIT licencet használja.

Projektmunka: precíz RTSS profilelemzés/írás és töredékes kódolás, biztonsági mentések, felülírások eltávolítása, újratöltési híd, előfeltételek észlelése, kompakt felhasználói felület, tálca életciklusa, indítási vezérlők és lokalizáció. Az RTSS tényleges korlátozást hajt végre.

Nincs RTSS forrás, hook DLL, SDK vagy telepítő. A híd egy meglévő, felhasználó által kiválasztott RTSS telepítésben hívja meg az exportálást. Ebben a csomagban nincs NVIDIA illesztőprogram-csomag, natív kísérleti korlátozó, Framepacer, MinHook, ReShade vagy DLSS futtatókörnyezet.

<a id="assets-generated-data-and-tools"></a>
## Eszközök, generált adatok és eszközök

Az [Eszközjóváírások](../assets/README.md) azonosítja a meglévő interfész előnézeteket és az NVPI beállításválasztót. A bennük lévő kitalált értékek fel vannak címkézve. Nincs játék/Nexus elem, személyes profil, privát ICC, vállalati NVIDIA logó vagy betűtípusfájl másolása.

Az NVMFG-ben örökölt generált játékkompatibilitási nevek az észlelést segítik, nem pedig teszt bizonyítékok. A generált telepítői katalógusok jóváírása az [fordító észreveszi](../../../../licenses/INSTALLER-TRANSLATORS.md). Az abszolút elérési úttal generált build rekordok privátak maradnak.

A privát összeállítási eszközök közé tartozik a .NET SDK/MSBuild, Visual Studio C++/MASM, Windows SDK, PowerShell, Inno Setup és Python audit scripts. Fordítóik, fejléceik, tesztfuttatóik és hibakeresési eszközeik nincsenek terjesztve. A statikus kioldású CRT továbbra is az Microsoft vonatkozó eszközlánc feltételei alatt marad.

<a id="scope-of-verification"></a>
## Az ellenőrzés hatálya

A helyi ellenőrzés a három fejlesztési gyökérben lévő összes fájlt leltározta, miközben kizárta a Git-objektum-adatbázisokat és a kapcsolódó címtárcélokat. Az aktív forrás/dokumentumok ellenőrzése megtörtént; a történelmi építményeket leltározták és kizárták. A kiválasztott ZIP-eket és az aktuális rakományokat megvizsgálták és kivonatozták; a .NET-csomagokat további ellenőrzés céljából kicsomagoltuk. A kezdeti ellenőrzés nem futtatott terméket, telepítőt, játékot, RTSS folyamatot vagy illesztőprogramot.

A későbbi NVPI telepítési verzió 2 javítja az önálló nyelvválasztást a megosztott Inno vezérlők és rendszerindító segítségével. A világos/sötét privát lámpatestek ellenőrizték az egér és a billentyűzet navigációját, valamint mind a 34 kifejezett nyelvi kódot. A tényleges beállításválasztót egy soha meg nem jelenített privát asztalon nyitották meg, és a telepítés előtt törölték. Hét alkalmazásfájlja és hordozható ZIP-fájlja változatlan. NVDriverForge Az 0.1.3 tartalmazza a javított kísérőt, és továbbra is továbbítja az `/LANG` fájlt.

NVDriverForge Az 0.1.3 2026-09-10-én készült el. A privát hitelesítési jelentés 366 alkalmazástesztet, 118 kísérőellenőrzést, 32 beállítási ellenőrzést, 156 natív összehasonlítást és 34 nyelvi továbbítási esetet rögzít. A védett komponens-kiválasztási javítást egy eredeti illesztőprogram-csomaggal újra lejátszották anélkül, hogy megváltoztatták volna a hasznos terhelést vagy telepítették volna az illesztőprogramot. Ezek a termékcsapat által keltezett eredmények, nem a jelen dokumentációfrissítés által újrafutott tesztek vagy a sikeres, valódi illesztőprogram-telepítés bizonyítéka.

Ez a hub-frissítés semmilyen funkcionális alkalmazáskódot nem módosít. A korábbi alkalmazások build/unit/UI tesztjei elavult történelmi bizonyítékok maradnak. Ez nem minden harmadik féltől származó bináris program teljes visszafejtése vagy garancia minden lehetséges titkos mintára.

2026. szeptember 18-i frissítés: NVDriverForge Az 0.1.4 kiegészíti a készenléti ellenőrzéseket, a natív profil biztonsági mentését, az összetevők útmutatásait, a beállításokat és a készleteket, a részletes eredményeket, a helyi jelentéseket és az alkalmazásfrissítéseket. NVRasterPulse Az 0.2 konfigurációs diagnosztikát, FPS útmutatást, szüneteltetést/folytatást, visszavonást, `.nvrp` profilokat és kedvenceket/elrejtést ad hozzá, új korlátozó motor nélkül. Az egyéni útmutatók leírják a felhasználást és a korlátokat. A statikus hub-ellenőrzések elkülönülnek a szeptember 18-i magánjelentésekben rögzített alkalmazástesztektől; ehhez a hubhoz nem történt illesztőprogram telepítése, valós profilimportálás vagy várakozási idő mérése.
