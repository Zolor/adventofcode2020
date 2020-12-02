import re
import time
start_time = time.time()

valid_passwords = 0

with open('input.txt') as input:
    for i in input.readlines():
        bigger_than = int(re.search("^[0-9]{1,2}", i).group(0))
        less_than = int(re.search("(?<=-)\\d{1,2}", i).group(0))
        match = re.search("(?<!:)[a-zA-Z]", i).group(0)
        entry = re.search("(?<=: )[a-zA-Z]*$", i).group(0)
        
        result = 0
        for x in entry:
            if x == match:
                result += 1
        if result >= bigger_than and result <= less_than:
            valid_passwords += 1

print("Valid Passwords: " + str(valid_passwords))
print("--- %s seconds ---" % (time.time() - start_time))