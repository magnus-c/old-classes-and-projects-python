# using conditional threading
"""Class that implements a condition variable.

A condition variable allows one or more threads to wait until they are
notified by another thread.

If the lock argument is given and not None, it must be a Lock or RLock
object, and it is used as the underlying lock. Otherwise, a new RLock object
is created and used as the underlying lock.

Note:  RLock is a reentrant lock

"""
import _thread as thread, time
import queue
import threading
import random

cookiejar = queue.Queue()
condition = threading.Condition()
homerlist = []
margelist = []
cookie = 0

class ConsumerThread(threading.Thread):
    def run(self):
        global cookiejar
        condition.acquire()
        print("<<Homer lock acquired>>")
        if not cookiejar.empty():
            chip = cookiejar.get()
            print("Homer consumed", chip)
        else:
            condition.wait()
        condition.release()
        print(">>Homerlock released<<")
        time.sleep(0.1)
            
class ProducerThread(threading.Thread):
    def run(self):
        global cookie
        global cookiejar
        condition.acquire()
        print("<<marge lock acquired>>")
        if cookiejar.empty():
            cookie += 1
            cookiejar.put(cookie)
            print("Marge", cookie)
            print(">>Marge lock released<<")
            time.sleep(0.1)
        condition.notify()
        condition.release()        

nruns = 10
for pc in range(nruns):            
    homerlist.append(ProducerThread())
    margelist.append(ConsumerThread())
    
for pc in range(nruns):            
    homerlist[pc].start()
    margelist[pc].start()
    
for pc in range(nruns):            
    homerlist[pc].join()
    margelist[pc].join()    