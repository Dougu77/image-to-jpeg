# Imports

import os
from functions import *

# User instructions

functions.instructions.folder_instructions()

# Paths

folder_opening = 'images/original'
folder_saving = 'images/final'

# Loop

while True:
    
    # Check paths
    
    functions.path.check_path(folder_opening)
    functions.path.check_path(folder_saving)
    
    # Check images
    
    functions.instructions.ask_ok()

    # Find files

    files = os.listdir(folder_opening)

    # Convertion

    functions.convert.convert_to_jpeg(files, folder_opening, folder_saving)

    # Convert again

    again = functions.instructions.convert_again()
    if not again: break
    
    # Write line
    
    functions.instructions.write_line()
