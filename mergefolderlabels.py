import os
import shutil

# List of folder names
folders = [
    "Missing_hole",
    "Mouse_bite",
    "Open_circuit",
    "Short",
    "Spur",
    "Spurious_copper"
]

# Create a folder to store all the JPG files
output_folder = "allpcbfaulthh"
os.makedirs(output_folder, exist_ok=True)

# Iterate over each folder
for folder in folders:
    # Path to the current folder
    folder_path = os.path.join(os.getcwd(), folder)
    
    # Get a list of all JPG files in the current folder
    file_list = [f for f in os.listdir(folder_path) if f.endswith(".xml")]
    
    # Move each JPG file to the output folder
    for file_name in file_list:
        src = os.path.join(folder_path, file_name)
        dst = os.path.join(output_folder, file_name)
        shutil.copy2(src, dst)
        print(f"Moved {file_name} to {output_folder}")

print("All JPG files copied successfully!")

