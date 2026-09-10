<!-- nv-language-navigation:start -->
🌐 [English](../../../development.md) | [Français](../../../development.fr.md) · [NV Laboratory](../README.md)

<details>
<summary>🌐 Language · 34</summary>

[العربية](../../ar/docs/development.md) · [বাংলা](../../bn/docs/development.md) · [简体中文](../../zh/docs/development.md) · [Čeština](../../cs/docs/development.md) · [Dansk](../../da/docs/development.md) · [Nederlands](../../nl/docs/development.md) · [English](../../../development.md) · [Filipino](../../fil/docs/development.md) · [Suomi](../../fi/docs/development.md) · [Français](../../../development.fr.md) · [Deutsch](../../de/docs/development.md) · [Ελληνικά](../../el/docs/development.md) · [हिन्दी](../../hi/docs/development.md) · [Magyar](../../hu/docs/development.md) · [Bahasa Indonesia](../../id/docs/development.md) · [Italiano](../../it/docs/development.md) · [日本語](../../ja/docs/development.md) · [한국어](../../ko/docs/development.md) · [मराठी](../../mr/docs/development.md) · [فارسی](../../fa/docs/development.md) · [Polski](../../pl/docs/development.md) · [Português](../../pt/docs/development.md) · [ਪੰਜਾਬੀ](../../pa/docs/development.md) · **Română** · [Русский](../../ru/docs/development.md) · [Español](../../es/docs/development.md) · [Kiswahili](../../sw/docs/development.md) · [Svenska](../../sv/docs/development.md) · [தமிழ்](../../ta/docs/development.md) · [ไทย](../../th/docs/development.md) · [Türkçe](../../tr/docs/development.md) · [Українська](../../uk/docs/development.md) · [اردو](../../ur/docs/development.md) · [Tiếng Việt](../../vi/docs/development.md)

[Translation policy](../../README.md)

</details>
<!-- nv-language-navigation:end -->

<!-- nv-translation-notice:start -->
> Traducere asistată automat din engleză. Numele tehnice, comenzile, URL-urile și textele legale originale sunt păstrate. Evaluarea vorbitorilor nativi este binevenită; consultați referința în limba engleză dacă formularea este neclară.
<!-- nv-translation-notice:end -->

<a id="repository-architecture-and-maintenance"></a>
# Arhitectura și întreținerea depozitului

NV Laboratory este un ** hub de documentare și distribuție binară** public. Nu conține sursa aplicației. Cele patru proiecte păstrează arbori de construcție, versiuni, identități și active de lansare separate. Istoricul lor privat de dezvoltare nu este importat în acest depozit Git.

<a id="layout"></a>
## Aspect

| Locație | Scop |
| --- | --- |
| README.md / README.fr.md | Puncte de intrare engleză/franceză |
| Patru dosare de proiect | Ghiduri complete și notificări originale aplicabile |
| docs | Descărcări, compatibilitate, proveniență, dezvoltare și procedura de lansare |
| docs/releases.json | Metadatele, dimensiunile și hashurile auditate ale candidatului/lansării |
| documente/ proveniență | Comparații fișier/hash; nici un cod de aplicație |
| licențe | Partajate texte complete de la terți și credite pentru traducători de instalare |
| active | Previzualizările UI examinate existente și proveniența acestora |
| .github | Emite formulare și validarea documentației numai în citire |
| instrumente/validate_repository.py | Verificări standard-biblioteca-publicare-limită și link |

Engleza rămâne GitHub README implicit. Legăturile `.fr.md` adiacente existente rămân valabile. Traduceri suplimentare reflectă documentația sub `docs/languages/<code>`; selectorul de limbă păstrează aceeași pagină la schimbarea limbii. Catalogul `docs/languages/catalog.json` înregistrează toate cele 34 de limbi și amprentele digitale sursă. GitHub nu selectează automat un README în funcție de limba browserului. Vedeți [indexul lingvistic și politica de traducere](../../README.md).

<a id="application-technologies"></a>
## Tehnologii de aplicare

| Program | Tehnologia privată | Distributie |
| --- | --- | --- |
| NVPI fork | C#, WPF, .NET Framework 4.8, NVAPI/Windows interoperabilitate | Dosar portabil complet și Inno Setup separat |
| NVDriverForge | C#, WPF, .NET 8; bootstrap nativ C++; proces 7-Zip | EXE portabil autonom și configurare |
| NVMFG Unlock40 | C#/WPF .NET 8, cadru de ajutor 4.8, motor C++20/MASM/MinHook | Arborele portabil și configurarea |
| NVRasterPulse | C#/WPF Cadrul 4.8; Integrare profil/reîncărcare RTSS; bootstrap nativ | Arborele portabil și configurarea |

Această verificare publică nu poate reconstrui aplicațiile. Arhivele automate „Source code” sunt instantanee hub. Link-urile surselor din amonte nu reprezintă exact sursa privată modificată. CI public validează numai acest depozit.

<a id="local-checks"></a>
## Verificări locale

Din rădăcina depozitului:

```text
python tools/validate_repository.py
```

Python 3.10 sau mai nou este suficient. Verificarea citește fișiere, legături locale Markdown, notificări necesare/linkuri RTSS, metadate de lansare și limite de publicare. Nu execută software-ul, nu instalează dependențe sau contactează o rețea.

Fluxul de lucru GitHub rulează aceeași verificare cu permisiunea de conținut numai pentru citire la cerere push, pull sau expediere manuală. Checkout este fixat pe un commit auditat și nu persistă acreditările. Nu este configurată nicio sarcină de lansare sau de implementare.

<a id="maintain-the-boundary"></a>
## Menține granița

Actualizați împreună referința în engleză, ghidurile în franceză și traducerile afectate. Păstrați modificările substanțiale separate de comparațiile numai pentru formatare. Înregistrați hashurile reale ale candidaților, referințele de comitere în amonte și licențele; nu deduceți niciodată o licență din popularitatea unui proiect.

Folosiți materiale de lansare cu versiuni noi și auditați din nou fișierele binare modificate, arhivele și notificările încorporate. Păstrați copiile de rezervă private în afara acestui depozit. Nu utilizați un flux de lucru public pentru a importa sursa aplicației private sau foldere locale de compilare.

Testele adecvate pentru modificarea unei aplicații funcționale rulează în proiectul privat. Nu rerulați programele de instalare a driverelor și nu scrieți profiluri reale pentru o actualizare a documentației. [Procedura de eliberare manuală](releasing.md).
