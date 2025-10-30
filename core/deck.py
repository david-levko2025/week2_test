import random

def build_standard_deck() -> list[dict]:
    suits = ['H','D','C','S']
    ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
    deck = []
    for suit in suits:
        for rank in ranks:
            deck.append({"rank":rank, "suit":suit})
    return deck

def shuffle_by_suit(deck: list[dict], swaps: int = 5000) -> list[dict]:
   list_of_suits = ['H','D','C','S']
   for i in range(swaps):
       index_i = random.randint(0,51)
       index_i = deck[index_i]
       index_j_good = False
       while not index_j_good:
           index_j = random.randint(0,51)
           card_j = deck[index_j]
           if index_j_good != index_i:
               if card_j in ["list_of_suit"] == 'H' and card_j["list_of_suit"] % 5:
                   index_j, index_i = index_i, index_j
                   break
               elif card_j in ["list_of_suit"] == 'D' and card_j["list_of_suit"] % 3:
                   index_j,index_i = index_i ,index_j
                   break
               elif card_j in ["list_of_suit"] == 'C'and card_j["list_of_suit"] % 2 == 0:
                   index_j, index_i = index_i, index_j
                   break
               elif card_j in ["list_of_suit"] == 's' and card_j["list_of_suit"] % 7:
                   index_j, index_i = index_i, index_j
                   break
   return deck

