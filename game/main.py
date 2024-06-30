import pygame
from enum import Enum
from maps.mapFactory import MapFactory

pygame.init()
pygame.font.init()
pygame.mixer.init()

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
            if event.type == pygame.KEYDOWN:
                if event.mod and pygame.KMOD_SHIFT and event.key == pygame.K_COLON or event.key == pygame.K_SEMICOLON:
                    debugmenu = True
            match(scene):
                case scene.INTRO:
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_RIGHTBRACKET:
                            scene = gamescene.MAP
                case scene.MAP:
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_RIGHTBRACKET:
                            scene = gamescene.ROOM
                case scene.ROOM:
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_RIGHTBRACKET:
                            scene = gamescene.BATTLE
                case scene.BATTLE:
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_RIGHTBRACKET:
                            scene = gamescene.END
                case scene.END:
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_RIGHTBRACKET:
                            scene = gamescene.CREDITS
                case scene.CREDITS:
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_RIGHTBRACKET:
                            scene = gamescene.M
                case scene.M:
                    if event.type == pygame.KEYDOWN:
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
            pygame.draw.rect(screen, (0, 0, 255), (250, 450,250,250))
            screen.blit(hello_text,(250,150))
        case gamescene.BATTLE:
            cardsize = 80
            cardsize_opp = 30
            play = 150
            card1_text_value = "rock"
            card2_text_value = "paper"
            card3_text_value = "scissors"
            card1_opp_text_value = "rock"
            card2_opp_text_value = "paper"
            card3_opp_text_value = "scissors"
            hello_font = pygame.font.Font('./PixelScript.ttf', 20)
            deck_text = hello_font.render("Battle",1,(200,200,200))
            card_font = pygame.font.Font('./PixelScript.ttf', 20)
            card_opp_font = pygame.font.Font('./PixelScript.ttf', 18)
            card1_text = card_font.render(card1_text_value,1,(200,200,200))
            card2_text = card_font.render(card2_text_value,1,(200,200,200))
            card3_text = card_font.render(card3_text_value,1,(200,200,200))
            card1_opp_text = card_font.render(card1_opp_text_value,1,(200,200,200))
            card2_opp_text = card_font.render(card2_opp_text_value,1,(200,200,200))
            card3_opp_text = card_font.render(card3_opp_text_value,1,(200,200,200))

            screen.fill(bg_colour)
            pygame.draw.rect(screen, (55, 55, 55), (0,0,play,500))
            screen.blit(deck_text,(20,50))
            pygame.draw.rect(screen, (0, 0, 0), (play+30+10,20,cardsize_opp,cardsize_opp*2))
            screen.blit(card1_opp_text,(play,50))
            pygame.draw.rect(screen, (0, 0, 0), (play+30+100,20,cardsize_opp,cardsize_opp*2))
            screen.blit(card2_opp_text,(play,50))
            pygame.draw.rect(screen, (0, 0, 0), (play+30+190,20,cardsize_opp,cardsize_opp*2))
            screen.blit(card3_opp_text,(play,50))
            pygame.draw.rect(screen, (0, 0, 0), (play+30,300,cardsize,cardsize*2))
            screen.blit(card1_text,(play,50))
            pygame.draw.rect(screen, (0, 0, 0), (play+30+(cardsize+10),300,cardsize,cardsize*2))
            screen.blit(card2_text,(play,50))
            pygame.draw.rect(screen, (0, 0, 0), (play+30+(cardsize+10)*2,300,cardsize,cardsize*2))
            screen.blit(card3_text,(play,320))
        case gamescene.END:
            bg_colour = (30, 30, 30)
            fg_colour = (0, 0, 30)
            screen.fill(bg_colour)
            hello_font = pygame.font.Font('./PixelScript.ttf', 20)
            hello_text = hello_font.render("You LOSE....   WIN",1,(200,200,200))
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
        debug_pos_x = 150
        debug_pos_y = 250
        title_debug_font = pygame.font.Font('./PixelScript.ttf', 15)
        title_debug_text = title_debug_font.render("Menu",0,(200,200,200))
        debug_font = pygame.font.Font('./PixelScript.ttf', 20)
        debug_text = debug_font.render("Press q to quit",1,(0,0,0))
        pygame.draw.rect(screen, (50, 50, 55), (debug_pos_x,debug_pos_y,250,30))
        pygame.draw.rect(screen, (200, 200, 200), (debug_pos_x,debug_pos_y+30,250,150))
        screen.blit(title_debug_text,(debug_pos_x+12,debug_pos_y+2))
        screen.blit(debug_text,(debug_pos_x+32,debug_pos_y+32))
    pygame.display.flip()

pygame.quit()
