import pygame

from grid import Grid
from settings import Settings
from simulation import Simulation
from time import sleep
from util import check_user_exit
import os


def main():
    grid = Grid(Settings.WINDOW_WIDTH // 2, Settings.WINDOW_HEIGHT // 2)
    simulation = Simulation(Settings.WINDOW_WIDTH * Settings.BLOCKSIZE,
                            Settings.WINDOW_HEIGHT * Settings.BLOCKSIZE,
                            grid)
    with open("data.csv", "w") as f:
        i = 0
        grasshoppers = "1;1"
        if not os.path.exists("images") and Settings.SAVE_IMAGES:
            os.mkdir("images")
        try:
            while grasshoppers != "0;0":
                if Settings.SAVE_IMAGES:
                    simulation.save_image(i)
                    i += 1
                grasshoppers = simulation.tick()
                if Settings.SAVE_DATA:
                    f.write(f'{grasshoppers}\n')
                check_user_exit()
                sleep(Settings.SECONDS_BETWEEN_UPDATES)
        except:
            pass
    f.close()


if __name__ == "__main__":
    main()
