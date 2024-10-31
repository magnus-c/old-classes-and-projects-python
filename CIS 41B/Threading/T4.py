# thread queue
import queue
import threading
import time

exitFlag = False

def threadfunc(threadName, que):
    print('>>>>'+threadName)
    time.sleep(1)
    while not exitFlag:
        if not workQueue.empty():
            data = que.get()
            print('[',*data,']')
        time.sleep(2)
    print('<<<<'+threadName)
class TimeThread (threading.Thread):
    def __init__(self, name, q):
        threading.Thread.__init__(self)
        self.name = name
        self.que = q
    def run(self):
        print("Starting " + self.name)
        threadfunc(self.name, self.que)
        print("Exiting " + self.name)

threadList = ["AAAAAAAA", "BBBBBBBB", "CCCCCCCC"]
nameList = ["Alpha", "Beta", "Gamma"]
workQueue = queue.Queue(len(nameList))
threads = []

# Create new threads
for tName in threadList:
    thread = TimeThread(tName, workQueue)
    thread.start()
    threads.append(thread)

# Fill the queue
for word in nameList:
    print("inserting word "+word+" into queue")
    workQueue.put(word)

# Wait for queue to empty
while not workQueue.empty():
    pass

# Notify threads it's time to exit
exitFlag = True

# Wait for all threads to complete
for thread in threads:
    thread.join()
    
print("Exiting Main Thread")