from multiprocessing import Process, Manager

def func(dct, lst):
    dct[1] = '11'
    dct['2'] = 22
    dct[3.0] = 0.33
    lst.reverse()

if __name__ == '__main__':
    
    print('non-mp',10*'-')
    with Manager() as manager:
        dct = {}
        ml = [*range(1,11)]
        p = Process(target=func, args=(dct, ml))
        p.start()
        p.join()
        print(dct)
        print(ml)    
    
    print('mp',10*'-')
    with Manager() as manager:
        dct = manager.dict()
        ml = manager.list(range(10))
        p = Process(target=func, args=(dct, ml))
        p.start()
        p.join()
        print(dct)
        print(ml)
        
        print("Exiting main",10*'-')