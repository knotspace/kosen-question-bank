#!/usr/bin/env python3
"""Validate basic structure and publication status of KOSEN question datasets."""
import json
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
FILES = [
    ROOT / "data/questions/math.json",
    ROOT / "data/questions/science.json",
    ROOT / "data/questions/social.json",
    ROOT / "data/questions/expansion-2026-11-05.json",
    ROOT / "data/questions/expansion-2026-11-08.json",
    ROOT / "data/questions/expansion-2026-11-09.json",
    ROOT / "data/questions/expansion-2026-11-08-b.json",
    ROOT / "data/questions/expansion-2026-11-09-noon.json",
]
REQUIRED = {"id", "subject", "unit", "prompt", "answer", "explanation",
            "status", "verification", "created_at"}
VALID_SUBJECTS = {"math", "science", "social", "english", "japanese"}
VALID_STATUSES = {"draft", "review", "verified", "retired"}
VALID_ANSWER = {"official", "independently_verified", "provisional", "unresolved"}

def main():
    errors = []
    seen = set()
    count = 0
    for path in FILES:
        try:
            items = json.loads(path.read_text(encoding="utf-8"))
        except Exception as exc:
            errors.append(f"{path.relative_to(ROOT)}: JSON read error: {exc}")
            continue
        if not isinstance(items, list):
            errors.append(f"{path.relative_to(ROOT)}: root must be an array")
            continue
        for i, item in enumerate(items):
            count += 1
            where = f"{path.relative_to(ROOT)}[{i}]"
            if not isinstance(item, dict):
                errors.append(f"{where}: item must be an object")
                continue
            missing = REQUIRED - item.keys()
            if missing:
                errors.append(f"{where}: missing {', '.join(sorted(missing))}")
                continue
            if item["id"] in seen:
                errors.append(f"{where}: duplicate id {item['id']}")
            seen.add(item["id"])
            if item["subject"] not in VALID_SUBJECTS:
                errors.append(f"{where}: invalid subject")
            if item["status"] not in VALID_STATUSES:
                errors.append(f"{where}: invalid status")
            verification = item["verification"]
            if not isinstance(verification, dict) or verification.get("answer_status") not in VALID_ANSWER:
                errors.append(f"{where}: invalid verification.answer_status")
            if item["status"] == "verified" and verification.get("answer_status") in {"provisional", "unresolved"}:
                errors.append(f"{where}: verified question cannot have provisional/unresolved answer")
    if errors:
        print("\n".join(errors))
        return 1
    print(f"OK: {count} questions checked across {len(FILES)} datasets")
    return 0

if __name__ == "__main__":
    sys.exit(main())
