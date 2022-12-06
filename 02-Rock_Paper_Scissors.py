with open("Rock_Paper_Scissors.txt", "r") as file:
    selection_guide = file.read().replace(' ', "").splitlines()
    file.close()

all_combinations = ['AX', 'AY', 'AZ', 'BX', 'BY', 'BZ', 'CX', 'CY', 'CZ']
num_per_combination = []

for round in all_combinations:
    counter = selection_guide.count(round)
    num_per_combination.append(counter)

# Part 1
points1_selection = [1, 2, 3, 1, 2, 3, 1, 2, 3]
points1_outcome = [3, 6, 0, 0, 3, 6, 6, 0, 3]
total_points1 = 0

for round1, selection1, outcome1 in zip(num_per_combination, points1_selection, points1_outcome):
    total_points1 += (round1 * (selection1 + outcome1))

print("Part 1:", total_points1)

# Part 2
points2_outcome = [0, 3, 6, 0, 3, 6, 0, 3, 6]
points2_selection = [3, 1, 2, 1, 2, 3, 2, 3, 1]
total_points2 = 0

for round2, selection2, outcome2 in zip(num_per_combination, points2_selection, points2_outcome):
    total_points2 += (round2 * (selection2 + outcome2))

print("Part 2:", total_points2)