# Python File Organizer

A simple Python tool that automatically organizes files into folders based on their file extensions.

---

## Features

- Sorts files into categorized folders automatically
- Creates folders if they don't already exist
- Prevents overwriting existing files
- Lets you organize any folder you choose
- Fast and lightweight
- Uses only Python's built-in libraries (no installation required)

---

## Supported File Types

| Category | Extensions |
|----------|------------|
| Documents | `.pdf`, `.doc`, `.docx`, `.csv`, `.xlsx`, `.pptx` |
| Images | `.jpg`, `.jpeg`, `.png`, `.gif`, `.svg`, `.webp` |
| Audio | `.mp3`, `.wav` |
| Videos | `.mp4`, `.mkv`, `.avi` |
| Archives | `.zip`, `.rar`, `.7z` |
| Code | `.py`, `.java`, `.cpp`, `.c`, `.js` |
| Web | `.html`, `.css` |
| Text | `.txt` |

---

## Requirements

- Python 3.9 or later

No external libraries are required.

---

## Installation

### Clone the repository

```bash
git clone https://github.com/Normal-repo/python-file-organizer
```

### Navigate to the project folder

```bash
cd python-file-organizer
```

### Run the program

```bash
python organizer.py
```

---

## Usage

When you run the script, you'll see:

```text
Enter folder path (leave blank for current directory):
```

- Enter the path of the folder you want to organize.
- Press **Enter** without typing anything to organize the current directory.

Example:

```text
C:\Users\John\Downloads
```

or simply:

```text
(Press Enter)
```

---

## Example

### Before

```text
Downloads/
├── report.pdf
├── photo.jpg
├── song.mp3
├── archive.zip
└── app.py
```

### After

```text
Downloads/
├── Documents/
│   └── report.pdf
├── Images/
│   └── photo.jpg
├── Audio/
│   └── song.mp3
├── Archives/
│   └── archive.zip
└── Code/
    └── app.py
```

---

## How It Works

The project uses:

- `pathlib` for working with file paths
- `shutil` for moving files
- Dictionaries to map file extensions to folders
- Basic loops and conditionals
- Simple error handling

---

## Future Improvements

Planned features include:

- Organize subfolders recursively
- Automatically rename duplicate files
- Real-time folder monitoring
- Build a simple GUI with Tkinter
- Add drag-and-drop support
- Package it as a Windows executable

---

## Contributing

Contributions are welcome.

1. Fork the repository.
2. Create a new branch.
3. Make your changes.
4. Commit your changes.
5. Open a Pull Request.

---

## License

This project is licensed under the MIT License.

---

## Author

**Normal Singh**

If you found this project useful, consider giving it a star on GitHub.
