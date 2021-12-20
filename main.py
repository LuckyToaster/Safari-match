import sys, pygame as pg
from states.base import BaseState
from states.startscreen import StartScreen
from states.mainmenu import MainMenu
from states.gameplay import GamePlay
from states.pausemenu import PauseMenu
from game import Game

# initialize pygame
pg.init()

# get resolution
screen_w = pg.display.Info().current_w
screen_h = pg.display.Info().current_h

# set up display
screen = pg.display.set_mode((screen_w,screen_h))
pg.display.set_caption("Safari Match!")
pg.display.set_icon(pg.image.load("assets/sprites/logo.png"))

# the game states
states = {
    "START_SCREEN": StartScreen(),
    "MAIN_MENU": MainMenu(),
    "GAME_PLAY": GamePlay(),
    "PAUSE_MENU": PauseMenu()
}

# Run the game (the state machine)
game = Game(screen, states, "START_SCREEN")
game.run() 
pg.quit()
sys.exit()

