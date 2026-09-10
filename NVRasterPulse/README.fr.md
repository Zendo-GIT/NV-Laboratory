<!-- nv-language-navigation:start -->
🌐 [English](README.md) | Français · [NV Laboratory](../README.fr.md)

<details>
<summary>🌐 Language · 34</summary>

[العربية](../docs/languages/ar/NVRasterPulse/README.md) · [বাংলা](../docs/languages/bn/NVRasterPulse/README.md) · [简体中文](../docs/languages/zh/NVRasterPulse/README.md) · [Čeština](../docs/languages/cs/NVRasterPulse/README.md) · [Dansk](../docs/languages/da/NVRasterPulse/README.md) · [Nederlands](../docs/languages/nl/NVRasterPulse/README.md) · [English](README.md) · [Filipino](../docs/languages/fil/NVRasterPulse/README.md) · [Suomi](../docs/languages/fi/NVRasterPulse/README.md) · **Français** · [Deutsch](../docs/languages/de/NVRasterPulse/README.md) · [Ελληνικά](../docs/languages/el/NVRasterPulse/README.md) · [हिन्दी](../docs/languages/hi/NVRasterPulse/README.md) · [Magyar](../docs/languages/hu/NVRasterPulse/README.md) · [Bahasa Indonesia](../docs/languages/id/NVRasterPulse/README.md) · [Italiano](../docs/languages/it/NVRasterPulse/README.md) · [日本語](../docs/languages/ja/NVRasterPulse/README.md) · [한국어](../docs/languages/ko/NVRasterPulse/README.md) · [मराठी](../docs/languages/mr/NVRasterPulse/README.md) · [فارسی](../docs/languages/fa/NVRasterPulse/README.md) · [Polski](../docs/languages/pl/NVRasterPulse/README.md) · [Português](../docs/languages/pt/NVRasterPulse/README.md) · [ਪੰਜਾਬੀ](../docs/languages/pa/NVRasterPulse/README.md) · [Română](../docs/languages/ro/NVRasterPulse/README.md) · [Русский](../docs/languages/ru/NVRasterPulse/README.md) · [Español](../docs/languages/es/NVRasterPulse/README.md) · [Kiswahili](../docs/languages/sw/NVRasterPulse/README.md) · [Svenska](../docs/languages/sv/NVRasterPulse/README.md) · [தமிழ்](../docs/languages/ta/NVRasterPulse/README.md) · [ไทย](../docs/languages/th/NVRasterPulse/README.md) · [Türkçe](../docs/languages/tr/NVRasterPulse/README.md) · [Українська](../docs/languages/uk/NVRasterPulse/README.md) · [اردو](../docs/languages/ur/NVRasterPulse/README.md) · [Tiếng Việt](../docs/languages/vi/NVRasterPulse/README.md)

[Translation policy](../docs/languages/README.md)

</details>
<!-- nv-language-navigation:end -->

<a id="nvrasterpulse"></a>
# NVRasterPulse

**Des limites FPS par application avec RivaTuner Statistics Server.**

> **Installez RTSS d'abord.** NVRasterPulse nécessite [RivaTuner Statistics Server (RTSS), disponible sur Guru3D](https://www.guru3d.com/download/rtss-rivatuner-statistics-server-download/). RTSS doit être actif pour appliquer les limites. Aucun installateur, hook DLL ou SDK RTSS n'est inclus.

