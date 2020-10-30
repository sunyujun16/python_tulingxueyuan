import tkinter
# from snake import Snake
from food import Food


class World():

    def __init__(self):
        self.root = tkinter.Tk()
        self.root.wm_title('军仔贪吃蛇')
        self.width = 320
        self.height = 240
        self.color = 'white'
        self.canvas = tkinter.Canvas(self.root, width=self.width, height=self.height, bg=self.color)
        self.canvas.pack()



