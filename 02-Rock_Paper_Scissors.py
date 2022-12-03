with open("Rock_Paper_Scissors.txt", "r") as file:
    my_list = file.read().replace(' ', "").splitlines()

cde = ['AX', 'AY', 'AZ', 'BX', 'BY', 'BZ', 'CX', 'CY', 'CZ']
lst = []

for i in cde:
    cnt = my_list.count(i)
    lst.append(cnt)

# Part 1
rps1 = [1, 2, 3, 1, 2, 3, 1, 2, 3]
ldw1 = [3, 6, 0, 0, 3, 6, 6, 0, 3]
vals1 = []

for x1, a1, b1 in zip(lst, rps1, ldw1):
    vals1.append(x1 * (a1 + b1))

print("Part 1:", sum(vals1))

# Part 2
ldw2 = [0, 3, 6, 0, 3, 6, 0, 3, 6]
rps2 = [3, 1, 2, 1, 2, 3, 2, 3, 1]
vals2 = []

for x2, a2, b2 in zip(lst, rps2, ldw2):
    vals2.append(x2 * (a2 + b2))

print("Part 2:", sum(vals2))

file.close()