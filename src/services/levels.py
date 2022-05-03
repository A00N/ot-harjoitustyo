from entities.constants import *
from services.marker import Marker
from services.number_marker import Numbers


class Grid:
    """Luokka, joka hallinnoi ruudukkon piirtämisen sekä sen tapahtumat

    Attributes:
        level: Tason tiedot taulukossa
        level_answer: Tason vastaus taulukossa
    """
    def __init__(self, level, level_answer):
        """ Luokan konstruktori, joka hallinnoi, että taso ja sen vastaus ovat oikeat

        Args:
            level: Tason tiedot taulukossa
            level_answer: Tason vastaus taulukossa
        """
        self.grid = []
        self.level = level
        self.level_answer = level_answer
        self.create_level(self.level)
        self.answer = [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [
            0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]
        self.completed = False

    def draw_grid(self, win):
        """ Piirtää ruudukon ikkunaan ennaltamääritettyjen arvojen mukaan

        Args:
            win: muuttuja, johon ruudukko piirtyy
        """
        win.fill(WHITE)
        for row in range(ROWS):
            for col in range(row % 2, COLS, 2):
                if 7 > col > 1 and 1 < row < 7:
                    pygame.draw.rect(
                        win, GRAY, (row * SQUARE_SIZE, col * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))

    def draw(self, win):
        """ Piirtää taustan

        Args:
            win: muuttuja, johon ruudukko piirtyy
        """
        self.draw_grid(win)
        for row in range(LEVEL_LENGTH):
            for col in range(LEVEL_LENGTH):
                image = self.grid[row][col]
                if image != 0:
                    image.draw(win)

    def create_level(self, level):
        """ Luo pelin vaativat merkinnät ruudukkoon luoden tason lisäämällä taulukkoon arvoja.

        Args:
            level: mikä taso kyseessä sekä sen arvot
        """
        for row in range(LEVEL_LENGTH):
            self.grid.append([])
            for col in range(LEVEL_LENGTH):
                if level[row][col] != 0:
                    value = level[row][col]
                    if value == 1:
                        color = CYAN
                    if value == 2:
                        color = GREEN
                    if value == 3:
                        color = YELLOW
                    if value == 4:
                        color = ORANGE
                    if value == 5:
                        color = RED
                    self.grid[row].append(Numbers(row, col, value, color))
                    print(Numbers(row, col, value, CYAN).value)
                else:
                    self.grid[row].append(0)

    def grid_check(self, row, col):
        """ Tarkistaa, onko hiiri ruudukossa sellaisessa kohdassa, jota voi klikata.
         Mikäli voi, palauttaa se että siihen voi lisätä merkin.

        Args:
            row: rivin arvo
            col: kolumnin arvo

        Returns:
            True jos on kohdassa jota voi klikata, False jos ei ole
        """
        if row < 7:
            if col < 7:
                if self.grid[row][col] == 0:
                    return True
        return False

    def new_marker(self, row, col, color):
        """ Luo uuden merkin ruudukkoon.

        Args:
            row: rivin arvo
            col: kolumnin arvo
            color: merkin väri
        """

        if 1 < row < 7:
            if 1 < col < 7:
                if color == DARKGRAY:
                    value = -1
                    self.answer[row - 2][col - 2] = value
                else:
                    value = -2
                    self.answer[row - 2][col - 2] = value
                self.grid[row][col] = Marker(row, col, color)

    def remove_marker(self, row, col):
        """ Poistaa merkinnän valitusta kohdasta ruudukossa

        Args:
            row: rivin arvo
            col: kolumnin arvo
        """
        if 1 < row < 7:
            if 1 < col < 7:
                self.grid[row][col] = 0
                self.answer[row - 2][col - 2] = 0

    def check_for_complition(self):
        """ Tarkistaa, onko taso suoritettu.
         Mikäli on, muuttuu self.completedin arvo True:ksi, muulloin False

        """
        markersum = 0
        for row in range(LEVEL_LENGTH):
            for col in range(LEVEL_LENGTH):
                if 1 < row < 7:
                    if 1 < col < 7:
                        if self.grid[row][col] != 0:
                            markersum += 1
        print(markersum)
        if markersum == 25:
            if self.answer == self.level_answer:
                print("Oikein")
                self.completed = True
            else:
                print("Väärin")
                self.completed = False

    def is_completed(self, win):
        """ Mikäli taso on suoritettu, piirää funktio näytölle tekstin "Läpäisty"

        """
        if self.completed:
            button_completed = pygame.Rect(
                WIDTH / 2 - 100, HEIGHT / 10 * 8, 200, 50)
            pygame.draw.rect(win, PURPLE, button_completed)
            draw_text("Läpäisty", text_font, WHITE, win,
                      WIDTH / 2, HEIGHT / 10 * 8 + 25)
