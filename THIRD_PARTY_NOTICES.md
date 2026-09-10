<!-- nv-language-navigation:start -->
🌐 English | [Français](docs/languages/fr/THIRD_PARTY_NOTICES.md) · [NV Laboratory](README.md)

<details>
<summary>🌐 Language · 34</summary>

[العربية](docs/languages/ar/THIRD_PARTY_NOTICES.md) · [বাংলা](docs/languages/bn/THIRD_PARTY_NOTICES.md) · [简体中文](docs/languages/zh/THIRD_PARTY_NOTICES.md) · [Čeština](docs/languages/cs/THIRD_PARTY_NOTICES.md) · [Dansk](docs/languages/da/THIRD_PARTY_NOTICES.md) · [Nederlands](docs/languages/nl/THIRD_PARTY_NOTICES.md) · **English** · [Filipino](docs/languages/fil/THIRD_PARTY_NOTICES.md) · [Suomi](docs/languages/fi/THIRD_PARTY_NOTICES.md) · [Français](docs/languages/fr/THIRD_PARTY_NOTICES.md) · [Deutsch](docs/languages/de/THIRD_PARTY_NOTICES.md) · [Ελληνικά](docs/languages/el/THIRD_PARTY_NOTICES.md) · [हिन्दी](docs/languages/hi/THIRD_PARTY_NOTICES.md) · [Magyar](docs/languages/hu/THIRD_PARTY_NOTICES.md) · [Bahasa Indonesia](docs/languages/id/THIRD_PARTY_NOTICES.md) · [Italiano](docs/languages/it/THIRD_PARTY_NOTICES.md) · [日本語](docs/languages/ja/THIRD_PARTY_NOTICES.md) · [한국어](docs/languages/ko/THIRD_PARTY_NOTICES.md) · [मराठी](docs/languages/mr/THIRD_PARTY_NOTICES.md) · [فارسی](docs/languages/fa/THIRD_PARTY_NOTICES.md) · [Polski](docs/languages/pl/THIRD_PARTY_NOTICES.md) · [Português](docs/languages/pt/THIRD_PARTY_NOTICES.md) · [ਪੰਜਾਬੀ](docs/languages/pa/THIRD_PARTY_NOTICES.md) · [Română](docs/languages/ro/THIRD_PARTY_NOTICES.md) · [Русский](docs/languages/ru/THIRD_PARTY_NOTICES.md) · [Español](docs/languages/es/THIRD_PARTY_NOTICES.md) · [Kiswahili](docs/languages/sw/THIRD_PARTY_NOTICES.md) · [Svenska](docs/languages/sv/THIRD_PARTY_NOTICES.md) · [தமிழ்](docs/languages/ta/THIRD_PARTY_NOTICES.md) · [ไทย](docs/languages/th/THIRD_PARTY_NOTICES.md) · [Türkçe](docs/languages/tr/THIRD_PARTY_NOTICES.md) · [Українська](docs/languages/uk/THIRD_PARTY_NOTICES.md) · [اردو](docs/languages/ur/THIRD_PARTY_NOTICES.md) · [Tiếng Việt](docs/languages/vi/THIRD_PARTY_NOTICES.md)

[Translation policy](docs/languages/README.md)

</details>
<!-- nv-language-navigation:end -->

# Third-party notices and credits

Initial audit: 2026-09-09; NVDriverForge 0.1.3 and provenance update: 2026-09-10. **A component's license covers that
component, not the entire suite.** Application source remains private. Copyright
and permission notices are retained verbatim; this table is an index, not a
replacement for them. “External” means not distributed in the application assets.

