with open("day 7\\data.txt") as file:
    lines = file.readlines()

all_dirs = {"root":0}

for line in lines:

    if line == "$ cd /\n":
        current_path = ["root"]

    elif line.startswith("$ cd .."):
        current_path.pop()

    elif line.startswith("$ cd"):
        current_path.append(current_path[-1] + ":" + line.split(" ")[2])
        all_dirs.update({current_path[-1]: 0})

    elif line[0].isdigit():
        for dir in current_path:
            all_dirs[dir] += int(line.split(" ")[0])


total = 0
for key, value in all_dirs.items(): 
    if value <= 100000:
        total += value

print("part 1: " + str(total))

valid_dirs = []
for key, value in all_dirs.items(): 
    if all_dirs["root"] - value <= 40_000_000:
        valid_dirs.append(value)

print("part 2: " + str(min(valid_dirs)))
