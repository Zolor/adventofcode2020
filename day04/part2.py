
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
        if all(entries in lex for entries in check):
            if (1920 <= int(lex.get("byr")) <= 2002):
                count += 1
                print("Birth Year Check")
            if (2010 <= int(lex.get("iyr")) <= 2020):
                count += 1
                print("Issue Year Check")
            if (2020 <= int(lex.get("eyr")) <= 2030):
                count += 1
                print("Expiration Year Check")
            height = lex.get("hgt")
            if height.endswith("cm"):
                if (150 <= int(height.strip("cm")) <= 193):
                    count += 1
                    print("Height CM Check")
            elif height.endswith("in"):
                if (59 <= int(height.strip("in")) <= 76):
                    count += 1
                    print("Height IN Check")
            if lex.get("hcl").startswith("#") and int(lex.get("hcl")[1:],16) and len(lex.get("hcl")) == 7:
                count += 1
                print("Hair Color Check")
            if lex.get("ecl") in ["amb","blu","brn","gry","grn","hzl","oth"]:
                count += 1
                print("Eye Color Check")
            if lex.get("pid").isnumeric() and len(lex.get("pid")) == 9:
                count += 1
                print("PID Check")
        if count == calc:
            valid_passports += 1
        print("Done!")
        print(lex)
    print("Valid:" + str(valid_passports))


""" byr (Birth Year) - four digits; at least 1920 and at most 2002.
iyr (Issue Year) - four digits; at least 2010 and at most 2020.
eyr (Expiration Year) - four digits; at least 2020 and at most 2030.
hgt (Height) - a number followed by either cm or in:
If cm, the number must be at least 150 and at most 193.
If in, the number must be at least 59 and at most 76.
hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f.
ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth.
pid (Passport ID) - a nine-digit number, including leading zeroes.
cid (Country ID) - ignored, missing or not. """

check_validity()