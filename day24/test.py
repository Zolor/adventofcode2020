testdict = {}

x = 0
y = 0
tile = [x,y]

tile[x] = 3
tile[y] = 5
tile[x] += 1

tile = tuple(tile)
print(type(tile))
testdict[tile] = True

print(testdict)