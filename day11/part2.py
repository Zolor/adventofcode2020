from copy import deepcopy

seatlist = [list(l) for l in open("input.txt").read().split("\n")]
tmp_array = []
state = True
summa = 0

len_array = len(seatlist[0])
height_array = len(seatlist)

def runda(array):
    tmp_array = deepcopy(array)
    for row in range(height_array):
        for seat in range(len_array):
            checker = 0
            for rowc in [-1,0,1]:
                for seatc in [-1,0,1]:
                    if not (rowc == 0 and seatc == 0):
                        new_row = row + rowc
                        new_seat = seat + seatc
                        while 0 <= new_row < height_array and 0 <= new_seat < len_array and array[new_row][new_seat]==".":
                            new_row = new_row + rowc
                            new_seat = new_seat + seatc
                        if 0 <= new_row < height_array and 0 <= new_seat < len_array and array[new_row][new_seat]=="#":
                            checker += 1
            if array[row][seat] == "L":
                if checker == 0:
                    tmp_array[row][seat] = "#"
            elif array[row][seat] == "#" and checker >= 5:
                tmp_array[row][seat] = "L"
    return(tmp_array)

while state == True:
    tmp_arr = runda(seatlist)
    if tmp_arr != seatlist:
        seatlist = tmp_arr
    else:
        seatlist = tmp_arr
        state = False

for elem in seatlist:
    summa += elem.count("#")

print(summa)