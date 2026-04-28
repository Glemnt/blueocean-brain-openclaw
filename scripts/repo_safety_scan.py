#!/usr/bin/env python3
"""Safety scan for Blue Ocean Brain repository.

Checks for raw data extensions, likely secrets, and obvious PII patterns.
Designed as a conservative pre-commit gate; findings must be reviewed by a human.
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SKIP_DIRS = {".git", "node_modules", ".venv", "venv", "__pycache__"}
RAW_EXTS = {".csv", ".tsv", ".xlsx", ".xls", ".pdf", ".html", ".json"}
ALLOW_RAW = set()  # no raw payloads should be versioned by default
SECRET_PATTERNS = [
    re.compile(r"KOMMO_ACCESS_TOKEN\s*="),
    re.compile(r"(?i)(access_token|refresh_token|client_secret|private_key)\s*[:=]"),
    re.compile(r"-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----"),
    re.compile(r"\bsk-[A-Za-z0-9_-]{20,}\b"),
]
PII_PATTERNS = [
    re.compile(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}"),
    re.compile(r"(?:\+?55\s?)?(?:\(?\d{2}\)?\s?)?9?\d{4}[-\s]?\d{4}"),
]
ALLOW_CONCEPT_FILES = {
    "governance/data-and-evidence-policy.md",
    "integrations/kommo-field-mapping.md",
    "schemas/whatsapp-redirect-event.md",
    "history/README.md",
    "INFRA_ROBUSTNESS_AUDIT.md",
}


def iter_files():
    for path in ROOT.rglob("*"):
        if not path.is_file():
            continue
        if any(part in SKIP_DIRS for part in path.parts):
            continue
        yield path


def main() -> int:
    findings: list[str] = []
    for path in iter_files():
        rel = path.relative_to(ROOT).as_posix()
        if path.suffix.lower() in RAW_EXTS and rel not in ALLOW_RAW:
            findings.append(f"raw-like file extension not allowed: {rel}")
            continue
        text = path.read_text(encoding="utf-8", errors="ignore")
        for pat in SECRET_PATTERNS:
            if pat.search(text):
                findings.append(f"possible secret: {rel} :: {pat.pattern}")
        if rel not in ALLOW_CONCEPT_FILES:
            for pat in PII_PATTERNS:
                if pat.search(text):
                    findings.append(f"possible PII: {rel} :: {pat.pattern}")

    if findings:
        for f in findings:
            print(f"FAIL: {f}")
        return 1
    print("OK: no raw files, obvious secrets, or unapproved PII patterns detected")
    return 0


if __name__ == "__main__":
    sys.exit(main())
