<!-- nv-language-navigation:start -->
🌐 [English](../../../../NVRasterPulse/README.md) | [Français](../../../../NVRasterPulse/README.fr.md) · [NV Laboratory](../README.md)

<details>
<summary>🌐 Language · 34</summary>

[العربية](../../ar/NVRasterPulse/README.md) · [বাংলা](../../bn/NVRasterPulse/README.md) · [简体中文](../../zh/NVRasterPulse/README.md) · [Čeština](../../cs/NVRasterPulse/README.md) · [Dansk](../../da/NVRasterPulse/README.md) · [Nederlands](../../nl/NVRasterPulse/README.md) · [English](../../../../NVRasterPulse/README.md) · [Filipino](../../fil/NVRasterPulse/README.md) · [Suomi](../../fi/NVRasterPulse/README.md) · [Français](../../../../NVRasterPulse/README.fr.md) · [Deutsch](../../de/NVRasterPulse/README.md) · [Ελληνικά](../../el/NVRasterPulse/README.md) · [हिन्दी](../../hi/NVRasterPulse/README.md) · **Magyar** · [Bahasa Indonesia](../../id/NVRasterPulse/README.md) · [Italiano](../../it/NVRasterPulse/README.md) · [日本語](../../ja/NVRasterPulse/README.md) · [한국어](../../ko/NVRasterPulse/README.md) · [मराठी](../../mr/NVRasterPulse/README.md) · [فارسی](../../fa/NVRasterPulse/README.md) · [Polski](../../pl/NVRasterPulse/README.md) · [Português](../../pt/NVRasterPulse/README.md) · [ਪੰਜਾਬੀ](../../pa/NVRasterPulse/README.md) · [Română](../../ro/NVRasterPulse/README.md) · [Русский](../../ru/NVRasterPulse/README.md) · [Español](../../es/NVRasterPulse/README.md) · [Kiswahili](../../sw/NVRasterPulse/README.md) · [Svenska](../../sv/NVRasterPulse/README.md) · [தமிழ்](../../ta/NVRasterPulse/README.md) · [ไทย](../../th/NVRasterPulse/README.md) · [Türkçe](../../tr/NVRasterPulse/README.md) · [Українська](../../uk/NVRasterPulse/README.md) · [اردو](../../ur/NVRasterPulse/README.md) · [Tiếng Việt](../../vi/NVRasterPulse/README.md)

[Translation policy](../../README.md)

</details>
<!-- nv-language-navigation:end -->

<!-- nv-translation-notice:start -->
> Gépi fordítás angolból. A műszaki nevek, parancsok, URL-ek és az eredeti jogi szövegek megmaradnak. Szívesen fogadjuk az anyanyelvű véleményt; olvassa el az angol hivatkozást, ha a megfogalmazás nem egyértelmű.
<!-- nv-translation-notice:end -->

<a id="nvrasterpulse"></a>
# NVRasterPulse

**Alkalmazásonkénti FPS korlátok az RivaTuner Statistics Server-ig.**

