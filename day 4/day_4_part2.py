with open("day 4\\data.txt") as file:
    lines = file.readlines()
sum = 0
for line in lines:
    first, second = line.split(",")
    first_start, first_end = first.split("-")
    second_start, second_end = second.split("-")
    if int(first_start) <= int(second_start) and int(first_end) >= int(second_start): sum+= 1
    elif int(first_start) <= int(second_end) and int(first_end) >= int(second_end): sum+= 1
    elif int(second_start) <= int(first_start) and int(second_end) >= int(first_start): sum+= 1
    elif int(second_start) <= int(first_end) and int(second_end) >= int(first_end): sum+= 1
print(sum)