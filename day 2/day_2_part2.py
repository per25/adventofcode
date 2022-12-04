with open("day 2\\data.txt") as file:
    lines = file.readlines()

sum = 0
for i in lines:
    sum += ((ord(i[0])) + (ord(i[2])) - 151) % 3 + 1 + ((ord(i[2]) - 88) * 3)

print(sum)

# first solution 
# x = ord(i[0]) - 64
# y = ord(i[2]) - 87
# sum += (x + y) % 3 + 1 + ((y - 1) * 3)
    
# 1 = lose 
# 2 = draw
# 3 = win
# 
# R + 1 -> S = 3
# R + 2 -> R = 1
# R + 3 -> P = 2
# P + 1 -> 
# P + 2 -> P = 2 

# S + 3 -> R = 1 