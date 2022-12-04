
with open("day 2\\data.txt") as file:
    lines = file.readlines()

sum = 0
for i in lines:
    x = ord(i[0]) - 64
    y = ord(i[2]) - 87
    sum += y + 3 if x == y else 0
    sum += y + 6 if x - y == -1 or x - y == 2 else 0
    sum += y if not (x == y or x - y == -1 or x - y == 2 ) else 0

print("The total score is:" + str(sum))
