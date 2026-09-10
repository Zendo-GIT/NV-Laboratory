"""Validate the documentation hub without executing applications or using a network.

Copyright (c) 2026 禅堂 Zendo (RevoluSound Team). Scoped MIT: root LICENSE.
"""
from pathlib import Path
from urllib.parse import unquote, urlsplit
import collections
import json
import os
import posixpath
import re
import stat
import sys

ROOT = Path(__file__).resolve().parents[1]
PROJECTS = {
    "nvpi": ("NVIDIA-Profile-Inspector", "NVIDIA Profile Inspector – NV Tools Fork"),
    "nvdriverforge": ("NVDriverForge", "NVDriverForge"),
    "nvmfg-unlock40": ("NVMFG-Unlock40", "NVMFG Unlock40"),
    "nvrasterpulse": ("NVRasterPulse", "NVRasterPulse"),
}
RTSS = "https://www.guru3d.com/download/rtss-rivatuner-statistics-server-download/"
ROOT_FILES = {"README.md", "README.fr.md", "LICENSE", "CHANGELOG.md", "CONTRIBUTING.md",
              "SECURITY.md", "THIRD_PARTY_NOTICES.md", ".gitignore", ".gitattributes"}
FOLDERS = {".github", "assets", "docs", "licenses", "tools"} | {v[0] for v in PROJECTS.values()}
EXTENSIONS = {".md", ".txt", ".json", ".yml", ".png"}
SECRET_PATTERNS = {
    "GitHub token": r"\b(?:gh[pousr]_[A-Za-z0-9]{30,255}|github_pat_[A-Za-z0-9_]{40,255})\b",
    "cloud key": r"\b(?:AKIA|ASIA)[A-Z0-9]{16}\b|\bsk-(?:proj-)?[A-Za-z0-9_-]{40,255}\b",
    "chat token": r"\bxox[baprs]-[A-Za-z0-9-]{20,255}\b|https://discord(?:app)?\.com/api/webhooks/[0-9]+/[A-Za-z0-9_-]{20,255}",
    "private key": r"-----BEGIN (?:RSA |EC |OPENSSH |DSA |ENCRYPTED )?PRIVATE KEY-----",
    "personal workspace path": r"(?i)(?:[A-Z]:[/\\]Users[/\\](?!Public\b|Default\b)[^/\\\s]+|[A-Z]:[/\\]Windows[/\\](?:Documents|Bureau)[/\\]|NVIDIA\sR&D)",
}
errors = []
files = {}
texts = {}

def fail(message):
    errors.append(message)

def linked(path):
    info = path.lstat()
    return path.is_symlink() or bool(getattr(info, "st_file_attributes", 0) & getattr(stat, "FILE_ATTRIBUTE_REPARSE_POINT", 0x400))

for current, dirs, names in os.walk(ROOT, followlinks=False):
    current = Path(current)
    kept = []
    for name in dirs:
        path = current / name
        rel = path.relative_to(ROOT).as_posix()
        if linked(path):
            fail(f"Linked directory: {rel}")
        elif rel != ".git":
            kept.append(name)
    dirs[:] = kept
    for name in names:
        path = current / name
        rel = path.relative_to(ROOT).as_posix()
        if linked(path):
            fail(f"Linked file: {rel}")
            continue
        files[rel] = path
        parts = Path(rel).parts
        if len(parts) == 1:
            if rel not in ROOT_FILES:
                fail(f"Unexpected root file: {rel}")
        elif parts[0] not in FOLDERS:
            fail(f"Unexpected root directory: {parts[0]}")
        allowed = path.suffix in EXTENSIONS or path.name == "LICENSE" or rel in ROOT_FILES
        if rel == "tools/validate_repository.py":
            allowed = True
        if not allowed:
            fail(f"Private/source/binary or unsupported file type: {rel}")
        if any(x.lower() in {"bin", "obj", ".vs", "artifacts", "private", "audit", "node_modules", "__pycache__"} for x in parts):
            fail(f"Development directory: {rel}")
        if re.search(r"(?i)^(AGENTS|MEMOIRE|PROJECT-MEMORY|credentials|secrets|\.env)", name):
            fail(f"Private filename: {rel}")
        if path.stat().st_size > 5 * 1024 * 1024:
            fail(f"Unexpected large hub file: {rel}")
            continue
        data = path.read_bytes()
        if path.suffix == ".png":
            if not data.startswith(b"\x89PNG\r\n\x1a\n"):
                fail(f"Invalid PNG signature: {rel}")
            continue
        try:
            text = data.decode("cp1252" if rel.endswith(".original.txt") else "utf-8-sig")
        except UnicodeDecodeError:
            fail(f"Text is not readable UTF-8: {rel}")
            continue
        texts[rel] = text
        for label, pattern in SECRET_PATTERNS.items():
            if re.search(pattern, text):
                fail(f"Potential {label} in {rel}; value intentionally not displayed")

def without_fences(text):
    return re.sub(r"(?ms)^```[^\n]*\n.*?^```\s*$", "", text)

def anchors(text):
    result = set(re.findall(r'<(?:a|span)\s+id="([^"]+)"', text))
    counts = collections.Counter()
    for heading in re.findall(r"(?m)^#{1,6}\s+(.+?)\s*#*\s*$", without_fences(text)):
        heading = re.sub(r"<[^>]*>", "", heading)
        slug = re.sub(r"[^\w\- ]", "", heading.lower()).replace(" ", "-")
        n = counts[slug]
        counts[slug] += 1
        result.add(slug + (f"-{n}" if n else ""))
    return result

