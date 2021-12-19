import pygame as pg
import os

class BaseState(object):
    def __init__(self):
        self.done = False
        self.quit = False
        self.next_state = None
        self.screen_rect = pg.display.get_surface().get_rect()
        self.persist = {}
        self.font = pg.font.Font(None, 24)
        # things I've added
        self.backgrounds = os.listdir("./assets/backgrounds")
        self.screen_w = pg.display.Info().current_w
        self.screen_h = pg.display.Info().current_h

    def startup(self, persistent):
        self.persist = persistent

    def get_event(self, event):
        pass

    def update(self, dt):
        pass

    def draw(self, surface):
        pass