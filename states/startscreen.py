import random, pygame as pg
from .base import BaseState 

class StartScreen(BaseState):
    def __init__(self):
        super(StartScreen, self).__init__()
        self.title = self.font.render("Safari Match!", True, pg.Color("blue"))
        self.title_rect = self.title.get_rect(center=self.screen_rect.center)
        self.next_state = "MAIN_MENU"
        self.time_active = 0
        # get a random bg image for every startscreen
        self.ran_bg_index = random.randrange(len(self.backgrounds))

    def update(self, dt):
        self.time_active += dt
        if self.time_active >= 5000:
            self.done = True

    def draw(self, surface):
        bg_img = pg.image.load("assets/backgrounds/" + self.backgrounds[self.ran_bg_index]) # get a random background
        bg_img = pg.transform.smoothscale(bg_img,(self.screen_w,self.screen_h)) # scale it
        surface.blit(bg_img, (0,0)) # draw it
        surface.blit(self.title, self.title_rect) # draw the game title

