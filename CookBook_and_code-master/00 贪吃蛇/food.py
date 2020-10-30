import random
import threading
import time


class Food(threading.Thread):
    def __init__(self,canvas, q_instance):
        threading.Thread.__init__(self)

        self.pos = (40, 40)
        self.canvas = canvas
        self.ate = False
        self.q_instance = q_instance
        self.died = False

    def run(self):
        self.draw_food()
        while True:
            if self.ate:
                self.delete_food()
                self.update_food()
                self.draw_food()
                self.ate = False
            if self.died:
                break

            time.sleep(0.1)

    def update_food(self):
        self.pos = (random.randint(1, 320/10)*10, random.randint(1, 240/10)*10)

    def draw_food(self):
        self.canvas.create_rectangle(self.pos[0]-5, self.pos[1]-5, self.pos[0]+5, self.pos[1]+5,
                                     outline=None, fill='orange', tag='food')

    def delete_food(self):
        self.canvas.delete('food')



