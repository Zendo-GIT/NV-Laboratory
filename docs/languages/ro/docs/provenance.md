<!-- nv-language-navigation:start -->
🌐 [English](../../../provenance.md) | [Français](../../../provenance.fr.md) · [NV Laboratory](../README.md)

<details>
<summary>🌐 Language · 34</summary>

[العربية](../../ar/docs/provenance.md) · [বাংলা](../../bn/docs/provenance.md) · [简体中文](../../zh/docs/provenance.md) · [Čeština](../../cs/docs/provenance.md) · [Dansk](../../da/docs/provenance.md) · [Nederlands](../../nl/docs/provenance.md) · [English](../../../provenance.md) · [Filipino](../../fil/docs/provenance.md) · [Suomi](../../fi/docs/provenance.md) · [Français](../../../provenance.fr.md) · [Deutsch](../../de/docs/provenance.md) · [Ελληνικά](../../el/docs/provenance.md) · [हिन्दी](../../hi/docs/provenance.md) · [Magyar](../../hu/docs/provenance.md) · [Bahasa Indonesia](../../id/docs/provenance.md) · [Italiano](../../it/docs/provenance.md) · [日本語](../../ja/docs/provenance.md) · [한국어](../../ko/docs/provenance.md) · [मराठी](../../mr/docs/provenance.md) · [فارسی](../../fa/docs/provenance.md) · [Polski](../../pl/docs/provenance.md) · [Português](../../pt/docs/provenance.md) · [ਪੰਜਾਬੀ](../../pa/docs/provenance.md) · **Română** · [Русский](../../ru/docs/provenance.md) · [Español](../../es/docs/provenance.md) · [Kiswahili](../../sw/docs/provenance.md) · [Svenska](../../sv/docs/provenance.md) · [தமிழ்](../../ta/docs/provenance.md) · [ไทย](../../th/docs/provenance.md) · [Türkçe](../../tr/docs/provenance.md) · [Українська](../../uk/docs/provenance.md) · [اردو](../../ur/docs/provenance.md) · [Tiếng Việt](../../vi/docs/provenance.md)

[Translation policy](../../README.md)

</details>
<!-- nv-language-navigation:end -->

<!-- nv-translation-notice:start -->
> Traducere asistată automat din engleză. Numele tehnice, comenzile, URL-urile și textele legale originale sunt păstrate. Evaluarea vorbitorilor nativi este binevenită; consultați referința în limba engleză dacă formularea este neclară.
<!-- nv-translation-notice:end -->

<a id="provenance-changes-and-licensing"></a>
# Proveniență, modificări și licențiere

Acest audit descrie candidații pregătiți la **2026-09-18**. Sursele aplicației rămân private; inventarele publice conțin nume de fișiere și hashuri, nu cod sursă. Vezi [notificări complete ale componentelor](../THIRD_PARTY_NOTICES.md).

<a id="nvidia-profile-inspector--nv-tools-fork"></a>
## NVIDIA Profile Inspector – NV Tools Fork

Referință: Orbmu2k/nvidiaProfileInspector commit `592d962cca8827efe8859461a84267755595064a`; versiune executabilă candidată 3.0.2.3. Comiterea de referință și versiunea de asamblare a fork sunt identificatori diferiți; nicio versiune de lansare în amonte nu este dedusă din versiunea fork.

Cele 157 de fișiere sursă/resurse ale companionului curat au fost comparate cu acel commit: 2 octeți identici, 134 diferă doar în terminațiile de linie sau BOM UTF-8, 11 modificate, 10 absente la calea amonte comparată. „Adăugat” este relativ la acea cale și nu este în sine o dovadă a dreptului de autor original.

[Comparație completă fișier/hash](../../../provenance/nvpi-source-provenance.json).

