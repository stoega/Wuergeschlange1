import os

def print_directory(dir_path: str):
    if not os.path.exists(dir_path):
        print(f"{dir_path} is invalid")
    elif os.path.isfile(dir_path):
        print(f"{dir_path} is a file not a directory")
    elif os.path.isdir(dir_path):
        print_directory_recursively(dir_path, 0)
    else:
        print(f"{dir_path} is invalid")

def print_directory_recursively(dir_path: str, level: int):
    # Print the current directory at the specified level
    if level == 0:
        print(dir_path)
    else:
        print("\t" * level + os.path.basename(dir_path))

    # Get all files and subdirectories in the current directory
    items = os.listdir(dir_path)

    # Iterate through the items
    for item in items:
        item_path = os.path.join(dir_path, item)

        # If the item is a directory
        if os.path.isdir(item_path):
            print_directory_recursively(item_path, level + 1)
        # If the item is a file
        elif os.path.isfile(item_path):
            print("\t" * (level + 1) + os.path.basename(item_path))

# Example usage
print_directory("./a5/d0")
print_directory("D:/JKU/23WS/Python1/Wuergeschlange1/a5/d0")


