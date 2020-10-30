import threading
import time

# 参数定义最多几个线程同时使用资源
semaphore = threading.Semaphore(3)


# 用法：
def func():
    if semaphore.acquire():
        print(threading.currentThread().getName() + ' get semaphore')
        time.sleep(3)
        semaphore.release()
        print(threading.currentThread().getName() + ' release semaphore')


for i in range(8):
    t1 = threading.Thread(target=func)
    t1.start()
