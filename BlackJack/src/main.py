import os
import pygame
from . import setup
from .elements.game import Game

def main():
    game = Game()
    while True:
        game.loop()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return 
        pygame.display.update()