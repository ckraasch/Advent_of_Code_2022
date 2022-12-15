with open("test1.txt", "r") as file:
    monkey_notes = file.read().replace(" ", "").replace(":", "").replace("Monkey", "").replace("Startingitems", "").replace("Operationnew=old", "").replace("Testdivisibleby", "").replace("Iftruethrowtomonkey", "").replace("Iffalsethrowtomonkey", "").splitlines()
monkey_notes.append("")
print(monkey_notes)

"""
maxi = 0
tf, starting_items, operation, test, to_monkey = [], [], [], [], []
for note in monkey_notes:
    a = note.find(":")
    items = []
    if note:
        if note[0] == "M":
            monkey = int(note[6:len(note)-1])
            if maxi < monkey:
                maxi = monkey
        if note[0] == "S":
            items = note[a+1:].split(",")
            items = [int(i) for i in items]
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


new_worry, monkey = 0, 0
inspections = [0]*(maxi + 1)
for n in range(20): # range(10000)
    for items in starting_items:
        monkeys = starting_items.index(items)
        for m in range(len(items)):
            inspections[monkeys] += 1
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
            worry = new_worry//3 # worry = new_worry
            if worry % test[monkeys] == 0:
                starting_items[to_monkey[monkeys][1]].append(worry)
            else:
                starting_items[to_monkey[monkeys][0]].append(worry)
        starting_items[monkeys] = []
sorted_monkeys = sorted(inspections, reverse=True)
monkey_business = sorted_monkeys[0]*sorted_monkeys[1]
print("Part 1:", monkey_business)
"""