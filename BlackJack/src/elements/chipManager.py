import math
from ..setup import *
from .bet import Bet
from .chip import Chip
from .player import Player
from .UI.UIHandler import UIHandler 


class ChipManager:
    def __init__(self):
        self.chips = []
        self.chip_images = {}
        self.values = [[1, 5, 10, 25, 50],
                      [100, 250, 500, 1000, 5000]]

        self.bet = Bet()
        
        # Array containing Rects that will create a new
        # Chip object When clicked
        self.chip_surfaces = []
        self.load_surfaces()

    def update(self) -> None:
        UIHandler.draw_background()
        UIHandler.draw_deal_button()
        # Redraws all chips
        self.draw_chips()   
        for chip in self.chips:
            chip.update()
        self.bet.update()
    
    def reset(self):
        self.bet.stack = []
        self.bet.total_value = 0
        self.update()


    def handle_event(self, pos) -> None:
        # Any chips in the bet area are objects that have already been created
        # that are contained in a stack
        if self.bet.was_clicked(pos):
            chip = self.bet.get_last_chip()
            if chip:
                x,y = pygame.mouse.get_pos()
                chip.offset_x = x - chip.x
                chip.offset_y = y - chip.y
                self.move_chip(chip)
        # If the bet area wasn't clicked and one of the
        # surfaces was clicked, a new chip object must be made
        else:
            for surface in self.chip_surfaces:
                if surface.collidepoint(pos):
                    chip = self.create_chip(pos)
                    chip.offset_x = pos[0] - chip.x
                    chip.offset_y = pos[0] - chip.y
                    self.move_chip(chip)

    def move_chip(self, chip):
        chip.being_dragged = True
        while chip.being_dragged:
            self.update()
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONUP:
                    chip.being_dragged = False
                    if self.bet.chip_was_placed(chip):
                        self.bet.add_chip(chip)
                        chip.offset_x = 0
                        chip.offset_y = 0
                        x, y = self.bet.area.center
                        x -= CHIP_WIDTH // 2
                        y -= CHIP_HEIGHT // 2
                        chip.move((x,y))
                    else:                
                        chip.reset_pos()
                if event.type == pygame.MOUSEMOTION:
                    chip.move(event.pos)

    def create_chip(self, pos: tuple) -> Chip:
        # This method takes a coordinate of a click (x, y) 
        # and calculates which chip was clicked on below
        # then creates a new object of that chip
        x,y = pos
        column = math.floor((x - 29) / CHIP_WIDTH)
        if column > 4:
            column = 4
        row = abs(math.floor((475 - y) / CHIP_HEIGHT)) - 1
        
        starting_x = 20
        starting_y = 475
        chip_x = starting_x + (column * (CHIP_WIDTH + 5))
        chip_y = starting_y + (row * (CHIP_WIDTH + 5))
         
        value = self.values[row][column]
        image = self.chip_images[value]
        chip = Chip(chip_x, chip_y, value, image)
        return chip

    def was_clicked(self, chip, pos):
        if chip.was_clicked(pos):
            return True

    def draw_chips(self) -> None:
        # Draws the permanent chips to the screen
        # These are only the images not the actual object
        starting_x = 20
        starting_y = 475
        offset = CHIP_WIDTH
        index = 0
        for i in range(5):
            for j in range(2):
                x = starting_x + (i * (offset + 5))
                y = starting_y + (j * (offset + 5))
                value = self.values[j][i]
                image = self.chip_images[self.values[j][i]]
                SCREEN.blit(image, (x, y))
                index += 1

    def load_surfaces(self) -> None:
        # Loads the surfaces that allow the class to know
        # when one of the chips has been clicked on.
        # Also loads all the chip images into a dict 
        # with the structure {value: image name}
        starting_x = 20
        starting_y = 475
        offset = CHIP_WIDTH

        index = 0
        for i in range(5):
            for j in range(2):
                x = starting_x + (i * (offset + 5))
                y = starting_y + (j * (offset + 10))
                image_name = 'chip_' + str(self.values[j][i])
                image = IMAGES[image_name]
                value = self.values[j][i]
                self.chip_images[value] = image

                surface = pygame.Rect(x, y, CHIP_WIDTH, CHIP_HEIGHT)
                self.chip_surfaces.append(surface)
                index += 1
    