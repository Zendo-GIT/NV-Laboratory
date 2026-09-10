<!-- nv-language-navigation:start -->
🌐 [English](../../../installation.md) | [Français](../../../installation.fr.md) · [NV Laboratory](../README.md)

<details>
<summary>🌐 Language · 34</summary>

[العربية](../../ar/docs/installation.md) · [বাংলা](../../bn/docs/installation.md) · [简体中文](../../zh/docs/installation.md) · [Čeština](../../cs/docs/installation.md) · [Dansk](../../da/docs/installation.md) · [Nederlands](../../nl/docs/installation.md) · [English](../../../installation.md) · [Filipino](../../fil/docs/installation.md) · [Suomi](../../fi/docs/installation.md) · [Français](../../../installation.fr.md) · [Deutsch](../../de/docs/installation.md) · [Ελληνικά](../../el/docs/installation.md) · [हिन्दी](../../hi/docs/installation.md) · **Magyar** · [Bahasa Indonesia](../../id/docs/installation.md) · [Italiano](../../it/docs/installation.md) · [日本語](../../ja/docs/installation.md) · [한국어](../../ko/docs/installation.md) · [मराठी](../../mr/docs/installation.md) · [فارسی](../../fa/docs/installation.md) · [Polski](../../pl/docs/installation.md) · [Português](../../pt/docs/installation.md) · [ਪੰਜਾਬੀ](../../pa/docs/installation.md) · [Română](../../ro/docs/installation.md) · [Русский](../../ru/docs/installation.md) · [Español](../../es/docs/installation.md) · [Kiswahili](../../sw/docs/installation.md) · [Svenska](../../sv/docs/installation.md) · [தமிழ்](../../ta/docs/installation.md) · [ไทย](../../th/docs/installation.md) · [Türkçe](../../tr/docs/installation.md) · [Українська](../../uk/docs/installation.md) · [اردو](../../ur/docs/installation.md) · [Tiếng Việt](../../vi/docs/installation.md)

[Translation policy](../../README.md)

</details>
<!-- nv-language-navigation:end -->

<!-- nv-translation-notice:start -->
> Gépi fordítás angolból. A műszaki nevek, parancsok, URL-ek és az eredeti jogi szövegek megmaradnak. Szívesen fogadjuk az anyanyelvű véleményt; olvassa el az angol hivatkozást, ha a megfogalmazás nem egyértelmű.
<!-- nv-translation-notice:end -->

<a id="installation-guide"></a>
# Telepítési útmutató

Kezdje az [Letöltések](downloads.md)-el, amely rögzíti a közzététel állapotát és a pontos eszközneveket. Ezek különálló eszközök: csak azokat telepítse, amelyekre szüksége van.

