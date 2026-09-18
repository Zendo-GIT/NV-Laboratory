<!-- nv-language-navigation:start -->
🌐 [English](../../../../NVMFG-Unlock40/README.md) | [Français](../../../../NVMFG-Unlock40/README.fr.md) · [NV Laboratory](../README.md)

<details>
<summary>🌐 Language · 34</summary>

[العربية](../../ar/NVMFG-Unlock40/README.md) · [বাংলা](../../bn/NVMFG-Unlock40/README.md) · [简体中文](../../zh/NVMFG-Unlock40/README.md) · [Čeština](../../cs/NVMFG-Unlock40/README.md) · [Dansk](../../da/NVMFG-Unlock40/README.md) · [Nederlands](../../nl/NVMFG-Unlock40/README.md) · [English](../../../../NVMFG-Unlock40/README.md) · [Filipino](../../fil/NVMFG-Unlock40/README.md) · [Suomi](../../fi/NVMFG-Unlock40/README.md) · [Français](../../../../NVMFG-Unlock40/README.fr.md) · [Deutsch](../../de/NVMFG-Unlock40/README.md) · [Ελληνικά](../../el/NVMFG-Unlock40/README.md) · [हिन्दी](../../hi/NVMFG-Unlock40/README.md) · [Magyar](../../hu/NVMFG-Unlock40/README.md) · [Bahasa Indonesia](../../id/NVMFG-Unlock40/README.md) · [Italiano](../../it/NVMFG-Unlock40/README.md) · [日本語](../../ja/NVMFG-Unlock40/README.md) · [한국어](../../ko/NVMFG-Unlock40/README.md) · [मराठी](../../mr/NVMFG-Unlock40/README.md) · [فارسی](../../fa/NVMFG-Unlock40/README.md) · [Polski](../../pl/NVMFG-Unlock40/README.md) · [Português](../../pt/NVMFG-Unlock40/README.md) · [ਪੰਜਾਬੀ](../../pa/NVMFG-Unlock40/README.md) · **Română** · [Русский](../../ru/NVMFG-Unlock40/README.md) · [Español](../../es/NVMFG-Unlock40/README.md) · [Kiswahili](../../sw/NVMFG-Unlock40/README.md) · [Svenska](../../sv/NVMFG-Unlock40/README.md) · [தமிழ்](../../ta/NVMFG-Unlock40/README.md) · [ไทย](../../th/NVMFG-Unlock40/README.md) · [Türkçe](../../tr/NVMFG-Unlock40/README.md) · [Українська](../../uk/NVMFG-Unlock40/README.md) · [اردو](../../ur/NVMFG-Unlock40/README.md) · [Tiếng Việt](../../vi/NVMFG-Unlock40/README.md)

[Translation policy](../../README.md)

</details>
<!-- nv-language-navigation:end -->

<!-- nv-translation-notice:start -->
> Traducere asistată automat din engleză. Numele tehnice, comenzile, URL-urile și textele legale originale sunt păstrate. Evaluarea vorbitorilor nativi este binevenită; consultați referința în limba engleză dacă formularea este neclară.
<!-- nv-translation-notice:end -->

<a id="nvmfg-unlock40"></a>
# NVMFG Unlock40

**NVIDIA Multi Frame Generation experimental pentru GeForce RTX 40, cu un controler central și opțiuni pentru fiecare joc.**

