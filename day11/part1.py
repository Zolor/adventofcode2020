seatlist = open("input.txt").read().split("\n")
arr = []
state = True
summa = 0

for i in seatlist:
    arr += [i]

len_array = len(arr[0]) - 1
height_array = len(arr) - 1

def runda(array):
    tmp_array = []
    for y, row in enumerate(array):
        tmp_row = ""
        checker = ()
        for x, _ in enumerate(row):
            if x == 0 and y == 0: # Check if we're in a corner
                checker = (array[y][x + 1], array[y + 1][x], array[y + 1][x + 1])
            elif y == 0 and x == len_array:
                checker = (array[y][x - 1], array[y + 1][x], array[y + 1][x - 1])
            elif x == 0 and y == height_array:
                checker = (array[y][x + 1], array[y - 1][x], array[y - 1][x + 1])
            elif y == height_array and x == len_array:
                checker = (array[y][x - 1], array[y - 1][x], array[y - 1][x - 1])
            elif y == 0: # Check if we're at the top not corner
                checker = ( array[y + 1][x], array[y][x - 1], array[y][x + 1], array[y + 1][x - 1], array[y + 1][x + 1])
            elif x == 0: # Check if we're at the left side not corner
                checker = (array[y + 1][x], array[y - 1][x], array[y][x + 1], array[y + 1][x + 1], array[y - 1][x + 1])
            elif x == len_array: # Check if we're on the right side not corner
                checker = (array[y + 1][x], array[y - 1][x], array[y][x - 1], array[y - 1][x - 1], array[y + 1][x - 1])
            elif y == height_array: # Check if we're on the bottom not corner
                checker = (array[y - 1][x], array[y][x + 1], array[y][x - 1], array[y - 1][x - 1], array[y - 1][x + 1])
            else:
                checker = (array[y + 1][x], array[y - 1][x], array[y][x + 1], array[y][x - 1], array[y - 1][x - 1], array[y + 1][x + 1], array[y + 1][x - 1], array[y - 1][x + 1])
            if array[y][x] == "L":
                if "#" not in checker:
                    tmp_row += "#"
                else:
                    tmp_row += "L"
            elif array[y][x] == ".":
                tmp_row += "."
            elif array[y][x] == "#":
                if checker.count("#") > 3:
                    tmp_row += "L"
                else:
                    tmp_row += "#"
        tmp_array.append(tmp_row)
    return(tmp_array)


while state == True:
    tmp_arr = runda(arr)
    if tmp_arr != arr:
        arr = tmp_arr
    else:
        arr = tmp_arr
        state = False

for elem in arr:
    summa += elem.count("#")

print(summa)