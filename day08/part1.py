import re

forms = open("input.txt").read().split("\n")
tmp = range(len(forms))
program = dict(zip(tmp,forms))
checklist = []
accumulator = 0
instruction = 0

while instruction not in checklist:
    if program.get(instruction).startswith("nop"):
        checklist.append(instruction)
        instruction += 1
    elif program.get(instruction).startswith("acc"):
        accumulator += int((re.search(r"[\d\(\)\-+]+$", program.get(instruction))).group(0))
        checklist.append(instruction)
        instruction += 1
    elif program.get(instruction).startswith("jmp"):
        checklist.append(instruction)
        instruction += int((re.search(r"[\d\(\)\-+]+$", program.get(instruction))).group(0))

print(accumulator)