[Descărcați 0.2.3 și starea](../docs/downloads.md#nvmfg-unlock40) · [Instalare](#installation) · [în amonte](#upstream-and-modifications) · [Licențe](LICENSES/README.md)

<a id="overview-and-purpose"></a>
## Prezentare generală și scop

NVMFG Unlock40 este o aplicație dezvoltată independent de 禅堂 Zendo (RevoluSound Team). Combină un controler Windows, un strat nativ, un asistent de profil și managementul jocului/Streamline SDK. Vizează jocurile care integrează deja NVIDIA DLSS Frame Generation și runtime compatibile NVIDIA.

[RTX40MFG-Unlock](https://github.com/dashdogy/RTX40MFG-Unlock) a fost consultat pentru a compara și a rafina lucrarea. Stratul nativ actual conține componente partajate și adaptate, creditate individual mai jos. Această referință nu face din întreaga aplicație NVMFG un fork al proiectului respectiv.

Există pentru a coordona comportamentul experimental MFG la nivel central, pentru a reține alegerile specifice jocului și pentru a menține vizibile actualizările de rulare și backup-urile. Nu adaugă DLSS Frame Generation la fiecare joc și nu convertește o implementare arbitrară FSR.

Pachetul actual este **0.2.3**. Acesta adaugă o bibliotecă de jocuri persistentă, informații despre activități și capacități, diagnostice locale și comportament corectat de selecție/progres. [Descărcări](../docs/downloads.md#nvmfg-unlock40) identifică fișierele exacte și hashurile.

<a id="features"></a>
## Caracteristici

- Activare/dezactivare centrală a controlului și pornire opțională a tăvii Windows.
- Selecție per joc între Dynamic MFG, setarea jocului și multiplicatorii fiși acceptați.
- Opțiunile memorate separate pentru stările de pornire/oprire V-Sync observate.
- Dynamic folosește modul NVIDIA; este suspendat când V-Sync este dezactivat, cu o alegere separată în joc/fixă.
- Ghid pentru meniul de joc și excluderi persistente; jocurile fără DLSS FG păstrează controlul.
- Descoperirea jocului, selectarea folderului părinte, căutarea, gruparea și eliminarea fără ștergerea fișierelor de joc.
- Streamline Descărcare/import SDK, cache local verificat, selecție explicită, backup și restaurare per joc.
- Verificarea furnizorului nativ, diagnosticare per sesiune, jurnal de profil global și recuperare în funcție de conflict.
- 34 de limbi de interfață și patru teme.

Dezactivarea FG în joc îl menține oprit. Opțiunile fixe de la 2x la 6x depind de joc/meniu/rulare; nu sunt o promisiune că fiecare combinație funcționează. Controlerul observă V-Sync și nu setează V-Sync sau VRR pentru utilizator.

<a id="compatibility"></a>
## Compatibilitate

| Cerință | Detalii |
| --- | --- |
| Sistem | Windows 10/11 x64 |
| GPU | GeForce RTX 40 țintă; nicio revendicare universală de compatibilitate GPU |
| Joc | Integrarea NVIDIA DLSS Frame Generation existentă și timpul de rulare acceptat; fără certificare de compatibilitate anti-cheat |
| Furnizor | Candidatul este fixat la furnizorul SHA-256 documentat în [proveniența](../docs/provenance.md); hashes-urile necunoscute sunt refuzate |
| Timp de rulare | Pachet .NET 8/WPF 8.0.30 pentru aplicație/agent; .NET Framework 4.8 pentru ajutoare de profil |
| Permisiuni | Acces de administrator pentru operațiunile de controlor/profil |
| Rețea | Necesar pentru descărcări oficiale SDK selectate; SDKs compatibil importat poate fi stocat în cache local |
| Binare externe | Driverul NVIDIA, furnizorul/modelele NGX și duratele de rulare a jocului Streamline nu sunt incluse în pachet |

Numai o etichetă de versiune este insuficientă: driverul, hashul furnizorului, integrarea jocului și modulele încărcate real contează. Procesele protejate sau incompatibile pot refuza atașarea. Aplicația nu este concepută pentru a sustrage protecțiile anti-cheat.

<a id="installation"></a>
## Instalare

1. Citiți [statutul de candidat și nota de licență](../docs/downloads.md#nvmfg-unlock40).
2. Descărcați `NVMFGUnlock40-0.2.3-Setup-x64.exe` sau `NVMFGUnlock40-0.2.3-Portable-x64.zip` când versiunea sa este disponibilă.
3. Verificați SHA-256 și păstrați notificările însoțitoare. Instalați .NET Framework 4.8 dacă Windows nu îl furnizează deja.
4. Rulați Configurarea sau extrageți **întregul** fișier ZIP portabil într-un folder local care poate fi scris.
5. Lansați `NVMFGUnlock40.exe`; păstrați `agent`, `driver`, `engine` și `Licenses` în aspectul furnizat.

Dosarul numit `driver` conține ajutoare pentru spațiul utilizatorului, nu un driver de kernel. Nu copiați doar EXE-ul principal și nu înlocuiți hash-ul furnizorului pentru a forța compatibilitatea. EXE-urile actuale sunt nesemnate.

<a id="usage"></a>
## Utilizare

1. Începeți cu controlerul dezactivat. Adăugați un joc sau un folder părinte și alegeți instalările reale.
2. Examinați setările MFG ale fiecărui joc. Răspundeți ce oferă meniul său; răspunsul este stocat pe joc.
3. Alegeți Dynamic sau setarea din joc la nivel global, apoi ajustați opțiunile eligibile pentru fiecare joc după cum este necesar.
4. Activați controlerul numai atunci când intenționați să îl utilizați. Poate schimba temporar șase setări globale de profil NVIDIA, cu un jurnal de recuperare.
5. Lansați un joc eligibil și activați propriul său DLSS Frame Generation. Urmați orice solicitare pentru opțiunea V-Sync-off.
6. Utilizați excluderile pentru jocurile pe care nu doriți să le gestionați. Eliminarea unui joc înregistrează o excludere și păstrează fișierele/backup-urile acestuia.
7. Utilizați fluxul complet de ieșire/dezactivare și recuperare a aplicației când ați terminat.

Închiderea ferestrei principale poate lăsa controlerul în tavă. Un DLL deja încărcat într-un joc rămâne acolo până când jocul iese; dezactivarea controlerului nu este o garanție de descărcare. Închideți jocurile afectate înainte de întreținere sau actualizări.

**Streamline SDKs:** pe pagina NVIDIA SDK, descărcați o versiune oficială sau importați un SDK local compatibil. Importul stochează o copie verificată; **Use this version** îl selectează, iar **Uninstall** elimină acea copie din cache. DLL-urile Streamline lipsă pot fi completate dintr-un NVIDIA SDK oficial, cu sursa afișată. Acest lucru nu descarcă/înlocuiește un model NGX. Închideți jocul, selectați actualizarea dorită a jocului și păstrați backup-ul original. Pentru a reveni la fișierele jocului, utilizați restaurarea de rezervă, nu butonul Uninstall al memoriei cache.

<a id="library-diagnostics-and-updates"></a>
## Bibliotecă, diagnosticare și actualizări

**Bibliotecă persistentă:** selectați mai multe foldere de jocuri, inclusiv unități diferite, înainte de a începe o scanare. Progresul este vizibil și anularea este disponibilă. După prima scanare, un cache local restaurează biblioteca la lansare fără a parcurge fiecare folder de joc. Actualizează pentru a găsi modificări sau pentru a adăuga un alt dosar. Operațiunile de întreținere încă revalidează fișierele afectate; monitorizarea de rezervă rămâne activă. Cache-ul este stocat la `%LOCALAPPDATA%\RtxMfg\library-cache.json`.

**Selectare:** Ctrl+A selectează toate, iar Ctrl+D șterge fila Jocuri sau Backup-uri active. Niciun joc nu este selectat automat. Actualizările și reîmprospătările de activitate nu mai creează selecții fantomă sau numărări inconsecvente.

**Activitate și compatibilitate:** informațiile MFG per joc provin din observațiile NGX fără o nouă suprapunere. Nu este un număr fizic de cadre afișate. Suportul Dynamic-with-V-Sync vine din capabilitățile de rulare; capacitatea necunoscută nu este dedusă dintr-un număr de versiune. Aplicația nu modifică nici V-Sync, nici VRR. Cu V-Sync dezactivat, Dynamic rămâne suspendat; opțiunile fixe sau controlate de joc sunt separate.

**Următoarea lansare:** excluderea temporară omite corecțiile la următoarea lansare a jocului și restabilește gestionarea normală după ieșire. Nu poate elimina un DLL deja încărcat într-un joc: închideți și reporniți acel joc. Wallpaper Engine este recunoscut ca o aplicație desktop; această corecție păstrează protecția pentru jocurile ignorate reale.

**Preferințe și asistență:** importul/exportul preferințelor necesită reasociere manuală a folderelor de joc. Diagnosticul local din Despre filtrează informațiile private și raportează codurile de eroare NVAPI sau categoriile de conflict disponibile. Examinați-l înainte de a partaja; nimic nu este încărcat automat.

**Actualizări ale aplicației:** o verificare opțională afișează notele de lansare și oferă configurația oficială. Descărcarea explicită este verificată cu dimensiunea GitHub și metadatele SHA-256; inițiați singur instalarea. Versiunea 0.2.3 șterge, de asemenea, mesajele de progres finalizate, păstrând în același timp erorile și rezultatele semnificative. Aceste completări includ modificările de la versiunea publică 0.1.1.

<a id="screenshots"></a>
## Capturi de ecran

![NVMFG SDK-list previzualizare](../../../../assets/screenshots/nvmfg-0.1.1-sdk-preview.png)

Interfața existentă în limba engleză 0.1.1 este redată cu un exemplu de inventar SDK. Nu este o listă de versiuni actuale sau o dovadă a unui joc care rulează. [Proveniența imaginii](../assets/README.md).

<a id="update-and-uninstall"></a>
## Actualizați și dezinstalați

Închide jocurile afectate. Dezactivați/închideți NVMFG și rezolvați orice recuperare a setărilor NVIDIA în așteptare înainte de actualizare. Instalați următoarea instalare cu identitatea existentă sau extrageți noul portabil într-un folder nou; păstrează starea/backup-urile.

Înainte de dezinstalare, restabiliți backup-urile dorite ale jocului SDK și setările NVIDIA prin aplicație, apoi închideți jocurile și părăsiți controlerul. Utilizați Windows **Installed apps** pentru configurare sau eliminați folderul portabil închis după păstrarea fișierelor necesare. Nu ștergeți manual un jurnal de recuperare activ pentru a debloca Configurarea.

Backup-urile locale de rulare a jocului folosesc `%LOCALAPPDATA%\NvidiaStreamlineMaintenance\Backups`. Setările MFG/datele SDK folosesc `%LOCALAPPDATA%\RtxMfg`; ieșirea sesiunii este sub `Sessions` lângă aplicație. Aceste fișiere pot conține căi de joc. Nu le posta neredactate.

<a id="known-limitations"></a>
## Limitări cunoscute

- O blocare raportată la activarea/restaurarea/dezinstalarea 0.1.1 rămâne nereprodusă și cauza acesteia este necunoscută. Această versiune nu pretinde că o remediază. După o defecțiune, păstrați jurnalul de recuperare și inspectați diagnosticul local; nu forțați ștergerea datelor de recuperare.
- Patch-urile native experimentale pot provoca blocări sau artefacte vizuale; un accident nerezolvat Bodycam este înregistrat în istoricul dezvoltării.
- Testele de redare controlate nu sunt certificări pentru fiecare joc, driver sau anti-cheat.
- Cadrele generate nu creează noi mostre de intrare; nicio latență măsurată sau un câștig de performanță nu este promis de acest hub.
- Mai multe instrumente/suprapuneri de generare a cadrelor pot intra în conflict. Aplicația raportează modulele observate fără a dovedi fiecare scenariu de coexistență.
- Manifestul de compatibilitate este un ajutor de detectare, nu o listă de jocuri complet testate.
- Termenii completi NVIDIA SDK și restricția de limitare tehnică nerezolvată rămân documentate în [proveniența](../docs/provenance.md).

<a id="troubleshooting"></a>
## Depanare

| Simptom | Acțiune |
| --- | --- |
| Furnizorul nu este acceptat | Păstrați fișierele originale verificate. Raportați versiunile de driver/furnizor și eroarea; nu ocoli verificarea hash. |
| Nu există DLSS FG în joc | Selectați acel răspuns și lăsați jocul în control; acest instrument nu poate produce acea integrare. |
| Blocări de joc/artefacte | Închideți jocul, dezactivați NVMFG, utilizați backup-ul de rulare original al jocului dacă a fost modificat și raportați detalii reproductibile. |
| Lista SDK sau descărcare indisponibilă | Actualizați și verificați sursa oficială; o versiune cache/importată trebuie să treacă în continuare validarea. |
| În așteptare, recuperarea NVIDIA blochează ieșirea/actualizarea | Utilizați recuperarea și păstrați jurnalul; conflictele nu trebuie suprascrise orbeste. |
| Un joc eliminat nu este redescoperit | Excluderea sa este persistentă. Adăugați-l în mod explicit când doriți să fie gestionat din nou. |

[Îndrumări de asistență partajate](../docs/support.md) explică ce să includă într-un raport.

<a id="faq"></a>
## Întrebări frecvente

**Include DLL-uri sau modele NVIDIA?** Nu este inclus niciun driver, furnizorul/modelul NGX sau runtimeul Streamline. Descărcările explicite SDK provin de la NVIDIA.

**Dynamic funcționează cu V-Sync dezactivat?** Este suspendat în acea stare. Alegeți setarea în joc sau un multiplicator fix eligibil pentru starea separată a jocului respectiv.

**Este acesta un pachet ReShade/OptiScaler/FSR?** Nu. Acestea nu sunt compilate sau livrate ca parte a acestui pachet de producție.

**Sursele modificate sunt publice?** Nu. Sunt furnizate pachete compilate și creditele/licențele necesare. Acest lucru nu înlătură drepturile sau restricțiile terților.

<a id="upstream-and-modifications"></a>
## În amonte și modificări

Referință de comparație și componente native partajate: **RTX40MFG-Unlock de către Michael Robles / dashdogy**, referință commit `4e776d068f91b4a665425542bb005dd57cc3d891`, MIT. [Depozitul](https://github.com/dashdogy/RTX40MFG-Unlock) · [Descărcări originale](https://github.com/dashdogy/RTX40MFG-Unlock/releases).

Comparația surselor identifică corecțiile partajate, gestionarea furnizorului/politicii, corecțiile temporale și componentele ocolitoare bazate pe MinHook. Notificările lor MIT și BSD sunt păstrate. Comparația completă include și fișiere din afara țintei de producție.

Aplicația desktop, controlerul și fluxul de lucru de gestionare a SDK sunt dezvoltate de 禅堂 Zendo (RevoluSound Team). Lucrarea la proiect include încărcarea centrală, integrarea NGX bootstrap, selecția verificată a furnizorului, coordonarea jocului/V-Sync și diagnosticarea sesiunii. Ghidul de proveniență separă această lucrare de componentele comune; doar o comparație de fișiere nu stabilește când vreunul dintre autori a avut ideea.

Asistentul de profil adaptează ambalajul MIT NVAPI de la Profile Inspector de la Orbmu2k. [Proveniența detaliată și domeniul de aplicare al componentelor](../docs/provenance.md).

<a id="credits-and-license"></a>
## Credite și licență

Michael Robles; Orbmu2k; Tsuda Kageyu și colaboratori HDE; NVIDIA Corporation; Microsoft și colaboratori; Inno Setup autori și traducători. Dezvoltare de aplicații, integrări și ambalare: 禅堂 Zendo (RevoluSound Team).

[permisiunea existentă de partajare a pachetului compilat](../../../../NVMFG-Unlock40/LICENSE) și toate [licențe pentru componente](LICENSES/README.md) sunt păstrate. Permisiunile MIT pentru codul în amonte sunt distincte de termenii NVIDIA SDK. Nicio licență generală nu le înlocuiește.

Independent de, nu este sponsorizat de și nu este aprobat oficial de NVIDIA Corporation. Toate mărcile comerciale la care se face referire rămân proprietatea proprietarilor lor.
