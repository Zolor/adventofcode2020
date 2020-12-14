import re
bit_data = open("input.txt").read().split("\n")

memory = {}
mask = ""
summa = 0

# Takes value and mask and returns result
def rewriter(val, msk):
    res = ""
    #Convert val to binary
    binar = bin(val)[2:].zfill(36)
    #Make a new binary from mask
    for x, b in enumerate(msk):
        if b == "X":
            res += binar[x]
        else:
            res += mask[x]
    #Calculate int from new binary
    res = int(res, 2)
    #Return int
    return res

for i in bit_data:
    if i.startswith("mask"):
        mask = i.split(" = ")[1]
    elif i.startswith("mem"):
        val = int(i.split(" = ")[1])
        v = rewriter(val, mask)
        mem_space = re.search(r"\[(.*?)\]", i).group(1)
        memory[mem_space] = v

for values in memory.values():
    summa += values

print(summa)