internal_links = 0
external_links = set()
for rel, text in texts.items():
    if not rel.endswith(".md"):
        continue
    for target in re.findall(r"\[[^\]\n]+\]\((<[^>]+>|[^\s)]+)(?:\s+\"[^\"]*\")?\)", without_fences(text)):
        target = target.strip("<>")
        url = urlsplit(target)
        if url.scheme in {"https", "http"}:
            external_links.add(target)
            continue
        if url.scheme or target.startswith("/"):
            fail(f"Unexpected absolute/special link in {rel}: {target}")
            continue
        link_path = unquote(url.path)
        if "\\" in link_path:
            fail(f"Non-portable link separator in {rel}: {target}")
            continue
        # Keep lexical case: Windows Path.resolve() can silently correct it.
        dest = posixpath.normpath(posixpath.join(posixpath.dirname(rel), link_path)) if link_path else rel
        if dest == ".." or dest.startswith(("../", "/")):
            fail(f"Link escapes repository in {rel}: {target}")
            continue
        if dest not in files:
            fail(f"Missing or case-mismatched link in {rel}: {target}")
            continue
        if url.fragment and dest.endswith(".md"):
            if unquote(url.fragment) not in anchors(texts[dest]):
                fail(f"Missing anchor in {rel}: {target}")
        internal_links += 1

required = ROOT_FILES | {"tools/validate_repository.py", ".github/workflows/validate.yml",
    ".github/ISSUE_TEMPLATE/bug-report.yml", ".github/ISSUE_TEMPLATE/feature-request.yml",
    ".github/ISSUE_TEMPLATE/security-contact.yml", "docs/releases.json", "licenses/HUB-MIT.txt",
    "licenses/third-party/LGPL-2.1.txt", "NVMFG-Unlock40/LICENSES/NVIDIA-RTX-SDK.txt"}
for folder, _ in PROJECTS.values():
    required |= {f"{folder}/README.md", f"{folder}/README.fr.md", f"{folder}/LICENSE", f"{folder}/LICENSES/README.md"}
for name in required - files.keys():
    fail(f"Missing required file: {name}")

for name in ["README.md", "README.fr.md", "NVRasterPulse/README.md", "NVRasterPulse/README.fr.md",
             "docs/installation.md", "docs/installation.fr.md", "docs/downloads.md", "docs/downloads.fr.md"]:
    if RTSS not in texts.get(name, ""):
        fail(f"Missing official RTSS link: {name}")
for folder, _ in PROJECTS.values():
    for suffix, counterpart in [(".md", "README.fr.md"), (".fr.md", "README.md")]:
        if f"]({counterpart})" not in texts.get(f"{folder}/README{suffix}", ""):
            fail(f"Missing language navigation: {folder}/README{suffix}")

try:
    catalog = json.loads(texts["docs/releases.json"])
    assert catalog["repository"] == "Zendo-GIT/NV-Laboratory"
    assert catalog["application_sources"] == "private"
    assert {p["id"] for p in catalog["projects"]} == set(PROJECTS)
    assert len(catalog["projects"]) == len(PROJECTS)
    assert len({p["tag"] for p in catalog["projects"]}) == len(PROJECTS)
    for project in catalog["projects"]:
        assert (project["folder"], project["name"]) == PROJECTS[project["id"]]
        assert project["status"] in {"prepared", "published", "withdrawn"}
        assert project["release_url"] == "https://github.com/Zendo-GIT/NV-Laboratory/releases/tag/" + project["tag"]
        if project["status"] == "published":
            assert re.fullmatch(r"\d{4}-\d{2}-\d{2}", project["release_date"])
        else:
            assert project["release_date"] is None
        assert len({a["name"] for a in project["assets"]}) == len(project["assets"])
        for asset in project["assets"]:
            assert re.fullmatch(r"[A-Za-z0-9_.-]+", asset["name"])
            assert asset["bytes"] > 0 and re.fullmatch(r"[0-9a-f]{64}", asset["sha256"])
            for page in ["docs/downloads.md", "docs/downloads.fr.md"]:
                assert asset["name"] in texts[page] and asset["sha256"] in texts[page]
except (KeyError, ValueError, AssertionError, TypeError) as exc:
    fail(f"Invalid or inconsistent release catalog/download pages: {type(exc).__name__}")

workflow = texts.get(".github/workflows/validate.yml", "")
if "contents: read" not in workflow or "persist-credentials: false" not in workflow:
    fail("Workflow must use read-only contents and not persist credentials")
if re.search(r"pull_request_target|contents:\s*write|gh\s+release|git\s+push", workflow):
    fail("Workflow contains an unexpected publication/write operation")
if not re.search(r"actions/checkout@[0-9a-f]{40}", workflow):
    fail("Checkout must be pinned to a full commit hash")

result = {"passed": not errors, "files": len(files), "internal_links": internal_links,
          "external_urls_inventory_only": len(external_links), "projects": len(PROJECTS),
          "executed_applications": False, "network_access": False, "errors": errors}
print(json.dumps(result, ensure_ascii=False, indent=2))
sys.exit(0 if not errors else 1)
