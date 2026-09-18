<!-- nv-language-navigation:start -->
🌐 English | [Français](README.fr.md) · [NV Laboratory](../README.md)

<details>
<summary>🌐 Language · 34</summary>

[العربية](../docs/languages/ar/NVDriverForge/README.md) · [বাংলা](../docs/languages/bn/NVDriverForge/README.md) · [简体中文](../docs/languages/zh/NVDriverForge/README.md) · [Čeština](../docs/languages/cs/NVDriverForge/README.md) · [Dansk](../docs/languages/da/NVDriverForge/README.md) · [Nederlands](../docs/languages/nl/NVDriverForge/README.md) · **English** · [Filipino](../docs/languages/fil/NVDriverForge/README.md) · [Suomi](../docs/languages/fi/NVDriverForge/README.md) · [Français](README.fr.md) · [Deutsch](../docs/languages/de/NVDriverForge/README.md) · [Ελληνικά](../docs/languages/el/NVDriverForge/README.md) · [हिन्दी](../docs/languages/hi/NVDriverForge/README.md) · [Magyar](../docs/languages/hu/NVDriverForge/README.md) · [Bahasa Indonesia](../docs/languages/id/NVDriverForge/README.md) · [Italiano](../docs/languages/it/NVDriverForge/README.md) · [日本語](../docs/languages/ja/NVDriverForge/README.md) · [한국어](../docs/languages/ko/NVDriverForge/README.md) · [मराठी](../docs/languages/mr/NVDriverForge/README.md) · [فارسی](../docs/languages/fa/NVDriverForge/README.md) · [Polski](../docs/languages/pl/NVDriverForge/README.md) · [Português](../docs/languages/pt/NVDriverForge/README.md) · [ਪੰਜਾਬੀ](../docs/languages/pa/NVDriverForge/README.md) · [Română](../docs/languages/ro/NVDriverForge/README.md) · [Русский](../docs/languages/ru/NVDriverForge/README.md) · [Español](../docs/languages/es/NVDriverForge/README.md) · [Kiswahili](../docs/languages/sw/NVDriverForge/README.md) · [Svenska](../docs/languages/sv/NVDriverForge/README.md) · [தமிழ்](../docs/languages/ta/NVDriverForge/README.md) · [ไทย](../docs/languages/th/NVDriverForge/README.md) · [Türkçe](../docs/languages/tr/NVDriverForge/README.md) · [Українська](../docs/languages/uk/NVDriverForge/README.md) · [اردو](../docs/languages/ur/NVDriverForge/README.md) · [Tiếng Việt](../docs/languages/vi/NVDriverForge/README.md)

[Translation policy](../docs/languages/README.md)

</details>
<!-- nv-language-navigation:end -->

# NVDriverForge

**Prepare an NVIDIA driver installation with clear component choices and optional settings.**

