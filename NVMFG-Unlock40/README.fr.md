<!-- nv-language-navigation:start -->
🌐 [English](README.md) | Français · [NV Laboratory](../README.fr.md)

<details>
<summary>🌐 Language · 34</summary>

[العربية](../docs/languages/ar/NVMFG-Unlock40/README.md) · [বাংলা](../docs/languages/bn/NVMFG-Unlock40/README.md) · [简体中文](../docs/languages/zh/NVMFG-Unlock40/README.md) · [Čeština](../docs/languages/cs/NVMFG-Unlock40/README.md) · [Dansk](../docs/languages/da/NVMFG-Unlock40/README.md) · [Nederlands](../docs/languages/nl/NVMFG-Unlock40/README.md) · [English](README.md) · [Filipino](../docs/languages/fil/NVMFG-Unlock40/README.md) · [Suomi](../docs/languages/fi/NVMFG-Unlock40/README.md) · **Français** · [Deutsch](../docs/languages/de/NVMFG-Unlock40/README.md) · [Ελληνικά](../docs/languages/el/NVMFG-Unlock40/README.md) · [हिन्दी](../docs/languages/hi/NVMFG-Unlock40/README.md) · [Magyar](../docs/languages/hu/NVMFG-Unlock40/README.md) · [Bahasa Indonesia](../docs/languages/id/NVMFG-Unlock40/README.md) · [Italiano](../docs/languages/it/NVMFG-Unlock40/README.md) · [日本語](../docs/languages/ja/NVMFG-Unlock40/README.md) · [한국어](../docs/languages/ko/NVMFG-Unlock40/README.md) · [मराठी](../docs/languages/mr/NVMFG-Unlock40/README.md) · [فارسی](../docs/languages/fa/NVMFG-Unlock40/README.md) · [Polski](../docs/languages/pl/NVMFG-Unlock40/README.md) · [Português](../docs/languages/pt/NVMFG-Unlock40/README.md) · [ਪੰਜਾਬੀ](../docs/languages/pa/NVMFG-Unlock40/README.md) · [Română](../docs/languages/ro/NVMFG-Unlock40/README.md) · [Русский](../docs/languages/ru/NVMFG-Unlock40/README.md) · [Español](../docs/languages/es/NVMFG-Unlock40/README.md) · [Kiswahili](../docs/languages/sw/NVMFG-Unlock40/README.md) · [Svenska](../docs/languages/sv/NVMFG-Unlock40/README.md) · [தமிழ்](../docs/languages/ta/NVMFG-Unlock40/README.md) · [ไทย](../docs/languages/th/NVMFG-Unlock40/README.md) · [Türkçe](../docs/languages/tr/NVMFG-Unlock40/README.md) · [Українська](../docs/languages/uk/NVMFG-Unlock40/README.md) · [اردو](../docs/languages/ur/NVMFG-Unlock40/README.md) · [Tiếng Việt](../docs/languages/vi/NVMFG-Unlock40/README.md)

[Translation policy](../docs/languages/README.md)

</details>
<!-- nv-language-navigation:end -->

<a id="nvmfg-unlock40"></a>
# NVMFG Unlock40

**Multi Frame Generation NVIDIA expérimentale pour GeForce RTX 40, avec contrôleur central et choix par jeu.**

