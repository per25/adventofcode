
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

print(d)
print("Elf number " + str(max(d, key=d.get)) + " with " + str(d[max(d, key=d.get)]) + " calories")
