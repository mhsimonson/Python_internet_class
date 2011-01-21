import socket
import sys

s=socket.socket(socket.AF_NET, socket.SOCK_STREAM)

host=sys.argv[1]
port=int(sys.argv[2])
s.connect((host,port))

s.send(sys.argv[3])

i=0
while(1):
    data = s.recv(1000000)
    i +=1
    if (i<5):
        print data
    if not data:
        break
    print 'received', len(data), 'bytes'

s.close()
