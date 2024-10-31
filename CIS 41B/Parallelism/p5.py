from multiprocessing import Process, Lock

def displayNoLock(n):
    for i in range(1,n):
        print ("index: "+str(i))  
    print(10*'*')

def displayLock(lck, n):
    lck.acquire()
    print("lock acquire")
    for i in range(1,n):
        print ("index: "+str(i))
    lck.release()
    print("lock release")
    print(10*'*')
    
if __name__ == '__main__':
    
    numbers = [*range(11)]
    for n in numbers:
        p = Process(target=displayNoLock, args=(n,))
        p.start()
        p.join()
        
    lock = Lock()
    numbers = [*range(11)]
    for n in numbers:
        p = Process(target=displayLock, args=(lock,n,))
        p.start()
        p.join()
    
    print("Exiting main")