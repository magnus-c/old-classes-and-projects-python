from pprint import pprint
import threading
import time
import queue 
q = queue.Queue()

def thread_function(name):
    print("Thread %s: starting" % name)
    time.sleep(2)
    print("Thread %s: finishing" % name)

arg1 = ("TEST1",)
threadA = threading.Thread(target=thread_function,args=arg1)
arg2 = ("TEST2",)
threadB = threading.Thread(target=thread_function,args=arg2)
arg3 = ("TEST3",)
threadC = threading.Thread(target=thread_function,args=arg3)

q.put(threadA)
q.put(threadB)
q.put(threadC)

threadA.start() 
threadB.start() 
threadC.start() 


for i in q.queue:
    print(i)

