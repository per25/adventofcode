with open("day 8\\data.txt") as file:
    lines = file.readlines()

grid = []
t = []
for i in lines: 
    for j in i:
        if j == "\\n":
            continue 
        t.append(j)
    grid.append(t)
    t = []

for row in t:
    grid.append(row)

visible_trees = 0
scenic_score = []

for row in range(1, len(grid) - 1):
    for colum in range(1, 98):
        tree_left = False
        tree_right = False
        tree_top = False
        tree_bottom = False
        current_tree_hight = grid[row][colum]
        current_score = 1
        for i in range(1,99):
            # left 
            if colum - i  >= 0 and not tree_left and grid[row][colum -i] >= current_tree_hight:
                tree_left = True
            # right
            if colum + i <= 98 and not tree_right and grid[row][colum + i] >= current_tree_hight:
                tree_right = True
            # top
            if row - i >= 0 and not tree_top and grid[row - i][colum] >= current_tree_hight:
                tree_top = True
            # bottom
            if row + i <= 98 and not tree_bottom and grid[row + i][colum] >= current_tree_hight:
               tree_bottom = True

        if tree_left and tree_right and tree_top and tree_bottom:
            visible_trees += 1

print(99*99 - visible_trees)
            