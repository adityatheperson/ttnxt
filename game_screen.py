import sys

import pygame
from pygame import KEYDOWN, QUIT

from game_core import Position, Game


class Gamescreen:
    def __init__(self):
        self.game = Game()
        pygame.init()
        self.surface = pygame.display.set_mode((660, 510))
        pygame.display.set_caption('TTNXT')
        pygame.time.set_timer(pygame.USEREVENT, 100)

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

        self.draw_circle(1, Position(630, 30))
        self.draw_circle(2, Position(330, 480))

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