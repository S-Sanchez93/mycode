import shutil

# Define the paths
source_file = 'myflask01.py'  # Assuming example.txt is in your current directory
destination_directory = 'two_flasks'  # Specify the destination directory

# Copy the file
shutil.copy(source_file, destination_directory)

print(f"File '{source_file}' copied to '{destination_directory}'")

