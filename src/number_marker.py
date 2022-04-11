import pygame
from constants import *


class Numbers:
    def __init__(self, row, col, value, color):
        self.row = row
        self.col = col
        self.value = value
        self.color = color
        self.x = 0
        self.y = 0
        self.calc_pos()

    # Check for position
    def calc_pos(self):
        self.x = int(SQUARE_SIZE * self.col + SQUARE_SIZE // 2)
        self.y = int(SQUARE_SIZE * self.row + SQUARE_SIZE // 2)

    # Draw
    def draw(self, win):
        radius = int(SQUARE_SIZE//2)-10
        pygame.draw.circle(win, self.color, (self.x, self.y), radius)
        draw_text(str(self.value), font, BLACK, win, self.x, self.y)

    def returnvalue(self):
        return self.value
