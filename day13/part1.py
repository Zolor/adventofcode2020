bus_notes = open("input.txt").read().split("\n")

my_time = int(bus_notes[0])
buss_schedule = (bus_notes[1].split(","))
summa = {}

for buss in buss_schedule:
    if buss == "x":
        continue
    buss_depart = 0
    buss = int(buss)
    while buss_depart < my_time:
        buss_depart = buss_depart + buss
    summa[buss] = buss_depart - my_time

best_buss = min(summa, key=summa.get)

print(summa.get(best_buss) * best_buss)
