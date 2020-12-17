max_cycles = 6
from typing import NamedTuple


class Coord(NamedTuple):
	x: int
	y: int

dct = {}

for x in range(10):
    for y in range(10):
        dct[Coord(x,y)] = True

for key in dct.keys():
    print(key)

"""     
    for k, v in tmp_copy.items():
        if tmp_copy.get(k) == True:
            tmp_lista.append("#")
        else:
            tmp_lista.append(".")
        if len(tmp_lista) == len(x_range):
            print("".join(tmp_lista))
            tmp_lista = [] 
"""