import time
start_time = time.time()

import re

bags_itinerary = open("input.txt").read().split("\n")
list_of_bags = ["shiny gold"]
len_check = 0
checker = False

def bag_counter(color):
    list_of_found_bags = []
    for bags in bags_itinerary:
        if color in bags and not bags.startswith(color):
            list_of_found_bags.append((re.search("^.+?(?= bags)", bags).group(0)))
    if len(list_of_found_bags) > 0:
        return(True,list_of_found_bags)
    else:
        return(False, None)


while len_check != len(list_of_bags):
    for i in list_of_bags:
        checker, lista = bag_counter(i)
        if checker == True:
            for b in lista:
                list_of_bags.append(b)
            len_check = len(list_of_bags)
        else:
            len_check = len(list_of_bags)

print(len(set(list_of_bags)) - 1)
print("--- %s seconds ---" % (time.time() - start_time))