navigation = open("input.txt").read().split("\n")

facing = "E"
location = {"N":0, "E":0, "S":0, "W":0}
nav = ["N", "E", "S", "W"]

for i in navigation:
    direction = i[0]
    if direction == "L" or direction == "R":
        turns = int(i[1:]) / 90
        curr = nav.index(facing)
        if direction == "L":
            if curr - turns < 0:
                facing = nav[int(curr - turns + 4)]
            else:
                facing = nav[int((curr - turns) % 4)]
        elif direction == "R":
            facing = nav[int((curr + turns) % 4)]
    elif direction in nav:
        location[direction] += int(i[1:])
    elif i[0] == "F":
        location[facing] += int(i[1:])
    print(location)

longitude = abs(location.get("N") - location.get("S"))
latitude = abs(location.get("W") - location.get("E"))
print(latitude + longitude)