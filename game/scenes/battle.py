import pygame
from assets.assetManager import load_font

class BattleScene:
    def __init__(self):
        self.bg_colour = (30, 30, 30)
        self.fg_colour = (0, 0, 30)
        self.cardsize = 80
        self.cardsize_opp = 30
        self.playarea = 150
        self.card1_text_value = "rock"
        self.card2_text_value = "paper"
        self.card3_text_value = "scissors"
        self.card1_opp_text_value = "rock"
        self.card2_opp_text_value = "paper"
        self.card3_opp_text_value = "scissors"
        self.hello_font = load_font('PixelScript', 20)
        self.deck_text = self.hello_font.render("Battle",1,(200,200,200))
        self.card_font = load_font('PixelScript', 20)
        self.card_opp_font = load_font('PixelScript', 18)
        self.card1_text = self.card_font.render(self.card1_text_value,1,(200,200,200))
        self.card2_text = self.card_font.render(self.card2_text_value,1,(200,200,200))
        self.card3_text = self.card_font.render(self.card3_text_value,1,(200,200,200))
        self.card1_opp_text = self.card_font.render(self.card1_opp_text_value,1,(200,200,200))
        self.card2_opp_text = self.card_font.render(self.card2_opp_text_value,1,(200,200,200))
        self.card3_opp_text = self.card_font.render(self.card3_opp_text_value,1,(200,200,200))

    def handle_input(self, event):
        pass

    def update(self):
        pass

    def render(self,screen):
        screen.fill(self.bg_colour)
        pygame.draw.rect(screen, (55, 55, 55), (0,0,self.playarea,500))
        screen.blit(self.deck_text,(20,50))
        pygame.draw.rect(screen, (0, 0, 0), (self.playarea+30+10,20,self.cardsize_opp,self.cardsize_opp*2))
        screen.blit(self.card1_opp_text,(self.playarea,50))
        pygame.draw.rect(screen, (0, 0, 0), (self.playarea+30+100,20,self.cardsize_opp,self.cardsize_opp*2))
        screen.blit(self.card2_opp_text,(self.playarea,50))
        pygame.draw.rect(screen, (0, 0, 0), (self.playarea+30+190,20,self.cardsize_opp,self.cardsize_opp*2))
        screen.blit(self.card3_opp_text,(self.playarea,50))
        pygame.draw.rect(screen, (0, 0, 0), (self.playarea+30,300,self.cardsize,self.cardsize*2))
        screen.blit(self.card1_text,(self.playarea,50))
        pygame.draw.rect(screen, (0, 0, 0), (self.playarea+30+(self.cardsize+10),300,self.cardsize,self.cardsize*2))
        screen.blit(self.card2_text,(self.playarea,50))
        pygame.draw.rect(screen, (0, 0, 0), (self.playarea+30+(self.cardsize+10)*2,300,self.cardsize,self.cardsize*2))
        screen.blit(self.card3_text,(self.playarea,320))
