with open("data.txt") as file:
    lines = file.readlines()
largest, sum = 0, 0
for line in lines:
    if len(line) > 1:
        sum += int(line)
    else:
        largest = sum if sum > largest else largest
        sum = 0
print("The largest amount of calories is:" + str(largest))