| Zona | Munca moștenită | Contribuția Fork |
| --- | --- | --- |
| Editor de profil | Model de profil, import/export, asociații de aplicații și date de referință | Integrare cu Screen și lansatorul de instrumente extern |
| NVAPI | Interoperabilitatea DRS a lui Orbmu2k | Interoperabilitate legată de culoare/afișaj, restricții de încărcare nativă de producție și eliminare simulată |
| Servicii de afișare | API-urile Windows/NVIDIA ca interfețe externe | DisplayInfoService, DisplayConfigurationService, DisplaySettingsBackend |
| UI | Resurse, palete și pictograme WPF în amonte | Casete de dialog pe ecran, confirmare de 15 secunde, stare/citire înapoi și aspect al barei de instrumente |
| Lansatorul | Shell de aplicație existent | Căutare și lansare RasterPulse instalate separat protejate |
| Ambalare | MIT în amonte | Curățare însoțitor autonom, instalare/dezinstalare separată, notificări reținute |

Harta surselor publice include căi de soluție/resurse pentru trasabilitate; acele fișiere nu sunt distribuite ca sursă. Testele de dezvoltare, interfețele simulate și vechiul binar combinat NVPI/RasterPulse sunt excluse.

<a id="nvdriverforge"></a>
## NVDriverForge

Aplicație independentă C#/.NET 8/WPF; fluxul de lucru orientat spre utilizator este inspirat parțial de NVCleanstall. Nu a fost identificată nicio sursă/binar NVCleanstall în sarcina utilă de producție. Nu este reprezentat ca un fork al acelei aplicații proprietare.

Lucrarea inițială a proiectului include analiza/selectarea componentelor, lucrări de instalare protejate, backup-uri și recuperare a tranzacțiilor, descărcări de catalog NVIDIA, verificări de actualizare, explicații localizate, fluxuri de lucru opționale avansate/NVENC și bootstrap pentru instalare.

Componente moștenite/adaptate: patru palete tematice NVPI, referință extinsă pentru interfața NVAPI DRS și însoțitorul MIT NVPI opțional separat. Interfața de utilizare pentru selecția presetărilor Custom NV și integrarea tranzacțiilor permise aparțin NVDriverForge; presetarea nu este o recomandare oficială NVIDIA.

7-Zip 26.03, .NET/WPF 8.0.31 și Inno Setup rămân componente externe nemodificate utilizate în propriile lor condiții. keylase Datele NVENC nu sunt încorporate; un singur commit exact este ales și verificat atunci când utilizatorul solicită o descărcare compatibilă. Nu a fost stabilită nicio licență de redistribuire pentru acele date din amonte.

<a id="nvmfg-unlock40"></a>
## NVMFG Unlock40

NVMFG Unlock40 a fost dezvoltat independent de 禅堂 Zendo (RevoluSound Team). Menținătorul a folosit RTX40MFG-Unlock pentru comparație și rafinare. Aplicația în ansamblu nu este prezentată ca fork. Această distincție nu elimină creditele pentru componentele partajate/adaptate din stratul nativ curent.

Referință de comparație: dashdogy/RTX40MFG-Unlock, Michael Robles, MIT, commit `4e776d068f91b4a665425542bb005dd57cc3d891`. Arborele privat al motorului nativ conține 48 de fișiere comparate: 35 de diferențe doar de formatare, 4 fișiere modificate și 9 absente la calea de referință. [Comparație completă](../../../provenance/nvmfg-source-provenance.json).

Fișierele moștenite modificate: `entry_detour.h`, `patcher.cpp`, `temporal_interval_trace.cpp`, `temporal_interval_trace.h`. Căile suplimentare includ `game_selection.*`, `ngx_bootstrap.*`, `ngx_capability.h`, `presentation_tracker.h`, `vsync_observer.*` și o licență reținută în amonte.

Unități C++ de producție: patcher, midpoint_fix, dlssg_provider_policy, entry_detour, nvidia_mfg_policy, temporal_interval_trace, ngx_bootstrap, game_selection și vsync_observer; plus ansamblu entry_detour și tampon/cârlig/trambulină/HDE64 MinHook. Frontend-ul ReShade moștenit, resursele shim moștenite și țintele CMake neutilizate nu fac parte din această compilație de producție.

