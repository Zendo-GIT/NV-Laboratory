<!-- nv-language-navigation:start -->
🌐 [English](../../../../NVRasterPulse/README.md) | [Français](../../../../NVRasterPulse/README.fr.md) · [NV Laboratory](../README.md)

<details>
<summary>🌐 Language · 34</summary>

[العربية](../../ar/NVRasterPulse/README.md) · [বাংলা](../../bn/NVRasterPulse/README.md) · [简体中文](../../zh/NVRasterPulse/README.md) · [Čeština](../../cs/NVRasterPulse/README.md) · [Dansk](../../da/NVRasterPulse/README.md) · [Nederlands](../../nl/NVRasterPulse/README.md) · [English](../../../../NVRasterPulse/README.md) · [Filipino](../../fil/NVRasterPulse/README.md) · [Suomi](../../fi/NVRasterPulse/README.md) · [Français](../../../../NVRasterPulse/README.fr.md) · [Deutsch](../../de/NVRasterPulse/README.md) · [Ελληνικά](../../el/NVRasterPulse/README.md) · [हिन्दी](../../hi/NVRasterPulse/README.md) · [Magyar](../../hu/NVRasterPulse/README.md) · [Bahasa Indonesia](../../id/NVRasterPulse/README.md) · [Italiano](../../it/NVRasterPulse/README.md) · [日本語](../../ja/NVRasterPulse/README.md) · [한국어](../../ko/NVRasterPulse/README.md) · [मराठी](../../mr/NVRasterPulse/README.md) · [فارسی](../../fa/NVRasterPulse/README.md) · [Polski](../../pl/NVRasterPulse/README.md) · [Português](../../pt/NVRasterPulse/README.md) · [ਪੰਜਾਬੀ](../../pa/NVRasterPulse/README.md) · **Română** · [Русский](../../ru/NVRasterPulse/README.md) · [Español](../../es/NVRasterPulse/README.md) · [Kiswahili](../../sw/NVRasterPulse/README.md) · [Svenska](../../sv/NVRasterPulse/README.md) · [தமிழ்](../../ta/NVRasterPulse/README.md) · [ไทย](../../th/NVRasterPulse/README.md) · [Türkçe](../../tr/NVRasterPulse/README.md) · [Українська](../../uk/NVRasterPulse/README.md) · [اردو](../../ur/NVRasterPulse/README.md) · [Tiếng Việt](../../vi/NVRasterPulse/README.md)

[Translation policy](../../README.md)

</details>
<!-- nv-language-navigation:end -->

<!-- nv-translation-notice:start -->
> Traducere asistată automat din engleză. Numele tehnice, comenzile, URL-urile și textele legale originale sunt păstrate. Evaluarea vorbitorilor nativi este binevenită; consultați referința în limba engleză dacă formularea este neclară.
<!-- nv-translation-notice:end -->

<a id="nvrasterpulse"></a>
# NVRasterPulse

**Limite FPS per aplicație prin RivaTuner Statistics Server.**

