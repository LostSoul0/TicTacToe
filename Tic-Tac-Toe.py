### Imports
import pyglet
import random
import time
import os
import sys

## Constants / Variables
win = pyglet.window.Window(500, 500, caption='Tic Tac Toe')
turn = False
# True means x turn
# False means os turn

### Lines and Boxes
grid = [
    # Vertical Lines
    [100, 100, 100, 400],
    [200, 100, 200, 400],
    [300, 100, 300, 400],
    [400, 100, 400, 400],
    # Horizontal Lines
    [100, 100, 400, 100],
    [100, 200, 400, 200],
    [100, 300, 400, 300],
    [100, 400, 400, 400]
]

board = [
    [None, 110, 310], [None, 210, 310], [None, 310, 310],
    [None, 110, 210], [None, 210, 210], [None, 310, 210],
    [None, 110, 110], [None, 210, 110], [None, 310, 110]
]

boxes = [
    [100, 300, 200, 400], [200, 300, 300, 400], [300, 300, 400, 400],
    [100, 200, 200, 300], [200, 200, 300, 300], [300, 200, 400, 300],
    [100, 100, 200, 200], [200, 100, 300, 200], [300, 100, 400, 200]
]

### Fucntions
def Grid():
    win.clear()
    global grid
    batch = pyglet.graphics.Batch()
    batch_grid = []
    for line in grid:
        batch_grid.append(pyglet.shapes.Line(line[0], line[1], line[2], line[3], width=5, color=(255, 255, 255), batch=batch))
    batch.draw()

    label = pyglet.text.Label(
        "X's turn" if turn else "O's turn",
        font_size=24,
        color=(255, 0, 0, 255) if turn else (0, 0, 255, 255),
        x=win.height-120 if turn else 5,
        y = 5
    )
    label.draw()

def o_and_x():
    global board
    for entity in board:
        if entity[0] is not None:
            if entity[0] == 'x':
                x = pyglet.image.load('res/x.png')
                x.blit(entity[1], entity[2])
            elif entity[0] == 'o':
                o = pyglet.image.load('res/o.png')
                o.blit(entity[1], entity[2])

def restart(f):
    os.execl(sys.executable, sys.executable, *sys.argv)

def checkwin():
    global board
    game_over = False
    winner = None
    # Horizontal Rows
    # Top Row
    if board[0][0] == board[1][0] == board[2][0] and board[0][0] is not None: 
        game_over = True
        winner = f"{board[0][0].upper()} Wins!!!"

    # Middle Row
    elif board[3][0] == board[4][0] == board[5][0] and board[3][0] is not None:
        game_over = True
        winner = f"{board[3][0].upper()} Wins!!!"

    # Bottom Row
    elif board[6][0] == board[7][0] == board[8][0] and board[6][0] is not None:
        game_over = True
        winner = f"{board[6][0].upper()} Wins!!!"

    # Vertical Rows
    # Left Row 
    elif board[0][0] == board[3][0] == board[6][0] and board[0][0] is not None: 
        game_over = True
        winner = f"{board[0][0].upper()} Wins!!!"

    # Middle Row
    elif board[1][0] == board[4][0] == board[7][0] and board[1][0] is not None:
        game_over = True
        winner = f"{board[1][0].upper()} Wins!!!"

    # Right Row 
    elif board[2][0] == board[5][0] == board[8][0] and board[2][0] is not None:
        game_over = True
        winner = f"{board[2][0].upper()} Wins!!!"

    # Diagonal Rows
    # Top left to bottom right 
    elif board[0][0] == board[4][0] == board[8][0] and board[0][0] is not None: 
        game_over = True
        winner = f"{board[0][0].upper()} Wins!!!"

    # Top right to bottom left 
    elif board[2][0] == board[4][0] == board[6][0] and board[2][0] is not None:
        game_over = True
        winner = f"{board[2][0].upper()} Wins!!!"

    elif board[0][0] and board[1][0] and board[2][0] and board[3][0] and board[4][0] and board[5][0] and board[6][0] and board[7][0] and board[8][0]:
        game_over = True
        winner = f"It's a tie!"


    if game_over:
        label = pyglet.text.Label(
            winner,
            font_size=24,
            bold=True,
            italic=True,
            color=(66, 245, 227, 255),
            x=win.width//2,
            y=win.height//2,
            width=win.width,
            anchor_x='center',
            anchor_y='center',
            align='center',
        )
        win.clear()
        label.draw()
        music = pyglet.resource.media('res/applause.wav', streaming=False)
        music.play()
        pyglet.clock.schedule_once(restart, 3)

## Main Event
@win.event
def on_draw():
    win.clear()
    Grid()
    o_and_x()
    checkwin()


### 
@win.event
def on_mouse_press(x, y, button, modifiers):
    global boxes, turn, board
    for box in boxes:
        if x > box[0] and box[2] > x and y > box[1] and box[3] > y:
            box = boxes.index(box)
            if board[box][0] == None:
                if turn == True:
                    board[box][0] = 'x'
                    turn = False
                else:
                    board[box][0] = 'o'
                    turn = True


pyglet.app.run()