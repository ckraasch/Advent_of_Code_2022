with open("Counted_Calories.txt", "r") as file:
    cals_per_item = file.read().split('\n')     # Read text file and split the string 'file' by newline to create list.

cals_per_elf = []
cal_counter = 0

for item in cals_per_item:
    if item:
        cal_counter += int(item)
    else:
        cals_per_elf.append(cal_counter)
        cal_counter = 0

# Part 1
print("Part 1:", max(cals_per_elf))

# Part 2
cals_per_elf.sort()
print("Part 2:", sum(cals_per_elf[-3:]))

file.close()