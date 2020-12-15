data = open("input.txt").read().split(",")

memory = []
for i in data:
    memory.append(int(i))
number = len(memory)

while number != 2020:
    indices = [i for i, x in enumerate(memory) if x == memory[number-1]]
    if len(indices) == 1:
        memory.append(0)
    else:
        indices.pop(len(indices) - 1)
        memory.append((number - 1) - max(indices))
    number += 1

print(memory)
print(memory[2020-1])