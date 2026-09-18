<!-- nv-language-navigation:start -->
🌐 [English](../../../support.md) | [Français](../../../support.fr.md) · [NV Laboratory](../README.md)

<details>
<summary>🌐 Language · 34</summary>

[العربية](../../ar/docs/support.md) · [বাংলা](../../bn/docs/support.md) · [简体中文](../../zh/docs/support.md) · [Čeština](../../cs/docs/support.md) · [Dansk](../../da/docs/support.md) · [Nederlands](../../nl/docs/support.md) · [English](../../../support.md) · [Filipino](../../fil/docs/support.md) · [Suomi](../../fi/docs/support.md) · [Français](../../../support.fr.md) · [Deutsch](../../de/docs/support.md) · [Ελληνικά](../../el/docs/support.md) · [हिन्दी](../../hi/docs/support.md) · **Magyar** · [Bahasa Indonesia](../../id/docs/support.md) · [Italiano](../../it/docs/support.md) · [日本語](../../ja/docs/support.md) · [한국어](../../ko/docs/support.md) · [मराठी](../../mr/docs/support.md) · [فارسی](../../fa/docs/support.md) · [Polski](../../pl/docs/support.md) · [Português](../../pt/docs/support.md) · [ਪੰਜਾਬੀ](../../pa/docs/support.md) · [Română](../../ro/docs/support.md) · [Русский](../../ru/docs/support.md) · [Español](../../es/docs/support.md) · [Kiswahili](../../sw/docs/support.md) · [Svenska](../../sv/docs/support.md) · [தமிழ்](../../ta/docs/support.md) · [ไทย](../../th/docs/support.md) · [Türkçe](../../tr/docs/support.md) · [Українська](../../uk/docs/support.md) · [اردو](../../ur/docs/support.md) · [Tiếng Việt](../../vi/docs/support.md)

[Translation policy](../../README.md)

</details>
<!-- nv-language-navigation:end -->

<!-- nv-translation-notice:start -->
> Gépi fordítás angolból. A műszaki nevek, parancsok, URL-ek és az eredeti jogi szövegek megmaradnak. Szívesen fogadjuk az anyanyelvű véleményt; olvassa el az angol hivatkozást, ha a megfogalmazás nem egyértelmű.
<!-- nv-translation-notice:end -->

<a id="compatibility-and-troubleshooting"></a>
# Kompatibilitás és hibaelhárítás

Ezek az előkészített jelöltek, nem pedig egy minősítési mátrix minden Windows, GPU, illesztőprogram és játék kombinációhoz.

| Eszköz | Windows / futásidejű | Hardver/külső függőség | Gondozást igénylő műveletek |
| --- | --- | --- | --- |
| NVPI fork 3.0.2.3 | Windows 10/11 x64, .NET-keretrendszer 4.8 | Kompatibilis NVIDIA illesztőprogram/kijelző | Profil ír és megjeleníti az előnézeteket |
| NVDriverForge 0.1.4 | Windows 10 build 19041+ / 11 x64; .NET/WPF tartalmazza | Kompatibilis NVIDIA illesztőprogram-csomag | Magasabb szintű telepítés, speciális beállítások, opcionális NVENC |
| NVMFG Unlock40 0.2.3 | Windows 10/11 x64; .NET/WPF tartalmazza, Framework 4.8 segítők | RTX 40, jogosult DLSS FG játék és rögzített szolgáltató | Natív játékon belüli javítás, globális profilnapló, SDK játékfrissítések |
| NVRasterPulse 0.2 | Windows 10/11 x64, .NET-keretrendszer 4.8 | RTSS telepítve; fut a sapkákért | RTSS végrehajtható profilonkénti változások |

Nincs ARM64 csomag. A kijelző/API elérhetősége és a régi Windows verziók korlátozhatják az egyes funkciókat. Nincs univerzális minimum NVIDIA vagy RTSS verzió. A pontos NVMFG szolgáltató hash az [eredetét](provenance.md) fájlban található.

<a id="before-reporting-a-bug"></a>
## Mielőtt hibát jelentene

Határozza meg pontosan a megnyitott futtatható fájlt/verziót. A korábban telepített példány nem feltétlenül az újonnan letöltött ZIP verziója. Jegyezze fel a reprodukciós lépéseket, a várt eredményt és a tényleges eredményt. Renderelési/korlátozási problémák esetén adja meg a játék verzióját, a kijelző frissítését, az FG/V-Sync/VRR állapotot és bármely más korlátozót vagy átfedést.

