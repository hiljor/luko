import pygame
import moviepy.editor as mpy
import os

asset_dirs = ['game/assets', 'assets']

asset_type_folder = {
    'font': 'fonts',
    'image': 'images',
    'audio': 'audio',
    'video': 'video',
    'script': 'scripts',
    'data': 'data',
    'other': 'other'
}

accepted_extensions = {
    'font': ['.ttf'],
    'image': ['.png', '.jpg', '.jpeg', '.gif', '.bmp'],
    'audio': ['.wav', '.mp3', '.ogg'],
    'video': ['.mp4', '.avi', '.mkv', '.webm'],
    'script': ['.py', '.js', '.lua', '.cs', '.cpp', '.c', '.h', '.hpp'],
    'data': ['.json', '.xml', '.csv', '.tsv', '.yaml', '.yml', '.ini', '.cfg', '.conf', '.txt'],
    'other': []
}

asset_loader = {
    'font': pygame.font.Font,
    'image': pygame.image.load,
    'audio': pygame.mixer.Sound,
    'video': mpy.VideoFileClip,
    'script': open,
    'data': open,
    'other': open
}

def _load_object(filename: str, file_type, *args):
    extensions = accepted_extensions[file_type]
    folder = asset_type_folder[file_type]
    
    # If file has no extension
    if '.' not in filename:
        # Check if the filename exists with an accepted extension
        for ext in extensions:
            new_filename = filename + ext
            for asset_dir in asset_dirs:
                path = os.path.join(asset_dir, folder, new_filename)
                if os.path.exists(path):
                    return asset_loader[file_type](path, *args)
        raise FileNotFoundError(f"File '{filename}' of type '{file_type}' was not found in the asset directory with any of the accepted extensions: {extensions}")
    
    # If the filename already has an accepted extension, return it
    elif filename.endswith(tuple(extensions)):
        for asset_dir in asset_dirs:
            path = os.path.join(asset_dir, folder, filename)
            if os.path.exists(path):
                return asset_loader[file_type](path, *args)
        raise FileNotFoundError(f"File '{filename}' of type '{file_type}' was not found in the asset directory with the accepted extension: {extensions}")
    
    # If the filename has an extension but it's not accepted
    else:
        raise ValueError(f"File '{filename}' of type {file_type} was not accepted due to its extension. Valid extensions are {extensions}")

def load_font(filename, size=20):
    return _load_object(filename, 'font', size)
    
def load_image(filename):
    return _load_object(filename, 'image')

def load_audio(filename):
    return _load_object(filename, 'audio')

def load_video(filename):
    return _load_object(filename, 'video')

def load_script(filename):
    return _load_object(filename, 'script')

def load_data(filename):
    return _load_object(filename, 'data')