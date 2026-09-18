<!-- nv-language-navigation:start -->
🌐 [English](../../../../NVDriverForge/README.md) | [Français](../../../../NVDriverForge/README.fr.md) · [NV Laboratory](../README.md)

<details>
<summary>🌐 Language · 34</summary>

[العربية](../../ar/NVDriverForge/README.md) · [বাংলা](../../bn/NVDriverForge/README.md) · [简体中文](../../zh/NVDriverForge/README.md) · [Čeština](../../cs/NVDriverForge/README.md) · [Dansk](../../da/NVDriverForge/README.md) · [Nederlands](../../nl/NVDriverForge/README.md) · [English](../../../../NVDriverForge/README.md) · [Filipino](../../fil/NVDriverForge/README.md) · [Suomi](../../fi/NVDriverForge/README.md) · [Français](../../../../NVDriverForge/README.fr.md) · [Deutsch](../../de/NVDriverForge/README.md) · [Ελληνικά](../../el/NVDriverForge/README.md) · [हिन्दी](../../hi/NVDriverForge/README.md) · [Magyar](../../hu/NVDriverForge/README.md) · [Bahasa Indonesia](../../id/NVDriverForge/README.md) · [Italiano](../../it/NVDriverForge/README.md) · [日本語](../../ja/NVDriverForge/README.md) · [한국어](../../ko/NVDriverForge/README.md) · [मराठी](../../mr/NVDriverForge/README.md) · [فارسی](../../fa/NVDriverForge/README.md) · [Polski](../../pl/NVDriverForge/README.md) · [Português](../../pt/NVDriverForge/README.md) · [ਪੰਜਾਬੀ](../../pa/NVDriverForge/README.md) · **Română** · [Русский](../../ru/NVDriverForge/README.md) · [Español](../../es/NVDriverForge/README.md) · [Kiswahili](../../sw/NVDriverForge/README.md) · [Svenska](../../sv/NVDriverForge/README.md) · [தமிழ்](../../ta/NVDriverForge/README.md) · [ไทย](../../th/NVDriverForge/README.md) · [Türkçe](../../tr/NVDriverForge/README.md) · [Українська](../../uk/NVDriverForge/README.md) · [اردو](../../ur/NVDriverForge/README.md) · [Tiếng Việt](../../vi/NVDriverForge/README.md)

[Translation policy](../../README.md)

</details>
<!-- nv-language-navigation:end -->

<!-- nv-translation-notice:start -->
> Traducere asistată automat din engleză. Numele tehnice, comenzile, URL-urile și textele legale originale sunt păstrate. Evaluarea vorbitorilor nativi este binevenită; consultați referința în limba engleză dacă formularea este neclară.
<!-- nv-translation-notice:end -->

<a id="nvdriverforge"></a>
# NVDriverForge

**Pregătiți o instalare a driverului NVIDIA cu opțiuni clare pentru componente și setări opționale.**

