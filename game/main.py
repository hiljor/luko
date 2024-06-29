import pygame

pygame.init()
screen = pygame.display.set_mode([500, 500])

running = True
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


    #GameLoop?
    #   Intro Screen
    #   Create Character
    #   StartLocationEvent
    #   Map Screen
    #       -> LocationEvent
    #           -> CheckPlayHealth/Sanity
    #               -> Show Death Screen
    #               -> Save Death

    screen.fill((255, 255, 255))
    pygame.draw.circle(screen, (0, 0, 255), (250, 250),75)
    pygame.display.flip()

pygame.quit()      
