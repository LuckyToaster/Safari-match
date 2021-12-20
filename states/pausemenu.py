import pygame as pg
from .base import BaseState, Dimmer
from pygame.locals import *

class PauseMenu(BaseState):
    def __init__(self):
        super(PauseMenu, self).__init__()
        self.title = self.render_text("Pause", "Upheavtt.ttf", 65, Color("white"))
        self.instructions1 = self.font.render("Space / Enter - to continue", True, Color("white"))
        self.instructions2 = self.font.render("Escape - to go back", True, Color("white"))
        #instructions_center = (self.screen_rect.center[0], self.screen_rect.center[1] +  50)
        title_center = (self.screen_rect.center[0], self.screen_rect.center[1] - 100)
        instructions_center = (self.screen_rect.center[0], self.screen_rect.center[1] - 40)
        self.title_rect = self.title.get_rect(center=title_center)
        self.instructions1_rect = self.instructions1.get_rect(center=instructions_center)
        self.instructions2_rect = self.instructions2.get_rect(center=self.screen_rect.center)
        self.dim = Dimmer(1)

    def get_event(self, event):
        if event.type == QUIT:
            self.quit = True
        elif event.type == KEYUP:
            if event.key == K_RETURN or event.key == K_SPACE:
                self.dim.undim()
                self.next_state = "GAME_PLAY"
                self.done = True
            elif event.key == K_ESCAPE:
                self.dim.undim()
                self.next_state = "MAIN_MENU"
                self.done = True

    def draw(self, surface):
        self.dim.dim(10,(10,10,10))
        surface.blit(self.title, self.title_rect)
        surface.blit(self.instructions1,self.instructions1_rect)
        surface.blit(self.instructions2, self.instructions2_rect)

        