[Download 0.1.4 & status](../docs/downloads.md#nvdriverforge) · [Installation](#installation) · [Credits](#credits-and-upstream) · [License](LICENSE)

## Overview and purpose

NVDriverForge guides you through an original NVIDIA driver package: choose the
driver, inspect its components, review optional tweaks, then confirm installation.
It exists to make those choices understandable and keep the installation,
privileged operations and recovery information together.

It is an independently developed application inspired in part by NVCleanstall's
workflow. It does not include NVCleanstall or claim complete feature parity.

## Features

- NVIDIA Game Ready / Studio lookup and downloads; optional hotfix discovery with manual fallback.
- Analysis of the original package, hashes, NVIDIA signatures, manifests and compatible INF entries.
- Component selection with dependencies and preservation of unknown components.
- Version 0.1.4 keeps selected optional NVIDIA components skippable and excludes only verified unchecked components from discovery. Already-current or inapplicable optional runtimes are no longer forced as critical components.
- Clear installation failure summaries and access to detailed logs in all 34 languages.
- Readiness checks, explicit confirmation, driver-store export and native NVIDIA profile backup before installation.
- Optional advanced settings, with preflight checks, journals and conflict-aware recovery.
- Optional **Custom NV** preset with named choices and explanations, including a separate SILK strength selection and compatibility checks.
- Optional exact-version NVENC patch downloads; source commit and target bytes are checked.
- A separate, optional installation of the Profile Inspector fork from the Tools screen.
- Component guide, reusable preferences, driver kits, local support reports and optional application updates.
- 34 interface languages and four themes.

Available advanced options concern MPO, the DLSS indicator, Ansel, NVIDIA audio
sleep, MSI, interrupt policy/priority, HDCP, display-container startup and an
eligible legacy telemetry service. Each has its own prerequisites and effects;
these are not universal performance improvements.

## Compatibility

| Requirement | Details |
| --- | --- |
| System | Windows 10 build 19041 or newer / Windows 11, x64 |
| GPU/driver | Compatible NVIDIA package and detected hardware; automatic catalog lookup primarily covers known GeForce models |
| Runtime | .NET 8 / WPF 8.0.31 included in the prepared self-contained package |
| Privileges | Normal UI/per-user setup; driver installation and system changes request administrator access |
| Network | Required for online NVIDIA lookup/downloads and explicit upstream NVENC requests; a local original driver can be selected |
| Included tools | Unmodified 7-Zip 26.03, runtime notices, optional MIT Profile Inspector companion |
| Optional companion | .NET Framework 4.8 for the separate Profile Inspector fork |

No arbitrary minimum driver version covers all features. Multi-GPU lookup must
match every detected GPU. Unsupported/professional models can require manual
driver selection. NVIDIA's installer remains the final hardware/OS authority.

## Installation

1. Visit [downloads](../docs/downloads.md#nvdriverforge) and confirm the Release is published.
2. Choose `NVDriverForge-Setup.exe` for installation, or `NVDriverForge.exe` for portable use.
3. Compare SHA-256 with the Release's `SHA256SUMS.txt`.
4. Run Setup for a per-user installation and standard uninstaller, or place the portable EXE in a writable folder and open it.

The portable includes its runtime and its optional installer. Installing
NVDriverForge does not install a GPU driver. Its EXEs are currently unsigned.

## Usage

1. **Driver:** download from NVIDIA or select an original NVIDIA installer EXE. Let analysis finish.
2. **Components:** review descriptions and required dependencies. Unknown components are retained.
3. **Tweaks:** leave unwanted options unchanged. Read effects and trade-offs before selecting anything.
4. **Review:** check the exact driver, components and optional operations, then confirm installation.
5. Accept UAC only for the operation you chose. Keep the protected job's recovery instructions.
6. If the new driver needs a restart, follow the reported state. Deferred operations require explicit resume after that restart.

Custom NV starts unchanged. Choose individual named values or review the supplied
preset and its exclusions. Its two informational internal fields are not independently
written. Settings are applied only in the verified new-driver workflow, never by
opening a preview. Installing the separate NVPI editor is not required.

Optional NVENC work downloads compatible data from a pinned keylase commit.
It alters two driver DLLs and invalidates their signatures; it can be refused
by Windows, encoders, DRM or anti-cheat. No such data or NVIDIA DLL is embedded
in NVDriverForge. [Provenance and licensing limits](../docs/provenance.md).

Preferences control language, theme and optional installed-user update checks.
The portable does not create the installed background-check task. Tools and
recovery are separate from the four installation steps.

## Backup and diagnostic tools

**Before installation:** readiness checks cover the package signature, GPUs, estimated workspace/backup space, pending restart and competing installers. The elevated worker repeats them. Competing processes are never stopped automatically. The native NVIDIA profile-database backup must succeed before NVIDIA Setup starts; driver-store export is a separate backup.

**Reusable choices:** the component guide asks four questions about games, audio, NVIDIA App and recording. Review its suggestions; required, unknown and dependency components remain protected. Export preferences, then preview and revalidate them against the selected package when importing. Consents, restart operations, program paths and patch payloads are not imported.

**Driver kit:** export a `.nvdfkit.zip` to keep the original signed NVIDIA installer, choices, hashes and instructions together. Carry `NVDriverForge.exe` separately. Import the kit in Tools, review the preview, then use the normal installation workflow. This is not a slim driver or modified standalone installer. Optional NVENC still needs a download and consent for that exact driver. NVIDIA's redistribution terms still apply.

**Results and support:** read the short result and expand the per-stage/per-option details. Successful read-back establishes a stored value, not a measured improvement. The local JSON support report uses allowlisted fields, including the last saved job after restarting the app. Preview it before saving or sharing. It includes no raw logs, profile contents or hardware identifiers and is never uploaded automatically.

**Recovery:** follow the protected job's guide to recover the backed-up driver. Explicit profile restoration requires the original driver version and same GPUs; it replaces the entire database, preserves a current copy, and checks hashes and conflicting state. Do not erase its journal or force a mismatch. Real driver installation, complete recovery and native profile import with this new workflow remain unvalidated on a real system.

**Application updates:** read the release notes, then explicitly choose a SHA-256-verified download. Checking is manual by default, with an optional check at startup. No installer is started automatically. This feature is separate from driver update checks and the installed edition's optional driver-check task.

## Screenshots

![NVDriverForge driver-page preview](../assets/screenshots/nvdriverforge-0.1.2-preview.png)

Existing 0.1.2 French UI render with example data; retained as an interface preview. The displayed 699.99 driver is a
test fixture, not a real version to download. [Image provenance](../assets/README.md).

## Update and uninstall

Close NVDriverForge, obtain the next official package and verify its hash.
Use the same Setup identity for an installed update; replace a closed portable
EXE with the new one. Keep settings and protected jobs.

Uninstall from Windows **Installed apps**. It removes the app and its update
task, not the NVIDIA driver. Settings, logs and backups remain. If desired,
restore advanced/NVENC changes through the documented recovery flow **before**
removing the app. Restore refuses conflicting changes from another tool.

Local data is under `%LOCALAPPDATA%\NVDriverForge`; protected jobs and driver
exports are under `%PROGRAMDATA%\NVDriverForge\Jobs`. Portable use also creates
local data. Driver-store export and the native profile backup are separate. Neither is a system image.

## Known limitations

- No hardware additions/INF editing, regenerated NVIDIA signatures, anti-cheat-compatible resigning or automatic unsigned-warning acceptance.
- No complete telemetry/advertising removal, slim-package export or automatic full rollback to the previous driver.
- Driver installation, boot recovery and optional profile writes have not been comprehensively validated on real machines by the hub audit.
- Registry read-back is not proof of actual HDCP, performance or latency effects.
- Signature checks use locally available Windows trust; online revocation is not performed.
- 34 languages are present, but full native-speaker/accessibility testing remains incomplete.

## Troubleshooting

| Symptom | Action |
| --- | --- |
| Online catalog unavailable | Select an original package from [NVIDIA driver downloads](https://www.nvidia.com/en-us/drivers/). Do not substitute a neighboring GPU model. |
| Hotfix lookup unavailable | Use [NVIDIA's Game Ready driver forum](https://www.nvidia.com/en-us/geforce/forums/game-ready-drivers/13/) and verify the actual package. |
| NVIDIA installation fails | Read the failure summary and open the detailed logs. Optional components already current or inapplicable remain skippable in 0.1.4. Failed installs do not trigger optional tweaks or a success/restart flow. |
| Signature/hash/backup failure | Stop that installation and retain the error; obtain the original package again if corrupted. |
| Option unavailable | Read its hardware, component or target-driver reason; keep it unchanged. |
| Restart or job still pending | Use the job's recovery instructions and explicit resume; do not erase its journal. |
| Restore conflict | Another state differs from the recorded transaction. Preserve it and request help instead of forcing a restore. |

For reports, include the selected tool version, Windows, GPU, driver and reproducible
steps; redact paths and personal details from logs. [Support](../docs/support.md).

## FAQ

**Does Setup install a graphics driver?** No. That requires the application's
separate analysis, review, confirmation and elevated installation process.

**Do I need NVCleanstall or NVPI?** No. NVCleanstall is inspiration only. The
Profile Inspector companion is an independent optional editor.

**Does it make every NVIDIA driver smaller or faster?** No. Selected components
and prerequisites determine what can change; no measured gain is promised.

**Where are the sources?** Application-specific source and private tests are
maintained separately. This hub provides documentation, binaries and third-party
source links required for attribution/licensing.

## Credits and upstream

Original application, workflow, transactions, localization, bootstrap and adaptations:
禅堂 Zendo (RevoluSound Team).

- [NVCleanstall / TechPowerUp](https://www.techpowerup.com/download/techpowerup-nvcleanstall/): workflow inspiration; no source or binary imported.
- [NVIDIA Profile Inspector / Orbmu2k](https://github.com/Orbmu2k/nvidiaProfileInspector): MIT themes, extended NVAPI interface reference and separately packaged fork.
- [7-Zip / Igor Pavlov](https://www.7-zip.org/): unmodified extraction tools.
- [Microsoft .NET](https://github.com/dotnet/runtime) and [WPF](https://github.com/dotnet/wpf): bundled runtime.
- [Inno Setup](https://jrsoftware.org/isinfo.php): original installer engine and credited translations.
- [keylase/nvidia-patch](https://github.com/keylase/nvidia-patch): external optional NVENC data source; redistribution license not established.
- [NVIDIA](https://www.nvidia.com/en-us/drivers/): external driver downloads and installed NVAPI/NVML libraries.

[Full component table](../THIRD_PARTY_NOTICES.md) · [Changes and provenance](../docs/provenance.md)

## License

[Existing binary distribution permission](LICENSE) permits use and sharing of
unmodified official executables with their notices. Application-specific source
rights are reserved. It does not restrict rights granted by the separate
third-party licenses. [Full notices](LICENSES/README.md).

Independent of NVIDIA Corporation, TechPowerUp and keylase; not sponsored or
officially endorsed by them. Product names remain their owners' trademarks.
