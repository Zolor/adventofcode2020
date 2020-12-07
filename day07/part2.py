import re

bags_itinerary = open("input.txt").read().split("\n")

def bag_counter(color, amount, summa):
    for bags in bags_itinerary:
        if bags.startswith(color) and not bags.endswith("no other bags."):
            for b in re.finditer(r"\d.+?(?= bag)", bags):
                col = b.group(0)[2:]
                num = b.group(0)[0]
                summa += int(num) * amount
                summa = bag_counter(col, int(num) * amount, summa)
    return summa

print(bag_counter("shiny gold", 1, 0))