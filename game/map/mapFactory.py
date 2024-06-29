from map import Map

class MapFactory:
    
    def __init__(self):
        return
        
    def newMap(self, n_paths, n_points, scale=1.0):
        return Map(self.n_paths, self.n_points, self.scale)