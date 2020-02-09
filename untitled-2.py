# -*- coding: utf8 -*-
from tkinter import *

def toggle_eyes():
    curent_color = c.itemcget(eye_left, 'fil')
    if curent_color == 'white':
        new_color = body_color
        new_state = HIDDEN
    else:
        new_color = 'white'
        new_state = NORMAL
    c.itemconfigure(eye_left, fil=new_color)
    c.itemconfigure(eye_right, fil=new_color)
    c.itemconfigure(pupil_left, state=new_state)
    c.itemconfigure(pupil_right, state=new_state)
    root.after(500, toggle_eyes)

def toggle_hvost(event):
    curent_state = c.itemcget(hvost_normal, 'state')
    if curent_state == NORMAL:
        c.itemconfigure(hvost_normal, state=HIDDEN)
        c.itemconfigure(hvost_happy, state=NORMAL)
    else:
        c.itemconfigure(hvost_normal, state=NORMAL)
        c.itemconfigure(hvost_happy, state=HIDDEN)
    if 45 < event.x < 375 and 30 < event.y < 100:
        root.after(300, toggle_hvost)
        
def show_happy(event):
    if 45 < event.x < 375 and 30 < event.y < 100:
        c.itemconfigure(cheek_left, state=NORMAL)
        c.itemconfigure(cheek_right, state=NORMAL)
        c.itemconfigure(mouth_normal, state=HIDDEN)
        c.itemconfigure(mouth_happy, state=NORMAL)
        toggle_hvost(event)
    else:
        c.itemconfigure(cheek_left, state=HIDDEN)
        c.itemconfigure(cheek_right, state=HIDDEN)
        c.itemconfigure(mouth_normal, state=NORMAL)
        c.itemconfigure(mouth_happy, state=HIDDEN)
        
    
root = Tk()
root.title("Чучундрик")
c = Canvas(root, width = 400, height = 400)
c.configure(bg = "mediumspringgreen", highlightthickness = 10)
body_color = "magenta"

body = c.create_oval(45, 30, 375, 360, outline=body_color, fil=body_color)

ear_left=c.create_polygon(85,85,75,10,165,70,outline=body_color, fil=body_color)
ear_right=c.create_polygon(265,55,335,10,330,80,outline=body_color,\
                           fil=body_color)
mouth_normal=c.create_line(170,260,215,282,260,260, width=7, smooth=1,\
                           fil="blue")
hvost_normal=c.create_line(335,300,385,260,400,140, width=7, smooth=1,\
                           fil=body_color)
hvost_happy=c.create_line(335,300,390,260,380,140, width=7, smooth=1,\
                           fil=body_color, state=HIDDEN)
mouth_happy=c.create_line(170,240,215,292,260,240, width=7, smooth=1,\
                          fil="blue", state=HIDDEN)
foot_left = c.create_oval(75, 340, 165, 380, outline=body_color, fil=body_color)
foot_right = c.create_oval(255, 340, 345, 380, outline=body_color, fil=body_color)
eye_left = c.create_oval(130, 110, 160, 170, outline="black", fil="white")
eye_right = c.create_oval(260, 110, 290, 170, outline="black", fil="white")
pupil_left = c.create_oval(140, 140, 150, 160, outline="black", fil="black")
pupil_right = c.create_oval(270, 140, 280, 160, outline="black", fil="black")
cheek_left = c.create_oval(75, 190, 125, 240, outline="pink", fil="pink",\
                           state=HIDDEN)
cheek_right = c.create_oval(298, 190, 348, 240, outline="pink", fil="pink",\
                            state=HIDDEN)

c.pack()

toggle_eyes()
c.bind('<Motion>', show_happy)
root.mainloop()
