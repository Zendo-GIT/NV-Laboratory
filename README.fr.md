🌐 **Langue :** [English](README.md) | Français

# NV Laboratory

**NV Tools par 禅堂 Zendo (RevoluSound Team).** Quatre utilitaires Windows indépendants pour les profils et pilotes NVIDIA, la Multi Frame Generation expérimentale et les limites FPS RTSS.

[Téléchargements](docs/downloads.fr.md) · [Installation](docs/installation.fr.md) · [Compatibilité et aide](docs/support.fr.md) · [Crédits et licences](THIRD_PARTY_NOTICES.md)

> **NVRasterPulse nécessite RTSS.** Installez d'abord [RivaTuner Statistics Server depuis Guru3D](https://www.guru3d.com/download/rtss-rivatuner-statistics-server-download/). RTSS doit fonctionner pour appliquer ses limites FPS. Son téléchargement est séparé.

## Projets

| Projet | Utilité | Version candidate | Documentation | Téléchargement |
| --- | --- | --- | --- | --- |
| **NVIDIA Profile Inspector – NV Tools Fork** | Éditeur de profils NVIDIA enrichi de réglages écran, couleurs, HDR et ICC/WCS. Anciennement NVPI Custom. | 3.0.2.3 | [Guide](NVIDIA-Profile-Inspector/README.fr.md) | [Paquets](docs/downloads.fr.md#nvidia-profile-inspector) |
| **NVDriverForge** | Choisir les composants du pilote, examiner les réglages facultatifs et installer un paquet NVIDIA original. | 0.1.2 | [Guide](NVDriverForge/README.fr.md) | [Paquets](docs/downloads.fr.md#nvdriverforge) |
| **NVMFG Unlock40** | Outil MFG expérimental pour RTX 40, avec choix par jeu et maintenance des SDK Streamline. Dérivé de RTX40MFG-Unlock. | 0.1.1 | [Guide](NVMFG-Unlock40/README.fr.md) | [Paquets et statut](docs/downloads.fr.md#nvmfg-unlock40) |
| **NVRasterPulse** | Gérer les limites FPS RTSS par exécutable, avec valeurs fractionnaires, sauvegardes et accès depuis la zone de notification. | 0.1 | [Guide](NVRasterPulse/README.fr.md) | [Paquets](docs/downloads.fr.md#nvrasterpulse) |

**État de publication :** premières versions candidates préparées. Aucun téléchargement GitHub n'est encore publié. La [page de téléchargement](docs/downloads.fr.md) identifie les fichiers et les pages de Release prévues. Une archive du dépôt contient la documentation, pas les installateurs. Les fonctions expérimentales et les limites des validations matérielles sont détaillées dans chaque guide.

## Bien démarrer

1. Choisissez l'outil adapté à votre besoin. Chaque programme fonctionne séparément.
2. Consultez ses prérequis, puis choisissez **Setup** pour l'installer ou **portable** pour un dossier autonome.
3. Une fois sa Release publiée, téléchargez le fichier applicatif indiqué, lisez les notices et comparez son SHA-256.
4. Conservez des sauvegardes avant de modifier un pilote, l'écran, un profil NVIDIA ou les fichiers d'un jeu.

La documentation existe en anglais et en français grâce au sélecteur en haut des guides. GitHub ne choisit pas automatiquement le README selon la langue du navigateur. La langue de la documentation et celle du programme se règlent séparément.

## Provenance et droits

Ce hub distribue la documentation et les applications compilées. Leurs sources sont maintenues en privé. Les auteurs et licences des composants upstream restent identifiés ; conserver les sources privées ne remplace pas ces licences.

- La fork Profile Inspector conserve la licence MIT d'Orbmu2k et indique explicitement sa provenance.
- NVDriverForge possède ses propres conditions de distribution binaire et inclut des composants sous d'autres licences.
- Le moteur de NVMFG Unlock40 dérive de RTX40MFG-Unlock de Michael Robles. Ses composants MIT, MinHook et les conditions des SDK NVIDIA restent distincts.
- NVRasterPulse conserve la licence MIT fournie et les crédits de l'interface issue de Profile Inspector. RTSS est un programme externe requis.

Consultez le [tableau complet des composants](THIRD_PARTY_NOTICES.md), la [provenance et les modifications](docs/provenance.fr.md), ainsi que le [périmètre des licences](LICENSE).

## Autres projets – RevoluSound Team

Ces mods audio sont des projets séparés, présentés ici pour découvrir les autres travaux de l'équipe.

| Jeu | Projet | Présentation |
| --- | --- | --- |
| Forza Horizon 6 | [Forza Horizon 6 Revolusound Team Pack](https://www.nexusmods.com/forzahorizon6/mods/56) | Modifications des sons de moteurs, échappements, admissions et turbos. |
| Forza Horizon 5 | [Forza Horizon 5 Revolusound Team Pack 1.4.4 FINAL](https://www.nexusmods.com/forzahorizon5/mods/86) | Pack audio automobile FH5 plus récent de l'équipe. |
| Forza Horizon 5 | [Forza Horizon 5.5 Zendo Revolusound Pack](https://www.nexusmods.com/forzahorizon5/mods/20) | Ancien pack FH5 ; sa page Nexus renvoie vers le pack de l'équipe ci-dessus. |

Les titres correspondent aux pages Nexus Mods. Téléchargements, prérequis, crédits et permissions restent disponibles sur ces pages.

## Aide et participation

[Signaler un bug ou proposer une fonction](https://github.com/Zendo-GIT/NV-Laboratory/issues) · [Contribuer](CONTRIBUTING.md) · [Sécurité](SECURITY.md) · [Historique](CHANGELOG.md)

Consultez SECURITY.md avant de publier les détails d'une faille ou des journaux. Le signalement privé devra être activé par le mainteneur après la publication du dépôt.

> **Projets communautaires indépendants.** NV Laboratory, NV Tools et ces utilitaires ne sont ni affiliés à NVIDIA Corporation, ni sponsorisés ou officiellement approuvés par celle-ci. NVIDIA, GeForce, RTX, DLSS et les autres noms de produits sont les marques de leurs propriétaires respectifs. Ils indiquent une compatibilité ou une provenance, sans approbation officielle.
