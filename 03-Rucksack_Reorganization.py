import string

with open("Rucksack_Contents.txt", "r") as file:
    my_list = file.read().splitlines()

ltrs = list(string.ascii_letters)

# Part 1
lst1 = []

for x1 in my_list:
    for i1 in x1[:len(x1)//2]:
        if i1 in x1[len(x1)//2:]:
            lst1.append(ltrs.index(i1)+1)
            break

print("Part 1:", sum(lst1))

# Part 2
lst2 = []
sublst2 = []
n = 0

for x2 in my_list:
    sublst2.append(x2)
    if n == 2:
        for i2 in sublst2[0]:
            if i2 in sublst2[1] and i2 in sublst2[2]:
                lst2.append(ltrs.index(i2)+1)
                break
        n = 0
        sublst2 = []
    else:
        n = n + 1

print("Part 2:", sum(lst2))

