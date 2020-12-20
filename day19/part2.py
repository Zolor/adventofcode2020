import re

data = open("input_part2.txt").read().split("\n")

messages = []
dct_rules = {}
summa = 0

istrue = False
for line in data:
    if line == "":
        istrue = True
    elif istrue:
        messages.append(line)
    else:
        k, _, v = line.partition(": ")
        dct_rules[k] = v

def gen_regex(rules, messages):
    def get_regex(s):
        if s == '|':
            return s

        rule = dct_rules[s]
        if rule.startswith('"'):
            return rule.strip('"')
        else:
            return f'({"".join(get_regex(part) for part in rule.split())})'
    
    reg_42 = re.compile(get_regex("42"))
    reg_31 = re.compile(get_regex("31"))

    count = 0
    for message in messages:
        pos = 0

        count_42 = 0
        match = reg_42.match(message, pos)
        while match:
            count_42 += 1
            pos = match.end()
            match = reg_42.match(message, pos)
        
        count_31 = 0
        match = reg_31.match(message, pos)
        while match:
            count_31 += 1
            pos = match.end()
            match = reg_31.match(message, pos)

        if pos == len(message) and 0 < count_31 < count_42:
            count += 1
    
    return count
            
print(gen_regex(dct_rules, messages))