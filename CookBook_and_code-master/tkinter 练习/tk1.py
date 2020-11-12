# 随即生成一个名字

import tkinter
import random

root = tkinter.Tk()
canvas = tkinter.Canvas(root, width=400, height=800)
canvas.pack()


name = random.choice(r'[u4e00-u9fa5]')
# name = random.choice(r'[u4e00-u9fa5]')


def button():
    canvas.create_text(200, 400, anchor=tkinter.CENTER, text=name, font=60)

