import unittest
from services.marker import *

row = 2
col = 2
color = (0, 0, 0)


class TestMarker(unittest.TestCase):
    def setUp(self):
        self.marker = Marker(row, col, color)
        self.row = row
        self.col = col
        self.color = color

    def test_color_black(self):
        self.assertEqual(self.color, (0, 0, 0))

    def test_col(self):
        self.assertEqual(self.col, 2)

    def test_row(self):
        self.assertEqual(self.row, 2)
