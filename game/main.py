import pygame
from enum import Enum
from scenemanager import SceneManager

pygame.init()
pygame.font.init()
pygame.mixer.init()

screen = pygame.display.set_mode([500, 500], pygame.RESIZABLE)

running = True
debugmenu = False

scenemanager = SceneManager()

#DEBUG  MENU
debug_pos_x = 150
debug_pos_y = 250
title_debug_font = pygame.font.Font('./PixelScript.ttf', 15)
title_debug_text = title_debug_font.render("Menu",0,(200,200,200))
debug_font = pygame.font.Font('./PixelScript.ttf', 20)
debug_text1 = debug_font.render("q to quit",1,(0,0,0))
debug_text2 = debug_font.render("left bracket previous scene",1,(0,0,0))
debug_text3 = debug_font.render("right bracket scene",1,(0,0,0))

while running:
    #Handle Input
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if debugmenu == True:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    debugmenu = not debugmenu
                if  event.key == pygame.K_q:
                    running = False
                if event.key == pygame.K_RIGHTBRACKET or event.key == pygame.K_LEFTBRACKET:
                    scenemanager.handle_input(event)
        else:
            if event.type == pygame.KEYDOWN:
                if event.mod and pygame.KMOD_SHIFT and event.key == pygame.K_COLON or event.key == pygame.K_SEMICOLON:
                    debugmenu = not debugmenu
                if event.key == pygame.K_ESCAPE:
                    debugmenu = not debugmenu
            scenemanager.handle_input(event)

    scenemanager.update()
    #Handle GameLogic Updates:
        #Non existant, no time basedupdates here

    #Renders/views
    scenemanager.render(screen)
    if debugmenu == True:
        pygame.draw.rect(screen, (50, 50, 55), (debug_pos_x,debug_pos_y,250,30))
        pygame.draw.rect(screen, (200, 200, 200), (debug_pos_x,debug_pos_y+30,250,150))
        screen.blit(title_debug_text,(debug_pos_x+12,debug_pos_y+2))
        screen.blit(debug_text1,(debug_pos_x+12,debug_pos_y+32))
        screen.blit(debug_text2,(debug_pos_x+12,debug_pos_y+62))
        screen.blit(debug_text3,(debug_pos_x+12,debug_pos_y+92))
    pygame.display.flip()

pygame.quit()
