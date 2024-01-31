class Settings:
    """
    Graphical settings impacting the aspect of the Pygame window
    """
    WINDOW_HEIGHT = 20
    WINDOW_WIDTH = 20
    BLOCKSIZE = 40

    SECONDS_BETWEEN_UPDATES = 0.1

    SAVE_IMAGES = True
    SAVE_DATA = True


class SimulationParameters:
    """
    Settings potentially impacting on the simulation's results
    """

    # How much temperature and humidity parameters change at each iteration
    HUMIDITY_CHANGE = 10
    TEMPERATURE_CHANGE = 5

    # Minimum and maximum number of grasshoppers placed in each cell when the
    # cell is initialized
    MIN_GRASSHOPPERS_PER_CELL = 0
    MAX_GRASSHOPPERS_PER_CELL = 2
