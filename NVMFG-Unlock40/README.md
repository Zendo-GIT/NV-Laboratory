<!-- nv-language-navigation:start -->
🌐 English | [Français](README.fr.md) · [NV Laboratory](../README.md)

<details>
<summary>🌐 Language · 34</summary>

[العربية](../docs/languages/ar/NVMFG-Unlock40/README.md) · [বাংলা](../docs/languages/bn/NVMFG-Unlock40/README.md) · [简体中文](../docs/languages/zh/NVMFG-Unlock40/README.md) · [Čeština](../docs/languages/cs/NVMFG-Unlock40/README.md) · [Dansk](../docs/languages/da/NVMFG-Unlock40/README.md) · [Nederlands](../docs/languages/nl/NVMFG-Unlock40/README.md) · **English** · [Filipino](../docs/languages/fil/NVMFG-Unlock40/README.md) · [Suomi](../docs/languages/fi/NVMFG-Unlock40/README.md) · [Français](README.fr.md) · [Deutsch](../docs/languages/de/NVMFG-Unlock40/README.md) · [Ελληνικά](../docs/languages/el/NVMFG-Unlock40/README.md) · [हिन्दी](../docs/languages/hi/NVMFG-Unlock40/README.md) · [Magyar](../docs/languages/hu/NVMFG-Unlock40/README.md) · [Bahasa Indonesia](../docs/languages/id/NVMFG-Unlock40/README.md) · [Italiano](../docs/languages/it/NVMFG-Unlock40/README.md) · [日本語](../docs/languages/ja/NVMFG-Unlock40/README.md) · [한국어](../docs/languages/ko/NVMFG-Unlock40/README.md) · [मराठी](../docs/languages/mr/NVMFG-Unlock40/README.md) · [فارسی](../docs/languages/fa/NVMFG-Unlock40/README.md) · [Polski](../docs/languages/pl/NVMFG-Unlock40/README.md) · [Português](../docs/languages/pt/NVMFG-Unlock40/README.md) · [ਪੰਜਾਬੀ](../docs/languages/pa/NVMFG-Unlock40/README.md) · [Română](../docs/languages/ro/NVMFG-Unlock40/README.md) · [Русский](../docs/languages/ru/NVMFG-Unlock40/README.md) · [Español](../docs/languages/es/NVMFG-Unlock40/README.md) · [Kiswahili](../docs/languages/sw/NVMFG-Unlock40/README.md) · [Svenska](../docs/languages/sv/NVMFG-Unlock40/README.md) · [தமிழ்](../docs/languages/ta/NVMFG-Unlock40/README.md) · [ไทย](../docs/languages/th/NVMFG-Unlock40/README.md) · [Türkçe](../docs/languages/tr/NVMFG-Unlock40/README.md) · [Українська](../docs/languages/uk/NVMFG-Unlock40/README.md) · [اردو](../docs/languages/ur/NVMFG-Unlock40/README.md) · [Tiếng Việt](../docs/languages/vi/NVMFG-Unlock40/README.md)

[Translation policy](../docs/languages/README.md)

</details>
<!-- nv-language-navigation:end -->

# NVMFG Unlock40

**Experimental NVIDIA Multi Frame Generation for GeForce RTX 40, with a central controller and per-game choices.**

