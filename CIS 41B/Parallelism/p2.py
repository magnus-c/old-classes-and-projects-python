from multiprocessing import Process

numbers = [*range(10)]

def cube():
    for x in numbers:
        print('%s cube  is  %s' % (x, x**3))
        
def evenno():
    for x in numbers:
        if x % 2 == 0:
            print('%s is an even number ' % (x))
            
if __name__ == '__main__':
    process1 = Process(target=cube)
    process2 = Process(target=evenno)
    process1.start()
    process2.start()
    process1.join()
    process2.join()
    print("Exiting main")