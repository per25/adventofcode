with open("day 7\\data.txt") as file:
    lines = file.readlines()

all_dirs = [{},{}]
current_path = ["root"]
current_depth = 1
current_sum = 0
sub_sum = 0
current_dir = "root"

all_dirs[0].update({"root":0})

counter = 1

for i in range(5):
    lines.append("$ cd ..")

lines.pop(0)

for line in lines:
    line = line.replace("\n", "")

    if counter == 163:
        print("!")

    if line == "$ ls":
        pass
    
    elif line == "$ cd ..":
        current_path.pop(current_depth - 1)
        current_depth -= 1
        current_dir = current_path[len(current_path)- 1]

    elif line.startswith("dir"):
        all_dirs[current_depth].update({line.split(" ")[1]: 0})

    elif line.startswith("$ cd"):
        current_dir = line.split(" ")[2]
        current_depth += 1
        current_path.append(current_dir)
        if current_depth == len(all_dirs):
            all_dirs.append({})

    elif line[0].isdigit():
        c = 0
        for d in current_path:
            all_dirs[c][d] += int(line.split(" ")[0])
            c += 1

    counter += 1

print(counter)
counter = 0
total = 0
for i in all_dirs:
    for key, value in i.items(): 
        if value <= 100000:
            total += value
            counter += 1

print(total)
print(counter)
