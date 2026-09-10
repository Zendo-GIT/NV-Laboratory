<!-- nv-language-navigation:start -->
🌐 [English](../../../../NVMFG-Unlock40/README.md) | [Français](../../../../NVMFG-Unlock40/README.fr.md) · [NV Laboratory](../README.md)

<details>
<summary>🌐 Language · 34</summary>

[العربية](../../ar/NVMFG-Unlock40/README.md) · [বাংলা](../../bn/NVMFG-Unlock40/README.md) · [简体中文](../../zh/NVMFG-Unlock40/README.md) · [Čeština](../../cs/NVMFG-Unlock40/README.md) · [Dansk](../../da/NVMFG-Unlock40/README.md) · [Nederlands](../../nl/NVMFG-Unlock40/README.md) · [English](../../../../NVMFG-Unlock40/README.md) · [Filipino](../../fil/NVMFG-Unlock40/README.md) · [Suomi](../../fi/NVMFG-Unlock40/README.md) · [Français](../../../../NVMFG-Unlock40/README.fr.md) · [Deutsch](../../de/NVMFG-Unlock40/README.md) · [Ελληνικά](../../el/NVMFG-Unlock40/README.md) · [हिन्दी](../../hi/NVMFG-Unlock40/README.md) · **Magyar** · [Bahasa Indonesia](../../id/NVMFG-Unlock40/README.md) · [Italiano](../../it/NVMFG-Unlock40/README.md) · [日本語](../../ja/NVMFG-Unlock40/README.md) · [한국어](../../ko/NVMFG-Unlock40/README.md) · [मराठी](../../mr/NVMFG-Unlock40/README.md) · [فارسی](../../fa/NVMFG-Unlock40/README.md) · [Polski](../../pl/NVMFG-Unlock40/README.md) · [Português](../../pt/NVMFG-Unlock40/README.md) · [ਪੰਜਾਬੀ](../../pa/NVMFG-Unlock40/README.md) · [Română](../../ro/NVMFG-Unlock40/README.md) · [Русский](../../ru/NVMFG-Unlock40/README.md) · [Español](../../es/NVMFG-Unlock40/README.md) · [Kiswahili](../../sw/NVMFG-Unlock40/README.md) · [Svenska](../../sv/NVMFG-Unlock40/README.md) · [தமிழ்](../../ta/NVMFG-Unlock40/README.md) · [ไทย](../../th/NVMFG-Unlock40/README.md) · [Türkçe](../../tr/NVMFG-Unlock40/README.md) · [Українська](../../uk/NVMFG-Unlock40/README.md) · [اردو](../../ur/NVMFG-Unlock40/README.md) · [Tiếng Việt](../../vi/NVMFG-Unlock40/README.md)

[Translation policy](../../README.md)

</details>
<!-- nv-language-navigation:end -->

<!-- nv-translation-notice:start -->
> Gépi fordítás angolból. A műszaki nevek, parancsok, URL-ek és az eredeti jogi szövegek megmaradnak. Szívesen fogadjuk az anyanyelvű véleményt; olvassa el az angol hivatkozást, ha a megfogalmazás nem egyértelmű.
<!-- nv-translation-notice:end -->

<a id="nvmfg-unlock40"></a>
# NVMFG Unlock40

**Kísérleti NVIDIA Multi Frame Generation GeForce RTX 40-hez, központi vezérlővel és játékonkénti választási lehetőséggel.**

