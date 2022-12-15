with open("test1.txt", "r") as file:
    monkey_notes = file.read().replace(" ", "").splitlines()
monkey_notes.append("")
print(monkey_notes)

tf = []
starting_items, operation, test, to_monkey = [], [], [], []
for note in monkey_notes:
    a = note.find(":")
    items = []
    true, false = 0, 0
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
            t = int(note[20:])
            tf.insert(0, t)
        if note[0:3] == "Iff":
            f = int(note[21:])
            tf.insert(0, f)
    if not note:
        to_monkey.insert(monkey, tf)
        tf = []
print(starting_items)
print(operation)
print(test)
print(to_monkey)

for n in range(20):
    for items in starting_items:
        monkeys = starting_items.index(items)
        for m in range(len(items)):
            old_worry = items[m]
            if operation[monkeys][1:] == "old":
                value = int(old_worry)
            else:
                value = int(operation[monkeys][1:])
            if operation[monkeys][0] == "*":
                new_worry = old_worry * value
            if operation[monkeys][0] == "/":
                new_worry = old_worry / value
            if operation[monkeys][0] == "+":
                new_worry = old_worry + value
            if operation[monkeys][0] == "-":
                new_worry = old_worry - value
            worry = new_worry//3
            if worry % test[monkeys] == 0:
                starting_items[to_monkey[monkeys][1]].append(worry)
            else:
                starting_items[to_monkey[monkeys][0]].append(worry)
                print(to_monkey[monkeys][1])
        starting_items[monkeys] = []
        print(monkeys, starting_items)
