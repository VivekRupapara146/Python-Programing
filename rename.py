import os

old_name = "python.txt"
new_name = "renamed_python.txt"

os.rename(old_name, new_name)

print(f"Renamed '{old_name}' to '{new_name}'")

os.rename(new_name, old_name)

print(f"Renamed '{new_name}' to '{old_name}'")
