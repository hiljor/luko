import pygame
from fonts.fontManager import load_font
from common import Scene

class IntroScene:
    def __init__(self):
        self.bg_colour = (30, 30, 30)
        self.fg_colour = (0, 0, 30)
        self.playaudio = 0
        self.audio = pygame.mixer.Sound("./audio/placeholder_song-ko.wav")
        self.audio.set_volume(0.7)
        self.clock = pygame.time.get_ticks()
        
    def init(self):
        self.playaudio = 0

    def handle_input(self, event):
        pass

    def update(self):
        if self.playaudio == 0:
            self.clock = pygame.time.get_ticks()
            self.audio.play()
            self.playaudio = 1

        print(pygame.time.get_ticks())
        if pygame.time.get_ticks() - self.clock > 5500:
            return Scene.MAINMENU


    def render(self, screen):
        logo_font = load_font('PixelScript', 40)
        logo_text = logo_font.render("Luko Games",1,(200,200,200))
        screen.fill(self.bg_colour)
        pygame.draw.circle(screen, (100, 150, 230), (198, 196),78)
        pygame.draw.circle(screen, (200, 200, 150), (198, 198),77)
        pygame.draw.circle(screen, (200, 200, 150), (200, 200),75)
        pygame.draw.circle(screen, self.bg_colour, (175, 194),58)
        screen.blit(logo_text,(205,400))
