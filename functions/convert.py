# Imports

import os
from PIL import Image

# Function

def convert_to_jpeg(files, folder_opening, folder_saving):
    for file in files:
        if any(file.endswith(ext) for ext in ['.png', '.jpg', '.jpeg', '.webp']):
            path_opening = os.path.join(folder_opening, file)
            img = Image.open(path_opening).convert('RGB')
            filename = os.path.join(folder_saving, os.path.splitext(file)[0])
            img.save(filename + '.jpeg', 'JPEG')
