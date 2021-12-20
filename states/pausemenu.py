import pygame as pg
from .base import BaseState


class PauseMenu(BaseState):
    def __init__(self):
        super(PauseMenu, self).__init__()
        self.title = self.render_text("Pause", "Upheavtt.ttf", 60, pg.Color("white"))
        self.instructions1 = self.font.render("Space / Enter - to continue", True, pg.Color("white"))
        self.instructions2 = self.font.render("Escape - to go back", True, pg.Color("white"))
        instructions_center = (self.screen_rect.center[0], self.screen_rect.center[1] +  50)
        self.title_rect = self.title.get_rect(center=self.screen_rect.center)
        self.instructions1_rect = self.instructions1.get_rect(center=instructions_center)
        self.instructions2_rect = self.instructions2.get_rect(center=(self.screen_rect.center[0], self.screen_rect.center[1]+100))

    def get_event(self, event):
        if event.type == pg.QUIT:
            self.quit = True
        elif event.type == pg.KEYUP:
            if event.key == pg.K_RETURN:
                self.next_state = "GAME_PLAY"
                self.done = True
            elif event.key == pg.K_SPACE:
                self.next_state = "GAME_PLAY"
                self.done = True
            elif event.key == pg.K_ESCAPE:
                self.next_state = "MAIN_MENU"
                self.done = True

    def draw(self, surface):
        #surface.fill(pg.Color("black"))
        surface.blit(self.title, self.title_rect)
        surface.blit(self.instructions1,self.instructions1_rect)
        surface.blit(self.instructions2, self.instructions2_rect)