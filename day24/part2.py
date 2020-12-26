from copy import deepcopy

data = open("input.txt").read().split("\n")

floor = {}

for line in data:
    tile = [0,0]
    skip = False
    for num, direction in enumerate(line):
        #Make sure we skip next letter if we find a double
        if skip == True:
            skip = False
            continue
        if direction == "s":
            if line[num + 1] == "w":
                tile[0] -= 1
                tile[1] -= 0.5
            elif line[num + 1] == "e":
                tile[0] -= 1
                tile[1] += 0.5
            skip = True
        elif direction == "n":
            if line[num + 1] == "w":
                tile[0] += 1
                tile[1] -= 0.5
            elif line[num + 1] == "e":
                tile[0] += 1
                tile[1] += 0.5
            skip = True
        elif direction == "w":
            tile[1] -= 1
        elif direction == "e":
            tile[1] += 1
    tmp_tile = tuple(tile)
    if tmp_tile in floor:
        floor[tmp_tile] = not floor.get(tmp_tile)
    else:
        floor[tmp_tile] = True

def flipper(tile):
    tmp_set = set()
    collect_black = 0
    #Check southeast, southwest, northwest, and northeast
    #True = Black, White = False
    for x in [-1, 1]:
        for y in [-0.5, 0.5]:
            if (tile[0] + x, tile[1] + y) not in floor:
                tmp_set.add((tile[0] + x, tile[1] + y))
            elif floor[(tile[0] + x, tile[1] + y)] == True:
                collect_black += 1
            else:
                tmp_set.add((tile[0] + x, tile[1] + y))
    #Check East
    if (tile[0],tile[1] + 1) in floor:
        if floor[(tile[0],tile[1] + 1)] == True:
            collect_black += 1
        else:
            tmp_set.add((tile[0],tile[1] + 1))
    else:
        tmp_set.add((tile[0],tile[1] + 1))
    #Check West
    if (tile[0],tile[1] - 1) in floor:
        if floor[(tile[0],tile[1] - 1)] == True:
            collect_black += 1
        else:
            tmp_set.add((tile[0],tile[1] - 1))
    else:
        tmp_set.add((tile[0],tile[1] - 1))
    return collect_black, tmp_set

days = 0
while days < 100:
    tmp_floor = {}
    orig_tmp_set = set()
    for tile in floor.keys():
        if floor[tile] == False:
            continue
        collect, tmp_set2 = flipper(tile)
        orig_tmp_set |= tmp_set2
        #Count how many tiles and act accordingly to our tile color True = Black False = White
        if collect == 0 or collect > 2:
            tmp_floor[tile] = False
        else:
            tmp_floor[tile] = True
    for white_tile in orig_tmp_set:
        collect, _ = flipper(white_tile)
        if collect == 2:
            tmp_floor[white_tile] = True
        else:
            tmp_floor[white_tile] = False

    floor = deepcopy(tmp_floor)
    days += 1

summa = 0
for item in floor.values():
    if item == True:
        summa += 1

print(summa)