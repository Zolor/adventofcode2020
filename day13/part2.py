bus_notes = open("input.txt").read().split("\n")
buss_schedule = (bus_notes[1].split(","))
summa = {}
time = 1
lista = []
inc = 1

for x in range(len(buss_schedule)):
    if buss_schedule[x] == "x":
        continue
    summa[buss_schedule[x]] = x
    lista.append(int(buss_schedule[x]))
print(summa)

def find_xy(k, v, i, incr):
    while True:
        if (i + v) % k == 0:
            return(i)
        i += incr

for k, v in summa.items():
    time = find_xy(int(k) , v, time, inc)
    inc *= int(k)
print(time)