Használja az [bug forma](https://github.com/Zendo-GIT/NV-Laboratory/issues/new?template=bug-report.yml)-et. Soha ne csatoljon teljes privát fejlesztési mappát, illesztőprogram-archívumot, modellt, játék DLL-t, rendszerleíró adatbázis kiíratását vagy át nem vizsgált naplógyűjteményt.

| Probléma | Első ellenőrzések |
| --- | --- |
| Hibás alkalmazásverzió | Erősítse meg az EXE-azonosságot és engedje fel a hash-t; csere előtt zárja be a régebbi példányt. |
| Futási/indítási hiba | Telepítse a szükséges 4.8 keretrendszert, vagy őrizze meg az összes mellékelt hordozható almappát. |
| UAC törölve | Csak a tervezett műveletet próbálja újra; a törlés nem sikeres a telepítés. |
| Hash/aláírás eltérés | Hagyja abba a jelölt használatát, és szerezze be a várt hivatalos bájtokat. |
| NVPI szín/mód elutasítva | Állítsa vissza, és használja a tényleges kijelző/illesztőprogram által támogatott kombinációt. |
| NVDF biztonsági mentési vagy helyreállítási hiba | Védett munka és RECOVERY.txt megőrzése; ne törölje a naplót, és ne kényszerítse az egymásnak ellentmondó írásokat. |
| NVMFG pending settings | Oldja meg a helyreállítást a játékok lezárásával, megőrizve a többi eszköz változásait. |
| Az RP sapkának nincs hatása | Futtassa az RTSS programot, azonosítsa az igazi játék EXE-t, ellenőrizze a horog állapotát és a versengő limiteket. |
| Az RP kupak az eltávolítás után is megmarad | Vizsgálja meg az RTSS Global; eltávolítási változások csak helyi korlátozó felülbírálja. |

Az NVDriverForge egy megtekinthető helyi JSON jelentést kínál; Az NVMFG diagnosztikát kínál az About. Előnyben részesítse ezeket a szűrt jelentéseket a teljes naplóarchívum helyett, és megosztás előtt ellenőrizze őket. Az NVMFG 0.1.1 jelzett helyreállítási elakadásának még mindig nincs megállapított oka; őrizze meg a naplóját, és rögzítse a rendelkezésre álló hibakódokat. NVRasterPulse Az 0.2 konfigurációs diagnosztikát kínál a műveletek menüjében, az FPS mérése nélkül.

<a id="logs-and-privacy"></a>
## Naplók és adatvédelem

| Eszköz | Helyi adatok áttekintésére, nem nagykereskedelmi feltöltésre |
| --- | --- |
| NVDF | `%LOCALAPPDATA%\NVDriverForge`; védett munkahelyek `%PROGRAMDATA%\NVDriverForge\Jobs` |
| NVMFG | `%LOCALAPPDATA%\RtxMfg`; biztonsági mentések `%LOCALAPPDATA%\NvidiaStreamlineMaintenance\Backups`; `Sessions` az EXE mellett |
| RP | `%LOCALAPPDATA%\NVRasterPulse`; `Backups\RTSS` alatta |
| NVPI | Az Ön által kiválasztott exportok és a megjelenített hiba; nincs kitalált univerzális rönkút |

Távolítsa el a fiókneveket, a kezdőkönyvtárakat, a játékkönyvtár útvonalait, az eszközazonosítókat, a tokeneket és a nem kapcsolódó ablakokat a megosztott szövegekből/képekből. Tartsa magánál az eredetiket a helyreállításhoz. A nyilvános kérdések mindenki számára láthatóak.

Sebezhetőség, veszélyes kiváltságos viselkedés vagy nem szándékos romboló művelet esetén kövesse az [SECURITY.md](../SECURITY.md) kódot a részletek nyilvános közzététele helyett.

<a id="what-has-been-verified"></a>
## Amit ellenőriztek

A hub előkészítéséhez statikus hasznos adat/ZIP/hash/metaadat vizsgálatokat és dokumentáció-ellenőrzéseket végeztünk. A meglévő privát alkalmazások build/unit/UI tesztjei történelmi, keltezett bizonyítékok. Ennek az előkészítésnek a részeként nem történt illesztőprogram-telepítés, megjelenítésváltás, élő RTSS művelet vagy játék benchmark.

Az „észlelve”, „írva”, „újratöltve”, „elérhető képesség” és „játékban mérve” különböző eredmények. Jelentse, melyiket figyelte meg.
