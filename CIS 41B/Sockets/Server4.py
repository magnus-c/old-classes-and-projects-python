# transmitting a picture
import socket                   # Import socket module

def server(portnumber):
    port = portnumber                    # Reserve a port for your service every new transfer wants a new port or you must wait.
    s = socket.socket()             # Create a socket object
    host = socket.gethostname()   # Get local machine name
    s.bind((host, port))            # Bind to the port
    s.listen(5)                     # Now wait for client connection.
    
    print('Server listening....')
    
    while True:
        conn, addr = s.accept()     # Establish connection with client.
        print('Got connection from', addr)
        data = conn.recv(1024)
        print('Server received', repr(data))
    
        filename='dog.jpg' #In the same folder or path is this file running must the file you want to tranfser to be
        f = open(filename,'rb')
        l = f.read(1024)
        while (l):
            conn.send(l)
            print('Sent ',repr(l))
            l = f.read(1024)
        f.close()
    
        print('Done sending')
        conn.close()
        
server(5000)