import pygame as pg
import os

class BaseState(object):
    def __init__(self):
        self.done = False
        self.quit = False
        self.next_state = None
        self.screen_rect = pg.display.get_surface().get_rect()
        self.persist = {}
        self.font = pg.font.Font("assets/KarmaFuture.ttf", 40)
        # things I've added
        self.backgrounds = os.listdir("./assets/backgrounds")
        self.screen_w = pg.display.Info().current_w
        self.screen_h = pg.display.Info().current_h
        self.colors = {
            "CYAN": (172,238,243),
            "CORAL": (255,112,119),
            "ROSE": (255,233,228),
            "ORANGE": (255,176,103)
        }

    def startup(self, persistent):
        self.persist = persistent

    def get_event(self, event):
        pass

    def update(self, dt):
        pass

    def draw(self, surface):
        pass