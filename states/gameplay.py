import pygame as pg
from .base import BaseState

class GamePlay(BaseState):
    def __init__(self):
        super(GamePlay, self).__init__()
        self.rect = pg.Rect((0, 0), (80, 80))
        self.rect.center = self.screen_rect.center
        self.next_state = "GAME_OVER"

    def get_event(self, event):
        if event.type == pg.QUIT:
            self.quit = True
        elif event.type == pg.KEYUP:
            if event.key == pg.K_UP:
                self.rect.move_ip(0, -10)
            if event.key == pg.K_DOWN:
                self.rect.move_ip(0, 10)
            if event.key == pg.K_LEFT:
                self.rect.move_ip(-10, 0)
            if event.key == pg.K_RIGHT:
                self.rect.move_ip(10, 0)
            if event.key == pg.K_SPACE:
                self.done = True

    def draw(self, surface):
        surface.fill(pg.Color("black"))
        pg.draw.rect(surface, pg.Color("blue"), self.rect)