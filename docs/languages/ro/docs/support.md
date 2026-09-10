<!-- nv-language-navigation:start -->
🌐 [English](../../../support.md) | [Français](../../../support.fr.md) · [NV Laboratory](../README.md)

<details>
<summary>🌐 Language · 34</summary>

[العربية](../../ar/docs/support.md) · [বাংলা](../../bn/docs/support.md) · [简体中文](../../zh/docs/support.md) · [Čeština](../../cs/docs/support.md) · [Dansk](../../da/docs/support.md) · [Nederlands](../../nl/docs/support.md) · [English](../../../support.md) · [Filipino](../../fil/docs/support.md) · [Suomi](../../fi/docs/support.md) · [Français](../../../support.fr.md) · [Deutsch](../../de/docs/support.md) · [Ελληνικά](../../el/docs/support.md) · [हिन्दी](../../hi/docs/support.md) · [Magyar](../../hu/docs/support.md) · [Bahasa Indonesia](../../id/docs/support.md) · [Italiano](../../it/docs/support.md) · [日本語](../../ja/docs/support.md) · [한국어](../../ko/docs/support.md) · [मराठी](../../mr/docs/support.md) · [فارسی](../../fa/docs/support.md) · [Polski](../../pl/docs/support.md) · [Português](../../pt/docs/support.md) · [ਪੰਜਾਬੀ](../../pa/docs/support.md) · **Română** · [Русский](../../ru/docs/support.md) · [Español](../../es/docs/support.md) · [Kiswahili](../../sw/docs/support.md) · [Svenska](../../sv/docs/support.md) · [தமிழ்](../../ta/docs/support.md) · [ไทย](../../th/docs/support.md) · [Türkçe](../../tr/docs/support.md) · [Українська](../../uk/docs/support.md) · [اردو](../../ur/docs/support.md) · [Tiếng Việt](../../vi/docs/support.md)

[Translation policy](../../README.md)

</details>
<!-- nv-language-navigation:end -->

<!-- nv-translation-notice:start -->
> Traducere asistată automat din engleză. Numele tehnice, comenzile, URL-urile și textele legale originale sunt păstrate. Evaluarea vorbitorilor nativi este binevenită; consultați referința în limba engleză dacă formularea este neclară.
<!-- nv-translation-notice:end -->

<a id="compatibility-and-troubleshooting"></a>
# Compatibilitate și depanare

Aceștia sunt candidații pregătiți, nu o matrice de certificare pentru toate combinațiile Windows, GPU, driver și joc.

| Instrument | Windows / runtime | Hardware/dependență externă | Operații care necesită îngrijire |
| --- | --- | --- | --- |
| NVPI fork 3.0.2.3 | Windows 10/11 x64, .NET Framework 4.8 | Driver/afișaj compatibil NVIDIA | Profilul scrie și afișează previzualizări |
| NVDriverForge 0.1.2 | Windows 10 build 19041+ / 11 x64; .NET/WPF inclus | Pachet de driver compatibil NVIDIA | Instalare ridicată, setări avansate, opțional NVENC |
| NVMFG Unlock40 0.1.1 | Windows 10/11 x64; .NET/WPF inclus, ajutoare Framework 4.8 | RTX 40, joc DLSS FG eligibil și furnizor fixat | Patch nativ în joc, jurnal de profil global, actualizări ale jocului SDK |
| NVRasterPulse 0.1 | Windows 10/11 x64, .NET Framework 4.8 | RTSS instalat; alergând după capace | RTSS modificări de profil per-executable |

Nu este pregătit niciun pachet ARM64. Disponibilitatea afișajului/API și versiunile vechi Windows pot limita funcțiile individuale. Nu este inventată nicio versiune minimă universală NVIDIA sau RTSS. Hash-ul exact al furnizorului NVMFG este în [proveniența](provenance.md).

<a id="before-reporting-a-bug"></a>
## Înainte de a raporta o eroare

