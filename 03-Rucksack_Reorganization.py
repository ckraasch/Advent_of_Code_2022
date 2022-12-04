import string

with open("Rucksack_Contents.txt", "r") as file:
    all_contents = file.readlines()

letters_list = list(string.ascii_letters)

# Part 1
duplicate_per_elf = []

for content_per_elf1 in all_contents:
    for item1 in content_per_elf1[:len(content_per_elf1)//2]:
        if item1 in content_per_elf1[len(content_per_elf1)//2:]:
            duplicate_per_elf.append(letters_list.index(item1)+1)
            break

print("Part 1:", sum(duplicate_per_elf))

# Part 2
total_duplicates = []
duplicate_per_group = []
n = 0

for content_per_elf2 in all_contents:
    duplicate_per_group.append(content_per_elf2)
    if n == 2:
        for item2 in duplicate_per_group[0]:
            if item2 in duplicate_per_group[1] and item2 in duplicate_per_group[2]:
                total_duplicates.append(letters_list.index(item2)+1)
                break
        n = 0
        duplicate_per_group = []
    else:
        n = n + 1

print("Part 2:", sum(total_duplicates))

file.close()
