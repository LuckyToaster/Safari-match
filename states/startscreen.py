import random, pygame as pg
from .base import BaseState 

class StartScreen(BaseState):
    def __init__(self):
        super(StartScreen, self).__init__()
        self.next_state = "MAIN_MENU"
        self.time_active = 0
        self.title = self.render_text("Safari Match!", "StarBorn.ttf", 80, pg.Color("white")) 
        self.title_rect = self.title.get_rect(center=self.screen_rect.center)

    def update(self, dt):
        self.time_active += dt
        if self.time_active >= 1000:
            self.done = True

    def draw(self, surface):
        surface.blit(self.get_rand_bg(), (0,0))
        surface.blit(self.title, self.title_rect)



