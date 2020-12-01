import itertools
list = set()
with open('input.txt') as input:
	for i in input.readlines():
		list.add(i.rstrip())

for a, b in itertools.combinations(list, 2):
    if int(a) + int(b) == 2020:
        print(int(a) * int(b))

