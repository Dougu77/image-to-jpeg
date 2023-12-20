# Import

import os

# Function

def find_files(opening_folder):
    files = []
    for root, dirs, filenames in os.walk(opening_folder):
        for filename in filenames:
            if any(filename.endswith(ext) for ext in ['.png', '.jpg', '.jpeg', '.webp']):
                files.append(os.path.join(root, filename))
    return files
