import random
import time
import queue
from multiprocessing.managers import BaseManager
import multiprocessing


task_queue = queue.Queue()
result_queue = queue.Queue()


class QueueManager(BaseManager):
    pass


def get_task_queue():
    return task_queue


def get_result_queue():
    return result_queue


QueueManager.register("get_task_queue", callable=get_task_queue)
QueueManager.register("get_result_queue", callable=get_result_queue)


if __name__ == '__main__':
    multiprocessing.freeze_support()
    manager = QueueManager(address=('127.0.0.1', 2314), authkey=b'abc')
    manager.start()

    taskQ = manager.get_task_queue()
    resultQ = manager.get_result_queue()

    for i in range(10):
        n = random.randint(0, 100000)
        print('Put task %d' % n)
        taskQ.put(n)

    print('Try get result')
    for i in range(10):
        r = resultQ.get(timeout=10)
        print('Result is :%s' % r)
    manager.shutdown()
    print('Master end!')
