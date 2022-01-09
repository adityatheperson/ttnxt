from enum import Enum
import chime


class Playertype(Enum):
    NOPLAYER = 0
    PLAYER1 = 1
    PLAYER2 = 2


class Errors(Enum):
    NOPAWNSELECTED = 0
    ALREADYPAWNTHERE = 1
    POINTDOESNOTEXIST = 2
    OPPOSITEPAWN = 3
    SAMEPOINT = 4


class Location(Enum):
    TOPLEFT = 0
    TOPCENTER = 1
    TOPRIGHT = 2
    MIDDLELEFT = 3
    MIDDLECENTER = 4
    MIDDLERIGHT = 5
    BOTTOMLEFT = 6
    BOTTOMCENTER = 7
    BOTTOMRIGHT = 8


class Position:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y


class Game:

    def __init__(self):
        self.board = [0, 0, 0, 0, 0, 0, 0, 0, 0]
        self.player_turn = 1
        self.pawns_placed = 0
        self.pawn_selected = None

    def get_board(self):
        return self.board

    def get_player_turn(self):
        return self.player_turn

    def get_pos(self, location: Location):
        return self.board[location.value]
        # return self.board[posx][posy]

    def validate_point(self, location: Location):
        possible_points = [0, 1, 2, 3, 4, 5, 6, 7, 8]
        if location.value not in possible_points:
            return False
        return True

    def check_if_won(self, player : Playertype, list):
        if list[0] == player and list[1] == player and list[2] == player:
            chime.theme('zelda')
            chime.success()
            return True
        if list[3] == player and list[4] == player and list[5] == player:
            chime.theme('zelda')
            chime.success()
            return True
        if list[6] == player and list[7] == player and list[8] == player:
            chime.theme('zelda')
            chime.success()
            return True
        if list[0] == player and list[3] == player and list[6] == player:
            chime.theme('zelda')
            chime.success()
            return True
        if list[1] == player and list[4] == player and list[7] == player:
            chime.theme('zelda')
            chime.success()
            return True
        if list[2] == player and list[5] == player and list[8] == player:
            chime.theme('zelda')
            chime.success()
            return True
        if list[0] == player and list[4] == player and list[8] == player:
            chime.theme('zelda')
            chime.success()
            return True
        if list[2] == player and list[4] == player and list[6] == player:
            chime.theme('zelda')
            chime.success()
            return True
        return False
    def check_possible_moves(self, location : Location):
        if location == Location.TOPLEFT:
            return[Location.TOPCENTER, Location.MIDDLECENTER, Location.MIDDLELEFT]
        if location == Location.TOPCENTER:
            return[Location.TOPLEFT, Location.MIDDLECENTER, Location.TOPRIGHT]
        if location == Location.TOPRIGHT:
            return[Location.TOPCENTER, Location.MIDDLECENTER, Location.MIDDLERIGHT]
        if location == Location.MIDDLELEFT:
            return[Location.TOPLEFT, Location.MIDDLECENTER, Location.BOTTOMLEFT]
        if location == Location.MIDDLECENTER:
            return[Location.TOPLEFT, Location.TOPCENTER, Location.TOPRIGHT, Location.MIDDLELEFT, Location.MIDDLERIGHT, Location. BOTTOMLEFT, Location.BOTTOMCENTER, Location.BOTTOMRIGHT]
        if location == Location.MIDDLERIGHT:
            return[Location.TOPRIGHT, Location.MIDDLECENTER, Location.BOTTOMRIGHT]
        if location == Location.BOTTOMLEFT:
            return[Location.MIDDLELEFT, Location.MIDDLECENTER, Location.BOTTOMCENTER]
        if location == Location.BOTTOMCENTER:
            return[Location.BOTTOMLEFT, Location.MIDDLECENTER, Location.BOTTOMRIGHT]
        if location == Location.BOTTOMRIGHT:
            return[Location.BOTTOMCENTER, Location.MIDDLECENTER, Location.MIDDLERIGHT]
        return False
    def check_if_nearby(self, mouseposx, mouseposy):
        marginoferror = 50

        startpointx = 30 - marginoferror / 2
        startpointy = 30 - marginoferror / 2
        if startpointx <= mouseposx <= startpointx + 50:
            if startpointy <= mouseposy <= startpointy + 50:
                return Location.TOPLEFT
        startpointx = 330 - marginoferror / 2
        startpointy = 30 - marginoferror / 2
        if startpointx <= mouseposx <= startpointx + 50:
            if startpointy <= mouseposy <= startpointy + 50:
                return Location.TOPCENTER

        startpointx = 630 - marginoferror / 2
        startpointy = 30 - marginoferror / 2
        if startpointx <= mouseposx <= startpointx + 50:
            if startpointy <= mouseposy <= startpointy + 50:
                return Location.TOPRIGHT

        startpointx = 30 - marginoferror / 2
        startpointy = 255 - marginoferror / 2
        if startpointx <= mouseposx <= startpointx + 50:
            if startpointy <= mouseposy <= startpointy + 50:
                return Location.MIDDLELEFT

        startpointx = 330 - marginoferror / 2
        startpointy = 255 - marginoferror / 2
        if startpointx <= mouseposx <= startpointx + 50:
            if startpointy <= mouseposy <= startpointy + 50:
                return Location.MIDDLECENTER

        startpointx = 630 - marginoferror / 2
        startpointy = 255 - marginoferror / 2
        if startpointx <= mouseposx <= startpointx + 50:
            if startpointy <= mouseposy <= startpointy + 50:
                return Location.MIDDLERIGHT

        startpointx = 30 - marginoferror / 2
        startpointy = 480 - marginoferror / 2
        if startpointx <= mouseposx <= startpointx + 50:
            if startpointy <= mouseposy <= startpointy + 50:
                return Location.BOTTOMLEFT

        startpointx = 330 - marginoferror / 2
        startpointy = 480 - marginoferror / 2
        if startpointx <= mouseposx <= startpointx + 50:
            if startpointy <= mouseposy <= startpointy + 50:
                return Location.BOTTOMCENTER

        startpointx = 630 - marginoferror / 2
        startpointy = 480 - marginoferror / 2
        if startpointx <= mouseposx <= startpointx + 50:
            if startpointy <= mouseposy <= startpointy + 50:
                return Location.BOTTOMRIGHT

    def move_piece(self, player: Playertype, fromlos: Location, tolos: Location):
        if not self.validate_point(tolos) or not self.validate_point(fromlos):

            return Errors.POINTDOESNOTEXIST
        if self.get_pos(fromlos) == 0:
            chime.theme('mario')
            chime.warning()
            return Errors.NOPAWNSELECTED
        if self.get_pos(tolos) != 0:
            chime.theme('mario')
            chime.warning()
            return Errors.ALREADYPAWNTHERE
        if tolos.value == fromlos.value:
            chime.theme('mario')
            chime.warning()
            return Errors.SAMEPOINT
        if player != self.get_pos(fromlos):
            chime.theme('mario')
            chime.warning()
            return Errors.OPPOSITEPAWN
        self.board[tolos.value] = player
        self.board[fromlos.value] = 0

        return True

    def place_piece(self, player: Playertype, tolos: Location):
        if not self.validate_point(tolos):
            return False
        if self.get_pos(tolos) != 0:
            return False
        self.board[tolos.value] = player

        return True
