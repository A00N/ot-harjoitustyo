import pygame
from constants import BLACK, GRAY, CYAN, SQUARE_SIZE

class Numbers:
    def __init__(self,row, col, value, color):
        self.row = row
        self.col = col
        self.value = value
        self.color = color
        self.x = 0
        self.y = 0
        self.calc_pos()

    #Check for position
    def calc_pos(self):
        self.x = SQUARE_SIZE * self.col + SQUARE_SIZE // 2
        self.y = SQUARE_SIZE * self.row + SQUARE_SIZE // 2

    #Draw
    def draw(self, win):
        radius = SQUARE_SIZE//2
        pygame.draw.circle(win,self.color,(self.x, self.y), radius-10)

    def returnvalue(self):
        return self.value

