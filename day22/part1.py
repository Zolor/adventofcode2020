data = open("input.txt").read().split("\n")

player1 = []
player2 = []

condition = False
for line in data:
    if line == "Player 2:":
        condition = True
        continue
    elif line == "Player 1:" or line == "":
        continue
    if condition == False:
        player1.append(int(line))
    elif condition == True:
        player2.append(int(line))

def round():
    p1_card = player1.pop(0)
    p2_card = player2.pop(0)
    if p1_card > p2_card:
        player1.append(p1_card)
        player1.append(p2_card)
    else:
        player2.append(p2_card)
        player2.append(p1_card)

def calculate_score(winner):
    summa = 0
    for i in range(1, len(winner) + 1):
        summa += i * winner.pop(-1)
    return(summa)

while True:
    round()
    if len(player1) == 0:
        print("Player 2 Won")
        print(calculate_score(player2))
        break
    elif len(player2) == 0:
        print("Player 1 Won")
        print(calculate_score(player1))
        break
