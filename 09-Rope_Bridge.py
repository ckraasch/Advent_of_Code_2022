with open("Motion_Series.txt", "r") as file:
    motion_series = file.read().splitlines()
    file.close()
print(motion_series)


def move(a, b, x, y, lst):
    if abs(x - a) > 1 and not abs(y - b) > 1:
        if x > a:
            a += 1
            b = y
        if x < a:
            a -= 1
            b = y
    if not abs(x - a) > 1 and abs(y - b) > 1:
        if y > b:
            b += 1
            a = x
        if y < b:
            b -= 1
            a = x
    if abs(x - a) > 1 and abs(y - b) > 1:
        if y > b:
            b += 1
        if y < b:
            b -= 1
        if x > a:
            a += 1
        if x < a:
            a -= 1
    if (a, b) not in lst:
        lst.append((a, b))
    return a, b


a0, b0 = 0, 0
a1, b1 = 0, 0
a2, b2 = 0, 0
a3, b3 = 0, 0
a4, b4 = 0, 0
a5, b5 = 0, 0
a6, b6 = 0, 0
a7, b7 = 0, 0
a8, b8 = 0, 0
a9, b9 = 0, 0
head = [(0, 0)]
knot1 = [(0, 0)]
knot2 = [(0, 0)]
knot3 = [(0, 0)]
knot4 = [(0, 0)]
knot5 = [(0, 0)]
knot6 = [(0, 0)]
knot7 = [(0, 0)]
knot8 = [(0, 0)]
tail = [(0, 0)]
for motion in motion_series:
    steps = int(motion[2:])
    if motion[0] in ["R", "L"]:
        if motion[0] == "R":
            for i in range(steps):
                a0 += 1
                head.append((a0, b0))
                a1, b1 = move(a1, b1, a0, b0, knot1)
                a2, b2 = move(a2, b2, a1, b1, knot2)
                a3, b3 = move(a3, b3, a2, b2, knot3)
                a4, b4 = move(a4, b4, a3, b3, knot4)
                a5, b5 = move(a5, b5, a4, b4, knot5)
                a6, b6 = move(a6, b6, a5, b5, knot6)
                a7, b7 = move(a7, b7, a6, b6, knot7)
                a8, b8 = move(a8, b8, a7, b7, knot8)
                a9, b9 = move(a9, b9, a8, b8, tail)
        else:
            for i in range(steps):
                a0 -= 1
                head.append((a0, b0))
                a1, b1 = move(a1, b1, a0, b0, knot1)
                a2, b2 = move(a2, b2, a1, b1, knot2)
                a3, b3 = move(a3, b3, a2, b2, knot3)
                a4, b4 = move(a4, b4, a3, b3, knot4)
                a5, b5 = move(a5, b5, a4, b4, knot5)
                a6, b6 = move(a6, b6, a5, b5, knot6)
                a7, b7 = move(a7, b7, a6, b6, knot7)
                a8, b8 = move(a8, b8, a7, b7, knot8)
                a9, b9 = move(a9, b9, a8, b8, tail)
    else:
        if motion[0] == "U":
            for i in range(steps):
                b0 += 1
                head.append((a0, b0))
                a1, b1 = move(a1, b1, a0, b0, knot1)
                a2, b2 = move(a2, b2, a1, b1, knot2)
                a3, b3 = move(a3, b3, a2, b2, knot3)
                a4, b4 = move(a4, b4, a3, b3, knot4)
                a5, b5 = move(a5, b5, a4, b4, knot5)
                a6, b6 = move(a6, b6, a5, b5, knot6)
                a7, b7 = move(a7, b7, a6, b6, knot7)
                a8, b8 = move(a8, b8, a7, b7, knot8)
                a9, b9 = move(a9, b9, a8, b8, tail)
        else:
            for i in range(steps):
                b0 -= 1
                head.append((a0, b0))
                a1, b1 = move(a1, b1, a0, b0, knot1)
                a2, b2 = move(a2, b2, a1, b1, knot2)
                a3, b3 = move(a3, b3, a2, b2, knot3)
                a4, b4 = move(a4, b4, a3, b3, knot4)
                a5, b5 = move(a5, b5, a4, b4, knot5)
                a6, b6 = move(a6, b6, a5, b5, knot6)
                a7, b7 = move(a7, b7, a6, b6, knot7)
                a8, b8 = move(a8, b8, a7, b7, knot8)
                a9, b9 = move(a9, b9, a8, b8, tail)
print(head)
print(knot1)
print(knot2)
print(knot3)
print(knot4)
print(knot5)
print(knot6)
print(knot7)
print(knot8)
print(tail)
print("Part 1:", len(set(knot1)))
print("Part 2:", len(set(tail)))

