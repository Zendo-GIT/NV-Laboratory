🌐 **Language:** English | [Français](support.fr.md) · [Home](../README.md)

# Compatibility and troubleshooting

These are the prepared candidates, not a certification matrix for all Windows,
GPU, driver and game combinations.

| Tool | Windows / runtime | Hardware / external dependency | Operations needing care |
| --- | --- | --- | --- |
| NVPI fork 3.0.2.3 | Windows 10/11 x64, .NET Framework 4.8 | Compatible NVIDIA driver/display | Profile writes and display previews |
| NVDriverForge 0.1.2 | Windows 10 build 19041+ / 11 x64; .NET/WPF included | Compatible NVIDIA driver package | Elevated installation, advanced settings, optional NVENC |
| NVMFG Unlock40 0.1.1 | Windows 10/11 x64; .NET/WPF included, Framework 4.8 helpers | RTX 40, eligible DLSS FG game and pinned provider | Native in-game patching, global profile journal, SDK game updates |
| NVRasterPulse 0.1 | Windows 10/11 x64, .NET Framework 4.8 | RTSS installed; running for caps | RTSS per-executable profile changes |

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