Componentele de potrivire acoperă politica de corecție/furnizor și munca temporală; notificările lor privind drepturile de autor și permisiunea rămân intacte. Coordonarea centrală NGX/bootstrap/controler, manipularea V-Sync per joc, diagnosticarea sesiunii și aplicația Windows/SDK/fluxul de lucru de rezervă sunt lucrări de proiect ale 禅堂 Zendo (RevoluSound Team). Numărările de mai sus descriu fișiere, inclusiv fișiere terțe și neutilizate, nu un procent de autor sau cronologia ideii fiecărei proiecte.

Asistentul adaptează NVPI NvapiDrsWrapper și NativeArrayHelper într-un ansamblu separat, cu logica de profil creată de proiect. Vechea cale de dezvoltare simulată este exclusă. Paletele de familie partajate provin din NVPI.

Referință MinHook: `8fda4f5481fed5797dc2651cd91e238e9b3928c6`; subsetul compilat moștenit nu are modificări locale funcționale în comparație. Anteturi de integrare Streamline: 2.12; licență antet deschisă verificată la v2.12.0. Sursa antet NGX: NVIDIA/DLSS commit `a291cc7d2cc642a51566f3dfd5376f635cd1b284`.

Motor candidat SHA-256: `C793770D329B99CD9C5C640317CE435BFE353CA2868E36CF5DCD4D5295EFAE13`.

Furnizorul necesar SHA-256 în engine.json: `C64928FDB7C48A57722EA8EEF2662171EDC323473ADEA66C29A206A23F1A2BED`. O familie de furnizori 310.9 raportată nu este interschimbabilă cu acest hash exact. Nu este inclus niciun DLL sau model de furnizor.

**Punctul de licență remarcabil:** licența completă NVIDIA RTX SDK, versiunea 14 martie 2024, conține o restricție de secțiune 4(d) relevantă pentru ocolirea limitărilor tehnice. Auditul nu stabilește permisiunea pentru această utilizare. Păstrarea licenței de motor MIT, a fi gratuit sau observarea altor moduri nu rezolvă acea condiție separată. Pregătirea candidaților nu este o autorizație legală. Notul de antet scurt inițial este completat cu licența completă; textul său Windows-1252 este, de asemenea, furnizat ca UTF-8 lizibil, cu octeții originali păstrați.

Comparația nativă a fost recalculată pentru 0.2.3: aceleași 48 de fișiere și clasificări. De la auditul anterior, `game_selection.cpp`, `game_selection.h` și `patcher.cpp` s-au schimbat pentru observațiile de activitate/capacitate. Noile fluxuri de lucru de bibliotecă, diagnosticare, preferințe, actualizare și selecție aparțin aplicației de întreținere. Licențele pentru componente și hash-ul necesar furnizorului sunt neschimbate.

<a id="nvrasterpulse"></a>
## NVRasterPulse

Manager de profil independent RTSS dezvoltat în depozitul derivat din NVPI. Resursele/paletele UI MIT moștenite și originea proiectului rămân creditate. Aplicația de producție utilizează în mod explicit acea licență MIT furnizată.

Lucru la proiect: analiza/scrierea precisă a profilului RTSS și codificare fracțională, backup-uri, eliminarea suprascrierii, puntea de reîncărcare, detectarea cerințelor preliminare, interfața de utilizare compactă, ciclul de viață al tăvii, controale de pornire și localizare. RTSS efectuează limitarea efectivă.

Nu este inclusă nicio sursă RTSS, DLL hook, SDK sau program de instalare. Puntea apelează exportul într-o instalare RTSS selectată de utilizator. În acest pachet nu se află niciun pachet de driver NVIDIA, limitator experimental nativ, Framepacer, MinHook, ReShade sau DLSS.

