import pygame
from fonts.fontManager import load_font
from common import Scene

class IntroScene:
    def __init__(self):
        self.bg_colour = (20, 20, 20)
        self.fg_colour = (0, 0, 30)
        self.playaudio = 0
        self.audio = pygame.mixer.Sound("./audio/placeholder_song-ko.wav")
        self.audio.set_volume(0.7)
        self.clock = pygame.time.get_ticks()
        self.logo_font = load_font('PixelScript', 40)
        self.logo_text1 = self.logo_font.render("Lu",1,(200,200,200))
        self.logo_text2 = self.logo_font.render("Luko",1,(200,200,200))
        self.logo_text3 = self.logo_font.render("Luko Game",1,(200,200,200))
        self.logo_text4 = self.logo_font.render("Luko Games Studio",1,(200,200,200))
        self.frame = 0
        
    def handle_input(self, event):
        pass

    def update(self):
        if self.playaudio == 0:
            self.clock = pygame.time.get_ticks()
            self.audio.play()
            self.playaudio = 1

        print(pygame.time.get_ticks())
        if self.frame == 0 and pygame.time.get_ticks() - self.clock > 300:
            self.frame = 1
        if self.frame == 1 and pygame.time.get_ticks() - self.clock > 2400:
            self.frame = 2
        if self.frame == 2 and pygame.time.get_ticks() - self.clock > 2700:
            self.frame = 3
        if self.frame == 3 and pygame.time.get_ticks() - self.clock > 2900:
            self.frame = 4
        if self.frame == 4 and pygame.time.get_ticks() - self.clock > 3100:
            self.frame = 5
        if self.frame == 5 and pygame.time.get_ticks() - self.clock > 4000:
            self.frame = 6


        if pygame.time.get_ticks() - self.clock > 5500:
            return Scene.MAINMENU


    def render(self, screen):
        screen.fill(self.bg_colour)
        if self.frame == 1:
            pygame.draw.circle(screen, (100, 150, 230), (208, 196),78)
            pygame.draw.circle(screen, (200, 200, 150), (208, 198),77)
            pygame.draw.circle(screen, (200, 200, 150), (210, 200),75)
        if self.frame == 2:
            pygame.draw.circle(screen, (100, 150, 230), (208, 196),78)
            pygame.draw.circle(screen, (200, 200, 150), (208, 198),77)
            pygame.draw.circle(screen, (200, 200, 150), (210, 200),75)
            screen.blit(self.logo_text1,(55,300))
        if self.frame == 3:
            pygame.draw.circle(screen, (100, 150, 230), (208, 196),78)
            pygame.draw.circle(screen, (200, 200, 150), (208, 198),77)
            pygame.draw.circle(screen, (200, 200, 150), (210, 200),75)
            screen.blit(self.logo_text2,(55,300))
        if self.frame == 4:
            pygame.draw.circle(screen, (100, 150, 230), (208, 196),78)
            pygame.draw.circle(screen, (200, 200, 150), (208, 198),77)
            pygame.draw.circle(screen, (200, 200, 150), (210, 200),75)
            screen.blit(self.logo_text3,(55,300))
        if self.frame == 5:
            pygame.draw.circle(screen, (100, 150, 230), (208, 196),78)
            pygame.draw.circle(screen, (200, 200, 150), (208, 198),77)
            pygame.draw.circle(screen, (200, 200, 150), (210, 200),75)
            screen.blit(self.logo_text4,(55,300))
        if self.frame == 6:
            pygame.draw.circle(screen, (100, 150, 230), (208, 196),78)
            pygame.draw.circle(screen, (200, 200, 150), (208, 198),77)
            pygame.draw.circle(screen, (200, 200, 150), (210, 200),75)
            screen.blit(self.logo_text4,(55,300))
            pygame.draw.circle(screen, self.bg_colour, (185, 194),58)

