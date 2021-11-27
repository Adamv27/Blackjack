import queue
import pygame
from ..setup import *
from .player import Player

class Bet:
    def __init__(self):
        self.x = 250
        self.y = 350
        self.width = 100
        self.area = pygame.Rect(self.x, self.y, self.width, self.width)
        
        #Betting area represented with a stack
        # Last chip in is the first chip out
        self.stack = []
        self.total_value = 0

    def add_chip(self, chip):
        value = chip.value
        if Player.balance - value >= 0:
            self.stack.append(chip)
            self.total_value += chip.value
            Player.balance -= chip.value
    
    def get_last_chip(self):
        if self.stack:
            chip = self.stack.pop(-1)
            self.total_value -= chip.value
            Player.balance += chip.value
            return chip
        return None
    
    def was_clicked(self, pos):
        return self.area.collidepoint(pos)

    def chip_was_placed(self, chip) -> bool:
        return self.area.colliderect(chip.rect)

    def display_text(self) -> None:
        font = pygame.font.SysFont('Arial', 30)
        textsurface = font.render(f'Bet: {self.total_value}', True, COLORS['white'])
        SCREEN.blit(textsurface, (400, 400))

        text_surface = font.render(f'Money: {Player.balance}', True, COLORS['white'])
        SCREEN.blit(text_surface, (400, 450))

    def update(self):
        self.display_text()
        for chip in self.stack:
            chip.update()
        pygame.draw.rect(SCREEN, COLORS['black'], self.area, 4)
