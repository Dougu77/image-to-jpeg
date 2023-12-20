# Imports

import os
from PIL import Image

# Function

def convert_to_jpeg(files, saving_folder):
    for file in files:
        if any(file.endswith(ext) for ext in ['.png', '.jpg', '.jpeg', '.webp']):
            path_opening = os.path.normpath(file)
            img = Image.open(path_opening).convert('RGBA')
            white_img = Image.new('RGBA', img.size, (255, 255, 255, 255))
            white_img.paste(img, (0, 0), img)
            rgb_img = white_img.convert('RGB')
            relative_path = os.path.relpath(file, 'images/original')
            chapter_number = relative_path.split(os.path.sep)[0]
            output_path = os.path.join(saving_folder, chapter_number)
            os.makedirs(output_path, exist_ok=True)
            filename = os.path.basename(file)
            rgb_img.save(os.path.join(output_path, os.path.splitext(filename)[0] + '.jpeg'), 'JPEG')
