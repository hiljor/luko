from .mapGenerator import generate_map
from .room import RoomFactory
import pygame
import numpy as np

class Map:
    
    def __init__(self, rows, cols, n_paths):
        self.rows = rows
        self.cols = cols
        self.n_paths = n_paths
        
        self.points, self.edges, self.neighbours, self.starts, self.end = generate_map(10, 8, 5)
        
        self.rooms = {}
        
        self.current = None
        self.nexts = sorted(self.starts)
        self.path = []
        self.selected = self.starts[0]
        
    def _generate_rooms(self):
        rf = RoomFactory()
        for i in range(len(self.points)):
            self.rooms[i] = rf.newRoom()
            # add boss room at end point location
            if self.points[i] == self.end:
                self.rooms[i] = rf.newRoom('boss')
            # add start room at start point location
            if self.points[i] in self.starts:
                self.rooms[i] = rf.newRoom('start')
    
    def choose_location(self):
        self.path.append(self.selected)
        self.current = self.selected
        if self.current == self.end:
            return
        self.selected = self.neighbours[self.current][0]
        self.nexts = sorted(self.neighbours[self.current])
        
        # return event for room
        return self.rooms[self.points.index(self.current)].getEvent()
        
    def swap_selected_location(self, direction):
        index = self.nexts.index(self.selected)
        index = (index + direction + len(self.nexts)) % len(self.nexts)
        self.selected = self.nexts[index]
        
    
    def render(self, screen):
        width = screen.get_width() - 100  # Subtracting buffer from total width
        height = screen.get_height() - 100  # Subtracting buffer from total height

        buffer = 50  # Buffer offset for initial point

        # Calculate grid dimensions with buffer
        grid_width = width + buffer
        grid_height = height + buffer

        # Draw all paths between points
        for edge in self.edges:
            pygame.draw.line(screen, (255, 255, 255),
                            (buffer + edge[0][1] * grid_height / self.rows, buffer + edge[0][0] * grid_width / self.cols),
                            (buffer + edge[1][1] * grid_height / self.rows, buffer + edge[1][0] * grid_width / self.cols))

        # Draw the current path
        for i in range(len(self.path) - 1):
            pygame.draw.line(screen, (255, 0, 0),
                            (buffer + self.path[i][1] * grid_height / self.rows, buffer + self.path[i][0] * grid_width / self.cols),
                            (buffer + self.path[i + 1][1] * grid_height / self.rows, buffer + self.path[i + 1][0] * grid_width / self.cols))

        # Draw all points
        for point in self.points:
            pygame.draw.circle(screen, (255, 255, 255),
                            (buffer + int(point[1] * grid_height / self.rows), buffer + int(point[0] * grid_width / self.cols)), 5)

        # Highlight current location
        if self.current is not None:
            pygame.draw.circle(screen, (255, 0, 0),
                            (buffer + int(self.current[1] * grid_height / self.rows), buffer + int(self.current[0] * grid_width / self.cols)), 10, 3)

        # Highlight neighbors
        if self.current is not None:
            for neighbour in self.neighbours[self.current]:
                color = (255, 255, 0) if neighbour == self.selected else (255, 255, 255)
                pygame.draw.circle(screen, color,
                                (buffer + int(neighbour[1] * grid_height / self.rows), buffer + int(neighbour[0] * grid_width / self.cols)), 10, 3)
        else:
            for start in self.starts:
                color = (255, 255, 0) if start == self.selected else (255, 255, 255)
                pygame.draw.circle(screen, color,
                                (buffer + int(start[1] * grid_height / self.rows), buffer + int(start[0] * grid_width / self.cols)), 10, 3)
                    
            

class MapFactory:
    
    def __init__(self):
        return
        
    def new_map(self, rows, cols, n_paths):
        return Map(rows, cols, n_paths)