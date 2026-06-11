#!/usr/bin/env python3
import argparse
import re
from pathlib import Path
from docx import Document

def extract_images_from_docx(docx_path: str):
    """
    Extracts all embedded images from a .docx file sequentially.
    Saves the output in a subdirectory within the same folder as the input file.
    """
    # Convert string input to a robust Path object
    file_path = Path(docx_path).resolve()
    
    if not file_path.is_file():
        print(f"Error: The file '{file_path}' does not exist.")
        return

    # Determine output directory in the same path: /parent/folder/filename_extracted_images
    output_dir = file_path.parent / f"{file_path.stem}_extracted_images"
    
    # Create directory if it doesn't exist (exist_ok=True prevents errors if it already exists)
    output_dir.mkdir(parents=True, exist_ok=True)
    print(f"Target directory: {output_dir}")

    try:
        doc = Document(file_path)
    except Exception as e:
        print(f"Error opening document {file_path}: {e}")
        return

    # --- Added Feature: Extract IEEE-style figure captions sequentially ---
    caption_pattern = re.compile(r'\b(Fig\.|Figure|Fig)\s*(\d+[-.\w]*)', re.IGNORECASE)
    found_captions = []
    
    for paragraph in doc.paragraphs:
        text = paragraph.text.strip()
        match = caption_pattern.search(text)
        if match:
            # Extract the raw caption identifier (e.g., "Fig. 1" or "Fig. 3.a")
            # Plus up to 10 chars to ensure sub-figure parts like "(a)" are captured
            raw_label = text[match.start():match.end() + 10].strip()
            # Clean it up slightly for previewing purposes
            cleaned_label = re.sub(r'[^\w\s\.-]', '', raw_label).replace(' ', '_')
            found_captions.append(cleaned_label)
    # ---------------------------------------------------------------------

    image_count = 0
    mapping_proposals = []
    
    # Iterate through internal document relationships sequentially (Your exact working loop)
    for rel_id, rel in doc.part.rels.items():
        if "image" in rel.target_ref:
            try:
                image_data = rel.target_part.blob
                
                # Using Path to safely extract the original extension
                original_ext = Path(rel.target_ref).suffix
                
                image_count += 1
                new_filename = f"Images.{image_count:03d}{original_ext}"
                output_path = output_dir / new_filename
                
                # Path.write_bytes() opens, writes, and closes the file automatically
                output_path.write_bytes(image_data)
                print(f"Extracted: {new_filename}")

                # --- Added Feature: Build proposal pair while processing ---
                if (image_count - 1) < len(found_captions):
                    suggested_name = f"{found_captions[image_count - 1]}{original_ext}"
                else:
                    suggested_name = f"Images.{image_count:03d}_unlabeled{original_ext}"
                
                mapping_proposals.append((new_filename, suggested_name))
                # -----------------------------------------------------------
                
            except Exception as e:
                print(f"Failed to extract image relationship {rel_id}: {e}")

    print(f"\nFinished. Extracted {image_count} images to:\n{output_dir}")

    # --- Added Feature: Print table of suggestions at the end ---
    if mapping_proposals:
        print("\n" + "="*70)
        print(" SUGGESTED FILENAME MAPPING PROPOSAL")
        print("="*70)
        print(f"{'Current Sequenced File':<25} -> {'Suggested Label Filename':<35}")
        print("-"*70)
        for current, suggested in mapping_proposals:
            print(f"{current:<25} -> {suggested:<35}")
        print("="*70)
    # -------------------------------------------------------------

def main():
    parser = argparse.ArgumentParser(
        description="Extract embedded images (SVG, PNG, JPEG) from a Word .docx file sequentially using pathlib."
    )
    parser.add_argument(
        "file_path", 
        help="Path to the target Word (.docx) file."
    )
    
    args = parser.parse_args()
    extract_images_from_docx(args.file_path)

if __name__ == "__main__":
    main()