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

summa = 0
for item in floor.values():
    if item == True:
        summa += 1

print(summa)