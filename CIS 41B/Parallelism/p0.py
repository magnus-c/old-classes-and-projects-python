from multiprocessing import Process
import threading
import time
import datetime 
import pendulum as dt

def display(val):
    print ("display ",val)
    
def paralleltest():
    p1 = Process(target=display,args=(1,))
    p2 = Process(target=display,args=(2,))
    p3 = Process(target=display,args=(3,))
    p1.start()
    p2.start()   
    p3.start()
    p1.join()
    p2.join()
    p3.join()

def threadingtest():
    threadA = threading.Thread(target=display,args=(11,))
    threadB = threading.Thread(target=display,args=(22,))
    threadC = threading.Thread(target=display,args=(33,))
    threadA.start() 
    threadB.start() 
    threadC.start()
    threadA.join()
    threadB.join()
    threadC.join()
    
if __name__ == '__main__':
    start = dt.now()
    paralleltest()
    stop = dt.now()
    duration = dt.period(start,stop)
    print("Parallel = ",duration.microseconds)
    
    start = dt.now()
    threadingtest()
    stop = dt.now()
    duration = dt.period(start,stop)
    print("Thread = ",duration.microseconds)