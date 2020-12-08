import re
forms = open("testinput.txt").read().split("\n")

for i in forms:
    match = (re.search(r"[\d\(\)\-+]+$", i)).group(0)
    tmp = range(len(forms))
    program = dict(zip(tmp,forms))
print(len(program))