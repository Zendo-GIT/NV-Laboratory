<!-- nv-language-navigation:start -->
🌐 English | [Français](docs/languages/fr/CONTRIBUTING.md) · [NV Laboratory](README.md)

<details>
<summary>🌐 Language · 34</summary>

[العربية](docs/languages/ar/CONTRIBUTING.md) · [বাংলা](docs/languages/bn/CONTRIBUTING.md) · [简体中文](docs/languages/zh/CONTRIBUTING.md) · [Čeština](docs/languages/cs/CONTRIBUTING.md) · [Dansk](docs/languages/da/CONTRIBUTING.md) · [Nederlands](docs/languages/nl/CONTRIBUTING.md) · **English** · [Filipino](docs/languages/fil/CONTRIBUTING.md) · [Suomi](docs/languages/fi/CONTRIBUTING.md) · [Français](docs/languages/fr/CONTRIBUTING.md) · [Deutsch](docs/languages/de/CONTRIBUTING.md) · [Ελληνικά](docs/languages/el/CONTRIBUTING.md) · [हिन्दी](docs/languages/hi/CONTRIBUTING.md) · [Magyar](docs/languages/hu/CONTRIBUTING.md) · [Bahasa Indonesia](docs/languages/id/CONTRIBUTING.md) · [Italiano](docs/languages/it/CONTRIBUTING.md) · [日本語](docs/languages/ja/CONTRIBUTING.md) · [한국어](docs/languages/ko/CONTRIBUTING.md) · [मराठी](docs/languages/mr/CONTRIBUTING.md) · [فارسی](docs/languages/fa/CONTRIBUTING.md) · [Polski](docs/languages/pl/CONTRIBUTING.md) · [Português](docs/languages/pt/CONTRIBUTING.md) · [ਪੰਜਾਬੀ](docs/languages/pa/CONTRIBUTING.md) · [Română](docs/languages/ro/CONTRIBUTING.md) · [Русский](docs/languages/ru/CONTRIBUTING.md) · [Español](docs/languages/es/CONTRIBUTING.md) · [Kiswahili](docs/languages/sw/CONTRIBUTING.md) · [Svenska](docs/languages/sv/CONTRIBUTING.md) · [தமிழ்](docs/languages/ta/CONTRIBUTING.md) · [ไทย](docs/languages/th/CONTRIBUTING.md) · [Türkçe](docs/languages/tr/CONTRIBUTING.md) · [Українська](docs/languages/uk/CONTRIBUTING.md) · [اردو](docs/languages/ur/CONTRIBUTING.md) · [Tiếng Việt](docs/languages/vi/CONTRIBUTING.md)

[Translation policy](docs/languages/README.md)

</details>
<!-- nv-language-navigation:end -->

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

Documentation PRs should keep the 34 language counterparts and navigation aligned,
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

Gardez les versions dans les 34 langues cohérentes, sans traduire commandes,
fichiers et noms techniques. Décrivez les fonctions réelles. Identifiez version,
provenance et droits des captures ; masquez les données personnelles et signalez
les exemples synthétiques.

Utilisez UTF-8, LF et des modifications ciblées, puis lancez la commande ci-dessus.
Pour une Release, vérifiez version/tag, taille, SHA-256 et pages de téléchargement.
Les tests documentaires ne remplacent pas les tests applicatifs privés.

Les contributions originales au hub suivent la licence MIT limitée par
[LICENSE](LICENSE), sans remplacer les droits upstream. Toute acceptation et
publication reste une décision du mainteneur.
