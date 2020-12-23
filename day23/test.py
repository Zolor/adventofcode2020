data = open("input.txt").read()

test = {'1': '8', '8': '6', '6': '5', '5': '2', '2': '4', '4': '9', '9': '7', '7': '3'}

third_pointer = test[test[test[test["1"]]]]
tmp_lista = [test["1"],test[test["1"]],test[test[test["1"]]]]
print(third_pointer)
print(tmp_lista)

""" 
clock = [int(i) for i in data]
for x in range(max(clock) + 1, 10 + 1):
    clock.append(x)
first = clock[0]
last = clock[-1]
clock_dict = {clock[k-1]:clock[k] for k in range(1, len(clock))}
clock_dict[last] = first

print(clock_dict)


clock = [int(i) for i in data]
print(clock)
for x in range(max(clock) + 1, 1000000 + 1):
    clock.append(x)

print(max(clock))

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