<!-- nv-language-navigation:start -->
🌐 [English](../../../releasing.md) | [Français](../../../releasing.fr.md) · [NV Laboratory](../README.md)

<details>
<summary>🌐 Language · 34</summary>

[العربية](../../ar/docs/releasing.md) · [বাংলা](../../bn/docs/releasing.md) · [简体中文](../../zh/docs/releasing.md) · [Čeština](../../cs/docs/releasing.md) · [Dansk](../../da/docs/releasing.md) · [Nederlands](../../nl/docs/releasing.md) · [English](../../../releasing.md) · [Filipino](../../fil/docs/releasing.md) · [Suomi](../../fi/docs/releasing.md) · [Français](../../../releasing.fr.md) · [Deutsch](../../de/docs/releasing.md) · [Ελληνικά](../../el/docs/releasing.md) · [हिन्दी](../../hi/docs/releasing.md) · **Magyar** · [Bahasa Indonesia](../../id/docs/releasing.md) · [Italiano](../../it/docs/releasing.md) · [日本語](../../ja/docs/releasing.md) · [한국어](../../ko/docs/releasing.md) · [मराठी](../../mr/docs/releasing.md) · [فارسی](../../fa/docs/releasing.md) · [Polski](../../pl/docs/releasing.md) · [Português](../../pt/docs/releasing.md) · [ਪੰਜਾਬੀ](../../pa/docs/releasing.md) · [Română](../../ro/docs/releasing.md) · [Русский](../../ru/docs/releasing.md) · [Español](../../es/docs/releasing.md) · [Kiswahili](../../sw/docs/releasing.md) · [Svenska](../../sv/docs/releasing.md) · [தமிழ்](../../ta/docs/releasing.md) · [ไทย](../../th/docs/releasing.md) · [Türkçe](../../tr/docs/releasing.md) · [Українська](../../uk/docs/releasing.md) · [اردو](../../ur/docs/releasing.md) · [Tiếng Việt](../../vi/docs/releasing.md)

[Translation policy](../../README.md)

</details>
<!-- nv-language-navigation:end -->

<!-- nv-translation-notice:start -->
> Gépi fordítás angolból. A műszaki nevek, parancsok, URL-ek és az eredeti jogi szövegek megmaradnak. Szívesen fogadjuk az anyanyelvű véleményt; olvassa el az angol hivatkozást, ha a megfogalmazás nem egyértelmű.
<!-- nv-translation-notice:end -->

<a id="publishing-and-releases"></a>
# Kiadás és kiadások

A nyilvános adattár a **Zendo-GIT/NV-Laboratory**. A dokumentációs változtatásokat a karbantartó felülvizsgálja, elfogadja és továbbítja az **GitHub Desktop** segítségével. A helyi véglegesítés nem tölt fel fájlokat. A bináris csomagok különálló GitHub kiadási eszközök; soha nem tartoznak a Git változások listájába.

<a id="documentation-updates"></a>
## Dokumentációs frissítések

1. Nyissa meg az **NV-Laboratory** mappát az GitHub Desktop-ben.
2. Tekintse át a dokumentációt, az értesítéseket, a képeket, a JSON-metaadatokat és a dokumentáció érvényesítőjét.
3. Futtassa az `python tools/validate_repository.py` fájlt ebből a mappából.
4. Végezze el a felülvizsgált módosításokat, majd használja az **Push origin** kódot. Ellenőrizze a Műveletek eredményét.
5. Tartsa meg a nyilvános szerzői azonosítót (**禅堂 Zendo (RevoluSound Team)**) és a fiók GitHub `noreply` címét.

