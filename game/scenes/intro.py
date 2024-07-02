import pygame

class IntroScene:
    def __init__(self):
        self.bg_colour = (30, 30, 30)
        self.fg_colour = (0, 0, 30)

    def handle_input(self, event):
        pass

    def update(self):
        pass

    def render(self, screen):
        logo_font = pygame.font.Font('./PixelScript.ttf', 40)
        logo_text = logo_font.render("Luko Games",1,(200,200,200))
        screen.fill(self.bg_colour)
        pygame.draw.circle(screen, (100, 150, 230), (198, 196),78)
        pygame.draw.circle(screen, (200, 200, 150), (198, 198),77)
        pygame.draw.circle(screen, (200, 200, 150), (200, 200),75)
        pygame.draw.circle(screen, self.bg_colour, (175, 194),58)
        screen.blit(logo_text,(205,400))
