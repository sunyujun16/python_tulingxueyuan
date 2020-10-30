import threading
import time


def t_1():
    global a
    while True:
        a = 1
        print(a)
        time.sleep(1)


def t_2():
    global a
    while True:
        a = 2
        print(a)
        time.sleep(1)


t1 = threading.Thread(target=t_1())
t1.start()
t1.setDaemon(True)


t2 = threading.Thread(target=t_2())
t2.start()
t2.setDaemon(True)


while True:
    a = 0
    print(a)
    time.sleep(1)


