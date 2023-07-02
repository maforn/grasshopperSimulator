class Settings:
    """
    Graphical settings impacting the aspect of the Pygame window
    """
    WINDOW_HEIGHT = 20
    WINDOW_WIDTH = 20
    BLOCKSIZE = 40

    SECONDS_BETWEEN_UPDATES = 1

    SAVE_IMAGES = True
    SAVE_DATA = True

class SimulationParameters:
    """
    Settings potentially impacting on the simulation's results
    """
    HUMIDITY_CHANGE = 10
    TEMPERATURE_CHANGE = 5