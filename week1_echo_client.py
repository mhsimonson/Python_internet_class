import socket 
import time
host = 'block115379-pwc.blueboxgrid.com' 
port = 50000 
size = 1024 
s = socket.socket(socket.AF_INET, 
                  socket.SOCK_STREAM) 
s.connect((host,port)) 
s.send('Hello, world') 
data = s.recv(size) 
##
s.send('telnet mail.blueboxgrid.com 25')
s.send('helo  block115379-pwc.blueboxgrid.com')
s.send('mail from:<yoda@force2.com>')
s.send('rcpt to:<markhsimonson@hotmail.com>')
s.send('data')
s.send('Subject: This is the subject.\r\n')
#       ')
s.send('quit')
##
s.close() 
print 'Received:', data

print time.time()
