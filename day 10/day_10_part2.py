with open("day 10\\data.txt") as file:
    lines = file.readlines()

sprite = 1
clock = 0
current_row = 0
crt_pixels = [[" " for _ in range(40)] for _ in range(6)]

for instruction in lines:
    if not instruction.startswith("noop"):
        if sprite - 1 == clock or sprite == clock or sprite + 1 == clock:
            crt_pixels[current_row][clock] = "#"
        clock += 1

        if clock == 40:
            clock = 0        
            current_row += 1
            

        if sprite - 1 == clock or sprite == clock or sprite + 1 == clock:
            crt_pixels[current_row][clock] = "#"
        clock += 1

        if clock == 40:
            clock = 0        
            current_row += 1


        sprite += int(instruction[5:])
    else:
        if sprite - 1 == clock or sprite == clock or sprite + 1 == clock:
            crt_pixels[current_row][clock] = "#"
        clock += 1

        if clock == 40:
            clock = 0        
            current_row += 1
      
for row in crt_pixels:
    for pixel in row:
        print(pixel, end="")
    print()
