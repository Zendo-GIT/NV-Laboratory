🌐 **Langue :** [English](releasing.md) | Français · [Accueil](../README.fr.md)

# Publication et Releases manuelles

Le mainteneur crée le dépôt distant et pousse avec **GitHub Desktop**.
Cette préparation ne crée aucun dépôt distant, push, déploiement ou Release.

## Première publication du dépôt

1. Examinez le rapport privé avant publication et résolvez les éléments NOT READY avant de considérer toute la distribution comme validée.
2. Dans GitHub Desktop, choisissez **File → Add local repository**, puis le dossier **NV-Laboratory** lui-même.
3. Vérifiez les changements : documents, notices, images, métadonnées JSON et automatisation du dépôt. Aucun source applicatif, EXE, DLL ou ZIP ne doit apparaître.
4. Créez le premier commit, par exemple `chore: initialize NV Laboratory documentation hub`. Aucun ancien historique n'est fabriqué.
5. Utilisez **Publish repository**, propriétaire **Zendo-GIT**, nom **NV-Laboratory**, puis choisissez vous-même la visibilité publique au moment voulu.
6. Activez le signalement privé de vulnérabilités dans les paramètres de sécurité GitHub et vérifiez le bouton avant de l'annoncer.
7. Contrôlez le workflow documentaire et les deux accueils linguistiques.

Aucun remote n'est configuré avant votre publication. Ne sélectionnez jamais
le dossier parent de recherche ou le dossier privé d'audit/pièces jointes.

L'identité publique du mainteneur est **禅堂 Zendo (RevoluSound Team)**.
Vérifiez aussi l'auteur du premier commit et son adresse GitHub `noreply`
dans GitHub Desktop : les métadonnées des commits font partie de la publication.
[Confidentialité de l'adresse des commits](https://docs.github.com/en/account-and-profile/how-tos/email-preferences/setting-your-commit-email-address).

## Releases applicatives indépendantes

| Outil | Premier tag prévu | Numérotation |
| --- | --- | --- |
| Fork NVPI | nvpi-v3.0.2.3 | Version existante à quatre nombres conservée |
| NVDriverForge | nvdriverforge-v0.1.2 | Version 0.x conservée ; SemVer peut guider les évolutions |
| NVMFG Unlock40 | nvmfg-unlock40-v0.1.1 | Numéro public conservé ; candidate UI2 identifiée par les hashes |
| NVRasterPulse | nvrasterpulse-v0.1 | Version publique à deux nombres demandée conservée |

Ne transformez pas artificiellement 3.0.2.3 ou 0.1 en une autre version.
Une modification ultérieure demande une version/révision et de nouveaux hashes.
Ne remplacez pas discrètement un binaire déjà publié sous la même identité.

1. Après publication du hub, ouvrez **Releases → Draft a new release** sur GitHub.
2. Utilisez le tag du programme, ciblant le commit examiné, et son texte de Release local préparé.
3. Joignez uniquement les assets applicatifs de ce tag, `Licenses-and-Credits.zip` et `SHA256SUMS.txt`.
4. Vérifiez version, vraie date, compatibilité, installation, changements, dépendances, problèmes et hashes. RTSS doit rester visible en haut de la Release RP.
5. Choisissez le statut prerelease selon le support réel. Un numéro sans suffixe ne certifie pas la stabilité.
6. Publiez manuellement selon le rapport et les problèmes restants. Aucun workflow ne publie à chaque commit.

[releases.json](releases.json) contient tailles et empreintes. Les binaires existants
doivent conserver leurs octets audités. Le setup NVPI révision 2 a son propre nom
et ses hashes ; le payload applicatif reste identique. Les notices supplémentaires complètent celles embarquées.
La réserve NVIDIA de NVMFG reste dans ses notes candidates et ne disparaît pas
avec la création d'une Release.

## Activer les téléchargements

Une fois la Release réellement publiée, mettez son `status` à `published`
et sa vraie `release_date` dans releases.json. Adaptez les mentions de publication
des téléchargements et accueils anglais/français. Vérifiez chaque lien réel,
lancez la validation puis commitez avec GitHub Desktop. Ne présentez pas une
candidate en attente comme « dernière version disponible ».

Le monorepo utilise des **liens de tags par programme**, pas un unique
`releases/latest` pouvant mener à un autre outil. Les archives automatiques
« Source code » contiennent le hub documentaire, pas les sources applicatives.

## Stockage des binaires

Le portable NVDriverForge fait 141 525 846 octets, au-delà de la limite GitHub
de 100 Mio par fichier Git ordinaire. Tous les programmes sont donc des pièces
jointes de Releases, hors historique Git. Git LFS n'est pas nécessaire ici.
[Limites GitHub](https://docs.github.com/en/repositories/working-with-files/managing-large-files/about-large-files-on-github).

Conservez les hashes exacts, notices et informations de récupération.
Les builds/tests fonctionnels restent privés.
[Documentation GitHub Releases](https://docs.github.com/en/repositories/releasing-projects-on-github/managing-releases-in-a-repository).
