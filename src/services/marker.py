import pygame
from entities.constants import SQUARE_SIZE


class Marker:
    """ Luokka, joka hallinnoi pelaajan merkkejä sekä niiden arvoja

    Attributes:
        row: Merkin sijainti rivillä
        col: Merkin sijainti kolumnissa
        color: Merkin väri
    """

    def __init__(self, row, col, color):
        """ Luokan konstruktori, joka määrittää merkin arvot.
            Arvot ovat sijainti ruudukossa sekä väri

        Args:
            row: Merkin sijainti rivillä
            col: Merkin sijainti kolumnissa
            color: Merkin väri
        """
        self.x = 0
        self.y = 0
        self.row = row
        self.col = col
        self.color = color
        self.calc_pos()

    def calc_pos(self):
        """ Laskee, merkin sijainnin

        """
        self.x = SQUARE_SIZE * self.col + SQUARE_SIZE // 2
        self.y = SQUARE_SIZE * self.row + SQUARE_SIZE // 2

    # Draw self
    def draw(self, win):
        """ Piirtää merkin annettuun taustaan.

        Args:
            win: muuttuja, johon piirretään merkki itse
        """
        box = pygame.Rect(self.x-25, self.y-25, 50, 50)
        pygame.draw.rect(win, self.color, box)
