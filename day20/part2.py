import time
start_time = time.time()

import collections
import re

data = open("input.txt").read().split("\n")

tile_dct = {}
#Dict containing connections
matches = collections.defaultdict(dict)
start_corner = ""
image = []

class piece:
    def __init__(self, image):
        self.update_image(image)
    
    def update_image(self, image):
        self.right = "".join([i[-1:]for i in image])
        self.left = "".join([i[:1]for i in image])
        self.top = image[0]
        self.bottom = image[-1]
        self.content = image
    
    def get_content(self):
        return(self.content)

    def get_content_without_sides(self):
        tmp_img = []
        for line in self.content[1:-1]:
            tmp_img.append(line[1:-1])
        return(tmp_img)
    
    def get_sides(self):
        #Return a list of all corners
        return([self.top, self.right, self.bottom, self.left])

    def h_flipper(self):
        #Take a list of strings and return it flipped
        tmp_img = []
        for line in self.content:
            tmp_img.append(''.join(reversed(line)))
        self.update_image(tmp_img)

    def v_flipper(self):
        #Take a list of strings and return it flipped
        tmp_img = []
        for line in reversed(self.content):
            tmp_img.append(''.join(line))
        self.update_image(tmp_img)

    def rotate(self):
        self.update_image([''.join(list(i)[::-1]) for i in zip(*self.content)])

def build_data_struct():
    img = []
    for line in data:
        if "Tile" in line:
            key = line.split()[1].strip(":")
            count = 0
        elif line == "":
            tile_dct[key] = piece(img)
            img = []
        else:
            img.append(line)
            count += 1

build_data_struct()

for k, v in tile_dct.items():
    for side in v.get_sides():
        for k2, v2 in tile_dct.items():
            if k == k2:
                continue
            for side2 in v2.get_sides():
                flipped_side2 = ''.join(reversed(side2)) #side2[len(side2)::-1]
                if flipped_side2 == side:
                    matches[k].update({k2 : side2})
                elif side2 == side:
                    matches[k].update({k2 : side2})

#Find a corner piece
for key in matches.keys():
    if len(matches.get(key)) == 2:
        start_corner = key
        break

#For all corner piece buddies flip the corner piece until it's in a top left position
corners = matches.get(start_corner)
one, two = corners.values()
right_side = ""
down_side = ""

for counter in range(15):
    start_corner_sides = tile_dct[start_corner].get_sides()
    if start_corner_sides[1] in [one, two, ''.join(reversed(one)), ''.join(reversed(two))]:
        if start_corner_sides[2] in [one, two, ''.join(reversed(one)), ''.join(reversed(two))]:
            image = tile_dct[start_corner].get_content_without_sides()
            right_side = start_corner_sides[1]
            down_side = start_corner_sides[2]
            break
    if counter == 4:
        tile_dct[start_corner].h_flipper()
    elif counter == 8:
        tile_dct[start_corner].h_flipper()
        tile_dct[start_corner].rotate()
    elif counter == 9:
        tile_dct[start_corner].h_flipper()
    else:
        tile_dct[start_corner].rotate()

#Find our next piece and rotate it correctly towards our previous piece
prev_piece = start_corner
curr_piece = [k for k,v in matches.get(prev_piece).items() if v == right_side or v == ''.join(reversed(right_side))][0]
count = 0
line = 0
corner = False
pieces_added = 1

while True:
    correct_index = 0
    sides = tile_dct[curr_piece].get_sides()
    reverse = None
    if right_side in sides:
        correct_index = sides.index(right_side)
    elif ''.join(reversed(right_side)) in sides:
        correct_index = sides.index(''.join(reversed(right_side)))
    if corner:
        turns = 4 - correct_index
    else:
        turns = 3 - correct_index
    if turns > 0:
        for x in range(turns):
            tile_dct[curr_piece].rotate()

    sides = tile_dct[curr_piece].get_sides()
    if right_side in sides:
        reverse = False
    elif ''.join(reversed(right_side)) in sides:
        reverse = True
    if reverse == True:
        if corner:
            tile_dct[curr_piece].h_flipper()
        else:
            tile_dct[curr_piece].v_flipper()
        reverse = False
    #Append to image
    if corner:
        #image.append("")
        line = len(image)
        for tile_line in tile_dct[curr_piece].get_content_without_sides():
        #for tile_line in tile_dct[curr_piece].get_content_without_sides():
            image.append(tile_line)
        down_side = tile_dct[curr_piece].get_sides()[2]
        corner = False
        pieces_added += 1
    else:
        for num, tile_line in enumerate(tile_dct[curr_piece].get_content_without_sides()):
        #for num, tile_line in enumerate(tile_dct[curr_piece].get_content_without_sides()):
            image[line + num] += tile_line
        pieces_added += 1

    prev_piece = curr_piece
    right_side = tile_dct[prev_piece].get_sides()[1]
    #Check if we've reached corner
    if len([k for k,v in matches.get(prev_piece).items() if v == right_side or v == ''.join(reversed(right_side))]) == 0:
        prev_piece = start_corner
        if len([k for k,v in matches.get(prev_piece).items() if v == down_side or v == ''.join(reversed(down_side))]) != 0:
            curr_piece = [k for k,v in matches.get(prev_piece).items() if v == down_side or v == ''.join(reversed(down_side))][0]
            start_corner = curr_piece
            right_side = tile_dct[prev_piece].get_sides()[2]
            corner = True
        else:
            break
    else:
        prev_piece = curr_piece
        right_side = tile_dct[prev_piece].get_sides()[1]
        curr_piece = [k for k,v in matches.get(prev_piece).items() if v == right_side or v == ''.join(reversed(right_side))][0]
    count += 1

image = piece(image)

#Picture Complete!? Time to find seamonsters!
sea_monster_hash = 15

head_regex = re.compile("(?=[.#]{18}#[.#]{1})")
mid_regex = re.compile("#[.#]{4}[#]{2}[.#]{4}[#]{2}[.#]{4}[#]{3}")
bot_regex = re.compile("[.#]{1}#[.#]{2}#[.#]{2}#[.#]{2}#[.#]{2}#[.#]{2}#[.#]{3}")

def find_seamonsters(img):
    sea_monsters = 0
    tmp_img = img.get_content()
    for n in range(len(tmp_img) - 1):
        for match in head_regex.finditer(tmp_img[n]):
            if mid_regex.match(tmp_img[n+1], match.start()) and bot_regex.match(tmp_img[n+2], match.start()):
                sea_monsters += 1
    return sea_monsters

counter = 0
while True:
    found_monsters = find_seamonsters(image)
    if found_monsters == 0:
        image.rotate()
        if counter == 4:
            image.h_flipper()
        elif counter == 8:
            image.v_flipper()
        elif counter == 12:
            image.h_flipper()
            image.v_flipper()
    else:
        hashtags = 0
        for row in image.get_content():
            for x in row:
                if x == "#":
                    hashtags += 1
        print(hashtags - (found_monsters * sea_monster_hash))
        break
    if counter > 15:
        break
    counter += 1

print("--- %s seconds ---" % (time.time() - start_time))

#2136 Too low
#2586 Too high