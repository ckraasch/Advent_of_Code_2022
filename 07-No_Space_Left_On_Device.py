with open("System_Commands.txt", "r") as file:
    system_commands = file.read().splitlines()
    file.close()

# Part 1
directory = ""
lst = []
lst1 = []
lst2 = [0]
lst3 = [0]
x = 0
counter = 1
counter2 = 0
a = 0
tester = []

for command in system_commands:
    if command[0] != "$" and command[0:3] != "dir":
        command = command.split(" ")
        x += int(command[0])
        lst1.append(x)
        x = 0
        counter += 1
        lst2[a] = counter
        counter2 += 1
        lst3[a] = counter2
    if command[0:3] == "dir":
        tester += command[5:]
    if command[0] == "$":
        if command[2:4] == "cd":
            if command[5:] == "..":
                directory = directory[:directory.rfind("/")]
            elif command[5:] not in tester:
                if command[5:] != "/":
                    directory += "/" + command[5:]
                    tester = []
                else:
                    directory = "/"
        if command[2:4] == "ls":
            if directory not in lst:
                lst.append(directory)
                a += 1
                counter = 0
                lst2.append(0)
                lst3.append(0)

lst2 = lst2[1:]
lst3 = lst3[1:]
lst4 = []
value = 0

for x, y in zip(lst2, lst3):
    lst4.append(sum(lst1[y-x:y]))

m = 0
n = 0
values = 0
lst100 = []

for n in range(len(lst)):
    for item in lst:
        if lst[n] in item:
            m += lst4[lst.index(item)]
    lst100.append(m)
    if m <= 100000:
        values += m
    m = 0

print("Part 1:", values)

# Part 2
needed_space = 30000000
available_space = 70000000
used_space = sum(lst1)
space_to_free_up = used_space - (available_space - needed_space)
lst001 = sorted(lst100, reverse=True)

for item in lst001:
    if item >= space_to_free_up and lst001[lst001.index(item)+1] < space_to_free_up:
        print("Part 2:", item)



