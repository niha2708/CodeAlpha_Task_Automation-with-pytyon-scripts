import os
import shutil

# Define the directory to organize
DIRECTORY_TO_ORGANIZE = "E:\python"  # Replace with your directory path

# Define the mapping of file extensions to folders
FILE_TYPE_FOLDERS = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".svg"],
    "Documents": [".pdf", ".docx", ".txt", ".pptx", ".xlsx"],
    "Videos": [".mp4", ".mov", ".avi", ".mkv"],
    "Music": [".mp3", ".wav", ".aac", ".flac"],
    "Archives": [".zip", ".rar", ".7z", ".tar", ".gz"],
    "Code": [".py", ".java", ".js", ".html", ".css"],
    "Others": []
}

def organize_files(directory):
    # Check if the directory exists
    if not os.path.exists(directory):
        print(f"The directory '{directory}' does not exist.")
        return

    # Create subfolders if they don't exist
    for folder in FILE_TYPE_FOLDERS.keys():
        folder_path = os.path.join(directory, folder)
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)

    # Iterate through files in the directory
    for file_name in os.listdir(directory):
        file_path = os.path.join(directory, file_name)

        # Skip directories
        if os.path.isdir(file_path):
            continue

        # Move files to the appropriate folder
        moved = False
        for folder, extensions in FILE_TYPE_FOLDERS.items():
            if file_name.lower().endswith(tuple(extensions)):
                shutil.move(file_path, os.path.join(directory, folder, file_name))
                moved = True
                print(f"Moved '{file_name}' to '{folder}'")
                break

        # Move files without a defined type to the "Others" folder
        if not moved:
            shutil.move(file_path, os.path.join(directory, "Others", file_name))
            print(f"Moved '{file_name}' to 'Others'")

    print("File organization complete!")

# Run the organizer
if __name__ == "__main__":
    organize_files(DIRECTORY_TO_ORGANIZE)
