# Contributing / Contribuer

NV Laboratory is maintained by 禅堂 Zendo (RevoluSound Team).
The maintainer decides what is accepted and released. Opening an Issue or Pull
Request does not mean a contribution is accepted or authorized for distribution.

## English

Use the bug or feature form and identify the program/version. Search existing
Issues first. Discuss substantial changes before preparing a large contribution.
For security matters, follow [SECURITY.md](SECURITY.md).

This public hub contains documentation, notices, release metadata and repository
validation. Application source and tests are maintained privately. Do not submit
decompiled code, private source, credentials, user profiles or executable payloads.

Documentation PRs should keep English/French counterparts and navigation aligned,
preserve command/file/product names, and describe actual behavior. New screenshots
must be your own, version-identified and free of personal details; synthetic data
must be labeled. Provide provenance and permission for every new third-party asset.

Use UTF-8, LF, readable Markdown and small focused changes. The Python validator
uses only the standard library. Match its existing style, avoid unnecessary
dependencies, and run:

```text
python tools/validate_repository.py
```

For release metadata changes, include the exact version/tag, file sizes and SHA-256
from the audited binaries, and keep download pages aligned. Application changes
require private build/tests appropriate to the affected behavior; a documentation
check is not an application test. Never invent historical test results or gains.

By contributing original hub material, you agree to its scoped MIT license in
[LICENSE](LICENSE). Keep third-party notices and identify your changes; do not
replace an upstream license. Acceptance and publishing remain maintainer decisions.

## Français

Identifiez outil et version dans le formulaire, recherchez les Issues existantes
et discutez les changements importants avant une grosse contribution.
Les sujets de sécurité suivent [SECURITY.md](SECURITY.md).

Ce hub public contient documents, notices, métadonnées et validation du dépôt.
Sources et tests applicatifs restent privés. N'envoyez ni code décompilé ou privé,
ni identifiants, profils personnels ou exécutables.

Gardez les versions anglaise/française cohérentes, sans traduire commandes,
fichiers et noms techniques. Décrivez les fonctions réelles. Identifiez version,
provenance et droits des captures ; masquez les données personnelles et signalez
les exemples synthétiques.

Utilisez UTF-8, LF et des modifications ciblées, puis lancez la commande ci-dessus.
Pour une Release, vérifiez version/tag, taille, SHA-256 et pages de téléchargement.
Les tests documentaires ne remplacent pas les tests applicatifs privés.

Les contributions originales au hub suivent la licence MIT limitée par
[LICENSE](LICENSE), sans remplacer les droits upstream. Toute acceptation et
publication reste une décision du mainteneur.
