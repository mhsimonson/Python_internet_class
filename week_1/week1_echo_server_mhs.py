import socket
import time
# Yea, I be dumb
host = 'block115399-f9p.blueboxgrid.com' ## My host name
port = 50000 
backlog = 5 
size = 1024 
s = socket.socket(socket.AF_INET,
                  socket.SOCK_STREAM) 
s.bind((host,port)) 
s.listen(backlog) 
while True: 
    client, address = s.accept()
    # data = client.recv(size)
    data = time.time()
    if data: 
        client.send(data)
        
    client.close()

