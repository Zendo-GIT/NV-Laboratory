<!-- nv-language-navigation:start -->
🌐 [English](../../../releasing.md) | [Français](../../../releasing.fr.md) · [NV Laboratory](../README.md)

<details>
<summary>🌐 Language · 34</summary>

[العربية](../../ar/docs/releasing.md) · [বাংলা](../../bn/docs/releasing.md) · [简体中文](../../zh/docs/releasing.md) · [Čeština](../../cs/docs/releasing.md) · **Dansk** · [Nederlands](../../nl/docs/releasing.md) · [English](../../../releasing.md) · [Filipino](../../fil/docs/releasing.md) · [Suomi](../../fi/docs/releasing.md) · [Français](../../../releasing.fr.md) · [Deutsch](../../de/docs/releasing.md) · [Ελληνικά](../../el/docs/releasing.md) · [हिन्दी](../../hi/docs/releasing.md) · [Magyar](../../hu/docs/releasing.md) · [Bahasa Indonesia](../../id/docs/releasing.md) · [Italiano](../../it/docs/releasing.md) · [日本語](../../ja/docs/releasing.md) · [한국어](../../ko/docs/releasing.md) · [मराठी](../../mr/docs/releasing.md) · [فارسی](../../fa/docs/releasing.md) · [Polski](../../pl/docs/releasing.md) · [Português](../../pt/docs/releasing.md) · [ਪੰਜਾਬੀ](../../pa/docs/releasing.md) · [Română](../../ro/docs/releasing.md) · [Русский](../../ru/docs/releasing.md) · [Español](../../es/docs/releasing.md) · [Kiswahili](../../sw/docs/releasing.md) · [Svenska](../../sv/docs/releasing.md) · [தமிழ்](../../ta/docs/releasing.md) · [ไทย](../../th/docs/releasing.md) · [Türkçe](../../tr/docs/releasing.md) · [Українська](../../uk/docs/releasing.md) · [اردو](../../ur/docs/releasing.md) · [Tiếng Việt](../../vi/docs/releasing.md)

[Translation policy](../../README.md)

</details>
<!-- nv-language-navigation:end -->

<!-- nv-translation-notice:start -->
> Maskinassisteret oversættelse fra engelsk. Tekniske navne, kommandoer, URL'er og originale lovtekster er bevaret. Native-speaker anmeldelse er velkommen; se den engelske reference, hvis ordlyden er uklar.
<!-- nv-translation-notice:end -->

<a id="publishing-and-releases"></a>
# Udgivelse og udgivelser

Det offentlige depot er **Zendo-GIT/NV-Laboratory**. Dokumentationsændringer gennemgås, forpligtes og skubbes af vedligeholderen med **GitHub Desktop**. En lokal commit uploader ikke filer. Binære pakker er separate GitHub Release-aktiver; de hører aldrig hjemme på Git-ændringslisten.

<a id="documentation-updates"></a>
## Opdatering af dokumentation

1. Åbn mappen **NV-Laboratory** i GitHub Desktop.
2. Gennemgå dokumentation, meddelelser, billeder, JSON-metadata og dokumentationsvalidatoren.
3. Kør `python tools/validate_repository.py` fra den mappe.
4. Forpligt de gennemgåede ændringer, og brug derefter **Push origin**. Tjek Actions-resultatet.
5. Behold den offentlige forfatteridentitet **禅堂 Zendo (RevoluSound Team)** og kontoens GitHub `noreply`-adresse.

Vælg aldrig det overordnede udviklingsarbejdsområde, det private revisionsmappe eller det binære vedhæftede bibliotek. [Forpligt e-mail privatliv](https://docs.github.com/en/account-and-profile/how-tos/email-preferences/setting-your-commit-email-address).

<a id="independent-application-releases"></a>
## Uafhængige applikationsudgivelser

| Værktøj | Tag | Versionspolitik |
| --- | --- | --- |
| NVIDIA Profile Inspector – NV Tools Fork | nvpi-v3.0.2.3 | Eksisterende firedelt applikationsversion; setup revision 2 har sit eget filnavn |
| NVDriverForge | nvdriverforge-v0.1.3 | Eksisterende 0.x-skema; versionerede opdateringer bevarer tidligere pakker |
| NVMFG Unlock40 | nvmfg-unlock40-v0.1.1 | UI2-kandidat identificeret ved nøjagtige hashes uden at opfinde en ny applikationsversion |
| NVRasterPulse | nvrasterpulse-v0.1 | Eksisterende todelt version |

Vedligeholderen kan offentliggøre direkte eller autorisere en assistent til at offentliggøre de reviderede aktiver. Offentliggørelsen er eksplicit; ingen arbejdsgange opretter en udgivelse på hver commit.

1. Gennemgå den aktuelle præpubliceringsrapport, kilder til binære filer, licenser og SHA-256-værdier.
2. Opret et udkast til værktøjets tag, målrettet mod den gennemgåede hub-commit. Medtag de forberedte versionsspecifikke udgivelsesbemærkninger.
3. Vedhæft kun den versions opsætning/bærbare aktiver, `Licenses-and-Credits.zip` og `SHA256SUMS.txt`.
4. Tjek kompatibilitet, installation, afhængigheder, ændringer og kendte grænser. Hold RTSS fremtrædende for NVRasterPulse.
5. Udgiv, bekræft de offentlige aktivs URL'er, størrelser og hashes, og optag den faktiske udgivelsesdato i `docs/releases.json`.
6. Opdater downloadsiderne og oversættelserne, og bekræft/skub derefter deres ændringer i GitHub Desktop.

Tag-links pr. projekt undgår at sende brugere til et andet værktøj via et delt `releases/latest`-link. GitHub's automatiske **Source code**-arkiver indeholder denne dokumentationshub. Applikationskilder forbliver private. Oprindelige komponentmeddelelser forbliver intakte, og en udgivelse løser ikke NVMFGs dokumenterede NVIDIA SDK-reserve.

<a id="integrity-and-storage"></a>
## Integritet og opbevaring

Udskift aldrig publicerede binære bytes uden lyd. Brug en ny eksplicit version eller installationsrevision med nye hashes. Lovlige sidevogne supplerer indlejrede meddelelser. NVDriverForge 0.1.3 bærbar er 141.760.351 bytes, over GitHub's almindelige 100 MiB Git-filgrænse. Frigiv vedhæftede filer undgå at sætte binære filer eller Git LFS i denne hub. [GitHub stor fil vejledning](https://docs.github.com/en/repositories/working-with-files/managing-large-files/about-large-files-on-github).

Privat sårbarhedsrapportering bør aktiveres i sikkerhedsindstillingerne for lageret. Bekræft dets tilgængelighed, før du sender følsomme rapporter dertil; [SECURITY.md](../SECURITY.md) giver en fallback, der ikke afslører sårbarhedsdetaljer.

[Download katalog](downloads.md) · [GitHub udgivelsesdokumentation](https://docs.github.com/en/repositories/releasing-projects-on-github/managing-releases-in-a-repository)
