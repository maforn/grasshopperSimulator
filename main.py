import pygame
import sys

from color import Color
from grid import Tile
from settings import Settings
from time import sleep
from util import check_user_exit

class Grid:
    def __init__(self, width=10, height=10):
        self.grid = []
        self.pygame_screen = pygame.display.set_mode((Settings.WINDOW_WIDTH,
                                                      Settings.WINDOW_HEIGHT))

grid = []

for x in range(0, Settings.WINDOW_WIDTH, Settings.BLOCKSIZE):
    column = []
    for y in range(0, Settings.WINDOW_HEIGHT, Settings.BLOCKSIZE):
        column.append(Tile(x, y))
    grid.append(column)

def changeConditions():
    for tiles in grid:
        for tile in tiles:
            tile.changeHumidity();

def drawGrid():
    for tiles in grid:
        for tile in tiles:
            rect = pygame.Rect(tile.x, tile.y, Settings.BLOCKSIZE, Settings.BLOCKSIZE)
            pygame.draw.rect(SCREEN, (0, 0, tile.humidity), rect, 0)  # fill
            pygame.draw.rect(SCREEN, Color.BLACK, rect, 1)  # border

def main():
    global SCREEN, CLOCK
    pygame.init()
    SCREEN = pygame.display.set_mode((Settings.WINDOW_WIDTH, Settings.WINDOW_HEIGHT))
    CLOCK = pygame.time.Clock()
    SCREEN.fill(Color.BLACK)

    while True:
        changeConditions()
        drawGrid()
        check_user_exit()
        pygame.display.update()

        sleep(Settings.SECONDS_BETWEEN_UPDATES)

if __name__ == "__main__":
    main()