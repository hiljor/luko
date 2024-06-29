import pygame
from maps.mapFactory import MapFactory

pygame.init()
screen = pygame.display.set_mode([500, 500])

mapFactory = MapFactory()
current_map = mapFactory.new_map(5, 50, 2)

running = True
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


    #MainGameLoop?
    #   Intro Screen        }  We can probably
    #   Create Character    }  Ignore these
    #   StartLocationEvent  }  for now
    #   Map Screen
    #       -> LocationEvent
    #           -> CheckPlayHealth/Sanity
    #               -> Show Death Screen
    #               -> Save Death

    screen.fill((255, 255, 255))
    current_map.render(screen)
    pygame.draw.circle(screen, (0, 0, 255), (250, 250),75)
    pygame.display.flip()

pygame.quit()