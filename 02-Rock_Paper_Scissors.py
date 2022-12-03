with open("Rock_Paper_Scissors.txt", "r") as file:
    my_list = file.read().replace(' ', "").splitlines()

cde = ['AX', 'AY', 'AZ', 'BX', 'BY', 'BZ', 'CX', 'CY', 'CZ']
# Part 1
# rps = [1, 2, 3, 1, 2, 3, 1, 2, 3]
# ldw = [3, 6, 0, 0, 3, 6, 6, 0, 3]
# Part 2
ldw = [0, 3, 6, 0, 3, 6, 0, 3, 6]
rps = [3, 1, 2, 1, 2, 3, 2, 3, 1]
lst = []
vals = []

for i in cde:
    cnt = my_list.count(i)
    lst.append(cnt)

for x, a, b in zip(lst, rps, ldw):
    vals.append(x * (a + b))

print(sum(vals))

