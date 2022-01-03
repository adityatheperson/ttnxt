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
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y


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