Identificați exact executabilul/versiunea pe care ați deschis-o. O copie instalată anterioară nu este neapărat versiunea unui ZIP nou descărcat. Înregistrați etapele de reproducere, rezultatul așteptat și rezultatul real. Pentru probleme de randare/limitare, includeți versiunea jocului, reîmprospătarea afișajului, starea FG/V-Sync/VRR și orice alt limitator sau suprapunere.

Utilizați [formă de bug](https://github.com/Zendo-GIT/NV-Laboratory/issues/new?template=bug-report.yml). Nu atașați niciodată un întreg folder privat de dezvoltare, arhivă de drivere, model, DLL de joc, dump de registry sau colecții de jurnal nerevizuite.

| Problemă | Primele verificări |
| --- | --- |
| Versiune greșită a aplicației | Confirmați identitatea EXE și eliberați hash; închideți copia mai veche înainte de înlocuire. |
| Eroare de rulare/pornire | Instalați cadrul necesar 4.8 sau păstrați toate subfolderele portabile furnizate. |
| UAC anulat | Reîncercați numai operațiunea intenționată; anularea nu este instalată cu succes. |
| Nepotrivire hash/semnătură | Nu mai utilizați acel candidat și obțineți octeții oficiali așteptați. |
| NVPI culoare/mod respins | Reveniți și utilizați o combinație acceptată de afișajul/driverul actual. |
| NVDF backup sau eșec de recuperare | Păstrați locul de muncă protejat și RECOVERY.txt; nu șterge jurnalul și nu forța scrierile contradictorii. |
| Setări NVMFG în așteptare | Rezolvați recuperarea cu jocurile închise, păstrând modificările de la alte instrumente. |
| Capacul RP nu are efect | Rulați RTSS, identificați jocul real EXE, inspectați starea cârligului și limitele concurente. |
| Capacul RP persistă după îndepărtare | Inspectați RTSS Global; eliminarea modifică numai anulări ale limitatorului local. |

<a id="logs-and-privacy"></a>
## Jurnalele și confidențialitatea

| Instrument | Date locale de examinat, nu de încărcat cu ridicata |
| --- | --- |
| NVDF | `%LOCALAPPDATA%\NVDriverForge`; locuri de muncă protejate `%PROGRAMDATA%\NVDriverForge\Jobs` |
| NVMFG | `%LOCALAPPDATA%\RtxMfg`; copii de rezervă `%LOCALAPPDATA%\NvidiaStreamlineMaintenance\Backups`; `Sessions` lângă EXE |
| RP | `%LOCALAPPDATA%\NVRasterPulse`; `Backups\RTSS` dedesubt |
| NVPI | Exporturile alese de dvs. și eroarea afișată; nicio cale universală de log inventată |

Eliminați numele conturilor, directoarele de acasă, căile de bibliotecă de jocuri, identificatorii dispozitivului, jetoanele și ferestrele care nu au legătură din textul/imaginile pe care le partajați. Păstrați originalele în mod privat pentru recuperare. Problemele publice sunt vizibile pentru toată lumea.

Pentru o vulnerabilitate, un comportament privilegiat periculos sau o operațiune distructivă neintenționată, urmați [SECURITY.md](../SECURITY.md) în loc să publicați detalii în mod public.

<a id="what-has-been-verified"></a>
## Ce s-a verificat

Pentru pregătirea hub-ului, au fost efectuate scanări statice de încărcare utilă/ZIP/hash/metadate și verificări ale documentației. Testele de compilare/unitate/UI de aplicații private existente sunt dovezi istorice, datate. Nu a fost efectuată nicio instalare a driverului, schimbarea afișajului, operațiune live RTSS sau benchmark al jocului ca parte a acestei pregătiri.

„Detectat”, „scris”, „reîncărcat”, „capacitate disponibilă” și „măsurat în joc” sunt rezultate diferite. Raportați pe care ați observat-o.
