class Player:
    balance = 500
    hand = []
    hand_value = 0

    def bust():
        return Player.hand_value > 21

    def reset():
        Player.hand = []
        Player.hand_value = 0
          
def print_hand():
    for card in Player.hand:
        print(card.get_name())

