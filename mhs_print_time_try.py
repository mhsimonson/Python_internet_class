import time
import datetime


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.bind(("localhost", 8080))
s.listen(5)





    
if __name__ == '__main__':
   x=time.time()
   print x 
#print "Here is the time: %s" % time.time()
#print "and again: %s" % datetime.datetime.now()


#create an INET, STREAMing socket
s = socket.socket(
    socket.AF_INET, socket.SOCK_STREAM)
#now connect to the web server on port 80
# - the normal http port
s.connect(("www.mcmillan-inc.com", 80))
