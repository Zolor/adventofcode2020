map = []

with open('input.txt') as input:
    for i in input.readlines():
        map.append(i.rstrip()*len(i*3))

def count_tree(right, down):
    first = True
    sled_move = right
    tree_count = 0
    loop = 0
    for line in map:
        if first == True:
            first = False
            loop += 1
            continue
        elif line[sled_move] == "#" and down != 2:
            tree_count += 1
        elif loop % down == 0 and line[sled_move] == "#":
            tree_count += 1
        elif sled_move + right > len(line):
                return(tree_count)
        loop += 1
        sled_move += right
    return(tree_count)

print(count_tree(1,1) * count_tree(3,1) * count_tree(5,1) * count_tree(7,1) * count_tree(1,2))