import unittest
from entities.constants import *

WIDTH, HEIGHT = 600, 600
ROWS = COLS = 9
SQUARE_SIZE = WIDTH / COLS
LEVEL_LENGTH = 7
RED = (255, 0, 0)
WHITE = (255, 255, 255)
FPS = 60


class TestConstants(unittest.TestCase):
    def setUp(self):
        self.width = WIDTH
        self.height = HEIGHT
        self.red = RED
        self.level_length = LEVEL_LENGTH
        self.square_size = SQUARE_SIZE
        self.white = (255, 255, 255)
        self.fps = FPS

    def test_color_red(self):
        self.assertEqual(self.red, (255, 0, 0))

    def test_color_white(self):
        self.assertEqual(self.white, (255, 255, 255))

    def test_window_size(self):
        self.assertEqual(self.width*self.height, 360000)

    def test_fps(self):
        self.assertEqual(self.fps, 60)

    def test_level_length(self):
        self.assertEqual(self.level_length, 7)

    def test_square_size(self):
        self.assertEqual(self.square_size, 600/9)
