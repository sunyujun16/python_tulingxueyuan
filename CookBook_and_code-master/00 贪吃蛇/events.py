"""
事实上, 这整个模块都完全可以没有...淦!
"""
import threading
import time
import queue



class Events(threading.Thread):
    def __init__(self, q_instance, snake, food, canvas):
        threading.Thread.__init__(self)
        self.q_instance = q_instance
        self.snake = snake
        self.food = food
        self.canvas = canvas
        self.restart = False

    def run(self):
        self.queue_handler()

    def queue_handler(self):
        while True:

            # died
            if not len(self.snake.pos) == len(set(self.snake.pos))\
            or not self.snake_in_board():
                self.snake_died()
                break

            # ate
            if self.food.pos in self.snake.pos:
                self.food_ate()

            time.sleep(0.01)

    def food_ate(self):
        self.food.ate = True
        self.snake.ate = True

    def snake_died(self):
        self.canvas.create_text(150, 110, text='我草, 真特么菜', tag='hint')
        self.snake.died = True
        self.food.died = True

    def snake_in_board(self):
        k,v = self.snake.pos[-1]
        if k < 0 or k > 320 or v<0 or v>240:
            return False
        else:
            return True
