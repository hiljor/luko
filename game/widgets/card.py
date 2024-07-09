import pygame
from assets.assetManager import load_font

class CardWidget:
    def __init__(self):
        self.size = 80 #1x2
        self.colour = (0,0,0)
        self.colourselect = (200,200,0)
        self.font = load_font('PixelScript', 20)
        self.text_value = ''
        self.text = self.font.render(self.text_value,1,(200,200,200))
        self.text_value
        self.hidden = True
        self.selected = False
        self.x = 0
        self.y = 0

    def with_in(self, pos):
        if pos[0] >= self.x and pos[0] <= self.x + self.size \
            and pos[1] >= self.y and pos[1] <= self.y + (self.size*2):
            return True

        return False 

    def select(self):
        self.selected = not self.selected

    def setName(self, text_value):
        self.text_value = text_value
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
        self.font = load_font('PixelScript', int(self.size/3))
        self.text = self.font.render(self.text_value,1,(200,200,200))
        self.hidden = False
        self.selected = False
        return self

    def destroy(self):
        self.hidden = True

    def render(self, screen):
        if self.selected:
            pygame.draw.rect(screen, self.colourselect,(self.x,self.y,self.size,self.size*2))
        if not self.hidden:
            pygame.draw.rect(screen, self.colour,(self.x+2,self.y+2,self.size-4,self.size*2-4))
            screen.blit(self.text,(self.x+2,self.y+2))
