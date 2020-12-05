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

    elif bpass[state] == "R" or bpass[state] == "B":
        middle = findMiddle(result, "U")
        result = range(middle, result[-1]+1)
        state += 1
        return recursiva_functiona(state, result, bpass)
    
    elif bpass[state] == "F" or bpass[state] == "L":
        middle = findMiddle(result, "L")
        result = range(result[0],middle)
        state +=1
        return recursiva_functiona(state, result, bpass)


def findMiddle(input_list, direction):
    middle = float(len(input_list))/2
    if direction == "U":
        return (input_list[int(middle + .5)])
    if direction == "L":
        return (input_list[int(middle)])

for i in boardingpasses:
    row = recursiva_functiona(0, range(127), i[:7])
    seat = recursiva_functiona(0, range(7), i[7:])
    seatID = (row * 8) + seat
    lista.append(seatID)

for i in range(min(lista),max(lista)):
    plus = False
    minus = False
    if i in lista:
        continue
    if i + 1 in lista:
        plus = True
    if i - 1 in lista:
        minus = True
    if plus == True and minus == True:
        print("My Seat number is: " + str(i))

print("--- %s seconds ---" % (time.time() - start_time))