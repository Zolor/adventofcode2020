data = open("testinput.txt").read().split("\n")

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

summa = 0
for item in floor.values():
    if item == True:
        summa += 1

print(summa)

days = 1
while days < 2:
    tmp_floor = {}
    for tile in floor.keys():
        collect = {"black": 0, "white": 0}
        #Check southeast, southwest, northwest, and northeast
        for x in [-1, 1]:
            for y in [-0.5, 0.5]:
                if (tile[0] + x, tile[1] + y) not in floor:
                    collect["white"] += 1
                    tmp_floor[(tile[0] + x, tile[1] + y)] = False
                elif floor[(tile[0] + x, tile[1] + y)] == True:
                    collect["black"] += 1
                else:
                    collect["white"] += 1
        #Check East
        if (tile[0],tile[1] + y) in floor:
            if floor[(tile[0],tile[1] + y)] == True:
                collect["black"] += 1
            else:
                collect["white"] += 1
        else:
            collect["white"] += 1
            tmp_floor[(tile[0],tile[1] + y)] = False
        #Check West
        if (tile[0],tile[1] - y) in floor:
            if floor[(tile[0],tile[1] - y)] == True:
                collect["black"] += 1
            else:
                collect["white"] += 1
        else:
            collect["white"] += 1
            tmp_floor[(tile[0],tile[1] - y)] = False
        print(collect)
        #Count how many tiles and act accordingly to our tile color True = Black False = White
        if floor[tile] == True and (collect["black"] == 0 or collect["black"] > 2):
            tmp_floor[tile] = False
        elif floor[tile] == False and collect["black"] == 2:
            tmp_floor[tile] = True
        else:
            tmp_floor[tile] = floor.get(tile)
    floor = tmp_floor
    days += 1

    summa = 0
    for item in floor.values():
        if item == True:
            summa += 1

    print(summa)