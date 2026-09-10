🌐 **Langue :** [English](development.md) | Français · [Accueil](../README.fr.md)

# Architecture et maintenance

NV Laboratory est un **hub de documentation et de distribution binaire**.
Les sources applicatives restent privées. Les quatre projets conservent leurs
builds, versions, identités et assets séparés ; leur historique privé n'est pas importé.

## Organisation

| Emplacement | Rôle |
| --- | --- |
| README.md / README.fr.md | Accueils anglais/français |
| Quatre dossiers de projets | Guides complets et notices originales applicables |
| docs | Téléchargements, compatibilité, provenance et maintenance |
| docs/releases.json | Versions, tailles et SHA-256 des candidates/Releases |
| docs/provenance | Comparaisons noms/hashes, sans code applicatif |
| licenses | Textes tiers complets et crédits des traducteurs |
| assets | Aperçus existants examinés et provenance |
| .github | Formulaires et validation documentaire en lecture seule |
| tools/validate_repository.py | Contrôle des liens et limites de publication |

Les fichiers `.fr.md` voisins gardent une navigation simple. L'anglais est
l'accueil GitHub par défaut ; le visiteur choisit le français. GitHub Pages
n'apporte pas ici de bénéfice nécessaire.

## Technologies des applications privées

| Programme | Technologie | Distribution |
| --- | --- | --- |
| Fork NVPI | C#, WPF, .NET Framework 4.8, interop Windows/NVAPI | Dossier portable et Inno Setup séparé |
| NVDriverForge | C#/WPF .NET 8, bootstrap C++, processus 7-Zip | EXE portable autonome et Setup |
| NVMFG Unlock40 | C#/WPF .NET 8, helpers Framework 4.8, moteur C++20/MASM/MinHook | Arborescence portable et Setup |
| NVRasterPulse | C#/WPF Framework 4.8, profils/rechargement RTSS et bootstrap natif | Arborescence portable et Setup |

Ce dépôt ne permet pas de reconstruire les applications. Les archives automatiques
« Source code » sont des copies du hub. Les liens upstream ne représentent pas
le code privé modifié. La CI publique ne vérifie que ce dépôt.

## Vérification locale

Depuis la racine :

```text
python tools/validate_repository.py
```

Python 3.10 ou ultérieur suffit. La validation lit fichiers, liens Markdown locaux,
notices requises, lien RTSS, métadonnées et frontières de publication.
Elle n'exécute pas les programmes et ne contacte aucun réseau.

Le workflow GitHub rejoue ce contrôle en lecture seule à chaque push, Pull Request
ou déclenchement manuel. Checkout est figé sur un commit et ne conserve pas
d'identifiants. Aucun job de Release ou déploiement n'est configuré.

## Préserver le périmètre

Mettez à jour les guides anglais/français ensemble. Distinguez modifications de
fond et simple formatage. Enregistrez les vrais hashes, références et licences,
sans déduire une licence de la popularité du composant.

Préparez des assets de version neufs et réauditez les binaires, archives et notices
changés. Gardez les backups privés à l'extérieur. Ne faites pas importer les sources
ou dossiers de build privés par une CI publique.

Les tests d'une modification fonctionnelle se font dans le projet privé.
Une mise à jour documentaire ne justifie pas d'installer un pilote ou de modifier
des profils réels. [Procédure manuelle de Release](releasing.fr.md).
