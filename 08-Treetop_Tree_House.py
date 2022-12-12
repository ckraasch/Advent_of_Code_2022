with open("Tree_Grid.txt", "r") as file:
    tree_grid = file.read().splitlines()
    file.close()

grid = []
for row in tree_grid:
    grid.append(list(row))

north_view = []
east_view = []
south_view = []
west_view = []
inner_trees = []
counter_columns = 0
position = 0
for row in grid[1:len(grid)-1]:
    counter_rows = 0
    for tree in row[1:len(row)-1]:
        inner_trees.append(int(tree))
        north_view.insert(position, [n[counter_columns + 1] for n in grid[:counter_rows + 1]])
        east_view.append(row[counter_rows + 2:])
        south_view.insert(position, [s[counter_columns + 1] for s in grid[counter_rows + 2:]])
        west_view.append(row[:counter_rows + 1])
        counter_rows += 1
        position += counter_columns + 1
    counter_columns += 1
    position = counter_columns


# Part 1
max_north = [int(max(n)) for n in north_view]
max_east = [int(max(e)) for e in east_view]
max_south = [int(max(s)) for s in south_view]
max_west = [int(max(w)) for w in west_view]

visible_inner_trees = 0
for n, e, s, w, t in zip(max_north, max_east, max_south, max_west, inner_trees):
    if n < t or e < t or s < t or w < t:
        visible_inner_trees += 1
outer_trees = (len(tree_grid) + len(tree_grid[0]))*2 - 4
visible_trees = visible_inner_trees + outer_trees
print("Part 1:", visible_trees)


# Part 2
def revers(input):
    output = []
    for x in input:
        x.reverse()
        output.append(x)
    return output

north_rev = revers(north_view)
west_rev = revers(west_view)

def ic_trees(listname):
    new_list = []
    for x in listname:
        counter = 0
        for item in x:
            item = int(item)
            if item >= inner_trees[listname.index(x)] or counter == len(x):
                counter += 1
                break
            else:
                counter += 1
        new_list.append(counter)
    return new_list

north = ic_trees(north_rev)
east = ic_trees(east_view)
south = ic_trees(south_view)
west = ic_trees(west_rev)

scenic_scores = []
for n, e, s, w in zip(north, east, south, west):
    score = int(n) * int(e) * int(s) * int(w)
    scenic_scores.append(score)
print("Part 2:", max(scenic_scores))