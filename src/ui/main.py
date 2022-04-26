import sys
from services.levels import *
from entities.level_list import *


def get_row_col_from_mouse(pos):
    x, y = pos
    row = y // SQUARE_SIZE
    col = x // SQUARE_SIZE
    return row, col


class MainMenu:
    def __init__(self):
        self.WIN = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption('Nonograms by Nooa')
        pygame.init()

        self.level = level0
        self.level_answer = level0_answer

    def main_menu(self):
        click = False
        clock = pygame.time.Clock()
        run = True
        while run:
            clock.tick(FPS)
            self.WIN.fill(LIGHTBLUE)
            draw_text("Nonograms", font, BLACK,
                      self.WIN, WIDTH / 2, HEIGHT / 4)

            mouse_x, mouse_y = pygame.mouse.get_pos()

            # Define play button
            button_play = pygame.Rect(WIDTH / 2 - 75, HEIGHT / 5 * 2, 150, 50)
            # Define levels button
            button_levels = pygame.Rect(
                WIDTH / 2 - 75, HEIGHT / 5 * 3, 150, 50)
            # Define quit button
            button_quit = pygame.Rect(WIDTH / 2 - 75, HEIGHT / 5 * 4, 150, 50)

            # Draw play button
            pygame.draw.rect(self.WIN, (180, 150, 255), button_play)
            draw_text("Play", font, BLACK, self.WIN,
                      WIDTH / 2, HEIGHT / 5 * 2 + 25)
            # Play buttons action
            if button_play.collidepoint((mouse_x, mouse_y)):
                if click:
                    self.play(self.level, self.level_answer)

            # Draw levels button
            pygame.draw.rect(self.WIN, (180, 150, 255), button_levels)
            draw_text("Levels", font, BLACK, self.WIN,
                      WIDTH / 2, HEIGHT / 5 * 3 + 25)
            # Levels buttons action
            if button_levels.collidepoint((mouse_x, mouse_y)):
                if click:
                    self.levels()

            # Draw quit button
            pygame.draw.rect(self.WIN, (180, 150, 255), button_quit)
            draw_text("Quit", font, BLACK, self.WIN,
                      WIDTH / 2, HEIGHT / 5 * 4 + 25)
            # Quit buttons action
            if button_quit.collidepoint((mouse_x, mouse_y)):
                if click:
                    pygame.quit()
                    sys.exit()

            click = False
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        click = True
            pygame.display.update()

    def levels(self):
        run = True
        click = False
        clock = pygame.time.Clock()
        while run:
            clock.tick(FPS)
            self.WIN.fill(LIGHTBLUE)

            draw_text("Levels", font, BLACK, self.WIN, WIDTH / 2, HEIGHT / 8)
            mouse_x, mouse_y = pygame.mouse.get_pos()

            # Define buttons
            button_back = pygame.Rect(WIDTH / 2 - 75, HEIGHT / 6 * 5, 150, 50)
            draw_text("Back", font, BLACK, self.WIN,
                      WIDTH / 2, HEIGHT / 6 * 5 + 25)

            level1_button = pygame.Rect(
                WIDTH / 2 - 75, HEIGHT / 10 * 3, 150, 50)
            level2_button = pygame.Rect(
                WIDTH / 2 - 75, HEIGHT / 10 * 4, 150, 50)
            level3_button = pygame.Rect(
                WIDTH / 2 - 75, HEIGHT / 10 * 5, 150, 50)
            level4_button = pygame.Rect(
                WIDTH / 2 - 75, HEIGHT / 10 * 6, 150, 50)
            level5_button = pygame.Rect(
                WIDTH / 2 - 75, HEIGHT / 10 * 7, 150, 50)

            # Draw buttons
            pygame.draw.rect(self.WIN, (180, 150, 255), button_back)
            draw_text("Back", font, BLACK, self.WIN,
                      WIDTH / 2, HEIGHT / 6 * 5 + 25)

            pygame.draw.rect(self.WIN, (180, 150, 255), level1_button)
            draw_text("Level: 1", font, BLACK, self.WIN,
                      WIDTH / 2, HEIGHT / 10 * 3 + 25)

            pygame.draw.rect(self.WIN, (180, 150, 255), level2_button)
            draw_text("Level: 2", font, BLACK, self.WIN,
                      WIDTH / 2, HEIGHT / 10 * 4 + 25)

            pygame.draw.rect(self.WIN, (180, 150, 255), level3_button)
            draw_text("Level: 3", font, BLACK, self.WIN,
                      WIDTH / 2, HEIGHT / 10 * 5 + 25)

            pygame.draw.rect(self.WIN, (180, 150, 255), level4_button)
            draw_text("Level: 4", font, BLACK, self.WIN,
                      WIDTH / 2, HEIGHT / 10 * 6 + 25)

            pygame.draw.rect(self.WIN, (180, 150, 255), level5_button)
            draw_text("Level: 5", font, BLACK, self.WIN,
                      WIDTH / 2, HEIGHT / 10 * 7 + 25)

            # Button actions
            if button_back.collidepoint((mouse_x, mouse_y)):
                if click:
                    run = False
                    self.main_menu()
            if level1_button.collidepoint((mouse_x, mouse_y)):
                if click:
                    level = level0
                    level_answer = level0_answer
                    self.play(level, level_answer)
            elif level2_button.collidepoint((mouse_x, mouse_y)):
                if click:
                    level = level1
                    level_answer = level1_answer
                    self.play(level, level_answer)
            elif level3_button.collidepoint((mouse_x, mouse_y)):
                if click:
                    level = level2
                    level_answer = level2_answer
                    self.play(level, level_answer)
            elif level4_button.collidepoint((mouse_x, mouse_y)):
                if click:
                    level = level3
                    level_answer = level3_answer
                    self.play(level, level_answer)
            elif level5_button.collidepoint((mouse_x, mouse_y)):
                if click:
                    level = level4
                    level_answer = level4_answer
                    self.play(level, level_answer)

            click = False
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        click = True
            pygame.display.update()

    def play(self, level, level_answer):
        run = True
        clock = pygame.time.Clock()
        grid = Grid(level, level_answer)
        grid.completed = False
        while run:
            clock.tick(FPS)
            click = False
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    click = True
                # Check if level is completed
                if grid.completed is False:
                    # Leftclick
                    if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                        pos = pygame.mouse.get_pos()
                        row, col = get_row_col_from_mouse(pos)
                        print("Leftclick", row, col)
                        # Add black marker
                        if grid.grid_check(int(row), int(col)):
                            grid.new_marker(int(row), int(col), BLACK)
                            # Check for completion
                            grid.check_for_complition()
                        else:
                            # Remove marker
                            grid.remove_marker(int(row), int(col))

                        pygame.display.update()

                    # Rightclick
                    if event.type == pygame.MOUSEBUTTONDOWN and event.button == 3:
                        pos = pygame.mouse.get_pos()
                        row, col = get_row_col_from_mouse(pos)
                        print("Rightclick", row, col)
                        # Add gray marker
                        if grid.grid_check(int(row), int(col)):
                            grid.new_marker(int(row), int(col), DARKGRAY)
                            # Check for completion
                            grid.check_for_complition()
                        else:
                            # Remove marker
                            grid.remove_marker(int(row), int(col))
                    pygame.display.update()

            grid.draw(self.WIN)

            mouse_x, mouse_y = pygame.mouse.get_pos()
            # Define back button
            button_back = pygame.Rect(
                WIDTH / 2 - 75, HEIGHT / 6 * 5 + 40, 150, 50)

            # Draw back button
            pygame.draw.rect(self.WIN, (180, 150, 255), button_back)
            draw_text("Back", font, BLACK, self.WIN, WIDTH /
                      2, HEIGHT / 6 * 5 + 25 + 40)

            # Back buttons action
            if button_back.collidepoint(mouse_x, mouse_y):
                if click:
                    run = False
                    self.levels()

            grid.is_completed(self.WIN)

            pygame.display.update()

        pygame.quit()
