<!-- nv-language-navigation:start -->
🌐 [English](../../../../NVDriverForge/README.md) | [Français](../../../../NVDriverForge/README.fr.md) · [NV Laboratory](../README.md)

<details>
<summary>🌐 Language · 34</summary>

[العربية](../../ar/NVDriverForge/README.md) · [বাংলা](../../bn/NVDriverForge/README.md) · [简体中文](../../zh/NVDriverForge/README.md) · [Čeština](../../cs/NVDriverForge/README.md) · [Dansk](../../da/NVDriverForge/README.md) · [Nederlands](../../nl/NVDriverForge/README.md) · [English](../../../../NVDriverForge/README.md) · [Filipino](../../fil/NVDriverForge/README.md) · [Suomi](../../fi/NVDriverForge/README.md) · [Français](../../../../NVDriverForge/README.fr.md) · [Deutsch](../../de/NVDriverForge/README.md) · [Ελληνικά](../../el/NVDriverForge/README.md) · [हिन्दी](../../hi/NVDriverForge/README.md) · **Magyar** · [Bahasa Indonesia](../../id/NVDriverForge/README.md) · [Italiano](../../it/NVDriverForge/README.md) · [日本語](../../ja/NVDriverForge/README.md) · [한국어](../../ko/NVDriverForge/README.md) · [मराठी](../../mr/NVDriverForge/README.md) · [فارسی](../../fa/NVDriverForge/README.md) · [Polski](../../pl/NVDriverForge/README.md) · [Português](../../pt/NVDriverForge/README.md) · [ਪੰਜਾਬੀ](../../pa/NVDriverForge/README.md) · [Română](../../ro/NVDriverForge/README.md) · [Русский](../../ru/NVDriverForge/README.md) · [Español](../../es/NVDriverForge/README.md) · [Kiswahili](../../sw/NVDriverForge/README.md) · [Svenska](../../sv/NVDriverForge/README.md) · [தமிழ்](../../ta/NVDriverForge/README.md) · [ไทย](../../th/NVDriverForge/README.md) · [Türkçe](../../tr/NVDriverForge/README.md) · [Українська](../../uk/NVDriverForge/README.md) · [اردو](../../ur/NVDriverForge/README.md) · [Tiếng Việt](../../vi/NVDriverForge/README.md)

[Translation policy](../../README.md)

</details>
<!-- nv-language-navigation:end -->

<!-- nv-translation-notice:start -->
> Gépi fordítás angolból. A műszaki nevek, parancsok, URL-ek és az eredeti jogi szövegek megmaradnak. Szívesen fogadjuk az anyanyelvű véleményt; olvassa el az angol hivatkozást, ha a megfogalmazás nem egyértelmű.
<!-- nv-translation-notice:end -->

<a id="nvdriverforge"></a>
# NVDriverForge

**Készítsen elő egy NVIDIA illesztőprogram-telepítést egyértelmű komponensválasztással és opcionális beállításokkal.**

