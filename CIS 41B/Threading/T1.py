# multiple threads
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
    
def threadList():
    
    for index in range(count):
        targ = (tnames[index])
        thread = threading.Thread(target=threadfunc,args=targ)
        print("inserting "+targ)
        threadlist.append(thread)    
        
    for index in range(count):    
        print("starting "+tnames[index])
        threadlist[index].start()        
        
    for index in range(count):
        print("joining "+tnames[index])
        threadlist[index].join()
    
threadList()