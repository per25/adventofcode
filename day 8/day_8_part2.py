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
            if (colum - i >= 0 and not tree_left and grid[row][colum -i] >= current_tree_hight) or (colum - i == 0 and not tree_left):
                tree_left = True
                current_score *= i
            # right
            if (colum + i <= 98 and not tree_right and grid[row][colum + i] >= current_tree_hight) or (colum + i == 98 and not tree_right):
                tree_right = True
                current_score *= i
            # top
            if (row - i >= 0 and not tree_top and grid[row - i][colum] >= current_tree_hight) or (row - i == 0 and not tree_top):
                tree_top = True
                current_score *= i
            # bottom
            if (row + i <= 98 and not tree_bottom and grid[row + i][colum] >= current_tree_hight) or (row + i == 98 and not tree_bottom):
               tree_bottom = True
               current_score *= i

        scenic_score.append(current_score)
print(max(scenic_score))
            