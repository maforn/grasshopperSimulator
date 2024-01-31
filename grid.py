from random import randint, seed, random

import pygame.image

from settings import SimulationParameters
from util import gauss_to_color
from math import ceil


class Tile:
    def __init__(self, x_coordinate_in_grid, y_coordinate_in_grid):
        self.x_coordinate_in_grid = x_coordinate_in_grid
        self.y_coordinate_in_grid = y_coordinate_in_grid

        self.pheromone = 0.0
        self.grasshoppers_p = abs(randint(
            SimulationParameters.MIN_GRASSHOPPERS_PER_CELL, SimulationParameters.MAX_GRASSHOPPERS_PER_CELL))
        self.grasshoppers_NOT_p = abs(randint(
            SimulationParameters.MIN_GRASSHOPPERS_PER_CELL, SimulationParameters.MAX_GRASSHOPPERS_PER_CELL))

        self.temperature = gauss_to_color(192, 64)
        self.resources = gauss_to_color(192, 64)
        self.humidity = gauss_to_color(192, 64)

    def _update_pheromone(self):
        if self.grasshoppers_p > 0 and self.temperature > 128 and self.resources > 128 and self.humidity > 128:
            if self.pheromone < 1.0:
                self.pheromone += 0.1
        else:
            if self.pheromone > 0.1:
                self.pheromone -= 0.1
            elif self.pheromone <= 0.1:
                self.pheromone = 0

    def _update_temperature(self):
        t = self.temperature
        t_change = SimulationParameters.TEMPERATURE_CHANGE
        if t < t_change:
            self.temperature += t_change
        elif t > 255 - t_change:
            self.temperature -= t_change
        else:
            self.temperature += randint(-t_change, t_change)

    def _update_resources(self):
        self.resources = max(
            0, self.resources - ceil((self.grasshoppers_p + self.grasshoppers_NOT_p) / 5))
        if random() > 2/3:
            self.resources = min(255, self.resources + 1)

    def _update_humidity(self):
        h = self.humidity
        h_change = SimulationParameters.HUMIDITY_CHANGE
        if h < h_change:
            self.humidity += h_change
        elif h > 255 - h_change:
            self.humidity -= h_change
        else:
            self.humidity += randint(-h_change, h_change)

    def update(self):
        self._update_temperature()
        self._update_resources()
        self._update_humidity()
        self._update_pheromone()


