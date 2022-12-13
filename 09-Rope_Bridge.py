with open("Motion_Series_test.txt", "r") as file:
    motion_series = file.read().splitlines()
print(motion_series)


def move(a1, b1, x1, y1):
    if abs(x1 - a1) > 1:
        if x1 > a1:
            a1 += 1
            b1 = y1
        if x1 < a1:
            a1 -= 1
            b1 = y1
    if abs(y1 - b1) > 1:
        if y1 > b1:
            b1 += 1
            a1 = x1
        if y1 < b1:
            b1 -= 1
            a1 = x1
    return a1, b1


x, y = 0, 0
position = [(0, 0)]
a, b = 0, 0
tail = []
for motion in motion_series:
    steps = int(motion[2:])
    if motion[0] in ["R", "L"]:
        if motion[0] == "R":
            for i in range(steps):
                x += 1
                position.append((x, y))
                a, b = move(a, b, x, y)
                tail.append((a, b))
        else:
            for i in range(steps):
                x -= 1
                position.append((x, y))
                a, b = move(a, b, x, y)
                tail.append((a, b))
    else:
        if motion[0] == "U":
            for i in range(steps):
                y -= 1
                position.append((x, y))
                a, b = move(a, b, x, y)
                tail.append((a, b))
        else:
            for i in range(steps):
                y += 1
                position.append((x, y))
                a, b = move(a, b, x, y)
                tail.append((a, b))
print(position)
print(tail)
print(len(set(tail)))

# Part 2
