import collections

data = open("testinput.txt").read().split("\n")

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
    
    def get_sides(self):
        #Return a list of all corners
        return([self.top, self.right, self.bottom, self.left])

    def flipper(self):
        #Take a list of strings and return it flipped
        tmp_img = []
        for line in self.content:
            tmp_img.append(''.join(reversed(line)))
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
                flipped_side2 = side2[len(side2)::-1]
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
            image = tile_dct[start_corner].get_content()
            right_side = start_corner_sides[1]
            down_side = start_corner_sides[2]
            break
    if counter == 4:
        tile_dct[start_corner].flipper()
    elif counter == 8:
        tile_dct[start_corner].flipper()
        tile_dct[start_corner].rotate()
    elif counter == 9:
        tile_dct[start_corner].flipper()
    else:
        tile_dct[start_corner].rotate()

#Find our next piece and rotate it correctly towards our previous piece
prev_piece = start_corner
print(prev_piece)
curr_piece = [k for k,v in matches.get(prev_piece).items() if v == right_side or v == ''.join(reversed(right_side))][0]
count = 0
line = 0
corner = False

while count < 9:
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
    if right_side in sides:
        reverse = False
    elif ''.join(reversed(right_side)) in sides:
        reverse = False
    if reverse == True:
        tile_dct[curr_piece].flipper()
        reverse = False
    #Append to image
    if corner:
        image.append("")
        line = len(image)
        for tile_line in tile_dct[curr_piece].get_content():
            image.append(tile_line)
        down_side = tile_dct[curr_piece].get_sides()[2]
        corner = False
    else:
        for num, tile_line in enumerate(tile_dct[curr_piece].get_content()):
            image[line + num] += " " + tile_line
    for image_line in image:
        print(image_line)
    print("LOL")

    prev_piece = curr_piece
    right_side = tile_dct[prev_piece].get_sides()[1]
    #Check if we've reached corner
    if len([k for k,v in matches.get(prev_piece).items() if v == right_side or v == ''.join(reversed(right_side))]) == 0:
        prev_piece = start_corner
        curr_piece = [k for k,v in matches.get(prev_piece).items() if v == down_side or v == ''.join(reversed(down_side))][0]
        start_corner = curr_piece
        right_side = tile_dct[prev_piece].get_sides()[2]
        corner = True
    else:
        prev_piece = curr_piece
        right_side = tile_dct[prev_piece].get_sides()[1]
        curr_piece = [k for k,v in matches.get(prev_piece).items() if v == right_side or v == ''.join(reversed(right_side))][0]
    count += 1
