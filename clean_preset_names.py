import os

# Path to the "mother" folder
mother_folder_path = '/Develop presets'

# Walk through all subfolders and files
for root, dirs, files in os.walk(mother_folder_path):
    for filename in files:
        if '~~' in filename:
            # Create the new filename by replacing '~~' with an empty string
            new_filename = filename.replace('~~', '')
            
            # Get the full path for the old and new filenames
            old_file = os.path.join(root, filename)
            new_file = os.path.join(root, new_filename)
            
            # Rename the file
            os.rename(old_file, new_file)
            
            print(f'Renamed: {old_file} -> {new_file}')
