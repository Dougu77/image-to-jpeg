# Import

import os

# Function

def check_path(path):
    if not os.path.exists(path):
        os.makedirs(path)
