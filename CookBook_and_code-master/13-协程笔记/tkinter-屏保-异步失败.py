'''
在这个单元中, 我试图对这个屏保程序实现异步IO的应用
'''

import tkinter
import random
import asyncio
import time


class RandomBall():

    def __init__(self, canvas, screen_width, screen_height):

        self.xpos = random.randint(10, int(screen_width) - 10)
        self.ypos = random.randint(10, int(screen_height) - 10)

        self.xvelocity = random.randint(4, 20)
        self.yvelocity = random.randint(4, 20)

        self.screenwidth = screen_width
        self.screenheight = screen_height

        self.radius = random.randint(20, 100)

        if self.xpos + self.radius >= self.screenwidth:
            self.xpos = self.screenwidth - self.radius
        if self.xpos - self.radius <= 0:
            self.xpos = self.radius
        if self.ypos + self.radius >= self.screenheight:
            self.ypos = self.screenheight - self.radius
        if self.ypos - self.radius <= 0:
            self.ypos = self.radius

        c = lambda: random.randint(0, 255)
        self.color = '#%02x%02x%02x' % (c(), c(), c())

        self.canvas = canvas

        self.x = screen_width
        self.y = screen_height  # 老师这个命名方式非常不好,容易引起误会, 以后得注意

    def create_ball(self):

        x1 = self.xpos - self.radius
        y1 = self.ypos - self.radius

        x2 = self.xpos + self.radius
        y2 = self.ypos + self.radius

        self.item = self.canvas.create_oval(x1, y1, x2, y2,
                                            fill=self.color,
                                            outline=self.color)

    def move_ball(self):

        self.xpos += self.xvelocity
        self.ypos += self.yvelocity

        if self.xpos > self.x - self.radius:
            self.xvelocity *= -1
        if self.xpos < 0 + self.radius:
            self.xvelocity *= -1
        if self.ypos > self.y - self.radius:
            self.yvelocity *= -1
        if self.ypos < 0 + self.radius:
            self.yvelocity *= -1

        self.canvas.move(self.item, self.xvelocity, self.yvelocity)


class ScreenSaver():
    # balls = list()

    def __init__(self):  # 实际上这个就是主程序, 可以当成__main__来看待
        self.num_balls = random.randint(8, 20)

        self.root = tkinter.Tk()

        self.root.overrideredirect(1)

        self.root.bind('<Motion>', self.myquit)

        self.root.bind('<Key>', self.myquit)

        w, h = self.root.winfo_screenwidth(), self.root.winfo_screenheight()

        self.canvas = tkinter.Canvas(self.root, width=w, height=h)
        self.canvas.pack()

        self.balls = []
        for i in range(self.num_balls):
            ball = RandomBall(self.canvas, w, h)
            ball.create_ball()
            self.balls.append(ball)

        loop_ = asyncio.get_event_loop()
        tasks = []
        for ball in self.balls:
            tasks.append(self.running_balls(ball))
        loop_.run_until_complete(asyncio.wait(tasks))
        loop_.close()

        # 跑到这里果然出了问题, 在主循环创建之前,程序就卡在await那里了, mainloop不执行了, 操蛋了, 咋整?
        # 放前面也白扯, 这俩循环互相掣肘, 只能运行一个, 有点像死锁.
        # 无论如何都要有mainloop()的, 那么想要实现异步, 恐怕只有修改它的源码了(重写方法), 因为他的源码内恐怕不会自带await或者yield等字样来支持异步.
        # 好家伙, 遇到不支持异步的模块怎么办来着? 好像是future转换啥的
        self.root.mainloop()

    async def running_balls(self, ball):
        while True:
            ball.move_ball()
            await asyncio.sleep(0.04)

    def myquit(self, event):
        # 此处只是利用了事件处理机制
        # 实际上并不关心事件的类型
        # 作业：
        # 次屏保程序扩展成，一旦捕获事件，则判断退出
        # 显示一个button，button上显示事件类型，点击button后屏保才退出
        self.root.destroy()


if __name__ == '__main__':
    ScreenSaver()