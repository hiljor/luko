import pygame
from assets.assetManager import load_font

class HandWidget:
    def __init__(self):
        self.size = 200 #1x2
        self.colour = (0,0,0)
        self.font = load_font('PixelScript', 20)
        self.text = self.font.render("",1,(200,200,200))
        self.hidden = True
        self.x = 0
        self.y = 0

    def setName(self, text_value):
        self.text = self.font.render(text_value,1,(200,200,200))
        return self
    def setPos(self, x, y):
        self.x = x
        self.y = y
        return self
    def setSize(self, size):
        self.size = size
        return self
    def setColour(self, colour):
        self.colour = colour
        return self
    def create(self):
        self.hidden = False
        return self

    def destroy(self):
        self.hidden = True

    def render(self, screen):
        pygame.draw.rect(screen, self.colour,(self.x,self.y,(4*self.size)+10,(self.size*2)+10))
        screen.blit(self.text,(self.x+1,self.y))
