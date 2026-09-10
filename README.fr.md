<!-- nv-language-navigation:start -->
🌐 [English](README.md) | Français · [NV Laboratory](README.fr.md)

<details>
<summary>🌐 Language · 34</summary>

[العربية](docs/languages/ar/README.md) · [বাংলা](docs/languages/bn/README.md) · [简体中文](docs/languages/zh/README.md) · [Čeština](docs/languages/cs/README.md) · [Dansk](docs/languages/da/README.md) · [Nederlands](docs/languages/nl/README.md) · [English](README.md) · [Filipino](docs/languages/fil/README.md) · [Suomi](docs/languages/fi/README.md) · **Français** · [Deutsch](docs/languages/de/README.md) · [Ελληνικά](docs/languages/el/README.md) · [हिन्दी](docs/languages/hi/README.md) · [Magyar](docs/languages/hu/README.md) · [Bahasa Indonesia](docs/languages/id/README.md) · [Italiano](docs/languages/it/README.md) · [日本語](docs/languages/ja/README.md) · [한국어](docs/languages/ko/README.md) · [मराठी](docs/languages/mr/README.md) · [فارسی](docs/languages/fa/README.md) · [Polski](docs/languages/pl/README.md) · [Português](docs/languages/pt/README.md) · [ਪੰਜਾਬੀ](docs/languages/pa/README.md) · [Română](docs/languages/ro/README.md) · [Русский](docs/languages/ru/README.md) · [Español](docs/languages/es/README.md) · [Kiswahili](docs/languages/sw/README.md) · [Svenska](docs/languages/sv/README.md) · [தமிழ்](docs/languages/ta/README.md) · [ไทย](docs/languages/th/README.md) · [Türkçe](docs/languages/tr/README.md) · [Українська](docs/languages/uk/README.md) · [اردو](docs/languages/ur/README.md) · [Tiếng Việt](docs/languages/vi/README.md)

[Translation policy](docs/languages/README.md)

</details>
<!-- nv-language-navigation:end -->

<a id="nv-laboratory"></a>
# NV Laboratory

**NV Tools par 禅堂 Zendo (RevoluSound Team).** Quatre utilitaires Windows indépendants pour les profils et pilotes NVIDIA, la Multi Frame Generation expérimentale et les limites FPS RTSS.

[Téléchargements](docs/downloads.fr.md) · [Installation](docs/installation.fr.md) · [Compatibilité et aide](docs/support.fr.md) · [Crédits et licences](THIRD_PARTY_NOTICES.md)

> **NVRasterPulse nécessite RTSS.** Installez d'abord [RivaTuner Statistics Server depuis Guru3D](https://www.guru3d.com/download/rtss-rivatuner-statistics-server-download/). RTSS doit fonctionner pour appliquer ses limites FPS. Son téléchargement est séparé.

<a id="projects"></a>
## Projets

