with open("day 3\\data.txt") as file:
    lines = file.readlines()
sum = 0
for line in lines:
    first_half = line[0:int(len(line)/ 2)]
    second_half = line[int(len(line)/ 2):].replace("\n", "")
    for letter in first_half:
        if letter in second_half:
            sum += ord(letter) - 96 if letter.islower() else ord(letter) - 38
            break
print(sum)