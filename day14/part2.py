import re
import itertools
from itertools import combinations

bit_data = open("input.txt").read().split("\n")

memory = {}
mask = ""
summa = 0

#Return a list of all memory allocations we find for the int
def memory_finder(mem_val, msk):
    int_list = []
    res = ""
    #Flip int to binary
    binar_mem = bin(mem_val)[2:].zfill(36)
    #List of locations where X is found and converted into corresponding binary value
    x_list = []
    #List of resulting memory places in int
    res_list = []
    s = 34359738368
    for x, b in enumerate(msk):
        if b == "X":
            x_list.append(s)
            res += "0"
        elif b == "1":
            res += b
        elif b == "0":
            res += binar_mem[x]
        s = s // 2
    #Determine all possible combos and add to list
    res = int(res, 2)
    
    for n in range(1, len(x_list) + 1):
        int_list += [sum(comb) for comb in itertools.combinations(x_list, n)]
    for i in int_list:
        res_list.append(i + res)
    res_list.append(res)
    return res_list

for i in bit_data:
    if i.startswith("mask"):
        mask = i.split(" = ")[1]
    elif i.startswith("mem"):
        val = int(i.split(" = ")[1])
        #v = rewriter(val, mask)
        mem_space = int(re.search(r"\[(.*?)\]", i).group(1))
        #Call for a list of memory locations
        lista = memory_finder(mem_space, mask)
        #Update memory accordingly
        for item in lista:
            memory[item] = val
        #Do we need to flip the val going into mem? No?

for values in memory.values():
    summa += values

print(summa)