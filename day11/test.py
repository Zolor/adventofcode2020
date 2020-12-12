seatlist = open("testinput.txt").read().split("\n")

print(seatlist)

for i in seatlist:
    if "L" in i:
        print("True")




                        #Down            Up                right          left          Up Left                 Up Right            Down Left            Down Right
#if "." or "L" in (array[y + 1][x], array[y - 1][x], array[y][x + 1], array[y][x - 1], array[y - 1][x - 1], array[y + 1][x + 1], array[y + 1][x - 1], array[y + 1][x + 1]):