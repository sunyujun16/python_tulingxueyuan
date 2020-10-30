import threading
import time


sum = 0
loop_sum = 10

lock = threading.Lock()


def my_add():
    global sum, loop_sum
    for i in range(loop_sum):
        lock.acquire()
        sum += 1
        time.sleep(0.1)
        lock.release()


def my_minus():
    global sum, loop_sum
    for i in range(loop_sum):
        lock.acquire()
        sum -= 1
        time.sleep(0.1)
        lock.release()


if __name__ == '__main__':
    time_0 = time.time()
    t1 = threading.Thread(target=my_add(), args=())
    t2 = threading.Thread(target=my_minus(), args=())
    t1.start()
    t2.start()
    t1.join()
    t2.join()

    print('运行时间 ', time.time() - time_0)
    print("It's done with number {0}".format(sum))

# 这里加锁或者不加锁, 运行时间是一样的10秒.为什么呢?好像我把锁取消了之后, 它仍然存在呢
# 然后我又拿案例11试验了一下, 果然只有1秒, 即是说, 加锁的确会影响运行速度.
