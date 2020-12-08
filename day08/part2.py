import time
start_time = time.time()
import re, copy

forms = open("input.txt").read().split("\n")
tmp = range(len(forms))
inputs = dict(zip(tmp,forms))
counter = 0

def check_compatibility(program):
    instruction = 0
    accumulator = 0
    checklist = []
    length = len(program)
    while instruction not in checklist:
        if instruction >= length:
            return(accumulator)
        elif program.get(instruction).startswith("nop"):
            checklist.append(instruction)
            instruction += 1
        elif program.get(instruction).startswith("acc"):
            accumulator += int((re.search(r"[\d\(\)\-+]+$", program.get(instruction))).group(0))
            checklist.append(instruction)
            instruction += 1
        elif program.get(instruction).startswith("jmp"):
            checklist.append(instruction)
            instruction += int((re.search(r"[\d\(\)\-+]+$", program.get(instruction))).group(0))
    return(None)
    
for i in forms:
    tmp = copy.deepcopy(inputs)
    if "nop" in i:
        tmp[counter] = i.replace("nop", "jmp")
        out = check_compatibility(tmp)
        if out != None:
            print(out)
            break
    elif "jmp" in i:
        tmp[counter] = i.replace("jmp", "nop")
        out = check_compatibility(tmp)
        if out != None:
            print(out)
            break
    counter += 1

print("--- %s seconds ---" % (time.time() - start_time))