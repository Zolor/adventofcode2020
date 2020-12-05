import time
start_time = time.time()

boardingpasses = open("input.txt").read().split("\n")
highest = 0
lista = []

def recursiva_functiona(state, result, bpass):
    if isinstance(result, int):
        return result
# B and R = Upper, F and L means lower
    if len(result) == 1:
        if bpass[state] == "R" or bpass[state] == "B":
            result = result[-1] + 1
        elif bpass[state] == "F" or bpass[state] == "L":
            result = result[0]
        return recursiva_functiona(state, result, bpass)
    else:
        result = findMiddle(result, bpass[state])
        state += 1
        return recursiva_functiona(state, result, bpass)

def findMiddle(input_list, direction):
    middle = float(len(input_list))/2
    if direction == "R" or direction == "B":
        return range((input_list[int(middle + .5)]), input_list[-1]+1)
    if direction == "F" or direction == "L":
        return range(input_list[0],(input_list[int(middle)]))

for i in boardingpasses:
    row = recursiva_functiona(0, range(127), i[:7])
    seat = recursiva_functiona(0, range(7), i[7:])
    lista.append((row * 8) + seat)

for i in range(min(lista),max(lista)):
    if i not in lista and i + 1 in lista and i - 1 in lista:
        print("My Seat number is: " + str(i))

print("--- %s seconds ---" % (time.time() - start_time))