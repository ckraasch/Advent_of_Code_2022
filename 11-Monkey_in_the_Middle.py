with open("test1.txt", "r") as file:
    monkey_notes = file.read().replace(" ", "").splitlines()

notes = []
for note in monkey_notes:
    if note:
        notes.append(note)
print(notes)

monkey = 0
for note in notes:
    a = note.find(":")
    if note[0] == "M":
        monkey = int(note[6])
        print(monkey)
    if note[0] == "S":
        item = note[a+1:].split(",")
        for i in item:
            old_worry = int(i)
            if notes[notes.index(note)+1][18:] == "old":
                value = int(old_worry)
            else:
                value = int(notes[notes.index(note)+1][18:])
            if notes[notes.index(note) + 1][17] == "*":
                new_worry = old_worry * value
            if notes[notes.index(note) + 1][17] == "/":
                new_worry = old_worry / value
            if notes[notes.index(note) + 1][17] == "+":
                new_worry = old_worry + value
            if notes[notes.index(note) + 1][17] == "-":
                new_worry = old_worry - value
            worry = new_worry//3
            print(new_worry, worry)