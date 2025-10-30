from lessens_exersice_in_the_army.tests.test2.core.deck import build_standard_deck
from lessens_exersice_in_the_army.tests.test2.core.deck import shuffle_by_suit
from lessens_exersice_in_the_army.tests.test2.core.game_logic import run_full_game
if __name__ == '__main__':
    deck = build_standard_deck()
    shuffle = shuffle_by_suit(deck)
    player = {"hand":[]}
    dealer = {"hand":[]}
    run_full_game(deck,player,dealer)


