import pygame
from fonts.fontManager import load_font

class MScene:
    def __init__(self):
        self.bg_colour = (30, 30, 30)
        self.fg_colour = (0, 0, 30)
        self.hello_font = load_font('PixelScript', 20)
        self.hello_text = self.hello_font.render("Hidden M",1,(200,200,200))

    def handle_input(self, event):
        pass

    def update(self):
        pass

    def render(self,screen):
        screen.fill(self.bg_colour)
        screen.blit(self.hello_text,(200,300))
