import pygame
import random

CELL_WIDTH = 32
CELL_HEIGHT = 32
GRID_COLS = 20
GRID_ROWS = 16


def main():
    try:
        pygame.init()
        mole_image = pygame.image.load("mole.png")
        screen = pygame.display.set_mode((640, 512))
        clock = pygame.time.Clock()

        mole_x, mole_y = 0, 0  #top left

        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_x, mouse_y = event.pos
                    mole_rect = pygame.Rect(mole_x, mole_y, CELL_WIDTH, CELL_HEIGHT)
                    if mole_rect.collidepoint(mouse_x, mouse_y):
                        mole_x = random.randrange(0, GRID_COLS) * CELL_WIDTH
                        mole_y = random.randrange(0, GRID_ROWS) * CELL_HEIGHT

            screen.fill((50, 113, 168))
            for col in range(1, GRID_COLS):
                pygame.draw.line(screen, "red", (col * CELL_WIDTH, 0), (col * CELL_WIDTH, 512))
            for row in range(1, GRID_ROWS):
                pygame.draw.line(screen, "red", (0, row * CELL_HEIGHT), (640, row * CELL_HEIGHT))

            screen.blit(mole_image, mole_image.get_rect(topleft=(mole_x, mole_y)))
            pygame.display.flip()
            clock.tick(60)
    finally:
        pygame.quit()


if __name__ == "__main__":
    main()
