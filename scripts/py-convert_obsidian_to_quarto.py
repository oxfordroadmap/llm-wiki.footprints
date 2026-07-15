#!/usr/bin/env python3
"""
py-convert_obsidian_to_quarto.py

Copies an Obsidian .md vault to a Quarto output folder,
rewriting [[wiki links]] to [label](path.qmd) along the way.

Usage:
    python scripts/convert_obsidian_to_quarto.py
    python scripts/convert_obsidian_to_quarto.py --src brain/wiki --out site_src
    python scripts/convert_obsidian_to_quarto.py --dry-run
"""

import re
import os
import shutil
import argparse
from pathlib import Path

# ── Patterns ──────────────────────────────────────────────────────────────────

# [[path/to/page|display label]]   →  [display label](path/to/page.qmd)
# [[path/to/page]]                 →  [path/to/page](path/to/page.qmd)
# [[path/to/page#Heading]]         →  [path/to/page](path/to/page.qmd#heading)
# ![[image.png]]                   →  ![image.png](image.png)

# Files to exclude from conversion (matched by filename, any folder)
SKIP_FILES = {"log.md"}

WIKI_LINK    = re.compile(r'\[\[([^\]|#]+?)(?:#([^\]|]+?))?(?:\|([^\]]+?))?\]\]')
EMBED_IMAGE  = re.compile(r'!\[\[([^\]]+?)\]\]')


def _slugify_heading(heading: str) -> str:
    """Convert a heading to a URL-safe anchor (Quarto/Pandoc style)."""
    return heading.strip().lower().replace(" ", "-")


def convert_wikilinks(text: str, file_vault_rel: Path) -> str:
    """
    Rewrite wiki links so hrefs are RELATIVE TO THE FILE, not the vault root.

    Example: file is at  concepts/grid-paradox.md
      [[concepts/socio-technical-systems]]  →  [socio-technical-systems](../concepts/socio-technical-systems.qmd)
      [[entities/taipower]]                 →  [taipower](../entities/taipower.qmd)
      [[concepts/grid-paradox]]             →  [grid-paradox](grid-paradox.qmd)  (same folder → no prefix)

    file_vault_rel: path of this file relative to the vault root, e.g. PurePosixPath("concepts/grid-paradox.md")
    """
    file_folder = file_vault_rel.parent   # e.g. PurePosixPath("concepts")

    # 1. Embedded images — keep relative to same folder
    def replace_embed(m: re.Match) -> str:
        img = m.group(1).strip()
        # Images usually have no folder prefix in Obsidian; keep as-is
        return f"![{img}]({img})"

    text = EMBED_IMAGE.sub(replace_embed, text)

    # 2. Wiki links
    def replace(m: re.Match) -> str:
        raw_path = m.group(1).strip()        # e.g. "entities/siemens"  or  "siemens"
        heading  = m.group(2)                # e.g. "Section Title"  (may be None)
        label    = m.group(3)                # e.g. "Siemens"        (may be None)

        target   = Path(raw_path)            # vault-root-relative target (no extension)
        display  = (label or target.name).strip()

        # Compute href relative to this file's folder
        try:
            rel = Path(os.path.relpath(target, file_folder))
        except ValueError:
            # os.path.relpath can fail across Windows drive letters — fall back
            rel = target

        href = rel.as_posix() + ".qmd"

        if heading:
            href += "#" + _slugify_heading(heading)

        return f"[{display}]({href})"

    return WIKI_LINK.sub(replace, text)


def process_file(src: Path, dst: Path, src_root: Path, dry_run: bool) -> int:
    """Convert one .md file → .qmd file.  Returns number of links rewritten."""
    raw = src.read_text(encoding="utf-8")

    # vault-relative path for this file (used to compute relative hrefs)
    vault_rel = src.relative_to(src_root)
    converted = convert_wikilinks(raw, vault_rel)

    qmd_path = dst.with_suffix(".qmd")

    if not dry_run:
        qmd_path.parent.mkdir(parents=True, exist_ok=True)
        qmd_path.write_text(converted, encoding="utf-8")

    count = len(WIKI_LINK.findall(raw)) + len(EMBED_IMAGE.findall(raw))
    return count


def copy_non_md(src: Path, dst: Path, dry_run: bool) -> None:
    """Copy images and other assets unchanged."""
    if not dry_run:
        dst.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(src, dst)


def run(src_root: Path, out_root: Path, dry_run: bool) -> None:
    if dry_run:
        print(f"[dry-run] Would convert: {src_root}  →  {out_root}\n")
    else:
        print(f"Converting: {src_root}  →  {out_root}\n")

    md_count    = 0
    asset_count = 0
    link_count  = 0

    for src_file in sorted(src_root.rglob("*")):
        if not src_file.is_file():
            continue

        rel      = src_file.relative_to(src_root)
        dst_file = out_root / rel

        # Skip hidden files (e.g. .obsidian folder)
        if any(part.startswith(".") for part in rel.parts):
            continue

        # Skip excluded filenames
        if src_file.name in SKIP_FILES:
            print(f"  {'[dry]' if dry_run else '     '} SKIP  {rel}")
            continue

        if src_file.suffix.lower() == ".md":
            n = process_file(src_file, dst_file, src_root, dry_run)
            link_count += n
            md_count   += 1
            marker = f"  ({n} links)" if n else ""
            print(f"  {'[dry]' if dry_run else '     '} {rel}  →  {rel.with_suffix('.qmd')}{marker}")
        else:
            copy_non_md(src_file, dst_file, dry_run)
            asset_count += 1

    print(f"\n{'[dry-run] ' if dry_run else ''}Done.")
    print(f"  .md files converted : {md_count}")
    print(f"  wiki links rewritten: {link_count}")
    print(f"  assets copied       : {asset_count}")


def main() -> None:
    parser = argparse.ArgumentParser(description="Convert Obsidian vault to Quarto source.")
    parser.add_argument("--src", default=".",       help="Obsidian vault root (default: .)")
    parser.add_argument("--out", default="site_src", help="Quarto output folder (default: site_src)")
    parser.add_argument("--dry-run", action="store_true", help="Print what would happen; write nothing")
    args = parser.parse_args()

    src_root = Path(args.src).resolve()
    out_root = Path(args.out).resolve()

    if not src_root.exists():
        raise SystemExit(f"Source folder not found: {src_root}")

    if src_root == out_root:
        raise SystemExit("Source and output folders must be different.")

    run(src_root, out_root, args.dry_run)


if __name__ == "__main__":
    main()