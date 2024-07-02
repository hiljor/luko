import pygame
from fonts.fontManager import load_font

class MainMenuScene:
    def __init__(self):
        self.bg_colour = (30, 30, 30)
        self.fg_colour = (0, 0, 30)
        self.gamename1_text_value = "Dungeons"
        self.gamename2_text_value = "Of"
        self.gamename3_text_value = "Jongunpo"
        self.start_text_value = "Enter"
        self.quit_text_value = "quit"
        self.gamename_font = load_font('PixelScript', 50)
        self.start_font = load_font('PixelScript', 30)
        self.quit_font = load_font('PixelScript', 20)

        self.gamename1_text = self.gamename_font.render(self.gamename1_text_value,1,(200,200,200))
        self.gamename2_text = self.gamename_font.render(self.gamename2_text_value,1,(200,200,200))
        self.gamename3_text = self.gamename_font.render(self.gamename3_text_value,1,(200,200,200))
        self.start_text = self.start_font.render(self.start_text_value,1,(200,200,200))
        self.quit_text = self.quit_font.render(self.quit_text_value,1,(200,200,200))

    def handle_input(self, event):
        pass

    def update(self):
        pass

    def render(self,screen):
        screen.fill(self.bg_colour)
        screen.blit(self.gamename1_text,(70,10))
        screen.blit(self.gamename2_text,(150,70))
        screen.blit(self.gamename3_text,(170,140))
        screen.blit(self.start_text,(200,250))
        screen.blit(self.quit_text,(200,350))
