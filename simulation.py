import itertools

import pygame

import color
from settings import Settings


class Simulation:
    """
    Simulation object exposing methods to control the simulation.
    The drawing on a pygame screen is done internally.
    """
    def __init__(self, window_width, window_height, grid):
        self.grid = grid
        # Pygame setup
        pygame.init()
        self.clock = pygame.time.Clock()
        self.pygame_screen = pygame.display.set_mode((window_width,
                                                      window_height))
        self.pygame_screen.fill(color.BLACK)
        self._draw_grid()
        pygame.display.update()
    
    def _draw_grid(self):
        bs = Settings.BLOCKSIZE
        for tile in self.grid: 
            rect = pygame.Rect(tile.x_coordinate_in_grid * bs,
                               tile.y_coordinate_in_grid * bs, bs, bs)
            # Fill
            pygame.draw.rect(self.pygame_screen, (0, 0, tile.humidity),
                             rect, 0)
            # Border
            pygame.draw.rect(self.pygame_screen, color.BLACK,
                             rect, 1)
    
    def tick(self):
        """
        Moves the simulation one step forward.
        """
        self.grid.update()
        self._draw_grid()
        pygame.display.update()