import random, time, sys, os, pygame as pg
from pygame.locals import *
from other import Dimmer, FPSCounter

""" The Game Class"""
class Game(object):
    def __init__(self, screen, states, start_state):
        self.done = False
        self.screen = screen
        self.clock = pg.time.Clock()
        self.fps = 60
        self.states = states
        self.state_name = start_state
        self.state = self.states[self.state_name]

    def event_loop(self):
        for event in pg.event.get():
            self.state.get_event(event)

    def flip_state(self):
        current_state = self.state_name
        next_state = self.state.next_state
        self.state.done = False
        self.state_name = next_state
        persistent = self.state.persist
        self.state = self.states[self.state_name]
        self.state.startup(persistent)

    def update(self, dt):
        if self.state.quit:
            self.done = True
        elif self.state.done:
            self.flip_state()
        self.state.update(dt)

    def draw(self):
        self.state.draw(self.screen)

    def run(self):
        while not self.done:
            dt = self.clock.tick(self.fps)
            self.event_loop()
            self.update(dt)
            self.draw()
            pg.display.update()


""" The Base Class """
# all other classes that are 'game states' will inherit from this class
class BaseState(object):
    def __init__(self):
        self.done = False
        self.quit = False
        self.next_state = None
        self.screen_rect = pg.display.get_surface().get_rect()
        self.persist = {}
        self.font = pg.font.Font("assets/fonts/RetroGaming.ttf", 30) # default font and font size
        self.backgrounds = os.listdir("./assets/backgrounds")
        self.screen_w = pg.display.Info().current_w
        self.screen_h = pg.display.Info().current_h
        self.dim = Dimmer(1)
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
        self.rand_color = list(self.colors.values())[random.randrange(len(self.colors))] # get a random color
        self.ran_bg_index = random.randrange(len(self.backgrounds)) # get a random index for the backgrounds

    def startup(self, persistent):
        self.persist = persistent

    def get_event(self, event):
        pass

    def update(self, dt):
        pass

    def draw(self, surface):
        pass

    # get random background image, scaled to screen dimensions
    def get_rand_bg(self):
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

    def draw_cursor(self, surface, x, y):
        if pg.MOUSEBUTTONDOWN: surface.blit(self.cursor_clicked,(x,y))
        else: surface.blit(self.cursor,(x,y)) 


""" The StartScreen Class"""
class StartScreen(BaseState):
    def __init__(self):
        super(StartScreen, self).__init__()
        self.next_state = "MAIN_MENU"
        self.time_active = 0
        self.title = self.render_text("Safari Match!", "StarBorn.ttf", 80, pg.Color("white")) 
        self.title_rect = self.title.get_rect(center=self.screen_rect.center)

    def update(self, dt):
        self.time_active += dt
        if self.time_active >= 2000:
            self.done = True

    def draw(self, surface):
        surface.blit(self.get_rand_bg(), (0,0))
        surface.blit(self.title, self.title_rect)


""" The MainMenu Class"""
class MainMenu(BaseState):
    def __init__(self):
        super(MainMenu, self).__init__()
        self.active_index = 0
        self.options = ["Play", "Exit"]
        self.next_state = "GAME_PLAY"
        self.game_logo = self.render_text("Safari Match!", "Starborn.ttf", 45, Color("white"))
        logo_position = (self.screen_rect.center[0], 100)
        self.game_logo_rect = self.game_logo.get_rect(center=logo_position)

    def render_options(self, index):
        if index == self.active_index:
            return self.render_text(self.options[index], "StarBorn.ttf", 50, Color("orange"))
        else: 
            return self.render_text(self.options[index], "StarBorn.ttf", 40, Color("white"))

    def get_text_position(self, text, index):
        center = (self.screen_rect.center[0], self.screen_rect.center[1] + (index * 70))
        return text.get_rect(center=center)

    def handle_action(self):
        if self.active_index == 0:
            self.done = True
        elif self.active_index == 1:
           self.quit = True

    def get_event(self, event):
        if event.type == QUIT:
            self.quit = True
        elif event.type == KEYUP:
            if event.key == K_UP:
                self.active_index = 1 if self.active_index <= 0 else 0
            elif event.key == K_DOWN:
                self.active_index = 0 if self.active_index >= 1 else 1
            elif event.key == K_RETURN:
                self.handle_action()
            elif event.key == K_ESCAPE:
                self.quit = True

    def draw(self, surface):
        surface.blit(self.get_rand_bg(), (0,0)) 
        surface.blit(self.game_logo, self.game_logo_rect)
        for index, option in enumerate(self.options):
            text_render = self.render_options(index)
            surface.blit(text_render, self.get_text_position(text_render, index))


