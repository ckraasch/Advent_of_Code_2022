with open("Datastream_Buffer.txt", "r") as file:
    datastream_buffer = file.read()
    file.close()

# Part 1
last_four_chars = []
position1 = 0
counter1 = 0

for character1 in datastream_buffer:
    print(character1)
    if character1 in last_four_chars:
        if last_four_chars.index(character1) + 1 <= counter1:
            counter1 = last_four_chars.index(character1) + 1
    if len(last_four_chars) == 4:
        last_four_chars.pop(3)
    last_four_chars.insert(0, character1)
    counter1 += 1
    position1 += 1
    if counter1 == 5:
        print("Part 1:", position1)
        break

# Part 2
last_fourteen_chars = []
position2 = 0
counter2 = 0

for character2 in datastream_buffer:
    if character2 in last_fourteen_chars:
        if last_fourteen_chars.index(character2) + 1 <= counter2:
            counter2 = last_fourteen_chars.index(character2) + 1
    if len(last_fourteen_chars) == 14:
        last_fourteen_chars.pop(13)
    last_fourteen_chars.insert(0, character2)
    counter2 += 1
    position2 += 1
    if counter2 == 15:
        print("Part 2:", position2)
        break