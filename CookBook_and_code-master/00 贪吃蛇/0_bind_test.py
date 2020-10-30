
from tkinter import *


def movetriangle(event):
    if event.keysym == 'Up':
        canvas.move(a1,0,-3)
    elif event.keysym == 'Down':
        canvas.move(a1,0,3)
    elif event.keysym == 'Left':
        canvas.move(a1,-3,0)
    elif event.keysym == 'Right':
        canvas.move(a1,3,0)

tk = Tk()
canvas = Canvas(tk,width=400,height=400)
a1 = canvas.create_polygon(10,10,10,60,50,35)
canvas.bind_all('<KeyPress-Up>',movetriangle)
canvas.bind_all('<KeyPress-Down>',movetriangle)
canvas.bind_all('<KeyPress-Left>',movetriangle)
canvas.bind_all('<KeyPress-Right>',movetriangle)
canvas.pack()

mainloop()

import tkinter
#
#
# class Fuck():
#     def __init__(self):
#         self.root = tkinter.Tk()
#
#         self.canvas = tkinter.Canvas(self.root, width=1000, height=600, bg='blue')
#
#         self.canvas.bind('<KeyPress>', self.func1)
#         self.canvas.pack()
#
#         tkinter.mainloop()
#
#     def func1(self, event):
#         print('啥鸡巴玩应')
#         print(event)
#
# fuck = Fuck()

