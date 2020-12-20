import collections

data = open("input.txt").read().split("\n")

tile_dct = {}
right,left,top,bottom = "","","",""
matches = collections.defaultdict(set)
summa = 1

for line in data:
    if "Tile" in line:
        key = line.split()[1].strip(":")
        count = 0
    elif line == "":
        tile_dct[key] = {"U":top,"L":left,"R":right,"D":bottom}
        top = ""
        left = ""
        right = ""
        bottom = ""
    else:
        if count == 0:
            top = line
            right += line[len(line) - 1]
            left += line[0]
            count += 1
        elif count == 9:
            bottom = line
            right += line[len(line) - 1]
            left += line[0]
        else:
            right += line[len(line) - 1]
            left += line[0]
            count += 1

for k, v in tile_dct.items():
    for side in v.values():
        for k2, v2 in tile_dct.items():
            if k == k2:
                continue
            for side2 in v2.values():
                flipped_side2 = side2[len(side2)::-1]
                if flipped_side2 == side or side2 == side:
                    matches[k].add(side2)
                    matches[k2].add(side)

for k, v in matches.items():
    if len(v) == 2:
        summa *= int(k)

print(summa)