> **Instalați mai întâi RTSS.** NVRasterPulse necesită [RivaTuner Statistics Server (RTSS), descărcat de pe Guru3D](https://www.guru3d.com/download/rtss-rivatuner-statistics-server-download/). RTSS trebuie să ruleze pentru a aplica limitele. Nu este inclus niciun program de instalare RTSS, DLL hook sau SDK.

[Descărcați 0.2 și starea](../docs/downloads.md#nvrasterpulse) · [Instalare](#installation) · [Cum funcționează limitele](#usage) · [Licență](../../../../NVRasterPulse/LICENSE)

<a id="overview-and-purpose"></a>
## Prezentare generală și scop

NVRasterPulse este o interfață compactă Windows pentru gestionarea limitelor cadrelor RTSS după numele executabilului. RTSS efectuează limitarea. NVRasterPulse gestionează valorile de profil corespunzătoare, copiile de rezervă și solicitările de reîncărcare, cu acces la tavă și opțiuni persistente.

Există pentru a face mai ușor de editat limitele exacte pentru fiecare joc fără a înlocui un întreg profil RTSS sau a deranja setările de suprapunere. Versiunea **0.2** adaugă diagnostice de configurare, un ajutor FPS, pauză, anulare și partajare a profilului.

<a id="features"></a>
## Caracteristici

- Selectați o aplicație care rulează sau adăugați manual executabilul acesteia.
- Salvați limitele FPS de la 1 la 1000, cu până la trei zecimale.
- Codificarea rațională exactă a valorilor introduse: 59.94 devine 2997/50.
- Configurație Front Edge Sync (`SyncLimiter=1`) cu așteptare activă (`PassiveWait=0`).
- Actualizări de profil per-executabil, backup-uri automate și scrieri atomice.
- Eliminarea suprascrierilor limitatorului, păstrând în același timp alt conținut de profil.
- Detectarea instalării RTSS, selectarea manuală a căii și lansarea/reîncărcarea explicită.
- Operare cu tavă cu o singură instanță, pornire instalată opțională, 34 de limbi și patru teme.
- Separați acțiunile de ieșire normală și **Ieșire + RTSS**.

<a id="compatibility"></a>
## Compatibilitate

| Cerință | Detalii |
| --- | --- |
| Sistem | Windows 10/11 x64 |
| Timp de rulare | [.NET Framework 4.8](https://dotnet.microsoft.com/en-us/download/dotnet-framework/net48), instalat separat dacă este necesar |
| Software-ul necesar | RTSS cu `RTSS.exe`, un director `Profiles` potrivit și suport pentru profil/reîncărcare compatibil |
| GPU | Compatibilitatea RTSS determină limitatorul; acest manager de profil nu necesită o anumită generație RTX |
| Permisiuni | Aplicația curentă solicită acces de administrator; folderul de profil RTSS selectat trebuie să fie accesibil |
| Jocuri | Depinde de suportul de conectare RTSS și de restricțiile fiecărui joc; fără garanție anti-cheat |

Nicio versiune minimă specifică RTSS nu a fost certificată pentru fiecare funcție de către acest audit hub. Utilizați distribuția curentă oficială și raportați versiunea exactă dacă o cheie de profil/reîncărcare nu funcționează. RTSS instalat-dar oprit trece verificarea instalării; trebuie apoi pornit pentru limitarea efectivă.

<a id="installation"></a>
## Instalare

1. **[Descărcați și instalați RTSS de la Guru3D](https://www.guru3d.com/download/rtss-rivatuner-statistics-server-download/).**
2. Deschideți [NVRasterPulse descărcări](../docs/downloads.md#nvrasterpulse) și verificați disponibilitatea lansării.
3. Descărcați `NVRasterPulse-0.2-win-x64-Setup.exe` sau `NVRasterPulse-0.2-win-x64-portable.zip`, plus notificările/sumele de verificare.
4. Comparați SHA-256. Rulați Setup sau extrageți întregul ZIP portabil într-un folder local care poate fi scris.
5. Deschideți `NVRasterPulse.exe`. Dacă RTSS lipsește, utilizați **Descărcați RTSS**, instalați-l, apoi **Verificați din nou** sau selectați manual `RTSS.exe`.
6. Porniți RTSS folosind comanda sa rapidă normală sau butonul RTSS al lui NVRasterPulse dacă este oprit.

Dezactivarea mementoului opțional nu omite verificarea cerințelor preliminare. O pornire silențioasă a tăvii Windows așteaptă până când se deschide fereastra principală înainte de a afișa această verificare. Configurarea instalează numai NVRasterPulse. EXE-urile sale sunt nesemnate.

<a id="usage"></a>
## Utilizare

1. Selectați aplicația care rulează sau navigați la jocul său EXE.
2. Introduceți o limită între 1 și 1000 FPS, inclusiv o valoare fracțională dacă este necesar.
3. Salvați și verificați rezultatul raportat. NVRasterPulse actualizează profilul RTSS al acelui executabil și solicită o reîncărcare.
4. Confirmați că RTSS rulează și verificați comportamentul în jocul dorit.

Profilurile sunt introduse după **nume executabil**, cum ar fi `Game.exe.cfg`. Două foldere diferite care conțin `Game.exe` au același profil RTSS; stocarea traseului complet nu înlătură această coliziune.

Salvarea utilizează Front Edge Sync și așteptarea activă. Așteptarea activă poate crește utilizarea CPU. Câmpurile alternative `LimitTime` sunt neutralizate. Comentariile existente, setările de suprapunere și `EnableHooking=0` sunt păstrate. Profilul global RTSS nu este modificat.

Folosiți acțiunea de gunoi pentru a elimina suprascrierile limitatorului NVRasterPulse. Nu șterge întregul profil RTSS. O limită moștenită de la RTSS Global sau de la un alt instrument se poate aplica în continuare ulterior.

**Închidere și ieșire:** fereastra principală se poate ascunde în tavă. Normal **Ieșire** lasă RTSS în funcțiune și limitele salvate intacte. **Ieșire + RTSS** solicită o închidere normală a procesului RTSS care se potrivește în sesiunea curentă, așteaptă până la opt secunde și nu îl forțat. Limitele stocate rămân în ambele cazuri.

Limba și tema sunt selectate în aplicație. Pornirea la conectarea Windows este opțională și este destinată unei copii instalate. Butonul de informații explică acțiunile comune.

<a id="diagnostics-and-profile-tools"></a>
## Instrumente de diagnosticare și profil

Deschideți meniul de acțiuni pentru instrumentele suplimentare. Ele păstrează RTSS Global, setările de suprapunere și excluderile.

**Diagnosticare:** inspectați limitele locale/eficiente, RTSS oprit, un executabil lipsă, nicio fereastră detectată, conectarea dezactivată, moștenirea, limitele întrerupte, setările concurente și numele executabilelor duplicat. Această verificare numai în citire descrie configurația; nu dovedește că un joc este agățat de RTSS și nici nu măsoară FPS.

**FPS helper:** selectați afișajul și declarați dvs. VRR/G-Sync, V-Sync, Reflex și Frame Generation. Frecvența de reîmprospătare rotunjită provine de la Windows. Dacă Reflex sau Frame Generation este activ sau necunoscut, nu este oferit niciun plafon automat. Pentru VRR cu V-Sync activat și Reflex/FG dezactivat, euristica scade cel puțin 3 FPS sau aproximativ 2% din rata de reîmprospătare. Acesta nu este un optim măsurat. Aplicarea sugestiei umple schița; **Salvare** rămâne o acțiune separată.

**Întrerupeți și reluați:** suspendați limita programului selectat, apoi restabiliți câmpurile de limitare anterioare. Modificările contradictorii ale unui alt instrument împiedică un CV ambiguu. Ascunderea unei intrări nu întrerupe limita sa.

**Anulați:** restabiliți ultima modificare a celor șase câmpuri de limitare gestionate pentru programul respectiv. Există un singur nivel; acest lucru nu restabilește tot RTSS. Schimbările externe contradictorii sunt refuzate. Copiile de rezervă ale fișierelor rămân separate.

**Partajați profiluri:** exportați profilurile selectate într-un fișier `.nvrp`. Import afișează o previzualizare și lasă majusculele existente nebifate în mod prestabilit. Fișierul conține doar nume executabile, limite și stări, fără căi sau scripturi absolute. Examinați selecția dvs. și aplicați. O eroare I/O poate lăsa unele profiluri deja aplicate; rezultatul le identifică și fiecare își păstrează anularea. Nume executabile identice se adresează în continuare aceluiași profil RTSS.

**Preferate și intrări ascunse:** fixați mai întâi programele utile, ascundeți intrările nedorite și restaurați-le în dialogul dedicat. Aceste alegeri persistă. Un favorit închis nu apare ca o aplicație care rulează.

<a id="screenshots"></a>
## Capturi de ecran

![Previzualizarea ferestrei principale NVRasterPulse](../../../../assets/screenshots/nvrasterpulse-0.1-preview.png)

Interfața de utilizare franceză existentă 0.1 este redată cu exemple de nume executabile și o valoare de 176 FPS. RTSS este afișat oprit; aceasta este o ilustrare a interfeței, nu un limitator de funcționare sau o măsurare a latenței. [Proveniența imaginii](../assets/README.md).

<a id="update-and-uninstall"></a>
## Actualizați și dezinstalați

Ieșiți din NVRasterPulse, descărcați și verificați noua versiune, apoi executați configurarea acesteia sau extrageți portabilul într-un folder nou. Păstrați setările și backup-urile RTSS. Actualizările RTSS sunt separate și provin de la Guru3D.

Pentru a elimina o copie instalată, utilizați Windows **Installed apps**. Pentru portabil, ieșiți, apoi eliminați folderul extras atunci când copiile de siguranță sunt în siguranță. Limitele salvate RTSS nu sunt eliminate prin dezinstalarea NVRasterPulse: eliminați mai întâi suprascrierile de limitare dorite. RTSS are propriul său dezinstalare.

Stat local: `%LOCALAPPDATA%\NVRasterPulse`. Backup-uri automate RTSS: `%LOCALAPPDATA%\NVRasterPulse\Backups\RTSS`. O locație mai veche `%LOCALAPPDATA%\RTSSProfileBridge` poate fi citită pentru migrare. Aceste fișiere pot conține căi executabile personale și nu trebuie postate public.

<a id="known-limitations"></a>
## Limitări cunoscute

- RTSS efectuează capacul. O valoare salvată sau o solicitare de reîncărcare reușită nu este un rezultat măsurat în timpul cadrului.
- Executabile cu același nume partajează un profil.
- Un alt limitator global/per-joc poate afecta rezultatul; dezactivarea suprascrierii locale nu elimină o limită moștenită.
- Un cârlig RTSS dezactivat în mod deliberat rămâne dezactivat.
- Așteptarea activă are un compromis CPU/putere.
- Fără joc universal, anti-cheat sau validare end-to-end a latenței.
- Motorul de limitator independent experimental anterior nu este compilat sau livrat.
- Backup-urile automate nu implică o interfață completă de backup-restaurare cu un singur clic.

<a id="troubleshooting"></a>
## Depanare

| Simptom | Acțiune |
| --- | --- |
| Cerința RTSS rămâne deschisă | Selectați `RTSS.exe` real și folderul Profiluri potrivit, apoi Verificați din nou. |
| Limită salvată, dar fără efect | Porniți RTSS; verificați EXE/profilul corect de joc, permisiunile de cârlig și alte limitatoare. |
| Salvarea eșuează | Verificați permisiunile folderului și păstrați eroarea/backup-ul afișat. |
| Limita rămâne după îndepărtare | Inspectați RTSS Global și alte instrumente; acțiunea de gunoi elimină doar suprascrierile limitatorului local. |
| Două jocuri primesc aceeași limită | Verificați dacă numele fișierelor executabile ale acestora sunt identice. |
| Ieșire + RTSS lasă RTSS deschis | Închideți RTSS în mod normal; această comandă evită în mod deliberat încetarea forțată. |

Dacă restaurați manual o copie de rezervă RTSS, închideți mai întâi RTSS și păstrați profilul curent înainte de a-l înlocui cu backup-ul dorit. Acest lucru poate suprascrie editările de profil care nu au legătură; inspectați dosarul și data. [Asistență comună](../docs/support.md).

<a id="faq"></a>
## Întrebări frecvente

**Am nevoie și de MSI Afterburner?** NVRasterPulse necesită RTSS; nu depinde de aplicația Afterburner. Urmați opțiunile de instalare ale distribuitorului RTSS.

**Pot folosi acest lucru fără a rula RTSS?** Puteți gestiona profilurile odată ce este detectată o instalare, dar RTSS trebuie să ruleze pentru limitare.

**Închiderea sau dezinstalarea elimină capacele?** Nu. Eliminați limitatorul dorit anulează în mod explicit înainte de a elimina NVRasterPulse.

**Este un fork al RTSS?** Nu. Este un manager de profil independent; nu este încorporată nicio sursă sau executabil RTSS.

<a id="upstream-modifications-and-credits"></a>
## Upstream, modificari si credite

Depozitul de dezvoltare provine de la [Orbmu2k's NVIDIA Profile Inspector](https://github.com/Orbmu2k/nvidiaProfileInspector). Paletele sale MIT/resursele UI sunt creditate. Serviciile de gestionare a profilului, codificarea fracțiilor, backup-urile, puntea de reîncărcare RTSS, comportamentul tăvii, ghidul de cerințe preliminare, limbile și pictograma specifică aplicației au fost dezvoltate/adaptate de 禅堂 Zendo (RevoluSound Team).

RTSS este dezvoltat de **Unwinder** și distribuit separat prin Guru3D. NVRasterPulse apelează `UpdateProfiles` din DLL-ul hook instalat selectat; niciun RTSS SDK sau binar cârlig nu este redistribuit. Programul de instalare folosește Inno Setup 7.1.0 nemodificat cu scripturi/traduceri adaptate și un bootstrap de proiect.

[Proveniență deplină](../docs/provenance.md) · [Masă terță parte](../THIRD_PARTY_NOTICES.md)

<a id="license"></a>
## Licență

Pachetul distribuie în mod explicit NVRasterPulse sub [Licență MIT](../../../../NVRasterPulse/LICENSE) furnizat, păstrând Copyright (c) 2016 Orbmu2k. Sursa aplicației este menținută în mod privat; MIT nu necesită publicarea sursei modificate. RTSS și Windows/.NET rămân în condițiile proprii. [Notificări complete](LICENSES/README.md).

Independent de NVIDIA Corporation, MSI și RTSS; nesponsorizat sau susținut oficial de aceștia. Numele produselor rămân mărci comerciale ale proprietarilor lor.
