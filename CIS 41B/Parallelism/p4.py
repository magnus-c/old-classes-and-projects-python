import multiprocessing
import pickle
import queue

numbers = [*range(11)]

def even(n, q):
    return [q.put(n) for n in numbers if n % 2 == 0]
            
if __name__ == "__main__":
    try:
        # standard queue
        que = queue.Queue()    
        p = multiprocessing.Process(target=even, args=(numbers, que))
        p.start()
        p.join()
        while que.empty() is  False:
            print(que.get())
    except:
        print('Error handling queue')
    
    # multiprocessing queue
    queQ = multiprocessing.Queue()
    p = multiprocessing.Process(target=even, args=(numbers, queQ))
    p.start()
    p.join()
    while queQ.empty() is  False:
        print(queQ.get())
        
    print("Exiting main")