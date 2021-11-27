import pygame
from ..setup import *


class Chip:
    def __init__(self, x, y, value, image: pygame.Surface) -> None:
        self.value = value
        self.x = x
        self.y = y

        # Location where certain chip will always be
        self.HOME_X = x
        self.HOME_Y = y

        self.offset_x = 0
        self.offset_y = 0

        self.image = image
        self.size = 4
        self.rect = pygame.Rect(x, y, CHIP_WIDTH, CHIP_HEIGHT)

        self.being_dragged = False

    def move(self, pos: tuple) -> None:
        # Updates location while being dragged
        x,y = pos
        self.x = x - self.offset_x
        self.y = y - self.offset_x
        self.update()
        pygame.display.update()

    def reset_pos(self):
        self.x = self.HOME_X
        self.y = self.HOME_Y
        self.offset_x = 0
        self.offset_y = 0
        self.update()

    def update(self):
        self.rect = pygame.Rect(self.x, self.y, CHIP_WIDTH, CHIP_HEIGHT)
        SCREEN.blit(self.image, (self.x, self.y))

    def was_clicked(self, pos: tuple) -> bool:
        return self.rect.collidepoint(pos)