class Grid:
    def __init__(self, x_number_of_tiles, y_number_of_tiles):
        """
        Initialises a Grid object with random values for humidity and 
        other parameters in each tile.
        x and y are the number of tiles in the grid in width and height.
        The class is designed to be independent of the graphical
        details (screen size etc.) and only represents the grid as an
        abstract entity.
        """
        self.x_number_of_tiles = x_number_of_tiles
        self.y_number_of_tiles = y_number_of_tiles
        self.table = []
        for x in range(x_number_of_tiles):
            column = []
            for y in range(y_number_of_tiles):
                column.append(Tile(x, y))
            self.table.append(column)

        # set the seed for random so that the result can always be compared
        seed(0)

    def __getitem__(self, key):
        """
        key is a (x, y) tuple with the indices of the tile you want to get.
        """
        return self.table[key[0]][key[1]]

    def __iter__(self):
        self.current_x_index = 0
        self.current_y_index = 0
        return self

    def __next__(self):
        if self.current_x_index < self.x_number_of_tiles and \
                self.current_y_index != self.y_number_of_tiles:
            tile = self[self.current_x_index, self.current_y_index]
            self.current_x_index += 1
        elif self.current_y_index < self.y_number_of_tiles:
            # If the current x index exceeded the maximum index, then
            # its real current value is zero
            self.current_x_index = 0
            tile = self[self.current_x_index, self.current_y_index]
            self.current_y_index += 1
        else:
            raise StopIteration
        return tile

    def _move_grasshoppers(self):
        """
        This method is called after the grid is updated to change the
        position of grasshoppers in the grid based on humidity, 
        pheromones etc.
        """
        for x in range(self.x_number_of_tiles):
            for y in range(self.y_number_of_tiles):
                tile = self.__getitem__((x, y))
                if (tile.grasshoppers_p > 0 or tile.grasshoppers_NOT_p > 0) and not (
                        tile.temperature > 128 and tile.resources > 128 and tile.humidity > 128):
                    # calc the boundaries of the "square" in which the grasshoppers can move
                    x_min_right = 1
                    x_min_left = -1
                    y_min_top = -1
                    y_min_bot = 1
                    if tile.x_coordinate_in_grid == 0:
                        x_min_left = 0
                    if tile.x_coordinate_in_grid == self.x_number_of_tiles - 1:
                        x_min_right = 0
                    if tile.y_coordinate_in_grid == 0:
                        y_min_top = 0
                    if tile.y_coordinate_in_grid == self.y_number_of_tiles - 1:
                        y_min_bot = 0

                    preferred = (-1, -1)
                    max_ph = 0.0
                    for x in range(x_min_left, x_min_right + 1):
                        for y in range(y_min_top, y_min_bot + 1):
                            tile_xy = (tile.x_coordinate_in_grid + x,
                                       tile.y_coordinate_in_grid + y)
                            # avoid auto selecting with the and
                            if self.__getitem__(tile_xy).pheromone > max_ph and tile_xy != (
                                    tile.x_coordinate_in_grid, tile.y_coordinate_in_grid):
                                max_ph = self.__getitem__(tile_xy).pheromone
                                preferred = tile_xy

                    if randint(64, 193) >= (
                            (tile.temperature + tile.resources + tile.humidity) // 3 + 5 * (tile.grasshoppers_p + tile.grasshoppers_NOT_p)) and tile.grasshoppers_p > 0:
                        tile.grasshoppers_p -= 1
                    if randint(64, 193) >= (
                            (tile.temperature + tile.resources + tile.humidity) // 3 + 5 * (tile.grasshoppers_p + tile.grasshoppers_NOT_p)) and tile.grasshoppers_NOT_p > 0:
                        tile.grasshoppers_NOT_p -= 1

                    if tile.grasshoppers_p > 0 and tile.pheromone < 1.0:
                        if max_ph == 0.0:
                            for e in range(tile.grasshoppers_p):
                                p_preferred = (tile.x_coordinate_in_grid + randint(x_min_left, x_min_right),
                                               tile.y_coordinate_in_grid + randint(y_min_top, y_min_bot))
                                tile.grasshoppers_p -= 1
                                self.__getitem__(
                                    p_preferred).grasshoppers_p += 1
                        elif preferred != (-1, -1):  # and max_ph / 3 * 2 > random()
                            self.__getitem__(
                                preferred).grasshoppers_p += tile.grasshoppers_p
                            tile.grasshoppers_p = 0

                    if tile.grasshoppers_NOT_p > 0:
                        for e in range(tile.grasshoppers_NOT_p):
                            preferred = (tile.x_coordinate_in_grid + randint(x_min_left, x_min_right),
                                         tile.y_coordinate_in_grid + randint(y_min_top, y_min_bot))
                            self.__getitem__(preferred).grasshoppers_NOT_p += 1
                            tile.grasshoppers_NOT_p -= 1

    def update(self):
        """
        Updates the status of all the tiles in the grid
        """
        tot_grasshoppers_p = 0
        tot_grasshoppers_NOT_p = 0
        for x in range(self.x_number_of_tiles):
            for y in range(self.y_number_of_tiles):
                tile = self.__getitem__((x, y))
                tile.update()
                tot_grasshoppers_p += tile.grasshoppers_p
                tot_grasshoppers_NOT_p += tile.grasshoppers_NOT_p
        self._move_grasshoppers()
        return f'{tot_grasshoppers_p};{tot_grasshoppers_NOT_p}'
