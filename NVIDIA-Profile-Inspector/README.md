<!-- nv-language-navigation:start -->
🌐 English | [Français](README.fr.md) · [NV Laboratory](../README.md)

<details>
<summary>🌐 Language · 34</summary>

[العربية](../docs/languages/ar/NVIDIA-Profile-Inspector/README.md) · [বাংলা](../docs/languages/bn/NVIDIA-Profile-Inspector/README.md) · [简体中文](../docs/languages/zh/NVIDIA-Profile-Inspector/README.md) · [Čeština](../docs/languages/cs/NVIDIA-Profile-Inspector/README.md) · [Dansk](../docs/languages/da/NVIDIA-Profile-Inspector/README.md) · [Nederlands](../docs/languages/nl/NVIDIA-Profile-Inspector/README.md) · **English** · [Filipino](../docs/languages/fil/NVIDIA-Profile-Inspector/README.md) · [Suomi](../docs/languages/fi/NVIDIA-Profile-Inspector/README.md) · [Français](README.fr.md) · [Deutsch](../docs/languages/de/NVIDIA-Profile-Inspector/README.md) · [Ελληνικά](../docs/languages/el/NVIDIA-Profile-Inspector/README.md) · [हिन्दी](../docs/languages/hi/NVIDIA-Profile-Inspector/README.md) · [Magyar](../docs/languages/hu/NVIDIA-Profile-Inspector/README.md) · [Bahasa Indonesia](../docs/languages/id/NVIDIA-Profile-Inspector/README.md) · [Italiano](../docs/languages/it/NVIDIA-Profile-Inspector/README.md) · [日本語](../docs/languages/ja/NVIDIA-Profile-Inspector/README.md) · [한국어](../docs/languages/ko/NVIDIA-Profile-Inspector/README.md) · [मराठी](../docs/languages/mr/NVIDIA-Profile-Inspector/README.md) · [فارسی](../docs/languages/fa/NVIDIA-Profile-Inspector/README.md) · [Polski](../docs/languages/pl/NVIDIA-Profile-Inspector/README.md) · [Português](../docs/languages/pt/NVIDIA-Profile-Inspector/README.md) · [ਪੰਜਾਬੀ](../docs/languages/pa/NVIDIA-Profile-Inspector/README.md) · [Română](../docs/languages/ro/NVIDIA-Profile-Inspector/README.md) · [Русский](../docs/languages/ru/NVIDIA-Profile-Inspector/README.md) · [Español](../docs/languages/es/NVIDIA-Profile-Inspector/README.md) · [Kiswahili](../docs/languages/sw/NVIDIA-Profile-Inspector/README.md) · [Svenska](../docs/languages/sv/NVIDIA-Profile-Inspector/README.md) · [தமிழ்](../docs/languages/ta/NVIDIA-Profile-Inspector/README.md) · [ไทย](../docs/languages/th/NVIDIA-Profile-Inspector/README.md) · [Türkçe](../docs/languages/tr/NVIDIA-Profile-Inspector/README.md) · [Українська](../docs/languages/uk/NVIDIA-Profile-Inspector/README.md) · [اردو](../docs/languages/ur/NVIDIA-Profile-Inspector/README.md) · [Tiếng Việt](../docs/languages/vi/NVIDIA-Profile-Inspector/README.md)

[Translation policy](../docs/languages/README.md)

</details>
<!-- nv-language-navigation:end -->

# NVIDIA Profile Inspector – NV Tools Fork

