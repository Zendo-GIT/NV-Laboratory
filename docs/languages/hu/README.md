<!-- nv-language-navigation:start -->
🌐 [English](../../../README.md) | [Français](../../../README.fr.md) · [NV Laboratory](README.md)

<details>
<summary>🌐 Language · 34</summary>

[العربية](../ar/README.md) · [বাংলা](../bn/README.md) · [简体中文](../zh/README.md) · [Čeština](../cs/README.md) · [Dansk](../da/README.md) · [Nederlands](../nl/README.md) · [English](../../../README.md) · [Filipino](../fil/README.md) · [Suomi](../fi/README.md) · [Français](../../../README.fr.md) · [Deutsch](../de/README.md) · [Ελληνικά](../el/README.md) · [हिन्दी](../hi/README.md) · **Magyar** · [Bahasa Indonesia](../id/README.md) · [Italiano](../it/README.md) · [日本語](../ja/README.md) · [한국어](../ko/README.md) · [मराठी](../mr/README.md) · [فارسی](../fa/README.md) · [Polski](../pl/README.md) · [Português](../pt/README.md) · [ਪੰਜਾਬੀ](../pa/README.md) · [Română](../ro/README.md) · [Русский](../ru/README.md) · [Español](../es/README.md) · [Kiswahili](../sw/README.md) · [Svenska](../sv/README.md) · [தமிழ்](../ta/README.md) · [ไทย](../th/README.md) · [Türkçe](../tr/README.md) · [Українська](../uk/README.md) · [اردو](../ur/README.md) · [Tiếng Việt](../vi/README.md)

[Translation policy](../README.md)

</details>
<!-- nv-language-navigation:end -->

<!-- nv-translation-notice:start -->
> Gépi fordítás angolból. A műszaki nevek, parancsok, URL-ek és az eredeti jogi szövegek megmaradnak. Szívesen fogadjuk az anyanyelvű véleményt; olvassa el az angol hivatkozást, ha a megfogalmazás nem egyértelmű.
<!-- nv-translation-notice:end -->

<a id="nv-laboratory"></a>
# NV Laboratory

**NV Tools, 禅堂 Zendo (RevoluSound Team).** Négy független Windows segédprogram NVIDIA illesztőprogram-profilokhoz, illesztőprogram-telepítés, kísérleti Multi Frame Generation és RTSS keretkorlátozás.

[Szerezd meg az eszközöket](docs/downloads.md) · [Telepítés](docs/installation.md) · [Kompatibilitás és segítség](docs/support.md) · [Kreditek és licencek](THIRD_PARTY_NOTICES.md)

