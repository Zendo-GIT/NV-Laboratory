<!-- nv-language-navigation:start -->
🌐 [English](../../../../NVIDIA-Profile-Inspector/README.md) | [Français](../../../../NVIDIA-Profile-Inspector/README.fr.md) · [NV Laboratory](../README.md)

<details>
<summary>🌐 Language · 34</summary>

[العربية](../../ar/NVIDIA-Profile-Inspector/README.md) · [বাংলা](../../bn/NVIDIA-Profile-Inspector/README.md) · [简体中文](../../zh/NVIDIA-Profile-Inspector/README.md) · [Čeština](../../cs/NVIDIA-Profile-Inspector/README.md) · [Dansk](../../da/NVIDIA-Profile-Inspector/README.md) · [Nederlands](../../nl/NVIDIA-Profile-Inspector/README.md) · [English](../../../../NVIDIA-Profile-Inspector/README.md) · [Filipino](../../fil/NVIDIA-Profile-Inspector/README.md) · [Suomi](../../fi/NVIDIA-Profile-Inspector/README.md) · [Français](../../../../NVIDIA-Profile-Inspector/README.fr.md) · [Deutsch](../../de/NVIDIA-Profile-Inspector/README.md) · [Ελληνικά](../../el/NVIDIA-Profile-Inspector/README.md) · [हिन्दी](../../hi/NVIDIA-Profile-Inspector/README.md) · [Magyar](../../hu/NVIDIA-Profile-Inspector/README.md) · [Bahasa Indonesia](../../id/NVIDIA-Profile-Inspector/README.md) · [Italiano](../../it/NVIDIA-Profile-Inspector/README.md) · [日本語](../../ja/NVIDIA-Profile-Inspector/README.md) · [한국어](../../ko/NVIDIA-Profile-Inspector/README.md) · [मराठी](../../mr/NVIDIA-Profile-Inspector/README.md) · [فارسی](../../fa/NVIDIA-Profile-Inspector/README.md) · [Polski](../../pl/NVIDIA-Profile-Inspector/README.md) · [Português](../../pt/NVIDIA-Profile-Inspector/README.md) · [ਪੰਜਾਬੀ](../../pa/NVIDIA-Profile-Inspector/README.md) · **Română** · [Русский](../../ru/NVIDIA-Profile-Inspector/README.md) · [Español](../../es/NVIDIA-Profile-Inspector/README.md) · [Kiswahili](../../sw/NVIDIA-Profile-Inspector/README.md) · [Svenska](../../sv/NVIDIA-Profile-Inspector/README.md) · [தமிழ்](../../ta/NVIDIA-Profile-Inspector/README.md) · [ไทย](../../th/NVIDIA-Profile-Inspector/README.md) · [Türkçe](../../tr/NVIDIA-Profile-Inspector/README.md) · [Українська](../../uk/NVIDIA-Profile-Inspector/README.md) · [اردو](../../ur/NVIDIA-Profile-Inspector/README.md) · [Tiếng Việt](../../vi/NVIDIA-Profile-Inspector/README.md)

[Translation policy](../../README.md)

</details>
<!-- nv-language-navigation:end -->

<!-- nv-translation-notice:start -->
> Traducere asistată automat din engleză. Numele tehnice, comenzile, URL-urile și textele legale originale sunt păstrate. Evaluarea vorbitorilor nativi este binevenită; consultați referința în limba engleză dacă formularea este neclară.
<!-- nv-translation-notice:end -->

<a id="nvidia-profile-inspector--nv-tools-fork"></a>
# NVIDIA Profile Inspector – NV Tools Fork

