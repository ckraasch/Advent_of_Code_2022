with open("Motion_Series_test.txt", "r") as file:
    motion_series = file.read().splitlines()
print(motion_series)


tail_position = [[0, 0]]
head = [0, 0]
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
    while head[0]-tail[0] not in [-1, 0, 1] or head[1]-tail[1] not in [-1, 0, 1]:
        tail_position.append(tail)
        if head[0] > tail[0]:
            tail[0] += 1
        if head[0] < tail[0]:
            tail[0] -= 1
        if head[1] > tail[1]:
            tail[1] += 1
        if head[1] < tail[1]:
            tail[1] -= 1
        tail = [tail[0], tail[1]]


temp = []
[temp.append(x) for x in tail_position if x not in temp]
print(len(temp))