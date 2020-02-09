# -*- config: utf8 -*-
from tkinter import *
from time import *
from random import *

def DrawSnake(table_x,table_y,n):
    i=0
    while i < n:
        DrawCircle(table_x[i], table_y[i], r, "#baa02d")
        i+=1

def DrawCircle(x,y,r,col):
    c.create_oval(x-r,y-r,x+r,y+r,fil=col)

def draw_rec():
    c.create_rectangle(0, 0, w, h, fil="#94002d")
    c.create_rectangle(r, r, w - r, h - r, fil="#218359")

def draw_bonus():
    DrawCircle(xb, yb, r, "red")

def turn_snake(event):
    global dx, dy
    if event.keycode == 37 and dx != 1:
        dx = -1
        dy = 0
    elif event.keycode == 39 and dx != -1:
        dx = 1
        dy = 0
    elif event.keycode == 38 and dy != 1:
        dx = 0
        dy = -1
    elif event.keycode == 40 and dy != -1:
        dx = 0
        dy = 1

def gamover():
    Label(c, text="Game, как говорится, Over!!!", font=("Times New Roman",36,"bold"),\
          justify=CENTER, bg="red").place(x=0,y=0)


def draw_count():
    Label(c, text=count, font=("Times New Roman",20,"bold")).place(x=w-100, y=0)

def move_snake():
    global xb, yb, n, count
    if (table_x[0] == xb) and (table_y[0] == yb):
        xb, yb = randrange(d, w-d, d), randrange(d, h-d, d)
        n += 1
        count += 1
    else:
        table_x.pop()
        table_y.pop()
    table_x.insert(0, table_x[0]+dx*d)
    table_y.insert(0, table_y[0]+dy*d)
    c.delete("all")
    draw_rec()
    draw_bonus()
    draw_count()
    DrawSnake(table_x,table_y,n)
    c.update()

h = 500
w = 1000
r = 25
d = r*2
t = 0.3
dx = -1
dy = 0
xb = 100
yb = 100
count = 0

root = Tk()
root.title("Змейка")
root.bind("<Right>", turn_snake)
root.bind("<Left>", turn_snake)
root.bind("<Up>", turn_snake)
root.bind("<Down>", turn_snake)
c = Canvas(root, width=w, height=h)
c.pack()

draw_rec()
# drawing
table_x = [0]*4
table_y = [100]*4
i = 0
n = len(table_x)
while i < n:
    table_x[i] = d*i + w-300
    i += 1
DrawSnake(table_x,table_y,n)
flag = False
while True:
    if (table_x[0] == d) and (dx == -1):
        gamover()
        break
    else:
        if (table_x[0] == w-d) and (dx == 1):
            gamover()
            break
        else:
            if (table_y[0] == d) and (dy == -1):
                gamover()
                break
            else:
                if (table_y[0] == h-d) and (dy == 1):
                    gamover()
                    break
    for i in range(1, len(table_x)):
        if (table_x[0] == table_x[i]) and (table_y[0] == table_y[i]):
            flag = True
            break
    if flag:
        gamover()
        break
    move_snake()
    sleep(t)
root.mainloop()
