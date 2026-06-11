#!/usr/bin/env python3
"""
py-label_ieee_figures.py  —  Step 2 of a two-step workflow

Step 1 (your existing script): extract images sequentially as Images.001.png, etc.
Step 2 (this script):          walk document.xml in reading order to assign Fig. N labels,
                                then rename (or copy) the extracted files.

Usage:
    python py-label_ieee_figures.py paper.docx
    python py-label_ieee_figures.py paper.docx --images-dir path/to/extracted/
    python py-label_ieee_figures.py paper.docx --dry-run
    python py-label_ieee_figures.py paper.docx --copy        # keep originals, write renamed copies
    python py-label_ieee_figures.py paper.docx --csv         # write figures.csv summary

How it works:
    1. Parse word/_rels/document.xml.rels  →  {rId: media/imageN.xxx}
    2. Walk document.xml paragraphs in order, collecting rIds as images appear
       → builds  {rId: doc_sequence_index}   (1-based, reading order)
    3. For each image paragraph, look ahead ≤3 paragraphs for a Fig. caption
       → builds  {rId: "fig_2a"}
    4. Load the already-extracted files, match by sequence index, rename.
"""

import argparse
import csv
import re
import shutil
import sys
import zipfile
from pathlib import Path
from lxml import etree

# ── XML namespaces ────────────────────────────────────────────────────────────
NS = {
    "w":   "http://schemas.openxmlformats.org/wordprocessingml/2006/main",
    "a":   "http://schemas.openxmlformats.org/drawingml/2006/main",
    "r":   "http://schemas.openxmlformats.org/officeDocument/2006/relationships",
    "v":   "urn:schemas-microsoft-com:vml",
}
IMAGE_REL_TYPE = "http://schemas.openxmlformats.org/officeDocument/2006/relationships/image"

# ── Caption regex ─────────────────────────────────────────────────────────────
# Matches: Fig. 1 / Fig 1 / Figure 1 / fig.1
#          Fig. 2a / Fig. 2(a) / Fig. 2.a / Fig. 2 (a)
FIG_RE = re.compile(
    r"(?:Fig(?:ure)?\.?\s*)(\d+)(?:[\s.\-]?\(?([a-zA-Z])\)?)?",
    re.IGNORECASE,
)


def slugify(num: str, sub: str | None) -> str:
    return f"fig_{num}" + (sub.lower() if sub else "")


# ── Helpers ───────────────────────────────────────────────────────────────────

def load_image_rels(zf: zipfile.ZipFile) -> dict[str, str]:
    """Return {rId: 'media/imageN.ext'} for image relationships only."""
    rels = {}
    try:
        with zf.open("word/_rels/document.xml.rels") as f:
            tree = etree.parse(f)
        for rel in tree.getroot():
            if IMAGE_REL_TYPE in rel.get("Type", ""):
                rels[rel.get("Id")] = rel.get("Target", "").lstrip("../")
    except KeyError:
        pass
    return rels


def para_text(el) -> str:
    return "".join(t.text or "" for t in el.xpath(".//w:t", namespaces=NS))


def image_rids_in_para(el) -> list[str]:
    """Collect image rIds from DrawingML blips and legacy VML imagedata."""
    rids = []
    for blip in el.xpath(".//a:blip", namespaces=NS):
        rid = blip.get("{%s}embed" % NS["r"])
        if rid:
            rids.append(rid)
    for imgdata in el.xpath(".//v:imagedata", namespaces=NS):
        rid = imgdata.get("{%s}id" % NS["r"])
        if rid:
            rids.append(rid)
    return rids


# ── Core: build rId → (doc_seq, fig_label) map ───────────────────────────────

def build_figure_map(zf: zipfile.ZipFile, image_rels: dict[str, str]) -> list[dict]:
    """
    Walk document paragraphs in reading order.
    Returns a list (in doc order) of:
        { seq: int,          # 1-based position among ALL images in doc
          rid: str,
          media: str,        # 'media/image3.png'
          label: str|None,   # 'fig_2a' or None
          caption: str }
    """
    with zf.open("word/document.xml") as f:
        body = etree.parse(f).find(".//w:body", NS)

    paragraphs = list(body)
    records = []
    seq = 0

    for i, para in enumerate(paragraphs):
        rids = image_rids_in_para(para)
        if not rids:
            continue

        # Look ahead for caption
        caption_text = ""
        label = None
        for j in range(i + 1, min(i + 4, len(paragraphs))):
            txt = para_text(paragraphs[j]).strip()
            m = FIG_RE.search(txt)
            if m:
                caption_text = txt
                label = slugify(m.group(1), m.group(2))
                break

        for k, rid in enumerate(rids):
            if rid not in image_rels:
                continue
            seq += 1
            rec_label = label
            # Multiple images under one caption → append part letter
            if label and len(rids) > 1:
                rec_label = label + chr(ord("a") + k) if not label[-1].isalpha() else label
            records.append({
                "seq":     seq,
                "rid":     rid,
                "media":   image_rels[rid],
                "label":   rec_label,
                "caption": caption_text,
            })

    return records


