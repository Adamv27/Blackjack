import os
import pygame
from . import tools


WIDTH = 612
HEIGHT = 612

pygame.init()
pygame.font.init()
pygame.display.set_caption("Black Jack")
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))

COLORS = {'white': (255, 255, 255), 'black': (0, 0, 0), 'gray': (100, 100, 100)}

# IMAGES
CHIP_WIDTH = 60
CHIP_HEIGHT = 60

CARD_WIDTH = 50
CARD_HEIGHT = int(CARD_WIDTH * 1.44)

IMAGES = tools.load_images(os.path.join("resources", "images"))
SOUNDS = tools.load_sounds(os.path.join("resources", "sounds"))