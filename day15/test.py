memory = [10,16,6,0,1,17]
memory2 = "10,16,6,0,1,17"
print(len(memory))

indices = [i for i, x in enumerate(memory)]
indices.pop(len(indices) - 1)
print(indices)

num_list = list(map(int, memory2.split(',')))
print(num_list)

numbers = {v: i + 1 for i, v in enumerate(indices)}
print(numbers)