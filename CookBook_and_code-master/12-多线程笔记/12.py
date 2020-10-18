import threading

sum = 0
loop_sum = 1000000

lock = threading.Lock()


def my_add():
    global sum, loop_sum
    for i in range(loop_sum):
        lock.acquire()
        sum += 1
        lock.release()


def my_minus():
    global sum, loop_sum
    for i in range(loop_sum):
        lock.acquire()
        sum -= 1
        lock.release()


if __name__ == '__main__':
    t1 = threading.Thread(target=my_add(), args=())
    t2 = threading.Thread(target=my_minus(), args=())
    t1.start()
    t2.start()
    t1.join()
    t2.join()

    print("It's done with number {0}".format(sum))
