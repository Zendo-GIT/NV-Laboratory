🌐 **Langue :** [English](provenance.md) | Français · [Accueil](../README.fr.md)

# Provenance, modifications et licences

Audit des candidates préparées le **2026-09-09**. Les sources applicatives restent
privées ; les inventaires publics donnent noms et empreintes, sans code source.
Le [tableau complet](../THIRD_PARTY_NOTICES.md) conserve les notices applicables.

## NVIDIA Profile Inspector – NV Tools Fork

Référence Orbmu2k/nvidiaProfileInspector :
`592d962cca8827efe8859461a84267755595064a`. Version EXE de la fork : 3.0.2.3.
Le commit et la version de la fork sont distincts ; celle-ci n'est pas une preuve
du numéro de Release upstream.

Comparaison des 157 fichiers source/ressource du compagnon propre : 2 identiques,
134 différant seulement par fins de ligne/BOM UTF-8, 11 modifiés et 10 absents au
chemin upstream comparé. Une absence à ce chemin ne prouve pas une création originale.
[Inventaire complet](provenance/nvpi-source-provenance.json).

| Partie | Héritage | Apport de la fork |
| --- | --- | --- |
| Éditeur de profils | Modèles, import/export, associations et références | Intégration de Screen et du lanceur externe |
| NVAPI | Interop DRS d'Orbmu2k | Couleurs/affichage, restrictions de chargement natif et retrait des mocks |
| Services écran | API Windows/NVIDIA externes | DisplayInfoService, DisplayConfigurationService et DisplaySettingsBackend |
| Interface | Ressources, palettes et icônes WPF | Dialogues écran, confirmation 15 secondes, relecture et barre d'outils |
| Lanceur | Structure applicative existante | Recherche et lancement protégés d'un RasterPulse installé séparément |
| Packaging | Licence MIT upstream | Compagnon autonome nettoyé, installateur/désinstallateur et notices |

Les chemins du manifeste servent à la traçabilité ; les sources correspondantes
ne sont pas publiées. Tests, mocks et ancien paquet combiné NVPI/RasterPulse sont exclus.

## NVDriverForge

Application C#/.NET 8/WPF indépendante, partiellement inspirée du parcours
NVCleanstall. Aucun code ou binaire NVCleanstall identifié dans la distribution ;
ce programme n'est donc pas présenté comme sa fork.

Travail propre : analyse/choix des composants, installation protégée, sauvegardes
et récupération transactionnelle, téléchargements NVIDIA, surveillance facultative,
explications localisées, parcours avancés/NVENC et bootstrap du Setup.

Héritage/adaptations : quatre palettes NVPI, référence de l'interface DRS NVAPI
étendue et compagnon NVPI facultatif sous MIT. L'éditeur de choix Custom NV et
son intégration transactionnelle appartiennent à NVDriverForge. Le preset n'est
pas une recommandation officielle NVIDIA.

7-Zip 26.03, .NET/WPF 8.0.30 et Inno Setup restent non modifiés et sous leurs conditions.
Les données NVENC keylase ne sont pas embarquées : le téléchargement demandé fixe
un commit et vérifie sa correspondance. Aucune licence de redistribution de ces
données n'a été établie par cet audit.

## NVMFG Unlock40

Origine : dashdogy/RTX40MFG-Unlock, Michael Robles, MIT, référence
`4e776d068f91b4a665425542bb005dd57cc3d891`.
Sur les 48 fichiers du moteur comparés : 35 différences de formatage seulement,
4 modifications et 9 fichiers absents au chemin de référence.
[Comparaison complète](provenance/nvmfg-source-provenance.json).

Fichiers hérités modifiés : `entry_detour.h`, `patcher.cpp`,
`temporal_interval_trace.cpp` et `temporal_interval_trace.h`.
Chemins supplémentaires : `game_selection.*`, `ngx_bootstrap.*`,
`ngx_capability.h`, `presentation_tracker.h`, `vsync_observer.*`
et copie de licence upstream.

Unités C++ de production : patcher, midpoint_fix, dlssg_provider_policy, entry_detour,
nvidia_mfg_policy, temporal_interval_trace, ngx_bootstrap, game_selection et
vsync_observer, avec assembleur entry_detour et MinHook buffer/hook/trampoline/HDE64.
Frontend ReShade hérité, anciens shims et cibles CMake inutilisées ne sont pas compilés.

L'upstream apportait déjà les patchs, politiques de fournisseur et travaux temporels.
Coordination centrale NGX/contrôleur, gestion V-Sync par jeu, diagnostics et gestion
Windows/SDK/sauvegardes sont des ajouts et adaptations de 禅堂 Zendo (RevoluSound Team).
Il ne s'agit pas d'une création intégrale du moteur d'origine.

