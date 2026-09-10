<!-- nv-language-navigation:start -->
🌐 [English](../../../installation.md) | [Français](../../../installation.fr.md) · [NV Laboratory](../README.md)

<details>
<summary>🌐 Language · 34</summary>

[العربية](../../ar/docs/installation.md) · [বাংলা](../../bn/docs/installation.md) · [简体中文](../../zh/docs/installation.md) · [Čeština](../../cs/docs/installation.md) · [Dansk](../../da/docs/installation.md) · [Nederlands](../../nl/docs/installation.md) · [English](../../../installation.md) · [Filipino](../../fil/docs/installation.md) · [Suomi](../../fi/docs/installation.md) · [Français](../../../installation.fr.md) · [Deutsch](../../de/docs/installation.md) · [Ελληνικά](../../el/docs/installation.md) · [हिन्दी](../../hi/docs/installation.md) · [Magyar](../../hu/docs/installation.md) · [Bahasa Indonesia](../../id/docs/installation.md) · [Italiano](../../it/docs/installation.md) · [日本語](../../ja/docs/installation.md) · [한국어](../../ko/docs/installation.md) · [मराठी](../../mr/docs/installation.md) · [فارسی](../../fa/docs/installation.md) · [Polski](../../pl/docs/installation.md) · [Português](../../pt/docs/installation.md) · [ਪੰਜਾਬੀ](../../pa/docs/installation.md) · **Română** · [Русский](../../ru/docs/installation.md) · [Español](../../es/docs/installation.md) · [Kiswahili](../../sw/docs/installation.md) · [Svenska](../../sv/docs/installation.md) · [தமிழ்](../../ta/docs/installation.md) · [ไทย](../../th/docs/installation.md) · [Türkçe](../../tr/docs/installation.md) · [Українська](../../uk/docs/installation.md) · [اردو](../../ur/docs/installation.md) · [Tiếng Việt](../../vi/docs/installation.md)

[Translation policy](../../README.md)

</details>
<!-- nv-language-navigation:end -->

<!-- nv-translation-notice:start -->
> Traducere asistată automat din engleză. Numele tehnice, comenzile, URL-urile și textele legale originale sunt păstrate. Evaluarea vorbitorilor nativi este binevenită; consultați referința în limba engleză dacă formularea este neclară.
<!-- nv-translation-notice:end -->

<a id="installation-guide"></a>
# Ghid de instalare

Începeți cu [Descărcări](downloads.md), care înregistrează starea publicării și numele exacte ale activelor. Acestea sunt instrumente separate: instalați doar cele de care aveți nevoie.

> **Pentru NVRasterPulse, instalați [RTSS de la Guru3D](https://www.guru3d.com/download/rtss-rivatuner-statistics-server-download/) înainte de a deschide managerul de profil.**
> RTSS trebuie să ruleze pentru a aplica limite; nu este inclus în NV Tools.

| Instrument | Ediție instalată | Ediție portabilă | Condiție prealabilă principală |
| --- | --- | --- | --- |
| NVIDIA Profile Inspector – NV Tools Fork | NVPI-CustomNV-3.0.2.3-Setup-r2.exe | Extrageți complet NVPI ZIP | Driver NVIDIA și .NET Framework 4.8 |
| NVDriverForge | NVDriverForge-Setup.exe | NVDriverForge.exe, timp de rulare inclus | Pachetul de driver original compatibil NVIDIA pentru operațiunile de instalare |
| NVMFG Unlock40 | NVMFGUnlock40-0.1.1-Setup-x64.exe | Extrageți complet NVMFG ZIP, păstrați subfolderele | RTX 40, DLSS FG existent, furnizor exact și ajutoare .NET Framework 4.8 |
| NVRasterPulse | NVRasterPulse-0.1-win-x64-Setup.exe | Extrageți complet RP ZIP | RTSS și .NET Framework 4.8 |

<a id="download-verify-install"></a>
## Descărcați, verificați, instalați

1. În versiunea publicată aleasă, descărcați activul aplicației numite, notificările ZIP și SHA256SUMS.txt.
2. Utilizați [Exemplu SHA-256](downloads.md#sha-256), cu numele fișierului descărcat real.
3. Pentru configurare, urmați programul de instalare normal. Pentru ZIP portabil, extrageți totul într-un nou folder local de scriere; nu rulați din interiorul ZIP.
4. Deschideți propriul EXE al aplicației. Păstrați fișierele de licență/configurare/date însoțitoare.
5. Citiți instrucțiunile de utilizare ale instrumentului înainte de a activa setările sau operațiunile sistemului.

Binarele curente sunt nesemnate. Un hash potrivit confirmă octeții așteptați; nu este un certificat de securitate sau compatibilitate. Nu dezactivați protecțiile de securitate Windows doar pentru a suprima un avertisment.

Instalarea NVDF sau însoțitorul său opțional NVPI este separată de instalarea unui driver GPU. Companionul NVPI își păstrează numele instalării interne existente. Butonul RasterPulse ridicat necesită o instalare protejată la nivelul întregului sistem; alte copii RP pot fi deschise prin propriile comenzi rapide.

NVMFG este experimental și are [rezerva de licență documentată NVIDIA SDK](provenance.md). Nu este inclus niciun driver NVIDIA, furnizor/model NGX sau timp de rulare a jocului Streamline. Descărcările SDK și actualizările de joc selectate sunt operațiuni separate explicite.

<a id="language-and-updates"></a>
## Limba și actualizări

Utilizați selectorul în 34 de limbi al README pentru documentare. NVDF, NVMFG și RP au propria lor setare UI în 34 de limbi; NVPI își păstrează suportul lingvistic existent. Unele șiruri tehnice de instalare revin la engleză.

Păstrați identitatea de instalare a instrumentului atunci când actualizați. Închideți-l mai întâi și păstrați copiile de siguranță. Pentru NVMFG, închideți jocurile afectate și rezolvați recuperarea profilului în așteptare. Pentru actualizări portabile, utilizați un folder nou în loc să combinați versiunile.

<a id="removing-a-tool"></a>
## Scoaterea unui instrument

Dezinstalarea unei aplicații nu înseamnă anularea automată a setărilor acesteia.

- **NVPI:** restabiliți profilurile/setările de afișare dorite înainte de eliminare, dacă este necesar.
- **NVDF:** utilizați mai întâi recuperarea dacă doriți să restaurați modificările avansate/NVENC. Uninstall părăsește driverul grafic, setările și backup-urile.
- **NVMFG:** închideți jocurile, dezactivați/închideți controlerul, rezolvați recuperarea NVIDIA și restaurați copiile de siguranță ale jocului SDK dorite înainte de eliminare.
- **RP:** eliminați mai întâi suprascrierile de limitare prevăzute. Uninstall nu șterge capacele salvate RTSS și nici nu elimină RTSS.

Consultați fiecare [ghid de proiect](../README.md#projects) pentru locațiile și limitările exacte ale datelor sau [sprijin](support.md) dacă un pas de recuperare eșuează.