**Un fork independent de [NVIDIA Profile Inspector de la Orbmu2k](https://github.com/Orbmu2k/nvidiaProfileInspector), cu comenzi de afișare adăugate.** Fostul nume al proiectului: **NVPI Custom**.

[Descărcare și stare de lansare](../docs/downloads.md#nvidia-profile-inspector) · [Instalare](#installation) · [În amonte și schimbări](#upstream-and-changes) · [Licență](../../../../NVIDIA-Profile-Inspector/LICENSE)

<a id="overview"></a>
## Prezentare generală

Aplicația editează profilurile driverului NVIDIA, inclusiv setările pentru fiecare aplicație. Acest fork adaugă, de asemenea, un editor **Ecran** pentru afișajul activ Windows: rezoluție, rata de reîmprospătare, setări de culoare de ieșire, HDR și asocieri de profil ICC/WCS instalate.

Există pentru a aduce comenzile de afișare aferente în editorul de profil și pentru a face rezultatele previzualizării, confirmării și restaurării mai clare. Nu stabilește noi capabilități hardware.

Primul candidat este **3.0.2.3**, folosind versiunea însoțitoare autonomă curățată din 9 septembrie 2026. Executabilul său existent rămâne `nvidiaProfileInspector.exe`; instalatorul și unele etichete interne spun încă `NVPI Custom NV`. Titlul public de mai sus identifică fork fără a schimba identitatea instalării sau a pretinde că este versiunea oficială a Orbmu2k.

<a id="features"></a>
## Caracteristici

- Navigare în profil existent în amonte, asocieri de aplicații, modificări ale setărilor și import/export de profil.
- Dialog **Ecran** pentru afișaj, mod, Hz, RGB/YCbCr, adâncime de culoare, interval și colorimetrie.
- Controlul Windows HDR și selectarea asocierii ICC/WCS instalată.
- O previzualizare a afișajului de 15 secunde cu **Păstrare** / **Revenire** și restabilire timeout.
- Citire înapoi a modificărilor modului/HDR și a raportat erori de restaurare.
- Raportare separată pentru HDR, SDR cu ACM/WCG și adâncimea culorii semnalului.
- Un lansator NVRasterPulse pentru o copie eligibilă instalată separat.

<a id="compatibility"></a>
## Compatibilitate

| Cerință | Detalii |
| --- | --- |
| Sistem | Windows 10/11 x64 cu un driver compatibil NVIDIA |
| Timp de rulare | [.NET Framework 4.8](https://dotnet.microsoft.com/en-us/download/dotnet-framework/net48), furnizat de Windows sau instalat separat |
| Permisiuni | Editorul solicită acces de administrator când este deschis |
| Afișări | Modurile reale și combinațiile de culori depind de GPU, driver, afișaj, cablu și API-uri Windows |
| Instrumente opționale | NVRasterPulse pentru managementul limitelor RTSS; nici el, nici RTSS nu sunt necesare pentru editorul de ecran |
| Limbi | Configurare: selector în 34 de limbi. Editorul își păstrează suportul lingvistic existent. |

Nu există un minim de driver universal verificat sau o matrice de suport pentru fiecare GPU. Opțiunile bpc disponibile ale casetei de dialog sunt cereri, nu combinații certificate. Comenzile moderne HDR și sistemul de rezervă mai vechi Windows au capacități diferite.

<a id="installation"></a>
## Instalare

1. Deschideți [pagina de descărcare](../docs/downloads.md#nvidia-profile-inspector) și verificați starea publicării.
2. Descărcați Configurarea sau materialul portabil și comparați SHA-256 al acestuia cu manifestul de lansare.
3. Pentru configurare, rulați `NVPI-CustomNV-3.0.2.3-Setup-r2.exe`, selectați o limbă și urmați programul de instalare. Își creează propria scurtătură și dezinstalare.
4. Pentru portabil, extrageți fișierul ZIP complet într-un folder nou care poate fi scris. Păstrați `Reference.xml`, configurația EXE și toate notificările lângă executabil.
5. Lansați `nvidiaProfileInspector.exe`.

Instalarea editorului singură nu aplică un profil sau instalează un driver GPU. Companionul se instalează separat, nu preia asocierile `.nip` și nu activează pornirea la conectare. Binarele existente sunt nesemnate.

<a id="usage"></a>
## Utilizare

**Reviziunea 2 a instalatorului** adaugă același selector nativ în 34 de limbi ca și celelalte instrumente, cu navigare mouse/tastatură, aspect deschis/întunecat și anulare. Alegerea se aplică setării; nu traduce editorul NVPI. Un argument explicit `/LANG=fr` sau un mod silențios ocolește selecția pentru apelanții care oferă deja o limbă.

**Profiluri de șofer:** selectați un profil, exportați o copie de rezervă, apoi editați numai setările dorite și aplicați-le. Asociațiile de aplicații determină ce joc primește un profil. O valoare stocată nu este dovada că fiecare șofer sau joc o folosește.

**Comenzile afișajului:** deschideți **Ecranul**, alegeți afișajul și valorile solicitate, apoi începeți previzualizarea. Verificați imaginea înainte de a alege **Păstrați** în 15 secunde. Folosiți **Revertire**, închideți confirmarea sau lăsați-o să expire pentru a solicita restaurarea. Citiți orice mesaj de eșec: doar un apel API reușit nu este o dovadă a restaurării.

O selecție ICC modifică o asociere de profil instalată; nu generează, calibrează sau redistribuie un fișier ICC. HDR, ACM/WCG, RGB/YCbCr și bpc descriu diferite aspecte ale conductei. Nu este furnizat niciun comutator ACM independent nou.

**NVRasterPulse:** butonul din bara de instrumente acceptă o instalare înregistrată separat la nivelul întregului sistem de sub Fișiere de program cu drept de proprietate și permisiuni protejate. O copie portabilă sau o cale care poate fi scrisă de utilizator/legată poate fi refuzată de acest lansator ridicat. În acest caz, deschideți NVRasterPulse folosind propria sa comandă rapidă. [Instalați RTSS separat](https://www.guru3d.com/download/rtss-rivatuner-statistics-server-download/) pentru a utiliza NVRasterPulse.

<a id="screenshots"></a>
## Capturi de ecran

![NVPI selector de limbă pentru versiunea 2 de configurare](../../../../assets/screenshots/nvpi-setup-r2-language.png)

Selector de configurare reală în franceză, capturat în timpul unui test izolat și apoi anulat. Acesta arată instalatorul; editorul își păstrează interfața și dialogul Ecran.

<a id="update-and-uninstall"></a>
## Actualizați și dezinstalați

Închideți editorul înainte de a actualiza. Păstrați profilurile exportate și descărcați noua versiune fork; instalați peste aceeași identitate însoțitoare sau extrageți fișiere portabile într-un folder nou. Nu amestecați un vechi `Reference.xml` cu un executabil nou. Suprimarea verificării actualizării în amonte aparține acestui fork.

Pentru o copie instalată, utilizați Windows **Installed apps** și dezinstalarea acestuia. Pentru portabil, închideți-l și eliminați folderul extras atunci când exporturile dvs. sunt în siguranță. Eliminarea editorului **nu** anulează editările profilului driverului, preferințele de afișare, NVRasterPulse sau RTSS. Restabiliți setările dorite înainte de eliminare.

<a id="known-limitations"></a>
## Limitări cunoscute

- Confirmarea de 15 secunde nu este un supraveghetor pentru fiecare accident de șofer, pierdere de putere sau oprire forțată.
- Unele combinații de culoare/adâncime/împrospătare returnează `NVAPI_NOT_SUPPORTED`.
- Citirea software-ului nu măsoară adâncimea de biți a panoului, acuratețea culorii sau latența.
- Setările ecranului afectează afișarea curentă a Windows; acest dialog nu creează presetări de afișare pentru fiecare joc.
- Fără performanță, anti-cheat sau compatibilitate universală HDR.

<a id="troubleshooting"></a>
## Depanare

| Simptom | Acțiune |
| --- | --- |
| Eroare de rulare la lansare | Verificați actualizările Windows și .NET Framework 4.8; utilizați pachetul complet. |
| Modul de afișare solicitat a fost respins | Reveniți și testați un mod oferit de Windows/NVIDIA pentru acel afișaj. Citiți eroarea exactă și evitați modificările repetate ale orbului. |
| HDR sau culoarea revine la starea veche | Verificați dacă o altă operațiune a eșuat și a declanșat restaurarea; distinge HDR de ACM. |
| Butonul NVRasterPulse refuză o cale | Lansați propria sa comandă rapidă; acest buton necesită o instalare protejată la nivelul întregului sistem. |
| O modificare rămâne după dezinstalare | Restabiliți profilul NVIDIA exportat sau setările de afișare Windows dorite; dezinstalarea nu este o revenire a setărilor. |

Consultați [îndrumări de sprijin partajate](../docs/support.md) înainte de a trimite jurnalele.

<a id="faq"></a>
## Întrebări frecvente

**Este acest software oficial NVIDIA sau versiunea oficială a lui Orbmu2k?** Nu. Este un fork independent; autorul din amonte și licența MIT rămân creditate.

**NVDriverForge necesită acest editor?** Nu. Presetarea opțională Custom NV a NVDriverForge utilizează propria sa integrare. Instalarea editorului este o alegere separată.

**Este RTSS obligatoriu pentru acest fork?** Nu. RTSS este obligatoriu pentru limitatorul FPS al lui NVRasterPulse, nu pentru editare de profil sau ecran.

**Unde este sursa?** Sursa aplicației modificată este menținută în mod privat. Sunt furnizate notificarea MIT și depozitul în amonte; MIT nu necesită publicarea sursei modificate.

<a id="upstream-and-changes"></a>
## În amonte și schimbări

În amonte: [Orbmu2k/nvidiaProfileInspector](https://github.com/Orbmu2k/nvidiaProfileInspector), comitere referință `592d962cca8827efe8859461a84267755595064a`. [Descărcări originale](https://github.com/Orbmu2k/nvidiaProfileInspector/releases).

Moștenit: editor de profil, interoperabilitate NVAPI, date de referință, resurse și teme UI. Servicii de afișare adăugate sau adaptate 禅堂 Zendo (RevoluSound Team), tranzacții HDR/ICC, confirmare/citire în 15 secunde, aspect al barei de instrumente și comportament de lansare RasterPulse. Companionul curățat exclude punctele de intrare de simulare/testare de dezvoltare, utilizează un lansator extern protejat și oferă un program de instalare separat. Vechiul pachet de dezvoltare combinat NVPI/RasterPulse nu este candidatul în acest hub.

[Proveniența fișierului detaliat](../docs/provenance.md) · [Aviz original fork](../../../../NVIDIA-Profile-Inspector/LICENSES/ORIGINAL-FORK-NOTICE.txt)

<a id="credits-and-license"></a>
## Credite și licență

Drepturi de autor (c) 2016 Orbmu2k. [Licență MIT](../../../../NVIDIA-Profile-Inspector/LICENSE) furnizat este păstrat. Adaptări și ambalare: 禅堂 Zendo (RevoluSound Team). Programul de instalare folosește Inno Setup; Windows și .NET Framework rămân externe. [Notificări aplicabile complete](LICENSES/README.md).

Independent de, nu este sponsorizat de și nu este aprobat oficial de NVIDIA Corporation. Mărcile comerciale rămân la proprietarii lor respectivi.
