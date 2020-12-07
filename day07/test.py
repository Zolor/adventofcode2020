import re
bags_itinerary = open("testinput.txt").read().split("\n")

for bag in bags_itinerary:
    for b in re.finditer(r"\d.+?(?= bag)", bag):
        print(b)