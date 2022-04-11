import pygame
from constants import SQUARE_SIZE


class Marker:
    def __init__(self, row, col, color):
        self.row = row
        self.col = col
        self.color = color
        self.x = 0
        self.y = 0
        self.calc_pos()

    # Check for position
    def calc_pos(self):
        self.x = SQUARE_SIZE * self.col + SQUARE_SIZE // 2
        self.y = SQUARE_SIZE * self.row + SQUARE_SIZE // 2

    # Draw self
    def draw(self, win):
        box = pygame.Rect(self.x-25, self.y-25, 50, 50)
        pygame.draw.rect(win, self.color, box)
