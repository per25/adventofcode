
global grid
grid = [[False for _ in range(500)] for _ in range(500)]
global h_x_position
h_x_position = 0
global h_y_position
h_y_position = 0
global t_x_position
t_x_position = 0
global t_y_position
t_y_position = 0
global last_x
last_x = 0
global last_y
last_y = 0


def move_tail():
    global h_x_position
    global h_y_position
    global t_x_position
    global t_y_position
    global last_x
    global last_y
    if h_x_position - t_x_position > 1:
        t_x_position = last_x
        t_y_position = last_y
    if h_x_position - t_x_position < -1:
        t_x_position = last_x
        t_y_position = last_y
    if h_y_position - t_y_position > 1:
        t_y_position = last_y
        t_x_position = last_x
    if h_y_position - t_y_position < -1:
        t_y_position = last_y
        t_x_position = last_x 
    grid[t_x_position + 100][t_y_position + 100] = True

def set_last():
    global h_x_position
    global h_y_position
    global last_x
    global last_y
    last_x = h_x_position
    last_y = h_y_position


def move_head(d, num_mov ):
    global h_x_position
    global h_y_position
    global last_x
    global last_y

    for _ in range(num_mov):
        set_last()
        if d == "R":
            h_x_position += 1
            move_tail()
        elif d == "L":
            h_x_position -= 1
            move_tail()
        elif d == "U":
            h_y_position += 1
            move_tail()
        elif d == "D": 
            h_y_position -= 1

            move_tail()


def main():
    global grid

    with open("day 9\data.txt") as file:
        lines = file.readlines()

    for line in lines:
        line = line.replace("\n", "")
        if line.startswith("R"):
            move_head("R", int(line[2:]))
        elif line.startswith("L"):
            move_head("L", int(line[2:]))
        elif line.startswith("U"):
            move_head("U", int(line[2:]))
        elif line.startswith("D"):
            move_head("D", int(line[2:]))

    num_true = lambda grid: sum(map(lambda row: sum(row), grid))

    print(num_true(grid))


main()
