import pygame
from enum import Enum
from maps.mapFactory import MapFactory

pygame.init()
pygame.font.init()

screen = pygame.display.set_mode([500, 500], pygame.RESIZABLE)

mapFactory = MapFactory()
current_map = mapFactory.new_map(5, 50, 2)

running = True
debugmenu = False

class gamescene(Enum):
    INTRO = 0
    MAP = 1
    ROOM = 2
    BATTLE = 3
    END = 4
    CREDITS = 5
    M = 6

# init
scene = gamescene.INTRO
bg_colour = (30, 30, 30)
fg_colour = (0, 0, 30)

#init scenes
while running:
    #Handle Input
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if debugmenu == True:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    debugmenu = False
                if  event.key == pygame.K_q:
                    running = False
        else:
            if event.mod and pygame.KMOD_SHIFT and event.key == pygame.K_COLON or event.key == pygame.K_SEMICOLON:
                debugmenu = True
            match(scene):
                case scene.INTRO:
                    if event.key == pygame.K_RIGHTBRACKET:
                        scene = gamescene.MAP
                case scene.MAP:
                    if event.key == pygame.K_RIGHTBRACKET:
                        scene = gamescene.ROOM
                case scene.ROOM:
                    if event.key == pygame.K_RIGHTBRACKET:
                        scene = gamescene.BATTLE
                case scene.BATTLE:
                    if event.key == pygame.K_RIGHTBRACKET:
                        scene = gamescene.END
                case scene.END:
                    if event.key == pygame.K_RIGHTBRACKET:
                        scene = gamescene.CREDITS
                case scene.CREDITS:
                    if event.key == pygame.K_RIGHTBRACKET:
                        scene = gamescene.M
                case scene.M:
                    if event.key == pygame.K_RIGHTBRACKET:
                        scene = gamescene.INTRO
        
    
    #Handle GameLogic Updates:
        #Non existant, no time basedupdates here

    #Renders/views
    match(scene):
        case scene.INTRO:
            logo_font = pygame.font.Font('./PixelScript.ttf', 20)
            logo_text = logo_font.render("Luko Games",1,(200,200,200))
            screen.fill(bg_colour)
            pygame.draw.circle(screen, (150, 120, 0), (250, 250),75)
            pygame.draw.circle(screen, bg_colour, (225, 250),55)
            screen.blit(logo_text,(255,250))
        case gamescene.MAP:
            screen.fill(bg_colour)
            current_map.render(screen)
        case gamescene.ROOM:
            screen.fill(bg_colour)
            hello_font = pygame.font.Font('./PixelScript.ttf', 20)
            hello_text = hello_font.render("Room Test",1,(200,200,200))
            pygame.draw.rect(screen, (0, 0, 255), (250, 450,250,250),75)
            screen.blit(hello_text,(250,150))
        case gamescene.BATTLE:
            screen.fill(bg_colour)
            hello_font = pygame.font.Font('./PixelScript.ttf', 20)
            hello_text = hello_font.render("Battle",1,(200,200,200))
            pygame.draw.rect(screen, (0, 0, 255), (250, 450,250,250),75)
            screen.blit(hello_text,(250,150))
        case gamescene.END:
            screen.fill(bg_colour)
            hello_font = pygame.font.Font('./PixelScript.ttf', 20)
            hello_text = hello_font.render("You LOSE....   WIN",1,(200,200,200))
            pygame.draw.rect(screen, (0, 0, 255), (250, 450,250,250),75)
            screen.blit(hello_text,(250,150))
        case gamescene.CREDITS:
            screen.fill(bg_colour)
            hello_font = pygame.font.Font('./PixelScript.ttf', 20)
            hello_text = hello_font.render("By Luna & Miko",1,(200,200,200))
            pygame.draw.rect(screen, (0, 0, 255), (250, 450,250,250),75)
            screen.blit(hello_text,(250,150))
        case gamescene.M:
            screen.fill(bg_colour)
            hello_font = pygame.font.Font('./PixelScript.ttf', 20)
            hello_text = hello_font.render("M",1,(200,200,200))
            pygame.draw.rect(screen, (0, 0, 255), (250, 450,250,250),75)
            screen.blit(hello_text,(250,150))

    if debugmenu == True:
        debug_font = pygame.font.Font('./PixelScript.ttf', 20)
        debug_text = debug_font.render("Command > ",1,(200,200,200))
        pygame.draw.rect(screen, (0, 0, 255), (250, 450,250,250),75)
        screen.blit(debug_text,(250,450))
    pygame.display.flip()

pygame.quit()
