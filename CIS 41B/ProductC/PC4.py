#using semiphore
"""
Semaphores manage a counter representing the number of release() calls minus
the number of acquire() calls, plus an initial value. The acquire() method
blocks if necessary until it can return without making the counter
negative. If not given, value defaults to 1.

"""
import sys
import random
import time
from threading import *

class Producer(Thread):
    def __init__(self, *tup):
        Thread.__init__(self)
        self.name = 'marge'
        self.items = tup[0]
        self.limit = tup[1]
        self.produce = tup[2]
        self.consume = tup[3]
    def produce_item(self):
        self.items.append(1)
        print("${}{}: >>> produced".format(self.name,self.produce._value))
    def wait(self):
        time.sleep(random.uniform(0, 3))
    def run(self):
        count = 0
        while count < self.limit:
            self.wait()
            self.produce.acquire()
            self.produce_item()
            self.consume.release()	
            count += 1

class Consumer(Thread):
    def __init__(self, *tup):
        Thread.__init__(self)
        self.name = 'homer'
        self.items = tup[0]
        self.limit = tup[1]
        self.produce = tup[2]
        self.consume = tup[3]
    def consume_item(self):
        item = self.items.pop()
        print("@{}{}: <<< consumed".format(self.name,self.consume._value))
    def wait(self):
        time.sleep(random.uniform(0, 3))
    def run(self):
        count = 0
        while count < self.limit:
            self.wait()
            self.consume.acquire()
            self.consume_item()
            self.produce.release()
            count += 1

def testSemaphore():
    _producers = 1
    _consumers = 1
    _length = 10

    items = []
    producers = []
    consumers = []
    
    Sproduce = Semaphore(_length)
    Sconsume = Semaphore(0)
    tup = (items, _length, Sproduce, Sconsume)

    for i in range(_producers):
        producers.append(Producer(*tup))
        producers[-1].start()

    for i in range(_consumers):
        consumers.append(Consumer(*tup))
        consumers[-1].start()

    for p in producers:
        p.join()

    for c in consumers:
        c.join()
        
testSemaphore()