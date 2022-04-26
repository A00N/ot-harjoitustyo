import unittest
from services.levels import *
from entities.level_list import *



level = level0
level_answer = level0_answer


class TestGrid(unittest.TestCase):
    def setUp(self):
        self.grid = Grid(level, level_answer)
        self.level = level
        self.level_answer = level_answer
        self.RED = (255, 0, 0)
        self.WIDTH = self.HEIGHT = 600

    def test_grid_size(self):
        self.assertEqual(len(self.grid.grid), 7)

    def test_color_red(self):
        self.assertEqual(self.RED, (255, 0, 0))

    def test_window_size(self):
        self.assertEqual(self.WIDTH*self.HEIGHT, 360000)

    # def test_check_for_completion(self):