Soha ne válassza ki a szülő fejlesztői munkaterületet, a privát ellenőrzési könyvtárat vagy a bináris mellékletek könyvtárát. [Az e-mailek adatvédelmének biztosítása](https://docs.github.com/en/account-and-profile/how-tos/email-preferences/setting-your-commit-email-address).

<a id="independent-application-releases"></a>
## Független alkalmazáskiadások

| Eszköz | Címke | Verziószabályzat |
| --- | --- | --- |
| NVIDIA Profile Inspector – NV Tools Fork | nvpi-v3.0.2.3 | Meglévő négyrészes alkalmazásverzió; A 2. beállítási változatnak saját fájlneve van |
| NVDriverForge | nvdriverforge-v0.1.3 | Meglévő 0.x séma; A verziójú frissítések megőrzik a korábbi csomagokat |
| NVMFG Unlock40 | nvmfg-unlock40-v0.1.1 | Az UI2 jelölt pontos kivonatokkal azonosítható anélkül, hogy új alkalmazásverziót találtak volna ki |
| NVRasterPulse | nvrasterpulse-v0.1 | Meglévő kétrészes változat |

A fenntartó közvetlenül közzéteheti, vagy asszisztenst hatalmazhat fel az ellenőrzött vagyon közzétételére. A közzététel explicit; egyetlen munkafolyamat sem hoz létre kiadást minden véglegesítéskor.

1. Tekintse át az aktuális közzététel előtti jelentést, a binárisok forrásait, a licenceket és az SHA-256 értékeket.
2. Hozzon létre egy piszkozatot az eszköz címkéjéhez, megcélozva a felülvizsgált hub véglegesítést. Tartalmazza az elkészített verzióspecifikus kiadási megjegyzéseket.
3. Csak az adott verzió telepítő/hordozható eszközeit, az `Licenses-and-Credits.zip` és az `SHA256SUMS.txt` fájlokat csatolja.
4. Ellenőrizze a kompatibilitást, a telepítést, a függőségeket, a változtatásokat és az ismert korlátokat. Az RTSS legyen látható az NVRasterPulse esetében.
5. Tegye közzé, ellenőrizze a nyilvános tartalom URL-jét, méretét és kivonatát, és rögzítse a tényleges közzétételi dátumot az `docs/releases.json` fájlban.
6. Frissítse a letöltési oldalakat és a fordításokat, majd véglegesítse/küldje el a változtatásokat az GitHub Desktop fájlban.

A projektenkénti címkehivatkozások elkerülik, hogy a felhasználókat egy megosztott `releases/latest` hivatkozáson keresztül másik eszközbe küldjék. Az GitHub automatikus **Source code** archívuma tartalmazza ezt a dokumentációs központot. Az alkalmazásforrások privátak maradnak. Az eredeti összetevőkre vonatkozó megjegyzések érintetlenek maradnak, és a kiadás nem oldja meg az NVMFG dokumentált NVIDIA SDK tartalékát.

<a id="integrity-and-storage"></a>
## Integritás és tárolás

Soha ne cserélje le csendben a közzétett bináris bájtokat. Használjon új explicit verziót vagy telepítői változatot új hashekkel. A legális oldalkocsik kiegészítik a beágyazott figyelmeztetéseket. NVDriverForge Az 0.1.3 hordozható mérete 141 760 351 bájt, ami meghaladja az GitHub szokásos 100 MiB Git-fájl korlátját. A mellékletek kiadásakor ne helyezzen bináris fájlokat vagy Git LFS-t ebbe a hubba. [GitHub nagy fájlú útmutatás](https://docs.github.com/en/repositories/working-with-files/managing-large-files/about-large-files-on-github).

A lerakat biztonsági beállításainál engedélyezni kell a privát sebezhetőség jelentését. Ellenőrizze az elérhetőségét, mielőtt a bizalmas jelentéseket oda irányítaná; Az [SECURITY.md](../SECURITY.md) olyan tartalékot biztosít, amely nem fedi fel a sebezhetőség részleteit.

[Katalógus letöltése](downloads.md) · [GitHub kiadási dokumentáció](https://docs.github.com/en/repositories/releasing-projects-on-github/managing-releases-in-a-repository)
