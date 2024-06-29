import pygame
from maps.mapFactory import MapFactory

pygame.init()
pygame.font.init()

screen = pygame.display.set_mode([500, 500])

mapFactory = MapFactory()
current_map = mapFactory.new_map(5, 50, 2)

running = True
hidden = True
bg_colour = (30, 30, 30)
fg_colour = (0, 0, 30)
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            hidden = False



    #MainGameLoop?
    #   Intro Screen        }  We can probably
    #   Create Character    }  Ignore these
    #   StartLocationEvent  }  for now
    #   Map Screen
    #       -> LocationEvent
    #           -> CheckPlayHealth/Sanity
    #               -> Show Death Screen
    #               -> Save Death

    screen.fill(bg_colour)
    font = pygame.font.Font('game/PixelScript.ttf', 20)
    logo_text = font.render("Luko Games",1,(200,200,200))
    hello_text = font.render("Hidden",1,(200,200,200))
    current_map.render(screen)
    pygame.draw.circle(screen, (150, 120, 0), (250, 250),75)
    pygame.draw.circle(screen, bg_colour, (225, 250),55)
    screen.blit(logo_text,(255,250))
    if hidden == False:
        pygame.draw.rect(screen, (0, 0, 255), (250, 450),75)
        screen.blit(hello_text,(250,450))

    pygame.display.flip()

pygame.quit()
