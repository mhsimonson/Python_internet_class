import cherrypy
import datetime
import wsgiref.util


class CurrentTime(object):
    def index(self):
        #return "placeholder, some day this will show you the time" #datetime.datetime.now() - structure returns a TypeError: object is not iterable - does not return a number that can be returned?
        return [str(datetime.datetime.now())] # - doesn't work, because not being RETURNED - diff between return and print.
    index.exposed = True
    
class WTF(object):
    self.environ=environ
    def index(self):
        return [str(wsgiref.util.request_uri(self))]
    index.exposed = True    
    
class HelloWorld(object):
    currenttime=CurrentTime()    # needs to be in whatever class gets "mounted" in the quickstart statement below
    wtf=WTF()    
    def index(self):
        return "Hello World - You Suck"
    index.exposed = True
      

    
    
cherrypy.quickstart(HelloWorld())
root.currenttime=currenttime
root.wtf=wtf