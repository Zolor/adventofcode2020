import re
import functools

data = open("input.txt").read().split("\n")

ruless = []

for line in data:
    if line == "":
        break
    else:
        ruless.append(line)

rules = {}
for line in ruless:
    num, rule = line.split(': ')
    num = int(num)
    if rule[0] == '"':
        rule = rule[1] # Single character
        rules[num] = [rule]
        continue
    options = []
    for opt in rule.split('|'):
        options.append(tuple(map(int, opt.split())))
    rules[num] = options

print(rules)

def gen_rule_regex(rules, start):
    @functools.lru_cache()
    def impl(start):
        parts = []
        for option in rules[start]:
            if isinstance(option, str):
                parts.append(option)
            else:
                parts.append(''.join(impl(item) for item in option))
        if len(parts) == 1:
            return parts[0]
        return '(?:' + '|'.join(parts) + ')'
    return impl(start)

print(gen_rule_regex(rules, 0))
