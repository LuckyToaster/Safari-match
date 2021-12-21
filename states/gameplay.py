import random, pygame as pg
from pygame.locals import *
from .base import BaseState, Dimmer, FPSCounter

class GamePlay(BaseState):
    def __init__(self):
        super(GamePlay, self).__init__()
        self.rect = pg.Rect((0, 0), (80, 80))
        self.rect.center = self.screen_rect.center
        self.next_state = "PAUSE_MENU"
        self.names = ["bee", "cat", "cow", "elephant", "fox", "hen", "koala", "parrot", "penguin", "toucan", "turtle"]
        self.active_index = 0

    def get_event(self, event):
        if event.type == pg.QUIT:
            self.quit = True
        elif event.type == KEYUP:
            if event.key == K_LEFT or event.key == K_a:
                if self.active_index > 0: self.active_index -= 1 
                else: self.active_index = 3
            if event.key == K_RIGHT or event.key == K_d:
                if self.active_index < 3: self.active_index += 1
                else: self.active_index = 0
            if event.key == K_SPACE or event.key == K_ESCAPE:
                self.done = True

    def draw(self, surface):
        # background
        surface.blit(self.get_rand_bg(),(0,0))
        # get the cards in the damn screen
        card_list = self.get_card_list()
        name_deck = self.get_name_deck()
        x = 0
        for i, index in enumerate(name_deck):
            surface.blit(card_list[index],((self.screen_rect.center[0]/2)+x, self.screen_rect.center[1]))
            x = i*128
    

    # the same index in cards and names refers to the same animal
    def get_card_list(self):
        cards = []        
        for i, name in enumerate(self.names):
            cards.append(pg.image.load("assets/animals/" + self.names[i] + ".png"))
        return cards 

    # get a list with the indexes of 4 random cards
    def get_name_deck(self): 
        deck = []
        for i in range(4): deck.append(random.randrange(len(self.names)))
        return deck
        
           