[Descărcați 0.1.4 și starea](../docs/downloads.md#nvdriverforge) · [Instalare](#installation) · [Credite](#credits-and-upstream) · [Licență](../../../../NVDriverForge/LICENSE)

<a id="overview-and-purpose"></a>
## Prezentare generală și scop

NVDriverForge vă ghidează printr-un pachet original de driver NVIDIA: alegeți driverul, inspectați componentele acestuia, revizuiți ajustările opționale, apoi confirmați instalarea. Există pentru a face aceste alegeri ușor de înțeles și pentru a menține instalarea, operațiunile privilegiate și informațiile de recuperare împreună.

Este o aplicație dezvoltată independent, inspirată parțial de fluxul de lucru NVCleanstall. Nu include NVCleanstall sau revendică paritatea completă a caracteristicilor.

<a id="features"></a>
## Caracteristici

- NVIDIA Game Ready / Studio căutare și descărcări; Descoperire opțională a remedierii rapide cu rezervă manuală.
- Analiza pachetului original, hashuri, semnături NVIDIA, manifeste și intrări compatibile INF.
- Selectarea componentelor cu dependențe și păstrarea componentelor necunoscute.
- Versiunea 0.1.4 păstrează componentele opționale NVIDIA selectate care pot fi ignorate și exclude de la descoperire numai componentele verificate neverificate. Timpurile de rulare opționale deja actuale sau inaplicabile nu mai sunt forțate ca componente critice.
- Ștergeți rezumatele erorilor de instalare și accesați jurnalele detaliate în toate cele 34 de limbi.
- Verificări de pregătire, confirmare explicită, export din magazinul de drivere și backup nativ al profilului NVIDIA înainte de instalare.
- Setări avansate opționale, cu verificări preflight, jurnale și recuperare în funcție de conflict.
- Opțional **Custom NV** presetat cu opțiuni și explicații numite, inclusiv o selecție separată a puterii SILK și verificări de compatibilitate.
- Descărcări opționale de corecție NVENC pentru versiunea exactă; comiterea sursă și octeții țintă sunt verificați.
- O instalare separată, opțională, a Profile Inspector fork din ecranul Instrumente.
- Ghid de componente, preferințe reutilizabile, kituri de drivere, rapoarte de asistență locală și actualizări opționale ale aplicațiilor.
- 34 de limbi de interfață și patru teme.

Opțiunile avansate disponibile se referă la MPO, indicatorul DLSS, Ansel, somn audio NVIDIA, MSI, politica/prioritatea de întrerupere, HDCP, pornirea containerului de afișare și un serviciu de telemetrie moștenit eligibil. Fiecare are propriile premise și efecte; acestea nu sunt îmbunătățiri universale de performanță.

<a id="compatibility"></a>
## Compatibilitate

| Cerință | Detalii |
| --- | --- |
| Sistem | Windows 10 versiunea 19041 sau mai nouă / Windows 11, x64 |
| GPU/driver | Pachet NVIDIA compatibil și hardware detectat; Căutarea automată a catalogului acoperă în primul rând modelele cunoscute GeForce |
| Timp de rulare | .NET 8 / WPF 8.0.31 inclus în pachetul autonom pregătit |
| Privilegii | UI/Configurare normală pentru fiecare utilizator; instalarea driverului și modificările sistemului solicită acces de administrator |
| Rețea | Necesar pentru căutarea/descărcările online NVIDIA și solicitările explicite NVENC din amonte; poate fi selectat un driver original local |
| Instrumente incluse | 7-Zip 26.03 nemodificat, notificări de rulare, opțional MIT Profile Inspector însoțitor |
| Însoțitor opțional | .NET Framework 4.8 pentru Profile Inspector fork separat |

Nicio versiune minimă arbitrară a driverului nu acoperă toate caracteristicile. Căutarea multi-GPU trebuie să se potrivească cu fiecare GPU detectat. Modelele neacceptate/profesionale pot necesita selectarea manuală a driverului. Programul de instalare al lui NVIDIA rămâne autoritatea finală pentru hardware/OS.

<a id="installation"></a>
## Instalare

1. Vizitați [descărcări](../docs/downloads.md#nvdriverforge) și confirmați că Versiunea este publicată.
2. Alegeți `NVDriverForge-Setup.exe` pentru instalare sau `NVDriverForge.exe` pentru utilizare portabilă.
3. Comparați SHA-256 cu `SHA256SUMS.txt` al versiunii.
4. Rulați Setup pentru o instalare per utilizator și dezinstalare standard sau plasați EXE portabil într-un folder care poate fi scris și deschideți-l.

Portabilul include timpul de rulare și programul de instalare opțional. Instalarea NVDriverForge nu instalează un driver GPU. EXE-urile sale sunt momentan nesemnate.

<a id="usage"></a>
## Utilizare

1. **Driver:** descărcați de pe NVIDIA sau selectați un EXE original de instalare NVIDIA. Lasă analiza să se termine.
2. **Componente:** examinați descrierile și dependențele necesare. Componentele necunoscute sunt păstrate.
3. **Ajustări:** lăsați opțiunile nedorite neschimbate. Citiți efectele și compromisurile înainte de a selecta orice.
4. **Revizuire:** verificați driverul exact, componentele și operațiunile opționale, apoi confirmați instalarea.
5. Acceptați UAC numai pentru operațiunea pe care ați ales-o. Păstrați instrucțiunile de recuperare a jobului protejat.
6. Dacă noul driver necesită repornire, urmați starea raportată. Operațiunile amânate necesită reluare explicită după acea repornire.

Custom NV pornește neschimbat. Alegeți valori individuale denumite sau examinați presetarea furnizată și excluderile acesteia. Cele două câmpuri interne informaționale ale sale nu sunt scrise independent. Setările sunt aplicate numai în fluxul de lucru verificat pentru șofer nou, niciodată prin deschiderea unei previzualizări. Instalarea editorului separat NVPI nu este necesară.

Lucrarea opțională NVENC descarcă date compatibile dintr-un comit keylase fixat. Modifică două DLL-uri de driver și le invalidează semnăturile; poate fi refuzat de Windows, codificatoare, DRM sau anti-cheat. Nu există astfel de date sau DLL NVIDIA încorporate în NVDriverForge. [Limitele de proveniență și licențiere](../docs/provenance.md).

Preferințele controlează limba, tema și verificările opționale de actualizare a utilizatorului instalat. Portabilul nu creează sarcina de verificare a fundalului instalată. Instrumentele și recuperarea sunt separate de cei patru pași de instalare.

<a id="backup-and-diagnostic-tools"></a>
## Instrumente de backup și diagnosticare

**Înainte de instalare:** verificările de pregătire acoperă semnătura pachetului, GPU-urile, spațiul de lucru estimat/spațiul de rezervă, repornirea în așteptare și instalatorii concurenți. Muncitorul ridicat le repetă. Procesele concurente nu sunt niciodată oprite automat. Backup-ul nativ al bazei de date de profil NVIDIA trebuie să reușească înainte de a începe configurarea NVIDIA; exportul driver-store este o copie de rezervă separată.

**Opțiuni reutilizabile:** ghidul de componente pune patru întrebări despre jocuri, audio, NVIDIA App și înregistrare. Examinați sugestiile acestuia; componentele necesare, necunoscute și de dependență rămân protejate. Exportați preferințele, apoi previzualizați și revalidați-le în raport cu pachetul selectat la import. Consimțământurile, operațiunile de repornire, căile de program și încărcăturile utile de corecție nu sunt importate.

**Setul de driver:** exportați un `.nvdfkit.zip` pentru a păstra împreună programul de instalare NVIDIA original semnat, opțiunile, hashe-urile și instrucțiunile. Transportați `NVDriverForge.exe` separat. Importați kitul în Instrumente, examinați previzualizarea, apoi utilizați fluxul de lucru normal de instalare. Acesta nu este un driver subțire sau un program de instalare autonom modificat. Opțional NVENC necesită încă o descărcare și consimțământ pentru acel driver exact. Termenii de redistribuire ai NVIDIA încă se aplică.

**Rezultate și asistență:** citiți rezultatul scurt și extindeți detaliile pe etapă/pe opțiune. Citirea cu succes stabilește o valoare stocată, nu o îmbunătățire măsurată. Raportul de asistență local JSON utilizează câmpuri permise, inclusiv ultima lucrare salvată după repornirea aplicației. Previzualizează-l înainte de a salva sau de a partaja. Nu include jurnalele brute, conținutul profilului sau identificatorii hardware și nu este încărcat niciodată automat.

**Recuperare:** urmați ghidul lucrării protejate pentru a recupera driverul pentru care faceți backup. Restaurarea explicită a profilului necesită versiunea originală a driverului și aceleași GPU-uri; înlocuiește întreaga bază de date, păstrează o copie curentă și verifică hashurile și starea conflictuală. Nu ștergeți jurnalul și nu forțați o nepotrivire. Instalarea driverului real, recuperarea completă și importarea profilului nativ cu acest nou flux de lucru rămân nevalidate pe un sistem real.

**Actualizări ale aplicației:** citiți notele de lansare, apoi alegeți în mod explicit o descărcare verificată prin SHA-256. Verificarea este manuală în mod implicit, cu o verificare opțională la pornire. Niciun program de instalare nu este pornit automat. Această caracteristică este separată de verificările actualizării driverului și de sarcina opțională de verificare a driverului a ediției instalate.

<a id="screenshots"></a>
## Capturi de ecran

![Previzualizarea paginii driverului NVDriverForge](../../../../assets/screenshots/nvdriverforge-0.1.2-preview.png)

Interfața de utilizare franceză 0.1.2 existentă, cu date de exemplu; păstrat ca previzualizare a interfeței. Driverul 699.99 afișat este un dispozitiv de testare, nu o versiune reală de descărcat. [Proveniența imaginii](../assets/README.md).

<a id="update-and-uninstall"></a>
## Actualizați și dezinstalați

Închideți NVDriverForge, obțineți următorul pachet oficial și verificați hash-ul acestuia. Utilizați aceeași identitate de configurare pentru o actualizare instalată; înlocuiți un EXE portabil închis cu unul nou. Păstrați setările și locurile de muncă protejate.

Uninstall de la Windows **Installed apps**. Îndepărtează aplicația și sarcina de actualizare, nu driverul NVIDIA. Setările, jurnalele și backup-urile rămân. Dacă doriți, restaurați modificările avansate/NVENC prin fluxul de recuperare documentat **înainte** de a elimina aplicația. Restaurare refuză modificările conflictuale de la un alt instrument.

Datele locale sunt sub `%LOCALAPPDATA%\NVDriverForge`; locurile de muncă protejate și exporturile de șoferi sunt sub `%PROGRAMDATA%\NVDriverForge\Jobs`. Utilizarea portabilă creează și date locale. Exportul din magazinul de drivere și backupul profilului nativ sunt separate. Nici o imagine de sistem.

<a id="known-limitations"></a>
## Limitări cunoscute

- Fără adăugiri hardware/editare INF, semnături NVIDIA regenerate, demisie compatibilă cu anti-cheat sau acceptare automată a avertismentului nesemnat.
- Nicio eliminare completă a telemetriei/publicității, exportul pachetului subțire sau derularea automată completă la driverul anterior.
- Instalarea driverului, recuperarea pornirii și scrierile opționale de profil nu au fost validate complet pe mașinile reale de către auditul hub.
- Citirea registrului nu este o dovadă a efectelor reale ale HDCP, de performanță sau de latență.
- Verificările semnăturii folosesc încrederea Windows disponibilă local; revocarea online nu se efectuează.
- Sunt prezente 34 de limbi, dar testarea completă a vorbitorilor nativi/accesibilitate rămâne incompletă.

<a id="troubleshooting"></a>
## Depanare

| Simptom | Acțiune |
| --- | --- |
| Catalog online indisponibil | Selectați un pachet original din [Descărcări de drivere NVIDIA](https://www.nvidia.com/en-us/drivers/). Nu înlocuiți un model GPU vecin. |
| Căutarea remedierii rapide nu este disponibilă | Utilizați [Forumul de drivere NVIDIA al lui Game Ready](https://www.nvidia.com/en-us/geforce/forums/game-ready-drivers/13/) și verificați pachetul real. |
| Instalarea NVIDIA eșuează | Citiți rezumatul erorilor și deschideți jurnalele detaliate. Componentele opționale deja actuale sau inaplicabile rămân ignorabile în 0.1.4. Instalările eșuate nu declanșează modificări opționale sau un flux de succes/repornire. |
| Eșec de semnătură/hash/backup | Opriți instalarea și păstrați eroarea; obțineți din nou pachetul original dacă este corupt. |
| Opțiune indisponibilă | Citiți motivul hardware-ului, componentei sau driverului țintă; păstrați-l neschimbat. |
| Reporniți sau lucrare încă în așteptare | Utilizați instrucțiunile de recuperare ale jobului și CV-ul explicit; nu-i șterge jurnalul. |
| Restabiliți conflictul | O altă stare diferă de tranzacția înregistrată. Păstrați-l și solicitați ajutor în loc să forțați o restaurare. |

Pentru rapoarte, includeți versiunea instrumentului selectat, Windows, GPU, driver și pași reproductibili; redactați căile și detaliile personale din jurnale. [Sprijin](../docs/support.md).

<a id="faq"></a>
## Întrebări frecvente

**Setup instalează un driver grafic?** Nu. Aceasta necesită analiza, revizuirea, confirmarea și procesul de instalare avansat al aplicației separat.

**Am nevoie de NVCleanstall sau NVPI?** Nu. NVCleanstall este doar inspirație. Companionul Profile Inspector este un editor opțional independent.

**Face fiecare driver NVIDIA mai mic sau mai rapid?** Nu. Componentele și cerințele preliminare selectate determină ce se poate schimba; nu se promite nici un câștig măsurat.

**Unde sunt sursele?** Sursele specifice aplicației și testele private sunt menținute separat. Acest hub oferă documentație, binare și link-uri sursă terță parte necesare pentru atribuire/licențiere.

<a id="credits-and-upstream"></a>
## Credite și în amonte

Aplicație originală, flux de lucru, tranzacții, localizare, bootstrap și adaptări: 禅堂 Zendo (RevoluSound Team).

- [NVCleanstall / TechPowerUp](https://www.techpowerup.com/download/techpowerup-nvcleanstall/): inspirație pentru fluxul de lucru; nicio sursă sau binar importat.
- [NVIDIA Profile Inspector / Orbmu2k](https://github.com/Orbmu2k/nvidiaProfileInspector): teme MIT, referință extinsă pentru interfață NVAPI și fork ambalat separat.
- [7-Zip / Igor Pavlov](https://www.7-zip.org/): instrumente de extracție nemodificate.
- [Microsoft .NET](https://github.com/dotnet/runtime) și [WPF](https://github.com/dotnet/wpf): timp de rulare inclus.
- [Inno Setup](https://jrsoftware.org/isinfo.php): motor de instalare original și traduceri creditate.
- [keylase/nvidia-patch](https://github.com/keylase/nvidia-patch): sursă de date externă opțională NVENC; licența de redistribuire nu este stabilită.
- [NVIDIA](https://www.nvidia.com/en-us/drivers/): descărcări de drivere externe și biblioteci NVAPI/NVML instalate.

[Tabel complet cu componente](../THIRD_PARTY_NOTICES.md) · [Schimbări și proveniență](../docs/provenance.md)

<a id="license"></a>
## Licență

[Permisiune de distribuție binară existentă](../../../../NVDriverForge/LICENSE) permite utilizarea și partajarea executabilelor oficiale nemodificate cu notificările lor. Drepturile de sursă specifice aplicației sunt rezervate. Nu limitează drepturile acordate de licențele separate ale terților. [Notificări complete](LICENSES/README.md).

Independent de NVIDIA Corporation, TechPowerUp și keylase; nesponsorizat sau susținut oficial de aceștia. Numele produselor rămân mărci comerciale ale proprietarilor lor.
