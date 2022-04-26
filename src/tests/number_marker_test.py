import unittest
from services.number_marker import *

row = 2
col = 2
value = 2
color = (0, 0, 0)


class TestMarker(unittest.TestCase):
    def setUp(self):
        self.number = Numbers(row, col, value, color)
        self.row = row
        self.col = col
        self.value = value
        self.color = color

    def test_color_black(self):
        self.assertEqual(self.color, (0, 0, 0))

    def test_col(self):
        self.assertEqual(self.col, 2)

    def test_row(self):
        self.assertEqual(self.row, 2)

    def test_value(self):
        self.assertEqual(self.value, 2)
