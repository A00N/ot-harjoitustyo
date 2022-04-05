import unittest

from levels import Levels

class TestLevels(unittest.TestCase):
    def setUp(self):
        self.levels = Levels()


    def test_grid_size(self):
        self.assertEqual(len(self.grid), 7)