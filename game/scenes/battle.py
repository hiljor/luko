import pygame
from assets.assetManager import load_font
from widgets.card import CardWidget

class BattleScene:
    def __init__(self):
        self.bg_colour = (30, 30, 30)
        self.fg_colour = (0, 0, 30)
        self.cardsize = 80
        self.cardsize_opp = 30
        self.cardcolour = (50,50,100)
        self.cardcolour_opp = (100,50,50)
        self.selectedsize = 50
        self.playarea = 150
        self.margin = 10
        self.margin_opp = 20
        self.card1 = CardWidget() \
                .setName('Rock') \
                .setSize(self.cardsize) \
                .setColour(0,0,0) \
                .setPos(self.playarea+5,320) \
                .create()
        self.card2 = CardWidget() \
                .setName('Rock') \
                .setSize(self.cardsize) \
                .setColour(0,0,0) \
                .setPos(self.playarea+self.margin+((self.cardsize+5)),320) \
                .create()
        self.card3 = CardWidget() \
                .setName('Rock') \
                .setSize(self.cardsize) \
                .setColour(0,0,0) \
                .setPos(self.playarea+self.margin+((self.cardsize+5)*2),320) \
                .create()
        self.cardopp1 = CardWidget() \
                .setName('') \
                .setSize(self.cardsize_opp) \
                .setColour(100,50,50) \
                .setPos(self.playarea+self.margin_opp,15) \
                .create()
        self.cardopp2 = CardWidget() \
                .setName('') \
                .setSize(self.cardsize_opp) \
                .setColour(100,50,50) \
                .setPos(self.playarea+self.margin_opp+((self.cardsize_opp+5)),15) \
                .create()
        self.cardopp3 = CardWidget() \
                .setName('') \
                .setSize(self.cardsize_opp) \
                .setColour(100,50,50) \
                .setPos(self.playarea+self.margin_opp+((self.cardsize_opp+5)*2),15) \
                .create()

        self.card_selected = CardWidget() \
                .setName('Rock') \
                .setSize(self.selectedsize) \
                .setColour(0,50,100) \
                .setPos(self.playarea+100,190)\
                .create()

        self.cardopp_selected = CardWidget() \
                .setName('Rock') \
                .setSize(self.selectedsize) \
                .setColour(100,50,50) \
                .setPos(self.playarea+100,80) \
                .create()

    def handle_input(self, event):
        pass

    def update(self):
        pass

    def render(self,screen):
        screen.fill(self.bg_colour)
        #self.deck.render()
        #self.hand.render()
        self.cardopp1.render(screen)
        self.cardopp2.render(screen)
        self.cardopp3.render(screen)

        self.cardopp_selected.render(screen)
        self.card_selected.render(screen)

        self.card1.render(screen)
        self.card2.render(screen)
        self.card3.render(screen)



        #pygame.draw.rect(screen, (55, 55, 55), (0,0,self.playarea,500))
        #screen.blit(self.deck_text,(20,50))
