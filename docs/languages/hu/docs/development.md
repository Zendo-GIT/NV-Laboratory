<!-- nv-language-navigation:start -->
🌐 [English](../../../development.md) | [Français](../../../development.fr.md) · [NV Laboratory](../README.md)

<details>
<summary>🌐 Language · 34</summary>

[العربية](../../ar/docs/development.md) · [বাংলা](../../bn/docs/development.md) · [简体中文](../../zh/docs/development.md) · [Čeština](../../cs/docs/development.md) · [Dansk](../../da/docs/development.md) · [Nederlands](../../nl/docs/development.md) · [English](../../../development.md) · [Filipino](../../fil/docs/development.md) · [Suomi](../../fi/docs/development.md) · [Français](../../../development.fr.md) · [Deutsch](../../de/docs/development.md) · [Ελληνικά](../../el/docs/development.md) · [हिन्दी](../../hi/docs/development.md) · **Magyar** · [Bahasa Indonesia](../../id/docs/development.md) · [Italiano](../../it/docs/development.md) · [日本語](../../ja/docs/development.md) · [한국어](../../ko/docs/development.md) · [मराठी](../../mr/docs/development.md) · [فارسی](../../fa/docs/development.md) · [Polski](../../pl/docs/development.md) · [Português](../../pt/docs/development.md) · [ਪੰਜਾਬੀ](../../pa/docs/development.md) · [Română](../../ro/docs/development.md) · [Русский](../../ru/docs/development.md) · [Español](../../es/docs/development.md) · [Kiswahili](../../sw/docs/development.md) · [Svenska](../../sv/docs/development.md) · [தமிழ்](../../ta/docs/development.md) · [ไทย](../../th/docs/development.md) · [Türkçe](../../tr/docs/development.md) · [Українська](../../uk/docs/development.md) · [اردو](../../ur/docs/development.md) · [Tiếng Việt](../../vi/docs/development.md)

[Translation policy](../../README.md)

</details>
<!-- nv-language-navigation:end -->

<!-- nv-translation-notice:start -->
> Gépi fordítás angolból. A műszaki nevek, parancsok, URL-ek és az eredeti jogi szövegek megmaradnak. Szívesen fogadjuk az anyanyelvű véleményt; olvassa el az angol hivatkozást, ha a megfogalmazás nem egyértelmű.
<!-- nv-translation-notice:end -->

<a id="repository-architecture-and-maintenance"></a>
# Repository architektúra és karbantartás

Az NV Laboratory egy nyilvános **dokumentációs és bináris terjesztési központ**. Nem tartalmazza az alkalmazás forrását. A négy projekt külön összeállítási fákat, verziókat, identitásokat és kiadási eszközöket őriz meg. Saját fejlesztési előzményeiket nem importálják ebbe a Git-tárba.

<a id="layout"></a>
## Elrendezés

| Helyszín | Cél |
| --- | --- |
| README.md / README.fr.md | Angol/francia belépési pontok |
| Négy projektmappa | Teljes útmutatók és vonatkozó eredeti megjegyzések |
| dok | Letöltések, kompatibilitás, eredet, fejlesztés és kiadás |
| docs/releases.json | Ellenőrzött jelölt/kiadás metaadatok, méretek és hashek |
| dokumentumok/eredet | Fájl/hash összehasonlítások; nincs alkalmazáskód |
| engedélyeket | Megosztott teljes, harmadik féltől származó szövegeket és telepítői fordítói krediteket |
| eszközök | Meglévő felülvizsgált felhasználói felület előnézetek és származásuk |
| .github | Űrlapok kiadása és írásvédett dokumentáció érvényesítése |
| eszközök/validate_repository.py | Szabványos könyvtári kiadványhatárok és hivatkozások ellenőrzése |

Az angol továbbra is az alapértelmezett GitHub README. A meglévő szomszédos `.fr.md` hivatkozások érvényesek maradnak. A további fordítások tükrözik az `docs/languages/<code>` alatti dokumentációt; a nyelvválasztó ugyanazt az oldalt tartja a nyelvváltáskor. Az `docs/languages/catalog.json` katalógus mind a 34 nyelvet és a forrás ujjlenyomatait rögzíti. Az GitHub nem választ ki automatikusan egy README-t a böngésző nyelve szerint. Lásd: [nyelvi index és fordítási politika](../../README.md).

<a id="application-technologies"></a>
## Alkalmazási technológiák

| Program | Privát technológia | Elosztás |
| --- | --- | --- |
| NVPI fork | C#, WPF, .NET Framework 4.8, NVAPI/Windows együttműködés | Komplett hordozható mappa és külön Inno Setup |
| NVDriverForge | C#, WPF, .NET 8; natív C++ bootstrap; 7-Zip folyamat | Önálló hordozható EXE és telepítő |
| NVMFG Unlock40 | C#/WPF .NET 8, Framework 4.8 segítők, C++20/MASM/MinHook motor | Hordozható fa és beállítás |
| NVRasterPulse | C#/WPF Framework 4.8; RTSS profil/újratöltés integráció; natív bootstrap | Hordozható fa és beállítás |

Ez a nyilvános fizetés nem tudja újraépíteni az alkalmazásokat. Az automatikus „Source code” archívumok központi pillanatképek. Az upstream forráshivatkozások nem képviselik pontosan a privát módosított forrást. A nyilvános CI csak ezt a tárolót érvényesíti.

<a id="local-checks"></a>
## Helyi ellenőrzések

A tároló gyökérből:

```text
python tools/validate_repository.py
```

Python 3.10 vagy újabb elegendő. Az ellenőrzés beolvassa a fájlokat, a helyi Markdown hivatkozásokat, a kötelező értesítéseket/RTSS hivatkozásokat, a kiadási metaadatokat és a közzétételi határokat. Nem hajtja végre a szoftvert, nem telepít függőségeket, és nem lép kapcsolatba a hálózattal.

Az GitHub munkafolyamat ugyanezt az ellenőrzést futtatja csak olvasható tartalomengedéllyel push, pull kérés vagy kézi feladás esetén. A Checkout egy auditált véglegesítéshez van rögzítve, és nem őrzi meg a hitelesítő adatokat. Nincs konfigurálva kiadási vagy telepítési feladat.

<a id="maintain-the-boundary"></a>
## Tartsa be a határt

Frissítse együtt az angol nyelvű hivatkozást, a francia útmutatókat és az érintett fordításokat. A lényegi változtatásokat tartsa külön a csak formázási összehasonlításoktól. Rögzítse a tényleges jelölt kivonatokat, az upstream commit referenciákat és licenceket; soha ne következtessen licencre egy projekt népszerűségéből.

Használjon friss verziójú kiadási eszközöket, és ellenőrizze újra a megváltozott bináris fájlokat, archívumot és beágyazott értesítéseket. A privát biztonsági másolatok megőrzése ezen a tárolón kívül. Ne használjon nyilvános munkafolyamatot privát alkalmazásforrások vagy helyi összeállítási mappák importálásához.

A funkcionális alkalmazásmódosításoknak megfelelő tesztek futnak a privát projektben. Ne futtassa újra az illesztőprogram-telepítőket, és ne írjon valódi profilokat a dokumentáció frissítéséhez. [Kézi kioldási eljárás](releasing.md).
