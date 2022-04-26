from entities.constants import *
from services.marker import Marker
from services.number_marker import Numbers


class Grid:
    def __init__(self, level, level_answer):
        self.grid = []
        self.level = level
        self.level_answer = level_answer
        self.create_level(self.level)
        self.answer = [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [
            0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]
        self.completed = False

    # Draw the grid background
    def draw_grid(self, win):
        win.fill(WHITE)
        for row in range(ROWS):
            for col in range(row % 2, COLS, 2):
                if 7 > col > 1 and 1 < row < 7:
                    pygame.draw.rect(
                        win, GRAY, (row * SQUARE_SIZE, col * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))

    # Draw rest
    def draw(self, win):
        self.draw_grid(win)
        for row in range(LEVEL_LENGTH):
            for col in range(LEVEL_LENGTH):
                image = self.grid[row][col]
                if image != 0:
                    image.draw(win)

    # Create the level from given list
    def create_level(self, level):
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

    # Check for placable marker
    def grid_check(self, row, col):
        if row < 7:
            if col < 7:
                if self.grid[row][col] == 0:
                    return True
        return False

    # Place new marker
    def new_marker(self, row, col, color):
        if 1 < row < 7:
            if 1 < col < 7:
                if color == DARKGRAY:
                    value = -1
                    self.answer[row - 2][col - 2] = value
                    # print(self.answer)
                else:
                    value = -2
                    self.answer[row - 2][col - 2] = value
                    # print(self.answer)
                self.grid[row][col] = Marker(row, col, color)

    # Remove marker
    def remove_marker(self, row, col):
        if 1 < row < 7:
            if 1 < col < 7:
                self.grid[row][col] = 0
                self.answer[row - 2][col - 2] = 0

    def check_for_complition(self):
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
        if self.completed:
            button_completed = pygame.Rect(
                WIDTH / 2 - 100, HEIGHT / 10 * 8, 200, 50)
            pygame.draw.rect(win, PURPLE, button_completed)
            draw_text("Läpäisty", font, WHITE, win,
                      WIDTH / 2, HEIGHT / 10 * 8 + 25)
