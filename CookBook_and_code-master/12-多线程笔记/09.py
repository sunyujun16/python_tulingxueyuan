import threading
import time


# 1. 类需要继承自threading.Thread
class MyThread(threading.Thread):
    def __init__(self, arg):
        super(MyThread, self).__init__()
        self.arg = arg

    # 2 必须重写run函数，run函数代表的是真正执行的功能
    def run(self):
        time.sleep(2)
        print("The args for this class is {0}".format(self.arg))


for i in range(5):
    t = MyThread(i)
    t.start()  # 这里会默认以run函数创建一个线程
    t.join()

"""
这里如果不加t.join()会出现类似这样的输出, 其中除了第一行都几乎同时出现, 但先后顺序不一定
Main thread is done!!!!!!!!
The args for this class is 0
The args for this class is 2
The args for this class is 4
The args for this class is 3
The args for this class is 1
"""

print("Main thread is done!!!!!!!!")