""" The Pause Menu Class"""
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
        self.dim.dim(20,(10,10,10))
        surface.blit(self.title, self.title_rect)
        surface.blit(self.instructions1,self.instructions1_rect)
        surface.blit(self.instructions2, self.instructions2_rect)


""" The Game Over Class"""
class GameOver(BaseState):
    def __init__(self):
        super(GameOver, self).__init__()
        self.title = self.render_text("Game Over", "Upheavtt.ttf", 65, Color("white"))
        self.options = ["Retry", "Go Back"]
        self.next_state = "GAME_PLAY"

    def render_oprtions(self, index):
        if index == self.active_index:
            return self.render_text(self.options[index]), "StarBorn.ttf", 50, Color("orange")
        else: 
            return self.render_text(self.options[index]), "StarBorn.ttf", 40, Color("white")
    
    def handle_actions(self):
        if self.active_index == 0:
            self.done = True
        elif self.active_index == 1:
            self.next_state = "MAIN_MENU"
            self.done = True
    
    def get_event(self, event):
        if event.type == QUIT:
            self.quit = True
        elif event.type == KEYUP:
            if event.key == K_UP:
                self.active_index = 1 if self.active_index <= 0 else 0
            elif event.key == K_DOWN:
                self.active_index = 0 if self.active_index >= 1 else 1
            elif event.key == K_RETURN:
                self.handle_action()
            elif event.key == K_ESCAPE:
                self.quit = True
    
    def draw(self, surface):
        surface.blit(self.get_rand_bg(),(0,0))
        for index, option in enumerate(self.options):
            text_render = self.render_options(index)
            surface.blit(text_render, self.get_text_position(text_render, index))


""" The GamePlay Class"""
class GamePlay(BaseState):
    def __init__(self):
        super(GamePlay, self).__init__()
        self.rect = pg.Rect((0, 0), (80, 80))
        self.rect.center = self.screen_rect.center
        self.next_state = "PAUSE_MENU"
        self.names = ["bee", "cat", "cow", "elephant", "fox", "hen", "koala", "parrot", "penguin", "toucan", "turtle"]
        self.active_index = 0

    def get_event(self, event):
        if event.type == pg.QUIT:
            self.quit = True
        elif event.type == KEYUP:
            if event.key == K_LEFT or event.key == K_a:
                if self.active_index > 0: self.active_index -= 1 
                else: self.active_index = 3
            if event.key == K_RIGHT or event.key == K_d:
                if self.active_index < 3: self.active_index += 1
                else: self.active_index = 0
            if event.key == K_SPACE or event.key == K_ESCAPE:
                self.done = True

    def draw(self, surface):
        # background
        surface.blit(self.get_rand_bg(),(0,0))
        # get the cards in the damn screen
        card_list = self.get_card_list()
        name_deck = self.get_name_deck()
        x = 0
        for i, index in enumerate(name_deck):
            surface.blit(card_list[index],((self.screen_rect.center[0]/2)+x, self.screen_rect.center[1]))
            x = i*128

    # the same index in cards and names refers to the same animal
    def get_card_list(self):
        cards = []        
        for i, name in enumerate(self.names):
            cards.append(pg.image.load("assets/animals/" + self.names[i] + ".png"))
        return cards 

    # get a list with the indexes of 4 random cards
    def get_name_deck(self): 
        deck = []
        for i in range(4): deck.append(random.randrange(len(self.names)))
        return deck


""" Executing the state machine """

# initialize pygame
pg.init()

# get resolution
screen_w = pg.display.Info().current_w
screen_h = pg.display.Info().current_h

# set up display
screen = pg.display.set_mode((screen_w,screen_h))
pg.display.set_caption("Safari Match!")
pg.display.set_icon(pg.image.load("assets/sprites/logo.png"))
pg.mouse.set_visible(False)

# the game states
states = {
    "START_SCREEN": StartScreen(),
    "MAIN_MENU": MainMenu(),
    "GAME_PLAY": GamePlay(),
    "PAUSE_MENU": PauseMenu(),
    "GAME_OVER": GameOver()
}

# Run the game (the state machine)
game = Game(screen, states, "START_SCREEN")
game.run() 
pg.quit()