Le helper adapte NvapiDrsWrapper et NativeArrayHelper de NVPI, avec logique de
profils propre et exclusion des mocks. Les palettes familiales proviennent de NVPI.

MinHook : `8fda4f5481fed5797dc2651cd91e238e9b3928c6`, sous-ensemble hérité sans
modification fonctionnelle locale dans la comparaison. En-têtes Streamline 2.12,
licence ouverte vérifiée sur v2.12.0. En-têtes NGX :
NVIDIA/DLSS `a291cc7d2cc642a51566f3dfd5376f635cd1b284`.

SHA-256 du moteur candidat :
`0E7FC0277C88B22095B622F6A3CB292EC0C14F7A0253D392502257B75E548890`.

SHA-256 fournisseur exigé dans engine.json :
`C64928FDB7C48A57722EA8EEF2662171EDC323473ADEA66C29A206A23F1A2BED`.
La famille 310.9 rapportée ne remplace pas cette empreinte exacte.
Aucun fournisseur DLL ou modèle n'est inclus.

**Réserve de licence :** le texte NVIDIA RTX SDK du 14 mars 2024 comporte une
restriction §4(d) relative aux limitations techniques. L'audit n'établit pas
d'autorisation pour cet usage. La licence MIT du moteur, la gratuité ou l'existence
d'autres mods ne résolvent pas cette condition distincte. Préparer la candidate
ne constitue pas une validation juridique. La courte notice initiale est complétée
par le texte intégral, transcodé de Windows-1252 en UTF-8 pour la lecture ; les
octets originaux sont aussi conservés.

## NVRasterPulse

Gestionnaire RTSS indépendant, développé dans le dépôt issu de NVPI.
Origine du dépôt et ressources/palettes MIT sont créditées ; la notice de production
distribue explicitement l'application sous cette licence.

Apports : lecture/écriture ciblée et fractions exactes des profils RTSS, sauvegardes,
retrait des limites, pont de rechargement, détection du prérequis, interface compacte,
zone de notification, démarrage facultatif et traductions. RTSS applique les limites.

Aucun source, hook DLL, SDK ou installateur RTSS n'est inclus. Le pont appelle la DLL
d'une installation existante choisie par l'utilisateur. Aucun pilote NVIDIA, moteur
expérimental indépendant, Framepacer, MinHook, ReShade ou runtime DLSS n'est distribué.

## Assets, données générées et outils

Les [crédits des images](../assets/README.md) identifient trois rendus existants et
leurs données fictives. Aucun asset de jeu/Nexus, profil personnel, ICC privé,
logo corporate NVIDIA ou fichier de police n'est copié.

Les noms de compatibilité hérités de NVMFG servent à la détection, pas à prouver
des tests. Les catalogues d'installation sont crédités dans les
[notices des traducteurs](../licenses/INSTALLER-TRANSLATORS.md). Les manifestes
de build comportant des chemins absolus restent privés.

Outils privés : SDK .NET/MSBuild, Visual Studio C++/MASM, SDK Windows, PowerShell,
Inno Setup et scripts Python d'audit. Compilateurs, en-têtes, tests et artefacts
debug ne sont pas distribués. Le CRT statique de production conserve les conditions
Microsoft applicables à la chaîne de compilation.

## Périmètre des vérifications

L'audit a inventorié les trois racines de développement, hors objets Git et cibles
des liens de dossiers. Les textes actifs ont été scannés ; les anciens builds sont
inventoriés et exclus. ZIP retenus et payloads actuels sont scannés et hachés ; les
bundles .NET ont été décompressés pour contrôle complémentaire. Aucun programme,
installateur, jeu, RTSS ou pilote n'avait été exécuté lors de cet audit initial.

La révision 2 du setup NVPI corrige ensuite la sélection de langue au lancement
autonome, avec les contrôles Inno et le bootstrap communs. Des fixtures privées
claires/sombres ont vérifié le clavier, la souris et les 34 langues explicites.
Le sélecteur du vrai setup a été ouvert sur un bureau privé jamais affiché, puis
annulé avant installation. Les sept fichiers applicatifs et le ZIP portable restent
identiques. NVDriverForge 0.1.2 conserve son ancien compagnon embarqué, qui reçoit `/LANG`.

Aucun code fonctionnel applicatif n'a changé. Les builds et tests applicatifs
antérieurs restent des preuves historiques datées. Le contrôle n'est pas une
rétro-ingénierie exhaustive ni une garantie contre tout motif de secret.
