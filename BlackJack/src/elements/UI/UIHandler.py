import pygame
import time
from ...setup import *
from .Buttons import *
from ..player import Player
from ..dealer import Dealer
from ..deck import Deck


class UIHandler:
    all_buttons = [DealButton(), HitButton(), StandButton()]

    player_standing = False

    def reload_screen():
        UIHandler.draw_background()
        UIHandler.draw_buttons()
        if len(Player.hand) >= 2:
            UIHandler.draw_cards()
            UIHandler.draw_hand_values()

    def reset():
        UIHandler.player_standing = False
        
        for index, button in enumerate(UIHandler.all_buttons):
            if index == 0:
                button.is_visible = True
            else:
                button.is_visible = False

    def draw_background():
        SCREEN.blit(IMAGES['background'], (0,0))
            
    def deal_was_clicked(pos):
        # Deal Button
        button = UIHandler.all_buttons[0]
        was_clicked = button.was_clicked(pos) and button.is_visible
        if was_clicked:
            button.is_visible = False
            #Show hit and stand buttons
            UIHandler.all_buttons[1].is_visible = True
            UIHandler.all_buttons[2].is_visible = True
            
        return was_clicked

    def hit_was_clicked(pos):
        button = UIHandler.all_buttons[1]
        return button.was_clicked(pos) and not UIHandler.player_standing

    def stand_was_clicked(pos):
        button = UIHandler.all_buttons[2]
        return button.was_clicked(pos)

    def draw_deal_button():
        UIHandler.all_buttons[0].draw()
    
    def draw_buttons():
        for button in UIHandler.all_buttons:
            if button.is_visible:
                button.draw()
    
    def draw_hand_values():
        font = pygame.font.SysFont('Arial', 30)
        hand_value = Player.hand_value
        textsurface = font.render(f'Player: {hand_value}', True, COLORS['white'])
        x = (WIDTH / 2) - textsurface.get_width() / 2
        y = 540
        SCREEN.blit(textsurface, (x, y))
        
        # Dont show full value of dealers hand
        if not UIHandler.player_standing:
            hand_value = Deck.get_card_value(Dealer.hand[1])
        else:
            hand_value = Deck.calculate_dealer_hand(Dealer.hand)
        textsurface = font.render(f'Dealer: {hand_value}', True, COLORS['white'])
        x = (WIDTH / 2) - textsurface.get_width() / 2
        y = 50
        SCREEN.blit(textsurface, (x, y))


    def draw_cards():
        offset = 30
        # The amount of space the cards and the offset take up on the screen
        card_space = len(Player.hand) * CARD_WIDTH +  (offset * len(Player.hand) - 1)
        # Creates an even amount of pixels on each side to center the cards
        starting_x = (WIDTH - card_space) / 2
        for index, card in enumerate(Player.hand):
            image = IMAGES[card.get_name()]
            SCREEN.blit(image, (starting_x + offset * index, 350))
            starting_x += CARD_WIDTH

        card_space = len(Dealer.hand) * CARD_WIDTH +  (offset * len(Dealer.hand) - 1)
        starting_x = (WIDTH - card_space) / 2

        for index, card in enumerate(Dealer.hand):
            if index == 0 and not UIHandler.player_standing:
                # Dealer only shows one card
                image = IMAGES['back']
            else:
                image = IMAGES[card.get_name()]
            SCREEN.blit(image, (starting_x + offset * index, 100))
            starting_x += CARD_WIDTH
    
    def game_over(text):
        UIHandler.display_text(text)

    def display_text(text):
        image = IMAGES['background']
        SCREEN.blit(image, (0,0))

        font = pygame.font.SysFont('Arial', 60)
        textsurface = font.render(text, True, COLORS['white'])

        text_rect = textsurface.get_rect(center=(WIDTH/2, HEIGHT/2))
        SCREEN.blit(textsurface, text_rect)
        pygame.display.update()
        time.sleep(1.5)