from random import randint
from settings import SimulationParameters
from util import gauss_to_color


class Tile:
    def __init__(self, x_coordinate_in_grid, y_coordinate_in_grid):
        self.x_coordinate_in_grid = x_coordinate_in_grid
        self.y_coordinate_in_grid = y_coordinate_in_grid

        self.grasshoppers = 0
        self.pheromone = 0
        self.temperature = gauss_to_color(128, 64)
        self.resources = gauss_to_color(128, 64)
        self.humidity = gauss_to_color(128, 64)  

    def _update_grasshoppers(self):
        pass

    def _update_pheromone(self):
        pass

    def _update_temperature(self):
        pass

    def _update_resources(self):
        pass

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
        self._update_grasshoppers()
        self._update_pheromone()
        self._update_temperature()
        self._update_resources()
        self._update_humidity()


class Grid:
    def __init__(self, x_number_of_tiles, y_number_of_tiles):
        """
        Initialises a Grid object with random values for humidity and other
        parameters in each tile.
        x and y are the number of tiles in the grid in width and height.
        """
        self.x_number_of_tiles = x_number_of_tiles
        self.y_number_of_tiles = y_number_of_tiles
        self.table = []
        for x in range(x_number_of_tiles):
            column = []
            for y in range(y_number_of_tiles):
                column.append(Tile(x, y))
            self.table.append(column) 
    
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

    def update(self):
        """
        Updates the status of all the tiles in the grid
        """
        for tile in self:
            tile.update()