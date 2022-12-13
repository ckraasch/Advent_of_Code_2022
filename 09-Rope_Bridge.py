with open("Motion_Series.txt", "r") as file:
    motion_series = file.read().splitlines()
print(motion_series)

knot1_position = [[0, 0]]
tail_position = [[0, 0]]
head = [0, 0]
knot1 = [0, 0]
knot2 = [0, 0]
knot3 = [0, 0]
knot4 = [0, 0]
knot5 = [0, 0]
knot6 = [0, 0]
knot7 = [0, 0]
knot8 = [0, 0]
knot9 = [0, 0]
tail = [0, 0]
down_up = 0
right_left = 0
for direction in motion_series:
    steps = int(direction[2:])
    if direction[0] == "U":
        down_up -= steps
    if direction[0] == "R":
        right_left += steps
    if direction[0] == "D":
        down_up += steps
    if direction[0] == "L":
        right_left -= steps
    head = [right_left, down_up]
    while head[0]-knot1[0] not in [-1, 0, 1] or head[1]-knot1[1] not in [-1, 0, 1]:
        knot1_position.append(knot1)
        if head[0] > knot1[0]:
            knot1[0] += 1
        if head[0] < knot1[0]:
            knot1[0] -= 1
        if head[1] > knot1[1]:
            knot1[1] += 1
        if head[1] < knot1[1]:
            knot1[1] -= 1
        knot1 = [knot1[0], knot1[1]]
    while knot1[0]-knot2[0] not in [-1, 0, 1] or knot1[1]-knot2[1] not in [-1, 0, 1]:
        if knot1[0] > knot2[0]:
            knot2[0] += 1
        if knot1[0] < knot2[0]:
            knot2[0] -= 1
        if knot1[1] > knot2[1]:
            knot2[1] += 1
        if knot1[1] < knot2[1]:
            knot2[1] -= 1
    while knot2[0]-knot3[0] not in [-1, 0, 1] or knot2[1]-knot3[1] not in [-1, 0, 1]:
        if knot2[0] > knot3[0]:
            knot3[0] += 1
        if knot2[0] < knot3[0]:
            knot3[0] -= 1
        if knot2[1] > knot3[1]:
            knot3[1] += 1
        if knot2[1] < knot3[1]:
            knot3[1] -= 1
    while knot3[0]-knot4[0] not in [-1, 0, 1] or knot3[1]-knot4[1] not in [-1, 0, 1]:
        if knot3[0] > knot4[0]:
            knot4[0] += 1
        if knot3[0] < knot4[0]:
            knot4[0] -= 1
        if knot3[1] > knot4[1]:
            knot4[1] += 1
        if knot3[1] < knot4[1]:
            knot4[1] -= 1
    while knot4[0]-knot5[0] not in [-1, 0, 1] or knot4[1]-knot5[1] not in [-1, 0, 1]:
        if knot4[0] > knot5[0]:
            knot5[0] += 1
        if knot4[0] < knot5[0]:
            knot5[0] -= 1
        if knot4[1] > knot5[1]:
            knot5[1] += 1
        if knot4[1] < knot5[1]:
            knot5[1] -= 1
    while knot5[0]-knot6[0] not in [-1, 0, 1] or knot5[1]-knot6[1] not in [-1, 0, 1]:
        if knot5[0] > knot6[0]:
            knot6[0] += 1
        if knot5[0] < knot6[0]:
            knot6[0] -= 1
        if knot5[1] > knot6[1]:
            knot6[1] += 1
        if knot5[1] < knot6[1]:
            knot6[1] -= 1
    while knot6[0]-knot7[0] not in [-1, 0, 1] or knot6[1]-knot7[1] not in [-1, 0, 1]:
        if knot6[0] > knot7[0]:
            knot7[0] += 1
        if knot6[0] < knot7[0]:
            knot7[0] -= 1
        if knot6[1] > knot7[1]:
            knot7[1] += 1
        if knot6[1] < knot7[1]:
            knot7[1] -= 1
    while knot7[0]-knot8[0] not in [-1, 0, 1] or knot7[1]-knot8[1] not in [-1, 0, 1]:
        if knot7[0] > knot8[0]:
            knot8[0] += 1
        if knot7[0] < knot8[0]:
            knot8[0] -= 1
        if knot7[1] > knot8[1]:
            knot8[1] += 1
        if knot7[1] < knot8[1]:
            knot8[1] -= 1
    while knot8[0]-tail[0] not in [-1, 0, 1] or knot8[1]-tail[1] not in [-1, 0, 1]:
        tail_position.append(tail)
        if knot8[0] > tail[0]:
            tail[0] += 1
        if knot8[0] < tail[0]:
            tail[0] -= 1
        if knot8[1] > tail[1]:
            tail[1] += 1
        if knot8[1] < tail[1]:
            tail[1] -= 1
        tail = [tail[0], tail[1]]


temp = []
temp1 = []
[temp.append(x) for x in knot1_position if x not in temp]
[temp1.append(x) for x in tail_position if x not in temp1]
print(len(temp))
print(len(temp1))
