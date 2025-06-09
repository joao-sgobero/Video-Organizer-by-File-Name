import os
import shutil

# Get the path of the folder where the script is being executed
current_folder = os.getcwd()

# Display the current folder path
print(f"Current folder: {current_folder}")

# Iterate through all files in the current folder
files_found = False  # Check if there are files
for file_name in os.listdir(current_folder):
    print(f"Checking file: {file_name}")
    
    # Check if it's a video file (with extensions like .mp4, .avi, .mkv, .mov, .ts)
    if file_name.endswith(('.mp4', '.avi', '.mkv', '.mov', '.ts')):
        files_found = True  # Video file found
        # Get the file name without the extension
        folder_name = os.path.splitext(file_name)[0]
        
        # Complete path of the new folder to be created
        new_folder_path = os.path.join(current_folder, folder_name)
        
        # Create the folder with the video name, if it doesn't exist yet
        if not os.path.exists(new_folder_path):
            os.makedirs(new_folder_path)
            print(f"Folder '{folder_name}' created.")
        
        # Complete path of the original video
        video_path = os.path.join(current_folder, file_name)
        
        # Move the video to the newly created folder
        shutil.move(video_path, os.path.join(new_folder_path, file_name))
        print(f"Video '{file_name}' moved to the folder '{folder_name}'.")

# If no videos were found
if not files_found:
    print("No video files were found in the folder.")
    
print("Process completed.")
