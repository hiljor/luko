import pygame
from assets.assetManager import load_font

class RoomScene:
    def __init__(self):
        self.text = 'text'
        self.bg_colour = (0,0,0)

    def handle_input(self, event):
        pass

    def update(self):
        pass

    def render(self, screen):
        screen.fill(self.bg_colour)
        hello_font = load_font('PixelScript', 20)
        hello_text = hello_font.render("Room Test",1,(200,200,200))
        pygame.draw.rect(screen, (0, 0, 255), (250, 450,250,250))
        screen.blit(hello_text,(250,150))
