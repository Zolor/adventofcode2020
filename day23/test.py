data = open("testinput.txt").read()

clock = [int(i) for i in data]
print(clock)
for x in range(max(clock) + 1, 1000000 + 1):
    clock.append(x)

print(max(clock))

""" 
pick_up = []
curr_cup = 0
start = curr_cup + 1

for cup in range(3):
    pick_up.append(clock.pop(start))

print(pick_up)
print(clock)

pick_up.reverse()

for cup in pick_up:
    clock.insert(clock.index(2) + 1, cup)

print(pick_up)
print(clock)
 """