from .deck import Deck

class Dealer:
    hand = []
    hand_value = 0

    def get_hand_value():
        Dealer.hand_value = Deck.calculate_dealer_hand(Dealer.hand)
        return Dealer.hand_value

    def reset():
        Dealer.hand = []
        Dealer.hand_value = 0   


