import os

# Folder where files are located (change if needed)
folder = "."

for filename in os.listdir(folder):
    old_path = os.path.join(folder, filename)

    # Skip directories
    if not os.path.isfile(old_path):
        continue

    name, ext = os.path.splitext(filename)

    # Only process names starting with "Invicon_"
    if name.startswith("Invicon_"):
        # Replace prefix and convert to lowercase
        new_name = name.replace("Invicon_", "minecraft_").lower()
        new_filename = new_name + ext

        new_path = os.path.join(folder, new_filename)
        os.rename(old_path, new_path)
        print(f"Renamed: {filename} -> {new_filename}")

print("Done!")
