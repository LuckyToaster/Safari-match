import pygame as pg
from pygame.locals import *
from .base import BaseState, Dimmer

class GameOver(BaseState):
    def __init__(self):
        super(GameOver, self).__init__()
        self.title = self.render_text("Game Over", "Upheavtt.ttf", 65, Color("white"))
        self.options = ["Retry", "Go Back"]
        self.next_state = "GAME_PLAY"

    def render_oprtions(self, index):
        if index == self.active_index:
            return self.render_text(self.options[index]), "StarBorn.ttf", 50, Color("orange")
        else: 
            return self.render_text(self.options[index]), "StarBorn.ttf", 40, Color("white")
    
    def handle_actions(self):
        if self.active_index == 0:
            self.done = True
        elif self.active_index == 1:
            self.next_state = "MAIN_MENU"
            self.done = True
    
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
        surface.blit(self.get_rand_bg(),(0,0))
        for index, option in enumerate(self.options):
            text_render = self.render_options(index)
            surface.blit(text_render, self.get_text_position(text_render, index))



