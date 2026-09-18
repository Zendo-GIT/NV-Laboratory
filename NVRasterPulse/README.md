<!-- nv-language-navigation:start -->
🌐 English | [Français](README.fr.md) · [NV Laboratory](../README.md)

<details>
<summary>🌐 Language · 34</summary>

[العربية](../docs/languages/ar/NVRasterPulse/README.md) · [বাংলা](../docs/languages/bn/NVRasterPulse/README.md) · [简体中文](../docs/languages/zh/NVRasterPulse/README.md) · [Čeština](../docs/languages/cs/NVRasterPulse/README.md) · [Dansk](../docs/languages/da/NVRasterPulse/README.md) · [Nederlands](../docs/languages/nl/NVRasterPulse/README.md) · **English** · [Filipino](../docs/languages/fil/NVRasterPulse/README.md) · [Suomi](../docs/languages/fi/NVRasterPulse/README.md) · [Français](README.fr.md) · [Deutsch](../docs/languages/de/NVRasterPulse/README.md) · [Ελληνικά](../docs/languages/el/NVRasterPulse/README.md) · [हिन्दी](../docs/languages/hi/NVRasterPulse/README.md) · [Magyar](../docs/languages/hu/NVRasterPulse/README.md) · [Bahasa Indonesia](../docs/languages/id/NVRasterPulse/README.md) · [Italiano](../docs/languages/it/NVRasterPulse/README.md) · [日本語](../docs/languages/ja/NVRasterPulse/README.md) · [한국어](../docs/languages/ko/NVRasterPulse/README.md) · [मराठी](../docs/languages/mr/NVRasterPulse/README.md) · [فارسی](../docs/languages/fa/NVRasterPulse/README.md) · [Polski](../docs/languages/pl/NVRasterPulse/README.md) · [Português](../docs/languages/pt/NVRasterPulse/README.md) · [ਪੰਜਾਬੀ](../docs/languages/pa/NVRasterPulse/README.md) · [Română](../docs/languages/ro/NVRasterPulse/README.md) · [Русский](../docs/languages/ru/NVRasterPulse/README.md) · [Español](../docs/languages/es/NVRasterPulse/README.md) · [Kiswahili](../docs/languages/sw/NVRasterPulse/README.md) · [Svenska](../docs/languages/sv/NVRasterPulse/README.md) · [தமிழ்](../docs/languages/ta/NVRasterPulse/README.md) · [ไทย](../docs/languages/th/NVRasterPulse/README.md) · [Türkçe](../docs/languages/tr/NVRasterPulse/README.md) · [Українська](../docs/languages/uk/NVRasterPulse/README.md) · [اردو](../docs/languages/ur/NVRasterPulse/README.md) · [Tiếng Việt](../docs/languages/vi/NVRasterPulse/README.md)

[Translation policy](../docs/languages/README.md)

</details>
<!-- nv-language-navigation:end -->

# NVRasterPulse

**Per-application FPS limits through RivaTuner Statistics Server.**

