import sys, pygame as pg
from states.base import BaseState
from states.startscreen import StartScreen
from states.mainmenu import MainMenu
from states.gameplay import GamePlay
from states.gameover import GameOver
from game import Game

pg.init()
screen = pg.display.set_mode((1920,1080))
states = {
    "START_SCREEN": StartScreen(),
    "MAIN_MENU": MainMenu(),
    "GAME_PLAY": GamePlay(),
    "GAME_OVER": GameOver()
}

game = Game(screen, states, "START_SCREEN")
game.run()

pg.quit
sys.exit()

