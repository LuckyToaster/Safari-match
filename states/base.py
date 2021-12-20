import pygame as pg
import random, os

class BaseState(object):
    def __init__(self):
        self.done = False
        self.quit = False
        self.next_state = None
        self.screen_rect = pg.display.get_surface().get_rect()
        self.persist = {}
        self.font = pg.font.Font("assets/fonts/Upheavtt.ttf", 30) 
        # things I've added
        self.screen_w = pg.display.Info().current_w
        self.screen_h = pg.display.Info().current_h
        self.backgrounds = os.listdir("./assets/backgrounds")
        self.colors = {
            "CYAN": (172,238,243),
            "CORAL": (255,112,119),
            "ROSE": (255,233,228),
            "ORANGE": (255,176,103),
            "OLIVE_GREEN": (61,85,12),
            "LIME_GREEN": (129,182,34),
            "YELLOW_GREEN": (0,236,248),
            "GREEN": (89,152,26)
        }
        self.rand_color = list(self.colors.values())[random.randrange(len(self.colors))] # get a random colord
        self.ran_bg_index = random.randrange(len(self.backgrounds))

    def startup(self, persistent):
        self.persist = persistent

    def get_event(self, event):
        pass

    def update(self, dt):
        pass

    def draw(self, surface):
        pass

    # get random background image, scaled to screen dimensions
    def get_ran_bg(self):
        bg = pg.image.load("assets/backgrounds/" + self.backgrounds[self.ran_bg_index])
        return pg.transform.scale(bg, (self.screen_w,self.screen_h))

    # get a font render conveniently to then get rectangle and blit to screen
    def render_text(self, string, font_name, size, color):
        font = pg.font.Font("assets/fonts/" + font_name, size)
        return font.render(string, True, color)

    def load_sound(self, name):
        class NoneSound:
            def play(self):
                pass
        if not pg.mixer or not pg.mixer.get_init():
            return NoneSound()
        fullname = os.path.join("assets/sounds/", name)
        sound = pg.mixer.Sound(fullname)
        return sound
    

