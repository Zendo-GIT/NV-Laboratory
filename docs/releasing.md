🌐 **Language:** English | [Français](releasing.fr.md) · [Home](../README.md)

# Manual publishing and releases

The maintainer creates the remote repository and pushes with **GitHub Desktop**.
No remote repository, push, deployment or Release is created by this preparation.

## First repository publication

1. Review the private prepublication report and resolve any NOT READY items before treating the complete distribution as cleared.
2. In GitHub Desktop, use **File → Add local repository** and select the prepared **NV-Laboratory** folder itself.
3. Review the changes: documentation, notices, images, JSON metadata and repository automation only. No application source or EXE/DLL/ZIP should appear.
4. Create the first local commit, for example `chore: initialize NV Laboratory documentation hub`. No earlier history is fabricated.
5. Use **Publish repository** for owner **Zendo-GIT**, name **NV-Laboratory**; choose public visibility yourself when ready.
6. Enable private vulnerability reporting in GitHub's security settings. Verify the private reporting button before announcing it.
7. Check the documentation workflow result and both language entry points.

The repository has no configured remote before your publication step. Never
select the parent research workspace or the private audit/attachment directory.

The maintainer's public identity is **禅堂 Zendo (RevoluSound Team)**.
Also check the first commit's author and GitHub `noreply` address in GitHub Desktop:
commit metadata is part of the publication.
[Commit email privacy](https://docs.github.com/en/account-and-profile/how-tos/email-preferences/setting-your-commit-email-address).

## Independent application releases

| Tool | First planned tag | Version policy |
| --- | --- | --- |
| NVPI fork | nvpi-v3.0.2.3 | Preserve the existing four-part application version |
| NVDriverForge | nvdriverforge-v0.1.2 | Preserve 0.x versioning; SemVer can guide future compatible changes |
| NVMFG Unlock40 | nvmfg-unlock40-v0.1.1 | Preserve the public number; candidate UI2 is identified by exact hashes |
| NVRasterPulse | nvrasterpulse-v0.1 | Preserve the requested two-part public version |

Do not force 3.0.2.3 or 0.1 into a fictitious SemVer release. Future changes
must have an explicit version/revision and new hashes. Never replace an already
published binary under the same asset identity without a clearly identified revision.

1. Open the GitHub **Releases → Draft a new release** page after the hub is published.
2. Use the tool's tag above, targeting the reviewed hub commit. Copy its prepared local release body.
3. Upload only that tag's application assets, `Licenses-and-Credits.zip` and `SHA256SUMS.txt`.
4. Check version, actual publication date, compatibility, installation, changes, dependencies, known issues and hashes. Keep RTSS at the top of the RP Release.
5. Choose any prerelease designation based on actual support status. Plain numeric app versions do not themselves certify stability.
6. Publish manually when the report and outstanding issues permit it. No workflow publishes on commit.

The complete asset list and hashes are in [releases.json](releases.json). Keep
the selected asset bytes unchanged. NVPI setup revision 2 has its own filename
and hashes; the application payload is unchanged. Legal sidecars supplement, not overwrite,
embedded original notices. NVMFG's unresolved NVIDIA SDK reserve remains in its
candidate notes; it is not silently removed by creating a Release.

## Make downloads live

After the Release actually exists, update that project's `status` to
`published` and set its real `release_date` in releases.json. Change the matching
English/French download and homepage publication statements. Verify the actual
Release and every asset link, then run the repository validator and commit with
GitHub Desktop. Do not label a pending candidate “latest available”.

This monorepo uses **per-project tag links**, not a shared `releases/latest`
button which could lead to another tool. GitHub's automatically generated
“Source code” archives contain the hub documentation, not application source.

## Binary storage

NVDriverForge's standalone portable is 141,525,846 bytes, exceeding GitHub's
100 MiB ordinary Git-file limit. All applications are therefore Release attachments,
outside Git history; no Git LFS setup is needed for this hub.
[GitHub large-file guidance](https://docs.github.com/en/repositories/working-with-files/managing-large-files/about-large-files-on-github).

Keep exact candidate hashes, complete notices and recovery information.
Build/tests for functional changes remain in the private projects.
[GitHub release documentation](https://docs.github.com/en/repositories/releasing-projects-on-github/managing-releases-in-a-repository).
