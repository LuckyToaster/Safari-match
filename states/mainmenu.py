import random, pygame as pg
from .base import BaseState

class MainMenu(BaseState):
    def __init__(self):
        super(MainMenu, self).__init__()
        self.active_index = 0
        self.options = ["Play", "Exit"]
        self.next_state = "GAME_PLAY"
        self.click = False

    def render_options(self, index):
        if index == self.active_index:
            color = pg.Color("orange")
            return self.render_text(self.options[index], "StarBorn.ttf", 50, color)
        else: 
            color = pg.Color("white")
            return self.render_text(self.options[index], "StarBorn.ttf", 40, color)

    def get_text_position(self, text, index):
        center = (self.screen_rect.center[0], self.screen_rect.center[1] + (index * 50))
        return text.get_rect(center=center)

    def handle_action(self):
        if self.active_index == 0:
            self.done = True
        elif self.active_index == 1:
           self.quit = True

    def get_event(self, event):
        # the keyboard aspect
        if event.type == pg.QUIT:
            self.quit = True
        elif event.type == pg.KEYUP:
            if event.key == pg.K_UP:
                self.active_index = 1 if self.active_index <= 0 else 0
            elif event.key == pg.K_DOWN:
                self.active_index = 0 if self.active_index >= 1 else 1
            elif event.key == pg.K_RETURN:
                self.handle_action()
            elif event.key == pg.K_ESCAPE:
                self.quit = True
        # the mouse aspect ---> should add this funcionality
        elif event.type == pg.MOUSEBUTTONDOWN:
            if event.button == 1:
                self.click == True

    def draw(self, surface):
        surface.blit(self.get_ran_bg(), (0,0)) 
        for index, option in enumerate(self.options):
            text_render = self.render_options(index)
            surface.blit(text_render, self.get_text_position(text_render, index))