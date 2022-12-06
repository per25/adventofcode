with open("day 6\\data.txt") as file:
    lines = file.readlines()

buffer = ""
ans = 1
found = False
for next in lines[0]:
    found = True
    buffer += next
    for i in range(len(buffer)):
        for j in range(len(buffer)):
            if i == j:
                continue
            if buffer[i] == buffer[j]:
                found = False
    if found and len(buffer) == 14:
        break
    if len(buffer) == 14:
        buffer = buffer[1:14]

    ans += 1
print(ans)