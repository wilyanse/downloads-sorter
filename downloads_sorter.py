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

# Configure logging to log both errors and info messages
logging.basicConfig(level=logging.INFO)

# Create a file handler to save log messages to the error_log.txt file
log_file = "script_log.txt"
log_handler = logging.FileHandler(log_file, delay=True)
log_handler.setLevel(logging.INFO)  # Only log messages with ERROR level or above
log_format = logging.Formatter("%(asctime)s [%(levelname)s] %(message)s")
log_handler.setFormatter(log_format)

# Add the file handler to the root logger
logging.getLogger().addHandler(log_handler)

# Check if the download folder exists
if not os.path.exists(download_folder):
    logging.error(f"The download folder '{download_folder}' does not exist.")
    exit(1)

# Check if the destination folder exists;
# Sorts the files in the download folder if it does not
if not os.path.exists(destination_folder):
    logging.INFO(f"The destination folder does not exist, files will be sorted in the download folder instead")
    destination_folder = download_folder

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
        logging.info(f"File '{filename}' was moved into '{destination_folder}'.")


Categorize_Move(download_folder, destination_folder)
