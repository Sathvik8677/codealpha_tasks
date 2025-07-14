import os
import shutil

# 🔁 Replace these paths with the actual full paths on your system
source = "source_folder_path"          # Example: "C:/Users/YourName/Downloads"
destination = "destination_folder_path"  # Example: "C:/Users/YourName/Pictures/JPGs"

# 📂 Create destination folder if it doesn't exist
if not os.path.exists(destination):
    os.makedirs(destination)

# 📁 Move all .jpg files from source to destination
for file in os.listdir(source):
    if file.endswith(".jpg"):
        shutil.move(os.path.join(source, file), os.path.join(destination, file))

print("✅ All .jpg files moved successfully.")
