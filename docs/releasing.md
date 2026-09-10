<!-- nv-language-navigation:start -->
🌐 English | [Français](releasing.fr.md) · [NV Laboratory](../README.md)

<details>
<summary>🌐 Language · 34</summary>

[العربية](languages/ar/docs/releasing.md) · [বাংলা](languages/bn/docs/releasing.md) · [简体中文](languages/zh/docs/releasing.md) · [Čeština](languages/cs/docs/releasing.md) · [Dansk](languages/da/docs/releasing.md) · [Nederlands](languages/nl/docs/releasing.md) · **English** · [Filipino](languages/fil/docs/releasing.md) · [Suomi](languages/fi/docs/releasing.md) · [Français](releasing.fr.md) · [Deutsch](languages/de/docs/releasing.md) · [Ελληνικά](languages/el/docs/releasing.md) · [हिन्दी](languages/hi/docs/releasing.md) · [Magyar](languages/hu/docs/releasing.md) · [Bahasa Indonesia](languages/id/docs/releasing.md) · [Italiano](languages/it/docs/releasing.md) · [日本語](languages/ja/docs/releasing.md) · [한국어](languages/ko/docs/releasing.md) · [मराठी](languages/mr/docs/releasing.md) · [فارسی](languages/fa/docs/releasing.md) · [Polski](languages/pl/docs/releasing.md) · [Português](languages/pt/docs/releasing.md) · [ਪੰਜਾਬੀ](languages/pa/docs/releasing.md) · [Română](languages/ro/docs/releasing.md) · [Русский](languages/ru/docs/releasing.md) · [Español](languages/es/docs/releasing.md) · [Kiswahili](languages/sw/docs/releasing.md) · [Svenska](languages/sv/docs/releasing.md) · [தமிழ்](languages/ta/docs/releasing.md) · [ไทย](languages/th/docs/releasing.md) · [Türkçe](languages/tr/docs/releasing.md) · [Українська](languages/uk/docs/releasing.md) · [اردو](languages/ur/docs/releasing.md) · [Tiếng Việt](languages/vi/docs/releasing.md)

[Translation policy](languages/README.md)

</details>
<!-- nv-language-navigation:end -->

# Publishing and releases

The public repository is **Zendo-GIT/NV-Laboratory**. Documentation changes are
reviewed, committed and pushed by the maintainer with **GitHub Desktop**. A local
commit does not upload files. Binary packages are separate GitHub Release assets;
they never belong in the Git changes list.

## Documentation updates

1. Open the **NV-Laboratory** folder in GitHub Desktop.
2. Review documentation, notices, images, JSON metadata and the documentation validator.
3. Run `python tools/validate_repository.py` from that folder.
4. Commit the reviewed changes, then use **Push origin**. Check the Actions result.
5. Keep the public author identity **禅堂 Zendo (RevoluSound Team)** and the account's GitHub `noreply` address.

Never select the parent development workspace, private audit directory or binary
attachment directory. [Commit email privacy](https://docs.github.com/en/account-and-profile/how-tos/email-preferences/setting-your-commit-email-address).

## Independent application releases

| Tool | Tag | Version policy |
| --- | --- | --- |
| NVIDIA Profile Inspector – NV Tools Fork | nvpi-v3.0.2.3 | Existing four-part application version; setup revision 2 has its own filename |
| NVDriverForge | nvdriverforge-v0.1.3 | Existing 0.x scheme; versioned updates preserve earlier packages |
| NVMFG Unlock40 | nvmfg-unlock40-v0.1.1 | UI2 candidate identified by exact hashes without inventing a new application version |
| NVRasterPulse | nvrasterpulse-v0.1 | Existing two-part version |

The maintainer can publish directly or authorize an assistant to publish the audited
assets. Publication is explicit; no workflow creates a Release on each commit.

1. Review the current prepublication report, sources of the binaries, licenses and SHA-256 values.
2. Create a draft for the tool's tag, targeting the reviewed hub commit. Include the prepared version-specific release notes.
3. Attach only that version's Setup/portable assets, `Licenses-and-Credits.zip` and `SHA256SUMS.txt`.
4. Check compatibility, installation, dependencies, changes and known limits. Keep RTSS prominent for NVRasterPulse.
5. Publish, verify the public asset URLs, sizes and hashes, and record the actual publication date in `docs/releases.json`.
6. Update the download pages and translations, then commit/push their changes in GitHub Desktop.

The per-project tag links avoid sending users to another tool through a shared
`releases/latest` link. GitHub's automatic **Source code** archives contain this
documentation hub. Application sources stay private. Original component notices
remain intact, and a release does not resolve NVMFG's documented NVIDIA SDK reserve.

## Integrity and storage

Never silently replace published binary bytes. Use a new explicit version or
installer revision with new hashes. Legal sidecars supplement embedded notices.
NVDriverForge 0.1.3 portable is 141,760,351 bytes, above GitHub's ordinary 100 MiB
Git-file limit. Release attachments avoid putting binaries or Git LFS in this hub.
[GitHub large-file guidance](https://docs.github.com/en/repositories/working-with-files/managing-large-files/about-large-files-on-github).

Private vulnerability reporting should be enabled in repository security settings.
Verify its availability before directing sensitive reports there; [SECURITY.md](../SECURITY.md)
provides a fallback that does not expose vulnerability details.

[Download catalog](downloads.md) · [GitHub release documentation](https://docs.github.com/en/repositories/releasing-projects-on-github/managing-releases-in-a-repository)
