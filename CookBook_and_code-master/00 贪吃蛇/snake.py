import threading
import time


class Snake(threading.Thread):
    def __init__(self, canvas, q_instance):
        threading.Thread.__init__(self)
        self.canvas = canvas
        self.pos = [(10, 10), (10, 20), (10, 30), (10, 40), (10, 50)]
        self.width = 10
        self.direction = 'Right'
        self.ate = False
        self.q_instance = q_instance
        self.died = False
        self.point = 0
        self.canvas.create_text(5, 5, text=str(self.point), tag='point')
        # 绑定按键
        self.canvas.bind_all('<KeyPress-Left>', self.change_direction)
        self.canvas.bind_all('<KeyPress-Right>', self.change_direction)
        self.canvas.bind_all('<KeyPress-Up>', self.change_direction)
        self.canvas.bind_all('<KeyPress-Down>', self.change_direction)

    def run(self):
        self.draw_snake()
        while True:
            if self.died:
                break
            self.canvas.delete('snake')
            self.update_snake_pos()
            self.draw_snake()

            time.sleep(0.3)

    def update_snake_pos(self):

        if not self.ate:
            if self.direction == 'Up':
                self.add = (self.pos[-1][0], self.pos[-1][1]-10)
                self.pos.append(self.add)
                self.pos.pop(0)
            if self.direction == 'Down':
                self.add = (self.pos[-1][0], self.pos[-1][1]+10)
                self.pos.append(self.add)
                self.pos.pop(0)
            if self.direction == 'Right':
                self.add = (self.pos[-1][0]+10, self.pos[-1][1])
                self.pos.append(self.add)
                self.pos.pop(0)
            if self.direction == 'Left':
                self.add = (self.pos[-1][0]-10, self.pos[-1][1])
                self.pos.append(self.add)
                self.pos.pop(0)

        if self.ate:
            if self.direction == 'Up':
                self.add = (self.pos[-1][0], self.pos[-1][1]-10)
                self.pos.append(self.add)
            if self.direction == 'Down':
                self.add = (self.pos[-1][0], self.pos[-1][1]+10)
                self.pos.append(self.add)
            if self.direction == 'Right':
                self.add = (self.pos[-1][0]+10, self.pos[-1][1])
                self.pos.append(self.add)
            if self.direction == 'Left':
                self.add = (self.pos[-1][0]-10, self.pos[-1][1])
                self.pos.append(self.add)
            self.point += 1
            self.canvas.delete('point')
            self.canvas.create_text(10,10, text=str(self.point), tag='point')

        self.ate = False

    def draw_snake(self):
        self.canvas.create_line(*self.pos, fill='orange', width=self.width, tag='snake')

    def change_direction(self, event):
        if event.keysym == 'Left':
            self.direction = 'Left'
        if event.keysym == 'Right':
            self.direction = 'Right'
        if event.keysym == 'Up':
            self.direction = 'Up'
        if event.keysym == 'Down':
            self.direction = 'Down'

