from pathlib import Path
import shutil


folder = Path(input("Enter folder path (leave blank for current directory): ").strip() or ".").resolve()

if not folder.exists() or not folder.is_dir():
    print("Invalid folder path.")
    exit()


file_types = {
    ".pdf": "Documents",
    ".doc": "Documents",
    ".docx": "Documents",
    ".txt": "Text Files",
    ".csv": "Documents",
    ".xlsx": "Documents",
    ".pptx": "Documents",

    ".jpg": "Images",
    ".jpeg": "Images",
    ".png": "Images",
    ".webp": "Images",
    ".svg": "Images",
    ".gif": "Images",

    ".mp3": "Audio",
    ".wav": "Audio",

    ".mp4": "Videos",
    ".mkv": "Videos",
    ".avi": "Videos",

    ".zip": "Archives",
    ".rar": "Archives",
    ".7z": "Archives",

    ".py": "Python",
    ".java": "Code",
    ".cpp": "Code",
    ".c": "Code",
    ".js": "Code",
    ".html": "Web",
    ".css": "Web",
}

moved = 0
skipped = 0

for item in folder.iterdir():

    if not item.is_file():
        continue

    extension = item.suffix.lower()

    if extension not in file_types:
        print(f"Unknown file type: {item.name}")
        skipped += 1
        continue

    destination = folder / file_types[extension]
    destination.mkdir(exist_ok=True)

    new_path = destination / item.name

    if new_path.exists():
        print(f"File already exists: {item.name}")
        skipped += 1
        continue

    shutil.move(item, new_path)
    moved += 1

    print(f"{item.name} → {destination.name}")

# ==========================
# Summary
# ==========================

print("\n*********************************Summary********************************* ")
print(f"Files moved   : {moved}")
print(f"Files skipped : {skipped}")
print("Organization complete!")