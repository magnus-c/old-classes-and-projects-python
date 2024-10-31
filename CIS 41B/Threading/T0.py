# start threads by passing function to Thread constructor
from pprint import pprint
import threading
import time

def threadfunc(*t):
    print(">>>>",*t)
    time.sleep(1)
    print('[',*t,']')
    time.sleep(2)
    print("<<<<",*t)

arg1 = ("AAAAAAAA")
threadA = threading.Thread(target=threadfunc,args=arg1)
threadA.start() 

arg2 = ("BBBBBBBB")
threadB = threading.Thread(target=threadfunc,args=arg2)
threadB.start() 

arg3 = ("CCCCCCCC")
threadC = threading.Thread(target=threadfunc,args=arg3)
threadC.start() 

threadA.join()
threadB.join()
threadC.join()
