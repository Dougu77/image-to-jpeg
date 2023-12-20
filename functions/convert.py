# Imports

import os
from PIL import Image

# Functions

def convert_to_jpeg(files, saving_folder):
    for file in files:
        if any(file.endswith(ext) for ext in ['.png', '.jpg', '.jpeg', '.webp']):
            path_opening = os.path.normpath(file)
            img = Image.open(path_opening).convert('RGBA')
            if has_transparent_borders(img):
                white_img = Image.new('RGBA', img.size, (255, 255, 255, 255))
                white_img.paste(img, (0, 0), img)
                rgb_img = white_img.convert('RGB')
            else:
                rgb_img = img.convert('RGB')
            relative_path = os.path.relpath(file, 'images/original')
            chapter_number = relative_path.split(os.path.sep)[0]
            output_path = os.path.join(saving_folder, chapter_number)
            os.makedirs(output_path, exist_ok=True)
            filename = os.path.basename(file)
            rgb_img.save(os.path.join(output_path, os.path.splitext(filename)[0] + '.jpeg'), 'JPEG')

def has_transparent_borders(img):
    alpha = img.split()[3]
    return any(alpha.getpixel((x, 0)) == 0 for x in range(img.width)) or \
           any(alpha.getpixel((x, img.height - 1)) == 0 for x in range(img.width)) or \
           any(alpha.getpixel((0, y)) == 0 for y in range(img.height)) or \
           any(alpha.getpixel((img.width - 1, y)) == 0 for y in range(img.height))
