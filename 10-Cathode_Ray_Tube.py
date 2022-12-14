with open("CPU_input-test2.txt", "r") as file:
    cpu_input = file.read().splitlines()
print(cpu_input)


def cycling(cycle0, signal0, x0, n0, lst0, counter0):
    counter0 += 1
    if counter0 in range(x0-1, x0+1):
        print(counter0, x0)
        lst0[n0] += "#"
    else:
        lst0[n0] += "."
    cycle0 += 1
    if cycle0 == 20 or (cycle0 - 20) % 40 == 0:
        signal0 += (cycle0 * x0)
    if (cycle0-1) % 40 == 0:
        n0 += 1
        counter0 = 0
    return cycle0, signal0, x0, n0, counter0


counter = 0
lst = [""]*6
n = 0
signal = 0
cycle = 1
x = 1
for i in cpu_input:
    if i != "noop":
        cycle, signal, x, n, counter = cycling(cycle, signal, x, n, lst, counter)
        x += int(i[5:])
    cycle, signal, x, n, counter = cycling(cycle, signal, x, n, lst, counter)


print("Part 1:", signal)
print("Part 2:")
print(lst[0])
print(lst[1])
print(lst[2])
print(lst[3])
print(lst[4])
print(lst[5])
