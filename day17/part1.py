from typing import NamedTuple
from copy import deepcopy

data = open("input.txt").read().split("\n")
cycle = 0
max_cycles = 6
summa = 0
dct = {}

class Coord(NamedTuple):
    z: int
    y: int
    x: int

x_range = range(len(data[0]) + max_cycles * 2)
y_range = range(len(data) + max_cycles * 2)
z_range = range(1 + (max_cycles) * 2)

#Fill our 3D diagram with Coord keys and all False values
for z in z_range:
    for y in y_range:
        for x in x_range:
            dct[Coord(z,y,x)] = False

#Make sure we put our start data point in the middle of the 3D diagram
z_middle = int((1 + (max_cycles) * 2) / 2)

for y in range(len(data)):
    for x in range(len(data[0])):
        if data[y][x] == "#":
            dct[Coord(z_middle, max_cycles + y, max_cycles + x)] = True

def checker(key, state):
    checker = 0
    for xc in [-1,0,1]:
        for yc in [-1,0,1]:
            for zc in [-1,0,1]:
                if (xc == 0 and yc == 0 and zc == 0):
                    continue
                if dct.get(Coord(key.z + zc, key.y + yc, key.x + xc)) == True:
                    checker += 1
    if checker in [2,3] and state == True:
        return(True)
    elif checker == 3 and state == False:
        return(True)
    else:
        return(False)

#For key in dict, send to function to check wheter this should be true or false depending on neighbours
tmp_copy = deepcopy(dct)
tmp_lista = []
while cycle != max_cycles:
    for k, v in dct.items():
        tmp_copy[k] = checker(k, v)
    dct = deepcopy(tmp_copy)
    cycle += 1
    #print("================================================")

for k in dct:
    if dct.get(k) == True:
        summa += 1

print(summa)