navigation = open("input.txt").read().split("\n")

waypoint = {"N":1, "E":10, "S":0, "W":0}
location = {"N":0, "E":0, "S":0, "W":0}
nav = ["N", "E", "S", "W"]

for i in navigation:
    direction = i[0]
    if direction == "L" or direction == "R":
        turns = int(int(i[1:]) / 90)
        for x in range(turns):
            if direction == "R":
                tmp = waypoint.get("N")
                waypoint["N"] = waypoint.get("W")
                waypoint["W"] = waypoint.get("S")
                waypoint["S"] = waypoint.get("E")
                waypoint["E"] = tmp
            elif direction == "L":
                tmp = waypoint.get("N")
                waypoint["N"] = waypoint.get("E")
                waypoint["E"] = waypoint.get("S")
                waypoint["S"] = waypoint.get("W")
                waypoint["W"] = tmp
    elif direction in nav:
        waypoint[direction] += int(i[1:])
    elif i[0] == "F":
        for k, v in waypoint.items():
            location[k] += int(i[1:]) * v

longitude = abs(location.get("N") - location.get("S"))
latitude = abs(location.get("W") - location.get("E"))
print(latitude + longitude)