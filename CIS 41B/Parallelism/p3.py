from multiprocessing import Process, Pipe

def pipefunction(conn,txt):
    conn.send([txt])
    conn.close()
    
if __name__ == '__main__':
    parent, child = Pipe()
    
    p = Process(target=pipefunction, args=(child,'send parent from child'))
    p.start()
    print ( 'parent received: ',parent.recv() )  
    p.join()    
    
    c = Process(target=pipefunction, args=(parent,'send child from parent'))
    c.start()
    c.join()
    print ( 'child received: ',child.recv() )  
    p.join()
    
    print("Exiting main")