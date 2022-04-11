import pygame
from levelList import *

WIDTH, HEIGHT = 600, 600
ROWS = COLS = 9
SQUARE_SIZE = WIDTH / COLS
LEVEL_LENGTH = 7
FPS = 60
# Colors
DARKGRAY = (120, 120, 120)
CYAN = (180, 180, 255)
WHITE = (255, 255, 255)
LIGHTGRAY = (235, 235, 235)
BLACK = (0, 0, 0)
GRAY = (220, 220, 220)
GREEN = (125, 255, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
ORANGE = (255, 165, 0)
PURPLE = (255, 0, 125)
LIGHTBLUE = (180, 180, 255)
PINK = (255, 192, 192)

# Text options
pygame.init()
font = pygame.font.SysFont(None, 50)


def draw_text(text, font, color, surface, x, y):
    textobj = font.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.center = (x, y)
    surface.blit(textobj, textrect)


