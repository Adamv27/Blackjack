import random


class Card:
    def __init__(self, value, suit):
        self.value = value
        self.suit = suit

    def get_name(self):
        values = {11:'j', 12: 'q', 13: 'k', 14: 'a'}
        if self.value > 10:
            return f'{self.suit.lower()}{values[self.value]}'
        return f'{self.suit.lower()}{self.value}'
        

class Deck:
    def __init__(self):
        self.suits = ['H', 'D', 'S', 'C']
        self.deck = [Card(value, suit) for value in range(2, 15) for suit in self.suits]

    def shuffle(self):
        random.shuffle(self.deck)
    
    def select_card(self):
        return self.deck.pop(0)

    def print(self):
        for card in self.deck:
            print(card.get_name())
    
    @staticmethod
    def calculate_hand_value(hand):
        total_value = sum([Deck.get_card_value(card) for card in hand])

        if total_value <= 11 and any(card.value == 14 for card in hand):
            total_value += 10
        return total_value

    @staticmethod
    def calculate_dealer_hand(hand):
        """
        If the dealers hand total is over 17 they must stand. If their
        hand total is 16 or under they must take a card. If the dealer has an 
        ace, and counting it as 11 would bring the total to 17 or more (but not over 21), 
        the dealer must count the ace as 11 and stand.
        """
        total_value = 0

        for card in hand:
            if card.value in [11, 12, 13]:
                total_value += 10
            elif card.value == 14:
                if total_value + 11 >= 17 and total_value + 11 < 21:
                    total_value += 11
                else:
                    total_value += 1
            else:
                total_value += card.value
        return total_value

    @staticmethod
    def get_card_value(card):
        # Face cards
        if card.value in [11, 12, 13]:
            return 10
        # Ace
        elif card.value == 14:
            return 1
        else:
            return card.value    