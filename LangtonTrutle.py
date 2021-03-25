import turtle

W = 1280
H = 640
WHITE = 0
BLACK = 1

NORTH = 0
EAST = 1
SOUTH = 2
WEST = 3
curr_dir = EAST

grid = [[WHITE] * W for _ in range(H)]
x = W // 2
y = H // 2

t = turtle.Turtle()
turtle.title("Langton's Turtle")
t.shape('turtle')
t.pensize(10)
t.color('black', 'green')
t.speed(10)

scr = t.getscreen()
print(f'scr.window_width() {scr.window_width()}')
print(f'scr.window_height() {scr.window_height()}')
print(f'scr.canvwidth {scr.canvwidth}')
print(f'scr.canvheight {scr.canvheight}')

# t.forward(640)
# t.right(90)
# t.forward(320)
# t.right(90)
# t.forward(1280)
# t.right(90)
# t.forward(640)

print(len(grid[0]))
print(len(grid))
print(f'x,y {x, y}')
ctr = 0
while True:
    if grid[y][x] == WHITE:
        t.right(90)
        curr_dir = (curr_dir + 1) % 4
        t.color('black', 'green')
        t.forward(10)
        grid[y][x] = BLACK
        if curr_dir == NORTH:
            y += 1
        elif curr_dir == SOUTH:
            y -= 1
        elif curr_dir == EAST:
            x += 1
        else:
            x -= 1
    else:
        t.left(90)
        curr_dir = (curr_dir - 1) % 4
        t.color('white', 'green')
        t.forward(10)
        grid[y][x] = WHITE
        if curr_dir == NORTH:
            y += 1
        elif curr_dir == SOUTH:
            y -= 1
        elif curr_dir == EAST:
            x += 1
        else:
            x -= 1
    ctr += 1
    print(ctr)

turtle.mainloop()
