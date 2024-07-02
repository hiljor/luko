import pygame
import os

def load_font(filename, size):
    # Ensure the filename ends with '.ttf'
    if not filename.endswith('.ttf'):
        filename += '.ttf'
    
    # Defining possible paths to check for the font file.
    paths_to_check = [
        filename,                           # Current directory
        os.path.join('game', filename),     # Game directory
        os.path.join('game', 'fonts', filename),  # Fonts directory inside the game directory
        os.path.join('fonts', filename),    # Fonts directory in the root directory
    ]
    
    # Loop through each path in the list and check if the font file exists
    for path in paths_to_check:
        if os.path.isfile(path):
            return pygame.font.Font(path, size)
    
    # If the font file is not found, raise an exception
    raise FileNotFoundError(f"Font file '{filename}' not found in the following paths: {paths_to_check}")