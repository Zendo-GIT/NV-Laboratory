<!-- nv-language-navigation:start -->
🌐 [English](../../../releasing.md) | [Français](../../../releasing.fr.md) · [NV Laboratory](../README.md)

<details>
<summary>🌐 Language · 34</summary>

[العربية](../../ar/docs/releasing.md) · [বাংলা](../../bn/docs/releasing.md) · [简体中文](../../zh/docs/releasing.md) · [Čeština](../../cs/docs/releasing.md) · [Dansk](../../da/docs/releasing.md) · [Nederlands](../../nl/docs/releasing.md) · [English](../../../releasing.md) · [Filipino](../../fil/docs/releasing.md) · [Suomi](../../fi/docs/releasing.md) · [Français](../../../releasing.fr.md) · [Deutsch](../../de/docs/releasing.md) · [Ελληνικά](../../el/docs/releasing.md) · [हिन्दी](../../hi/docs/releasing.md) · [Magyar](../../hu/docs/releasing.md) · [Bahasa Indonesia](../../id/docs/releasing.md) · [Italiano](../../it/docs/releasing.md) · [日本語](../../ja/docs/releasing.md) · [한국어](../../ko/docs/releasing.md) · [मराठी](../../mr/docs/releasing.md) · [فارسی](../../fa/docs/releasing.md) · [Polski](../../pl/docs/releasing.md) · [Português](../../pt/docs/releasing.md) · [ਪੰਜਾਬੀ](../../pa/docs/releasing.md) · **Română** · [Русский](../../ru/docs/releasing.md) · [Español](../../es/docs/releasing.md) · [Kiswahili](../../sw/docs/releasing.md) · [Svenska](../../sv/docs/releasing.md) · [தமிழ்](../../ta/docs/releasing.md) · [ไทย](../../th/docs/releasing.md) · [Türkçe](../../tr/docs/releasing.md) · [Українська](../../uk/docs/releasing.md) · [اردو](../../ur/docs/releasing.md) · [Tiếng Việt](../../vi/docs/releasing.md)

[Translation policy](../../README.md)

</details>
<!-- nv-language-navigation:end -->

<!-- nv-translation-notice:start -->
> Traducere asistată automat din engleză. Numele tehnice, comenzile, URL-urile și textele legale originale sunt păstrate. Evaluarea vorbitorilor nativi este binevenită; consultați referința în limba engleză dacă formularea este neclară.
<!-- nv-translation-notice:end -->

<a id="publishing-and-releases"></a>
# Publicare și lansări

Depozitul public este **Zendo-GIT/NV-Laboratory**. Modificările documentației sunt revizuite, comise și împins de către întreținător cu **GitHub Desktop**. Un commit local nu încarcă fișiere. Pachetele binare sunt active GitHub Release separate; nu aparțin niciodată listei de modificări Git.

<a id="documentation-updates"></a>
## Actualizări de documentație

1. Deschideți folderul **NV-Laboratory** în GitHub Desktop.
2. Examinați documentația, notificările, imaginile, metadatele JSON și validatorul de documentație.
3. Rulați `python tools/validate_repository.py` din acel folder.
4. Commiteți modificările examinate, apoi utilizați **Push origin**. Verificați rezultatul Acțiunilor.
5. Păstrați identitatea autorului public **禅堂 Zendo (RevoluSound Team)** și adresa contului GitHub `noreply`.

Nu selectați niciodată spațiul de lucru de dezvoltare părinte, directorul de audit privat sau directorul de atașamente binar. [Angajați confidențialitatea e-mailului](https://docs.github.com/en/account-and-profile/how-tos/email-preferences/setting-your-commit-email-address).

<a id="independent-application-releases"></a>
## Lansări independente de aplicații

| Instrument | Etichetați | Politica de versiune |
| --- | --- | --- |
| NVIDIA Profile Inspector – NV Tools Fork | nvpi-v3.0.2.3 | Versiunea existentă a aplicației din patru părți; versiunea de configurare 2 are propriul nume de fișier |
| NVDriverForge | nvdriverforge-v0.1.3 | Schema 0.x existentă; actualizările versionate păstrează pachetele anterioare |
| NVMFG Unlock40 | nvmfg-unlock40-v0.1.1 | Candidatul UI2 identificat prin hashuri exacte fără a inventa o nouă versiune a aplicației |
| NVRasterPulse | nvrasterpulse-v0.1 | Versiune existentă în două părți |

Menținătorul poate publica direct sau poate autoriza un asistent să publice activele auditate. Publicarea este explicită; niciun flux de lucru nu creează o Lansare la fiecare comitere.

1. Examinați raportul curent de prepublicare, sursele binarelor, licențele și valorile SHA-256.
2. Creați o schiță pentru eticheta instrumentului, vizând comiterea hubului revizuită. Includeți notele de lansare pregătite specifice versiunii.
3. Atașați numai activele de configurare/portabile ale acelei versiuni, `Licenses-and-Credits.zip` și `SHA256SUMS.txt`.
4. Verificați compatibilitatea, instalarea, dependențele, modificările și limitele cunoscute. Păstrați RTSS proeminent pentru NVRasterPulse.
5. Publicați, verificați adresele URL ale activelor publice, dimensiunile și codurile hash și înregistrați data reală a publicării în `docs/releases.json`.
6. Actualizați paginile de descărcare și traducerile, apoi confirmați/împingeți modificările acestora în GitHub Desktop.

Legăturile etichetelor per proiect evită trimiterea utilizatorilor către un alt instrument printr-o legătură `releases/latest` partajată. Arhivele automate **Source code** ale GitHub conțin acest centru de documentație. Sursele aplicației rămân private. Notificările originale ale componentelor rămân intacte, iar o lansare nu rezolvă rezerva NVIDIA SDK documentată a NVMFG.

<a id="integrity-and-storage"></a>
## Integritate și stocare

Nu înlocuiți niciodată în tăcere octeții binari publicati. Utilizați o nouă versiune explicită sau o revizuire a programului de instalare cu noi hash-uri. Vehiculele laterale legale suplimentează notificările încorporate. NVDriverForge 0.1.3 portabil are 141.760.351 de octeți, peste limita obișnuită a fișierelor Git de 100 MiB a GitHub. Atașamentele de lansare evită introducerea binarelor sau Git LFS în acest hub. [GitHub ghid pentru fișiere mari](https://docs.github.com/en/repositories/working-with-files/managing-large-files/about-large-files-on-github).

Raportarea vulnerabilităților private ar trebui să fie activată în setările de securitate ale depozitului. Verificați disponibilitatea acestuia înainte de a direcționa rapoarte sensibile acolo; [SECURITY.md](../SECURITY.md) oferă o rezervă care nu expune detaliile vulnerabilității.

[Descărcați catalogul](downloads.md) · [Documentația de lansare a GitHub](https://docs.github.com/en/repositories/releasing-projects-on-github/managing-releases-in-a-repository)
