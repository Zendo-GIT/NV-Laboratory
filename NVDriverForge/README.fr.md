🌐 **Langue :** [English](README.md) | Français · [NV Laboratory](../README.fr.md)

# NVDriverForge

**Préparer l'installation d'un pilote NVIDIA avec des choix de composants et de réglages compréhensibles.**

[Télécharger 0.1.2 et consulter le statut](../docs/downloads.fr.md#nvdriverforge) · [Installation](#installation) · [Crédits](#crédits-et-origine) · [Licence](LICENSE)

## Présentation et raison d'être

NVDriverForge guide l'utilisateur à partir d'un paquet NVIDIA original :
choisir le pilote, examiner ses composants, sélectionner les réglages facultatifs,
puis confirmer l'installation. Il réunit ces choix, les opérations privilégiées
et les informations de récupération dans un même parcours.

C'est une application développée indépendamment, inspirée notamment du parcours
NVCleanstall. Elle n'inclut pas ce logiciel et ne revendique pas toutes ses fonctions.

## Fonctionnalités

- Recherche et téléchargement NVIDIA Game Ready / Studio ; recherche hotfix facultative avec repli manuel.
- Analyse du paquet original, empreintes, signatures NVIDIA, manifestes et entrées INF compatibles.
- Choix des composants avec dépendances et conservation des composants inconnus.
- Confirmation d'installation, préparation dans un espace protégé et export des pilotes existants du magasin Windows.
- Réglages avancés facultatifs avec contrôles préalables, journaux et récupération tenant compte des conflits.
- Preset **Custom NV** facultatif, choix nommés, explications, force SILK distincte et contrôles de compatibilité.
- Téléchargement facultatif de données NVENC correspondant exactement à une version et à un commit upstream.
- Installation séparée et facultative de la fork Profile Inspector depuis les outils.
- Vérifications de mises à jour facultatives pour l'application installée, 34 langues et quatre thèmes.

Les réglages avancés concernent MPO, l'indicateur DLSS, Ansel, la veille audio NVIDIA,
MSI, la politique/priorité des interruptions, HDCP, le démarrage du conteneur
d'affichage et un ancien service de télémétrie admissible. Chacun a ses prérequis
et contreparties ; aucun n'est une optimisation universelle.

## Compatibilité

| Prérequis | Détails |
| --- | --- |
| Système | Windows 10 build 19041 ou ultérieur / Windows 11, x64 |
| GPU/pilote | Paquet NVIDIA et matériel compatibles ; catalogue automatique surtout destiné aux modèles GeForce connus |
| Runtime | .NET 8 / WPF 8.0.30 inclus dans le paquet autonome préparé |
| Droits | Interface et Setup par utilisateur ; élévation pour le pilote et les changements système |
| Réseau | Recherche/téléchargement NVIDIA et demandes NVENC explicites ; sélection possible d'un paquet local original |
| Outils inclus | 7-Zip 26.03 non modifié, runtime et notices, compagnon Profile Inspector MIT facultatif |
| Compagnon | .NET Framework 4.8 pour la fork Profile Inspector séparée |

Aucune version minimale de pilote ne couvre toutes les fonctions. En multi-GPU,
le catalogue doit convenir à tous les GPU détectés. Certains modèles professionnels
ou inconnus demandent une sélection manuelle. L'installateur NVIDIA reste l'autorité
finale pour la compatibilité matérielle et Windows.

## Installation

1. Consultez les [téléchargements](../docs/downloads.fr.md#nvdriverforge) et leur statut.
2. Choisissez `NVDriverForge-Setup.exe` pour l'installation ou `NVDriverForge.exe` pour le portable.
3. Comparez le SHA-256 à `SHA256SUMS.txt` de la Release.
4. Lancez le Setup pour une installation par utilisateur avec désinstallateur, ou ouvrez le portable depuis un dossier accessible en écriture.

Le portable inclut son runtime et son installateur facultatif. Installer NVDriverForge
n'installe pas de pilote graphique. Les EXE existants ne sont pas signés.

## Utilisation

1. **Pilote :** téléchargez depuis NVIDIA ou sélectionnez son installateur EXE original. Attendez la fin de l'analyse.
2. **Composants :** consultez les descriptions et dépendances. Les éléments inconnus sont conservés.
3. **Réglages :** laissez inchangées les options inutiles. Lisez leurs effets et contreparties.
4. **Confirmation :** vérifiez pilote, composants et opérations, puis confirmez l'installation.
5. Acceptez l'UAC correspondant à votre choix et conservez les instructions du travail protégé.
6. Si un redémarrage est requis, suivez l'état annoncé. Les opérations différées demandent une reprise explicite après ce redémarrage.

Custom NV commence sans changement. Sélectionnez les valeurs par leur nom ou
examinez le preset proposé et ses exclusions. Les deux champs internes informatifs
ne sont pas écrits indépendamment. L'application des réglages se fait dans le
parcours du nouveau pilote vérifié, jamais en ouvrant l'aperçu. NVPI est facultatif.

L'option NVENC télécharge des données compatibles d'un commit keylase figé.
Elle modifie deux DLL du pilote et invalide leurs signatures : Windows, les
encodeurs, DRM ou anti-cheats peuvent les refuser. Aucune de ces données ni DLL
NVIDIA n'est intégrée au paquet NVDriverForge. [Provenance](../docs/provenance.fr.md).

Les préférences règlent langue, thème et recherches facultatives de l'application
installée. Le portable ne crée pas sa tâche de surveillance. Les outils et la
récupération sont séparés des quatre étapes d'installation.

## Captures

![Aperçu de la page pilote NVDriverForge](../assets/screenshots/nvdriverforge-0.1.2-preview.png)

Rendu existant en français, avec données d'exemple. Le pilote 699.99 affiché est
une donnée de test, pas une version à télécharger. [Provenance](../assets/README.md).

## Mise à jour et désinstallation

Fermez NVDriverForge, récupérez le nouveau paquet officiel et vérifiez son empreinte.
Utilisez la même identité Setup ou remplacez l'EXE portable fermé. Conservez les
réglages et travaux protégés.

La désinstallation Windows retire l'application et sa tâche, pas le pilote NVIDIA.
Réglages, journaux et sauvegardes restent présents. Restaurez si souhaité les
changements avancés/NVENC via la récupération **avant** de désinstaller.
Une restauration refuse d'écraser des changements incompatibles d'un autre outil.

Données : `%LOCALAPPDATA%\NVDriverForge`. Travaux protégés et exports :
`%PROGRAMDATA%\NVDriverForge\Jobs`. Le portable écrit aussi des données locales.
L'export du magasin de pilotes n'est ni une image système ni une sauvegarde complète
des profils NVIDIA.

## Limitations connues

- Pas d'ajout de matériel/édition INF, de nouvelles signatures NVIDIA, de signature certifiée anti-cheat ou d'acceptation automatique des avertissements de signature.
- Pas de retrait complet des publicités/télémétries, d'export d'un paquet allégé ou de retour automatique complet à l'ancien pilote.
- L'audit du hub ne certifie pas l'installation réelle, la récupération après redémarrage ou les écritures de profils sur toutes les machines.
- Une relecture du registre ne prouve pas l'effet réel sur HDCP, les performances ou la latence.
- Vérification de confiance Windows locale, sans révocation en ligne.
- 34 langues présentes ; relecture native et tests complets d'accessibilité encore incomplets.

## Dépannage

| Symptôme | Action |
| --- | --- |
| Catalogue indisponible | Choisissez un paquet original depuis [NVIDIA](https://www.nvidia.com/en-us/drivers/), sans remplacer votre modèle par un voisin. |
| Recherche hotfix indisponible | Consultez le [forum NVIDIA Game Ready](https://www.nvidia.com/en-us/geforce/forums/game-ready-drivers/13/). |
| Échec de signature, hash ou sauvegarde | Arrêtez cette installation et conservez l'erreur ; retéléchargez le paquet original s'il est corrompu. |
| Option indisponible | Lisez le motif matériel/composant/pilote et laissez-la inchangée. |
| Redémarrage ou travail en attente | Suivez les instructions de récupération et de reprise, sans effacer le journal. |
| Conflit de restauration | Préservez le changement extérieur et demandez de l'aide au lieu de forcer. |

Indiquez version, Windows, GPU, pilote et étapes reproductibles. Masquez les chemins
et données personnelles des journaux. [Aide commune](../docs/support.fr.md).

## FAQ

**Le Setup installe-t-il un pilote ?** Non : le programme exige une analyse,
un examen, une confirmation et une installation élevée distincts.

**Faut-il NVCleanstall ou NVPI ?** Non. Le premier sert d'inspiration ; le second
est un éditeur facultatif séparé.

**Tous les pilotes seront-ils plus petits ou rapides ?** Non. Les composants
et prérequis déterminent les changements ; aucun gain mesuré n'est promis.

**Où sont les sources ?** Le code applicatif et les tests restent privés.
Le hub fournit documents, binaires et liens des tiers nécessaires à leurs licences.

## Crédits et origine

Application originale, parcours, transactions, traductions, bootstrap et adaptations :
禅堂 Zendo (RevoluSound Team).

- [NVCleanstall / TechPowerUp](https://www.techpowerup.com/download/techpowerup-nvcleanstall/) : inspiration ; aucun code ou binaire importé.
- [NVIDIA Profile Inspector / Orbmu2k](https://github.com/Orbmu2k/nvidiaProfileInspector) : thèmes MIT, référence NVAPI étendue et fork séparée.
- [7-Zip / Igor Pavlov](https://www.7-zip.org/) : extraction, binaires non modifiés.
- [Microsoft .NET](https://github.com/dotnet/runtime) et [WPF](https://github.com/dotnet/wpf) : runtime inclus.
- [Inno Setup](https://jrsoftware.org/isinfo.php) : moteur d'installation original et traductions créditées.
- [keylase/nvidia-patch](https://github.com/keylase/nvidia-patch) : données NVENC externes facultatives ; licence de redistribution non établie.
- [NVIDIA](https://www.nvidia.com/en-us/drivers/) : pilotes et bibliothèques NVAPI/NVML installées.

[Tableau complet](../THIRD_PARTY_NOTICES.md) · [Modifications et provenance](../docs/provenance.fr.md)

## Licence

La [permission binaire existante](LICENSE) autorise l'utilisation et le partage
des exécutables officiels non modifiés avec leurs notices. Les droits sur le code
applicatif propre restent réservés ; ceux des composants tiers sont préservés.
[Notices complètes](LICENSES/README.md).

Indépendant de NVIDIA Corporation, TechPowerUp et keylase, sans sponsoring ou
approbation officielle. Les marques restent à leurs propriétaires.