[Télécharger 0.1 et consulter le statut](../docs/downloads.fr.md#nvrasterpulse) · [Installation](#installation) · [Utilisation](#utilisation) · [Licence](LICENSE)

<a id="overview-and-purpose"></a>
## Présentation et raison d'être

NVRasterPulse est une interface Windows compacte pour gérer les limites RTSS par
nom d'exécutable. RTSS effectue la limitation ; NVRasterPulse gère les valeurs des
profils, sauvegardes et demandes de rechargement, avec accès depuis la zone de
notification et mémorisation des choix.

Il facilite les limites précises par jeu sans remplacer un profil RTSS complet
ni perturber ses paramètres d'overlay. La candidate **0.1** retenue est celle du
9 septembre 2026 avec vérification obligatoire de l'installation RTSS.

<a id="features"></a>
## Fonctionnalités

- Choix d'une application ouverte ou ajout manuel de son exécutable.
- Limites de 1 à 1000 FPS, avec trois décimales au maximum.
- Fraction exacte de la valeur saisie : 59.94 devient 2997/50.
- Front Edge Sync (`SyncLimiter=1`) et attente active (`PassiveWait=0`).
- Modification ciblée, sauvegardes automatiques et écritures atomiques.
- Retrait des paramètres du limiteur tout en conservant le reste du profil.
- Détection RTSS, choix manuel, lancement et rechargement explicites.
- Instance unique, zone de notification, démarrage installé facultatif, 34 langues et quatre thèmes.
- Actions distinctes de fermeture normale et **Quitter + RTSS**.

<a id="compatibility"></a>
## Compatibilité

| Prérequis | Détails |
| --- | --- |
| Système | Windows 10/11 x64 |
| Runtime | [.NET Framework 4.8](https://dotnet.microsoft.com/en-us/download/dotnet-framework/net48), séparé si nécessaire |
| Logiciel requis | RTSS avec `RTSS.exe`, dossier `Profiles` correspondant et prise en charge des paramètres/rechargements utilisés |
| GPU | Compatibilité du limiteur déterminée par RTSS, sans génération RTX précise exigée par ce gestionnaire |
| Droits | L'application actuelle demande l'élévation ; le dossier de profils doit être accessible |
| Jeux | Dépend du hook RTSS et des restrictions du jeu, sans garantie anti-cheat |

Aucune version minimale RTSS n'a été certifiée pour toutes les fonctions par
l'audit du hub. Utilisez la distribution officielle actuelle et précisez sa version
en cas d'erreur. RTSS installé mais arrêté satisfait la détection ; il doit ensuite
être lancé pour limiter les FPS.

<a id="installation"></a>
## Installation

1. **[Téléchargez et installez RTSS depuis Guru3D](https://www.guru3d.com/download/rtss-rivatuner-statistics-server-download/).**
2. Consultez le [statut des téléchargements NVRasterPulse](../docs/downloads.fr.md#nvrasterpulse).
3. Téléchargez `NVRasterPulse-0.1-win-x64-Setup.exe` ou `NVRasterPulse-0.1-win-x64-portable.zip`, avec notices et empreintes.
4. Vérifiez le SHA-256. Lancez Setup ou extrayez tout le ZIP dans un dossier local accessible en écriture.
5. Ouvrez `NVRasterPulse.exe`. Si RTSS manque, utilisez le téléchargement, installez-le puis revérifiez ; vous pouvez aussi choisir manuellement `RTSS.exe`.
6. Lancez RTSS par son raccourci ou le bouton RTSS de NVRasterPulse s'il est arrêté.

Désactiver le rappel facultatif ne contourne pas le prérequis. Le démarrage discret
dans la zone de notification attend l'ouverture de la fenêtre avant de l'afficher.
Le Setup n'installe que NVRasterPulse. Ses EXE ne sont pas signés.

<a id="usage"></a>
## Utilisation

1. Sélectionnez l'application ouverte ou choisissez l'EXE du jeu.
2. Entrez une valeur de 1 à 1000 FPS, éventuellement fractionnaire.
3. Enregistrez et vérifiez le résultat annoncé. Le profil de cet exécutable est modifié puis son rechargement demandé.
4. Vérifiez que RTSS est actif et contrôlez le comportement dans le jeu.

Les profils utilisent le **nom de l'exécutable**, par exemple `Game.exe.cfg`.
Deux dossiers contenant `Game.exe` partagent donc un profil RTSS ; enregistrer
le chemin complet ne supprime pas cette collision.

L'enregistrement utilise Front Edge Sync et l'attente active, qui peut augmenter
l'usage CPU. Les champs alternatifs `LimitTime` sont neutralisés. Commentaires,
overlay et `EnableHooking=0` existant sont conservés. Le profil Global reste intact.

La corbeille retire les paramètres locaux du limiteur, sans supprimer tout le profil.
Une limite héritée du Global RTSS ou d'un autre outil peut donc rester active.

**Fermeture :** la fenêtre peut se masquer dans la zone de notification. **Quitter**
laisse RTSS actif et conserve les limites. **Quitter + RTSS** demande une fermeture
normale du processus RTSS correspondant dans la session, attend au maximum huit
secondes et ne le termine pas de force. Les limites enregistrées restent présentes.

Langue et thème se choisissent dans le programme. Le démarrage Windows est facultatif
et prévu pour une copie installée. Le bouton d'information explique les actions courantes.

<a id="screenshots"></a>
## Captures

![Aperçu de la fenêtre NVRasterPulse](../assets/screenshots/nvrasterpulse-0.1-preview.png)

Rendu existant de 0.1 en français, avec noms d'exécutables d'exemple et valeur 176 FPS.
RTSS est affiché arrêté : ce n'est pas une mesure de limiteur ou de latence.
[Provenance](../assets/README.md).

<a id="update-and-uninstall"></a>
## Mise à jour et désinstallation

Quittez NVRasterPulse, téléchargez et vérifiez la version suivante, puis lancez
son Setup ou extrayez le portable dans un nouveau dossier. Conservez réglages
et sauvegardes RTSS. RTSS se met à jour séparément depuis Guru3D.

Utilisez **Applications installées** pour la version installée. Pour portable,
quittez puis retirez le dossier en conservant vos sauvegardes. Les limites RTSS
ne sont pas retirées avec NVRasterPulse : supprimez d'abord les paramètres voulus
du limiteur. RTSS possède son propre désinstallateur.

État local : `%LOCALAPPDATA%\NVRasterPulse`.
Sauvegardes : `%LOCALAPPDATA%\NVRasterPulse\Backups\RTSS`.
L'ancien dossier `%LOCALAPPDATA%\RTSSProfileBridge` peut être lu pour la migration.
Ces données peuvent contenir des chemins personnels et ne doivent pas être publiées telles quelles.

<a id="known-limitations"></a>
## Limitations connues

- RTSS effectue la limitation ; une valeur enregistrée ou un rechargement réussi n'est pas une mesure des temps d'image.
- Les exécutables homonymes partagent un profil.
- Une autre limite globale/locale peut intervenir ; retirer l'override local ne retire pas une limite héritée.
- Un hook RTSS volontairement désactivé reste désactivé.
- L'attente active a une contrepartie CPU/énergie.
- Pas de validation universelle des jeux, anti-cheats ou latence de bout en bout.
- L'ancien moteur indépendant expérimental n'est ni compilé ni distribué.
- Les sauvegardes automatiques n'impliquent pas une interface de restauration complète en un clic.

<a id="troubleshooting"></a>
## Dépannage

| Symptôme | Action |
| --- | --- |
| Prérequis RTSS toujours affiché | Choisissez le vrai `RTSS.exe` et son dossier Profiles, puis revérifiez. |
| Limite enregistrée sans effet | Lancez RTSS ; vérifiez EXE/profil, hook et autres limiteurs. |
| Échec d'enregistrement | Vérifiez les permissions et conservez erreur et sauvegarde. |
| Limite persistante après retrait | Contrôlez Global RTSS et les autres outils : la corbeille ne retire que les paramètres locaux. |
| Deux jeux reçoivent la même limite | Vérifiez si leurs EXE portent le même nom. |
| Quitter + RTSS ne ferme pas RTSS | Fermez RTSS normalement ; cette action évite la terminaison forcée. |

Pour restaurer manuellement une sauvegarde RTSS, fermez RTSS et préservez le profil
actuel avant son remplacement. Cela peut écraser d'autres changements : vérifiez
fichier et date. [Aide commune](../docs/support.fr.md).

<a id="faq"></a>
## FAQ

**MSI Afterburner est-il nécessaire ?** NVRasterPulse dépend de RTSS, pas
de l'application Afterburner. Suivez les options du distributeur RTSS.

**Peut-on l'utiliser RTSS arrêté ?** Vous pouvez gérer les profils après détection
de l'installation ; RTSS doit fonctionner pour limiter les FPS.

**Quitter ou désinstaller retire-t-il les limites ?** Non. Retirez explicitement
les paramètres du limiteur souhaités avant la désinstallation.

**Est-ce une fork de RTSS ?** Non. C'est un gestionnaire indépendant ;
aucun code source ni exécutable RTSS n'y est intégré.

<a id="upstream-modifications-and-credits"></a>
## Origine, modifications et crédits

Le dépôt de développement vient de
[NVIDIA Profile Inspector d'Orbmu2k](https://github.com/Orbmu2k/nvidiaProfileInspector).
Ses ressources/palettes MIT sont créditées. Services de profils, fractions,
sauvegardes, pont de rechargement RTSS, zone de notification, guide de prérequis,
langues et icône propre ont été développés/adaptés par
禅堂 Zendo (RevoluSound Team).

RTSS est développé par **Unwinder**, distribué séparément via Guru3D.
NVRasterPulse appelle `UpdateProfiles` dans la DLL installée choisie, sans
redistribuer le SDK ou le hook RTSS. L'installateur utilise Inno Setup 7.1.0
non modifié, des scripts/traductions adaptés et un bootstrap du projet.

[Provenance complète](../docs/provenance.fr.md) · [Composants tiers](../THIRD_PARTY_NOTICES.md)

<a id="license"></a>
## Licence

La notice distribue explicitement NVRasterPulse sous la [licence MIT fournie](LICENSE),
en conservant Copyright (c) 2016 Orbmu2k. Les sources restent privées ; MIT n'impose
pas leur publication. RTSS et Windows/.NET gardent leurs propres conditions.
[Notices complètes](LICENSES/README.md).

Indépendant de NVIDIA Corporation, MSI et RTSS, sans sponsoring ou approbation
officielle. Les marques restent à leurs propriétaires.
