with open("Motion_Series.txt", "r") as file:
    motion_series = file.read().splitlines()
print(motion_series)

head_position = [[0, 0]]
tail_position = [[0, 0]]
head = [0, 0]
tail = [0, 0]
down_up = 0
# +D-U,
right_left = 0
# +R-L
grid = [0, 0, 0, 0]
# U, R, D, L
for direction in motion_series:
    steps = int(direction[2:])
    if direction[0] == "U":
        down_up -= steps
#        if down_up < grid[0]:
#            grid[0] = down_up
    if direction[0] == "R":
        right_left += steps
#        if right_left > grid[1]:
#            grid[1] = right_left
    if direction[0] == "D":
        down_up += steps
#        if down_up > grid[2]:
#            grid[2] = down_up
    if direction[0] == "L":
        right_left -= steps
#        if right_left < grid[3]:
#            grid[3] = right_left
    head_position.append([right_left, down_up])
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
        # wieso brauche ich diese zeile??
print(head_position)
print(tail_position)

height = grid[2] - grid[0] + 1
width = grid[1] - grid[3] + 1

grid = [[0]*height]*width
print(grid)

temp = []
print(len(tail_position))

[temp.append(x) for x in tail_position if x not in temp]

print(len(temp))
