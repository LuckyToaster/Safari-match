import pygame as pg
from .base import BaseState


class GameOver(BaseState):
    def __init__(self):
        super(GameOver, self).__init__()
        self.title = self.font.render("Game Over", True, pg.Color("white"))
        self.title_rect = self.title.get_rect(center=self.screen_rect.center)
        self.instructions = self.font.render("Press space to start again, or enter to go to the menu", True, pg.Color("white"))
        instructions_center = (self.screen_rect.center[0], self.screen_rect.center[1] +  50)
        self.instructions_rect = self.instructions.get_rect(center=instructions_center)

    def get_event(self, event):
        if event.type == pg.QUIT:
            self.quit = True
        elif event.type == pg.KEYUP:
            if event.key == pg.K_RETURN:
                self.next_state = "MAIN_MENU"
                self.done = True
            elif event.key == pg.K_SPACE:
                self.next_state = "GAME_PLAY"
                self.done = True
            elif event.key == pg.K_ESCAPE:
                self.quit = True

    def draw(self, surface):
        surface.fill(pg.Color("black"))
        surface.blit(self.title, self.title_rect)
        surface.blit(self.instructions, self.instructions_rect)