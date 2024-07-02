import pygame
from fonts.fontManager import load_font

class CreditScene:
    def __init__(self):
        self.bg_colour = (0,0,0)
        self.hello_font = load_font('PixelScript', 20)
        self.hello_text = self.hello_font.render("By Luna & Miko",1,(200,200,200))

    def handle_input(self, event):
        pass

    def update(self):
        pass

    def render(self, screen):
        screen.fill(self.bg_colour)
        screen.blit(self.hello_text,(200,150))
