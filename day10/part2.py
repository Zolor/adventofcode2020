import time
start_time = time.time()
adapters = [int(i) for i in open("input.txt").read().split("\n")]

adapters.append(0)
adapters.append(max(adapters) + 3)
adapters = sorted(adapters)
subsum = 1
count = 0

for x, n in enumerate(adapters):
    if x == len(adapters) - 1:
        break
    diff = adapters[x+1] - adapters[x]
    if diff == 3 and count > 1:
        if count == 2:
            subsum = subsum * 2
        elif count == 3:
            subsum = subsum * 4
        elif count == 4:
            subsum = subsum * 7
        count = 0
    elif diff == 3 and count == 1:
        count = 0
    elif diff == 1:
        count += 1

print(subsum)
print("--- %s seconds ---" % (time.time() - start_time))