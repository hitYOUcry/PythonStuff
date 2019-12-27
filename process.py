from multiprocessing import Process, Queue

import os, time, random

def run_proc(name):
    print("Run child process name:%s, pid:%s" % (name, os.getpid()))

def write(q):
    print('WRITE process pid: %s' % os.getpid())
    for value in ['E', 'N', 'C']:
        print('Put %s into queue.' % value)
        q.put(value)
        time.sleep(random.random())

def read(q):
    print('READ process pid: %s' % os.getpid())
    while(True):
        value = q.get(True)
        print('Get %s from queue.' % value)

if __name__ == "__main__":
    queue = Queue()
    writeProcess = Process(target=write, args=[queue])
    readProcess = Process(target=read, args=[queue])
    writeProcess.start()
    readProcess.start()
    writeProcess.join()
    readProcess.terminate()


