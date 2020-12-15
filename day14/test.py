import math
import re
bit_data = open("testinput.txt").read().split("\n")

memory = {}

for i in bit_data:
    if i.startswith("mask"):
        mask = i.split(" = ")[1]
        print(mask)
    elif i.startswith("mem"):
        val = [int(s) for s in i.split() if s.isdigit()]
        print(val)
        binar = bin(val[0])[2:].zfill(36)
        print(binar)
        mem_space = re.search(r"\[(.*?)\]", i).group(1)
        print(mem_space) 

x = 34359738368
while True:
    x = x // 2
    print(x)
    if x == 0:
        break