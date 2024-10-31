# queue lock
import queue
import threading
import time

exitFlag = False
threadList = ["AAAAAAAA", "BBBBBBBB", "CCCCCCCC"]
nameList = ["Alpha", "Beta", "Gamma"]
queueLock = threading.Lock()
workQueue = queue.Queue(3)
threads = []

def threadfunc(threadName, q):
    print('>>>>'+threadName)
    time.sleep(1)
    while not exitFlag:
        if not workQueue.empty():
            queueLock.acquire()
            data = q.get()
            print('[',*data,']')
            queueLock.release()
        time.sleep(2)
    print('<<<<'+threadName)
class TimeThread (threading.Thread):
    def __init__(self, name, q):
        threading.Thread.__init__(self)
        self.name = name
        self.q = q
    def run(self):
        print("Starting " + self.name)
        threadfunc(self.name, self.q)
        print("Exiting " + self.name)

# Create new threads
for tName in threadList:
    thread = TimeThread(tName, workQueue)
    threads.append(thread)
    thread.start()

# Fill the queue
queueLock.acquire()
for word in nameList:
    print("inserting word "+word+" into queue")
    workQueue.put(word)
queueLock.release()

# Wait for queue to empty
while not workQueue.empty():
    pass

# Notify threads it's time to exit
exitFlag = True

# Wait for all threads to complete
for thread in threads:
    thread.join()
    
print("Exiting Main Thread")