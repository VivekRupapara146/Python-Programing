import os

# Specify the directory you want to list (use "." for current directory)
directory_path = "."

try:
    # Get the list of all files and directories
    contents = os.listdir(directory_path)
    
    print(f"Contents of directory '{directory_path}':")
    for item in contents:
        print(item)
except FileNotFoundError:
    print(f"The directory '{directory_path}' was not found.")
except PermissionError:
    print(f"Permission denied to access '{directory_path}'.")
