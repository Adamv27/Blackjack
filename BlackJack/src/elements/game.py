import time
import math
import pygame
from ..setup import *
from .deck import Deck
from .player import Player, print_hand
from .dealer import Dealer
from.chipManager import ChipManager
from .UI.UIHandler import *


class Game:
    def __init__(self):
        Player.balance = 500

        self.deck = Deck()
        self.deck.shuffle()

        self.chips = ChipManager()
        self.betting = True
        self.bet = 0

    def update(self):
        UIHandler.reload_screen()
        if self.betting:
            self.chips.update()

    def deal_hands(self):
        for _ in range(2):
            card = self.deck.select_card()
            Player.hand.append(card)

            card = self.deck.select_card()
            Dealer.hand.append(card)

        Player.hand_value = Deck.calculate_hand_value(Player.hand) 
        if Player.hand_value == 21:
            self.blackjack()   


    def deal_player_card(self):
        card = self.deck.select_card()
        Player.hand.append(card)  
        Player.hand_value = Deck.calculate_hand_value(Player.hand)    
    
    def dealer_draw(self):
        time.sleep(1.5)
        while Dealer.get_hand_value() <= 16:
            card = self.deck.select_card()
            print(f'DRAWING CARD: {card.value}')
            Dealer.hand.append(card)
            UIHandler.reload_screen()
            pygame.display.update()
            time.sleep(1)


    def player_win(self):
        player_payout = self.bet * 2
        Player.balance += player_payout
        UIHandler.game_over("PLAYER WINS")

    def dealer_win(self):
        UIHandler.game_over("DEALER WINS")
        self.reset()
    
    def tie(self):
        Player.balance += self.bet
        UIHandler.game_over("TIE")
        self.reset()

    def blackjack(self):
        player_payout = self.bet * 1.5
        player_payout = int(math.ceil(player_payout))
        Player.balance += player_payout
        
        UIHandler.reload_screen()
        pygame.display.update()
        time.sleep(1.5)
        UIHandler.game_over("BLACKJACK")
        self.reset()


    def reset(self):
        self.betting = True
        self.deck = Deck()
        self.deck.shuffle()

        Player.reset()
        Dealer.reset()

        UIHandler.reset()
        self.chips.reset()

    def round_over(self):
        dealer = Dealer.hand_value
        player = Player.hand_value
        
        self.update()
        pygame.display.update()
        
        print(f'PLAYER: {player} DEALER: {dealer}')
        if (player > dealer and player <= 21) or dealer > 21:
            self.player_win()

        elif dealer > player and dealer <= 21:
            print("DEALER WIN")
            self.dealer_win()

        elif dealer == player and dealer <= 21 and player <= 21:
            self.tie()

        else:
            print('ERROR')
        self.reset()

    def loop(self):
        self.update()
    
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

            elif event.type == pygame.MOUSEBUTTONDOWN:
                if self.betting:
                    self.chips.handle_event(event.pos)

                    self.bet = self.chips.bet.total_value
                    # Player has to bet to play
                    if self.bet > 0:
                        if UIHandler.deal_was_clicked(event.pos):
                            self.betting = False
                            self.deal_hands()
                else:
                    if UIHandler.hit_was_clicked(event.pos):
                        self.deal_player_card()
                        if Player.bust():
                            UIHandler.reload_screen()
                            pygame.display.update()
                            time.sleep(1)
                            UIHandler.game_over("BUST")
                            self.reset()
                            

                    if UIHandler.stand_was_clicked(event.pos):
                        UIHandler.player_standing = True
                        self.update()
                        pygame.display.update()

                        self.dealer_draw()
                        time.sleep(1)
                        self.round_over()


            
                
                
                





