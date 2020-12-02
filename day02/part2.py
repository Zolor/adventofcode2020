import re
import time
start_time = time.time()

valid_passwords = 0

with open('input.txt') as input:
    for i in input.readlines():
        index_one = int(re.search("^[0-9]{1,2}", i).group(0))
        index_two = int(re.search("(?<=-)\\d{1,2}", i).group(0))
        match = re.search("(?<!:)[a-zA-Z]", i).group(0)
        entry = re.search("(?<=: )[a-zA-Z]*$", i).group(0)
        if entry[index_one-1] == match and entry[index_two-1] != match or entry[index_one-1] != match and entry[index_two-1] == match:
            valid_passwords += 1

print("Valid Passwords: " + str(valid_passwords))
print("--- %s seconds ---" % (time.time() - start_time))