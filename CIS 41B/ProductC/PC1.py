# using thread locks
'''
A lock ensures the mutual exclusion. By exclusion, it is meant 
that at a time only one thread is allowed to execute the block 
of a statement.  The lock for the duration of intended statements 
is acquired and is released when the control flow exits the 
indented block. Thread scheduling is inherently nondeterministic.
'''

import _thread as thread, queue, time
import threading

tlock = threading.Lock()
cookiejar = queue.Queue()
nruns = 10

def marge(cookie):
        tlock.acquire_lock()
        print("<marge> >>> cookie",cookie)
        cookiejar.put("{cookie} "+str(cookie))
        tlock.release()

def homer(cookie):
        tlock.acquire_lock()
        print('[homer] <<< ', cookie)
        cookie = cookiejar.get()
        tlock.release()

def _Threading():
        for i in range(nruns):
                thread.start_new_thread(marge, (i,))   
                thread.start_new_thread(homer, (i,))

def _NonThreading():
        for i in range(nruns):
                marge(i)  
                homer(i)  

def threadingtest():
        print('\nNonThreading ----------')
        _NonThreading()
        print('\nThreading ---------')
        _Threading()
        print('\nMain thread exit')

threadingtest()