import pygame
from .base import BaseState 

class StartScreen(BaseState):
    def __init__(self):
        super(StartScreen, self).__init__()
        self.title = self.font.render("Safari Match!", True, pygame.Color("blue"))
        self.title_rect = self.title.get_rect(center=self.screen_rect.center)
        self.next_state = "MAIN_MENU"
        self.time_active = 0

    def update(self, dt):
        self.time_active += dt
        if self.time_active >= 5000:
            self.done = True

    def draw(self, surface):
        surface.fill(pygame.Color("black"))
        surface.blit(self.title, self.title_rect)

