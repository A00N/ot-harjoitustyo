import pygame
from constants import *
from marker import Marker
from numberMarker import Numbers
import levelList

class Grid:
    def __init__(self):
        self.grid = []
        self.create_level(levelList.level2)
        self.answer = [(0,0,0,0,0),(0,0,0,0,0),(0,0,0,0,0),(0,0,0,0,0),(0,0,0,0,0)]


    #Draw the grid background
    def draw_grid(self, win):
        win.fill(WHITE)
        for row in range(ROWS):
            for col in range(row % 2, COLS, 2):
                if col < 7 and row > 1 and row < 7 and col > 1:
                    pygame.draw.rect(win, GRAY, (row*SQUARE_SIZE, col*SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))

    #Draw rest
    def draw(self, win):
        self.draw_grid(win)
        for row in range(LEVEL_LENGTH):
            for col in range(LEVEL_LENGTH):
                image = self.grid[row][col]
                if image != 0:
                    image.draw(win)

    #Create the level from given list
    def create_level(self,level):
        for row in range(LEVEL_LENGTH):
            self.grid.append([])
            for col in range(LEVEL_LENGTH):
                if level[row][col] != 0:
                    value = level[row][col]
                    if value == 1:
                        COLOR = CYAN
                    if value == 2:
                        COLOR = GREEN
                    if value == 3:
                        COLOR = YELLOW
                    if value == 4:
                        COLOR = ORANGE
                    if value == 5:
                        COLOR = RED
                    self.grid[row].append(Numbers(row, col, value , COLOR))
                    print(Numbers(row, col, value , CYAN).value)
                else:
                    self.grid[row].append(0)

    # Check for placable marker
    def grid_check(self, row, col):
        if  row < 7:
            if col < 7:
                if self.grid[row][col] == 0:
                    return True
        return False

    #Place new marker
    def new_marker(self,row,col, color):
        if row>1 and row <7:
            if col>1 and col <7:
                if color == DARKGRAY:
                    value = -1
                else:
                    value = -2

                self.grid[row][col] = Marker(row, col, color)


    #Remove marker
    def remove_marker(self,row,col):
        if row>1 and row <7:
            if col>1 and col <7:
                self.grid[row][col] = 0

    def check_for_complition(self):
        sum=0
        for row in range(LEVEL_LENGTH):
            for col in range(LEVEL_LENGTH):
                if row > 1 and row < 7:
                    if col > 1 and col < 7:
                        if self.grid[row][col] != 0:
                            sum +=1
        if sum == 25:
            if self.answer == levelList.level2_answer:
                print("OIKEIN")
            else:
                print("Väärin")




