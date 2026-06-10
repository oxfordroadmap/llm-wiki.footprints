import os

wiki_dir = r"Q:\__writing__\_LLM_wiki_\llm-wiki.footprints\brain\wiki"

print(f"Executing brute-force line replacement in: {wiki_dir}")
fixed_count = 0
scanned_count = 0

for root, dirs, files in os.walk(wiki_dir):
    for file in files:
        if file.endswith(".md"):
            scanned_count += 1
            path = os.path.join(root, file)
            try:
                with open(path, "r", encoding="utf-8-sig") as f:
                    lines = f.readlines()

                modified = False
                for i, line in enumerate(lines):
                    # Check if the line begins with sources metadata (ignoring leading spaces)
                    if line.strip().startswith("sources:"):
                        # Check if it contains the broken double quote sequence
                        if '""' in line:
                            # Scorched earth: replace the entire line with a clean, empty YAML array
                            lines[i] = "sources: []\n"
                            modified = True

                if modified:
                    with open(path, "w", encoding="utf-8") as f:
                        f.writelines(lines)
                    print(f"FORCED CLEAN: Reset sources line in -> {file}")
                    fixed_count += 1
            except Exception as e:
                print(f"Error on {file}: {e}")

print(f"\nExecution Complete. Scanned: {scanned_count} files. Fixed: {fixed_count} files.")