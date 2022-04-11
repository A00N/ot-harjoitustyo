import unittest
from levels import *


class TestGrid(unittest.TestCase):
    def setUp(self):
        self.grid = Grid()
        self.RED = (255, 0, 0)
        self.WIDTH = self.HEIGHT = 600

    def test_grid_size(self):
        self.assertEqual(len(self.grid.grid), 7)

    def test_color_red(self):
        self.assertEqual(self.RED, (255, 0, 0))

    def test_window_size(self):
        self.assertEqual(self.WIDTH*self.HEIGHT, 360000)