[Download 0.2.3 & status](../docs/downloads.md#nvmfg-unlock40) · [Installation](#installation) · [Upstream](#upstream-and-modifications) · [Licenses](LICENSES/README.md)

## Overview and purpose

NVMFG Unlock40 is an independently developed application by
禅堂 Zendo (RevoluSound Team). It combines a Windows controller, a native layer,
a profile helper and game/Streamline SDK management. It targets games that already
integrate NVIDIA DLSS Frame Generation and compatible NVIDIA runtimes.

[RTX40MFG-Unlock](https://github.com/dashdogy/RTX40MFG-Unlock) was consulted to
compare and refine the work. The current native layer contains shared and adapted
components, credited individually below. This reference does not make the entire
NVMFG application a fork of that project.

It exists to coordinate experimental MFG behavior centrally, remember game-specific
choices, and keep runtime updates and backups visible. It does not add DLSS Frame
Generation to every game or convert an arbitrary FSR implementation.

The current package is **0.2.3**. It adds a persistent game library, activity and
capability information, local diagnostics and corrected selection/progress behavior.
[Downloads](../docs/downloads.md#nvmfg-unlock40) identifies the exact files and hashes.

## Features

- Central enable/disable control and optional Windows tray startup.
- Per-game selection between Dynamic MFG, the game's setting and supported fixed multipliers.
- Separate remembered choices for observed V-Sync on/off states.
- Dynamic uses NVIDIA's mode; it is suspended when V-Sync is off, with a separate in-game/fixed choice.
- Game-menu guidance and persistent exclusions; games without DLSS FG stay in control.
- Game discovery, parent-folder selection, search, grouping and removal without deleting game files.
- Streamline SDK download/import, verified local cache, explicit selection, per-game backup and restoration.
- Native provider verification, per-session diagnostics, global profile journal and conflict-aware recovery.
- 34 interface languages and four themes.

Turning FG off in the game keeps it off. Fixed choices from 2x through 6x depend
on the game/menu/runtime; they are not a promise that every combination works.
The controller observes V-Sync and does not set V-Sync or VRR for the user.

## Compatibility

| Requirement | Details |
| --- | --- |
| System | Windows 10/11 x64 |
| GPU | GeForce RTX 40 target; no universal GPU compatibility claim |
| Game | Existing NVIDIA DLSS Frame Generation integration and supported runtime; no anti-cheat compatibility certification |
| Provider | Candidate is pinned to the provider SHA-256 documented in [provenance](../docs/provenance.md); unknown hashes are refused |
| Runtime | Bundled .NET 8/WPF 8.0.30 for app/agent; .NET Framework 4.8 for profile helpers |
| Permissions | Administrator access for the controller/profile operations |
| Network | Required for selected official SDK downloads; imported compatible SDKs can be cached locally |
| External binaries | NVIDIA driver, NGX provider/models and Streamline game runtimes are not bundled |

A version label alone is insufficient: driver, provider hash, game integration
and actual loaded modules matter. Protected or incompatible processes can refuse
attachment. The application is not designed to evade anti-cheat protections.

## Installation

1. Read the [candidate status and licensing note](../docs/downloads.md#nvmfg-unlock40).
2. Download `NVMFGUnlock40-0.2.3-Setup-x64.exe` or `NVMFGUnlock40-0.2.3-Portable-x64.zip` when its Release is available.
3. Check SHA-256 and keep the accompanying notices. Install .NET Framework 4.8 if Windows does not already provide it.
4. Run Setup, or extract the **entire** portable ZIP to a writable local folder.
5. Launch `NVMFGUnlock40.exe`; keep `agent`, `driver`, `engine` and `Licenses` in the supplied layout.

The folder named `driver` contains user-space helpers, not a kernel driver.
Do not copy only the main EXE or replace the provider hash to force compatibility.
The current EXEs are unsigned.

## Usage

1. Start with the controller disabled. Add a game or a parent folder and choose the actual installations.
2. Review each game's MFG settings. Answer what its menu offers; the answer is stored per game.
3. Choose Dynamic or the in-game setting globally, then adjust eligible per-game choices as needed.
4. Enable the controller only when you intend to use it. It can temporarily change six global NVIDIA profile settings, with a recovery journal.
5. Launch an eligible game and enable its own DLSS Frame Generation. Follow any request for the V-Sync-off choice.
6. Use exclusions for games you do not want managed. Removing a game records an exclusion and preserves its files/backups.
7. Use the application's full quit/disable and recovery flow when finished.

Closing the main window can leave the controller in the tray. A DLL already
loaded into a game remains there until the game exits; disabling the controller
is not an unload guarantee. Close affected games before maintenance or updates.

**Streamline SDKs:** on the NVIDIA SDK page, download an official version or import
a compatible local SDK. Import stores a verified copy; **Use this version** selects
it, and **Uninstall** removes that cached copy. Missing Streamline DLLs can be
supplemented from an official NVIDIA SDK, with the source shown. This does not
download/replace an NGX model. Close the game, select the intended game update,
and retain its original backup. To revert game files, use its backup restoration,
not the cache's Uninstall button.

## Library, diagnostics and updates

**Persistent library:** select several game folders, including different drives, before starting one scan. Progress is visible and cancellation is available. After the first scan, a local cache restores the library on launch without walking every game folder. Refresh to find changes or add another folder. Maintenance operations still revalidate the affected files; backup monitoring remains active. The cache is stored at `%LOCALAPPDATA%\RtxMfg\library-cache.json`.

**Selection:** Ctrl+A selects all and Ctrl+D clears the active Games or Backups tab. No game is automatically selected. Activity updates and refreshes no longer create ghost selections or inconsistent counts.

**Activity and compatibility:** per-game MFG information comes from NGX observations without a new overlay. It is not a physical count of displayed frames. Dynamic-with-V-Sync support comes from runtime capabilities; unknown capability is not inferred from a version number. The application changes neither V-Sync nor VRR. With V-Sync off, Dynamic remains suspended; fixed or game-controlled choices are separate.

**Next launch:** the temporary exclusion skips patching at the next game launch and restores normal management after it exits. It cannot remove a DLL already loaded in a game: close and restart that game. Wallpaper Engine is recognized as a desktop application; this correction preserves the protection for actual ignored games.

**Preferences and support:** preference import/export requires manual reassociation of game folders. The local diagnostic in About filters private information and reports available NVAPI error codes or conflict categories. Review it before sharing; nothing is uploaded automatically.

**Application updates:** an optional check displays release notes and offers the official Setup. The explicit download is checked against GitHub size and SHA-256 metadata; you initiate installation yourself. Version 0.2.3 also clears completed progress messages while preserving meaningful errors and results. These additions include the changes since public version 0.1.1.

## Screenshots

![NVMFG SDK-list preview](../assets/screenshots/nvmfg-0.1.1-sdk-preview.png)

Existing English 0.1.1 interface render with an example SDK inventory.
It is not a current version list or evidence of a running game.
[Image provenance](../assets/README.md).

## Update and uninstall

Close affected games. Disable/quit NVMFG and resolve any pending NVIDIA settings
recovery before updating. Install the next Setup with the existing identity,
or extract the new portable into a fresh folder; retain state/backups.

Before uninstalling, restore desired game SDK backups and NVIDIA settings through
the application, then close games and quit the controller. Use Windows
**Installed apps** for Setup, or remove the closed portable folder after preserving
needed files. Do not manually delete an active recovery journal to unblock Setup.

Local game-runtime backups use
`%LOCALAPPDATA%\NvidiaStreamlineMaintenance\Backups`. MFG settings/SDK data use
`%LOCALAPPDATA%\RtxMfg`; session output is under `Sessions` beside the application.
These files can contain game paths. Do not post them unredacted.

## Known limitations

- A reported 0.1.1 activation/restoration/uninstall blockage remains unreproduced and its cause is unknown. This release does not claim to fix it. After a failure, preserve the recovery journal and inspect the local diagnostic; do not force deletion of recovery data.
- Experimental native patches can cause crashes or visual artifacts; an unresolved Bodycam crash is recorded in development history.
- Controlled renderer tests are not certification for every game, driver or anti-cheat.
- Generated frames do not create new input samples; no measured latency or performance gain is promised by this hub.
- Multiple frame-generation tools/overlays may conflict. The application reports observed modules without proving every coexistence scenario.
- The compatibility manifest is a detection aid, not a list of fully tested games.
- Full NVIDIA SDK terms and the unresolved technical-limitation restriction remain documented in [provenance](../docs/provenance.md).

## Troubleshooting

| Symptom | Action |
| --- | --- |
| Provider not supported | Keep the original verified files. Report driver/provider versions and the error; do not bypass the hash check. |
| No DLSS FG in the game | Select that answer and leave the game in control; this tool cannot manufacture that integration. |
| Game crashes/artifacts | Quit the game, disable NVMFG, use the game's original runtime backup if it was changed, and report reproducible details. |
| SDK list or download unavailable | Refresh and check the official source; a cached/imported version must still pass validation. |
| Pending NVIDIA recovery blocks exit/update | Use recovery and preserve the journal; conflicts must not be overwritten blindly. |
| A removed game is not rediscovered | Its exclusion is persistent. Add it explicitly when you want it managed again. |

[Shared support guidance](../docs/support.md) explains what to include in a report.

## FAQ

**Does it include NVIDIA DLLs or models?** No driver, NGX provider/model or
Streamline runtime is included. Explicit SDK downloads come from NVIDIA.

**Does Dynamic work with V-Sync off?** It is suspended in that state. Choose the
in-game setting or an eligible fixed multiplier for that game's separate state.

**Is this a ReShade/OptiScaler/FSR package?** No. Those are not compiled or shipped
as part of this production package.

**Are the modified sources public?** No. Compiled packages and required credits/
licenses are provided. This does not remove rights or restrictions of third parties.

## Upstream and modifications

Comparison reference and shared native components: **RTX40MFG-Unlock by
Michael Robles / dashdogy**, reference commit
`4e776d068f91b4a665425542bb005dd57cc3d891`, MIT.
[Repository](https://github.com/dashdogy/RTX40MFG-Unlock) · [Original downloads](https://github.com/dashdogy/RTX40MFG-Unlock/releases).

The source comparison identifies shared patching, provider/policy handling,
temporal corrections and MinHook-based detour components. Their MIT and BSD notices
are retained. The complete comparison also includes files outside the production target.

The desktop application, controller and SDK-management workflow are developed by
禅堂 Zendo (RevoluSound Team). Project work includes central loading, NGX bootstrap
integration, verified provider selection, game/V-Sync coordination and session
diagnostics. The provenance guide separates that work from the shared components;
a file comparison alone does not establish when either author had the idea.

The profile helper adapts the MIT NVAPI wrapper from Orbmu2k's Profile Inspector.
[Detailed provenance and component scope](../docs/provenance.md).

## Credits and license

Michael Robles; Orbmu2k; Tsuda Kageyu and HDE contributors; NVIDIA Corporation;
Microsoft and contributors; Inno Setup authors and translators. Application
development, integrations and packaging: 禅堂 Zendo (RevoluSound Team).

The [existing compiled-package sharing permission](LICENSE) and all
[component licenses](LICENSES/README.md) are preserved. MIT permissions for upstream
code are distinct from NVIDIA SDK terms. No blanket license replaces them.

Independent of, not sponsored by, and not officially endorsed by NVIDIA Corporation.
All referenced trademarks remain their owners' property.
