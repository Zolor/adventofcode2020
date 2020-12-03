map = []
counter = 0
tree_count = 0
first = True
with open('input.txt') as input:
    for i in input.readlines():
        map.append(i.rstrip()*len(i*2))

for line in map:
    if first == True:
        first = False
        continue
    counter += 3
    if line[counter] == "#":
        tree_count += 1
        if counter + 6 > len(line):
            print(tree_count)
            quit()

print(tree_count)