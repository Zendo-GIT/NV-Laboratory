# Security / Sécurité

This policy covers NV Tools application packages and this distribution hub.
The maintainer prioritizes reports affecting the latest published version of
each tool. Prepared candidates are not an announced supported stable release.
No response deadline or security certification is promised.

## English: report privately

For vulnerabilities, unsafe elevated behavior, unintended destructive changes,
or sensitive data exposure, use the repository's **Security → Report a vulnerability**
feature **when it is enabled**:
[private report](https://github.com/Zendo-GIT/NV-Laboratory/security/advisories/new).

**Initial setup:** the maintainer must enable private vulnerability reporting after
creating the public repository. This file does not enable it, and no mailbox or
private channel is claimed to exist before then.

If the button is unavailable, open a public Issue containing only:
“I need a private contact channel for a security report concerning [tool/version].”
Do not include exploit details, credentials, affected paths, logs or attachments.
Wait for the maintainer to provide a private channel before sharing them.

In the private report, include tool/version and hash, Windows/GPU/driver versions,
impact, minimal safe reproduction and whether recovery is needed. Redact secrets
and personal data; preserve local recovery files. Do not upload proprietary driver
or game DLLs. Coordinate disclosure with the maintainer; a patch/release requires
review and is not automatic.

## Français : signalement confidentiel

Pour une faille, une élévation dangereuse, un changement destructif imprévu ou une
fuite de données, utilisez **Security → Report a vulnerability**, une fois activé :
[signalement privé](https://github.com/Zendo-GIT/NV-Laboratory/security/advisories/new).

Le mainteneur doit activer cette fonction après création du dépôt public.
Ce fichier ne l'active pas et ne prétend pas qu'un canal privé existe déjà.

Si le bouton manque, ouvrez seulement une Issue :
« J'ai besoin d'un canal privé pour signaler un problème de sécurité sur [outil/version]. »
N'y joignez aucun détail technique sensible, secret, chemin, journal ou pièce jointe.
Attendez le canal privé fourni par le mainteneur.

En privé, précisez version/hash, Windows/GPU/pilote, impact, reproduction minimale
et besoin de récupération. Masquez les données sensibles et préservez les fichiers
locaux utiles. N'envoyez pas de DLL propriétaire de jeu ou pilote.
La correction, sa publication et la divulgation doivent être coordonnées ;
aucun délai de réponse n'est garanti.

[GitHub private reporting documentation](https://docs.github.com/en/code-security/how-tos/report-and-fix-vulnerabilities/configure-vulnerability-reporting/configure-for-a-repository).
