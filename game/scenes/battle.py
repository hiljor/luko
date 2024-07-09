import pygame
from assets.assetManager import load_font
from widgets.card import CardWidget
from widgets.hand import HandWidget
from common import Scene
from deck.deck import Deck
from deck.battle import Battle, BattleResult
from deck.cards import cardlist
import random

class BattleScene:
    def __init__(self):
        self.initialise = True
        self.pause = False
        self.clock = pygame.time.get_ticks()
        self.win = False
        self.health = 10
        self.deckselect = False
        self.selected = False
        self.cardselected = 0
        self.result = 0
        self.resultshow = False
        self.cardoppselected = 0
        self.phase = 0
        self.frame = 0
        self.bg_colour = (30, 30, 30)
        self.fg_colour = (0, 0, 30)
        self.cardsize = 80
        self.cardsize_opp = 30
        self.cardcolour = (50,50,100)
        self.cardcolour_opp = (100,50,50)
        self.selectedsize = 50
        self.playarea = 150
        self.margin = 50
        self.margin_opp = 200
        self.font = load_font('PixelScript', 20)
        self.text1 = self.font.render('You Win',1,(200,200,200))
        self.text2 = self.font.render('You Lose',1,(200,200,200))
        self.textd = self.font.render('You Draw',1,(200,200,200))
        self.hand = HandWidget() \
                .setPos(self.margin-(self.cardsize/2),320) \
                .setSize(self.cardsize) \
                .create()
        self.hand_opp = HandWidget() \
                .setPos(self.playarea+self.margin_opp-(self.cardsize_opp/2),15) \
                .setSize(self.cardsize_opp) \
                .create()
        self.card1 = CardWidget() \
                .setName('Rock').setSize(self.cardsize).setColour(self.cardcolour) \
                .setPos(self.margin,320) \
                .create()
        self.card2 = CardWidget() \
                .setName('Rock').setSize(self.cardsize).setColour(self.cardcolour) \
                .setPos(self.margin+((self.cardsize+5)),320) \
                .create()
        self.card3 = CardWidget() \
                .setName('Rock').setSize(self.cardsize).setColour(self.cardcolour) \
                .setPos(self.margin+((self.cardsize+5)*2),320) \
                .create()
        self.cardopp1 = CardWidget() \
                .setName('').setSize(self.cardsize_opp).setColour(self.cardcolour_opp) \
                .setPos(self.playarea+self.margin_opp,15) \
                .create()
        self.cardopp2 = CardWidget() \
                .setName('').setSize(self.cardsize_opp).setColour(self.cardcolour_opp)\
                .setPos(self.playarea+self.margin_opp+((self.cardsize_opp+5)),15) \
                .create()
        self.cardopp3 = CardWidget() \
                .setName('').setSize(self.cardsize_opp).setColour(self.cardcolour_opp) \
                .setPos(self.playarea+self.margin_opp+((self.cardsize_opp+5)*2),15) \
                .create()

        self.card_selected = CardWidget() \
                .setName('Rock').setSize(self.selectedsize).setColour(self.cardcolour) \
                .setPos(self.playarea+100-(self.selectedsize/2),190)\
                .create()

        self.cardopp_selected = CardWidget() \
                .setName('Rock').setSize(self.selectedsize).setColour(self.cardcolour_opp) \
                .setPos(self.playarea+100-(self.selectedsize/2),80) \
                .create()

        self.deck = CardWidget() \
                .setName('Deck').setSize(self.cardsize-10).setColour(self.cardcolour) \
                .setPos(self.margin+((self.cardsize+5)*3+self.cardsize),330) \
                .create()
        self.deckopp = CardWidget() \
                .setName('Deck').setSize(self.cardsize_opp-2).setColour(self.cardcolour_opp) \
                .setPos(self.playarea+self.margin_opp-((self.cardsize_opp+5))-self.cardsize_opp,15) \
                .create()

        self.battle = Battle()
        self.player_deck = Deck(52)
        self.player_hand = Deck(3)
        self.playeropp_deck = Deck(52)
        self.playeropp_hand = Deck(3)

    def start(self):
        self.card1.destroy()
        self.card2.destroy()
        self.card3.destroy()
        self.cardopp1.destroy()
        self.cardopp2.destroy()
        self.cardopp3.destroy()
        self.card_selected.destroy()
        self.cardopp_selected.destroy()
        self.deck.create()
        self.deckopp.create()

        for i in range(52):
            card = cardlist.find(random.randrange(3))
            if card == False:
                print("Card does not exist")
            else:
                self.player_deck.add(card)

        for i in range(52):
            card = cardlist.find(random.randrange(3))
            if card == False:
                print("Card does not exist")
            else:
                self.playeropp_deck.add(card)
        
        self.player_deck.shuffle()
        self.playeropp_deck.shuffle()

        return self

    def handle_input(self, event):
        if not self.pause:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if self.deck.with_in(event.pos):
                    if self.phase == 0 and not self.pause:
                        self.deck.select()
                        self.cardoppselected = random.randrange(3)
                        self.resultshow = False
                        self.deckselect = True
                        self.pause = True
                if self.card1.with_in(event.pos):
                    if self.phase == 1 and not self.pause:
                        self.card1.select()
                        self.selected = True
                        self.cardselected = 0
                        self.pause = True
                if self.card2.with_in(event.pos):
                    if self.phase == 1 and not self.pause:
                        self.card2.select()
                        self.selected = True
                        self.cardselected = 1
                        self.pause = True
                if self.card3.with_in(event.pos):
                    if self.phase == 1 and not self.pause:
                        self.card3.select()
                        self.selected = True
                        self.cardselected = 2
                        self.pause = True


    def update(self):
        if self.initialise:
            self.start()
            self.initialise = False
        if not self.pause:
            self.clock = pygame.time.get_ticks()

        if self.phase == 0:
            if self.deckselect:
                if self.frame == 0:
                    self.card_selected.selected = False
                    self.cardopp_selected.selected = False
                    self.card_selected.destroy()
                    self.cardopp_selected.destroy()
                    for i in range(self.player_hand.total()):
                        if self.player_hand.count() < self.player_hand.total():
                            hand_add = self.player_hand.add(self.player_deck.pop())
                            if (hand_add != 0):
                                print("Hand Failed")
                                print(hand_add)
                                exit()
                    for i in range(self.playeropp_hand.total()):
                        if self.playeropp_hand.count() < self.playeropp_hand.total():
                            handopp_add = self.playeropp_hand.add(self.playeropp_deck.pop())
                            if (handopp_add != 0):
                                print("Hand Failed")
                                print(handopp_add)
                                exit()
                if self.frame == 0 and pygame.time.get_ticks() - self.clock > 500:
                    self.deck.select()
                    self.card2.hidden = True
                    self.card1.setName(self.player_hand.view(0).name).create()
                    self.frame += 1
                if self.frame == 1 and pygame.time.get_ticks() - self.clock > 700:
                    self.cardopp2.hidden = True
                    self.cardopp1.create()
                    self.frame += 1
                if self.frame == 2 and pygame.time.get_ticks() - self.clock > 1000:
                    self.card3.hidden = True
                    self.card2.setName(self.player_hand.view(1).name).create()
                    self.frame += 1
                if self.frame == 3 and pygame.time.get_ticks() - self.clock > 1200:
                    self.cardopp3.hidden = True
                    self.cardopp2.create()
                    self.frame += 1
                if self.frame == 4 and pygame.time.get_ticks() - self.clock > 1500:
                    self.card3.setName(self.player_hand.view(2).name).create()
                    self.frame += 1
                if self.frame == 5 and pygame.time.get_ticks() - self.clock > 1700:
                    self.cardopp3.create()
                    self.frame += 1
                if self.frame == 6 and pygame.time.get_ticks() - self.clock > 1900:
                    self.frame = 0
                    self.deckselect = False
                    self.pause = False
                    self.phase += 1
        if self.phase == 1:
            if self.selected:
                if self.frame == 0 and pygame.time.get_ticks() - self.clock > 600:
                    if self.cardselected == 0:
                        self.card1.select()
                        self.card1.destroy()
                    if self.cardselected == 1:
                        self.card2.select()
                        self.card2.destroy()
                    if self.cardselected == 2:
                        self.card3.select()
                        self.card3.destroy()
                    self.frame += 1
                if self.frame == 1 and pygame.time.get_ticks() - self.clock > 900:
                    if self.cardoppselected == 0:
                        self.cardopp1.destroy()
                    if self.cardoppselected == 1:
                        self.cardopp2.destroy()
                    if self.cardoppselected == 2:
                        self.cardopp3.destroy()
                    self.frame += 1
                if self.frame == 2 and pygame.time.get_ticks() - self.clock > 1200:
                    self.card_selected.setName(self.player_hand.view(self.cardselected).name).create()
                    self.frame += 1
                if self.frame == 3 and pygame.time.get_ticks() - self.clock > 1800:
                    self.cardopp_selected.setName(self.playeropp_hand.view(self.cardoppselected).name).create()
                    self.frame += 1
                if self.frame == 4 and pygame.time.get_ticks() - self.clock > 2400:
                    self.battle.fight(self.player_hand.pop(self.cardselected), self.playeropp_hand.pop(self.cardoppselected))
                    self.frame += 1
                if self.frame == 5 and pygame.time.get_ticks() - self.clock > 3500:
                    if self.battle.results() == BattleResult.PLAYER1:
                        self.card_selected.select()
                        self.cardopp_selected.destroy()
                        self.result = 1
                    if self.battle.results() == BattleResult.PLAYER2:
                        self.cardopp_selected.select()
                        self.card_selected.destroy()
                        self.result = 2
                    if self.battle.results() == BattleResult.DRAW:
                        self.card_selected.destroy()
                        self.cardopp_selected.destroy()
                        self.result = 0
                    self.resultshow = True
                    self.frame = 0
                    self.selected = False
                    self.pause = False
                    self.phase = 0
                    

        if self.win:
            return Scene.MAINMENU


    def render(self,screen):
        screen.fill(self.bg_colour)
        #self.deck.render()
        #self.hand.render()
        self.hand_opp.render(screen)
        self.cardopp1.render(screen)
        self.cardopp2.render(screen)
        self.cardopp3.render(screen)

        self.deckopp.render(screen)

        self.cardopp_selected.render(screen)
        self.card_selected.render(screen)

        self.hand.render(screen)
        self.card1.render(screen)
        self.card2.render(screen)
        self.card3.render(screen)

        self.deck.render(screen)

        if self.resultshow: 
            if self.result == 1:
                screen.blit(self.text1,(80,250))
            if self.result == 2:
                screen.blit(self.text2,(80,250))
            if self.result == 0:
                screen.blit(self.textd,(80,250))

        #pygame.draw.rect(screen, (55, 55, 55), (0,0,self.playarea,500))
        #screen.blit(self.deck_text,(20,50))
