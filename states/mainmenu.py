import random, pygame as pg
from .base import BaseState

class MainMenu(BaseState):
    def __init__(self):
        super(MainMenu, self).__init__()
        self.active_index = 0
        self.options = ["Play", "Exit"]
        self.next_state = "GAME_PLAY"
        self.click = False
        #self.ran_bg_index = random.randrange(len(self.backgrounds)) 
        #self.rand_color = list(self.colors.values())[random.randrange(len(self.colors))] # get a random color

    def render_text(self, index):
        #color = self.colors["ORANGE"] if index == self.active_index else pg.Color("white")
        color = self.rand_color if index == self.active_index else pg.Color("white")
        return self.font.render(self.options[index], True, color)

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
        #surface.fill(pg.Color("black"))
        bg_img = pg.image.load("assets/backgrounds/" + self.backgrounds[self.ran_bg_index]) # get a random background
        bg_img = pg.transform.smoothscale(bg_img,(self.screen_w,self.screen_h)) # scale it
        surface.blit(bg_img, (0,0)) # draw background

        for index, option in enumerate(self.options):
            text_render = self.render_text(index)
            surface.blit(text_render, self.get_text_position(text_render, index))