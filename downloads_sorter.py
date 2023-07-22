import os
import shutil
import logging

# Define file type categories and their corresponding folders
file_types = {
    "Documents": ["doc", "docx", "txt", "pdf"],
    "ProgramFiles": ["exe", "msi"],
    "ZipsAndFolders": ["zip", "rar", "tar", "gz"],
    "Images": ["jpg", "png", "gif"],
    "Others": []  # Add other file types above this line
}

# Define source and destination folders
download_folder = r"C:\Users\Admin\Downloads"
destination_folder = r"E:\Downloads"

# Iterate through files in the download folder
def Categorize_Move(download_folder, destination_folder):
    for filename in os.listdir(download_folder):
        src_file = os.path.join(download_folder, filename)

        # Determine the file type based on the extension
        file_ext = os.path.splitext(filename)[1][1:].lower()
        file_category = None

        # Find the category for the file type
        for category, extensions in file_types.items():
            if file_ext in extensions:
                file_category = category
                break

        # If the file type is not recognized, put it in the "Others" folder
        if file_category is None:
            file_category = "Others"

        # add case for folders
        if os.path.isdir(src_file):
            file_category = "ZipsAndFolders" 
        
        # Create the destination folder if it doesn't exist
        dest_folder = os.path.join(destination_folder, file_category)
        os.makedirs(dest_folder, exist_ok=True)

        dest_file = os.path.join(dest_folder, filename)
        shutil.move(src_file, dest_file)


Categorize_Move(download_folder, destination_folder)
