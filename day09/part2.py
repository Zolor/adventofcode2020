import itertools

lista = open("input.txt").read().split("\n")
int_lista = [int(i) for i in lista]

invalid_number = 1212510616
#invalid_number = 127 #TEST
counter = 0

for counter in range(len(int_lista)):
    preamble = 1
    summa = 0
    while summa <= invalid_number:
        summa = sum(int_lista[counter:counter + preamble])
        if summa == invalid_number:
            print(max(int_lista[counter:counter + preamble]) + min(int_lista[counter:counter + preamble]))
            quit()
        preamble += 1