| Component / original project | Author | Official site, repository or download | License / notice | Use in NV Tools | Modifications |
| --- | --- | --- | --- | --- | --- |
| NVIDIA Profile Inspector | Orbmu2k; Copyright 2016 | [Repository](https://github.com/Orbmu2k/nvidiaProfileInspector), [downloads](https://github.com/Orbmu2k/nvidiaProfileInspector/releases) | [MIT](NVIDIA-Profile-Inspector/LICENSE) | Whole NVPI fork; NVDF themes/extended interface reference; NVMFG wrapper/styles; RP UI resources | Fork display services, transactions and launcher; theme/control integration and wrapper adaptations |
| RTX40MFG-Unlock | Michael Robles / dashdogy; Copyright 2026 | [Repository](https://github.com/dashdogy/RTX40MFG-Unlock), [downloads](https://github.com/dashdogy/RTX40MFG-Unlock/releases) | [MIT](NVMFG-Unlock40/LICENSES/RTX40MFG-Unlock-MIT.txt) | Comparison/refinement reference and shared/adapted NVMFG native components; independently developed application | Central loading, NGX/controller coordination, per-game/V-Sync integration and diagnostics |
| MinHook, pinned 8fda4f5 | Tsuda Kageyu; Copyright 2009–2017 | [Repository](https://github.com/TsudaKageyu/minhook), [pinned source](https://github.com/TsudaKageyu/minhook/tree/8fda4f5481fed5797dc2651cd91e238e9b3928c6) | [BSD 2-clause notice](NVMFG-Unlock40/LICENSES/MinHook.txt) | Statically compiled into NVMFG engine | Included subset unchanged apart from text formatting against the inherited copy |
| Hacker Disassembler Engine (HDE64) | Vyacheslav Patkov; Copyright 2008–2009 | [MinHook's source collection](https://github.com/TsudaKageyu/minhook/tree/8fda4f5481fed5797dc2651cd91e238e9b3928c6/src/hde) | [Full MinHook/HDE notices](NVMFG-Unlock40/LICENSES/MinHook.txt) | MinHook decoder in NVMFG | No functional changes identified; HDE32 notice retained although production uses HDE64 |
| Streamline 2.12 integration headers | NVIDIA Corporation; Copyright 2023 | [Repository](https://github.com/NVIDIA-RTX/Streamline), [downloads](https://github.com/NVIDIA-RTX/Streamline/releases) | [MIT for eligible headers](NVMFG-Unlock40/LICENSES/Streamline-MIT.txt) | Compiles NVMFG Streamline integration | Headers not modified; no runtime DLL in the application package |
| NVIDIA NGX / DLSS SDK headers | NVIDIA Corporation | [Pinned repository](https://github.com/NVIDIA/DLSS/tree/a291cc7d2cc642a51566f3dfd5376f635cd1b284), [SDK](https://developer.nvidia.com/rtx/dlss) | [NVIDIA RTX SDK terms](NVMFG-Unlock40/LICENSES/NVIDIA-RTX-SDK.txt), [header notice](NVMFG-Unlock40/LICENSES/NGX-Header-Notice.txt) | Compiles NVMFG NGX integration | Headers not modified; no NGX model/provider bundled; unresolved restriction described below |
| .NET runtime 8.0.31 (NVDF) / 8.0.30 (NVMFG) | .NET Foundation, Microsoft and contributors | [Source](https://github.com/dotnet/runtime), [downloads](https://dotnet.microsoft.com/en-us/download/dotnet/8.0) | [MIT](licenses/third-party/Microsoft-NET-LICENSE.txt) and [complete third-party notices](licenses/third-party/Microsoft-NET-THIRD-PARTY-NOTICES.txt) | Self-contained NVDF and NVMFG app/agent | Runtime unmodified |
| WPF / Windows Desktop Runtime 8.0.31 (NVDF) / 8.0.30 (NVMFG) | .NET Foundation, Microsoft and contributors | [Source](https://github.com/dotnet/wpf), [downloads](https://dotnet.microsoft.com/en-us/download/dotnet/8.0) | [MIT](licenses/third-party/Microsoft-WPF-LICENSE.txt), runtime notices above | NVDF and NVMFG user interfaces | Framework unmodified; application UI authored/adapted separately |
| .NET Framework 4.8 | Microsoft | [Official runtime download](https://dotnet.microsoft.com/en-us/download/dotnet-framework/net48) | Microsoft platform/runtime terms; external | NVPI, RP and NVMFG profile helpers | None; no installer or framework DLL redistributed by this hub |
| 7-Zip 26.03 x64 | Igor Pavlov; Copyright 1999–2026 | [Site/downloads](https://www.7-zip.org/download.html), [exact source archive](https://github.com/ip7z/7zip/releases/download/26.03/7z2603-src.tar.xz) | [Full notice](licenses/third-party/7-Zip.txt), [LGPL 2.1-or-later](licenses/third-party/LGPL-2.1.txt), BSD portions and unRAR restriction | NVDF embeds unmodified 7z.exe/7z.dll and runs the CLI as a separate process | No modifications |
| Inno Setup 7.1.0 | Jordan Russell, Martijn Laan and contributors | [Site/downloads](https://jrsoftware.org/isinfo.php), [source](https://github.com/jrsoftware/issrc) | [Original Inno Setup license](licenses/third-party/Inno-Setup.txt) | Installer engines and generated uninstallers | Engine/compiler unmodified; project scripts, branding and native focus handling adapted |
| Inno Setup translation catalogs | Named original translators | [Official collection](https://jrsoftware.org/files/istrans/) | Inno/catalog notices and [complete header credits](licenses/INSTALLER-TRANSLATORS.md) | Shared 34-language catalogs for all four installers, including NVPI setup revision 2 | Keys, IDs, fonts, technical English fallback; project-authored preview catalogs where needed |
| Microsoft Visual C++ runtime / Windows SDK support | Microsoft | [Visual Studio tools](https://visualstudio.microsoft.com/downloads/), [redistribution terms index](https://learn.microsoft.com/en-us/visualstudio/releases/2022/redistribution) | Microsoft toolchain/runtime terms; not MIT by this table | Static release CRT in native engine/bootstrap binaries; installed Windows APIs | No runtime source changes; no compiler, SDK or debug runtime distributed |
| RivaTuner Statistics Server (RTSS) | Unwinder | [Official Guru3D download](https://www.guru3d.com/download/rtss-rivatuner-statistics-server-download/) | Vendor terms; no redistribution permission inferred from “freeware” | Required external limiter for RP; installed UpdateProfiles export | No RTSS code/binary modified or bundled; RP writes selected profile keys |
| NVIDIA driver / NVAPI / NVML | NVIDIA Corporation | [Driver downloads](https://www.nvidia.com/en-us/drivers/), [NVAPI](https://developer.nvidia.com/nvapi), [NVML](https://developer.nvidia.com/management-library-nvml) | NVIDIA driver/SDK terms; external | Installed native interfaces and explicit original-driver downloads | No NVIDIA DLL in hub assets; NVDF's optional NVENC operation modifies user-selected installed DLLs |
| NVIDIA NGX provider/models and Streamline runtime | NVIDIA Corporation | [DLSS SDK](https://developer.nvidia.com/rtx/dlss), [Streamline releases](https://github.com/NVIDIA-RTX/Streamline/releases) | Component-specific NVIDIA terms, distinct from MIT headers | External game/driver components used by NVMFG; SDK fetched only on request | NVMFG applies experimental in-memory behavior changes; SDK game copies can be updated with backup |
| keylase/nvidia-patch | keylase and contributors | [Repository](https://github.com/keylase/nvidia-patch), [Windows data](https://github.com/keylase/nvidia-patch/tree/master/win) | Redistribution license not established by this audit | External optional NVDF NVENC catalog/patch data, fetched from one pinned commit per selection | No upstream source, patcher or patch data copied into the hub/application assets |
| NVCleanstall | TechPowerUp | [Official page/download](https://www.techpowerup.com/download/techpowerup-nvcleanstall/) | Proprietary distribution; no source/binary redistribution permission inferred | Workflow and option inspiration for NVDF | No imported source or binary; not a fork or a runtime dependency |

## Obligations and boundaries

**MIT components:** retain copyright, permission text and disclaimer with copies.
Their license does not require publication of modified source. Original authorship
is preserved even when application source is maintained privately.

**MinHook/HDE:** preserve the notices, conditions and disclaimers in binary
documentation. The full combined notice is provided.

**7-Zip:** preserve LGPL/BSD/unRAR notices and provide access to the exact
unmodified source. The source archive is linked above, along with the full LGPL.
The unRAR restriction applies to the relevant decompression code; this is not a
blanket MIT dependency. See the author's [distribution FAQ](https://www.7-zip.org/faq.html).

**Inno Setup:** preserve required engine copyright/website notices and mark source
changes where applicable. The unmodified engine's credits remain in installers.
Adapted catalogs retain original source notices; names are indexed here.

**NVIDIA material:** the MIT license for Streamline integration headers does not
cover every SDK file. Its notice explicitly separates Nsight Perf SDK material;
that material is not used in this production target. The NGX headers are under
NVIDIA's proprietary RTX SDK terms. Their full text has been added, with an
[original-byte copy](NVMFG-Unlock40/LICENSES/NVIDIA-RTX-SDK.original.txt).
Section 4(d)'s restriction concerning technical limitations remains unresolved
for NVMFG's use. No affirmative permission is inferred from another mod's existence.

**External unknown/proprietary components:** RTSS, NVCleanstall, NVIDIA drivers,
models and keylase patch data are not bundled in the prepared hub assets. Links
identify their actual owners. A user-triggered download does not relicense a component.

The tools use Windows-provided APIs and fonts. No Windows SDK/compiler/font file
is copied into this Git repository. Build tools and private tests are outside
distribution. Runtime-internal component notices remain in the complete Microsoft
notice file rather than being reassigned to the publisher.

## Publisher contributions

禅堂 Zendo (RevoluSound Team) maintains the original application work,
adaptations and documentation described in the [provenance guide](docs/provenance.md).
[NVPI](NVIDIA-Profile-Inspector/README.md), [NVDF](NVDriverForge/README.md),
[NVMFG](NVMFG-Unlock40/README.md) and [RP](NVRasterPulse/README.md) each distinguish
inherited work from changes.

Independent projects; no affiliation with, sponsorship by or official endorsement
from NVIDIA Corporation or the listed upstream authors is implied.
