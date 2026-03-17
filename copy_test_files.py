#!/usr/bin/env python3
"""
Copy PDF files from source to test folder with random names
"""

import shutil
import random
import string
from pathlib import Path
import sys

def generate_random_name(length=10):
    """Generate a random filename"""
    letters = string.ascii_lowercase + string.digits
    return ''.join(random.choice(letters) for _ in range(length))

def copy_random_pdfs(source_folder, test_folder, max_files=15):
    """Copy random PDFs to test folder with random names"""
    source_path = Path(source_folder)
    test_path = Path(test_folder)

    if not source_path.exists():
        print(f"Error: Source folder not found: {source_folder}")
        sys.exit(1)

    # Find all PDF files
    pdf_files = list(source_path.rglob("*.pdf"))
    print(f"Found {len(pdf_files)} PDF files in source folder")

    if not pdf_files:
        print("No PDF files found!")
        sys.exit(1)

    # Randomly select files
    selected_files = random.sample(pdf_files, min(max_files, len(pdf_files)))
    print(f"Copying {len(selected_files)} files to test folder...")

    # Copy files with random names
    for i, source_file in enumerate(selected_files, 1):
        # Generate random name
        random_name = generate_random_name()
        dest_file = test_path / f"{random_name}.pdf"

        # Copy file
        try:
            shutil.copy2(source_file, dest_file)
            # Use a simpler name for display to avoid encoding issues
            print(f"[{i}/{len(selected_files)}] Copied file -> {random_name}.pdf")
        except Exception as e:
            print(f"Error copying file: {e}")

    print(f"\nSuccessfully copied {len(selected_files)} files to {test_path}")

if __name__ == '__main__':
    source_folder = "D:\\PDFs_Organized"
    test_folder = "test_skill"

    copy_random_pdfs(source_folder, test_folder, max_files=15)
