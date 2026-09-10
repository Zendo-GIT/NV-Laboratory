<!-- nv-language-navigation:start -->
🌐 [English](releasing.md) | Français · [NV Laboratory](../README.fr.md)

<details>
<summary>🌐 Language · 34</summary>

[العربية](languages/ar/docs/releasing.md) · [বাংলা](languages/bn/docs/releasing.md) · [简体中文](languages/zh/docs/releasing.md) · [Čeština](languages/cs/docs/releasing.md) · [Dansk](languages/da/docs/releasing.md) · [Nederlands](languages/nl/docs/releasing.md) · [English](releasing.md) · [Filipino](languages/fil/docs/releasing.md) · [Suomi](languages/fi/docs/releasing.md) · **Français** · [Deutsch](languages/de/docs/releasing.md) · [Ελληνικά](languages/el/docs/releasing.md) · [हिन्दी](languages/hi/docs/releasing.md) · [Magyar](languages/hu/docs/releasing.md) · [Bahasa Indonesia](languages/id/docs/releasing.md) · [Italiano](languages/it/docs/releasing.md) · [日本語](languages/ja/docs/releasing.md) · [한국어](languages/ko/docs/releasing.md) · [मराठी](languages/mr/docs/releasing.md) · [فارسی](languages/fa/docs/releasing.md) · [Polski](languages/pl/docs/releasing.md) · [Português](languages/pt/docs/releasing.md) · [ਪੰਜਾਬੀ](languages/pa/docs/releasing.md) · [Română](languages/ro/docs/releasing.md) · [Русский](languages/ru/docs/releasing.md) · [Español](languages/es/docs/releasing.md) · [Kiswahili](languages/sw/docs/releasing.md) · [Svenska](languages/sv/docs/releasing.md) · [தமிழ்](languages/ta/docs/releasing.md) · [ไทย](languages/th/docs/releasing.md) · [Türkçe](languages/tr/docs/releasing.md) · [Українська](languages/uk/docs/releasing.md) · [اردو](languages/ur/docs/releasing.md) · [Tiếng Việt](languages/vi/docs/releasing.md)

[Translation policy](languages/README.md)

</details>
<!-- nv-language-navigation:end -->

<a id="publishing-and-releases"></a>
# Publication et Releases

Le dépôt public est **Zendo-GIT/NV-Laboratory**. Le mainteneur examine, committe et
pousse les changements documentaires avec **GitHub Desktop**. Un commit local ne
téléverse rien. Les binaires sont des pièces jointes de Releases GitHub et ne
doivent jamais figurer parmi les changements Git.

<a id="documentation-updates"></a>
## Mise à jour documentaire

1. Ouvrez le dossier **NV-Laboratory** dans GitHub Desktop.
2. Examinez les documents, notices, images, métadonnées JSON et le validateur documentaire.
3. Lancez `python tools/validate_repository.py` depuis ce dossier.
4. Faites le commit puis **Push origin**. Vérifiez le résultat dans Actions.
5. Gardez l'identité publique **禅堂 Zendo (RevoluSound Team)** et l'adresse GitHub `noreply` du compte.

Ne sélectionnez jamais le dossier de développement parent, les audits privés ou
les pièces jointes binaires. [Confidentialité de l'adresse des commits](https://docs.github.com/en/account-and-profile/how-tos/email-preferences/setting-your-commit-email-address).

<a id="independent-application-releases"></a>
## Releases indépendantes

| Outil | Tag | Politique de version |
| --- | --- | --- |
| NVIDIA Profile Inspector – NV Tools Fork | nvpi-v3.0.2.3 | Version applicative à quatre parties conservée ; setup révision 2 identifié séparément |
| NVDriverForge | nvdriverforge-v0.1.3 | Numérotation 0.x conservée ; anciens paquets préservés |
| NVMFG Unlock40 | nvmfg-unlock40-v0.1.1 | Candidate UI2 identifiée par ses hashes sans inventer une version applicative |
| NVRasterPulse | nvrasterpulse-v0.1 | Version à deux parties conservée |

Le mainteneur peut publier directement ou autoriser un assistant à publier les
assets audités. La publication est explicite ; aucun workflow ne crée une Release
à chaque commit.

1. Examinez le rapport courant, la provenance des binaires, les licences et les SHA-256.
2. Créez un brouillon avec le tag de l'outil sur le commit du hub examiné, puis les notes de version préparées.
3. Joignez seulement les assets Setup/portable de cette version, `Licenses-and-Credits.zip` et `SHA256SUMS.txt`.
4. Vérifiez compatibilité, installation, dépendances, changements et limites. Gardez RTSS visible pour NVRasterPulse.
5. Publiez, contrôlez les URL publiques, tailles et hashes, puis inscrivez la date réelle dans `docs/releases.json`.
6. Actualisez les téléchargements et traductions, puis faites le commit/push dans GitHub Desktop.

Chaque projet utilise son tag ; un lien commun `releases/latest` risquerait de
diriger vers un autre outil. Les archives automatiques **Source code** contiennent
ce hub documentaire. Les sources applicatives restent privées. Les notices des
composants sont conservées et une Release ne résout pas la réserve NVIDIA de NVMFG.

<a id="integrity-and-storage"></a>
## Intégrité et stockage

Ne remplacez jamais silencieusement un binaire publié : utilisez une version ou
révision explicite et de nouveaux hashes. Les notices complémentaires s'ajoutent
aux notices embarquées. Le portable NVDriverForge 0.1.3 fait 141 760 351 octets,
au-dessus de la limite Git ordinaire de 100 Mio. Les pièces jointes de Releases
évitent de stocker des binaires ou Git LFS dans le hub.
[Documentation GitHub](https://docs.github.com/en/repositories/working-with-files/managing-large-files/about-large-files-on-github).

Le signalement privé doit être activé dans les réglages de sécurité du dépôt.
Vérifiez sa disponibilité avant d'y orienter les signalements sensibles ;
[SECURITY.md](../SECURITY.md) prévoit une solution de repli sans détail de faille public.

[Catalogue des téléchargements](downloads.fr.md) · [Gestion des Releases GitHub](https://docs.github.com/en/repositories/releasing-projects-on-github/managing-releases-in-a-repository)
