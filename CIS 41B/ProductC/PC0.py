#basic threads
import _thread as thread, queue, time

cookiejar = queue.Queue()
nruns = 10

def marge(cookie):
    print("<marge> >>> cookie",cookie)
    cookiejar.put("{cookie} "+str(cookie))
    time.sleep(1.0)

def homer(cookie):
    print('[homer] <<< ', cookie)
    cookie = cookiejar.get()
    time.sleep(0.1)

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