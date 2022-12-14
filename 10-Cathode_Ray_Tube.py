with open("CPU_input-test2.txt", "r") as file:
    cpu_input = file.read().splitlines()
print(cpu_input)


counter = 0
crt = []
row = 0
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
    if counter in range(x - 1, x + 1):
        crt.insert(counter, "#")
    else:
        crt.insert(counter, ".")
    counter += 1
print("Part 1:", signal)
print("Part 2:")
print(crt)
