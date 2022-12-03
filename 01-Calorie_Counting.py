with open("Counted_Calories.txt", "r") as file:
    my_list = file.read().split('\n')     # Read text file and split the string 'file' by newline to create list.

lst = []
a = 0

for x in my_list:
    if x:
        a += int(x)
    else:
        lst.append(a)
        a = 0

# Part 1
print("Part 1:", max(lst))

# Part 2
lst.sort()
print("Part 2:", sum(lst[-3:]))

file.close()