[Az 0.1.1 letöltése és állapota](../docs/downloads.md#nvmfg-unlock40) · [Telepítés](#installation) · [Upstream](#upstream-and-modifications) · [Licencek](LICENSES/README.md)

<a id="overview-and-purpose"></a>
## Áttekintés és cél

Az NVMFG Unlock40 az 禅堂 Zendo (RevoluSound Team) által önállóan fejlesztett alkalmazás. Egyesíti az Windows vezérlőt, a natív réteget, a profilsegítőt és a játék/Streamline SDK kezelést. Olyan játékokat céloz meg, amelyek már integrálják az NVIDIA DLSS Frame Generation és a kompatibilis NVIDIA futtatókörnyezeteket.

Az [RTX40MFG-Unlock](https://github.com/dashdogy/RTX40MFG-Unlock) konzultált a munka összehasonlítása és finomítása érdekében. Az aktuális natív réteg megosztott és adaptált összetevőket tartalmaz, amelyeket alább külön-külön írunk le. Ez a hivatkozás nem teszi a teljes NVMFG-alkalmazást az adott projekt fork változatává.

Létezik a kísérleti MFG viselkedésének központi koordinálására, a játékspecifikus választások emlékezésére, valamint a futásidejű frissítések és biztonsági másolatok láthatóságának megőrzésére. Nem ad hozzá minden játékhoz az DLSS Frame Generation kódot, és nem alakít át tetszőleges FSR implementációt.

Az előkészített jelölt **0.1.1**, beleértve az SDK-listás vizuális korrekciót, amely belsőleg UI2 néven van rögzítve. A nyilvános verzió 0.1.1 marad; pontos kivonatai megkülönböztetik ezt a jelöltet a régebbi helyi buildektől.

<a id="features"></a>
## Jellemzők

- Központi engedélyezési/letiltási vezérlés és opcionális Windows tálcaindítás.
- Játékonkénti választás az Dynamic MFG, a játék beállításai és a támogatott fix szorzók között.
- Külön megjegyzett választási lehetőségek a megfigyelt V-Sync be/ki állapotokhoz.
- Az Dynamic az NVIDIA módot használja; fel van függesztve, ha az V-Sync ki van kapcsolva, külön játékon belüli/fix választással.
- Útmutatás a játékmenühöz és tartós kizárások; Az DLSS FG nélküli játékok továbbra is kézben maradnak.
- Játékfelderítés, szülőmappa kiválasztása, keresés, csoportosítás és eltávolítás játékfájlok törlése nélkül.
- Streamline SDK letöltés/importálás, ellenőrzött helyi gyorsítótár, explicit kijelölés, játékonkénti biztonsági mentés és visszaállítás.
- Natív szolgáltató ellenőrzése, munkamenetenkénti diagnosztika, globális profilnapló és konfliktus-tudatos helyreállítás.
- 34 felületi nyelv és négy téma.

Az FG kikapcsolása a játékban kikapcsolja. A 2x és 6x közötti fix választás a játéktól/menütől/futási időtől függ; nem azt ígérik, hogy minden kombináció működik. A vezérlő figyeli az V-Sync paramétert, és nem állítja be az V-Sync vagy VRR értéket a felhasználó számára.

<a id="compatibility"></a>
## Kompatibilitás

| Követelmény | Részletek |
| --- | --- |
| Rendszer | Windows 10/11 x64 |
| GPU | GeForce RTX 40 cél; nincs univerzális GPU kompatibilitási igény |
| Játék | Meglévő NVIDIA DLSS Frame Generation integráció és támogatott futási környezet; nincs csalás elleni kompatibilitási tanúsítvány |
| Szolgáltató | A jelölt az SHA-256 szolgáltatóhoz van rögzítve, az [eredetét](../docs/provenance.md) dokumentumban dokumentálva; az ismeretlen hash-ek elutasítva |
| Futásidő | Csomagolt .NET 8/WPF 8.0.30 alkalmazáshoz/ügynökhöz; .NET-keretrendszer 4.8 profilsegédeknek |
| Engedélyek | Rendszergazdai hozzáférés a vezérlő/profil műveletekhez |
| Hálózat | Szükséges a kiválasztott hivatalos SDK letöltésekhez; Az importált kompatibilis SDKs helyben gyorsítótárazható |
| Külső binárisok | Az NVIDIA illesztőprogram, az NGX szolgáltató/modellek és az Streamline játék futtatókörnyezetei nincsenek csomagban |

A verziócímke önmagában nem elegendő: az illesztőprogram, a szolgáltató hash, a játékintegráció és a ténylegesen betöltött modulok számítanak. A védett vagy nem kompatibilis folyamatok megtagadhatják a csatolást. Az alkalmazást nem arra tervezték, hogy elkerülje a csalás elleni védelmet.

<a id="installation"></a>
## Telepítés

1. Olvassa el az [jelölt státusz és engedélyezési megjegyzés](../docs/downloads.md#nvmfg-unlock40) dokumentumot.
2. Töltse le az `NVMFGUnlock40-0.1.1-Setup-x64.exe` vagy `NVMFGUnlock40-0.1.1-Portable-x64.zip` fájlt, ha kiadása elérhető.
3. Ellenőrizze az SHA-256-et, és őrizze meg a kísérő megjegyzéseket. Telepítse a .NET Framework 4.8 fájlt, ha az Windows még nem biztosítja.
4. Futtassa a telepítőt, vagy bontsa ki a **teljes** hordozható ZIP-fájlt egy írható helyi mappába.
5. Indítsa el az `NVMFGUnlock40.exe`; tartsa meg az `agent`, `driver`, `engine` és `Licenses` fájlokat a mellékelt elrendezésben.

Az `driver` nevű mappa felhasználói terület-segítőket tartalmaz, nem kernel-illesztőprogramot. Ne másolja csak a fő EXE-t, és ne cserélje le a szolgáltatói hash-t a kompatibilitás kényszerítéséhez. A jelenlegi EXE-k aláíratlanok.

<a id="usage"></a>
## Használat

1. Kezdje a vezérlő letiltásával. Adjon hozzá egy játékot vagy egy szülőmappát, és válassza ki a tényleges telepítéseket.
2. Tekintse át az egyes játékok MFG beállításait. Válaszoljon arra, hogy mit kínál a menüje; a válasz játékonként tárolódik.
3. Válassza az Dynamic vagy a játékon belüli beállítást globálisan, majd módosítsa a megfelelő játékonkénti lehetőségeket szükség szerint.
4. Csak akkor engedélyezze a vezérlőt, ha használni kívánja. Ideiglenesen hat globális NVIDIA profilbeállítást módosíthat egy helyreállítási naplóval.
5. Indítson el egy alkalmas játékot, és engedélyezze a saját DLSS Frame Generation-et. Kövesse az V-Sync-off választási kéréseket.
6. Használjon kizárásokat azoknál a játékoknál, amelyeket nem szeretne kezelni. Egy játék eltávolítása rögzíti a kizárást, és megőrzi a fájljait/biztonsági másolatait.
7. Ha végzett, használja az alkalmazás teljes kilépési/letiltási és helyreállítási folyamatát.

A főablak bezárásával a vezérlő a tálcán maradhat. A játékba már betöltött DLL a játék kilépéséig ott marad; a vezérlő letiltása nem jelent garanciát a kirakodásra. Zárja be az érintett játékokat karbantartás vagy frissítés előtt.

**Streamline SDKs:** az NVIDIA SDK oldalon töltsön le egy hivatalos verziót, vagy importáljon egy kompatibilis helyi SDK-et. Az import egy ellenőrzött másolatot tárol; **Use this version** kiválasztja, az **Uninstall** pedig eltávolítja a gyorsítótárazott másolatot. A hiányzó Streamline DLL-ek kiegészíthetők egy hivatalos NVIDIA SDK-ből, a forrás feltüntetésével. Ez nem tölti le/cseréli az NGX modellt. Zárja be a játékot, válassza ki a kívánt játékfrissítést, és őrizze meg az eredeti biztonsági másolatot. A játékfájlok visszaállításához használja a biztonsági mentés visszaállítását, ne a gyorsítótár Uninstall gombját.

<a id="screenshots"></a>
## Képernyőképek

![NVMFG SDK-lista előnézet](../../../../assets/screenshots/nvmfg-0.1.1-sdk-preview.png)

Meglévő angol 0.1.1 interfész renderelés egy példa SDK leltárral. Ez nem egy aktuális verziólista vagy egy futó játék bizonyítéka. [A kép származása](../assets/README.md).

<a id="update-and-uninstall"></a>
## Frissítés és eltávolítás

Zárja be az érintett játékokat. A frissítés előtt tiltsa le/zárja ki az NVMFG-t, és oldja meg a függőben lévő NVIDIA beállítások helyreállítását. Telepítse a következő telepítőt a meglévő identitással, vagy bontsa ki az új hordozható eszközt egy új mappába; állapot/mentések megőrzése.

Az eltávolítás előtt állítsa vissza a kívánt játék SDK biztonsági másolatait és NVIDIA beállításait az alkalmazáson keresztül, majd zárja be a játékokat és lépjen ki a vezérlőből. Használja az Windows **Installed apps** fájlt a telepítéshez, vagy távolítsa el a zárt hordozható mappát a szükséges fájlok megőrzése után. Ne töröljön manuálisan egy aktív helyreállítási naplót a Telepítő blokkolásának feloldásához.

A helyi játék futásidejű biztonsági mentései az `%LOCALAPPDATA%\NvidiaStreamlineMaintenance\Backups` kódot használják. MFG beállítások/SDK adatok használata `%LOCALAPPDATA%\RtxMfg`; A munkamenet kimenete az `Sessions` alatt található az alkalmazás mellett. Ezek a fájlok játékútvonalakat tartalmazhatnak. Ne tegye közzé őket módosítatlanul.

<a id="known-limitations"></a>
## Ismert korlátozások

- A kísérleti natív javítások összeomlásokat vagy vizuális műtermékeket okozhatnak; egy megoldatlan Bodycam összeomlás szerepel a fejlesztési előzményekben.
- Az ellenőrzött renderelő tesztek nem minden játék, illesztőprogram vagy csalás elleni tanúsítvány.
- A generált keretek nem hoznak létre új bemeneti mintákat; ez a hub nem ígér mért késleltetést vagy teljesítménynövekedést.
- Több keretgeneráló eszköz/fedvény ütközhet egymással. Az alkalmazás minden együttélési forgatókönyv bizonyítása nélkül jelenti a megfigyelt modulokat.
- A kompatibilitási jegyzék egy észlelési segédlet, nem pedig a teljesen tesztelt játékok listája.
- A teljes NVIDIA SDK feltételek és a feloldatlan műszaki korlátozások az [eredetét](../docs/provenance.md) dokumentumban maradnak.

<a id="troubleshooting"></a>
## Hibaelhárítás

| Tünet | Akció |
| --- | --- |
| A szolgáltató nem támogatott | Őrizze meg az eredeti ellenőrzött fájlokat. Jelentse az illesztőprogram/szolgáltató verzióit és a hibát; ne kerülje ki a hash ellenőrzést. |
| Nincs DLSS FG a játékban | Válassza ki a választ, és hagyja a játék irányítását; ez az eszköz nem tudja elkészíteni ezt az integrációt. |
| A játék összeomlása/műtermékei | Lépjen ki a játékból, tiltsa le az NVMFG-t, használja a játék eredeti futásidejű biztonsági másolatát, ha megváltozott, és jelentse a reprodukálható részleteket. |
| Az SDK lista vagy letöltés nem érhető el | Frissítse és ellenőrizze a hivatalos forrást; a gyorsítótárazott/importált verziónak továbbra is át kell mennie az érvényesítésen. |
| A függőben lévő NVIDIA helyreállítás blokkolja a kilépést/frissítést | Használja a helyreállítást és őrizze meg a naplót; a konfliktusokat nem szabad vakon felülírni. |
| Az eltávolított játék nem kerül újra felfedezésre | Kizárása tartós. Adja hozzá kifejezetten, amikor újra kezelni szeretné. |

Az [Megosztott támogatási útmutató](../docs/support.md) elmagyarázza, mit kell tartalmaznia a jelentésben.

<a id="faq"></a>
## GYIK

**Tartalmaz NVIDIA DLL-eket vagy modelleket?** Nincs benne illesztőprogram, NGX szolgáltató/modell vagy Streamline futtatókörnyezet. Az explicit SDK letöltések az NVIDIA webhelyről származnak.

**Az Dynamic működik kikapcsolt V-Sync mellett?** Ebben az állapotban fel van függesztve. Válaszd ki a játékon belüli beállítást vagy egy alkalmas rögzített szorzót az adott játék külön állapotához.

**Ez egy ReShade/OptiScaler/FSR csomag?** Nem. Ezeket nem ennek az éles csomagnak a részeként fordítják vagy szállítják.

**Nyilvánosak a módosított források?** Nem. A lefordított csomagok és a szükséges kreditek/licencek rendelkezésre állnak. Ez nem szünteti meg harmadik felek jogait vagy korlátozásait.

<a id="upstream-and-modifications"></a>
## Upstream és módosítások

Összehasonlító referencia és megosztott natív összetevők: **RTX40MFG-Unlock, Michael Robles / dashdogy**, referencia véglegesítés `4e776d068f91b4a665425542bb005dd57cc3d891`, MIT. [Adattár](https://github.com/dashdogy/RTX40MFG-Unlock) · [Eredeti letöltések](https://github.com/dashdogy/RTX40MFG-Unlock/releases).

A forrás-összehasonlítás azonosítja a megosztott javításokat, a szolgáltató/házirend kezelését, az időbeli korrekciókat és az MinHook alapú kitérő összetevőket. Az MIT és BSD megjegyzéseiket megőrzik. A teljes összehasonlítás a termelési célon kívüli fájlokat is tartalmazza.

Az asztali alkalmazást, a vezérlőt és az SDK-kezelési munkafolyamatot az 禅堂 Zendo (RevoluSound Team) fejlesztette ki. A projektmunka magában foglalja a központi betöltést, az NGX bootstrap integrációt, az ellenőrzött szolgáltató kiválasztását, a játék/V-Sync koordinációt és a munkamenet-diagnosztikát. A származási útmutató elválasztja ezt a munkát a megosztott összetevőktől; a fájl-összehasonlítás önmagában nem határozza meg, hogy mikor volt az ötlet valamelyik szerzőnél.

A profilsegéd adaptálja az MIT NVAPI burkolóanyagot az Orbmu2k Profile Inspector-ből. [Részletes származás és az összetevők köre](../docs/provenance.md).

<a id="credits-and-license"></a>
## Kredit és licenc

Michael Robles; Orbmu2k; Tsuda Kageyu és HDE közreműködők; NVIDIA Corporation; Microsoft és közreműködők; Inno Setup szerzők és fordítók. Alkalmazásfejlesztés, integrációk és csomagolás: 禅堂 Zendo (RevoluSound Team).

Az [meglévő összeállított csomagmegosztási engedély](../../../../NVMFG-Unlock40/LICENSE) és az összes [komponens licencek](LICENSES/README.md) megmarad. Az upstream kód MIT engedélyei eltérnek az NVIDIA SDK feltételektől. Semmilyen általános engedély nem helyettesíti őket.

Független az NVIDIA Corporation-től, nem szponzorálja és hivatalosan nem hagyja jóvá. Minden hivatkozott védjegy a tulajdonosa tulajdona marad.
