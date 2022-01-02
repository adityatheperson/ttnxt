import pygame, sys
from pygame.locals import *
from enum import Enum


class Playertype(Enum):
    PLAYER1 = 1
    PLAYER2 = 2


class Errors(Enum):
    NOPAWNSELECTED = 0
    ALREADYPAWNTHERE = 1
    POINTDOESNOTEXIST = 2
    OPPOSITEPAWN = 3
    SAMEPOINT = 4


class Position:
    def __init__(self):
        self.x = 0
        self.y = 0


class Game:

    def __init__(self):
        self.board = [[0, 0, 0],
                      [0, 0, 0],
                      [0, 0, 0]]
        self.player_turn = 1

    def get_board(self):
        return self.board

    def get_player_turn(self):
        return self.player_turn

    def get_pos(self, posx, posy):
        return self.board[posx][posy]

    def validate_point(self, point: Position):
        possible_points = [0, 1, 2]
        if point.x not in possible_points:
            return False
        if point.y not in possible_points:
            return False
        return True

    def move_piece(self, player: Playertype, frompos: Position, topos: Position):
        if not self.validate_point(frompos) or not self.validate_point(topos):
            return Errors.POINTDOESNOTEXIST
        if self.get_pos(frompos.x, frompos.y) == 0:
            return Errors.NOPAWNSELECTED
        if self.get_pos(topos.x, topos.y) != 0:
            return Errors.ALREADYPAWNTHERE
        if frompos.x == topos.x and frompos.y == topos.y:
            return Errors.SAMEPOINT
        if player != self.get_pos(frompos.x, frompos.y):
            return Errors.OPPOSITEPAWN
        self.board[topos.x][topos.y] = player
        return True


class Gamescreen:
    def __init__(self):
        pygame.init()
        self.surface = pygame.display.set_mode((660, 510))
        pygame.display.set_caption('TTNXT')

    def draw_circle(self, player, position: Position):
        if player == 1:
            pygame.draw.circle(self.surface, (255, 0, 0), (position.x, position.y), 15, 15)
            pygame.display.update()
        if player == 2:
            pygame.draw.circle(self.surface, (0, 0, 255), (position.x, position.y), 15, 15)
            pygame.display.update()

    def draw_screen(self):
        self.surface.fill((255, 255, 255))
        pygame.draw.line(self.surface, (0, 0, 0), (330, 30), (330, 480), 5)
        pygame.draw.line(self.surface, (0, 0, 0), (30, 30), (630, 480), 5)
        pygame.draw.line(self.surface, (0, 0, 0), (630, 30), (30, 480), 5)
        pygame.draw.line(self.surface, (0, 0, 0), (30, 255), (630, 255), 5)
        pygame.draw.line(self.surface, (0, 0, 0), (30, 30), (30, 480), 5)
        pygame.draw.line(self.surface, (0, 0, 0), (30, 30), (630, 30), 5)
        pygame.draw.line(self.surface, (0, 0, 0), (30, 480), (630, 480), 5)
        pygame.draw.line(self.surface, (0, 0, 0), (630, 480), (630, 30), 5)

        position = Position()
        position.x = 630
        position.y = 30
        self.draw_circle(1, position)
        position.x = 330
        position.y = 480
        self.draw_circle(2, position)

        pygame.display.flip()



    def run_game_loop(self):
        while True:  # main game loop
            for event in pygame.event.get():
                if event.type == KEYDOWN:
                    self.draw_screen()
                    pygame.display.update()
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()


screen = Gamescreen()
screen.run_game_loop()
