import xmlrpclib
import time

s = xmlrpclib.ServerProxy('http://localhost:8000')

print s.echo('hello')
print s.echo('world')

def time_foo()



