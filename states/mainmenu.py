import random, pygame as pg
from pygame.locals import *
from .base import BaseState, Dimmer

class MainMenu(BaseState):
    def __init__(self):
        super(MainMenu, self).__init__()
        self.active_index = 0
        self.options = ["Play", "Exit"]
        self.next_state = "GAME_PLAY"

    def render_options(self, index):
        if index == self.active_index:
            return self.render_text(self.options[index], "StarBorn.ttf", 50, pg.Color("orange"))
        else: 
            return self.render_text(self.options[index], "StarBorn.ttf", 40, pg.Color("white"))

    def get_text_position(self, text, index):
        center = (self.screen_rect.center[0], self.screen_rect.center[1] + (index * 70))
        return text.get_rect(center=center)

    def handle_action(self):
        if self.active_index == 0:
            self.done = True
        elif self.active_index == 1:
           self.quit = True

    def get_event(self, event):
        if event.type == QUIT:
            self.quit = True
        elif event.type == KEYUP:
            if event.key == K_UP:
                self.active_index = 1 if self.active_index <= 0 else 0
            elif event.key == K_DOWN:
                self.active_index = 0 if self.active_index >= 1 else 1
            elif event.key == K_RETURN:
                self.handle_action()
            elif event.key == K_ESCAPE:
                self.quit = True

    def draw(self, surface):
        surface.blit(self.get_rand_bg(), (0,0)) 
        for index, option in enumerate(self.options):
            text_render = self.render_options(index)
            surface.blit(text_render, self.get_text_position(text_render, index))
