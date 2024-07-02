import pygame
from maps.mapFactory import MapFactory

class MapScene:
    def __init__(self):
        self.bg_colour = (30, 30, 30)
        self.fg_colour = (0, 0, 30)
        self.text = "woo"
        self.mapFactory = MapFactory()
        self.current_map = self.mapFactory.new_map(5, 50, 2)

    def handle_input(self, event):
        pass

    def update(self):
        pass

    def render(self, screen):
        screen.fill(self.bg_colour)
        self.current_map.render(screen)
