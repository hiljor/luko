import pygame

class TemplateScene:
    def __init__(self):
        self.bg_colour = (30, 30, 30)
        self.fg_colour = (0, 0, 30)

    def handle_input(self, event):
        pass

    def update(self):
        pass

    def render(self,screen):

        screen.fill(self.bg_colour)
        pygame.draw.rect(screen, self.fg_colour, (0,0,50,500))
