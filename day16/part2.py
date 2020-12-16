from collections import defaultdict

data = open("input.txt").read().split("\n")

ticket_dct = {}
ticket_dct2 = defaultdict(list)
summa = 1
valid_tickets = []
my_ticket = []

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
    ticket_dct[text] = tmp_list

ordered_lista = ["" for m in ticket_dct.keys()]

pay_attention = False
my_ticket_found = False

for line in data:
    if my_ticket_found:
        my_ticket = [int(l) for l in line.split(",")]
        my_ticket_found = False
    elif pay_attention:
        x_found = False
        for x in line.split(","):
            if any(int(x) in val for val in ticket_dct.values()):
                continue
            else:
                x_found = True
        if not x_found:
            ticket = [int(l) for l in line.split(",")]
            valid_tickets.append(ticket)
    else:
        if line == "nearby tickets:":
            pay_attention = True
        if line == "your ticket:":
            my_ticket_found = True

for k in ticket_dct.keys():
    for ticket_pos in range(0, len(valid_tickets[0])):
        n = 0
        for ticket in range(0, len(valid_tickets)):
            if valid_tickets[ticket][ticket_pos] in ticket_dct.get(k):
                n += 1
            else:
                break
        if n == len(valid_tickets) and ordered_lista[ticket_pos] == "":
            ticket_dct2[k].append(ticket_pos)

while ticket_dct2:
    for key, val in ticket_dct2.items():
        if len(val) == 1:
            tmp_val = val.pop()
            ordered_lista[tmp_val] = key
            for key2, val2 in ticket_dct2.items():
                if tmp_val in val2:
                    ticket_dct2[key2].remove(tmp_val)
    if not any(ticket_dct2.values()):
        break

for x, i in enumerate(ordered_lista):
    if "departure" in i:
        summa *= my_ticket[x]
print(summa)