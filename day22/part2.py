import time
start_time = time.time()
from copy import deepcopy

data = open("input.txt").read().split("\n")

orig_player1 = []
orig_player2 = []

condition = False
for line in data:
    if line == "Player 2:":
        condition = True
        continue
    elif line == "Player 1:" or line == "":
        continue
    if condition == False:
        orig_player1.append(int(line))
    elif condition == True:
        orig_player2.append(int(line))

def round(player1, player2):
    state = []
    while True:
        status, state = state_check(player1, player2, state)
        if status == True:
            return("player1")
        p1_card = player1.pop(0)
        p2_card = player2.pop(0)
        #If both players have at least as many cards remaining in their deck as the value of the card they just drew,
        #the winner of the round is determined by playing a new game of Recursive Combat (see below).
        if p1_card <= len(player1) and p2_card <= len(player2):
            winner = round(deepcopy(player1[0:p1_card]),deepcopy(player2[0:p2_card]))
            if winner == "player1":
                player1.append(p1_card)
                player1.append(p2_card)
            else:
                player2.append(p2_card)
                player2.append(p1_card)
        else:
            if p1_card > p2_card:
                player1.append(p1_card)
                player1.append(p2_card)
            else:
                player2.append(p2_card)
                player2.append(p1_card)
        if len(player1) == 0:
            return("player2")
        elif len(player2) == 0:
            return("player1")
        
def calculate_score(winner):
    summa = 0
    for i in range(1, len(winner) + 1):
        summa += i * winner.pop(-1)
    return(summa)

#Check wheter if there was a previous round in this game that had exactly the same cards in the same order. Return True if true
def state_check(p1_cards, p2_cards, curr_state):
    cards = tuple()
    cards = cards + tuple(p1_cards) + (-1,) + tuple(p2_cards)
    cards = hash(cards)
    if cards in curr_state:
        return True, curr_state
    else:
        curr_state.append(cards)
        return False, curr_state

winner = round(orig_player1, orig_player2)
if winner == "player1":
    print("Player 1 Won")
    print(calculate_score(orig_player1))
else:
    print("Player 2 Won")
    print(calculate_score(orig_player2))

print("--- %s seconds ---" % (time.time() - start_time))