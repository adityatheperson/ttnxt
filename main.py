from game_core import Game, Location, Playertype
from game_screen import Gamescreen

game = Game()
# print(game.validate_point(Location.TOPLEFT.value))
screen = Gamescreen()
screen.run_game_loop()