> **Az NVRasterPulse-hez RTSS szükséges.** Először telepítse az [RivaTuner Statistics Server a Guru3D-től](https://www.guru3d.com/download/rtss-rivatuner-statistics-server-download/)-et. Az RTSS-nek futnia kell ahhoz, hogy az FPS korlátai működjenek. Külön letölthető.

<a id="projects"></a>
## Projektek

| Projekt | Cél | Verzió | Dokumentáció | Letöltés |
| --- | --- | --- | --- | --- |
| **NVIDIA Profile Inspector – NV Tools Fork** | NVIDIA illesztőprogram-profil szerkesztő hozzáadott kijelzővel, színnel, HDR és ICC/WCS vezérlőkkel. Korábban NVPI Custom. | 3.0.2.3 | [Útmutató](NVIDIA-Profile-Inspector/README.md) | [Csomagok](docs/downloads.md#nvidia-profile-inspector) |
| **NVDriverForge** | Készítsen elő és telepítsen egy eredeti NVIDIA illesztőprogramot irányított választásokkal, biztonsági mentésekkel és helyreállítással. | 0.1.4 | [Útmutató](NVDriverForge/README.md) | [Csomagok](docs/downloads.md#nvdriverforge) |
| **NVMFG Unlock40** | Kísérleti RTX 40 MFG, állandó játékkönyvtár, diagnosztika és Streamline SDK karbantartás. | 0.2.3 | [Útmutató](NVMFG-Unlock40/README.md) | [Csomagok és állapot](docs/downloads.md#nvmfg-unlock40) |
| **NVRasterPulse** | RTSS FPS programonkénti korlátok kezelése: diagnosztika, javaslatok, szüneteltetés, visszavonás és profilmegosztás. | 0.2 | [Útmutató](NVRasterPulse/README.md) | [Csomagok](docs/downloads.md#nvrasterpulse) |

**Letöltések:** az [letöltési oldal](docs/downloads.md) felsorolja az egyes verziók állapotát, fájljait és SHA-256 értékeit. A kísérleti funkciók és a kompatibilitási korlátok leírása a projekt útmutatókban található.

<a id="start-here"></a>
## Kezdje itt

1. Válasszon egy eszközt fent. Mindegyik önállóan működik; szükségtelen az egész csomagot telepíteni.
2. Olvassa el a követelményeket, és válassza a **Beállítás** lehetőséget egy telepített alkalmazáshoz, vagy a **hordozható** lehetőséget külön mappához.
3. A kiadás közzétételekor töltse le a megnevezett alkalmazáselemet, olvassa el a kísérő megjegyzéseket, és hasonlítsa össze az SHA-256-et.
4. Készítsen biztonsági másolatot az illesztőprogram, a képernyőbeállítás, az NVIDIA profil vagy a játék futásidejének megváltoztatása előtt.

A dokumentáció ugyanazon a 34 nyelven érhető el, mint az NV alkalmazások az egyes útmutatók tetején található választó segítségével. Az GitHub nem választ automatikusan README-t a böngésző nyelve szerint. A dokumentáció nyelve és az alkalmazás saját nyelvi beállítása különálló.

<a id="provenance-and-ownership"></a>
## Származási hely és tulajdonjog

Ez a központ a dokumentációt és a lefordított alkalmazásokat terjeszti. Az alkalmazás forráskódját privát módon kezelik. Az upstream projektek megtartják szerzői jogukat és licenceiket; magánforrású terjesztés nem helyettesíti ezeket a kifejezéseket.

- Az Profile Inspector fork megtartja az Orbmu2k MIT licencét, és kifejezetten fork néven azonosítható.
- Az NVDriverForge saját bináris terjesztési feltételekkel rendelkezik, és külön licencelt futásidejű/eszköz-összetevőket tartalmaz.
- Az NVMFG Unlock40 egy önállóan fejlesztett alkalmazás. Összehasonlítás és finomítás céljából az RTX40MFG-Unlock konzultált; a megosztott natív összetevők megtartják MIT jóváírásukat. Az MinHook és az NVIDIA SDK feltételek külön maradnak.
- Az NVRasterPulse megtartja a mellékelt MIT licencet, és jóváírja az Profile Inspector-ből származó felhasználói felületet. Az RTSS egy kötelező külső program.

Lásd: [teljes komponens táblázat](THIRD_PARTY_NOTICES.md), [fájl eredete és változásai](docs/provenance.md) és [licenc hatálya](../../../LICENSE).

<a id="other-projects--revolusound-team"></a>
## Egyéb projektek – RevoluSound Team

Ezek különálló audio mod projektek, amelyek linkje itt segít felfedezni a csapat munkáját.

| Játék | Projekt | Körülbelül |
| --- | --- | --- |
| Forza Horizon 6 | [Forza Horizon 6 Revolusound Team Pack](https://www.nexusmods.com/forzahorizon6/mods/56) | Változások a jármű hangjában, beleértve a motorokat, a kipufogókat, a szívórendszereket és a turbóeffektusokat. |
| Forza Horizon 5 | [Forza Horizon 5 Revolusound Team Pack 1.4.4 FINAL](https://www.nexusmods.com/forzahorizon5/mods/86) | A csapat későbbi FH5 jármű audio csomagja. |
| Forza Horizon 5 | [Forza Horizon 5.5 Zendo Revolusound Pack](https://www.nexusmods.com/forzahorizon5/mods/20) | Korábbi FH5 csomag; Nexus oldala a fenti, későbbi csapatcsomaghoz irányítja a látogatókat. |

A címek a hivatkozott Nexus Mods oldalakat követik. Letöltéseik, követelményeik, jóváírásaik és engedélyeik az Nexus Mods-en maradnak.

<a id="help-and-participation"></a>
## Segítség és részvétel

[Hiba bejelentése vagy funkció javaslata](https://github.com/Zendo-GIT/NV-Laboratory/issues) · [Hozzájárulás](CONTRIBUTING.md) · [Biztonsági jelentések](SECURITY.md) · [Változásnapló](CHANGELOG.md)

Biztonsági probléma esetén olvassa el az SECURITY.md dokumentumot, mielőtt naplókat vagy műszaki adatokat tesz közzé. A privát jelentést a tár közzététele után a fenntartónak engedélyeznie kell.

> **Független közösségi projektek.** Az NV Laboratory, NV Tools és ezek a segédprogramok nem kapcsolódnak az NVIDIA Corporation-hez, nem szponzorálják vagy hivatalosan jóváhagyják. Az NVIDIA, GeForce, RTX, DLSS és más terméknevek megfelelő tulajdonosaik védjegyei. A nevek a kompatibilitást és a származást írják le, nem pedig a hivatalos jóváhagyást.
