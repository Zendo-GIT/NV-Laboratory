<!-- nv-language-navigation:start -->
🌐 English | [Français](support.fr.md) · [NV Laboratory](../README.md)

<details>
<summary>🌐 Language · 34</summary>

[العربية](languages/ar/docs/support.md) · [বাংলা](languages/bn/docs/support.md) · [简体中文](languages/zh/docs/support.md) · [Čeština](languages/cs/docs/support.md) · [Dansk](languages/da/docs/support.md) · [Nederlands](languages/nl/docs/support.md) · **English** · [Filipino](languages/fil/docs/support.md) · [Suomi](languages/fi/docs/support.md) · [Français](support.fr.md) · [Deutsch](languages/de/docs/support.md) · [Ελληνικά](languages/el/docs/support.md) · [हिन्दी](languages/hi/docs/support.md) · [Magyar](languages/hu/docs/support.md) · [Bahasa Indonesia](languages/id/docs/support.md) · [Italiano](languages/it/docs/support.md) · [日本語](languages/ja/docs/support.md) · [한국어](languages/ko/docs/support.md) · [मराठी](languages/mr/docs/support.md) · [فارسی](languages/fa/docs/support.md) · [Polski](languages/pl/docs/support.md) · [Português](languages/pt/docs/support.md) · [ਪੰਜਾਬੀ](languages/pa/docs/support.md) · [Română](languages/ro/docs/support.md) · [Русский](languages/ru/docs/support.md) · [Español](languages/es/docs/support.md) · [Kiswahili](languages/sw/docs/support.md) · [Svenska](languages/sv/docs/support.md) · [தமிழ்](languages/ta/docs/support.md) · [ไทย](languages/th/docs/support.md) · [Türkçe](languages/tr/docs/support.md) · [Українська](languages/uk/docs/support.md) · [اردو](languages/ur/docs/support.md) · [Tiếng Việt](languages/vi/docs/support.md)

[Translation policy](languages/README.md)

</details>
<!-- nv-language-navigation:end -->

# Compatibility and troubleshooting

These are the prepared candidates, not a certification matrix for all Windows,
GPU, driver and game combinations.

| Tool | Windows / runtime | Hardware / external dependency | Operations needing care |
| --- | --- | --- | --- |
| NVPI fork 3.0.2.3 | Windows 10/11 x64, .NET Framework 4.8 | Compatible NVIDIA driver/display | Profile writes and display previews |
| NVDriverForge 0.1.4 | Windows 10 build 19041+ / 11 x64; .NET/WPF included | Compatible NVIDIA driver package | Elevated installation, advanced settings, optional NVENC |
| NVMFG Unlock40 0.2.3 | Windows 10/11 x64; .NET/WPF included, Framework 4.8 helpers | RTX 40, eligible DLSS FG game and pinned provider | Native in-game patching, global profile journal, SDK game updates |
| NVRasterPulse 0.2 | Windows 10/11 x64, .NET Framework 4.8 | RTSS installed; running for caps | RTSS per-executable profile changes |

No ARM64 package is prepared. Display/API availability and old Windows versions
can limit individual features. No universal minimum NVIDIA or RTSS version is
invented. The exact NVMFG provider hash is in [provenance](provenance.md).

## Before reporting a bug

Identify the exact executable/version you opened. A previous installed copy is
not necessarily the version of a newly downloaded ZIP. Record the reproduction
steps, expected result and actual result. For rendering/limiting issues, include
game version, display refresh, FG/V-Sync/VRR state and any other limiter or overlay.

Use the [bug form](https://github.com/Zendo-GIT/NV-Laboratory/issues/new?template=bug-report.yml).
Never attach an entire private development folder, driver archive, model, game
DLL, registry dump or unreviewed log collection.

| Problem | First checks |
| --- | --- |
| Wrong application version | Confirm EXE identity and Release hash; close the older copy before replacement. |
| Runtime/startup error | Install required Framework 4.8 or retain all supplied portable subfolders. |
| UAC cancelled | Retry only the intended operation; cancellation is not successful installation. |
| Hash/signature mismatch | Stop using that candidate and obtain the expected official bytes. |
| NVPI color/mode rejected | Revert and use a combination supported by the actual display/driver. |
| NVDF backup or recovery failure | Preserve protected job and RECOVERY.txt; don't erase the journal or force conflicting writes. |
| NVMFG pending settings | Resolve recovery with games closed, preserving changes from other tools. |
| RP cap has no effect | Run RTSS, identify the real game EXE, inspect hook state and competing limits. |
| RP cap persists after removal | Inspect RTSS Global; removal changes local limiter overrides only. |

NVDriverForge offers a previewable local JSON report; NVMFG offers a diagnostic in About. Prefer these filtered reports to a complete log archive and inspect them before sharing. A restoration blockage reported on NVMFG 0.1.1 still has no established cause; preserve its journal and record any available error code. NVRasterPulse 0.2 offers configuration diagnostics in its actions menu, without measuring FPS.

## Logs and privacy

| Tool | Local data to review, not upload wholesale |
| --- | --- |
| NVDF | `%LOCALAPPDATA%\NVDriverForge`; protected jobs `%PROGRAMDATA%\NVDriverForge\Jobs` |
| NVMFG | `%LOCALAPPDATA%\RtxMfg`; backups `%LOCALAPPDATA%\NvidiaStreamlineMaintenance\Backups`; `Sessions` beside the EXE |
| RP | `%LOCALAPPDATA%\NVRasterPulse`; `Backups\RTSS` below it |
| NVPI | Your chosen exports and the displayed error; no invented universal log path |

Remove account names, home directories, game-library paths, device identifiers,
tokens and unrelated windows from the text/images you share. Keep the originals
privately for recovery. Public Issues are visible to everyone.

For a vulnerability, dangerous privileged behavior or unintended destructive
operation, follow [SECURITY.md](../SECURITY.md) instead of posting details publicly.

## What has been verified

For hub preparation, static payload/ZIP/hash/metadata scans and documentation
checks were run. Existing private application build/unit/UI tests are historical,
dated evidence. No driver install, display change, live RTSS operation or game
benchmark was performed as part of this preparation.

“Detected”, “written”, “reloaded”, “capability available” and “measured in game”
are different results. Report which one you observed.