> **Install RTSS first.** NVRasterPulse requires [RivaTuner Statistics Server (RTSS), downloaded from Guru3D](https://www.guru3d.com/download/rtss-rivatuner-statistics-server-download/). RTSS must be running to enforce limits. No RTSS installer, hook DLL or SDK is bundled.

[Download 0.2 & status](../docs/downloads.md#nvrasterpulse) · [Installation](#installation) · [How limits work](#usage) · [License](LICENSE)

## Overview and purpose

NVRasterPulse is a compact Windows interface for managing RTSS frame limits by
executable name. RTSS performs the limiting. NVRasterPulse manages the corresponding
profile values, backups and reload requests, with tray access and persistent choices.

It exists to make exact per-game limits easier to edit without replacing a whole
RTSS profile or disturbing its overlay settings. Version **0.2** adds configuration diagnostics, an FPS helper, pause, undo and profile sharing.

## Features

- Select a running application or add its executable manually.
- Save FPS limits from 1 to 1000, with up to three decimal places.
- Exact rational encoding of entered values: 59.94 becomes 2997/50.
- Front Edge Sync configuration (`SyncLimiter=1`) with active wait (`PassiveWait=0`).
- Per-executable profile updates, automatic backups and atomic writes.
- Removal of limiter overrides while retaining other profile content.
- RTSS installation detection, manual path selection and explicit launch/reload.
- Single-instance tray operation, optional installed startup, 34 languages and four themes.
- Separate normal quit and **Quit + RTSS** actions.

## Compatibility

| Requirement | Details |
| --- | --- |
| System | Windows 10/11 x64 |
| Runtime | [.NET Framework 4.8](https://dotnet.microsoft.com/en-us/download/dotnet-framework/net48), installed separately if needed |
| Required software | RTSS with `RTSS.exe`, a matching `Profiles` directory and compatible profile/reload support |
| GPU | RTSS compatibility determines the limiter; this profile manager does not require a particular RTX generation |
| Permissions | Current application requests administrator access; the selected RTSS profile folder must be accessible |
| Games | Depends on RTSS hooking support and each game's restrictions; no anti-cheat guarantee |

No specific RTSS minimum version has been certified for every function by this
hub audit. Use the official current distribution and report the exact version
if a profile key/reload does not work. Installed-but-stopped RTSS passes the
installation check; it must then be started for actual limiting.

## Installation

1. **[Download and install RTSS from Guru3D](https://www.guru3d.com/download/rtss-rivatuner-statistics-server-download/).**
2. Open [NVRasterPulse downloads](../docs/downloads.md#nvrasterpulse) and check Release availability.
3. Download `NVRasterPulse-0.2-win-x64-Setup.exe` or `NVRasterPulse-0.2-win-x64-portable.zip`, plus the notices/checksums.
4. Compare SHA-256. Run Setup or extract the entire portable ZIP to a writable local folder.
5. Open `NVRasterPulse.exe`. If RTSS is missing, use **Download RTSS**, install it, then **Check again**, or select `RTSS.exe` manually.
6. Start RTSS using its normal shortcut or NVRasterPulse's RTSS button if it is stopped.

Turning off the optional reminder does not skip the prerequisite check.
A silent Windows tray startup waits until the main window opens before displaying
this check. The setup installs NVRasterPulse only. Its EXEs are unsigned.

## Usage

1. Select the intended running application or browse to its game EXE.
2. Enter a limit between 1 and 1000 FPS, including a fractional value if needed.
3. Save and check the reported result. NVRasterPulse updates that executable's RTSS profile and requests a reload.
4. Confirm RTSS is running and verify the behavior in the intended game.

Profiles are keyed by **executable name**, such as `Game.exe.cfg`. Two different
folders containing `Game.exe` share the same RTSS profile; storing the full path
does not remove this collision.

Saving uses Front Edge Sync and active wait. Active wait may increase CPU use.
The alternate `LimitTime` fields are neutralized. Existing comments, overlay
settings and `EnableHooking=0` are preserved. The RTSS Global profile is not changed.

Use the trash action to remove NVRasterPulse's limiter overrides. It does not
delete the whole RTSS profile. A limit inherited from RTSS Global or another
tool may still apply afterwards.

**Closing and quitting:** the main window can hide to the tray. Normal **Quit**
leaves RTSS running and saved limits intact. **Quit + RTSS** requests a normal
close of the matching RTSS process in the current session, waits up to eight
seconds and does not force-kill it. Stored limits remain in both cases.

Language and theme are selected in the app. Startup at Windows sign-in is optional
and intended for an installed copy. The information button explains common actions.

## Diagnostics and profile tools

Open the actions menu for the additional tools. They preserve RTSS Global, overlay settings and exclusions.

**Diagnostics:** inspect local/effective limits, stopped RTSS, a missing executable, no detected window, disabled hooking, inheritance, paused limits, competing settings and duplicate executable names. This read-only check describes configuration; it does not prove a game is hooked by RTSS or measure its FPS.

**FPS helper:** select the display and declare VRR/G-Sync, V-Sync, Reflex and Frame Generation yourself. Rounded refresh frequency comes from Windows. If Reflex or Frame Generation is active or unknown, no automatic cap is offered. For VRR with V-Sync on and Reflex/FG off, the heuristic subtracts at least 3 FPS or approximately 2% of the refresh rate. This is not a measured optimum. Applying the suggestion fills the draft; **Save** remains a separate action.

**Pause and resume:** suspend the selected program's cap, then restore its previous limiter fields. Conflicting changes by another tool prevent an ambiguous resume. Hiding an entry does not pause its cap.

**Undo:** restore the last change to the six managed limiter fields for that program. There is one level; this does not restore all of RTSS. Conflicting external changes are refused. File backups remain separate.

**Share profiles:** export selected profiles to a `.nvrp` file. Import shows a preview and leaves existing caps unchecked by default. The file contains only executable names, limits and states, without absolute paths or scripts. Review your selection and apply. An I/O error can leave some profiles already applied; the result identifies them and each keeps its undo. Identical executable names still address the same RTSS profile.

**Favorites and hidden entries:** pin useful programs first, hide unwanted entries and restore them in the dedicated dialog. These choices persist. A closed favorite does not appear as a running application.

## Screenshots

![NVRasterPulse main-window preview](../assets/screenshots/nvrasterpulse-0.1-preview.png)

Existing French 0.1 UI render with example executable names and a 176 FPS value.
RTSS is shown stopped; this is an interface illustration, not a running limiter
or latency measurement. [Image provenance](../assets/README.md).

## Update and uninstall

Quit NVRasterPulse, download and verify the new version, then run its Setup or
extract the portable into a new folder. Preserve settings and RTSS backups.
RTSS updates are separate and come from Guru3D.

To remove an installed copy, use Windows **Installed apps**. For portable, quit
then remove its extracted folder when your backups are safe. Saved RTSS limits
are not removed by uninstalling NVRasterPulse: remove the intended limiter
overrides first. RTSS has its own uninstaller.

Local state: `%LOCALAPPDATA%\NVRasterPulse`.
Automatic RTSS backups: `%LOCALAPPDATA%\NVRasterPulse\Backups\RTSS`.
An older `%LOCALAPPDATA%\RTSSProfileBridge` location may be read for migration.
These files can contain personal executable paths and should not be posted publicly.

## Known limitations

- RTSS performs the cap. A saved value or successful reload request is not a measured frame-time result.
- Same-name executables share a profile.
- Another global/per-game limiter can affect the result; disabling the local override does not remove an inherited cap.
- A deliberately disabled RTSS hook remains disabled.
- Active waiting has a CPU/power trade-off.
- No universal game, anti-cheat or end-to-end latency validation.
- The earlier experimental independent limiter engine is not compiled or shipped.
- Automatic backups do not imply a one-click full backup-restore interface.

## Troubleshooting

| Symptom | Action |
| --- | --- |
| RTSS prerequisite remains open | Select the actual `RTSS.exe` and matching Profiles folder, then Check again. |
| Limit saved but no effect | Start RTSS; verify the correct game EXE/profile, hook permissions and other limiters. |
| Save fails | Check folder permissions and preserve the displayed error/backup. |
| Limit remains after removal | Inspect RTSS Global and other tools; the trash action only removes local limiter overrides. |
| Two games receive the same limit | Check whether their executable filenames are identical. |
| Quit + RTSS leaves RTSS open | Close RTSS normally yourself; this command deliberately avoids forced termination. |

If manually restoring an RTSS backup, close RTSS first and preserve the current
profile before replacing it with the intended backup. This can overwrite unrelated
profile edits; inspect the file and date. [Shared support](../docs/support.md).

## FAQ

**Do I need MSI Afterburner too?** NVRasterPulse requires RTSS; it does not depend
on the Afterburner application. Follow the RTSS distributor's installation options.

**Can I use this without RTSS running?** You can manage profiles once an installation
is detected, but RTSS must run for limiting.

**Does quitting or uninstalling remove the caps?** No. Remove the desired limiter
overrides explicitly before removing NVRasterPulse.

**Is it a fork of RTSS?** No. It is an independent profile manager; no RTSS source
or executable is incorporated.

## Upstream, modifications and credits

The development repository originates from
[Orbmu2k's NVIDIA Profile Inspector](https://github.com/Orbmu2k/nvidiaProfileInspector).
Its MIT palettes/UI resources are credited. The profile-management services,
fraction encoding, backups, RTSS reload bridge, tray behavior, prerequisite guide,
languages and application-specific icon were developed/adapted by
禅堂 Zendo (RevoluSound Team).

RTSS is developed by **Unwinder** and distributed separately through Guru3D.
NVRasterPulse calls `UpdateProfiles` from the selected installed hook DLL; no
RTSS SDK or hook binary is redistributed. The installer uses unmodified Inno Setup
7.1.0 with adapted scripts/translations and a project bootstrap.

[Full provenance](../docs/provenance.md) · [Third-party table](../THIRD_PARTY_NOTICES.md)

## License

The package explicitly distributes NVRasterPulse under the supplied [MIT license](LICENSE),
retaining Copyright (c) 2016 Orbmu2k. Application source is maintained privately;
MIT does not require publication of modified source. RTSS and Windows/.NET remain
under their own terms. [Full notices](LICENSES/README.md).

Independent of NVIDIA Corporation, MSI and RTSS; not sponsored or officially
endorsed by them. Product names remain their owners' trademarks.
