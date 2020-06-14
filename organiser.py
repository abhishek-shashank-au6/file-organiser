# Importing Necessary Modules
import sys
import argparse
import os
import shutil
import datetime
from pathlib import Path


# Command Line Interfacing in the Main() Function
def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--d', type=str, default=os.getcwd(),
                        help='Absolute path of the directory')
    parser.add_argument('--o', type=str, default='ext',
                        help='What Operation? (ext, size or date)')
    args = parser.parse_args()
    organise_folder(args)

# Dictionary of Directories Based on Extensions
DIRECTORIES = {
    "HTML": [".html5", ".html", ".htm", ".xhtml"],
    "CSS": [".css"],
    "JAVASCRIPT": [".js"],
    "IMAGES": [".jpeg", ".jpg", ".tiff", ".gif", ".bmp", ".png", ".bpg", "svg",
               ".heif", ".psd"],
    "VIDEOS": [".avi", ".flv", ".wmv", ".mov", ".mp4", ".webm", ".vob", ".mng",
               ".qt", ".mpg", ".mpeg", ".3gp"],
    "DOCUMENTS": [".oxps", ".epub", ".pages", ".docx", ".doc", ".fdf", ".ods",
                  ".odt", ".pwi", ".xsn", ".xps", ".dotx", ".docm", ".dox",
                  ".rvg", ".rtf", ".rtfd", ".wpd", ".xls", ".xlsx", ".ppt",
                  "pptx"],
    "ARCHIVES": [".a", ".ar", ".cpio", ".iso", ".tar", ".gz", ".rz", ".7z",
                 ".dmg", ".rar", ".xar", ".zip"],
    "AUDIO": [".aac", ".aa", ".aac", ".dvf", ".m4a", ".m4b", ".m4p", ".mp3",
              ".msv", "ogg", "oga", ".raw", ".vox", ".wav", ".wma"],
    "TEXT": [".txt", ".in", ".out"],
    "PDF": [".pdf"],
    "PYTHON": [".py"],
    "XML": [".xml"],
    "EXE": [".exe"],
    "SHELL": [".sh"]
}

# Mapping the File Extensions
FILE_FORMATS = {file_format: directory
                for directory, file_formats in DIRECTORIES.items()
                for file_format in file_formats}


def organise_folder(args):
    cwd = args.d    # Directory Path Given through the CLI
    if args.o == 'ext':  # Organising Option Given through the CLI
        for entry in os.scandir(cwd):
            # Recursively Iterating thorugh all the files in the Directory
            if not entry.is_dir():
                file_path = os.path.abspath(entry)
                if os.path.basename(file_path) == "organiser.py":
                    # Skipping the Organiser File
                    continue
                file_format = os.path.splitext(file_path)[1].lower()
                if file_format in FILE_FORMATS:
                    directory_path = os.path.join(cwd, "Organised")
                    if not os.path.exists(directory_path):
                        # Creating the 'Organised' Folder inside the Directory
                        os.mkdir(directory_path)
                    dest_folder = os.path.join(directory_path,
                                               FILE_FORMATS[file_format])
                    if not os.path.exists(dest_folder):
                        # Creating Different Directories Based On Extensions
                        os.mkdir(dest_folder)
                    # Copying the Current File Being Iterated over
                    shutil.copy2(file_path, dest_folder)
                    dest = os.path.join(dest_folder, entry)
                    if os.path.exists(dest):
                        # Deleting the File from the Original Directory
                        os.remove(file_path)
                else:
                    # If Extension not found in the Dictionary
                    directory_path = os.path.join(cwd, "Other")
                    if not os.path.exists(directory_path):
                        os.mkdir(directory_path)
                    shutil.copy2(file_path, directory_path)
                    dest = os.path.join(directory_path, entry)
                    if os.path.exists(dest):
                        os.remove(file_path)

    if args.o == 'size':
        for entry in os.scandir(cwd):
            if not entry.is_dir():
                file_path = os.path.abspath(entry)
                if os.path.basename(file_path) == "organiser.py":
                    continue
                # Getting the File Size
                file_size = os.stat(file_path).st_size/1000
                if file_size <= 10:
                    # Small Files
                    directory_path = os.path.join(cwd, "Organised")
                    if not os.path.exists(directory_path):
                        os.mkdir(directory_path)
                    dest_folder = os.path.join(directory_path, "Small")
                    if not os.path.exists(dest_folder):
                        os.mkdir(dest_folder)
                    shutil.copy2(file_path, dest_folder)
                    dest = os.path.join(dest_folder, entry)
                    if os.path.exists(dest):
                        os.remove(file_path)
                elif file_size > 10 and file_size <= 10000:
                    # Medium Sized Files
                    directory_path = os.path.join(cwd, "Organised")
                    if not os.path.exists(directory_path):
                        os.mkdir(directory_path)
                    dest_folder = os.path.join(directory_path, "Medium")
                    if not os.path.exists(dest_folder):
                        os.mkdir(dest_folder)
                    shutil.copy2(file_path, dest_folder)
                    dest = os.path.join(dest_folder, entry)
                    if os.path.exists(dest):
                        os.remove(file_path)
                else:
                    # Large Files
                    directory_path = os.path.join(cwd, "Organised")
                    if not os.path.exists(directory_path):
                        os.mkdir(directory_path)
                    dest_folder = os.path.join(directory_path, "Large")
                    if not os.path.exists(dest_folder):
                        os.mkdir(dest_folder)
                    shutil.copy2(file_path, dest_folder)
                    dest = os.path.join(dest_folder, entry)
                    if os.path.exists(dest):
                        os.remove(file_path)

    if args.o == 'date':
        for entry in os.scandir(cwd):
            if not entry.is_dir():
                file_path = os.path.abspath(entry)
                if os.path.basename(file_path) == "organiser.py":
                    continue
                # Getting the Latest Modified Date of the Current File
                file_mtime = os.stat(file_path).st_mtime
                file_timestamp = datetime.datetime.fromtimestamp(
                    file_mtime
                    ).strftime('%Y-%m-%d')
                directory_path = os.path.join(cwd, "Organised")
                if not os.path.exists(directory_path):
                    os.mkdir(directory_path)
                dest_folder = os.path.join(directory_path, file_timestamp)
                if not os.path.exists(dest_folder):
                    os.mkdir(dest_folder)
                shutil.copy2(file_path, dest_folder)
                dest = os.path.join(dest_folder, entry)
                if os.path.exists(dest):
                    os.remove(file_path)
    # Returning the Path of the Organised Folder
    sys.stdout.write(os.path.join(cwd, "Organised"))

    # Removing any Empty Directories
    for dir in os.scandir():
        try:
            if dir.is_dir():
                os.rmdir(dir)
        except BaseException:
            pass

if __name__ == "__main__":
    main()
