with open('Section_IDs.txt', 'r') as file:
    all_sections = file.read().replace(",", "\n").replace("-", "\n").splitlines()   # Can I combine the two replace functions?
    file.close()

pairs = len(all_sections)//4
counter1 = 0
counter2 = 0

for each_pair in range(pairs):
    n = int(each_pair)*4
# Just to make the following more readable:
    start1 = int(all_sections[n])
    end1 = int(all_sections[n + 1])
    start2 = int(all_sections[n + 2])
    end2 = int(all_sections[n + 3])
# Part 1
    if (start1 <= start2 and end1 >= end2) or (start1 >= start2 and end1 <= end2):
        counter1 += 1
# Part 2
    if not(start2 > end1 or start1 > end2):
        counter2 += 1

print("Part 1:", counter1)
print("Part 2:", counter2)


