<!-- nv-language-navigation:start -->
🌐 [English](development.md) | Français · [NV Laboratory](../README.fr.md)

<details>
<summary>🌐 Language · 34</summary>

[العربية](languages/ar/docs/development.md) · [বাংলা](languages/bn/docs/development.md) · [简体中文](languages/zh/docs/development.md) · [Čeština](languages/cs/docs/development.md) · [Dansk](languages/da/docs/development.md) · [Nederlands](languages/nl/docs/development.md) · [English](development.md) · [Filipino](languages/fil/docs/development.md) · [Suomi](languages/fi/docs/development.md) · **Français** · [Deutsch](languages/de/docs/development.md) · [Ελληνικά](languages/el/docs/development.md) · [हिन्दी](languages/hi/docs/development.md) · [Magyar](languages/hu/docs/development.md) · [Bahasa Indonesia](languages/id/docs/development.md) · [Italiano](languages/it/docs/development.md) · [日本語](languages/ja/docs/development.md) · [한국어](languages/ko/docs/development.md) · [मराठी](languages/mr/docs/development.md) · [فارسی](languages/fa/docs/development.md) · [Polski](languages/pl/docs/development.md) · [Português](languages/pt/docs/development.md) · [ਪੰਜਾਬੀ](languages/pa/docs/development.md) · [Română](languages/ro/docs/development.md) · [Русский](languages/ru/docs/development.md) · [Español](languages/es/docs/development.md) · [Kiswahili](languages/sw/docs/development.md) · [Svenska](languages/sv/docs/development.md) · [தமிழ்](languages/ta/docs/development.md) · [ไทย](languages/th/docs/development.md) · [Türkçe](languages/tr/docs/development.md) · [Українська](languages/uk/docs/development.md) · [اردو](languages/ur/docs/development.md) · [Tiếng Việt](languages/vi/docs/development.md)

[Translation policy](languages/README.md)

</details>
<!-- nv-language-navigation:end -->

<a id="repository-architecture-and-maintenance"></a>
# Architecture et maintenance

NV Laboratory est un **hub de documentation et de distribution binaire**.
Les sources applicatives restent privées. Les quatre projets conservent leurs
builds, versions, identités et assets séparés ; leur historique privé n'est pas importé.

<a id="layout"></a>
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

L'anglais reste l'accueil GitHub par défaut. Les liens `.fr.md` existants restent
valides. Les autres traductions reprennent l'arborescence sous `docs/languages/<code>`.
Le sélecteur conserve la page consultée. `docs/languages/catalog.json` indique les
34 langues et les empreintes des références. GitHub ne choisit pas automatiquement
le README selon la langue du navigateur. Voir l'[index et les règles de traduction](languages/README.md).

<a id="application-technologies"></a>
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

<a id="local-checks"></a>
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

<a id="maintain-the-boundary"></a>
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
