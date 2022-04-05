import pygame
from levelList import *

WIDTH, HEIGHT = 600, 600
ROWS = COLS = 9
SQUARE_SIZE = WIDTH/COLS
LEVEL_LENGTH = 7
# Colors
DARKGRAY = (120, 120, 120)
CYAN = (180, 180, 255)
WHITE = (255, 255, 255)
LIGHTGRAY = (235, 235, 235)
BLACK = (0, 0, 0)
GRAY = (220, 220, 220)
GREEN = (125,255,0)
RED = (255,0,0)
YELLOW = (255, 255, 0)
ORANGE = (255,165,0)
PURPLE = (255,0,125)

#levels

LEVEL0 = (level0, level0_answer)
LEVEL1 = (level1, level1_answer)
LEVEL2 = (level2, level2_answer)