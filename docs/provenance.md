🌐 **Language:** English | [Français](provenance.fr.md) · [Home](../README.md)

# Provenance, changes and licensing

This audit describes the candidates prepared on **2026-09-09**. Application
sources remain private; the public inventories contain filenames and hashes,
not source code. See [full component notices](../THIRD_PARTY_NOTICES.md).

## NVIDIA Profile Inspector – NV Tools Fork

Reference: Orbmu2k/nvidiaProfileInspector commit
`592d962cca8827efe8859461a84267755595064a`; candidate executable version 3.0.2.3.
The reference commit and the fork's assembly version are different identifiers;
no upstream release version is inferred from the fork version.

The clean companion's 157 source/resource files were compared with that commit:
2 byte-identical, 134 differing only in line endings or UTF-8 BOM, 11 modified,
10 absent at the compared upstream path. “Added” is relative to that path and
is not by itself proof of original authorship.

[Complete file/hash comparison](provenance/nvpi-source-provenance.json).

| Area | Inherited work | Fork contribution |
| --- | --- | --- |
| Profile editor | Profile model, import/export, application associations and reference data | Integration with Screen and the external tool launcher |
| NVAPI | Orbmu2k's DRS interop | Color/display-related interop, production native-loading restrictions and mock removal |
| Display services | Windows/NVIDIA APIs as external interfaces | DisplayInfoService, DisplayConfigurationService, DisplaySettingsBackend |
| UI | Upstream WPF resources, palettes and icons | Screen dialogs, 15-second confirmation, status/read-back and toolbar layout |
| Launcher | Existing app shell | Protected separately installed RasterPulse lookup and launch |
| Packaging | MIT upstream | Clean standalone companion, separate installer/uninstaller, retained notices |

The public source map includes solution/resource paths for traceability; those
files are not distributed as source. Development tests, mock interfaces and the
old combined NVPI/RasterPulse binary are excluded.

## NVDriverForge

Independent C#/.NET 8/WPF application; the user-facing workflow is inspired in part
by NVCleanstall. No NVCleanstall source/binary was identified in the production
payload. It is not represented as a fork of that proprietary application.

Original project work includes component analysis/selection, protected install
jobs, backups and transaction recovery, NVIDIA catalog downloads, update checks,
localized explanations, optional advanced/NVENC workflows and installer bootstrap.

Inherited/adapted components: four NVPI theme palettes, extended NVAPI DRS interface
reference, and the separately optional MIT NVPI companion. The Custom NV preset's
selection UI and allowlisted transaction integration belong to NVDriverForge;
the preset is not an official NVIDIA recommendation.

7-Zip 26.03, .NET/WPF 8.0.30 and Inno Setup remain unmodified external components
used under their own terms. keylase NVENC data is not embedded; one exact commit
is chosen and checked when the user requests a compatible download. No
redistribution license was established for that upstream data.

## NVMFG Unlock40

Origin: dashdogy/RTX40MFG-Unlock, Michael Robles, MIT, reference commit
`4e776d068f91b4a665425542bb005dd57cc3d891`.
The private native-engine tree contains 48 compared files: 35 formatting-only
differences, 4 modified files and 9 absent at the reference path.
[Complete comparison](provenance/nvmfg-source-provenance.json).

Modified inherited files: `entry_detour.h`, `patcher.cpp`,
`temporal_interval_trace.cpp`, `temporal_interval_trace.h`.
Additional paths include `game_selection.*`, `ngx_bootstrap.*`,
`ngx_capability.h`, `presentation_tracker.h`, `vsync_observer.*`
and a retained upstream license.

Production C++ units: patcher, midpoint_fix, dlssg_provider_policy, entry_detour,
nvidia_mfg_policy, temporal_interval_trace, ngx_bootstrap, game_selection and
vsync_observer; plus entry_detour assembly and MinHook buffer/hook/trampoline/HDE64.
The inherited ReShade frontend, legacy shim resources and unused CMake targets
are not part of this production compilation.

