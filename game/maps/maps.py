from builder import generateMap
import roomFactory
import pygame

class Map:
    
    def __init__(self, n_paths, n_points, scale=1.0):
        self.n_paths = n_paths
        self.n_points = n_points
        self.scale = scale
        
        graph, points, _, start, end = generateMap(n_points, n_paths)
        
        self.rooms = {}
        
        self.graph = graph
        self.points = points
        self.path = [start]
        self.start = start
        self.end = end
        self.current = start
        
    def _generate_rooms(self):
        f = roomFactory()
        for i in range(len(self.points)):
            self.rooms[i] = f.newRoom()
        
    
    def get_current_location(self):
        return self.points[self.current] * self.scale
    
    def get_all_rooms(self):
        return [(i, self.points[i] * self.scale, self.rooms[i]) for i in range(len(self.points))]
    
    def get_path_points(self):
        return [self.points[i] * self.scale for i in self.path]
    
    def get_end_location(self):
        return self.points[self.end] * self.scale
    
    def get_start_location(self):
        return self.points[self.start] * self.scale
    
    def get_next_locations(self):
        return [(i, self.points[i] * self.scale) for i in self.graph[self.current]]
    
    def choose_next_location(self, next_location):
        if next_location in self.graph[self.current]:
            self.path.append(next_location)
            self.current = next_location
            return True
        return False
    
    def render(self, screen):
        for i in range(len(self.points)):
            pygame.draw.circle(screen, (0, 0, 0), self.points[i] * self.scale, 5)
        
        for i in range(len(self.path) - 1):
            pygame.draw.line(screen, (0, 0, 0), self.points[self.path[i]] * self.scale, self.points[self.path[i+1]] * self.scale, 2)
