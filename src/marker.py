import pygame
from constants import SQUARE_SIZE


class Marker:
    def __init__(self, row, col, color):
        self.row = row
        self.col = col
        self.color = color
        self.xx = 0
        self.yy = 0
        self.calc_pos()

    # Check for position

    def calc_pos(self):
        self.xx = SQUARE_SIZE * self.col + SQUARE_SIZE // 2
        self.yy = SQUARE_SIZE * self.row + SQUARE_SIZE // 2

    # Draw self
    def draw(self, win):
        box = pygame.Rect(self.xx-25, self.yy-25, 50, 50)
        pygame.draw.rect(win, self.color, box)