> **NVRasterPulse esetén telepítse az [RTSS a Guru3D-től](https://www.guru3d.com/download/rtss-rivatuner-statistics-server-download/) fájlt a profilkezelő megnyitása előtt.**
> Az RTSS-nek futnia kell a korlátok alkalmazásához; az NV Tools nem tartalmazza.

| Eszköz | Telepített kiadás | Hordozható kiadás | Fő előfeltétel |
| --- | --- | --- | --- |
| NVIDIA Profile Inspector – NV Tools Fork | NVPI-CustomNV-3.0.2.3-Setup-r2.exe | A teljes NVPI ZIP kibontása | NVIDIA illesztőprogram és .NET Framework 4.8 |
| NVDriverForge | NVDriverForge-Setup.exe | NVDriverForge.exe, futásidővel | Kompatibilis eredeti NVIDIA illesztőprogram-csomag a telepítési műveletekhez |
| NVMFG Unlock40 | NVMFGUnlock40-0.1.1-Setup-x64.exe | A teljes NVMFG ZIP kibontása, az almappák megőrzése | RTX 40, meglévő DLSS FG, pontos szolgáltató és .NET Framework 4.8 segítők |
| NVRasterPulse | NVRasterPulse-0.1-win-x64-Setup.exe | A teljes RP ZIP kibontása | RTSS és .NET Framework 4.8 |

<a id="download-verify-install"></a>
## Töltse le, ellenőrizze, telepítse

1. A kiválasztott közzétett kiadáson töltse le a megnevezett alkalmazáselemet, a ZIP és SHA256SUMS.txt megjegyzéseket.
2. Használja az [SHA-256 példa](downloads.md#sha-256) fájlt a tényleges letöltött fájlnévvel.
3. A telepítéshez kövesse a normál telepítőt. Hordozható ZIP esetén csomagoljon ki mindent egy új helyi írható mappába; ne futtasson a ZIP-en belülről.
4. Nyissa meg az alkalmazás saját EXE-jét. Őrizze meg a mellékelt licenc-/konfigurációs/adatfájlokat.
5. A beállítások vagy a rendszerműveletek engedélyezése előtt olvassa el az eszköz használati utasítását.

Az aktuális binárisok előjel nélküliek. A megfelelő hash megerősíti a várt bájtokat; ez nem biztonsági vagy kompatibilitási tanúsítvány. Ne tiltsa le az Windows biztonsági védelmet csak a figyelmeztetés elnyomása érdekében.

Az NVDF vagy opcionális NVPI kísérőjének telepítése eltér az GPU illesztőprogram telepítésétől. Az NVPI kiegészítő megtartja meglévő belső telepítési nevét. A megemelt RasterPulse gombja védett rendszerszintű telepítést igényel; más RP másolatok saját parancsikonjaikon keresztül nyithatók meg.

Az NVMFG kísérleti jellegű, és rendelkezik az [dokumentált NVIDIA SDK licenctartalék](provenance.md)-vel. Nem tartalmaz NVIDIA illesztőprogramot, NGX szolgáltatót/modellt vagy játék Streamline futási környezetet. A kiválasztott SDK letöltések és játékfrissítések kifejezetten külön műveletek.

<a id="language-and-updates"></a>
## Nyelv és frissítések

Használja a README 34 nyelvű választóját a dokumentációhoz. Az NVDF, NVMFG és RP saját 34 nyelvű felhasználói felülettel rendelkezik; Az NVPI megtartja meglévő nyelvi támogatását. Néhány telepítő technikai karakterlánc visszanyúlik az angol nyelvre.

Frissítéskor őrizze meg az eszköz telepítési azonosítóját. Először zárja be, és őrizze meg a biztonsági másolatokat. NVMFG esetén zárja be az érintett játékokat, és oldja meg a függőben lévő profil-helyreállítást. Hordozható frissítésekhez használjon új mappát a kiadások kombinálása helyett.

<a id="removing-a-tool"></a>
## Szerszám eltávolítása

Egy alkalmazás eltávolítása nem jelenti automatikusan a beállítások visszavonását.

- **NVPI:** szükség esetén visszaállítja a kívánt profilokat/megjelenítési beállításokat az eltávolítás előtt.
- **NVDF:** először használja a helyreállítást, ha vissza szeretné állítani a speciális/NVENC módosításokat. Az Uninstall elhagyja a grafikus illesztőprogramot, a beállításokat és a biztonsági másolatokat.
- **NVMFG:** zárja be a játékokat, tiltsa le/kilép a vezérlőből, oldja meg az NVIDIA helyreállítást, és állítsa vissza a kívánt játék SDK biztonsági másolatait az eltávolítás előtt.
- **RP:** először távolítsa el a korlátozó szándékolt felülírásait. Az Uninstall nem törli a mentett RTSS kupakokat, és nem távolítja el az RTSS fájlt.

Tekintse meg az egyes [projekt útmutató](../README.md#projects)-eket az adatok pontos helyéről és korlátozásairól, vagy az [támogatást](support.md)-nél, ha a helyreállítási lépés sikertelen.
