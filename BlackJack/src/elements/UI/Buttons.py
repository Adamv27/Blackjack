import pygame
from ...setup import *


class Button:
    def __init__(self, x, y, width, height) -> None:
        self.x = x
        self.y = y
        self.width = width
        self.height = height 
        self.is_visible = False
        self.area = pygame.Rect(self.x, self.y, self.width, self.height)

    def was_clicked(self, pos):
        return self.area.collidepoint(pos)
    

class HitButton(Button):
    def __init__(self) -> None:
        super().__init__(170, 475, 100, 50)
        self.text = 'HIT'

    def draw(self):
        font = pygame.font.SysFont('Arial', 30)
        text_surface = font.render(self.text, False, COLORS['white'])
        
        pygame.draw.rect(SCREEN, COLORS['gray'], self.area)

        x, y = self.area.center
        SCREEN.blit(text_surface, (x - 20, y - 20))
    
    def on_click(self):
        print("hit")


class DealButton(Button):
    def __init__(self) -> None:
        super().__init__(75, 350, 100, 50)
        self.text = 'DEAL'
        self.is_visible = True

    def draw(self):
        font = pygame.font.SysFont('Arial', 30)
        text_surface = font.render(self.text, False, COLORS['white'])

        pygame.draw.rect(SCREEN, COLORS['gray'], self.area)

        x, y = self.area.center
        SCREEN.blit(text_surface, (x - 30, y - 20))
    
    def on_click(self):
        print("clicked")


class StandButton(Button):
    def __init__(self) -> None:
        super().__init__(320, 475, 100, 50)
        self.text = 'STAND'

    def draw(self):
        font = pygame.font.SysFont('Arial', 30)
        text_surface = font.render(self.text, False, COLORS['white'])

        pygame.draw.rect(SCREEN, COLORS['gray'], self.area)

        x, y = self.area.center
        SCREEN.blit(text_surface, (x - 37, y - 20))
    
    def on_click(self):
        print("stand")