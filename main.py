# Imports

import os
import functions

# Paths

folder_opening = 'images/original'
folder_saving = 'images/final'

functions.path.check_path(folder_opening)
functions.path.check_path(folder_saving)

# User instructions

language = functions.instructions.choose_language()
functions.instructions.folder_instructions(language)

# Find files

files = os.listdir(folder_opening)

# Convertion

functions.convert.convert_to_jpeg(files, folder_opening, folder_saving)

# The end

functions.instructions.ending(language)
