import sys, pygame as pg
from mystates.base import BaseState
from mystates.startscreen import StartScreen
from mystates.mainmenu import MainMenu
from mystates.gameplay import GamePlay
from mystates.gameover import GameOver
from mygame import Game

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

