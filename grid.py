from random import randint
from settings import SimulationParameters
from util import gauss_to_color

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
        h = self.humidity
        h_change = SimulationParameters.HUMIDITY_CHANGE
        if h < h_change:
            self.humidity += h_change
        elif h > 255 - h_change:
            self.humidity -= h_change
        else:
            self.humidity += randint(-h_change, h_change)
