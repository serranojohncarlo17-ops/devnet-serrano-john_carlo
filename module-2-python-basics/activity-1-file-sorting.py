"""
Module 2 — Activity: File Sorting with os and shutil
Student: [Serrano, John Carlo S.]
Date: [September 28, 2026]

============================================
WHAT DID YOU BUILD? (explain in your own words)
============================================
I made a simple Python program that automatically organizes
files into different folders. The program checks the file extension and uses it to decide
where the file should go. For example, image files like .jpg and .png go into the Images
folder, while .pdf and .docx files go into the Documents folder.


============================================
KEY VOCABULARY
============================================
- os module: module that I use to work with files, folders,
directories, and file paths on my computer.

- shutil module: module that I use to move, copy, and manage
files and folders.

- file path: the exact location of a file or folder on my computer.
For example: C:\Users\serra\OneDrive\Documents\DEVNET\files\Documents\SST.pdf

- directory: is just a folder. It is used to organize files
and other folders.

- file extension: the part at the end of a filename that shows what type
of file it is, like .jpg, .pdf, .mp3, or .mp4.

- source folder: the folder where the files are originally located before
the program sorts and moves them.


============================================
YOUR SCRIPT
============================================
Paste the code you already wrote for this activity below.
"""

import os
import shutil

source_folder = "files"

file_categories = {
    "Images": [".jpg", ".jpeg", ".png", ".gif"],
    "Documents": [".pdf", ".doc", ".docx", ".txt"],
    "Audio": [".mp3", ".wav"],
    "Videos": [".mp4", ".avi", ".mkv"],
    "Others": []
}

if not os.path.exists(source_folder):
    os.makedirs(source_folder)
    print("The 'files' folder was created.")
    print("Put some files inside it and run the program again.")

else:
    for filename in os.listdir(source_folder):

        file_path = os.path.join(source_folder, filename)

        if os.path.isdir(file_path):
            continue

        extension = os.path.splitext(filename)[1].lower()

        category = "Others"

        for folder_name, extensions in file_categories.items():
            if extension in extensions:
                category = folder_name
                break

        destination_folder = os.path.join(source_folder, category)

        if not os.path.exists(destination_folder):
            os.makedirs(destination_folder)

        destination_path = os.path.join(
            destination_folder,
            filename
        )

        shutil.move(file_path, destination_path)

        print(f"Moved {filename} -> {category}/")



"""
============================================
A MISTAKE I MADE (or one I want to avoid)
============================================
One thing I need to be careful about is the file path.
If the program is looking for a folder that does not exist, it
will not be able to find the files and if you're working in a wrong
directory, you might think that it doesnt work but in reality it created a folder
named files already but you cant see it because youre in a wrong directory in vscode.


============================================
HOW THIS CONNECTS TO SOMETHING ELSE
============================================
[optional: how is this similar to what real automation scripts do?
think about your own gradebook/attendance workflow — could something
like this save you time there?]
"""
