from .maps import Map

class MapFactory:
    
    def __init__(self):
        return
        
    def new_map(self, n_paths, n_points, scale=1.0):
        return Map(n_paths, n_points, scale)