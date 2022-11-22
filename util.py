"""
Utility functions
"""
import sys
from random import gauss

import pygame

def check_user_exit():
    """
    Quits pygame if the user closes the window
    """
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

def gauss_to_color(mu, sigma):
    return min(255, max(0, int(gauss(mu, sigma))))

