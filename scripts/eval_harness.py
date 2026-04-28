#!/usr/bin/env python3
"""Structural eval harness for Blue Ocean Brain Markdown evals.

This does not judge model quality. It validates that the eval suite is
well-formed enough to be used as a regression checklist.
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
EVALS = ROOT / "evals"
REQUIRED_FILES = [
    "README.md",
    "eval-manifest.md",
    "meta-ads.md",
    "dados-bi.md",
    "sdr-comercial.md",
    "copy.md",
    "competitive-intelligence.md",
]
CONFIDENCE = {"Alta", "Parcial", "Frágil", "Insuficiente"}


def fail(msg: str) -> None:
    print(f"FAIL: {msg}")
    raise SystemExit(1)


def main() -> int:
    missing = [f for f in REQUIRED_FILES if not (EVALS / f).exists()]
    if missing:
        fail(f"missing eval files: {missing}")

    total_scenarios = 0
    problems: list[str] = []

    for path in sorted(EVALS.glob("*.md")):
        text = path.read_text(encoding="utf-8", errors="replace")
        if not text.lstrip().startswith("# "):
            problems.append(f"{path.relative_to(ROOT)}: missing H1")
        if path.name not in {"README.md", "eval-manifest.md"}:
            scenarios = len(re.findall(r"^##\s+", text, flags=re.M))
            total_scenarios += scenarios
            if scenarios == 0:
                problems.append(f"{path.relative_to(ROOT)}: no scenarios")
            if not any(word in text for word in CONFIDENCE):
                problems.append(f"{path.relative_to(ROOT)}: no confidence language")
            for required in ["Resposta boa", "Resposta ruim"]:
                if required not in text:
                    problems.append(f"{path.relative_to(ROOT)}: missing '{required}' marker")

    if total_scenarios < 5:
        problems.append(f"eval suite has too few scenarios: {total_scenarios}")

    if problems:
        for p in problems:
            print(f"FAIL: {p}")
        return 1

    print(f"OK: {len(REQUIRED_FILES)} eval files, {total_scenarios} scenarios")
    return 0


if __name__ == "__main__":
    sys.exit(main())
