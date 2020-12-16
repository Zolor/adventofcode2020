data = open("testinput.txt").read().split("\n")

dct = {}
summa = 0
valid_tickets = []

#For each line in data before "your ticket:"
for line in data:
    tmp_list = []
    if line == "":
        break
#Add text as keys and the 2 ranges in a list as values
    text, val = line.split(":")
    val1, val2 = val.split(" or ")
    range1, range2 = val1.strip().split("-")
    range3, range4 = val2.strip().split("-")
    tmp_list.extend(range(int(range1), int(range2) + 1))
    tmp_list.extend(range(int(range3), int(range4) + 1))
    dct[text] = tmp_list

#For each line after nearby tickets
pay_attention = False
for line in data:
    if pay_attention:
        for x in line.split(","):
            x_found = False
            for item in dct.values():
                #Verify each number exists in the dict
                if int(x) in item:
                    x_found = True
            if not x_found:
                #If one value does not exist add said value to sum
                summa += int(x)
    else:
        if line == "nearby tickets:":
            pay_attention = True
print(dct)
#Print sum
print(summa)