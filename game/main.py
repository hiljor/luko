import pygame
from maps.mapFactory import MapFactory

pygame.init()
pygame.font.init()

screen = pygame.display.set_mode([500, 500])

mapFactory = MapFactory()
current_map = mapFactory.new_map(5, 50, 2)

running = True
hidden = True
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

    screen.fill((30, 30, 30))
    font = pygame.font.Font('game/PixelScript.ttf', 20)
    hello_text = font.render("Hello, World",1,(200,200,200))
    current_map.render(screen)
    pygame.draw.circle(screen, (0, 0, 255), (250, 250),75)
    pygame.draw.circle(screen, (0, 0, 0), (250, 250),50)
    if hidden == False:
        pygame.draw.circle(screen, (0, 0, 255), (250, 250),75)
        screen.blit(hello_text,(250,250))

    pygame.display.flip()

pygame.quit()
