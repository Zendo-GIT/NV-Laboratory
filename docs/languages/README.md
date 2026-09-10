# Documentation languages · Langues de documentation

[English home](../../README.md) · [Accueil français](../../README.fr.md)

The documentation covers the same **34 languages** as the NV application catalog.
Use the selector at the top of a page to switch to that page in another language.
English is GitHub's default README; GitHub does not automatically redirect visitors
by browser language. The application language and installer language are separate settings.

Chaque langue propose l'accueil, les quatre guides complets, l'installation,
les téléchargements, le support, la provenance, la maintenance, les Releases,
les crédits, les contributions, la sécurité, le changelog et les index de licences.
Le sélecteur en haut de page conserve le document consulté.

| Language | Code | Home |
| --- | --- | --- |
| العربية | `ar` | [العربية](ar/README.md) |
| বাংলা | `bn` | [বাংলা](bn/README.md) |
| 简体中文 | `zh` | [简体中文](zh/README.md) |
| Čeština | `cs` | [Čeština](cs/README.md) |
| Dansk | `da` | [Dansk](da/README.md) |
| Nederlands | `nl` | [Nederlands](nl/README.md) |
| English | `en` | [English](../../README.md) |
| Filipino | `fil` | [Filipino](fil/README.md) |
| Suomi | `fi` | [Suomi](fi/README.md) |
| Français | `fr` | [Français](../../README.fr.md) |
| Deutsch | `de` | [Deutsch](de/README.md) |
| Ελληνικά | `el` | [Ελληνικά](el/README.md) |
| हिन्दी | `hi` | [हिन्दी](hi/README.md) |
| Magyar | `hu` | [Magyar](hu/README.md) |
| Bahasa Indonesia | `id` | [Bahasa Indonesia](id/README.md) |
| Italiano | `it` | [Italiano](it/README.md) |
| 日本語 | `ja` | [日本語](ja/README.md) |
| 한국어 | `ko` | [한국어](ko/README.md) |
| मराठी | `mr` | [मराठी](mr/README.md) |
| فارسی | `fa` | [فارسی](fa/README.md) |
| Polski | `pl` | [Polski](pl/README.md) |
| Português | `pt` | [Português](pt/README.md) |
| ਪੰਜਾਬੀ | `pa` | [ਪੰਜਾਬੀ](pa/README.md) |
| Română | `ro` | [Română](ro/README.md) |
| Русский | `ru` | [Русский](ru/README.md) |
| Español | `es` | [Español](es/README.md) |
| Kiswahili | `sw` | [Kiswahili](sw/README.md) |
| Svenska | `sv` | [Svenska](sv/README.md) |
| தமிழ் | `ta` | [தமிழ்](ta/README.md) |
| ไทย | `th` | [ไทย](th/README.md) |
| Türkçe | `tr` | [Türkçe](tr/README.md) |
| Українська | `uk` | [Українська](uk/README.md) |
| اردو | `ur` | [اردو](ur/README.md) |
| Tiếng Việt | `vi` | [Tiếng Việt](vi/README.md) |

## Translation quality and legal texts

The existing English and French guides remain the reference editions. Additional
editions were produced with machine assistance and checked for coverage, links,
technical values and Markdown structure. They have **not** been reviewed by native
speakers of every language. Read the English reference if wording is unclear and
report a correction with the language, page and proposed wording. Arabic, Persian
and Urdu pages declare right-to-left direction.

La traduction automatique ne constitue pas une validation par un locuteur natif.
Les formulations peuvent encore être améliorées. Les noms de logiciels, commandes,
fichiers, paramètres, versions, hashes et URL sont conservés. Les notices juridiques
originales restent intégrales ; les explications traduites ne les remplacent pas.

## Maintaining translations

English and existing French paths remain stable. Other editions mirror the same
paths under `docs/languages/<code>`. Original license texts and images are shared.
The [catalog](catalog.json) records the 20 documents, language paths and exact
fingerprints; it contains no application source. Do not present an untranslated
English copy as a completed language edition.

When changing a reference page, update affected translations, navigation and the
catalog fingerprints together. Preserve technical tokens and original notices.
Run `python tools/validate_repository.py` from the repository root before a commit.
The validator checks coverage, hashes and links without contacting a translation
service or running any application. [Contribution rules](../../CONTRIBUTING.md).
