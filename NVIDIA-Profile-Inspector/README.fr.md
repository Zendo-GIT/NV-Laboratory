🌐 **Langue :** [English](README.md) | Français · [NV Laboratory](../README.fr.md)

# NVIDIA Profile Inspector – NV Tools Fork

**Une fork indépendante de [NVIDIA Profile Inspector d'Orbmu2k](https://github.com/Orbmu2k/nvidiaProfileInspector), enrichie de réglages écran.** Ancien nom du projet : **NVPI Custom**.

[Téléchargement et statut](../docs/downloads.fr.md#nvidia-profile-inspector) · [Installation](#installation) · [Origine et modifications](#origine-et-modifications) · [Licence](LICENSE)

## Présentation et raison d'être

Le programme édite les profils du pilote NVIDIA, notamment les réglages propres
aux applications. Cette fork ajoute un éditeur **Screen** pour l'affichage Windows
courant : résolution, fréquence, couleurs, HDR et associations ICC/WCS installées.

Elle réunit ces réglages dans l'éditeur de profils et rend plus explicites
l'aperçu, la confirmation et les résultats de restauration. Elle ne crée pas
de nouvelles capacités matérielles.

La première candidate est **3.0.2.3**, issue du compagnon autonome nettoyé du
9 septembre 2026. L'exécutable reste `nvidiaProfileInspector.exe` ; l'installateur
et certains libellés internes portent encore `NVPI Custom NV`. Le titre public
identifie la fork sans changer son identité d'installation ni la présenter
comme la version officielle d'Orbmu2k.

## Fonctionnalités

- Consultation et édition des profils, associations d'applications et import/export hérités du projet original.
- Dialogue **Screen** : écran, résolution, Hz, RGB/YCbCr, profondeur, plage et colorimétrie.
- Contrôle HDR Windows et choix d'une association ICC/WCS installée.
- Aperçu de 15 secondes avec **Keep** / **Revert** et restauration à expiration.
- Relecture du mode et du HDR ; signalement des échecs de restauration.
- Distinction entre HDR, SDR avec ACM/WCG et profondeur du signal.
- Bouton de lancement d'une installation séparée et admissible de NVRasterPulse.

## Compatibilité

| Prérequis | Détails |
| --- | --- |
| Système | Windows 10/11 x64 avec pilote NVIDIA compatible |
| Runtime | [.NET Framework 4.8](https://dotnet.microsoft.com/en-us/download/dotnet-framework/net48), fourni par Windows ou installé séparément |
| Droits | Le programme demande les droits administrateur à son ouverture |
| Écran | Combinaisons possibles dépendantes du GPU, du pilote, de l'écran, du câble et des API Windows |
| Outils facultatifs | NVRasterPulse pour les limites RTSS ; aucun des deux n'est requis pour Screen |
| Langues | Setup : sélecteur de 34 langues. L'éditeur conserve sa prise en charge linguistique existante. |

Aucun pilote minimal universel ni tableau certifiant tous les GPU n'est établi.
Les choix bpc affichés sont des demandes, pas des combinaisons garanties.
Les commandes HDR modernes et leur repli Windows ancien n'ont pas les mêmes capacités.

## Installation

1. Consultez le [statut de téléchargement](../docs/downloads.fr.md#nvidia-profile-inspector).
2. Téléchargez Setup ou portable et comparez son SHA-256 au manifeste de la Release.
3. Pour Setup, lancez `NVPI-CustomNV-3.0.2.3-Setup-r2.exe`, choisissez la langue puis suivez l'assistant. Il crée un raccourci et son propre désinstallateur.
4. Pour portable, extrayez tout le ZIP dans un nouveau dossier accessible en écriture. Gardez `Reference.xml`, la configuration EXE et les notices.
5. Ouvrez `nvidiaProfileInspector.exe`.

Installer l'éditeur n'applique aucun profil et n'installe aucun pilote. Le compagnon
s'installe séparément, ne reprend pas les associations `.nip` et n'active pas le
démarrage automatique. Les exécutables existants ne sont pas signés.

La **révision 2 du setup** ajoute le même sélecteur natif que les autres outils,
avec navigation clavier et souris, présentation claire/sombre et annulation.
Le choix concerne l'assistant d'installation. Il ne traduit pas l'éditeur NVPI.
Un lancement avec `/LANG=fr` ou en mode silencieux passe directement à l'assistant,
comme lorsqu'une application appelante fournit déjà la langue.

## Utilisation

**Profils NVIDIA :** choisissez un profil, exportez une sauvegarde, modifiez les
réglages voulus, puis appliquez-les. Les associations déterminent le jeu concerné.
Une valeur enregistrée ne prouve pas son utilisation effective par chaque pilote.

**Affichage :** ouvrez **Screen**, choisissez l'écran et les valeurs, puis lancez
l'aperçu. Vérifiez l'image avant **Keep**, dans les 15 secondes. **Revert**, la
fermeture ou l'expiration demandent une restauration. Lisez tout message d'échec :
le retour positif d'une API ne suffit pas à confirmer un résultat.

Le choix ICC modifie une association existante ; il ne crée ni ne calibre un profil.
HDR, ACM/WCG, RGB/YCbCr et bpc sont distincts. Cette reconstruction n'ajoute pas
d'interrupteur ACM indépendant.

**NVRasterPulse :** le bouton accepte une installation système enregistrée sous
Program Files, avec propriétaires et permissions protégés. Une copie portable,
un dossier accessible en écriture ou un lien peuvent être refusés par ce lanceur
élevé. Utilisez alors le raccourci propre à NVRasterPulse.
[Installez RTSS séparément](https://www.guru3d.com/download/rtss-rivatuner-statistics-server-download/) pour utiliser son limiteur.

## Captures

![Sélecteur de langue du setup NVPI, révision 2](../assets/screenshots/nvpi-setup-r2-language.png)

Sélecteur réel du setup, en français, capturé dans un test isolé puis annulé.
La capture montre l'installateur ; l'éditeur conserve son interface et Screen.

## Mise à jour et désinstallation

Fermez le programme et conservez vos profils exportés. Installez la nouvelle
Release de la fork sur la même identité, ou extrayez le portable dans un nouveau
dossier. Ne mélangez pas un ancien `Reference.xml` avec un nouvel EXE.
La désactivation du contrôle de mise à jour upstream fournie appartient à cette fork.

Utilisez **Applications installées** sous Windows pour le Setup. Pour portable,
fermez-le puis retirez son dossier une fois vos exports conservés.
La désinstallation ne restaure ni les profils NVIDIA, ni l'affichage, et ne retire
pas NVRasterPulse ou RTSS. Restaurez les réglages souhaités avant la suppression.

## Limitations connues

- Les 15 secondes ne protègent pas contre tous les plantages du pilote, arrêts forcés ou coupures.
- Certaines combinaisons couleur/profondeur/fréquence renvoient `NVAPI_NOT_SUPPORTED`.
- Une lecture logicielle ne mesure pas la dalle, sa fidélité colorimétrique ou la latence.
- Screen agit sur l'affichage Windows courant ; il ne crée pas de presets écran par jeu.
- Aucun gain de performances ni résultat anti-cheat ou HDR universel n'est garanti.

## Dépannage

| Symptôme | Vérification |
| --- | --- |
| Erreur de runtime | Vérifiez Windows et .NET Framework 4.8 ; conservez tout le paquet. |
| Mode écran refusé | Revenez à l'état précédent et essayez un mode proposé par Windows/NVIDIA pour cet écran. |
| HDR ou couleurs revenus à l'état précédent | Vérifiez si un autre échec a déclenché la restauration ; distinguez HDR et ACM. |
| NVRasterPulse refusé par le bouton | Ouvrez son raccourci : le bouton exige une installation système protégée. |
| Réglage conservé après désinstallation | Restaurez le profil exporté ou les réglages Windows souhaités. |

Consultez l'[aide commune](../docs/support.fr.md) avant d'envoyer des journaux.

## FAQ

**Est-ce une version officielle NVIDIA ou Orbmu2k ?** Non. C'est une fork
indépendante ; l'auteur original et sa licence MIT restent crédités.

**NVDriverForge en a-t-il besoin ?** Non. Son preset Custom NV utilise sa propre
intégration. L'installation de cet éditeur reste un choix séparé.

**RTSS est-il obligatoire pour cette fork ?** Non. Il est obligatoire pour le
limiteur NVRasterPulse, pas pour les profils NVIDIA ou Screen.

**Où sont les sources ?** Les sources modifiées sont maintenues en privé.
L'upstream et la notice MIT sont fournis ; MIT n'impose pas leur publication.

## Origine et modifications

Projet original : [Orbmu2k/nvidiaProfileInspector](https://github.com/Orbmu2k/nvidiaProfileInspector),
référence `592d962cca8827efe8859461a84267755595064a`.
[Téléchargements originaux](https://github.com/Orbmu2k/nvidiaProfileInspector/releases).

Héritage : éditeur de profils, interop NVAPI, données de référence, ressources et
thèmes. 禅堂 Zendo (RevoluSound Team) a ajouté ou adapté les services écran, les transactions
HDR/ICC, la confirmation avec relecture, la barre d'outils et le lanceur RasterPulse.
Le compagnon nettoyé exclut les mocks et points d'entrée de test, protège le lanceur
externe et possède son installateur séparé. L'ancien paquet combiné NVPI/RasterPulse
de développement n'est pas la candidate retenue.

[Provenance détaillée](../docs/provenance.fr.md) · [Notice originale de la fork](LICENSES/ORIGINAL-FORK-NOTICE.txt)

## Crédits et licence

Copyright (c) 2016 Orbmu2k. La [licence MIT fournie](LICENSE) est conservée.
Adaptations et packaging : 禅堂 Zendo (RevoluSound Team).
L'installateur utilise Inno Setup ; Windows et .NET Framework restent externes.
[Notices applicables](LICENSES/README.md).

Projet indépendant, ni sponsorisé ni officiellement approuvé par NVIDIA Corporation.
Les marques restent la propriété de leurs détenteurs.