[Télécharger 0.1.1 et consulter le statut](../docs/downloads.fr.md#nvmfg-unlock40) · [Installation](#installation) · [Origine](#origine-et-modifications) · [Licences](LICENSES/README.md)

<a id="overview-and-purpose"></a>
## Présentation et raison d'être

NVMFG Unlock40 est une application développée indépendamment par
禅堂 Zendo (RevoluSound Team). Elle réunit un contrôleur Windows, une couche native,
un helper de profils et la gestion des jeux/SDK Streamline. Elle cible les jeux
intégrant déjà NVIDIA DLSS Frame Generation avec des runtimes compatibles.

[RTX40MFG-Unlock](https://github.com/dashdogy/RTX40MFG-Unlock) a été consulté pour
comparer et parfaire le travail. La couche native actuelle contient des composants
partagés et adaptés, crédités individuellement ci-dessous. Cette référence ne fait
pas de l'application NVMFG entière une fork de ce projet.

Il coordonne le MFG expérimental, mémorise les choix propres aux jeux et rend
visibles les mises à jour de runtimes et leurs sauvegardes. Il n'ajoute pas DLSS FG
à tous les jeux et ne convertit pas une implémentation FSR quelconque.

La candidate **0.1.1** inclut la correction visuelle de la liste SDK appelée
UI2 dans l'historique interne. Sa version publique reste 0.1.1 ; ses empreintes
exactes la distinguent des anciens builds locaux.

<a id="features"></a>
## Fonctionnalités

- Activation/désactivation centrale et démarrage Windows facultatif dans la zone de notification.
- Choix par jeu entre Dynamic MFG, réglage du jeu et multiplicateurs fixes admissibles.
- Choix distincts mémorisés selon l'état V-Sync observé.
- Mode Dynamic NVIDIA suspendu sans V-Sync, avec choix séparé du réglage en jeu ou d'un multiplicateur fixe.
- Questionnaire sur le menu du jeu et exclusions persistantes ; les jeux sans DLSS FG restent autonomes.
- Découverte, sélection depuis un dossier parent, recherche, regroupement et retrait sans supprimer les jeux.
- Téléchargement/import de SDK Streamline, cache vérifié, sélection explicite, sauvegarde et restauration par jeu.
- Vérification du fournisseur natif, diagnostics de session, journal des profils globaux et récupération avec conflits.
- 34 langues et quatre thèmes.

Désactiver FG dans le jeu le laisse désactivé. Les choix de 2x à 6x dépendent du
jeu, du menu et du runtime ; toutes les combinaisons ne sont pas garanties.
Le contrôleur observe V-Sync sans modifier lui-même V-Sync ou VRR.

<a id="compatibility"></a>
## Compatibilité

| Prérequis | Détails |
| --- | --- |
| Système | Windows 10/11 x64 |
| GPU | Cible GeForce RTX 40, sans garantie pour tous les GPU |
| Jeu | Intégration DLSS Frame Generation existante et runtime admissible ; aucune certification anti-cheat |
| Fournisseur | SHA-256 figé dans la candidate, décrit dans la [provenance](../docs/provenance.fr.md) ; hash inconnu refusé |
| Runtime | .NET 8/WPF 8.0.30 inclus pour l'application/agent ; .NET Framework 4.8 pour les helpers |
| Droits | Administrateur pour le contrôleur et les opérations de profils |
| Réseau | Téléchargements SDK choisis ; cache local possible après import compatible |
| Binaires externes | Aucun pilote NVIDIA, fournisseur/modèle NGX ou runtime Streamline inclus |

Le numéro de version ne suffit pas : pilote, hash du fournisseur, intégration du
jeu et modules réellement chargés comptent. Les processus protégés ou incompatibles
peuvent refuser l'attachement. Le programme ne vise pas à contourner les anti-cheats.

<a id="installation"></a>
## Installation

1. Consultez le [statut de la candidate et la note de licence](../docs/downloads.fr.md#nvmfg-unlock40).
2. Une fois publié, téléchargez `NVMFGUnlock40-0.1.1-Setup-x64.exe` ou `NVMFGUnlock40-0.1.1-Portable-x64.zip`.
3. Vérifiez le SHA-256 et gardez les notices. Installez .NET Framework 4.8 s'il n'est pas déjà fourni par Windows.
4. Lancez le Setup ou extrayez **tout** le ZIP dans un dossier local accessible en écriture.
5. Ouvrez `NVMFGUnlock40.exe`, en conservant `agent`, `driver`, `engine` et `Licenses`.

Le dossier `driver` contient des helpers en espace utilisateur, pas un pilote noyau.
Ne copiez pas uniquement l'EXE et ne remplacez pas le hash pour forcer la compatibilité.
Les exécutables actuels ne sont pas signés.

<a id="usage"></a>
## Utilisation

1. Commencez contrôleur désactivé. Ajoutez un jeu ou un dossier parent, puis choisissez les installations réelles.
2. Examinez les réglages MFG du jeu. Indiquez ce que son menu propose ; cette réponse sera mémorisée.
3. Choisissez globalement Dynamic ou le réglage en jeu, puis adaptez les choix par jeu.
4. Activez le contrôleur uniquement au moment voulu. Il peut modifier temporairement six réglages globaux NVIDIA, avec journal de récupération.
5. Lancez un jeu admissible et activez son DLSS Frame Generation. Répondez si nécessaire au choix sans V-Sync.
6. Excluez les jeux à laisser autonomes. Retirer un jeu mémorise une exclusion et conserve fichiers et sauvegardes.
7. Utilisez la désactivation/fermeture complète et la récupération prévues dans l'application.

Fermer la fenêtre peut laisser le contrôleur actif dans la zone de notification.
Une DLL déjà chargée reste dans le jeu jusqu'à sa fermeture ; désactiver le contrôleur
ne garantit pas son déchargement. Fermez les jeux avant maintenance ou mise à jour.

**SDK Streamline :** téléchargez une version officielle ou importez un SDK local
compatible. L'import en garde une copie vérifiée ; **Use this version** la sélectionne,
**Uninstall** retire cette copie du cache. Les DLL Streamline manquantes peuvent
être complétées depuis un SDK officiel, avec provenance affichée. Cela ne remplace
pas un modèle NGX. Fermez le jeu, choisissez sa mise à jour et gardez sa sauvegarde.
Pour restaurer ses fichiers, utilisez la restauration du jeu, pas le bouton de
désinstallation du cache SDK.

<a id="screenshots"></a>
## Captures

![Aperçu de la liste SDK NVMFG](../assets/screenshots/nvmfg-0.1.1-sdk-preview.png)

Rendu existant en anglais de 0.1.1, avec inventaire SDK d'exemple.
Ce n'est ni une liste officielle actuelle ni une preuve d'exécution en jeu.
[Provenance](../assets/README.md).

<a id="update-and-uninstall"></a>
## Mise à jour et désinstallation

Fermez les jeux, désactivez/quittez NVMFG et résolvez toute récupération NVIDIA en
attente avant la mise à jour. Gardez la même identité Setup ou extrayez le nouveau
portable dans un dossier neuf, en conservant état et sauvegardes.

Avant désinstallation, restaurez si souhaité les SDK des jeux et les réglages
NVIDIA via l'application. Fermez les jeux et le contrôleur. Utilisez **Applications
installées** pour Setup, ou retirez le dossier portable fermé après sauvegarde.
N'effacez pas un journal de récupération actif pour débloquer le Setup.

Les sauvegardes de runtimes sont sous
`%LOCALAPPDATA%\NvidiaStreamlineMaintenance\Backups`. Réglages MFG/cache SDK :
`%LOCALAPPDATA%\RtxMfg`. Les sessions sont sous `Sessions` près de l'EXE.
Ces fichiers peuvent contenir des chemins de jeux : masquez-les avant partage.

<a id="known-limitations"></a>
## Limitations connues

- Des patchs natifs expérimentaux peuvent provoquer plantages ou artefacts ; un plantage Bodycam non résolu est consigné dans l'historique.
- Les essais d'un renderer contrôlé ne certifient pas tous les jeux, pilotes ou anti-cheats.
- Les images générées ne sont pas de nouveaux échantillons d'entrée ; le hub ne promet aucun gain mesuré de latence ou de performances.
- Plusieurs générateurs/overlays peuvent entrer en conflit ; le diagnostic des modules ne valide pas toutes les coexistences.
- Le manifeste de compatibilité aide à la détection ; ce n'est pas une liste de jeux tous testés.
- Les conditions NVIDIA et la réserve sur les limitations techniques restent documentées dans la [provenance](../docs/provenance.fr.md).

<a id="troubleshooting"></a>
## Dépannage

| Symptôme | Action |
| --- | --- |
| Fournisseur non pris en charge | Conservez les fichiers originaux ; indiquez versions et erreur sans contourner le contrôle du hash. |
| Aucun DLSS FG disponible | Choisissez cette réponse et laissez le jeu autonome ; l'outil ne crée pas cette intégration. |
| Plantage ou artefacts | Quittez le jeu, désactivez NVMFG, restaurez son runtime original s'il a été changé, puis signalez les étapes. |
| SDK indisponible | Actualisez et vérifiez la source officielle ; un cache/import doit aussi réussir les contrôles. |
| Récupération bloquant sortie ou mise à jour | Utilisez la récupération et préservez le journal ; ne forcez pas un conflit. |
| Jeu retiré non redécouvert | Son exclusion persiste. Ajoutez-le explicitement pour le gérer de nouveau. |

L'[aide commune](../docs/support.fr.md) précise les informations à joindre.

<a id="faq"></a>
## FAQ

**Des DLL ou modèles NVIDIA sont-ils inclus ?** Aucun pilote, modèle/fournisseur
NGX ou runtime Streamline. Les téléchargements SDK explicites viennent de NVIDIA.

**Dynamic fonctionne-t-il sans V-Sync ?** Il est suspendu ; choisissez alors
le réglage du jeu ou un multiplicateur fixe admissible pour cet état distinct.

**Est-ce un paquet ReShade/OptiScaler/FSR ?** Non. Ces composants ne sont ni compilés
ni distribués dans ce paquet de production.

**Les sources modifiées sont-elles publiques ?** Non. Les binaires, crédits et
licences sont fournis sans retirer les droits ou restrictions des tiers.

<a id="upstream-and-modifications"></a>
## Origine et modifications

Référence de comparaison et composants natifs partagés :
**RTX40MFG-Unlock de Michael Robles / dashdogy**,
référence `4e776d068f91b4a665425542bb005dd57cc3d891`, MIT.
[Dépôt](https://github.com/dashdogy/RTX40MFG-Unlock) · [Téléchargements originaux](https://github.com/dashdogy/RTX40MFG-Unlock/releases).

La comparaison identifie des composants partagés de patchs, politiques de
fournisseur, corrections temporelles et détours MinHook. Leurs notices MIT et BSD
sont conservées. La comparaison complète inclut aussi des fichiers non compilés.

L'application de bureau, le contrôleur et le parcours de gestion des SDK sont
développés par 禅堂 Zendo (RevoluSound Team). Ses travaux comprennent le chargement
central, l'intégration NGX, la sélection vérifiée du fournisseur, la coordination
jeu/V-Sync et les diagnostics. La provenance distingue ces travaux des composants
partagés ; une comparaison de fichiers ne date pas à elle seule l'idée des auteurs.

Le helper de profils adapte le wrapper NVAPI MIT d'Orbmu2k.
[Provenance et périmètre des composants](../docs/provenance.fr.md).

<a id="credits-and-license"></a>
## Crédits et licence

Michael Robles ; Orbmu2k ; Tsuda Kageyu et contributeurs HDE ; NVIDIA Corporation ;
Microsoft et contributeurs ; auteurs et traducteurs Inno Setup.
Développement applicatif, intégrations et packaging : 禅堂 Zendo (RevoluSound Team).

La [permission existante de partage du paquet](LICENSE) et les
[licences des composants](LICENSES/README.md) sont conservées. MIT pour l'upstream
et les conditions des SDK NVIDIA sont distinctes.

Projet indépendant de NVIDIA Corporation, ni sponsorisé ni officiellement approuvé.
Les marques restent à leurs propriétaires.
