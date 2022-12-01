
with open("data.txt") as file:
    lines = file.readlines()

d = {}
sum = 0
counter = 1

for line in lines:
    if (len(line) > 1):
        sum += int(line)
    else: 
        d[counter] = sum
        counter += 1
        sum = 0

three_largest = {}
sum = 0
for i in range(3):
    sum += d[max(d, key=d.get)]
    three_largest[max(d, key=d.get)] = d[max(d, key=d.get)]
    d.pop(max(d, key=d.get))

print(three_largest)
print("The sum is: " + str(sum))