import pygame
from assets.assetManager import load_font
from common import Scene

class MainMenuScene:
    def __init__(self):
        self.bg_colour = (20, 20, 20)
        self.fg_colour = (0, 0, 30)
        self.gamename1_text_value = "Dungeons"
        self.gamename2_text_value = "Of"
        self.gamename3_text_value = "Jongunpo"
        self.start_text_value = "Enter"
        self.quit_text_value = "quit"
        self.gamename_font = load_font('PixelScript', 50)
        self.start_font = load_font('PixelScript', 30)
        self.quit_font = load_font('PixelScript', 20)
        self.select = True

        self.gamename1_text = self.gamename_font.render(self.gamename1_text_value,1,(200,100,100))
        self.gamename2_text = self.gamename_font.render(self.gamename2_text_value,1,(200,100,100))
        self.gamename3_text = self.gamename_font.render(self.gamename3_text_value,1,(200,100,100))
        self.start_text = self.start_font.render(self.start_text_value,1,(200,200,200))
        self.quit_text = self.quit_font.render(self.quit_text_value,1,(200,200,200))

    def handle_input(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key in [pygame.K_DOWN , pygame.K_UP, pygame.K_j , pygame.K_k]:
                self.select = not self.select
            if event.key == pygame.K_RETURN:
                if self.select == True:
                    return Scene.MAP
                else:
                    return "quit"

    def update(self):
        pass

    def render(self,screen):
        screen.fill(self.bg_colour)
        screen.blit(self.gamename1_text,(80,10))
        screen.blit(self.gamename2_text,(160,75))
        screen.blit(self.gamename3_text,(180,150))
        if self.select == True:
            self.start_text = self.start_font.render(self.start_text_value,1,(250,250,100))
            self.quit_text = self.quit_font.render(self.quit_text_value,1,(200,200,200))
        else:
            self.start_text = self.start_font.render(self.start_text_value,1,(200,200,200))
            self.quit_text = self.quit_font.render(self.quit_text_value,1,(250,250,100))
        screen.blit(self.start_text,(210,290))
        screen.blit(self.quit_text,(210,390))