> **Először telepítse az RTSS fájlt.** Az NVRasterPulse használatához [RivaTuner Statistics Server (RTSS), letöltve a Guru3D-ről](https://www.guru3d.com/download/rtss-rivatuner-statistics-server-download/) szükséges. Az RTSS-nek futnia kell a korlátok érvényesítéséhez. Nincs csomagban RTSS telepítő, hook DLL vagy SDK.

[Az 0.1 letöltése és állapota](../docs/downloads.md#nvrasterpulse) · [Telepítés](#installation) · [Hogyan működnek a korlátok](#usage) · [Licenc](../../../../NVRasterPulse/LICENSE)

<a id="overview-and-purpose"></a>
## Áttekintés és cél

Az NVRasterPulse egy kompakt Windows interfész az RTSS keretkorlátok futtatható név alapján történő kezelésére. Az RTSS végrehajtja a korlátozást. Az NVRasterPulse kezeli a megfelelő profilértékeket, biztonsági mentéseket és újratöltési kéréseket, tálca-hozzáféréssel és állandó választási lehetőségekkel.

Létezik, hogy megkönnyítse a játékonkénti korlátok pontos szerkesztését anélkül, hogy egy teljes RTSS profilt le kellene cserélni, vagy megzavarná a fedvénybeállításait. A jelenlegi **0.1** jelölt a 2026. szeptember 9-i build, amelyhez szükséges az RTSS telepítési ellenőrzés.

<a id="features"></a>
## Jellemzők

- Válasszon ki egy futó alkalmazást, vagy adja hozzá manuálisan a végrehajtható fájlját.
- Mentse el az FPS korlátait 1 és 1000 között, legfeljebb három tizedesjegyig.
- A beírt értékek pontos racionális kódolása: 59.94 2997/50 lesz.
- Front Edge Sync konfiguráció (`SyncLimiter=1`) aktív várakozással (`PassiveWait=0`).
- Futtatható profilfrissítések, automatikus biztonsági mentések és atomi írások.
- A korlátozó felülírások eltávolítása a profil egyéb tartalmainak megőrzése mellett.
- RTSS telepítés észlelése, manuális elérési út kiválasztása és kifejezett indítás/újratöltés.
- Egypéldányos tálcás működés, opcionális telepített indítás, 34 nyelv és négy téma.
- Különítse el a normál kilépést és a **Kilépés + RTSS** műveleteket.

<a id="compatibility"></a>
## Kompatibilitás

| Követelmény | Részletek |
| --- | --- |
| Rendszer | Windows 10/11 x64 |
| Futásidő | [.NET-keretrendszer 4.8](https://dotnet.microsoft.com/en-us/download/dotnet-framework/net48), szükség esetén külön telepítve |
| Szükséges szoftver | RTSS `RTSS.exe`-szel, egy megfelelő `Profiles` könyvtárral és kompatibilis profil/újratöltés támogatással |
| GPU | Az RTSS kompatibilitás határozza meg a limitert; ez a profilkezelő nem igényel konkrét RTX generációt |
| Engedélyek | Az aktuális alkalmazás rendszergazdai hozzáférést kér; a kiválasztott RTSS profilmappának elérhetőnek kell lennie |
| Játékok | Az RTSS hooking támogatásától és az egyes játékok korlátozásaitól függ; nincs csalás elleni garancia |

Ez a hub-audit egyetlen RTSS minimális verziót sem tanúsított minden funkcióhoz. Használja a hivatalos aktuális disztribúciót, és jelentse a pontos verziót, ha a profilkulcs/újratöltés nem működik. A telepített, de leállított RTSS megfelel a telepítési ellenőrzésen; ezután el kell indítani a tényleges korlátozáshoz.

<a id="installation"></a>
## Telepítés

1. **[Töltse le és telepítse az RTSS-et a Guru3D-ről](https://www.guru3d.com/download/rtss-rivatuner-statistics-server-download/).**
2. Nyissa meg az [NVRasterPulse letöltések](../docs/downloads.md#nvrasterpulse) fájlt, és ellenőrizze a kiadás elérhetőségét.
3. Töltse le az `NVRasterPulse-0.1-win-x64-Setup.exe` vagy `NVRasterPulse-0.1-win-x64-portable.zip` fájlt, valamint a figyelmeztetéseket/ellenőrző összegeket.
4. Hasonlítsa össze: SHA-256. Futtassa a telepítőt, vagy bontsa ki a teljes hordozható ZIP-fájlt egy írható helyi mappába.
5. Nyissa meg az `NVRasterPulse.exe` fájlt. Ha az RTSS hiányzik, használja a **Töltse le az RTSS** fájlt, telepítse, majd **Ellenőrizze újra**, vagy válassza ki manuálisan az `RTSS.exe` lehetőséget.
6. Indítsa el az RTSS programot a normál parancsikonjával vagy az NVRasterPulse RTSS gombjával, ha le van állítva.

Az opcionális emlékeztető kikapcsolása nem hagyja ki az előfeltételek ellenőrzését. Az Windows tálca csendes indítása megvárja, amíg megnyílik a főablak, mielőtt megjeleníti ezt az ellenőrzést. A telepítés csak az NVRasterPulse fájlt telepíti. Az EXE-i aláíratlanok.

<a id="usage"></a>
## Használat

1. Válassza ki a kívánt futó alkalmazást, vagy tallózzon a játék EXE-jéhez.
2. Adjon meg egy korlátot 1 és 1000 FPS között, beleértve a töredékértéket is, ha szükséges.
3. Mentse el és ellenőrizze a jelentett eredményt. Az NVRasterPulse frissíti a végrehajtható fájl RTSS profilját, és újratöltést kér.
4. Győződjön meg arról, hogy az RTSS fut, és ellenőrizze a kívánt játék viselkedését.

A profilok **futtatható névvel** vannak kulcsolva, például `Game.exe.cfg`. Az `Game.exe` fájlt tartalmazó két különböző mappa ugyanazt az RTSS profilt használja; a teljes útvonal tárolása nem távolítja el ezt az ütközést.

A mentés a Front Edge Sync és az aktív várakozás használatával történik. Az aktív várakozás növelheti az CPU használatát. Az alternatív `LimitTime` mezők semlegesítve vannak. A meglévő megjegyzések, fedvénybeállítások és az `EnableHooking=0` megmarad. Az RTSS globális profil nem módosul.

A kuka művelettel távolítsa el az NVRasterPulse korlátozó-felülírásait. Nem törli a teljes RTSS profilt. Az RTSS Globaltól vagy más eszköztől örökölt korlát ezután is érvényben lehet.

**Bezárás és kilépés:** a főablak elrejthető a tálcán. Normál **Kilépés** esetén az RTSS fut, és a mentett korlátok érintetlenül maradnak. A **Kilépés + RTSS** a megfelelő RTSS folyamat normál bezárását kéri az aktuális munkamenetben, legfeljebb nyolc másodpercig vár, és nem kényszeríti ki. A tárolt határértékek mindkét esetben megmaradnak.

A nyelv és a téma az alkalmazásban van kiválasztva. Az Windows bejelentkezéskor történő indítás nem kötelező, és telepített példányhoz készült. Az információs gomb a gyakori műveleteket ismerteti.

<a id="screenshots"></a>
## Képernyőképek

![NVRasterPulse főablak előnézete](../../../../assets/screenshots/nvrasterpulse-0.1-preview.png)

Meglévő francia 0.1 felhasználói felület renderelés példa végrehajtható nevekkel és 176 FPS értékkel. Az RTSS leállt állapotban látható; ez egy interfész illusztráció, nem egy futáskorlátozó vagy késleltetésmérés. [A kép származása](../assets/README.md).

<a id="update-and-uninstall"></a>
## Frissítés és eltávolítás

Lépjen ki az NVRasterPulse alkalmazásból, töltse le és ellenőrizze az új verziót, majd futtassa a telepítőt, vagy bontsa ki a hordozható eszközt egy új mappába. A beállítások és az RTSS biztonsági másolatok megőrzése. Az RTSS frissítései különállóak, és a Guru3D-től származnak.

A telepített példány eltávolításához használja az Windows **Installed apps** fájlt. Hordozható esetén lépjen ki, majd távolítsa el a kibontott mappát, amikor a biztonsági másolatok biztonságban vannak. A mentett RTSS korlátokat nem távolítja el az NVRasterPulse eltávolítása: először távolítsa el a tervezett korlátozó-felülírásokat. Az RTSS saját eltávolítóval rendelkezik.

Helyi állapot: `%LOCALAPPDATA%\NVRasterPulse`. Automatikus RTSS biztonsági mentések: `%LOCALAPPDATA%\NVRasterPulse\Backups\RTSS`. Egy régebbi `%LOCALAPPDATA%\RTSSProfileBridge` hely beolvasható az áttelepítéshez. Ezek a fájlok tartalmazhatnak személyes végrehajtható elérési utat, és nem szabad nyilvánosan közzétenni.

<a id="known-limitations"></a>
## Ismert korlátozások

- Az RTSS végrehajtja a sapkát. A mentett érték vagy a sikeres újratöltési kérelem nem mért képkockaidő-eredmény.
- Az azonos nevű végrehajtható fájlok egy profilon osztoznak.
- Egy másik globális/játékonkénti korlátozó befolyásolhatja az eredményt; a helyi felülírás letiltása nem távolítja el az örökölt korlátot.
- A szándékosan letiltott RTSS horog letiltva marad.
- Az aktív várakozásnak CPU/teljesítmény kompromisszuma van.
- Nincs univerzális játék, csalás elleni vagy végpontok közötti késleltetési ellenőrzés.
- A korábbi kísérleti független limiter motort nem állítják össze és nem szállítják.
- Az automatikus biztonsági mentések nem jelentenek egy kattintással teljes biztonsági mentés-visszaállítás felületet.

<a id="troubleshooting"></a>
## Hibaelhárítás

| Tünet | Akció |
| --- | --- |
| Az RTSS előfeltétele nyitva marad | Válassza ki a tényleges `RTSS.exe` és a megfelelő Profiles mappát, majd ellenőrizze újra. |
| Limit mentve, de nincs hatása | Indítsa el az RTSS; ellenőrizze a megfelelő játék EXE/profilját, a horog jogosultságokat és egyéb korlátozókat. |
| A mentés sikertelen | Ellenőrizze a mappa engedélyeit, és őrizze meg a megjelenített hibát/biztonsági másolatot. |
| A határ az eltávolítás után is megmarad | Vizsgálja meg az RTSS globális és egyéb eszközöket; a kuka művelet csak a helyi korlátozó felülírásait távolítja el. |
| Két játék ugyanazt a limitet kapja | Ellenőrizze, hogy a futtatható fájlneveik megegyeznek-e. |
| Kilépés + RTSS az RTSS nyitva marad | Zárja be a szokásos módon az RTSS-et; ez a parancs szándékosan elkerüli a kényszerített befejezést. |

Ha manuálisan állít vissza egy RTSS biztonsági másolatot, először zárja be az RTSS fájlt, és őrizze meg az aktuális profilt, mielőtt lecserélné a kívánt biztonsági másolatra. Ez felülírhatja a nem kapcsolódó profilszerkesztéseket; nézze meg a fájlt és a dátumot. [Megosztott támogatás](../docs/support.md).

<a id="faq"></a>
## GYIK

**Szükségem van az MSI Afterburner-re is?** Az NVRasterPulse-hez RTSS szükséges; nem függ az Afterburner alkalmazástól. Kövesse az RTSS forgalmazó telepítési lehetőségeit.

**Használhatom ezt az RTSS futtatása nélkül?** A profilokat a telepítés észlelése után kezelheti, de az RTSS-nek futnia kell a korlátozáshoz.

**A kilépés vagy az eltávolítás eltávolítja a kupakokat?** Nem. Az NVRasterPulse eltávolítása előtt távolítsa el a kívánt korlátozó felülírásokat.

**Ez egy fork/RTSS?** Nem. Ez egy független profilkezelő; nincs RTSS forrás vagy végrehajtható fájl.

<a id="upstream-modifications-and-credits"></a>
## Upstream, módosítások és kreditek

A fejlesztési adattár az [Orbmu2k's NVIDIA Profile Inspector](https://github.com/Orbmu2k/nvidiaProfileInspector)-től származik. MIT palettáit/UI erőforrásait jóváírják. A profilkezelési szolgáltatásokat, a töredékkódolást, a biztonsági mentéseket, az RTSS újratöltési hidat, a tálca viselkedését, az előfeltételek útmutatóját, a nyelveket és az alkalmazás-specifikus ikont az 禅堂 Zendo (RevoluSound Team) fejlesztette/adaptálta.

Az RTSS-et az **Unwinder** fejlesztette ki, és külön terjeszti a Guru3D-n keresztül. Az NVRasterPulse meghívja az `UpdateProfiles` fájlt a kiválasztott telepített hook DLL-ből; nincs RTSS SDK vagy hook bináris újraelosztása. A telepítő módosítatlan Inno Setup 7.1.0 fájlt használ adaptált szkriptekkel/fordításokkal és egy projekt indító rendszerbetöltővel.

[Teljes eredet](../docs/provenance.md) · [Harmadik fél asztala](../THIRD_PARTY_NOTICES.md)

<a id="license"></a>
## Licenc

A csomag kifejezetten terjeszti az NVRasterPulse fájlt a mellékelt [MIT licenc](../../../../NVRasterPulse/LICENSE) alatt, megtartva a (c) 2016 Orbmu2k szerzői jogot. Az alkalmazás forrását privát módon kezelik; Az MIT nem igényli a módosított forrás közzétételét. Az RTSS és az Windows/.NET saját feltételei maradnak. [Teljes közlemények](LICENSES/README.md).

NVIDIA Corporation, MSI és RTSS független; általuk nem szponzorált vagy hivatalosan jóváhagyott. A terméknevek tulajdonosaik védjegyei maradnak.
