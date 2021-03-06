import sys
import chime

import pygame
from pygame import KEYDOWN, QUIT

from game_core import Position, Game, Location, Playertype

BLUE = (0, 0, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)


class Gamescreen:
    def __init__(self):
        self.game = Game()
        pygame.init()
        self.surface = pygame.display.set_mode((660, 600))
        pygame.display.set_caption('TTNXT')
        chime.theme('mario')

        self.next_turn = Playertype.PLAYER1
        self.game_won = False
        self.game_winner = 0
        self.game_mode = None

    def draw_pawn(self, player: Playertype, location: Location):
        if player == Playertype.PLAYER1:
            self.draw_circle(location, rgb=RED)
        if player == Playertype.PLAYER2:
            self.draw_circle(location, rgb=BLUE)

    def draw_circle(self, location, rgb):
        if location == Location.TOPLEFT:
            pygame.draw.circle(self.surface, rgb, (30, 30), 15, 15)
            pygame.display.update()
        if location == Location.TOPCENTER:
            pygame.draw.circle(self.surface, rgb, (330, 30), 15, 15)
            pygame.display.update()
        if location == Location.TOPRIGHT:
            pygame.draw.circle(self.surface, rgb, (630, 30), 15, 15)
            pygame.display.update()
        if location == Location.MIDDLELEFT:
            pygame.draw.circle(self.surface, rgb, (30, 255), 15, 15)
            pygame.display.update()
        if location == Location.MIDDLECENTER:
            pygame.draw.circle(self.surface, rgb, (330, 255), 15, 15)
            pygame.display.update()
        if location == Location.MIDDLERIGHT:
            pygame.draw.circle(self.surface, rgb, (630, 255), 15, 15)
            pygame.display.update()
        if location == Location.BOTTOMLEFT:
            pygame.draw.circle(self.surface, rgb, (30, 480), 15, 15)
            pygame.display.update()
        if location == Location.BOTTOMCENTER:
            pygame.draw.circle(self.surface, rgb, (330, 480), 15, 15)
            pygame.display.update()
        if location == Location.BOTTOMRIGHT:
            pygame.draw.circle(self.surface, rgb, (630, 480), 15, 15)
            pygame.display.update()

    def draw_starting_screen(self):
        self.surface.fill((255, 255, 255))
        dialogue_font = pygame.font.SysFont('arial', 40)
        dialogue = dialogue_font.render("Press 1 for Single Player", True, BLUE)
        dialogue2 = dialogue_font.render("Press 2 for Multiplayer ", True, RED)
        self.surface.blit(dialogue, (120, 100))
        self.surface.blit(dialogue2, (130, 350))

    def draw_screen(self):

        self.draw_background()
        self.draw_circles()

        pygame.display.flip()

    def draw_circles(self):
        for i in range(0, 9):
            self.draw_pawn(Playertype(self.game.board[i]), Location(i))

        if self.game.pawn_selected is not None:
            self.draw_circle(self.game.pawn_selected, GREEN)

    def draw_background(self):
        dialogue_font = pygame.font.SysFont('arial', 20)
        dialogue_font2 = pygame.font.SysFont('arial', 15)
        self.surface.fill((255, 255, 255))
        pygame.draw.line(self.surface, (0, 0, 0), (330, 30), (330, 480), 5)
        pygame.draw.line(self.surface, (0, 0, 0), (30, 30), (630, 480), 5)
        pygame.draw.line(self.surface, (0, 0, 0), (630, 30), (30, 480), 5)
        pygame.draw.line(self.surface, (0, 0, 0), (30, 255), (630, 255), 5)
        pygame.draw.line(self.surface, (0, 0, 0), (30, 30), (30, 480), 5)
        pygame.draw.line(self.surface, (0, 0, 0), (30, 30), (630, 30), 5)
        pygame.draw.line(self.surface, (0, 0, 0), (30, 480), (630, 480), 5)
        pygame.draw.line(self.surface, (0, 0, 0), (630, 480), (630, 30), 5)
        dialogue = dialogue_font.render("", True, (0, 0, 0))
        actor = self.next_turn.name
        if self.game.pawns_placed == 0:
            dialogue = dialogue_font.render(f"{actor} - Place a point to start the game", True, (0, 0, 0))
        elif self.game.pawns_placed < 6:
            dialogue = dialogue_font.render(f"{actor} - Click a unused corner to place a pawn", True, (0, 0, 0))
        else:
            if self.game.pawn_selected is None:
                dialogue = dialogue_font.render(f"{actor} - Select a Pawn to Move", True, (0, 0, 0))
            else:
                dialogue = dialogue_font2.render(
                    f"{actor} - Select a Empty Space to Move your pawn OR click on point to unselect", True, (0, 0, 0))
        if self.game_won and self.game_winner == 1:
            dialogue = dialogue_font.render("PLAYER 1 YOU WON!!!", True, RED)
        if self.game_won and self.game_winner == 2:
            dialogue = dialogue_font.render("PLAYER 2 YOU WON!!!", True, BLUE)

        self.surface.blit(dialogue, (30, 550))

    def run_game_loop(self):
        while self.game_mode is None:
            self.draw_starting_screen()
            pygame.display.update()
            while self.game_mode is None:  # main game loop
                for event in pygame.event.get():
                    if event.type == QUIT:
                        pygame.quit()
                        sys.exit()
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_1:
                            self.game_mode = 1
                        else:
                            if event.key == pygame.K_2:
                                self.game_mode = 2

        if self.game_mode == 2:
            self.draw_screen()
            pygame.display.update()
            while True:  # main game loop
                for event in pygame.event.get():
                    if event.type == QUIT:
                        pygame.quit()
                        sys.exit()
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if not self.game_won:
                            click_location = self.game.check_if_nearby(pygame.mouse.get_pos()[0],
                                                                       pygame.mouse.get_pos()[1])
                            if click_location is not None:
                                self.play_turn(click_location)
                                if self.game.check_if_won(Playertype.PLAYER1, self.game.board):
                                    self.game_won = True
                                    self.game_winner = 1
                                if self.game.check_if_won(Playertype.PLAYER2, self.game.board):
                                    self.game_won = True
                                    self.game_winner = 2
                                self.draw_screen()
                                pygame.display.update()
                        else:
                            self.draw_screen()
                            pygame.display.update()
        if self.game_mode == 2:
            print("hoi")

    def play_turn(self, click_location):
        # Check if it is place or move
        if self.game.pawns_placed < 6:
            if self.game.place_piece(self.next_turn, click_location):
                self.switch_player()
                self.game.pawns_placed += 1
        else:
            if self.game.pawn_selected is None:
                if self.game.get_pos(click_location) == self.next_turn:
                    self.game.pawn_selected = click_location
                else:
                    self.beep_error()
            else:
                if not click_location == self.game.pawn_selected:
                    if click_location in self.game.check_possible_moves(self.game.pawn_selected):
                        if self.game.move_piece(self.next_turn, self.game.pawn_selected, click_location) == True:
                            self.game.pawn_selected = None
                            self.switch_player()
                    else:
                        chime.warning()
                else:
                    self.game.pawn_selected = None

    def beep_error(self):
        chime.warning()

    def switch_player(self):
        chime.info()
        if self.next_turn == Playertype.PLAYER1:
            self.next_turn = Playertype.PLAYER2
        else:
            self.next_turn = Playertype.PLAYER1
