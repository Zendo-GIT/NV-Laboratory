🌐 **Language:** English | [Français](installation.fr.md) · [Home](../README.md)

# Installation guide

Start with [Downloads](downloads.md), which records publication status and exact
asset names. These are separate tools: install only the ones you need.

> **For NVRasterPulse, install [RTSS from Guru3D](https://www.guru3d.com/download/rtss-rivatuner-statistics-server-download/) before opening the profile manager.**
> RTSS must run to apply limits; it is not included in NV Tools.

| Tool | Installed edition | Portable edition | Main prerequisite |
| --- | --- | --- | --- |
| NVIDIA Profile Inspector – NV Tools Fork | NVPI-CustomNV-3.0.2.3-Setup-r2.exe | Extract complete NVPI ZIP | NVIDIA driver and .NET Framework 4.8 |
| NVDriverForge | NVDriverForge-Setup.exe | NVDriverForge.exe, runtime included | Compatible original NVIDIA driver package for installation operations |
| NVMFG Unlock40 | NVMFGUnlock40-0.1.1-Setup-x64.exe | Extract complete NVMFG ZIP, retain subfolders | RTX 40, existing DLSS FG, exact provider and .NET Framework 4.8 helpers |
| NVRasterPulse | NVRasterPulse-0.1-win-x64-Setup.exe | Extract complete RP ZIP | RTSS and .NET Framework 4.8 |

## Download, verify, install

1. On the chosen published Release, download its named application asset, notices ZIP and SHA256SUMS.txt.
2. Use the [SHA-256 example](downloads.md#sha-256), with the actual downloaded filename.
3. For Setup, follow the normal installer. For portable ZIP, extract everything to a new local writable folder; do not run from inside the ZIP.
4. Open the application's own EXE. Keep the accompanying license/configuration/data files.
5. Read that tool's usage instructions before enabling settings or system operations.

Current binaries are unsigned. A matching hash confirms the expected bytes;
it is not a security or compatibility certificate. Do not disable Windows
security protections just to suppress a warning.

Installing NVDF or its optional NVPI companion is separate from installing a GPU
driver. The NVPI companion keeps its existing internal installation name. Its
elevated RasterPulse button requires a protected system-wide installation;
other RP copies can be opened through their own shortcuts.

NVMFG is experimental and has the [documented NVIDIA SDK licensing reserve](provenance.md).
No NVIDIA driver, NGX provider/model or game Streamline runtime is included.
Selected SDK downloads and game updates are explicit separate operations.

## Language and updates

Use the README's English/Français selector for documentation. NVDF, NVMFG and RP
have their own 34-language UI setting; NVPI keeps its existing language support.
Some installer technical strings fall back to English.

Keep a tool's installation identity when updating. Close it first and preserve
backups. For NVMFG, close affected games and resolve pending profile recovery.
For portable updates, use a fresh folder rather than combining releases.

## Removing a tool

Uninstalling an application is not automatically undoing its settings.

- **NVPI:** restore intended profiles/display settings before removal if needed.
- **NVDF:** use recovery first if you want to restore advanced/NVENC changes. Uninstall leaves the graphics driver, settings and backups.
- **NVMFG:** close games, disable/quit the controller, resolve NVIDIA recovery and restore desired game SDK backups before removal.
- **RP:** remove the intended limiter overrides first. Uninstall does not erase saved RTSS caps or remove RTSS.

See each [project guide](../README.md#projects) for exact data locations and
limitations, or [support](support.md) if a recovery step fails.