[Az 0.1.4 letöltése és állapota](../docs/downloads.md#nvdriverforge) · [Telepítés](#installation) · [Kredit](#credits-and-upstream) · [Licenc](../../../../NVDriverForge/LICENSE)

<a id="overview-and-purpose"></a>
## Áttekintés és cél

Az NVDriverForge végigvezeti Önt egy eredeti NVIDIA illesztőprogram-csomagon: válassza ki az illesztőprogramot, ellenőrizze az összetevőit, tekintse át az opcionális módosításokat, majd erősítse meg a telepítést. Azért létezik, hogy érthetővé tegye ezeket a döntéseket, és együtt tartsa a telepítést, a kiemelt műveleteket és a helyreállítási információkat.

Ez egy független fejlesztésű alkalmazás, amelyet részben az NVCleanstall munkafolyamata inspirált. Nem tartalmazza az NVCleanstall kódot, és nem igényel teljes szolgáltatásparitást.

<a id="features"></a>
## Jellemzők

- NVIDIA Game Ready / Studio keresés és letöltések; opcionális gyorsjavítás-felderítés kézi tartalékkal.
- Az eredeti csomag, kivonatok, NVIDIA aláírások, jegyzékek és kompatibilis INF bejegyzések elemzése.
- Alkotóelemek kiválasztása függőséggel és ismeretlen komponensek megőrzésével.
- Az 0.1.4 verzió a kiválasztott opcionális NVIDIA összetevőket átugorhatóan tartja, és csak az ellenőrzött, ellenőrizetlen összetevőket zárja ki a felderítésből. A már aktuális vagy nem alkalmazható opcionális futási környezetek már nem kényszerülnek kritikus összetevőként.
- Tiszta telepítési hibaösszegzések és hozzáférés a részletes naplókhoz mind a 34 nyelven.
- Készenléti ellenőrzések, kifejezett megerősítés, exportálás az illesztőprogram-tárból és a natív NVIDIA profil biztonsági mentése a telepítés előtt.
- Opcionális speciális beállítások, repülés előtti ellenőrzésekkel, naplókkal és konfliktus-tudatos helyreállítással.
- Opcionális **Custom NV** előre beállított névvel ellátott választási lehetőségek és magyarázatok, beleértve a különálló SILK erősségválasztást és a kompatibilitási ellenőrzéseket.
- Opcionális pontos verziójú NVENC javítás letöltések; a forrás véglegesítés és a cél bájtok ellenőrzése megtörténik.
- Az Profile Inspector fork különálló, opcionális telepítése az Eszközök képernyőről.
- Összetevők útmutatója, újrafelhasználható beállítások, illesztőprogram-készletek, helyi támogatási jelentések és opcionális alkalmazásfrissítések.
- 34 felületi nyelv és négy téma.

Az elérhető speciális opciók az MPO, az DLSS jelző, az Ansel, az NVIDIA audio-alvó állapot, az MSI, a megszakítási házirend/prioritás, az HDCP, a kijelző-tároló indítása és a jogosult örökölt telemetriai szolgáltatás közé tartoznak. Mindegyiknek megvannak a maga előfeltételei és hatásai; ezek nem univerzális teljesítményjavítások.

<a id="compatibility"></a>
## Kompatibilitás

| Követelmény | Részletek |
| --- | --- |
| Rendszer | Windows 10 build 19041 vagy újabb / Windows 11, x64 |
| GPU/illesztőprogram | Kompatibilis NVIDIA csomag és észlelt hardver; Az automatikus katalóguskeresés elsősorban az ismert GeForce modelleket fedi le |
| Futásidő | .NET 8 / WPF 8.0.31 az előkészített önálló csomagban |
| Kiváltságok | Normál felhasználói felület/felhasználónkénti beállítás; az illesztőprogram telepítése és a rendszermódosítások rendszergazdai hozzáférést kérnek |
| Hálózat | Szükséges az online NVIDIA kereséshez/letöltésekhez és az explicit upstream NVENC kérésekhez; helyi eredeti illesztőprogram választható |
| Tartalmazott eszközök | Módosítatlan 7-Zip 26.03, futásidejű értesítések, opcionális MIT Profile Inspector kísérő |
| Választható társ | .NET Framework 4.8 a különálló Profile Inspector fork |

Nincs tetszőleges minimális illesztőprogram-verzió, amely lefedi az összes funkciót. A Multi-GPU keresésnek meg kell felelnie minden észlelt GPU-nek. A nem támogatott/professzionális modellekhez kézi illesztőprogram-választás szükséges. Az NVIDIA telepítője marad a végső hardver/OS jogosultság.

<a id="installation"></a>
## Telepítés

1. Látogasson el az [letöltések](../docs/downloads.md#nvdriverforge) oldalra, és ellenőrizze, hogy a kiadás megjelent.
2. Válassza az `NVDriverForge-Setup.exe`-et a telepítéshez, vagy az `NVDriverForge.exe`-et hordozható használatra.
3. Hasonlítsa össze az SHA-256-et a kiadás `SHA256SUMS.txt`-ével.
4. Futtassa a telepítőt felhasználónkénti telepítéshez és szabványos eltávolítóhoz, vagy helyezze a hordozható EXE-t egy írható mappába, és nyissa meg.

A hordozható eszköz tartalmazza a futási időt és az opcionális telepítőt. Az NVDriverForge telepítése nem telepíti az GPU illesztőprogramot. EXE-jei jelenleg aláíratlanok.

<a id="usage"></a>
## Használat

1. **Illesztőprogram:** Töltse le az NVIDIA webhelyről, vagy válasszon egy eredeti NVIDIA telepítő EXE-t. Legyen vége az elemzésnek.
2. **Alkatrészek:** tekintse át a leírásokat és a szükséges függőségeket. Az ismeretlen komponensek megmaradnak.
3. **Csípítések:** a nem kívánt opciókat változatlanul hagyja. Mielőtt bármit választana, olvassa el az effektusokat és a kompromisszumokat.
4. **Áttekintés:** ellenőrizze a pontos illesztőprogramot, összetevőket és opcionális műveleteket, majd erősítse meg a telepítést.
5. Csak az Ön által választott művelethez fogadja el az UAC-et. Tartsa meg a védett munka helyreállítási utasításait.
6. Ha az új illesztőprogramot újra kell indítani, kövesse a jelentett állapotot. A késleltetett műveletekhez kifejezett folytatás szükséges az újraindítás után.

Az Custom NV változatlan formában indul. Válasszon egyedi elnevezett értékeket, vagy tekintse át a mellékelt előre beállított értéket és annak kizárásait. Két információs belső mezője nincs önállóan írva. A beállítások csak az ellenőrzött új illesztőprogram-munkafolyamatban kerülnek alkalmazásra, előnézet megnyitásával soha. A különálló NVPI szerkesztő telepítése nem szükséges.

Az opcionális NVENC munka letölti a kompatibilis adatokat egy rögzített keylase véglegesítésből. Megváltoztat két illesztőprogram-DLL-t, és érvényteleníti az aláírásaikat; megtagadhatja az Windows, a kódolók, az DRM vagy az anti-cheat. Nincsenek ilyen adatok, vagy az NVIDIA DLL nincs beágyazva az NVDriverForge fájlba. [Származási és engedélyezési korlátok](../docs/provenance.md).

A beállítások szabályozzák a nyelvet, a témát és az opcionális telepített felhasználók frissítéseinek ellenőrzését. A hordozható eszköz nem hozza létre a telepített háttér-ellenőrzési feladatot. Az eszközök és a helyreállítás elkülönül a négy telepítési lépéstől.

<a id="backup-and-diagnostic-tools"></a>
## Biztonsági mentési és diagnosztikai eszközök

**Telepítés előtt:** A készenléti ellenőrzések kiterjednek a csomag aláírására, a GPU-kra, a becsült munkaterületre/biztonsági mentési területre, a függőben lévő újraindításra és a versengő telepítőkre. Az emelt munkás megismétli őket. A versengő folyamatok soha nem állnak le automatikusan. A natív NVIDIA profil-adatbázis biztonsági mentésnek sikeresnek kell lennie az NVIDIA telepítésének megkezdése előtt; A driver-store export egy külön biztonsági másolat.

**Újrafelhasználható lehetőségek:** az összetevők útmutatója négy kérdést tesz fel a játékokról, a hangról, az NVIDIA App-ről és a felvételről. Tekintse át javaslatait; szükséges, ismeretlen és függő összetevők védettek maradnak. Exportálja a beállításokat, majd importáláskor tekintse meg előnézetüket és érvényesítse újra a kiválasztott csomaggal szemben. A beleegyezések, az újraindítási műveletek, a program útvonalak és a javítócsomagok nem importálódnak.

**Illesztőprogram-készlet:** exportáljon egy `.nvdfkit.zip`-et, hogy az eredeti aláírt NVIDIA telepítő, a választási lehetőségek, a hash-ek és az utasítások együtt maradjanak. Az `NVDriverForge.exe`-et külön szállítsa. Importálja a készletet az Eszközökben, tekintse át az előnézetet, majd használja a normál telepítési munkafolyamatot. Ez nem egy vékony illesztőprogram vagy egy módosított önálló telepítő. Az opcionális NVENC-nek továbbra is le kell töltenie és beleegyeznie kell az adott illesztőprogramhoz. Az NVIDIA újraelosztási feltételei továbbra is érvényesek.

**Eredmények és támogatás:** Olvassa el a rövid eredményt, és bontsa ki a szakaszonkénti/opciónkénti részleteket. A sikeres visszaolvasás tárolt értéket hoz létre, nem pedig mért javulást. A helyi JSON támogatási jelentés az engedélyezési listán szereplő mezőket használja, beleértve az alkalmazás újraindítása utáni utolsó mentett feladatot. Mentés vagy megosztás előtt tekintse meg az előnézetet. Nem tartalmaz nyers naplókat, profiltartalmat vagy hardverazonosítókat, és soha nem töltődik fel automatikusan.

**Helyreállítás:** kövesse a védett feladatok útmutatóját a mentett illesztőprogram helyreállításához. Az explicit profil-visszaállításhoz az illesztőprogram eredeti verziója és ugyanazok a GPU-k szükségesek; lecseréli a teljes adatbázist, megőrzi az aktuális másolatot, és ellenőrzi a hash-eket és az ütköző állapotot. Ne törölje ki a naplóját, és ne erőltesse az eltérést. A valódi illesztőprogram-telepítés, a teljes helyreállítás és a natív profilimportálás ezzel az új munkafolyamattal érvényesítetlen marad egy valós rendszeren.

**Alkalmazásfrissítések:** olvassa el a kiadási megjegyzéseket, majd válasszon kifejezetten egy SHA-256 által ellenőrzött letöltést. Az ellenőrzés alapértelmezés szerint kézi, az indításkor opcionális ellenőrzéssel. Egyik telepítő sem indul el automatikusan. Ez a funkció elkülönül az illesztőprogram-frissítések ellenőrzésétől és a telepített kiadás opcionális illesztőprogram-ellenőrzési feladatától.

<a id="screenshots"></a>
## Képernyőképek

![NVDriverForge illesztőprogram-oldal előnézete](../../../../assets/screenshots/nvdriverforge-0.1.2-preview.png)

Meglévő 0.1.2 francia felhasználói felület renderelés példaadatokkal; interfész előnézetként megmaradt. A megjelenített 699.99 illesztőprogram egy tesztkészülék, nem egy valós letölthető verzió. [A kép származása](../assets/README.md).

<a id="update-and-uninstall"></a>
## Frissítés és eltávolítás

Zárja be az NVDriverForge-et, szerezze be a következő hivatalos csomagot, és ellenőrizze annak kivonatát. Használja ugyanazt a telepítőazonosítót a telepített frissítéshez; cserélje ki a zárt hordozható EXE-t egy újra. Őrizze meg a beállításokat és a védett feladatokat.

Uninstall innen: Windows **Installed apps**. Az alkalmazást és annak frissítési feladatát eltávolítja, nem az NVIDIA illesztőprogramot. A beállítások, naplók és biztonsági másolatok megmaradnak. Ha szükséges, állítsa vissza a speciális/NVENC módosításokat a dokumentált helyreállítási folyamaton keresztül **az alkalmazás eltávolítása előtt**. A Restore elutasítja a másik eszköz ütköző módosításait.

A helyi adatok `%LOCALAPPDATA%\NVDriverForge` alatt vannak; a védett munkák és az illesztőprogram-exportálások az `%PROGRAMDATA%\NVDriverForge\Jobs` alá tartoznak. A hordozható használat helyi adatokat is létrehoz. Az illesztőprogram-áruház exportálása és a natív profil biztonsági mentése különálló. Egyik rendszerkép sem.

<a id="known-limitations"></a>
## Ismert korlátozások

- Nincs hardver kiegészítés/INF szerkesztés, újragenerált NVIDIA aláírások, csalás elleni kompatibilis lemondás vagy automatikus aláírás nélküli figyelmeztetés elfogadása.
- Nincs teljes telemetria/hirdetés eltávolítás, vékony csomagexport vagy automatikus teljes visszaállítás az előző illesztőprogramhoz.
- Az illesztőprogram-telepítést, a rendszerindítási helyreállítást és az opcionális profilírásokat a hub-audit nem ellenőrizte teljes körűen valódi gépeken.
- A rendszerleíró adatbázis visszaolvasása nem a tényleges HDCP, a teljesítmény vagy a késleltetési hatások bizonyítéka.
- Az aláírás-ellenőrzések helyileg elérhető Windows megbízhatóságot használnak; online visszavonás nem történik.
- 34 nyelv van jelen, de a teljes anyanyelvi/kisegítő lehetőségek tesztelése továbbra is hiányos.

<a id="troubleshooting"></a>
## Hibaelhárítás

| Tünet | Akció |
| --- | --- |
| Az online katalógus nem elérhető | Válasszon egy eredeti csomagot az [NVIDIA illesztőprogram letöltések](https://www.nvidia.com/en-us/drivers/)-től. Ne cserélje ki a szomszédos GPU modellt. |
| A gyorsjavítások keresése nem érhető el | Használja az [Az NVIDIA Game Ready illesztőprogram-fóruma](https://www.nvidia.com/en-us/geforce/forums/game-ready-drivers/13/)-et, és ellenőrizze a tényleges csomagot. |
| Az NVIDIA telepítése sikertelen | Olvassa el a hibaösszefoglalót, és nyissa meg a részletes naplókat. A már aktuális vagy nem alkalmazható opcionális összetevők átugorhatók maradnak az 0.1.4-ben. A sikertelen telepítések nem váltanak ki opcionális módosításokat vagy sikeres/újraindítási folyamatot. |
| Aláírás/kivonat/biztonsági mentés hiba | Állítsa le a telepítést, és őrizze meg a hibát; szerezze be újra az eredeti csomagot, ha sérült. |
| Az opció nem elérhető | Olvassa el a hardver, alkatrész vagy a cél-illesztőprogram okát; változatlanul tartsa. |
| Újraindítás vagy a feladat még függőben | Használja a munka helyreállítási utasításait és kifejezett önéletrajzát; ne törölje ki a naplóját. |
| Konfliktus visszaállítása | Egy másik állapot eltér a rögzített tranzakciótól. Őrizze meg, és kérjen segítséget a visszaállítás kényszerítése helyett. |

A jelentések esetében tartalmazza a kiválasztott eszközverziót, Windows, GPU, illesztőprogramot és reprodukálható lépéseket; törölje az útvonalakat és a személyes adatokat a naplókból. [Támogatás](../docs/support.md).

<a id="faq"></a>
## GYIK

**A telepítő telepít grafikus illesztőprogramot?** Nem. Ehhez az alkalmazás külön elemzésére, áttekintésére, megerősítésére és magasabb szintű telepítési folyamatára van szükség.

**Szükségem van az NVCleanstall-re vagy az NVPI-re?** Nem. Az NVCleanstall csak inspiráció. Az Profile Inspector kiegészítő egy független opcionális szerkesztő.

**Minden NVIDIA illesztőprogramot kisebb vagy gyorsabbá tesz?** Nem. A kiválasztott összetevők és előfeltételek határozzák meg, hogy mi változhat; mért nyereséget nem ígérnek.

**Hol vannak a források?** Az alkalmazás-specifikus forrás- és magánteszteket külön karbantartják. Ez a központ a forrásmegjelöléshez/licenchez szükséges dokumentációt, bináris fájlokat és harmadik féltől származó forráshivatkozásokat biztosít.

<a id="credits-and-upstream"></a>
## Hitelek és upstream

Eredeti alkalmazás, munkafolyamat, tranzakciók, lokalizáció, bootstrap és adaptációk: 禅堂 Zendo (RevoluSound Team).

- [NVCleanstall / TechPowerUp](https://www.techpowerup.com/download/techpowerup-nvcleanstall/): munkafolyamat-inspiráció; nincs importált forrás vagy bináris fájl.
- [NVIDIA Profile Inspector / Orbmu2k](https://github.com/Orbmu2k/nvidiaProfileInspector): MIT témák, kiterjesztett NVAPI interfészreferencia és külön csomagolt fork.
- [7-Zip / Igor Pavlov](https://www.7-zip.org/): módosítatlan extrahálószerszámok.
- [Microsoft .NET](https://github.com/dotnet/runtime) és [WPF](https://github.com/dotnet/wpf): csomagban lévő futási idő.
- [Inno Setup](https://jrsoftware.org/isinfo.php): eredeti telepítőmotor és jóváírt fordítások.
- [keylase/nvidia-patch](https://github.com/keylase/nvidia-patch): külső opcionális NVENC adatforrás; újraelosztási engedély nem jött létre.
- [NVIDIA](https://www.nvidia.com/en-us/drivers/): külső illesztőprogramok letöltése és telepített NVAPI/NVML könyvtárak.

[Teljes komponens táblázat](../THIRD_PARTY_NOTICES.md) · [Változások és származás](../docs/provenance.md)

<a id="license"></a>
## Licenc

Az [Meglévő bináris terjesztési engedély](../../../../NVDriverForge/LICENSE) engedélyezi a módosítatlan hivatalos végrehajtható fájlok használatát és megosztását az értesítéseikkel együtt. Az alkalmazás-specifikus forrásjogok fenntartva. Nem korlátozza a különálló harmadik fél licencei által biztosított jogokat. [Teljes közlemények](LICENSES/README.md).

NVIDIA Corporation, TechPowerUp és keylase független; általuk nem szponzorált vagy hivatalosan jóváhagyott. A terméknevek tulajdonosaik védjegyei maradnak.
