#absolute value of x1-x2 + absolute value of y1-y2
with open("day3_inputs") as f:
    wireRoutes = [i.split(",") for i in f.read().split("\n")]
    print(wireRoutes)

def moves(wireRoute, ):
    x = 0
    y = 0
    moveList = []
    for point in wireRoute:
        if point[0] == "R":
            x += int(point[1:])
        if point[0] == "L":
            x -= int(point[1:])
        if point[0] == "U":
            y += int(point[1:])
        if point[0] == "D":
            y -= int(point[1:])
        moveList.append((x,y))
    return moveList

def getDistance(intersection):
    centerPoint = (0, 0)
    distance = abs(intersection[0] - centerPoint[0]) + abs(intersection[1] - centerPoint[1])
    return distance

a = moves(wireRoutes[0])
b = moves(wireRoutes[1])
intersections = [i for i in a for i in b]
print(intersections)
distances = [getDistance(intersection) for intersection in intersections]
distances.remove(distances[0])
minDistance = min(distances)

print(minDistance)

