with open("CPU_input.txt", "r") as file:
    cpu_input = file.read().splitlines()


signal = 0
cycle = 1
x = 1
for i in cpu_input:
    if i == "noop":
        cycle += 1
        if cycle == 20 or (cycle-20) % 40 == 0:
            signal += (cycle * x)
    else:
        cycle += 1
        if cycle == 20 or (cycle-20) % 40 == 0:
            signal += (cycle * x)
        x += int(i[5:])
        cycle += 1
        if cycle == 20 or (cycle-20) % 40 == 0:
            signal += (cycle * x)
print("Part 1:", signal)

