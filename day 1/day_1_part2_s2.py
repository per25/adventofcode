with open("data.txt") as file:
    lines = file.readlines()
s = 0
largest = [0,0,0] 
for line in lines:
    if len(line) > 1:
        s += int(line)
    else:
        for i in range(3):
            if (s > largest[i]):
                largest[i] = s
                break
        s = 0
print("The sum of the three largest:" + str(sum(largest)))