import itertools

lista = open("input.txt").read().split("\n")

preamble = 25
counter = 0

def is_valid(indexer):
    preamble_list = lista[counter:counter + preamble]
    for numbers in itertools.combinations(preamble_list, 2):
        tmp = [int(i) for i in numbers]
        if sum(tmp) == int(lista[indexer]):
            return True
    return False


while counter < (len(lista) - preamble):
    if is_valid(preamble + counter) == False:
        print(lista[preamble + counter])
    counter += 1