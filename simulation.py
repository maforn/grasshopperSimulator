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
        font = pygame.font.SysFont(pygame.font.get_fonts()[0], bs)
        for tile in self.grid:
            # humidity rect
            rect_h = pygame.Rect(tile.x_coordinate_in_grid * bs,
                                 tile.y_coordinate_in_grid * bs, bs, bs)
            # temperature rect
            rect_t = pygame.Rect((tile.x_coordinate_in_grid + Settings.WINDOW_WIDTH // 2) * bs,
                                 tile.y_coordinate_in_grid * bs, bs, bs)
            # resources rect
            rect_r = pygame.Rect(tile.x_coordinate_in_grid * bs,
                                 (tile.y_coordinate_in_grid + Settings.WINDOW_HEIGHT // 2) * bs, bs, bs)
            # pheromones and grasshoppers rect
            rect_p = pygame.Rect((tile.x_coordinate_in_grid + Settings.WINDOW_WIDTH // 2) * bs,
                                 (tile.y_coordinate_in_grid + Settings.WINDOW_HEIGHT // 2) * bs, bs, bs)

            # Fill
            pygame.draw.rect(self.pygame_screen, (0, 0, tile.humidity),
                             rect_h, 0)
            pygame.draw.rect(self.pygame_screen, (tile.temperature, 0, 0),
                             rect_t, 0)
            pygame.draw.rect(self.pygame_screen, (0, int(tile.resources), 0),
                             rect_r, 0)
            i_pheromone = min(128, int(tile.pheromone * 128))
            pygame.draw.rect(self.pygame_screen,
                             (127 + i_pheromone, 127 + i_pheromone, 127 + i_pheromone),
                             rect_p, 0)
            # draw also the number of grasshoppers
            widget = font.render(str(tile.grasshoppers), True, pygame.Color("black"))
            font_rect = widget.get_rect()
            font_rect.center = rect_p.center
            self.pygame_screen.blit(widget, font_rect)

            # Border
            pygame.draw.rect(self.pygame_screen, color.BLACK,
                             rect_h, 1)
            pygame.draw.rect(self.pygame_screen, color.BLACK,
                             rect_t, 1)
            pygame.draw.rect(self.pygame_screen, color.BLACK,
                             rect_r, 1)
            pygame.draw.rect(self.pygame_screen, color.BLACK,
                             rect_p, 1)

    def tick(self):
        """
        Moves the simulation one step forward.
        """
        self.grid.update()
        self._draw_grid()
        pygame.display.update()
