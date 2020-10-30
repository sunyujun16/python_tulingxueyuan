import threading
import time

sum = 0
loopSum = 10

lock = threading.Lock()


def myAdd():
    global sum, loopSum
    for i in range(1, loopSum):
        sum += 1
        time.sleep(0.1)


def myMinu():
    global sum, loopSum
    for i in range(1, loopSum):
        sum -= 1
        time.sleep(0.1)


if __name__ == '__main__':

    print("Starting ....{0}".format(sum))
    time_0 = time.time()
    # 开始多线程的实例，看执行结果是否一样
    t1 = threading.Thread(target=myAdd, args=())
    t2 = threading.Thread(target=myMinu, args=())

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    print('运行时间 ', time.time() - time_0)
    print("Done .... {0}".format(sum))
