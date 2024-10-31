# transmit a picture
import socket                   # Import socket module

def client(portnumber):
    s = socket.socket()             # Create a socket object
    host = socket.gethostname()  #Ip address that the TCPServer  is there
    port = portnumber                     # Reserve a port for your service every new transfer wants a new port or you must wait.
    
    s.connect((host, port))
    s.send(b"Hello server!")
    
    with open('dogcopy.jpg', 'wb') as f:
        print ('file opened')
        while True:
            print('receiving data...')
            data = s.recv(1024)
            print('data=',data)
            if not data:
                break
            # write data to a file
            print(data)
            f.write(data)
    
    f.close()
    print('Successfully got the file')
    s.close()
    print('connection closed')
    
client(5000)