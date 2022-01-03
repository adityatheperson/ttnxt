import sys

import pygame
from pygame import KEYDOWN, QUIT

from game_core import Position, Game, Location, Playertype


class Gamescreen:
    def __init__(self):
        self.game = Game()
        pygame.init()
        self.surface = pygame.display.set_mode((660, 600))
        pygame.display.set_caption('TTNXT')
        pygame.time.set_timer(pygame.USEREVENT, 100)

    def draw_circle(self, player : Playertype, location: Location):
        if player == Playertype.PLAYER1:
            if location == Location.TOPLEFT:
                pygame.draw.circle(self.surface, (255, 0, 0), (30, 30), 15, 15)
                pygame.display.update()
            if location == Location.TOPCENTER:
                pygame.draw.circle(self.surface, (255, 0, 0), (330, 30), 15, 15)
                pygame.display.update()
            if location == Location.TOPRIGHT:
                pygame.draw.circle(self.surface, (255, 0, 0), (630, 30), 15, 15)
                pygame.display.update()
            if location == Location.MIDDLELEFT:
                pygame.draw.circle(self.surface, (255, 0, 0), (30, 255), 15, 15)
                pygame.display.update()
            if location == Location.MIDDLECENTER:
                pygame.draw.circle(self.surface, (255, 0, 0), (330, 255), 15, 15)
                pygame.display.update()
            if location == Location.MIDDLELRIGHT:
                pygame.draw.circle(self.surface, (255, 0, 0), (630, 255), 15, 15)
                pygame.display.update()
            if location == Location.BOTTOMLEFT:
                pygame.draw.circle(self.surface, (255, 0, 0), (30, 480), 15, 15)
                pygame.display.update()
            if location == Location.BOTTOMCENTER:
                pygame.draw.circle(self.surface, (255, 0, 0), (330, 480), 15, 15)
                pygame.display.update()
            if location == Location.BOTTOMRIGHT:
                pygame.draw.circle(self.surface, (255, 0, 0), (630, 480), 15, 15)
                pygame.display.update()

        if player == Playertype.PLAYER2:
            if location == Location.TOPLEFT:
                pygame.draw.circle(self.surface, (0, 0, 255), (30, 30), 15, 15)
                pygame.display.update()
            if location == Location.TOPCENTER:
                pygame.draw.circle(self.surface, (0, 0, 255), (330, 30), 15, 15)
                pygame.display.update()
            if location == Location.TOPRIGHT:
                pygame.draw.circle(self.surface, (0, 0, 255), (630, 30), 15, 15)
                pygame.display.update()
            if location == Location.MIDDLELEFT:
                pygame.draw.circle(self.surface, (0, 0, 255), (30, 255), 15, 15)
                pygame.display.update()
            if location == Location.MIDDLECENTER:
                pygame.draw.circle(self.surface, (0, 0, 255), (330, 255), 15, 15)
                pygame.display.update()
            if location == Location.MIDDLELRIGHT:
                pygame.draw.circle(self.surface, (0, 0, 255), (630, 255), 15, 15)
                pygame.display.update()
            if location == Location.BOTTOMLEFT:
                pygame.draw.circle(self.surface, (0, 0, 255), (30, 480), 15, 15)
                pygame.display.update()
            if location == Location.BOTTOMCENTER:
                pygame.draw.circle(self.surface, (0, 0, 255), (330, 480), 15, 15)
                pygame.display.update()
            if location == Location.BOTTOMRIGHT:
                pygame.draw.circle(self.surface, (0, 0, 255), (630, 480), 15, 15)
                pygame.display.update()

    def draw_screen(self):

        dialogue_font = pygame.font.SysFont('arial', 30)
        self.surface.fill((255, 255, 255))
        pygame.draw.line(self.surface, (0, 0, 0), (330, 30), (330, 480), 5)
        pygame.draw.line(self.surface, (0, 0, 0), (30, 30), (630, 480), 5)
        pygame.draw.line(self.surface, (0, 0, 0), (630, 30), (30, 480), 5)
        pygame.draw.line(self.surface, (0, 0, 0), (30, 255), (630, 255), 5)
        pygame.draw.line(self.surface, (0, 0, 0), (30, 30), (30, 480), 5)
        pygame.draw.line(self.surface, (0, 0, 0), (30, 30), (630, 30), 5)
        pygame.draw.line(self.surface, (0, 0, 0), (30, 480), (630, 480), 5)
        pygame.draw.line(self.surface, (0, 0, 0), (630, 480), (630, 30), 5)
        dialogue = dialogue_font.render("Place a point to start the game", True, (0, 0, 0))
        self.surface.blit(dialogue, (150, 550))

        pygame.display.flip()

    def run_game_loop(self):
        while True:  # main game loop
            for event in pygame.event.get():
                if event.type == pygame.USEREVENT:
                    self.draw_screen()
                    pygame.display.update()
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
