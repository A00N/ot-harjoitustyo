import unittest
from levels import *


class TestGrid(unittest.TestCase):
    def setUp(self):
        self.grid = Grid()

    def test_grid_size(self):
        self.assertEqual(len(self.grid), 7)
