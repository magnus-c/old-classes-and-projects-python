from multiprocessing import Process
import threading
import pendulum as dt

numbers = [*range(10)]

def cube():
    for x in numbers:
        print('%s cube  is  %s' % (x, x**3))
        
def square():
    for x in numbers:
        print('%s square  is  %s' % (x, x**2))
        
def paralleltest():
    p1 = Process(target=cube)
    p2 = Process(target=square)
    p1.start()
    p2.start()
    p1.join()
    p2.join()

def threadingtest():
    threadA = threading.Thread(target=cube)
    threadB = threading.Thread(target=square)
    threadA.start() 
    threadB.start() 
    threadA.join()
    threadB.join()
    
if __name__ == '__main__':
    start = dt.now()
    paralleltest()
    stop = dt.now()
    duration = dt.period(start,stop)
    print("Parallel = ",duration.microseconds)
    '''
    start = dt.now()
    threadingtest()
    stop = dt.now()
    duration = dt.period(start,stop)
    print("Thread = ",duration.microseconds)
    '''