with open("test1.txt", "r") as file:
    monkey_notes = file.read().replace(" ", "").splitlines()
monkey_notes.append("")

to_monkey, starting_items, operation, test = [], [], [], []
for note in monkey_notes:
    a = note.find(":")
    items = []
    if note:
        if note[0] == "M":
            monkey = int(note[6:len(note)-1])
        if note[0] == "S":
            items = note[a+1:].split(",")
            for i in items:
                items[items.index(i)] = int(i)
            starting_items.insert(monkey, items)
        if note[0] == "O":
            operation.insert(monkey, note[17:])
        if note[0] == "T":
            test.insert(monkey, int(note[16:]))
        if note[0:3] == "Ift":
            true = int(note[20])
            false = int(monkey_notes[monkey_notes.index(note)+1][21])
            to_monkey.insert(monkey, (true, false))
print(starting_items)
print(operation)
print(test)
print(to_monkey)

for n in range(20):
    for items in starting_items:
        for m in range(len(items)):
            monkey = starting_items.index(items)
            old_worry = items[m]
            if operation[monkey][1:] == "old":
                value = int(old_worry)
            else:
                value = int(operation[monkey][1:])
            if operation[monkey][0] == "*":
                new_worry = old_worry * value
            if operation[monkey][0] == "/":
                new_worry = old_worry / value
            if operation[monkey][0] == "+":
                new_worry = old_worry + value
            if operation[monkey][0] == "-":
                new_worry = old_worry - value
            worry = new_worry//3
            print(new_worry)
