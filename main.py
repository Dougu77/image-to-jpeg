# Imports

import os
from functions import *

# User instructions

functions.instructions.folder_instructions()

# Paths

opening_folder = 'images/original'
saving_folder = 'images/final'

# Loop

while True:
    
    # Check paths
    
    functions.path.check_path(opening_folder)
    functions.path.check_path(saving_folder)
    
    # Check images
    
    functions.instructions.ask_ok()

    # Find files
    
    #files = os.listdir(folder_opening)

    files = functions.files.find_files(opening_folder)

    # Convertion

    functions.convert.convert_to_jpeg(files, saving_folder)

    # Convert again

    again = functions.instructions.convert_again()
    if not again: break
    
    # Write line
    
    functions.instructions.write_line()
