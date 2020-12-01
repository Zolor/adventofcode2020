import itertools
list = set()
with open('input.txt') as input:
	for i in input.readlines():
		list.add(int(i))

for a, b in itertools.combinations(list, 2):
    if a + b == 2020:
        print(a * b)

