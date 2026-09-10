<!-- nv-language-navigation:start -->
🌐 [English](../../../../NVIDIA-Profile-Inspector/README.md) | [Français](../../../../NVIDIA-Profile-Inspector/README.fr.md) · [NV Laboratory](../README.md)

<details>
<summary>🌐 Language · 34</summary>

[العربية](../../ar/NVIDIA-Profile-Inspector/README.md) · [বাংলা](../../bn/NVIDIA-Profile-Inspector/README.md) · [简体中文](../../zh/NVIDIA-Profile-Inspector/README.md) · [Čeština](../../cs/NVIDIA-Profile-Inspector/README.md) · [Dansk](../../da/NVIDIA-Profile-Inspector/README.md) · [Nederlands](../../nl/NVIDIA-Profile-Inspector/README.md) · [English](../../../../NVIDIA-Profile-Inspector/README.md) · [Filipino](../../fil/NVIDIA-Profile-Inspector/README.md) · [Suomi](../../fi/NVIDIA-Profile-Inspector/README.md) · [Français](../../../../NVIDIA-Profile-Inspector/README.fr.md) · [Deutsch](../../de/NVIDIA-Profile-Inspector/README.md) · [Ελληνικά](../../el/NVIDIA-Profile-Inspector/README.md) · [हिन्दी](../../hi/NVIDIA-Profile-Inspector/README.md) · **Magyar** · [Bahasa Indonesia](../../id/NVIDIA-Profile-Inspector/README.md) · [Italiano](../../it/NVIDIA-Profile-Inspector/README.md) · [日本語](../../ja/NVIDIA-Profile-Inspector/README.md) · [한국어](../../ko/NVIDIA-Profile-Inspector/README.md) · [मराठी](../../mr/NVIDIA-Profile-Inspector/README.md) · [فارسی](../../fa/NVIDIA-Profile-Inspector/README.md) · [Polski](../../pl/NVIDIA-Profile-Inspector/README.md) · [Português](../../pt/NVIDIA-Profile-Inspector/README.md) · [ਪੰਜਾਬੀ](../../pa/NVIDIA-Profile-Inspector/README.md) · [Română](../../ro/NVIDIA-Profile-Inspector/README.md) · [Русский](../../ru/NVIDIA-Profile-Inspector/README.md) · [Español](../../es/NVIDIA-Profile-Inspector/README.md) · [Kiswahili](../../sw/NVIDIA-Profile-Inspector/README.md) · [Svenska](../../sv/NVIDIA-Profile-Inspector/README.md) · [தமிழ்](../../ta/NVIDIA-Profile-Inspector/README.md) · [ไทย](../../th/NVIDIA-Profile-Inspector/README.md) · [Türkçe](../../tr/NVIDIA-Profile-Inspector/README.md) · [Українська](../../uk/NVIDIA-Profile-Inspector/README.md) · [اردو](../../ur/NVIDIA-Profile-Inspector/README.md) · [Tiếng Việt](../../vi/NVIDIA-Profile-Inspector/README.md)

[Translation policy](../../README.md)

</details>
<!-- nv-language-navigation:end -->

<!-- nv-translation-notice:start -->
> Gépi fordítás angolból. A műszaki nevek, parancsok, URL-ek és az eredeti jogi szövegek megmaradnak. Szívesen fogadjuk az anyanyelvű véleményt; olvassa el az angol hivatkozást, ha a megfogalmazás nem egyértelmű.
<!-- nv-translation-notice:end -->

<a id="nvidia-profile-inspector--nv-tools-fork"></a>
# NVIDIA Profile Inspector – NV Tools Fork

