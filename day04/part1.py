
passports = open("input.txt").read().split("\n\n")

check = ["ecl","pid","eyr","hcl","byr","iyr","hgt"]
calc = len(check)

def check_validity():
    valid_passports = 0
    for i in passports:
        tmp = i.split()
        lex = {}
        count = 0
        for x in tmp:
            if "\n" in x:
                tmplist = x.split("\n")
                for y in tmplist:
                    key, value = y.split(':')
                    lex[key] = value
            else:
                key, value = x.split(':')
                lex[key] = value
        print(lex)
        for item in check:
            if item in lex:
                count += 1
        if count == calc:
            valid_passports += 1
    print("Valid:" + str(valid_passports))

check_validity()