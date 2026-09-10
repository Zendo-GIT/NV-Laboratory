<!-- nv-language-navigation:start -->
🌐 [English](installation.md) | Français · [NV Laboratory](../README.fr.md)

<details>
<summary>🌐 Language · 34</summary>

[العربية](languages/ar/docs/installation.md) · [বাংলা](languages/bn/docs/installation.md) · [简体中文](languages/zh/docs/installation.md) · [Čeština](languages/cs/docs/installation.md) · [Dansk](languages/da/docs/installation.md) · [Nederlands](languages/nl/docs/installation.md) · [English](installation.md) · [Filipino](languages/fil/docs/installation.md) · [Suomi](languages/fi/docs/installation.md) · **Français** · [Deutsch](languages/de/docs/installation.md) · [Ελληνικά](languages/el/docs/installation.md) · [हिन्दी](languages/hi/docs/installation.md) · [Magyar](languages/hu/docs/installation.md) · [Bahasa Indonesia](languages/id/docs/installation.md) · [Italiano](languages/it/docs/installation.md) · [日本語](languages/ja/docs/installation.md) · [한국어](languages/ko/docs/installation.md) · [मराठी](languages/mr/docs/installation.md) · [فارسی](languages/fa/docs/installation.md) · [Polski](languages/pl/docs/installation.md) · [Português](languages/pt/docs/installation.md) · [ਪੰਜਾਬੀ](languages/pa/docs/installation.md) · [Română](languages/ro/docs/installation.md) · [Русский](languages/ru/docs/installation.md) · [Español](languages/es/docs/installation.md) · [Kiswahili](languages/sw/docs/installation.md) · [Svenska](languages/sv/docs/installation.md) · [தமிழ்](languages/ta/docs/installation.md) · [ไทย](languages/th/docs/installation.md) · [Türkçe](languages/tr/docs/installation.md) · [Українська](languages/uk/docs/installation.md) · [اردو](languages/ur/docs/installation.md) · [Tiếng Việt](languages/vi/docs/installation.md)

[Translation policy](languages/README.md)

</details>
<!-- nv-language-navigation:end -->

<a id="installation-guide"></a>
# Guide d'installation

Commencez par les [téléchargements](downloads.fr.md), avec statut et noms exacts
des fichiers. Les programmes sont indépendants : choisissez ceux dont vous avez besoin.

> **Pour NVRasterPulse, installez [RTSS depuis Guru3D](https://www.guru3d.com/download/rtss-rivatuner-statistics-server-download/) avant d'ouvrir le gestionnaire.**
> RTSS doit fonctionner pour appliquer les limites ; il n'est pas inclus.

| Outil | Édition installée | Édition portable | Prérequis principal |
| --- | --- | --- | --- |
| NVIDIA Profile Inspector – NV Tools Fork | NVPI-CustomNV-3.0.2.3-Setup-r2.exe | Extraire le ZIP NVPI complet | Pilote NVIDIA et .NET Framework 4.8 |
| NVDriverForge | NVDriverForge-Setup.exe | NVDriverForge.exe, runtime inclus | Paquet NVIDIA original compatible pour installer le pilote |
| NVMFG Unlock40 | NVMFGUnlock40-0.1.1-Setup-x64.exe | Extraire tout le ZIP avec ses sous-dossiers | RTX 40, DLSS FG existant, fournisseur exact et helpers .NET Framework 4.8 |
| NVRasterPulse | NVRasterPulse-0.1-win-x64-Setup.exe | Extraire tout le ZIP RP | RTSS et .NET Framework 4.8 |

<a id="download-verify-install"></a>
## Télécharger, vérifier, installer

1. Dans la Release publiée, prenez le fichier applicatif indiqué, le ZIP de notices et SHA256SUMS.txt.
2. Utilisez l'[exemple SHA-256](downloads.fr.md#sha-256) avec le vrai nom téléchargé.
3. Lancez Setup normalement, ou extrayez tout le portable dans un nouveau dossier local accessible en écriture. Ne lancez pas l'application depuis le ZIP.
4. Ouvrez son EXE et gardez les fichiers de licence, configuration et données associés.
5. Lisez son guide avant d'activer des réglages ou opérations système.

Les exécutables actuels ne sont pas signés. Un hash concordant confirme les octets
attendus, pas la sécurité ou la compatibilité. Ne désactivez pas les protections
Windows pour masquer un avertissement.

Installer NVDF ou le compagnon NVPI ne revient pas à installer un pilote.
Le compagnon conserve son nom d'installation interne. Son bouton RasterPulse
élevé exige une installation système protégée ; les autres copies de RP s'ouvrent
par leur propre raccourci.

NVMFG est expérimental et conserve la [réserve de licence NVIDIA documentée](provenance.fr.md).
Aucun pilote, fournisseur/modèle NGX ou runtime Streamline de jeu n'est inclus.
Téléchargements SDK et mises à jour des jeux sont des opérations distinctes explicites.

<a id="language-and-updates"></a>
## Langues et mises à jour

Le sélecteur English/Français concerne la documentation. NVDF, NVMFG et RP possèdent
leur réglage d'interface en 34 langues ; NVPI conserve sa prise en charge existante.
Certains messages techniques des installateurs ont un repli anglais.

Conservez l'identité d'installation, fermez le logiciel et gardez les sauvegardes.
Pour NVMFG, fermez les jeux et résolvez toute récupération de profils en attente.
Pour portable, utilisez un dossier neuf sans mélanger les versions.

<a id="removing-a-tool"></a>
## Retirer un outil

Désinstaller une application ne restaure pas automatiquement ses réglages.

- **NVPI :** restaurez si souhaité profils et écran avant son retrait.
- **NVDF :** utilisez la récupération pour les réglages avancés/NVENC avant désinstallation. Pilote, réglages et sauvegardes restent présents.
- **NVMFG :** fermez les jeux, désactivez/quittez le contrôleur, résolvez la récupération NVIDIA et restaurez les SDK voulus.
- **RP :** retirez d'abord les paramètres voulus du limiteur. Les limites RTSS enregistrées et RTSS restent présents après désinstallation.

Les [guides des projets](../README.fr.md#projets) indiquent les chemins de données
et limitations. Consultez l'[aide](support.fr.md) si une récupération échoue.
