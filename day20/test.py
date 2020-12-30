import re

data = open("testdragon.txt").read().split("\n")

sea = [l for l in data]

head_regex = re.compile("(?=..................#.)")
mid_regex = re.compile("#[.#]{4}[#]{2}[.#]{4}[#]{2}[.#]{4}[#]{3}")
bot_regex = re.compile("[.#]{1}#[.#]{2}#[.#]{2}#[.#]{2}#[.#]{2}#[.#]{2}#[.#]{3}")

sea_monsters = 0
for n, s in enumerate(sea):
    if n == len(s) - 1:
        continue
    else:
        for match in head_regex.finditer(s):
            print(match.start)
            if mid_regex.match(sea[n+1], match.start()) and bot_regex.match(sea[n+2], match.start()):
                sea_monsters += 1
print(sea_monsters)