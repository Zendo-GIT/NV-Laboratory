<!-- nv-language-navigation:start -->
🌐 English | [Français](README.fr.md) · [NV Laboratory](README.md)

<details>
<summary>🌐 Language · 34</summary>

[العربية](docs/languages/ar/README.md) · [বাংলা](docs/languages/bn/README.md) · [简体中文](docs/languages/zh/README.md) · [Čeština](docs/languages/cs/README.md) · [Dansk](docs/languages/da/README.md) · [Nederlands](docs/languages/nl/README.md) · **English** · [Filipino](docs/languages/fil/README.md) · [Suomi](docs/languages/fi/README.md) · [Français](README.fr.md) · [Deutsch](docs/languages/de/README.md) · [Ελληνικά](docs/languages/el/README.md) · [हिन्दी](docs/languages/hi/README.md) · [Magyar](docs/languages/hu/README.md) · [Bahasa Indonesia](docs/languages/id/README.md) · [Italiano](docs/languages/it/README.md) · [日本語](docs/languages/ja/README.md) · [한국어](docs/languages/ko/README.md) · [मराठी](docs/languages/mr/README.md) · [فارسی](docs/languages/fa/README.md) · [Polski](docs/languages/pl/README.md) · [Português](docs/languages/pt/README.md) · [ਪੰਜਾਬੀ](docs/languages/pa/README.md) · [Română](docs/languages/ro/README.md) · [Русский](docs/languages/ru/README.md) · [Español](docs/languages/es/README.md) · [Kiswahili](docs/languages/sw/README.md) · [Svenska](docs/languages/sv/README.md) · [தமிழ்](docs/languages/ta/README.md) · [ไทย](docs/languages/th/README.md) · [Türkçe](docs/languages/tr/README.md) · [Українська](docs/languages/uk/README.md) · [اردو](docs/languages/ur/README.md) · [Tiếng Việt](docs/languages/vi/README.md)

[Translation policy](docs/languages/README.md)

</details>
<!-- nv-language-navigation:end -->

# NV Laboratory

**NV Tools by 禅堂 Zendo (RevoluSound Team).** Four independent Windows utilities for NVIDIA driver profiles, driver installation, experimental Multi Frame Generation and RTSS frame limits.

[Get the tools](docs/downloads.md) · [Installation](docs/installation.md) · [Compatibility & help](docs/support.md) · [Credits & licenses](THIRD_PARTY_NOTICES.md)

> **NVRasterPulse requires RTSS.** Install [RivaTuner Statistics Server from Guru3D](https://www.guru3d.com/download/rtss-rivatuner-statistics-server-download/) first. RTSS must be running for its FPS limits to work. It is downloaded separately.

## Projects

| Project | Purpose | Version | Documentation | Download |
| --- | --- | --- | --- | --- |
| **NVIDIA Profile Inspector – NV Tools Fork** | NVIDIA driver profile editor with added display, color, HDR and ICC/WCS controls. Formerly NVPI Custom. | 3.0.2.3 | [Guide](NVIDIA-Profile-Inspector/README.md) | [Packages](docs/downloads.md#nvidia-profile-inspector) |
| **NVDriverForge** | Select driver components, review optional tweaks and install an original NVIDIA driver package. | 0.1.3 | [Guide](NVDriverForge/README.md) | [Packages](docs/downloads.md#nvdriverforge) |
| **NVMFG Unlock40** | Experimental RTX 40 MFG tool with per-game choices and Streamline SDK maintenance. | 0.1.1 | [Guide](NVMFG-Unlock40/README.md) | [Packages & status](docs/downloads.md#nvmfg-unlock40) |
| **NVRasterPulse** | Manage RTSS FPS limits per executable, with fractional values, backups and tray access. | 0.1 | [Guide](NVRasterPulse/README.md) | [Packages](docs/downloads.md#nvrasterpulse) |

**Downloads:** the [download page](docs/downloads.md) lists each version’s status, files and SHA-256 values. Experimental features and compatibility limits are described in the project guides.

## Start here

1. Pick one tool above. Each works independently; installing the whole suite is unnecessary.
2. Read its requirements and choose **Setup** for an installed app, or **portable** for a separate folder.
3. When its Release is published, download the named application asset, read the accompanying notices and compare its SHA-256.
4. Keep backups before changing a driver, display setting, NVIDIA profile or game runtime.

Documentation is available in the same 34 languages as the NV applications through the selector at the top of each guide. GitHub does not automatically select a README by browser language. The documentation language and the application's own language setting are separate.

## Provenance and ownership

This hub distributes documentation and compiled applications. Application source code is maintained privately. Upstream projects retain their authorship and licenses; private source distribution does not replace those terms.

- The Profile Inspector fork retains Orbmu2k's MIT license and is explicitly identified as a fork.
- NVDriverForge has its own binary distribution terms and includes separately licensed runtime/tool components.
- NVMFG Unlock40 is an independently developed application. RTX40MFG-Unlock was consulted for comparison and refinement; shared native components retain their MIT credits. MinHook and NVIDIA SDK terms remain separate.
- NVRasterPulse retains the supplied MIT license and credits the Profile Inspector-derived UI. RTSS is a required external program.

See the [complete component table](THIRD_PARTY_NOTICES.md), [file provenance and changes](docs/provenance.md), and [license scope](LICENSE).

## Other projects – RevoluSound Team

These are separate audio mod projects, linked here to help you discover the team's work.

| Game | Project | About |
| --- | --- | --- |
| Forza Horizon 6 | [Forza Horizon 6 Revolusound Team Pack](https://www.nexusmods.com/forzahorizon6/mods/56) | Vehicle sound changes covering engines, exhausts, intakes and turbo effects. |
| Forza Horizon 5 | [Forza Horizon 5 Revolusound Team Pack 1.4.4 FINAL](https://www.nexusmods.com/forzahorizon5/mods/86) | The team's later FH5 vehicle audio pack. |
| Forza Horizon 5 | [Forza Horizon 5.5 Zendo Revolusound Pack](https://www.nexusmods.com/forzahorizon5/mods/20) | Earlier FH5 pack; its Nexus page directs visitors to the later team pack above. |

Titles follow the linked Nexus Mods pages. Their downloads, requirements, credits and permissions remain on Nexus Mods.

## Help and participation

[Report a bug or suggest a feature](https://github.com/Zendo-GIT/NV-Laboratory/issues) · [Contributing](CONTRIBUTING.md) · [Security reports](SECURITY.md) · [Changelog](CHANGELOG.md)

For a security issue, read SECURITY.md before posting logs or technical details. Private reporting must be enabled by the maintainer after repository publication.

> **Independent community projects.** NV Laboratory, NV Tools and these utilities are not affiliated with, sponsored by or officially endorsed by NVIDIA Corporation. NVIDIA, GeForce, RTX, DLSS and other product names are trademarks of their respective owners. Names describe compatibility and provenance, not official endorsement.
