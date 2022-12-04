with open("day 3\\data.txt") as file:
    lines = file.readlines()
sum = 0

for i in range(0, len(lines), 3):
    for letter in lines[i]:
        if letter in lines[i + 1] and letter in lines[i + 2]:
            sum += ord(letter) - 96 if letter.islower() else ord(letter) - 38
            break
print(sum)