**An independent fork of [NVIDIA Profile Inspector by Orbmu2k](https://github.com/Orbmu2k/nvidiaProfileInspector), with added display controls.** Former project name: **NVPI Custom**.

[Download & release status](../docs/downloads.md#nvidia-profile-inspector) · [Installation](#installation) · [Upstream and changes](#upstream-and-changes) · [License](LICENSE)

## Overview

The application edits NVIDIA driver profiles, including per-application settings.
This fork also adds a **Screen** editor for the active Windows display: resolution,
refresh rate, output color settings, HDR and installed ICC/WCS profile associations.

It exists to bring related display controls into the profile editor and to make
preview, confirmation and restoration results clearer. It does not establish
new hardware capabilities.

The first candidate is **3.0.2.3**, using the cleaned standalone companion build
from September 9, 2026. Its existing executable remains
`nvidiaProfileInspector.exe`; the installer and some internal labels still say
`NVPI Custom NV`. The public title above identifies the fork without changing
installation identity or pretending it is Orbmu2k's official release.

## Features

- Existing upstream profile browsing, application associations, setting edits and profile import/export.
- **Screen** dialog for the display, mode, Hz, RGB/YCbCr, color depth, range and colorimetry.
- Windows HDR control and installed ICC/WCS association selection.
- A 15-second display preview with **Keep** / **Revert** and timeout restoration.
- Read-back of mode/HDR changes and reported restoration failures.
- Separate reporting of HDR, SDR with ACM/WCG and signal color depth.
- A NVRasterPulse launcher for an eligible separately installed copy.

## Compatibility

| Requirement | Details |
| --- | --- |
| System | Windows 10/11 x64 with a compatible NVIDIA driver |
| Runtime | [.NET Framework 4.8](https://dotnet.microsoft.com/en-us/download/dotnet-framework/net48), supplied by Windows or installed separately |
| Permissions | The editor requests administrator access when opened |
| Displays | Actual modes and color combinations depend on GPU, driver, display, cable and Windows APIs |
| Optional tools | NVRasterPulse for RTSS limit management; neither it nor RTSS is needed for the Screen editor |
| Languages | Setup: 34-language selector. The editor retains its existing language support. |

There is no verified universal driver minimum or support matrix for every GPU.
The dialog's available bpc choices are requests, not certified combinations.
Modern HDR controls and the older Windows fallback have different capabilities.

## Installation

1. Open the [download page](../docs/downloads.md#nvidia-profile-inspector) and check publication status.
2. Download the Setup or portable asset and compare its SHA-256 with the Release manifest.
3. For Setup, run `NVPI-CustomNV-3.0.2.3-Setup-r2.exe`, select a language and follow the installer. It creates its own shortcut and uninstaller.
4. For portable, extract the complete ZIP to a new writable folder. Keep `Reference.xml`, the EXE configuration and all notices beside the executable.
5. Launch `nvidiaProfileInspector.exe`.

Installing the editor alone does not apply a profile or install a GPU driver.
The companion installs separately, does not take over `.nip` associations and
does not enable startup at sign-in. Existing binaries are unsigned.

## Usage

**Installer revision 2** adds the same native 34-language selector as the other
tools, with mouse/keyboard navigation, light/dark appearance and cancellation.
The choice applies to setup; it does not translate the NVPI editor. An explicit
`/LANG=fr` argument or silent mode bypasses selection for callers that already
provide a language.

**Driver profiles:** select a profile, export a backup, then edit only the intended
settings and apply them. Application associations determine which game receives
a profile. A stored value is not proof that every driver or game uses it.

**Display controls:** open **Screen**, choose the display and requested values,
then start the preview. Check the image before choosing **Keep** within 15 seconds.
Use **Revert**, close the confirmation or let it expire to request restoration.
Read any failure message: a successful API call alone is not proof of restoration.

An ICC selection changes an installed profile association; it does not generate,
calibrate or redistribute an ICC file. HDR, ACM/WCG, RGB/YCbCr and bpc describe
different aspects of the pipeline. No new independent ACM switch is provided.

**NVRasterPulse:** the toolbar button accepts a separately registered system-wide
installation below Program Files with protected ownership and permissions. A
portable copy or a user-writable/linked path may be refused by this elevated
launcher. In that case open NVRasterPulse using its own shortcut.
[Install RTSS separately](https://www.guru3d.com/download/rtss-rivatuner-statistics-server-download/) to use NVRasterPulse.

## Screenshots

![NVPI setup revision 2 language selector](../assets/screenshots/nvpi-setup-r2-language.png)

Actual setup selector in French, captured during an isolated test and then cancelled.
This shows the installer; the editor retains its interface and Screen dialog.

## Update and uninstall

Close the editor before updating. Keep exported profiles and download the new
fork Release; install over the same companion identity or extract portable files
into a fresh folder. Do not mix an old `Reference.xml` with a new executable.
The bundled upstream update-check suppression belongs to this fork.

For an installed copy, use Windows **Installed apps** and its uninstaller.
For portable, close it and remove its extracted folder when your exports are safe.
Removing the editor does **not** undo driver profile edits, display preferences,
NVRasterPulse or RTSS. Restore desired settings before removal.

## Known limitations

- The 15-second confirmation is not a watchdog for every driver crash, power loss or forced shutdown.
- Some color/depth/refresh combinations return `NVAPI_NOT_SUPPORTED`.
- Software read-back does not measure panel bit depth, color accuracy or latency.
- Screen settings affect the current Windows display; this dialog does not create per-game display presets.
- No performance, anti-cheat or universal HDR compatibility guarantee.

## Troubleshooting

| Symptom | Action |
| --- | --- |
| Runtime error at launch | Check Windows updates and .NET Framework 4.8; use the complete package. |
| Requested display mode rejected | Revert and test a mode offered by Windows/NVIDIA for that display. Read the exact error and avoid repeated blind changes. |
| HDR or color returns to the old state | Check whether another operation failed and triggered restoration; distinguish HDR from ACM. |
| NVRasterPulse button refuses a path | Launch its own shortcut; this button requires a protected system-wide installation. |
| A change remains after uninstall | Restore the exported NVIDIA profile or the intended Windows display settings; uninstall is not a settings rollback. |

See [shared support guidance](../docs/support.md) before sending logs.

## FAQ

**Is this official NVIDIA software or Orbmu2k's official build?** No. It is an
independent fork; the upstream author and MIT license remain credited.

**Does NVDriverForge require this editor?** No. NVDriverForge's optional Custom NV
preset uses its own integration. Installing the editor is a separate choice.

**Is RTSS mandatory for this fork?** No. RTSS is mandatory for NVRasterPulse's
FPS limiter, not for profile or Screen editing.

**Where is the source?** The modified application source is maintained privately.
The MIT notice and upstream repository are provided; MIT does not require
publishing modified source.

## Upstream and changes

Upstream: [Orbmu2k/nvidiaProfileInspector](https://github.com/Orbmu2k/nvidiaProfileInspector),
reference commit `592d962cca8827efe8859461a84267755595064a`.
[Original downloads](https://github.com/Orbmu2k/nvidiaProfileInspector/releases).

Inherited: profile editor, NVAPI interop, reference data, UI resources and themes.
禅堂 Zendo (RevoluSound Team) added or adapted display services, HDR/ICC transactions,
15-second confirmation/read-back, toolbar layout and RasterPulse launch behavior.
The cleaned companion excludes development mocks/test entry points, uses a
protected external launcher and provides a separate installer. The old combined
NVPI/RasterPulse development package is not the candidate in this hub.

[Detailed file provenance](../docs/provenance.md) · [Original fork notice](LICENSES/ORIGINAL-FORK-NOTICE.txt)

## Credits and license

Copyright (c) 2016 Orbmu2k. The supplied [MIT license](LICENSE) is retained.
Adaptations and packaging: 禅堂 Zendo (RevoluSound Team).
The installer uses Inno Setup; Windows and .NET Framework remain external.
[Full applicable notices](LICENSES/README.md).

Independent of, not sponsored by, and not officially endorsed by NVIDIA Corporation.
Trademarks remain with their respective owners.
