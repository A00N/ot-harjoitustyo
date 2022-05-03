from entities.constants import SQUARE_SIZE, draw_text, text_font, BLACK, pygame


class Numbers:
    """ Luokka, joka hallinnoi tason merkkejä ja niiden arvoja

        Attributes:
            row: Merkin sijainti rivillä
            col: Merkin sijainti kolumnissa
            value: merkin arvo
            color: Merkin väri
    """

    def __init__(self, row, col, value, color):
        """ Luokan konstruktori, joka määrittää merkin arvot.
        Arvot ovat sijainti ruudukossa, merkin arvo sekä väri

        Args:
            row: Merkin sijainti rivillä
            col: Merkin sijainti kolumnissa
            value: Merkin arvo
            color: Merkin väri
        """

        self.row = row
        self.col = col
        self.value = value
        self.color = color
        self.x = 0
        self.y = 0
        self.calc_pos()

    def calc_pos(self):
        """ Laskee, merkin sijainnin

        """
        self.x = int(SQUARE_SIZE * self.col + SQUARE_SIZE // 2)
        self.y = int(SQUARE_SIZE * self.row + SQUARE_SIZE // 2)

    def draw(self, win):
        """ Piirtää merkin annettuun taustaan.

        Args:
            win: muuttuja, johon piirretään merkki itse
        """
        radius = int(SQUARE_SIZE//2)-10
        pygame.draw.circle(win, self.color, (self.x, self.y), radius)
        draw_text(str(self.value), text_font, BLACK, win, self.x, self.y)

    def returnvalue(self):
        """

        Returns:
            Palauttaa merkin arvon
        """
        return self.value
