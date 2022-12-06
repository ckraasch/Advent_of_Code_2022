import copy

with open("Starting_Stacks+Rearrangement_Procedure.txt", "r") as file:
    starting_stacks__rearr_procedure = file.read().splitlines()
    file.close()

starting_stacks = starting_stacks__rearr_procedure[:9]
rearrangement_procedure = starting_stacks__rearr_procedure[10:]

row1 = starting_stacks[0]
row2 = starting_stacks[1]
row3 = starting_stacks[2]
row4 = starting_stacks[3]
row5 = starting_stacks[4]
row6 = starting_stacks[5]
row7 = starting_stacks[6]
row8 = starting_stacks[7]

letter_position = (1, 5, 9, 13, 17, 21, 25, 29, 33)
all_stacks1 = []
n = 0

# rearranging the elements by stacks (each list is a stack from first(top) to last (bottom))
for stack1 in zip(row1, row2, row3, row4, row5, row6, row7, row8):
    stack1 = list(stack1)
    if n in letter_position:
           all_stacks1.append(stack1)
    n += 1


compact_stacks = []

# removing empty spaces at the front of the lists
for list1 in all_stacks1:
    stack2 = []
    m = 0
    for x in list1:
        if x != " ":
            stack2.append(x)
        m += 1
        if m == len(list1):
            compact_stacks.append(stack2)

no_whitespaces = []
all_instructions = []

# removing everything but the numbers in the instructions and making them integers
for element in rearrangement_procedure:
    only_numbers = []
    no_whitespaces = element.split(" ")
    for f in range(1, len(no_whitespaces), 2):
        d = int(no_whitespaces[f])
        only_numbers.append(d)
    all_instructions.append(only_numbers)

# Part 1
copy1_stacks = copy.deepcopy(compact_stacks)
top_boxes1 = ""

for item1 in all_instructions:
    how_many1 = item1[0]
    from_stack1 = copy1_stacks[item1[1]-1]
    to_stack1 = copy1_stacks[item1[2]-1]
    for x1 in range(how_many1):
        box = from_stack1[0]
        to_stack1.insert(0, box)
        from_stack1 = from_stack1[1:]
        copy1_stacks[item1[1]-1] = from_stack1
        copy1_stacks[item1[2]-1] = to_stack1

for first_item1 in copy1_stacks:
    top_boxes1 += first_item1[0]

print("Part 1:", top_boxes1)

# Part 2
copy2_stacks = copy.deepcopy(compact_stacks)
top_boxes2 = ""

for item2 in all_instructions:
    how_many2 = item2[0]
    from_stack2 = copy2_stacks[item2[1]-1]
    to_stack2 = copy2_stacks[item2[2]-1]
    for x2 in range(how_many2):
        boxes = from_stack2[0:how_many2]
        to_stack2 = boxes + to_stack2
        from_stack2 = from_stack2[how_many2:]
        copy2_stacks[item2[1]-1] = from_stack2
        copy2_stacks[item2[2]-1] = to_stack2
        break

for first_item2 in copy2_stacks:
    top_boxes2 += first_item2[0]

print("Part 2:", top_boxes2)



