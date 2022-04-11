import sys
from levels import *


FPS = 60
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Nonograms by Nooa')
pygame.init()


def get_row_col_from_mouse(pos):
    x, y = pos
    row = y // SQUARE_SIZE
    col = x // SQUARE_SIZE
    return row, col


def main_menu():
    click = False
    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        WIN.fill(LIGHTBLUE)
        draw_text("Nonograms", font, BLACK, WIN, WIDTH / 2, HEIGHT / 4)

        mouse_x, mouse_y = pygame.mouse.get_pos()

        # Define play button
        button_play = pygame.Rect(WIDTH / 2 - 75, HEIGHT / 5 * 2, 150, 50)
        # Define levels button
        button_levels = pygame.Rect(WIDTH / 2 - 75, HEIGHT / 5 * 3, 150, 50)
        # Define quit button
        button_quit = pygame.Rect(WIDTH / 2 - 75, HEIGHT / 5 * 4, 150, 50)

        # Draw play button
        pygame.draw.rect(WIN, (180, 150, 255), button_play)
        draw_text("Play", font, BLACK, WIN, WIDTH / 2, HEIGHT / 5 * 2 + 25)
        # Play buttons action
        if button_play.collidepoint((mouse_x, mouse_y)):
            if click:
                play()

        # Draw levels button
        pygame.draw.rect(WIN, (180, 150, 255), button_levels)
        draw_text("Levels", font, BLACK, WIN, WIDTH / 2, HEIGHT / 5 * 3 + 25)
        # Levels buttons action
        if button_levels.collidepoint((mouse_x, mouse_y)):
            if click:
                levels()

        # Draw quit button
        pygame.draw.rect(WIN, (180, 150, 255), button_quit)
        draw_text("Quit", font, BLACK, WIN, WIDTH / 2, HEIGHT / 5 * 4 + 25)
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


def levels():
    run = True
    click = False
    clock = pygame.time.Clock()
    while run:
        clock.tick(FPS)
        WIN.fill(LIGHTBLUE)

        draw_text("Levels", font, BLACK, WIN, WIDTH / 2, HEIGHT / 8)
        mouse_x, mouse_y = pygame.mouse.get_pos()

        # Define back button
        button_back = pygame.Rect(WIDTH / 2 - 75, HEIGHT / 6 * 5, 150, 50)
        # Draw back button
        pygame.draw.rect(WIN, (180, 150, 255), button_back)
        draw_text("Back", font, BLACK, WIN, WIDTH / 2, HEIGHT / 6 * 5 + 25)
        # Back buttons action
        if button_back.collidepoint((mouse_x, mouse_y)):
            if click:
                run = False
                main_menu()

        click = False
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True
        pygame.display.update()


def play():
    run = True
    clock = pygame.time.Clock()
    grid = Grid()
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

        grid.draw(WIN)

        mouse_x, mouse_y = pygame.mouse.get_pos()
        # Define back button
        button_back = pygame.Rect(WIDTH / 2 - 75, HEIGHT / 6 * 5 + 40, 150, 50)

        # Draw back button
        pygame.draw.rect(WIN, (180, 150, 255), button_back)
        draw_text("Back", font, BLACK, WIN, WIDTH /
                  2, HEIGHT / 6 * 5 + 25 + 40)

        # Back buttons action
        if button_back.collidepoint(mouse_x, mouse_y):
            if click:
                run = False
                levels()

        grid.is_completed(WIN)

        pygame.display.update()

    pygame.quit()


main_menu()
