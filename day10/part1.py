adapters = (int(i) for i in open("input.txt").read().split("\n"))

sorted_adapters = sorted(adapters)
sorted_adapters.insert(0, 0)
sorted_adapters.append(max(sorted_adapters) + 3)
result_dict = {}

for x, n in enumerate(sorted_adapters):
    if x == len(sorted_adapters) - 1:
        break
    diff = sorted_adapters[x+1] - sorted_adapters[x]
    if not diff in result_dict:
        result_dict[diff] = 1
    else:
        result_dict[diff] += 1

print(result_dict.get(1) * result_dict.get(3))