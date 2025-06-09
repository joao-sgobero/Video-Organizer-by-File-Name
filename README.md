# Video Organizer by File Name

This script automatically organizes video files by creating a folder with the file's name and moving the video into it. It's ideal for organizing projects, episodes, videos with additional files, and keeping your directory clean without having to manually create folders.

## 🧩 How It Works

The script scans all video files in the folder where it is located (.mp4, .avi, .mkv, .mov, .ts) and:

1. **Creates a folder with the file name (without the extension).**
2. **Moves the video into that folder.**

This eliminates the repetitive task of creating folders one by one, especially when videos come with subtitles, covers, project files, etc.

## 🛠️ How to Use

1. **Copy the file** `name_script.py` into the folder where your videos are.
2. **Run the script** using Python:

    ```bash
    python organize_videos.py
    ```

## Requirements

1. **Python 3.x**
2. **Libraries:**
   - `os` (for file and directory manipulation)
   - `shutil` (for moving files)

   **No external libraries are required**. The script uses only Python's standard libraries.

---

## Main Advantages

**Automatic Organization**: The script automatically creates folders based on each video's name, saving time when organizing videos with multiple files like subtitles or covers.

**Eliminates Manual Folder Creation**: When you have several videos that need to be moved to separate folders, the script handles this without the need for manual folder creation.

**Prevents Clutter**: By keeping the videos organized in specific folders, you eliminate the mess of having a single directory with multiple video files.

## 📌 Notes

**Supported Extensions**: Only files with the extensions `.mp4`, `.avi`, `.mkv`, `.mov`, and `.ts` are considered.

- The script must be run in the same folder as the videos to be organized.
- The current video name will be used as a reference to create the folder.
- The script does not overwrite existing files or folders.

### Developed by João Henrique Sgobero
