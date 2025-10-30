def ask_player_action() -> str:
    print("what do you want to do ?")
    choice = input('hit (H) or stand (S): ').upper()
    while choice != "S" or "H":
        choice = input('hit (H) or stand (S): ').upper()
    return choice



