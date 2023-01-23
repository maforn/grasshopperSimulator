import pygame

from grid import Grid
from settings import Settings
from simulation import Simulation
from time import sleep
from util import check_user_exit

def main():
    grid = Grid(Settings.WINDOW_WIDTH // 2, Settings.WINDOW_HEIGHT // 2)
    simulation = Simulation(Settings.WINDOW_WIDTH * Settings.BLOCKSIZE,
                            Settings.WINDOW_HEIGHT * Settings.BLOCKSIZE,
                            grid)
    while True:
        simulation.tick()
        check_user_exit()
        sleep(Settings.SECONDS_BETWEEN_UPDATES)

if __name__ == "__main__":
    main()