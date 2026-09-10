<!-- nv-language-navigation:start -->
🌐 [English](../../../CONTRIBUTING.md) | Français · [NV Laboratory](../../../README.fr.md)

<details>
<summary>🌐 Language · 34</summary>

[العربية](../ar/CONTRIBUTING.md) · [বাংলা](../bn/CONTRIBUTING.md) · [简体中文](../zh/CONTRIBUTING.md) · [Čeština](../cs/CONTRIBUTING.md) · [Dansk](../da/CONTRIBUTING.md) · [Nederlands](../nl/CONTRIBUTING.md) · [English](../../../CONTRIBUTING.md) · [Filipino](../fil/CONTRIBUTING.md) · [Suomi](../fi/CONTRIBUTING.md) · **Français** · [Deutsch](../de/CONTRIBUTING.md) · [Ελληνικά](../el/CONTRIBUTING.md) · [हिन्दी](../hi/CONTRIBUTING.md) · [Magyar](../hu/CONTRIBUTING.md) · [Bahasa Indonesia](../id/CONTRIBUTING.md) · [Italiano](../it/CONTRIBUTING.md) · [日本語](../ja/CONTRIBUTING.md) · [한국어](../ko/CONTRIBUTING.md) · [मराठी](../mr/CONTRIBUTING.md) · [فارسی](../fa/CONTRIBUTING.md) · [Polski](../pl/CONTRIBUTING.md) · [Português](../pt/CONTRIBUTING.md) · [ਪੰਜਾਬੀ](../pa/CONTRIBUTING.md) · [Română](../ro/CONTRIBUTING.md) · [Русский](../ru/CONTRIBUTING.md) · [Español](../es/CONTRIBUTING.md) · [Kiswahili](../sw/CONTRIBUTING.md) · [Svenska](../sv/CONTRIBUTING.md) · [தமிழ்](../ta/CONTRIBUTING.md) · [ไทย](../th/CONTRIBUTING.md) · [Türkçe](../tr/CONTRIBUTING.md) · [Українська](../uk/CONTRIBUTING.md) · [اردو](../ur/CONTRIBUTING.md) · [Tiếng Việt](../vi/CONTRIBUTING.md)

[Translation policy](../README.md)

</details>
<!-- nv-language-navigation:end -->

<!-- nv-translation-notice:start -->
> Traduction assistée par machine de l’anglais. Les noms techniques, commandes, URL et textes juridiques originaux sont conservés. L'évaluation par un locuteur natif est la bienvenue ; consulter la référence anglaise si le libellé n’est pas clair.
<!-- nv-translation-notice:end -->

<a id="contributing"></a>
# Contribuer

NV Laboratory est géré par 禅堂 Zendo (RevoluSound Team). Le responsable décide de ce qui est accepté et publié. L'ouverture d'un problème ou d'une pull request ne signifie pas qu'une contribution est acceptée ou autorisée pour la distribution.

Utilisez le formulaire de bogue ou de fonctionnalité et identifiez le programme/la version. Recherchez d'abord les problèmes existants. Discutez des changements substantiels avant de préparer une contribution importante. Pour des questions de sécurité, suivez [SECURITY.md](SECURITY.md).

Ce hub public contient de la documentation, des avis, des métadonnées de version et la validation du référentiel. La source de l’application et les tests sont gérés en privé. Ne soumettez pas de code décompilé, de source privée, d'informations d'identification, de profils utilisateur ou de charges utiles exécutables.

Les PR de documentation doivent maintenir les 34 équivalents linguistiques et la navigation alignés, conserver les noms de commande/fichier/produit et décrire le comportement réel. Les nouvelles captures d'écran doivent être les vôtres, identifiées par leur version et exemptes de détails personnels ; les données synthétiques doivent être étiquetées. Fournissez la provenance et l’autorisation pour chaque nouvel actif tiers.

Utilisez UTF-8, LF, Markdown lisible et de petites modifications ciblées. Le validateur Python utilise uniquement la bibliothèque standard. Faites correspondre son style existant, évitez les dépendances inutiles et exécutez :

```text
python tools/validate_repository.py
```

Pour les modifications des métadonnées de la version, incluez la version/balise exacte, la taille des fichiers et SHA-256 à partir des binaires audités, et gardez les pages de téléchargement alignées. Les modifications d’application nécessitent une construction/des tests privés adaptés au comportement affecté ; une vérification de la documentation n'est pas un test d'application. N’inventez jamais des résultats ou des gains de tests historiques.

En contribuant au matériel original du hub, vous acceptez sa licence MIT étendue dans [LICENCE](../../../LICENSE). Conservez les avis des tiers et identifiez vos modifications ; ne remplace pas une licence en amont. L'acceptation et la publication restent des décisions du responsable.
