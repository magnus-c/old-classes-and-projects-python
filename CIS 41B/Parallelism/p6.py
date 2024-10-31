from multiprocessing import Pool
import time

work = (["A", 5], ["B", 2], ["C", 1], ["D", 3])

def do_work(data):
    print(" Process %s waiting %s seconds" % (data[0], data[1]))
    time.sleep(int(data[1]))
    print(" Process %s Finished." % data[0])

def pool_handler():
    p = Pool(2)
    p.map(do_work, work)

if __name__ == '__main__':
    pool_handler()