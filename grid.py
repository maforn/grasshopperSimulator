import pygame, sys
from random import gauss, randint
from time import sleep

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLOOD_RED = (202, 11, 0)
RYB_RED = (243, 32, 19)
GREEN = (34, 187, 51)
YELLOW = (240, 213, 0)
BLUE = (91, 192, 222)
GRAY = (170, 170, 170)

WINDOW_HEIGHT = 400
WINDOW_WIDTH = 400

BLOCKSIZE = 40  # Set the size of the grid block

HUMIDITY_CHANGE = 10


def gauss_to_color(mu, sigma):
    return min(255, max(0, int(gauss(mu, sigma))))


class Tile:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.grasshoppers = 0
        self.pheromone = 0
        self.temperature = gauss_to_color(128, 64)
        self.resources = gauss_to_color(128, 64)
        self.humidity = gauss_to_color(128, 64)  # gaussian curve with mean 128 and standard deviation 64

    def changeHumidity(self):
        if self.humidity < HUMIDITY_CHANGE:
            self.humidity += HUMIDITY_CHANGE
        elif self.humidity > 255 - HUMIDITY_CHANGE:
            self.humidity -= HUMIDITY_CHANGE
        else:
            self.humidity += randint(-HUMIDITY_CHANGE, HUMIDITY_CHANGE)


grid = list()

for x in range(0, WINDOW_WIDTH, BLOCKSIZE):
    tiles = list()
    for y in range(0, WINDOW_HEIGHT, BLOCKSIZE):
        tiles.append(Tile(x, y))
    grid.append(tiles)


def main():
    global SCREEN, CLOCK
    pygame.init()
    SCREEN = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    CLOCK = pygame.time.Clock()
    SCREEN.fill(BLACK)

    while True:
        changeConditions()
        drawGrid()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        pygame.display.update()
        sleep(1)


def changeConditions():
    for tiles in grid:
        for tile in tiles:
            tile.changeHumidity();


def drawGrid():
    for tiles in grid:
        for tile in tiles:
            rect = pygame.Rect(tile.x, tile.y, BLOCKSIZE, BLOCKSIZE)
            pygame.draw.rect(SCREEN, (0, 0, tile.humidity), rect, 0)  # fill
            pygame.draw.rect(SCREEN, BLACK, rect, 1)  # border


if __name__ == "__main__":
    main()
