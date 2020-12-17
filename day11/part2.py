from typing import NamedTuple
from copy import deepcopy

data = open("input.txt").read().split("\n")
cycle = 0
max_cycles = 6
summa = 0
dct = {}

class Coord(NamedTuple):
    w: int
    z: int
    y: int
    x: int

w_range = range(1 + (max_cycles) * 2)
x_range = range(len(data[0]) + max_cycles * 2)
y_range = range(len(data) + max_cycles * 2)
z_range = range(1 + (max_cycles) * 2)

#Fill our 3D diagram with Coord keys and all False values
for w in w_range:
    for z in z_range:
        for y in y_range:
            for x in x_range:
                dct[Coord(w,z,y,x)] = False

#Make sure we put our start data point in the middle of the 3D diagram
z_middle = int((1 + (max_cycles) * 2) / 2)

for y in range(len(data)):
    for x in range(len(data[0])):
        if data[y][x] == "#":
            dct[Coord(z_middle, z_middle, max_cycles + y, max_cycles + x)] = True

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

seatlist = [list(l) for l in open("input.txt").read().split("\n")]
tmp_array = []
state = True
summa = 0

len_array = len(seatlist[0])
height_array = len(seatlist)

def runda(array):
    tmp_array = deepcopy(array)
    for row in range(height_array):
        for seat in range(len_array):
            checker = 0
            for rowc in [-1,0,1]:
                for seatc in [-1,0,1]:
                    if not (rowc == 0 and seatc == 0):
                        new_row = row + rowc
                        new_seat = seat + seatc
                        while 0 <= new_row < height_array and 0 <= new_seat < len_array and array[new_row][new_seat]==".":
                            new_row = new_row + rowc
                            new_seat = new_seat + seatc
                        if 0 <= new_row < height_array and 0 <= new_seat < len_array and array[new_row][new_seat]=="#":
                            checker += 1
            if array[row][seat] == "L":
                if checker == 0:
                    tmp_array[row][seat] = "#"
            elif array[row][seat] == "#" and checker >= 5:
                tmp_array[row][seat] = "L"
    return(tmp_array)

while state == True:
    tmp_arr = runda(seatlist)
    if tmp_arr != seatlist:
        seatlist = tmp_arr
    else:
        seatlist = tmp_arr
        state = False

for elem in seatlist:
    summa += elem.count("#")

print(summa)