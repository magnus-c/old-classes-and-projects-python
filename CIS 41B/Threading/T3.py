# Locks
import threading
import time

tnames = ('AAAAAAAA','BBBBBBBB','CCCCCCCC')
count = len(tnames)
threadlist = []
count = 3

def threadfunc(*t):
    print(">>>>",*t)
    time.sleep(1)
    print('[',*t,']')
    time.sleep(2)
    print("<<<<",*t)

class TimeThread (threading.Thread):
    def __init__(self, threadID, name):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
    def run(self):
        print("Starting " + self.name)
        threadLock.acquire()
        threadfunc(self.name)
        threadLock.release()
        print("Exiting " + self.name)

# Create new threads
threadLock = threading.Lock()
threadlist = [] 
for index in range(count):
    print("inserting "+tnames[index])
    threadlist.insert(index,TimeThread(index+1, tnames[index]))

# Start new Threads
for index in range(count):
    print("starting "+tnames[index])
    threadlist[index].start()

# Join Threads
for index in range(count):
    print("joining "+tnames[index])
    threadlist[index].join()

print("Exiting Main Thread")