**Az [NVIDIA Profile Inspector – Orbmu2k](https://github.com/Orbmu2k/nvidiaProfileInspector) független fork, hozzáadott kijelzővezérlőkkel.** A projekt korábbi neve: **NVPI Custom**.

[Letöltés és kiadás állapota](../docs/downloads.md#nvidia-profile-inspector) · [Telepítés](#installation) · [Upstream és változások](#upstream-and-changes) · [Licenc](../../../../NVIDIA-Profile-Inspector/LICENSE)

<a id="overview"></a>
## Áttekintés

Az alkalmazás szerkeszti az NVIDIA illesztőprogram-profilokat, beleértve az alkalmazásonkénti beállításokat. Ez az fork egy **Képernyő** szerkesztőt is hozzáad az aktív Windows kijelzőhöz: felbontás, frissítési gyakoriság, kimeneti színbeállítások, HDR és telepített ICC/WCS profiltársítások.

Azért létezik, hogy a kapcsolódó megjelenítési vezérlőket bevigye a profilszerkesztőbe, és világosabbá tegye az előnézeti, megerősítési és visszaállítási eredményeket. Nem hoz létre új hardverképességeket.

Az első jelölt az **3.0.2.3**, amely a 2026. szeptember 9-től megtisztított, önálló társverziót használja. Meglévő végrehajtható fájlja továbbra is `nvidiaProfileInspector.exe`; a telepítőn és néhány belső címkén továbbra is az `NVPI Custom NV` szerepel. A fenti nyilvános cím azonosítja az fork-et anélkül, hogy megváltoztatná a telepítési identitást, vagy úgy tesz, mintha az Orbmu2k hivatalos kiadása lenne.

<a id="features"></a>
## Jellemzők

- Meglévő upstream profilböngészés, alkalmazástársítások, beállítások módosításai és profilimportálás/exportálás.
- **Képernyő** párbeszédpanel a megjelenítéshez, módhoz, Hz-hez, RGB/YCbCr, színmélységhez, tartományhoz és kolorimetriához.
- Windows HDR vezérlés és telepített ICC/WCS társítás kiválasztása.
- 15 másodperces megjelenítési előnézet a **Keep** / **Revert** funkcióval és az időtúllépési visszaállítással.
- A mód/HDR változások és a jelentett helyreállítási hibák visszaolvasása.
- Külön jelentése HDR, SDR ACM/WCG-vel és jelszínmélységgel.
- NVRasterPulse indítóprogram egy alkalmas, külön telepített példányhoz.

<a id="compatibility"></a>
## Kompatibilitás

| Követelmény | Részletek |
| --- | --- |
| Rendszer | Windows 10/11 x64 kompatibilis NVIDIA illesztőprogrammal |
| Futásidő | [.NET-keretrendszer 4.8](https://dotnet.microsoft.com/en-us/download/dotnet-framework/net48), az Windows szállítja vagy külön telepíti |
| Engedélyek | A szerkesztő megnyitásakor rendszergazdai hozzáférést kér |
| Megjeleníti | A tényleges módok és színkombinációk az GPU-től, az illesztőprogramtól, a kijelzőtől, a kábeltől és az Windows API-któl függenek |
| Választható eszközök | NVRasterPulse az RTSS limitkezeléshez; sem ez, sem RTSS nem szükséges a Képernyőszerkesztőhöz |
| Nyelvek | Beállítás: 34 nyelv választó. A szerkesztő megtartja meglévő nyelvi támogatását. |

Nincs ellenőrzött univerzális illesztőprogram-minimum vagy támogatási mátrix minden GPU-hez. A párbeszédpanelen elérhető bpc-lehetőségek kérések, nem pedig hitelesített kombinációk. A modern HDR vezérlők és a régebbi Windows tartalék különböző képességekkel rendelkeznek.

<a id="installation"></a>
## Telepítés

1. Nyissa meg az [letöltési oldal](../docs/downloads.md#nvidia-profile-inspector) fájlt, és ellenőrizze a közzététel állapotát.
2. Töltse le a telepítőt vagy a hordozható eszközt, és hasonlítsa össze az SHA-256-et a kiadási jegyzékkel.
3. A telepítéshez futtassa az `NVPI-CustomNV-3.0.2.3-Setup-r2.exe` programot, válasszon nyelvet, és kövesse a telepítőt. Saját parancsikont és eltávolítóprogramot hoz létre.
4. Hordozható esetén bontsa ki a teljes ZIP-fájlt egy új írható mappába. Tartsa meg az `Reference.xml` fájlt, az EXE konfigurációt és az összes megjegyzést a végrehajtható fájl mellett.
5. Indítsa el az `nvidiaProfileInspector.exe` programot.

A szerkesztő telepítése önmagában nem alkalmaz profilt, és nem telepít GPU illesztőprogramot. A kísérő külön telepíti, nem veszi át az `.nip` társításokat, és nem teszi lehetővé az indítást a bejelentkezéskor. A meglévő binárisok előjel nélküliek.

<a id="usage"></a>
## Használat

A **Telepítői verzió 2** ugyanazt a natív 34 nyelvű választót tartalmazza, mint a többi eszköz, egér/billentyűzet navigációval, világos/sötét megjelenéssel és törléssel. A választás a beállításra vonatkozik; nem fordítja le az NVPI szerkesztőt. Az explicit `/LANG=fr` argumentum vagy a néma mód megkerüli a nyelvet már biztosító hívók kiválasztását.

**Illesztőprogram-profilok:** válasszon profilt, exportáljon biztonsági másolatot, majd csak a kívánt beállításokat szerkessze és alkalmazza azokat. Az alkalmazástársítások határozzák meg, hogy melyik játék kap profilt. A tárolt érték nem bizonyítja, hogy minden illesztőprogram vagy játék használja.

**Kijelző vezérlői:** nyissa meg a **Képernyőt**, válassza ki a kijelzőt és a kívánt értékeket, majd indítsa el az előnézetet. Ellenőrizze a képet, mielőtt 15 másodpercen belül a **Megtart** lehetőséget választja. A visszaállítás kéréséhez használja a **Visszaállítás** gombot, zárja be a megerősítést, vagy hagyja, hogy lejárjon. Olvasson el minden hibaüzenetet: a sikeres API-hívás önmagában nem bizonyítéka a visszaállításnak.

Az ICC kijelölés megváltoztatja a telepített profiltársítást; nem hoz létre, nem kalibrál vagy terjeszt újra ICC fájlt. Az HDR, ACM/WCG, RGB/YCbCr és bpc a folyamat különböző aspektusait írják le. Nincs új független ACM kapcsoló.

**NVRasterPulse:** az eszköztár gombja egy külön regisztrált rendszerszintű telepítést fogad el a Program Files alatt védett tulajdonnal és engedélyekkel. Ez az emelt szintű indító elutasíthatja a hordozható másolatot vagy a felhasználó által írható/linkelt elérési utat. Ebben az esetben nyissa meg az NVRasterPulse fájlt a saját parancsikonjával. [Telepítse az RTSS-et külön](https://www.guru3d.com/download/rtss-rivatuner-statistics-server-download/) az NVRasterPulse használatához.

<a id="screenshots"></a>
## Képernyőképek

![NVPI beállítási változat 2 nyelvválasztó](../../../../assets/screenshots/nvpi-setup-r2-language.png)

A tényleges beállításválasztó francia nyelven, egy elszigetelt teszt során rögzített, majd törölve. Ez mutatja a telepítőt; a szerkesztő megtartja felületét és Képernyő párbeszédpanelét.

<a id="update-and-uninstall"></a>
## Frissítés és eltávolítás

Frissítés előtt zárja be a szerkesztőt. Tartsa meg az exportált profilokat, és töltse le az új fork kiadást; telepítse ugyanazon a társazonosítón keresztül, vagy bontsa ki a hordozható fájlokat egy új mappába. Ne keverje össze a régi `Reference.xml` fájlt egy új végrehajtható fájllal. A kötegelt upstream frissítés-ellenőrzés-letiltás ehhez az fork-hez tartozik.

Telepített példányhoz használja az Windows **Installed apps** fájlt és annak eltávolítóját. Hordozható esetén zárja be, és távolítsa el a kibontott mappát, amikor az exportálás biztonságos. A szerkesztő eltávolítása **nem** vonja vissza az illesztőprogram-profil szerkesztéseit, a megjelenítési beállításokat, az NVRasterPulse vagy RTSS fájlokat. Az eltávolítás előtt állítsa vissza a kívánt beállításokat.

<a id="known-limitations"></a>
## Ismert korlátozások

- A 15 másodperces megerősítés nem őrzőkutya minden vezetői ütközésnél, áramkimaradásnál vagy kényszerleállásnál.
- Egyes szín/mélység/frissítés kombinációk az `NVAPI_NOT_SUPPORTED` értéket adják vissza.
- A szoftveres visszaolvasás nem méri a panel bitmélységét, színpontosságát vagy késleltetését.
- A képernyő beállításai befolyásolják az aktuális Windows kijelzőt; ez a párbeszédpanel nem hoz létre előre játékonkénti megjelenítési beállításokat.
- Nincs teljesítmény, csalás elleni vagy univerzális HDR kompatibilitási garancia.

<a id="troubleshooting"></a>
## Hibaelhárítás

| Tünet | Akció |
| --- | --- |
| Futásidejű hiba indításkor | Ellenőrizze az Windows frissítéseit és a .NET Framework 4.8; használja a teljes csomagot. |
| A kért megjelenítési mód elutasítva | Állítsa vissza és tesztelje az Windows/NVIDIA által az adott kijelzőhöz kínált módot. Olvassa el a pontos hibát, és kerülje az ismételt vak változtatásokat. |
| HDR vagy szín visszatér a régi állapotba | Ellenőrizze, hogy egy másik művelet meghiúsult-e, és nem vált-e ki visszaállítást; megkülönbözteti az HDR-et az ACM-től. |
| Az NVRasterPulse gomb visszautasítja az elérési utat | Indítsa el a saját parancsikonját; ehhez a gombhoz az egész rendszerre kiterjedő védett telepítés szükséges. |
| A változás az eltávolítás után is megmarad | Állítsa vissza az exportált NVIDIA profilt vagy a kívánt Windows megjelenítési beállításokat; Az eltávolítás nem a beállítások visszaállítása. |

A naplók küldése előtt tekintse meg az [megosztott támogatási útmutatást](../docs/support.md) dokumentumot.

<a id="faq"></a>
## GYIK

**Ez a hivatalos NVIDIA szoftver vagy az Orbmu2k hivatalos buildje?** Nem. Ez egy független fork; az upstream szerző és az MIT licenc továbbra is jóváírásra kerül.

**Az NVDriverForge-hez szükséges ez a szerkesztő?** Nem. Az NVDriverForge opcionális Custom NV előre beállított beállítása saját integrációt használ. A szerkesztő telepítése külön választás.

**Kötelező az RTSS ehhez az fork-hez?** Nem. Az RTSS kötelező az NVRasterPulse FPS korlátozójához, nem profil- vagy képernyőszerkesztéshez.

**Hol van a forrás?** A módosított alkalmazásforrást magán karbantartják. Az MIT értesítés és az upstream adattár biztosított; Az MIT nem igényli a módosított forrás közzétételét.

<a id="upstream-and-changes"></a>
## Upstream és változások

Felfelé: [Orbmu2k/nvidiaProfileInspector](https://github.com/Orbmu2k/nvidiaProfileInspector), referencia véglegesítés `592d962cca8827efe8859461a84267755595064a`. [Eredeti letöltések](https://github.com/Orbmu2k/nvidiaProfileInspector/releases).

Öröklött: profilszerkesztő, NVAPI interop, referencia adatok, UI erőforrások és témák. 禅堂 Zendo (RevoluSound Team) hozzáadott vagy adaptált megjelenítési szolgáltatások, HDR/ICC tranzakciók, 15 másodperces megerősítés/visszaolvasás, eszköztár elrendezés és RasterPulse indítási viselkedés. A megtisztított társ nem tartalmazza a fejlesztési gúnyokat/teszt belépési pontokat, védett külső indítót használ, és külön telepítőt biztosít. A régi kombinált NVPI/RasterPulse fejlesztői csomag nem a jelölt ebben a hubban.

[Részletes fájl származás](../docs/provenance.md) · [Eredeti fork értesítés](../../../../NVIDIA-Profile-Inspector/LICENSES/ORIGINAL-FORK-NOTICE.txt)

<a id="credits-and-license"></a>
## Kredit és licenc

Copyright (c) 2016 Orbmu2k. A mellékelt [MIT licenc](../../../../NVIDIA-Profile-Inspector/LICENSE) megmarad. Adaptációk és csomagolás: 禅堂 Zendo (RevoluSound Team). A telepítő az Inno Setup-et használja; Az Windows és a .NET-keretrendszer külső marad. [Teljes vonatkozó közlemények](LICENSES/README.md).

Független az NVIDIA Corporation-től, nem szponzorálja és hivatalosan nem hagyja jóvá. A védjegyek a megfelelő tulajdonosoknál maradnak.