The upstream already contributed patching/provider policy and temporal work.
The central NGX/bootstrap/controller coordination, per-game V-Sync handling,
session diagnostics and Windows application/SDK/backup workflow are adaptations
and additions by 禅堂 Zendo (RevoluSound Team), not a claim to have invented the upstream engine.

The helper adapts NVPI's NvapiDrsWrapper and NativeArrayHelper into a separate
assembly, with project-authored profile logic. The old development mock path is
excluded. Shared family palettes originate from NVPI.

MinHook reference: `8fda4f5481fed5797dc2651cd91e238e9b3928c6`; the inherited
compiled subset has no functional local changes in the comparison.
Streamline integration headers: 2.12; open header license verified at v2.12.0.
NGX header source: NVIDIA/DLSS commit
`a291cc7d2cc642a51566f3dfd5376f635cd1b284`.

Candidate engine SHA-256:
`0E7FC0277C88B22095B622F6A3CB292EC0C14F7A0253D392502257B75E548890`.

Required provider SHA-256 in engine.json:
`C64928FDB7C48A57722EA8EEF2662171EDC323473ADEA66C29A206A23F1A2BED`.
A reported 310.9 provider family is not interchangeable with this exact hash.
No provider DLL or model is included.

**Outstanding licensing point:** the full NVIDIA RTX SDK license, version
March 14, 2024, contains a section 4(d) restriction relevant to bypassing technical
limitations. The audit does not establish permission for this use. Retaining the
MIT engine license, being free of charge, or observing other mods does not resolve
that separate condition. Candidate preparation is not a legal clearance.
The original short header notice is supplemented with the full license;
its Windows-1252 text is also provided as readable UTF-8, with original bytes retained.

## NVRasterPulse

Independent RTSS profile manager developed in the NVPI-derived repository.
The inherited MIT UI resources/palettes and project origin remain credited.
The production app explicitly uses that supplied MIT license.

Project work: precise RTSS profile parsing/writes and fractional encoding,
backups, override removal, reload bridge, prerequisite detection, compact UI,
tray lifecycle, startup controls and localization. RTSS performs actual limiting.

No RTSS source, hook DLL, SDK or installer is bundled. The bridge calls the export
in an existing user-selected RTSS installation. No NVIDIA driver package, native
experimental limiter, Framepacer, MinHook, ReShade or DLSS runtime is in this package.

## Assets, generated data and tools

[Asset credits](../assets/README.md) identify the three existing interface previews.
The fictional values in them are labeled. No game/Nexus asset, personal profile,
private ICC, corporate NVIDIA logo or font file is copied.

Generated game compatibility names inherited in NVMFG are a detection aid, not
test evidence. Generated installer catalogs are credited in
[translator notices](../licenses/INSTALLER-TRANSLATORS.md). Generated build records
with absolute paths remain private.

Private build tools include .NET SDK/MSBuild, Visual Studio C++/MASM, Windows SDK,
PowerShell, Inno Setup and Python audit scripts. Their compilers, headers, test
runners and debug assets are not distributed. Static release CRT remains under
Microsoft's applicable toolchain terms.

## Scope of verification

The local audit inventoried all files in the three development roots while
excluding Git object databases and linked directory targets. Active source/docs
were scanned; historical builds were inventoried and excluded. Selected ZIPs and
current payloads were scanned and hashed; the .NET bundles were decompressed for
additional inspection. That initial audit ran no product, installer, game, RTSS
process or driver.

The later NVPI setup revision 2 fixes standalone language selection using the
shared Inno controls and bootstrap. Light/dark private fixtures verified mouse
and keyboard navigation and all 34 explicit language codes. The actual setup
selector was opened on a never-displayed private desktop and cancelled before
installation. Its seven application files and portable ZIP are unchanged.
NVDriverForge 0.1.2 retains its earlier embedded companion, which receives `/LANG`.

No functional application code was changed. Earlier application build/unit/UI
tests remain dated historical evidence. This is not full reverse engineering of
every third-party binary or a guarantee against every possible secret pattern.
