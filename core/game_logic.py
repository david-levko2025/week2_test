from lessens_exersice_in_the_army.tests.test2.core.deck import build_standard_deck
from lessens_exersice_in_the_army.tests.test2.core.player_io import ask_player_action

def calculate_hand_value(hand: list[dict]) -> int:
    build_standard_deck()
    value = 0
    aces = 0
    for card in hand:
        if card["rank"] == 'A':
            value += 11
            aces += 1
        elif card["rank"] in ['J', 'Q', 'K']:
            value += 10
        else:
            value += int(card["rank"])
    while value > 21 and aces > 0:
        value -= 10
        aces -= 1
    return value

def deal_two_each(deck: list[dict], player: dict, dealer: dict) -> None:
    player["hand"].append(deck[-2:])
    dealer["hand"].append(deck[-4:-2])
    p1 = player["hand"]
    p2 = dealer["hand"]
    f'your hand is {p1} and they equal to {calculate_hand_value(p1)}'
    f'your hand is {p2} and they equal to {calculate_hand_value(p2)}'
    return None


def dealer_play(deck: list[dict], dealer: dict) -> bool:
    dealer_hand = calculate_hand_value(dealer["hand"])
    while dealer_hand < 17:
        dealer["hand"].append(deck.pop())
        dealer_hand = calculate_hand_value(dealer["hand"])
        if dealer_hand > 21:
            print("the dealer lose")
        return False
    return True

def run_full_game(deck: list[dict], player: dict, dealer: dict) -> None:
    while True:
        print('your hand:')
        print(deal_two_each)
        print(ask_player_action())
        while ask_player_action() == 'H':
            player["hand"].append(deck.pop())
            if player["hand"] > 21:
                print(f'you busted! your hand was {player["hand"]}\n the hand of dealer was {dealer["hand"]}')
            elif ask_player_action() == 'S':
                dealer_play(dealer["hand"])
            else:
                calculate_hand_value(dealer["hand"])
                calculate_hand_value(player["hand"])
                if dealer["hand"] < player["hand"]:
                    print("you win , good job wanna play another round?")
                elif dealer["hand"] > player["hand"]:
                    print("you lose your money")
                else:
                    print("its a tie take your money back")


