<!-- nv-language-navigation:start -->
🌐 [English](support.md) | Français · [NV Laboratory](../README.fr.md)

<details>
<summary>🌐 Language · 34</summary>

[العربية](languages/ar/docs/support.md) · [বাংলা](languages/bn/docs/support.md) · [简体中文](languages/zh/docs/support.md) · [Čeština](languages/cs/docs/support.md) · [Dansk](languages/da/docs/support.md) · [Nederlands](languages/nl/docs/support.md) · [English](support.md) · [Filipino](languages/fil/docs/support.md) · [Suomi](languages/fi/docs/support.md) · **Français** · [Deutsch](languages/de/docs/support.md) · [Ελληνικά](languages/el/docs/support.md) · [हिन्दी](languages/hi/docs/support.md) · [Magyar](languages/hu/docs/support.md) · [Bahasa Indonesia](languages/id/docs/support.md) · [Italiano](languages/it/docs/support.md) · [日本語](languages/ja/docs/support.md) · [한국어](languages/ko/docs/support.md) · [मराठी](languages/mr/docs/support.md) · [فارسی](languages/fa/docs/support.md) · [Polski](languages/pl/docs/support.md) · [Português](languages/pt/docs/support.md) · [ਪੰਜਾਬੀ](languages/pa/docs/support.md) · [Română](languages/ro/docs/support.md) · [Русский](languages/ru/docs/support.md) · [Español](languages/es/docs/support.md) · [Kiswahili](languages/sw/docs/support.md) · [Svenska](languages/sv/docs/support.md) · [தமிழ்](languages/ta/docs/support.md) · [ไทย](languages/th/docs/support.md) · [Türkçe](languages/tr/docs/support.md) · [Українська](languages/uk/docs/support.md) · [اردو](languages/ur/docs/support.md) · [Tiếng Việt](languages/vi/docs/support.md)

[Translation policy](languages/README.md)

</details>
<!-- nv-language-navigation:end -->

<a id="compatibility-and-troubleshooting"></a>
# Compatibilité et dépannage

Ce tableau décrit les candidates préparées, sans certifier toutes les combinaisons
Windows, GPU, pilote et jeu.

| Outil | Windows / runtime | Matériel / dépendance externe | Opérations à examiner |
| --- | --- | --- | --- |
| Fork NVPI 3.0.2.3 | Windows 10/11 x64, .NET Framework 4.8 | Pilote NVIDIA/écran compatibles | Profils et aperçus écran |
| NVDriverForge 0.1.4 | Windows 10 build 19041+ / 11 x64, .NET/WPF inclus | Paquet NVIDIA compatible | Installation élevée, réglages et NVENC facultatifs |
| NVMFG Unlock40 0.2.3 | Windows 10/11 x64, .NET/WPF inclus et helpers Framework 4.8 | RTX 40, DLSS FG admissible et fournisseur figé | Patch natif, profils globaux et SDK de jeux |
| NVRasterPulse 0.2 | Windows 10/11 x64, .NET Framework 4.8 | RTSS installé, lancé pour limiter | Profils RTSS par exécutable |

Aucun paquet ARM64 n'est préparé. Les API d'affichage et versions Windows anciennes
peuvent limiter certaines fonctions. Aucune version minimale universelle de pilote
ou RTSS n'est inventée. Le hash fournisseur NVMFG figure dans la [provenance](provenance.fr.md).

<a id="before-reporting-a-bug"></a>
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

NVDriverForge propose un rapport JSON local avec aperçu ; NVMFG propose un diagnostic dans À propos. Préférez ces rapports filtrés à une archive complète des journaux et vérifiez leur contenu avant partage. Un blocage de restauration signalé sur NVMFG 0.1.1 reste sans cause établie ; conservez son journal et relevez le code d'erreur disponible. NVRasterPulse 0.2 fournit un diagnostic de configuration dans son menu d'actions, sans mesure de FPS.

<a id="logs-and-privacy"></a>
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

<a id="what-has-been-verified"></a>
## Vérifications effectuées

La préparation du hub a rejoué les audits statiques de payload/ZIP/hash/métadonnées
et les vérifications documentaires. Les tests privés de build/unité/UI sont des
preuves historiques datées. Aucun pilote installé, réglage écran modifié, vrai
RTSS manipulé ou benchmark en jeu dans cette préparation.

« Détecté », « écrit », « rechargé », « capacité disponible » et « mesuré en jeu »
sont des résultats différents : indiquez celui observé.