<a id="assets-generated-data-and-tools"></a>
## Active, date generate și instrumente

[Credite de active](../assets/README.md) identifică previzualizările interfeței existente și selectorul de configurare NVPI. Valorile fictive din ele sunt etichetate. Nu este copiat niciun joc/activ Nexus, profil personal, ICC privat, sigla corporativă NVIDIA sau fișier cu font.

Numele generate de compatibilitatea jocurilor moștenite în NVMFG sunt un ajutor de detectare, nu dovezi de testare. Cataloagele de instalare generate sunt creditate în [notificări ale traducătorului](../../../../licenses/INSTALLER-TRANSLATORS.md). Înregistrările de compilare generate cu căi absolute rămân private.

Instrumentele de construcție private includ scripturile de audit .NET SDK/MSBuild, Visual Studio C++/MASM, Windows SDK, PowerShell, Inno Setup și Python. Compilatoarele, anteturile, runnerele de testare și materialele de depanare ale acestora nu sunt distribuite. CRT de eliberare statică rămâne în conformitate cu termenii aplicabili ai lanțului de instrumente Microsoft.

<a id="scope-of-verification"></a>
## Domeniul verificării

Auditul local a inventariat toate fișierele din cele trei rădăcini de dezvoltare, excluzând în același timp bazele de date cu obiecte Git și directoarele ținte legate. Sursa/documentele active au fost scanate; construcțiile istorice au fost inventariate și excluse. ZIP-urile selectate și încărcăturile utile curente au fost scanate și hashing; pachetele .NET au fost decomprimate pentru inspecție suplimentară. Auditul inițial nu a rulat niciun produs, program de instalare, joc, proces RTSS sau driver.

Revizia 2 de configurare NVPI ulterioară remediază selecția autonomă a limbii folosind controalele Inno și bootstrap partajate. Corpurile private de iluminat/întuneric au verificat navigarea prin mouse și tastatură și toate cele 34 de coduri de limbă explicite. Selectorul de configurare real a fost deschis pe un desktop privat care nu a fost afișat niciodată și a fost anulat înainte de instalare. Cele șapte fișiere de aplicație și ZIP portabil sunt neschimbate. NVDriverForge 0.1.3 include însoțitorul corectat și încă transmite `/LANG`.

NVDriverForge 0.1.3 a fost finalizat pe 2026-09-10. Raportul său privat de verificare înregistrează 366 de teste de aplicație, 118 de verificări însoțitoare, 32 de verificări de configurare, 156 de comparații native și 34 de cazuri de redirecționare a limbii. Remedierea de selecție a componentelor protejate a fost reluată împotriva unui pachet de driver original fără a-i modifica sarcina utilă sau a instala driverul. Acestea sunt rezultate datate ale echipei de produs, nu teste reluate prin această actualizare a documentației sau dovada unei instalări reușite a driverului real.

Această actualizare hub nu modifică niciun cod funcțional al aplicației. Testele anterioare pentru crearea/unitatea/UI de aplicație rămân dovezi istorice datate. Aceasta nu este o inginerie inversă completă a fiecărui binar terță parte sau o garanție împotriva oricărui tipar secret posibil.

Actualizare din 18 septembrie 2026: NVDriverForge 0.1.4 adaugă verificări de pregătire, backup nativ al profilului, ghidare pentru componente, preferințe și kituri, rezultate detaliate, raportare locală și actualizări ale aplicațiilor. NVRasterPulse 0.2 adaugă diagnostice de configurare, ghidare FPS, pauză/reluare, anulare, profiluri `.nvrp` și favorite/ascundere, fără un nou motor de limitare. Ghidurile individuale descriu utilizarea și limitele. Verificările hub-ului statice sunt separate de testele de aplicare înregistrate în rapoartele private din 18 septembrie; nu a fost efectuată nicio instalare a driverului, importul de profil real sau măsurarea latenței pentru acest hub.
