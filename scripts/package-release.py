"""Build a self-contained Skill ZIP without changing global skill registration."""
from __future__ import annotations

import argparse
from pathlib import Path
from zipfile import ZIP_DEFLATED, ZipFile

ROOT = Path(__file__).resolve().parents[1]
NAME = "research-search-strategy-optimizer"


def package_release(target: Path) -> int:
    if target.exists():
        raise FileExistsError("release exists; choose a new filename")
    entries = {}
    def include(base: Path, prefix: str, pattern: str):
        for path in base.rglob(pattern):
            if path.is_file() and "__pycache__" not in path.parts:
                entries[f"{NAME}/{prefix}{path.relative_to(base).as_posix()}"] = path
    include(ROOT / NAME, "", "*.md")
    include(ROOT / "scripts" / "research_search", "scripts/research_search/", "*.py")
    include(ROOT / "scripts" / "research_search", "scripts/research_search/", "*.html")
    include(ROOT / "schemas", "schemas/", "*.json")
    include(ROOT / "assets", "assets/", "*.md")
    entries[f"{NAME}/scripts/research-search.py"] = ROOT / "scripts/research-search.py"
    entries[f"{NAME}/examples/semg-joint-angle.json"] = ROOT / "evals/cases/semg-joint-angle.json"
    target.parent.mkdir(parents=True, exist_ok=True)
    with ZipFile(target, "x", ZIP_DEFLATED) as archive:
        for name, path in sorted(entries.items()):
            archive.write(path, name)
        archive.writestr(f"{NAME}/requirements.txt", "jsonschema>=4.23,<5\n")
    return len(entries) + 1


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("output", type=Path)
    args = parser.parse_args()
    print(f"Packaged {package_release(args.output)} files into {args.output.resolve()}")
