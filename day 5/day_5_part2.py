with open("day 5\\data2.txt") as file:
    lines = file.readlines()

c = [[], ["T", "F", "V", "Z", "C", "W", "S", "Q"],["B", "R", "Q"],["S", "M", "P", "Q", "T", "Z", "B"],["H", "Q", "R", "F", "V", "D"],["P", "T", "S", "B", "D", "L", "G", "J"],["Z", "T", "R", "W"],["J", "R", "F", "S", "N", "M", "Q", "H"],["W", "H", "F", "N", "R", ],["B", "R", "P", "Q", "T", "Z", "J"]]

for line in lines:
    i = line.split(" ")
    i[5] = i[5].strip("\n")
    temp = []
    for j in range(int(i[1])):
        temp.insert(0, c[int(i[3])][0])
        c[int(i[3])].pop(0)
    for j in temp:
        c[int(i[5])].insert(0, j)

for i in c:
    try:
        print(i[0], end="")
    except:
        pass