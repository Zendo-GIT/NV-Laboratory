🌐 **Langue :** [English](support.md) | Français · [Accueil](../README.fr.md)

# Compatibilité et dépannage

Ce tableau décrit les candidates préparées, sans certifier toutes les combinaisons
Windows, GPU, pilote et jeu.

| Outil | Windows / runtime | Matériel / dépendance externe | Opérations à examiner |
| --- | --- | --- | --- |
| Fork NVPI 3.0.2.3 | Windows 10/11 x64, .NET Framework 4.8 | Pilote NVIDIA/écran compatibles | Profils et aperçus écran |
| NVDriverForge 0.1.2 | Windows 10 build 19041+ / 11 x64, .NET/WPF inclus | Paquet NVIDIA compatible | Installation élevée, réglages et NVENC facultatifs |
| NVMFG Unlock40 0.1.1 | Windows 10/11 x64, .NET/WPF inclus et helpers Framework 4.8 | RTX 40, DLSS FG admissible et fournisseur figé | Patch natif, profils globaux et SDK de jeux |
| NVRasterPulse 0.1 | Windows 10/11 x64, .NET Framework 4.8 | RTSS installé, lancé pour limiter | Profils RTSS par exécutable |

Aucun paquet ARM64 n'est préparé. Les API d'affichage et versions Windows anciennes
peuvent limiter certaines fonctions. Aucune version minimale universelle de pilote
ou RTSS n'est inventée. Le hash fournisseur NVMFG figure dans la [provenance](provenance.fr.md).

## Avant de signaler un bug

Identifiez la version et l'EXE réellement ouverts. Une ancienne installation
ne devient pas la version du ZIP téléchargé. Notez étapes, résultat attendu et
résultat observé. Pour affichage/limiteur, précisez jeu, fréquence écran, états
FG/V-Sync/VRR et autres limiteurs/overlays.

Utilisez le [formulaire de bug](https://github.com/Zendo-GIT/NV-Laboratory/issues/new?template=bug-report.yml).
Ne joignez pas un dossier de développement, paquet pilote, modèle, DLL de jeu,
export complet du registre ou collection de journaux non relue.

| Problème | Premières vérifications |
| --- | --- |
| Mauvaise version ouverte | Identifiez l'EXE et son hash ; fermez l'ancienne copie avant remplacement. |
| Erreur de runtime/démarrage | Installez Framework 4.8 si requis ou conservez tous les sous-dossiers portables. |
| UAC annulé | Reprenez seulement l'opération voulue ; annulation ne signifie pas installation réussie. |
| Hash/signature différent | Arrêtez l'utilisation de cette candidate et récupérez les octets officiels attendus. |
| Mode/couleur NVPI refusé | Revenez à l'état antérieur et à une combinaison prise en charge. |
| Échec NVDF de sauvegarde/récupération | Préservez travail protégé et RECOVERY.txt, sans effacer le journal ni forcer les conflits. |
| Réglages NVMFG en attente | Résolvez la récupération, jeux fermés et changements extérieurs conservés. |
| Limite RP sans effet | Lancez RTSS, identifiez l'EXE réel, le hook et les autres limiteurs. |
| Limite RP persistante après retrait | Vérifiez Global RTSS ; seul l'override local est retiré. |

## Journaux et vie privée

| Outil | Données locales à examiner, sans envoi intégral |
| --- | --- |
| NVDF | `%LOCALAPPDATA%\NVDriverForge` ; travaux `%PROGRAMDATA%\NVDriverForge\Jobs` |
| NVMFG | `%LOCALAPPDATA%\RtxMfg` ; backups `%LOCALAPPDATA%\NvidiaStreamlineMaintenance\Backups` ; `Sessions` près de l'EXE |
| RP | `%LOCALAPPDATA%\NVRasterPulse`, puis `Backups\RTSS` |
| NVPI | Vos exports et l'erreur affichée ; aucun chemin universel de journal n'est supposé |

Masquez comptes, dossiers personnels, bibliothèques de jeux, identifiants de
périphérique, tokens et fenêtres sans rapport. Gardez les originaux en privé pour
la récupération. Les Issues publiques sont visibles par tous.

Pour une vulnérabilité, un comportement privilégié dangereux ou une opération
destructive imprévue, suivez [SECURITY.md](../SECURITY.md) sans en publier les détails.

## Vérifications effectuées

La préparation du hub a rejoué les audits statiques de payload/ZIP/hash/métadonnées
et les vérifications documentaires. Les tests privés de build/unité/UI sont des
preuves historiques datées. Aucun pilote installé, réglage écran modifié, vrai
RTSS manipulé ou benchmark en jeu dans cette préparation.

« Détecté », « écrit », « rechargé », « capacité disponible » et « mesuré en jeu »
sont des résultats différents : indiquez celui observé.
