🌐 **Language:** English | [Français](development.fr.md) · [Home](../README.md)

# Repository architecture and maintenance

NV Laboratory is a public **documentation and binary-distribution hub**.
It does not contain application source. The four projects retain separate build
trees, versions, identities and release assets. Their private development history
is not imported into this Git repository.

## Layout

| Location | Purpose |
| --- | --- |
| README.md / README.fr.md | English/French entry points |
| Four project folders | Complete guides and applicable original notices |
| docs | Downloads, compatibility, provenance, development and release procedure |
| docs/releases.json | Audited candidate/release metadata, sizes and hashes |
| docs/provenance | File/hash comparisons; no application code |
| licenses | Shared full third-party texts and installer translator credits |
| assets | Existing reviewed UI previews and their provenance |
| .github | Issue forms and read-only documentation validation |
| tools/validate_repository.py | Standard-library publication-boundary and link checks |

Adjacent `.fr.md` files keep relative navigation predictable. English is the
default GitHub README; visitors choose French manually. No GitHub Pages site
is needed for these two maintainable entry points.

## Application technologies

| Program | Private technology | Distribution |
| --- | --- | --- |
| NVPI fork | C#, WPF, .NET Framework 4.8, NVAPI/Windows interop | Complete portable folder and separate Inno Setup |
| NVDriverForge | C#, WPF, .NET 8; native C++ bootstrap; 7-Zip process | Self-contained portable EXE and Setup |
| NVMFG Unlock40 | C#/WPF .NET 8, Framework 4.8 helpers, C++20/MASM/MinHook engine | Portable tree and Setup |
| NVRasterPulse | C#/WPF Framework 4.8; RTSS profile/reload integration; native bootstrap | Portable tree and Setup |

This public checkout cannot rebuild the applications. Automatic “Source code”
archives are hub snapshots. Upstream source links do not represent the exact
private modified source. The public CI validates this repository only.

## Local checks

From the repository root:

```text
python tools/validate_repository.py
```

Python 3.10 or newer is sufficient. The check reads files, local Markdown links,
required notices/RTSS links, release metadata and publication boundaries.
It does not execute the software, install dependencies or contact a network.

The GitHub workflow runs this same check with read-only contents permission on
push, pull request or manual dispatch. Checkout is pinned to an audited commit
and does not persist credentials. No release or deployment job is configured.

## Maintain the boundary

Update English/French guides together. Keep substantive changes separate from
formatting-only comparisons. Record actual candidate hashes, upstream commit
references and licenses; never infer a license from a project's popularity.

Use fresh versioned Release assets and re-audit changed binaries, archives and
embedded notices. Preserve private backups outside this repository. Do not use
a public workflow to import private application source or local build folders.

Tests appropriate to a functional application change run in the private project.
Do not rerun driver installers or write real profiles for a documentation update.
[Manual release procedure](releasing.md).
