data = open("input.txt").read()

clock = [int(i) for i in data]
cups = clock
curr_cup_index = 0
move = 1

for l in range(100):
    pick_up = []
    #Pick up the 3 cups
    pop_index = curr_cup_index + 1
    curr_cup = clock[curr_cup_index]
    for _ in range(3):
        if pop_index > (len(clock) - 1):
            pick_up.append(clock.pop(0))
        else:
            pick_up.append(clock.pop(pop_index))
    pick_up.reverse()
    dest_cup = curr_cup_index
    counter = 1
    #Find where to put our 3 cups and place accordingly
    while True:
        dest_cup = curr_cup - counter
        if dest_cup < 0:
            dest_cup = max(clock)
        if dest_cup in clock:
            for cup in pick_up:
                clock.insert(clock.index(dest_cup) + 1, cup)
            break
        counter += 1
    #Make sure to turn our list like a clock
    if curr_cup_index != clock.index(curr_cup):
        clock = clock[clock.index(curr_cup)-curr_cup_index:] + clock[:clock.index(curr_cup)-curr_cup_index]
    curr_cup_index += 1
    move += 1
    #Make sure we don't overflow our list index
    if curr_cup_index >= len(clock):
        curr_cup_index = 0

print(clock)

resultat = ""
ind = clock.index(1)
for x in clock:
    if clock[ind] == 1:
        ind += 1
        continue
    resultat += str(clock[ind])
    ind += 1
    if ind > len(clock) - 1:
        ind = 0
print(resultat)