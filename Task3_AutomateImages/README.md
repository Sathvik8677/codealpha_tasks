# 🗂️ Task 3: JPG File Automation Script

## 📌 Description
This Python script automates the process of organizing image files by **moving all `.jpg` files** from one folder to another. It helps save time and reduce manual effort for repetitive file management tasks.

## 🧠 Concepts Used
- File and folder operations with `os` and `shutil`
- Looping through directory contents
- Conditional checking based on file extensions

## 🧰 How It Works
1. The user sets a **source folder** and **destination folder**.
2. The script checks for `.jpg` files in the source.
3. It then moves all matching files into the destination folder.

## ⚠️ Note
Before running the script:
- **Replace** `"source_folder_path"` and `"destination_folder_path"` with actual full paths on your system.
- Example:
  ```python
  source = "C:/Users/Sathvik/Downloads"
  destination = "C:/Users/Sathvik/Pictures/JPGs"

How To Run
python move_images.py
