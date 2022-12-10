with open("day 10\\data.txt") as file:
    lines = file.readlines()

register = 1
clock_cycles = 0
sum_of_cycles = 0
cycle_counter = 20


for instruction in lines:
    if not instruction.startswith("noop"):
        clock_cycles += 1
        if clock_cycles == cycle_counter:
            sum_of_cycles += register * clock_cycles
            cycle_counter += 40
        
        clock_cycles += 1
        if clock_cycles == cycle_counter:
            sum_of_cycles += register * clock_cycles
            cycle_counter += 40

        register += int(instruction[5:])
    else:
        clock_cycles += 1
        if clock_cycles == cycle_counter:
            sum_of_cycles += register * clock_cycles
            cycle_counter += 40

print(sum_of_cycles)
