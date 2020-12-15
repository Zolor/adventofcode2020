data = open("input.txt").read().split(",")

numbers = []
for i in data:
    numbers.append(int(i))

memory = {v: i + 1 for i, v in enumerate(numbers)}

spoken = numbers[-1]
number = 1

for turn in range(len(memory) + 1, 30000000 + 1):
    last_spoken = spoken
    if spoken in memory:
        spoken = (turn - 1) - memory[spoken]
        memory[last_spoken] = turn - 1
    else:
        spoken = 0
        memory[last_spoken] = turn - 1
    number += 1

print(spoken)
