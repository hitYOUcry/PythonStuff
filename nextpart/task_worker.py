import random, time, queue
from multiprocessing.managers import BaseManager

class QueueManager(BaseManager):
    pass

QueueManager.register("get_task_queue")
QueueManager.register("get_result_queue")

server_addr = '127.0.0.1'
print('Connect to server %s...' % server_addr)
manager = QueueManager(address=('127.0.0.1', 2314), authkey=b'abc')

manager.connect()

taskQ = manager.get_task_queue()
resultQ =  manager.get_result_queue()


for i in range(10):
    try:
        n = taskQ.get(timeout=1)
        print('run task %d * %d...' % (n, n))
        r = '%d * %d = %d' % (n, n, n*n)
        time.sleep(1)
        resultQ.put(r)
    except queue.Queue.Empty:
        print('task queue is empty.')
    
print('worker exit!')