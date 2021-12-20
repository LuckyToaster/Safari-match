import pygame as pg
from pygame.locals import *
from .base import BaseState

class GamePlay(BaseState):
    def __init__(self):
        super(GamePlay, self).__init__()
        self.rect = pg.Rect((0, 0), (80, 80))
        self.rect.center = self.screen_rect.center
        self.next_state = "PAUSE_MENU"

    def get_event(self, event):
        if event.type == pg.QUIT:
            self.quit = True
        elif event.type == KEYUP:
            if event.key == K_UP:
                self.rect.move_ip(0, -10)
            if event.key == K_DOWN:
                self.rect.move_ip(0, 10)
            if event.key == K_LEFT:
                self.rect.move_ip(-10, 0)
            if event.key == K_RIGHT:
                self.rect.move_ip(10, 0)
            if event.key == K_SPACE or event.key == K_ESCAPE:
                self.done = True

    def draw(self, surface):
        surface.blit(self.get_rand_bg(),(0,0))
        pg.draw.rect(surface, pg.Color("blue"), self.rect)