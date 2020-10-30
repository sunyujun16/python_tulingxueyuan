import tkinter
import queue
from food import Food
from snake import Snake
from world import World
import events


def main():

    # 创建队列和世界实例
    q_instance = queue.Queue()
    world = World()

    # 创建snake和food和event实例, 并以守护线程运行
    snake = Snake(world.canvas, q_instance)
    snake.setDaemon(True)
    snake.start()

    food = Food(world.canvas, q_instance)
    food.setDaemon(True)
    food.start()

    event = events.Events(q_instance, snake, food, world.canvas)
    event.setDaemon(True)
    event.start()

    # 启动tkinter主循环
    tkinter.mainloop()


main()