| Projet | Utilité | Version | Documentation | Téléchargement |
| --- | --- | --- | --- | --- |
| **NVIDIA Profile Inspector – NV Tools Fork** | Éditeur de profils NVIDIA enrichi de réglages écran, couleurs, HDR et ICC/WCS. Anciennement NVPI Custom. | 3.0.2.3 | [Guide](NVIDIA-Profile-Inspector/README.fr.md) | [Paquets](docs/downloads.fr.md#nvidia-profile-inspector) |
| **NVDriverForge** | Choisir les composants du pilote, examiner les réglages facultatifs et installer un paquet NVIDIA original. | 0.1.3 | [Guide](NVDriverForge/README.fr.md) | [Paquets](docs/downloads.fr.md#nvdriverforge) |
| **NVMFG Unlock40** | Outil MFG expérimental pour RTX 40, avec choix par jeu et maintenance des SDK Streamline. | 0.1.1 | [Guide](NVMFG-Unlock40/README.fr.md) | [Paquets et statut](docs/downloads.fr.md#nvmfg-unlock40) |
| **NVRasterPulse** | Gérer les limites FPS RTSS par exécutable, avec valeurs fractionnaires, sauvegardes et accès depuis la zone de notification. | 0.1 | [Guide](NVRasterPulse/README.fr.md) | [Paquets](docs/downloads.fr.md#nvrasterpulse) |

**Téléchargements :** la [page dédiée](docs/downloads.fr.md) donne le statut de chaque version, ses fichiers et ses empreintes SHA-256. Les fonctionnalités expérimentales et les limites de compatibilité sont détaillées dans les guides.

<a id="start-here"></a>
## Bien démarrer

1. Choisissez l'outil adapté à votre besoin. Chaque programme fonctionne séparément.
2. Consultez ses prérequis, puis choisissez **Setup** pour l'installer ou **portable** pour un dossier autonome.
3. Une fois sa Release publiée, téléchargez le fichier applicatif indiqué, lisez les notices et comparez son SHA-256.
4. Conservez des sauvegardes avant de modifier un pilote, l'écran, un profil NVIDIA ou les fichiers d'un jeu.

La documentation existe dans les mêmes 34 langues que les logiciels NV grâce au sélecteur en haut des guides. GitHub ne choisit pas automatiquement le README selon la langue du navigateur. La langue de la documentation et celle du programme se règlent séparément.

<a id="provenance-and-ownership"></a>
## Provenance et droits

Ce hub distribue la documentation et les applications compilées. Leurs sources sont maintenues en privé. Les auteurs et licences des composants upstream restent identifiés ; conserver les sources privées ne remplace pas ces licences.

- La fork Profile Inspector conserve la licence MIT d'Orbmu2k et indique explicitement sa provenance.
- NVDriverForge possède ses propres conditions de distribution binaire et inclut des composants sous d'autres licences.
- NVMFG Unlock40 est une application développée indépendamment. RTX40MFG-Unlock a servi de comparaison et de perfectionnement ; les composants natifs partagés conservent leurs crédits MIT. MinHook et les conditions des SDK NVIDIA restent distincts.
- NVRasterPulse conserve la licence MIT fournie et les crédits de l'interface issue de Profile Inspector. RTSS est un programme externe requis.

Consultez le [tableau complet des composants](THIRD_PARTY_NOTICES.md), la [provenance et les modifications](docs/provenance.fr.md), ainsi que le [périmètre des licences](LICENSE).

<a id="other-projects--revolusound-team"></a>
## Autres projets – RevoluSound Team

Ces mods audio sont des projets séparés, présentés ici pour découvrir les autres travaux de l'équipe.

| Jeu | Projet | Présentation |
| --- | --- | --- |
| Forza Horizon 6 | [Forza Horizon 6 Revolusound Team Pack](https://www.nexusmods.com/forzahorizon6/mods/56) | Modifications des sons de moteurs, échappements, admissions et turbos. |
| Forza Horizon 5 | [Forza Horizon 5 Revolusound Team Pack 1.4.4 FINAL](https://www.nexusmods.com/forzahorizon5/mods/86) | Pack audio automobile FH5 plus récent de l'équipe. |
| Forza Horizon 5 | [Forza Horizon 5.5 Zendo Revolusound Pack](https://www.nexusmods.com/forzahorizon5/mods/20) | Ancien pack FH5 ; sa page Nexus renvoie vers le pack de l'équipe ci-dessus. |

Les titres correspondent aux pages Nexus Mods. Téléchargements, prérequis, crédits et permissions restent disponibles sur ces pages.

<a id="help-and-participation"></a>
## Aide et participation

[Signaler un bug ou proposer une fonction](https://github.com/Zendo-GIT/NV-Laboratory/issues) · [Contribuer](CONTRIBUTING.md) · [Sécurité](SECURITY.md) · [Historique](CHANGELOG.md)

Consultez SECURITY.md avant de publier les détails d'une faille ou des journaux. Le signalement privé devra être activé par le mainteneur après la publication du dépôt.

> **Projets communautaires indépendants.** NV Laboratory, NV Tools et ces utilitaires ne sont ni affiliés à NVIDIA Corporation, ni sponsorisés ou officiellement approuvés par celle-ci. NVIDIA, GeForce, RTX, DLSS et les autres noms de produits sont les marques de leurs propriétaires respectifs. Ils indiquent une compatibilité ou une provenance, sans approbation officielle.
