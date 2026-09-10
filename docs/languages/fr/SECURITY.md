<!-- nv-language-navigation:start -->
🌐 [English](../../../SECURITY.md) | Français · [NV Laboratory](../../../README.fr.md)

<details>
<summary>🌐 Language · 34</summary>

[العربية](../ar/SECURITY.md) · [বাংলা](../bn/SECURITY.md) · [简体中文](../zh/SECURITY.md) · [Čeština](../cs/SECURITY.md) · [Dansk](../da/SECURITY.md) · [Nederlands](../nl/SECURITY.md) · [English](../../../SECURITY.md) · [Filipino](../fil/SECURITY.md) · [Suomi](../fi/SECURITY.md) · **Français** · [Deutsch](../de/SECURITY.md) · [Ελληνικά](../el/SECURITY.md) · [हिन्दी](../hi/SECURITY.md) · [Magyar](../hu/SECURITY.md) · [Bahasa Indonesia](../id/SECURITY.md) · [Italiano](../it/SECURITY.md) · [日本語](../ja/SECURITY.md) · [한국어](../ko/SECURITY.md) · [मराठी](../mr/SECURITY.md) · [فارسی](../fa/SECURITY.md) · [Polski](../pl/SECURITY.md) · [Português](../pt/SECURITY.md) · [ਪੰਜਾਬੀ](../pa/SECURITY.md) · [Română](../ro/SECURITY.md) · [Русский](../ru/SECURITY.md) · [Español](../es/SECURITY.md) · [Kiswahili](../sw/SECURITY.md) · [Svenska](../sv/SECURITY.md) · [தமிழ்](../ta/SECURITY.md) · [ไทย](../th/SECURITY.md) · [Türkçe](../tr/SECURITY.md) · [Українська](../uk/SECURITY.md) · [اردو](../ur/SECURITY.md) · [Tiếng Việt](../vi/SECURITY.md)

[Translation policy](../README.md)

</details>
<!-- nv-language-navigation:end -->

<!-- nv-translation-notice:start -->
> Traduction assistée par machine de l’anglais. Les noms techniques, commandes, URL et textes juridiques originaux sont conservés. L'évaluation par un locuteur natif est la bienvenue ; consulter la référence anglaise si le libellé n’est pas clair.
<!-- nv-translation-notice:end -->

<a id="security"></a>
# Sécurité

Cette politique couvre les packages d'application NV Tools et ce hub de distribution. Le responsable donne la priorité aux rapports affectant la dernière version publiée de chaque outil. Les candidats préparés ne sont pas une version stable prise en charge annoncée. Aucun délai de réponse ni certification de sécurité n’est promis.

<a id="report-privately"></a>
## Signaler en privé

En cas de vulnérabilités, de comportements élevés dangereux, de modifications destructrices involontaires ou d'exposition de données sensibles, utilisez la fonctionnalité **Sécurité → Report a vulnerability** du référentiel **lorsqu'elle est activée** : [rapport privé](https://github.com/Zendo-GIT/NV-Laboratory/security/advisories/new).

**Configuration initiale :** le responsable doit activer le rapport privé sur les vulnérabilités après avoir créé le référentiel public. Ce fichier ne l'active pas, et aucune boîte aux lettres ou canal privé n'existe avant cela.

Si le bouton n'est pas disponible, ouvrez un problème public contenant uniquement : « J'ai besoin d'un canal de contact privé pour un rapport de sécurité concernant [outil/version] ». N'incluez pas les détails de l'exploit, les informations d'identification, les chemins concernés, les journaux ou les pièces jointes. Attendez que le responsable fournisse un canal privé avant de les partager.

Dans le rapport privé, indiquez l'outil/la version et le hachage, les versions Windows/GPU/du pilote, l'impact, la reproduction minimale sécurisée et si une récupération est nécessaire. Expurger les secrets et les données personnelles ; conserver les fichiers de récupération locaux. Ne téléchargez pas de pilote propriétaire ou de DLL de jeu. Coordonner la divulgation avec le responsable ; un correctif/une version nécessite une révision et n'est pas automatique.


[Documentation de reporting privé GitHub](https://docs.github.com/en/code-security/how-tos/report-and-fix-vulnerabilities/configure-vulnerability-reporting/configure-for-a-repository).