# ── Rename extracted files ────────────────────────────────────────────────────

def find_extracted_file(images_dir: Path, seq: int) -> Path | None:
    """Find Images.NNN.* for a given sequence number."""
    pattern = f"Images.{seq:03d}.*"
    matches = list(images_dir.glob(pattern))
    return matches[0] if matches else None


def rename_figures(
    records: list[dict],
    images_dir: Path,
    copy_mode: bool,
    dry_run: bool,
) -> list[dict]:
    """Rename (or copy) Images.NNN.ext → fig_N.ext. Returns enriched records."""
    used: dict[str, int] = {}

    for rec in records:
        src = find_extracted_file(images_dir, rec["seq"])
        if src is None:
            rec["status"] = f"MISSING (Images.{rec['seq']:03d}.*)"
            rec["dest"] = ""
            continue

        base = rec["label"] or f"fig_unknown_{rec['seq']:03d}"
        # Collision guard
        key = base
        if key in used:
            used[key] += 1
            base = f"{base}_{used[key]}"
        else:
            used[key] = 0

        dest = images_dir / (base + src.suffix)
        rec["dest"] = dest.name

        if dry_run:
            rec["status"] = "dry"
        else:
            try:
                if copy_mode:
                    shutil.copy2(src, dest)
                    rec["status"] = "copied"
                else:
                    src.rename(dest)
                    rec["status"] = "renamed"
            except Exception as e:
                rec["status"] = f"ERROR: {e}"

    return records


# ── Reporting ─────────────────────────────────────────────────────────────────

def print_report(records: list[dict], dry_run: bool) -> None:
    print(f"\n{'Seq':<5} {'Label':<12} {'Source':<18} {'→  Dest':<30}  Caption")
    print("─" * 95)
    for r in records:
        src_name = f"Images.{r['seq']:03d}.*"
        cap = (r["caption"][:38] + "…") if len(r["caption"]) > 38 else r["caption"]
        marker = "[dry]" if dry_run else f"[{r.get('status','?')}]"
        print(f"{r['seq']:<5} {(r['label'] or 'unknown'):<12} {src_name:<18} →  {r.get('dest',''):<28}  {cap}")
    print(f"\nTotal images mapped: {len(records)}")
    labeled   = sum(1 for r in records if r["label"])
    unlabeled = len(records) - labeled
    print(f"  With Fig. label : {labeled}")
    if unlabeled:
        print(f"  No caption found: {unlabeled}  (kept as fig_unknown_NNN)")


def write_csv(records: list[dict], images_dir: Path) -> None:
    csv_path = images_dir / "figures.csv"
    fields = ["seq", "label", "dest", "caption", "rid", "media", "status"]
    with open(csv_path, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fields, extrasaction="ignore")
        writer.writeheader()
        writer.writerows(records)
    print(f"CSV written: {csv_path}")


# ── CLI ───────────────────────────────────────────────────────────────────────

def main() -> None:
    parser = argparse.ArgumentParser(
        description="Label extracted IEEE figures by reading document order + captions."
    )
    parser.add_argument("docx", help="The original .docx file")
    parser.add_argument(
        "--images-dir", default=None,
        help="Folder with Images.NNN.* files (default: <docx_stem>_extracted_images/)"
    )
    parser.add_argument("--dry-run", action="store_true", help="Show plan, write nothing")
    parser.add_argument("--copy",    action="store_true", help="Copy instead of rename (keep originals)")
    parser.add_argument("--csv",     action="store_true", help="Write figures.csv")
    args = parser.parse_args()

    docx_path = Path(args.docx).resolve()
    if not docx_path.exists():
        sys.exit(f"File not found: {docx_path}")

    images_dir = (
        Path(args.images_dir).resolve()
        if args.images_dir
        else docx_path.parent / (docx_path.stem + "_extracted_images")
    )
    if not images_dir.exists():
        sys.exit(f"Images folder not found: {images_dir}\nRun Step 1 first.")

    print(f"DOCX      : {docx_path}")
    print(f"Images dir: {images_dir}")
    if args.dry_run:
        print("Mode      : DRY RUN\n")

    with zipfile.ZipFile(docx_path, "r") as zf:
        image_rels = load_image_rels(zf)
        records    = build_figure_map(zf, image_rels)

    records = rename_figures(records, images_dir, copy_mode=args.copy, dry_run=args.dry_run)
    print_report(records, args.dry_run)

    if args.csv and not args.dry_run:
        write_csv(records, images_dir)


if __name__ == "__main__":
    main()